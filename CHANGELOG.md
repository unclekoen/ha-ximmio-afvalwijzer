# Changelog

## 2026.11.07b-beta
_Release tag: `2026.11.0b1`_

### Gewijzigd
- Integratie hernoemd van `twente_milieu` naar `ximmio_afvalwijzer` (domeinnaam, mapnaam, klassen)
- Leesbare naam gewijzigd van "Twente Milieu" naar "Ximmio Afvalwijzer"
- GitHub repository URL bijgewerkt naar `https://github.com/unclekoen/ha-ximmio-afvalwijzer`
- `manifest.json`: `documentation` en `issue_tracker` URLs gecorrigeerd
- `sensor.py`: `_attr_unique_id` gebruikt nu de `DOMAIN` constante in plaats van een hardcoded string
- README volledig herschreven: Marketplace installatie, ondersteunde gemeenten, verbeterde uitleg

---

## 2026.11.07-beta
_Release tag: `2026.11.0b0`_

### Toegevoegd
- Custom component `twente_milieu` met config flow, coordinator en sensor platform
- Ximmio API integratie (`FetchAdress` + `GetCalendar`)
- Sensoren voor restafval, GFT, plastic/pakketjes, papier en kerstboom
- Extra sensorattributen: `days_until` en `friendly_date`

---

## 2026.10.26-alpha

### Gewijzigd
- Afbeeldingsgrootte gewijzigd van 48 naar 32 pixels in de dashboard card
- Afbeeldingen worden nu inline via base64-code aangeroepen in plaats van externe bestanden

---

## 2026.10.25-alpha

### Toegevoegd
- Papier (school/vereniging) toegevoegd aan de dashboard card
- Gekleurde SVG icoontjes voor afvaltypes
- Eerste versie van de dashboard card met afvalcontainers
- Initial commit: projectstructuur en README
