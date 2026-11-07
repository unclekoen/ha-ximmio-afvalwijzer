"""Constanten voor Ximmio Afvalwijzer integratie."""

DOMAIN = "ximmio_afvalwijzer"

# Ximmio API
XIMMIO_API_URL = "https://wasteapi.ximmio.com"
XIMMIO_COMPANY_CODE = "8d97bb56-5afd-4cbc-a651-b4f7314264b4"

# Config entry keys
CONF_POSTAL_CODE = "postal_code"
CONF_HOUSE_NUMBER = "house_number"
CONF_SUFFIX = "suffix"

# Update interval in minuten
UPDATE_INTERVAL = 480

# Sensor namen
WASTE_TYPES = {
    "non_recyclable": "Restafval",
    "organic": "GFT",
    "packages": "Plastic/Pakketjes",
    "paper": "Papier",
    "christmas_tree": "Kerstboom",
}

# Mapping van ximmio _pickupTypeText naar interne sleutels
WASTE_TYPE_MAP = {
    "restafval": "non_recyclable",
    "gft": "organic",
    "groente": "organic",
    "groente, fruit en tuinafval": "organic",
    "pmd": "packages",
    "plastic": "packages",
    "verpakkingen": "packages",
    "papier": "paper",
    "oud papier": "paper",
    "kerstboom": "christmas_tree",
    "kerstbomen": "christmas_tree",
}
