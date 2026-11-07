"""Config flow voor Ximmio Afvalwijzer."""
from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, CONF_POSTAL_CODE, CONF_HOUSE_NUMBER, CONF_SUFFIX

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_POSTAL_CODE): cv.string,
        vol.Required(CONF_HOUSE_NUMBER): cv.string,
        vol.Optional(CONF_SUFFIX, default=""): cv.string,
    }
)


class XimmioAfvalwijzerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow voor Ximmio Afvalwijzer."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Verwerk de gebruikersinput."""
        errors = {}

        if user_input is not None:
            postal_code = user_input[CONF_POSTAL_CODE].upper().replace(" ", "")
            house_number = user_input[CONF_HOUSE_NUMBER]

            await self.async_set_unique_id(f"{postal_code}_{house_number}")
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=f"Ximmio Afvalwijzer {postal_code} {house_number}",
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )
