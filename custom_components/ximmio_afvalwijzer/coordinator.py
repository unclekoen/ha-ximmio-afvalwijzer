"""DataUpdateCoordinator voor Ximmio Afvalwijzer."""

from __future__ import annotations

import logging
from datetime import timedelta, datetime

import requests
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    DOMAIN,
    XIMMIO_API_URL,
    XIMMIO_COMPANY_CODE,
    UPDATE_INTERVAL,
    WASTE_TYPE_MAP,
)

_LOGGER = logging.getLogger(__name__)

TIMEOUT = (5.0, 30.0)


class XimmioAfvalwijzerCoordinator(DataUpdateCoordinator):
    """Haalt ophaaldata op via de ximmio API."""

    def __init__(
        self,
        hass: HomeAssistant,
        postal_code: str,
        house_number: str,
        suffix: str,
    ) -> None:
        """Initialiseer de coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=UPDATE_INTERVAL),
        )
        self._postal_code = postal_code.upper().replace(" ", "")
        self._house_number = house_number
        self._suffix = suffix.strip().upper()
        self._unique_id: str | None = None
        self._community: str | None = None

    def _fetch_address(self) -> None:
        """Haal het unieke adres-ID op via de ximmio API."""
        payload = {
            "postCode": self._postal_code,
            "houseNumber": self._house_number,
            "companyCode": XIMMIO_COMPANY_CODE,
        }
        if self._suffix:
            payload["HouseLetter"] = self._suffix

        response = requests.post(
            f"{XIMMIO_API_URL}/api/FetchAdress",
            data=payload,
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()

        data_list = data.get("dataList") or data.get("datalist") or []
        if not data_list:
            raise UpdateFailed("Adres niet gevonden via Ximmio API")

        first = data_list[0]
        self._unique_id = first.get("UniqueId")
        self._community = first.get("Community", "")

        if not self._unique_id:
            raise UpdateFailed("Geen UniqueId ontvangen van Ximmio API")

    def _fetch_calendar(self) -> list[dict]:
        """Haal de ophaalkalender op."""
        now = datetime.now()
        end_date = (now.date() + timedelta(days=365)).strftime("%Y-%m-%d")

        payload = {
            "companyCode": XIMMIO_COMPANY_CODE,
            "uniqueAddressID": self._unique_id,
            "startDate": now.strftime("%Y-%m-%d"),
            "endDate": end_date,
            "community": self._community or "",
        }

        response = requests.post(
            f"{XIMMIO_API_URL}/api/GetCalendar",
            data=payload,
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()

        data_list = data.get("dataList") or data.get("datalist") or []
        results = []

        for item in data_list:
            if not isinstance(item, dict):
                continue
            pickup_dates = item.get("pickupDates") or []
            if not pickup_dates:
                continue

            raw_type = (item.get("_pickupTypeText") or "").strip().lower()
            waste_key = WASTE_TYPE_MAP.get(raw_type)
            if not waste_key:
                _LOGGER.debug("Onbekend afvaltype: %s", raw_type)
                continue

            for raw_date in pickup_dates:
                parsed = self._parse_date(raw_date)
                if parsed:
                    results.append({"type": waste_key, "date": parsed})

        return sorted(results, key=lambda x: x["date"])

    @staticmethod
    def _parse_date(value: str) -> str | None:
        """Converteer ximmio datumformaat naar yyyy-mm-dd."""
        if not value:
            return None
        for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
            try:
                return datetime.strptime(value, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
        try:
            return datetime.fromisoformat(value.replace("Z", "")).strftime("%Y-%m-%d")
        except ValueError:
            return None

    async def _async_update_data(self) -> dict[str, str]:
        """Update data — geeft dict terug met {waste_key: volgende_datum}."""
        try:
            if not self._unique_id:
                await self.hass.async_add_executor_job(self._fetch_address)

            all_pickups = await self.hass.async_add_executor_job(self._fetch_calendar)
        except requests.RequestException as err:
            raise UpdateFailed(f"API fout: {err}") from err

        today = datetime.now().date()
        next_dates: dict[str, str] = {}

        for pickup in all_pickups:
            waste_type = pickup["type"]
            pickup_date = datetime.strptime(pickup["date"], "%Y-%m-%d").date()
            if pickup_date >= today and waste_type not in next_dates:
                next_dates[waste_type] = pickup["date"]

        return next_dates