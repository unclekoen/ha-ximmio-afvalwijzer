"""Sensor platform voor Ximmio Afvalwijzer."""
from __future__ import annotations

import logging
from datetime import date

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, WASTE_TYPES
from .coordinator import XimmioAfvalwijzerCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Zet sensoren op vanuit een config entry."""
    coordinator: XimmioAfvalwijzerCoordinator = hass.data[DOMAIN][entry.entry_id]
    await coordinator.async_config_entry_first_refresh()
    entities = [
        XimmioAfvalwijzerSensor(coordinator, waste_key, label)
        for waste_key, label in WASTE_TYPES.items()
    ]
    async_add_entities(entities)


class XimmioAfvalwijzerSensor(CoordinatorEntity, SensorEntity):
    """Sensor voor een afvaltype van Ximmio Afvalwijzer."""

    def __init__(
        self,
        coordinator: XimmioAfvalwijzerCoordinator,
        waste_key: str,
        label: str,
    ) -> None:
        """Initialiseer de sensor."""
        super().__init__(coordinator)
        self._waste_key = waste_key
        self._label = label
        self._attr_name = f"{label} ophaaldag"
        self._attr_unique_id = f"{DOMAIN}_{waste_key}"
        self._attr_icon = "mdi:trash-can"

    @property
    def native_value(self) -> str | None:
        """Geef de volgende ophaaldatum terug als YYYY-MM-DD string."""
        return self.coordinator.data.get(self._waste_key)

    @property
    def extra_state_attributes(self) -> dict:
        """Extra attributen: dagen tot ophaling en vriendelijke datum."""
        raw = self.coordinator.data.get(self._waste_key)
        if not raw:
            return {}
        try:
            pickup_date = date.fromisoformat(raw)
            today = date.today()
            diff = (pickup_date - today).days
            return {
                "days_until": diff,
                "friendly_date": pickup_date.strftime("%d %B %Y"),
            }
        except ValueError:
            return {}
