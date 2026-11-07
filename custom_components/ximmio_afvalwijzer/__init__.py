"""Ximmio Afvalwijzer integratie voor Home Assistant."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform

from .const import DOMAIN, CONF_POSTAL_CODE, CONF_HOUSE_NUMBER, CONF_SUFFIX
from .coordinator import XimmioAfvalwijzerCoordinator

PLATFORMS = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Stel de integratie in vanuit een config entry."""
    coordinator = XimmioAfvalwijzerCoordinator(
        hass,
        postal_code=entry.data[CONF_POSTAL_CODE],
        house_number=entry.data[CONF_HOUSE_NUMBER],
        suffix=entry.data.get(CONF_SUFFIX, ""),
    )
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Verwijder een config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
