# Changelog

## 2026.11.0b2

### Opgelost
- `WASTE_TYPE_MAP` aangevuld met kleurcodes (`GREY`, `GREEN`, `PACKAGES`) die de Ximmio API retourneert — verpakkingen werd daardoor niet herkend
- `manifest.json` opgeslagen zonder UTF-8 BOM waardoor HA de integratie niet kon laden

### Gewijzigd
- Afvaltype "Plastic/Pakketjes" hernoemd naar "Verpakkingen" in `const.py`, `afvalwijzer_card.yaml` en `README.md`
- `afvalwijzer_card.yaml`: sensor-namen gecorrigeerd naar de juiste HA entity-IDs (`sensor.verpakkingen_ophaaldag` etc.)

---

## 2026.11.0b1

### Gewijzigd
- Integratie hernoemd van `twente_milieu` naar `ximmio_afvalwijzer` (domeinnaam, mapnaam, klassen)
- Leesbare naam gewijzigd van "Twente Milieu" naar "Ximmio Afvalwijzer"
- GitHub repository URL bijgewerkt naar `https://github.com/unclekoen/ha-ximmio-afvalwijzer`
- `manifest.json`: `documentation` en `issue_tracker` URLs gecorrigeerd, `codeowners` ingevuld
- `sensor.py`: `_attr_unique_id` gebruikt nu de `DOMAIN` constante in plaats van een hardcoded string
- README volledig herschreven: Marketplace installatie, ondersteunde gemeenten, verbeterde uitleg

---

## 2026.11.0b0

### Toegevoegd
- Custom component met config flow, coordinator en sensor platform
- Ximmio API integratie (`FetchAdress` + `GetCalendar`)
- Sensoren voor restafval, GFT, verpakkingen, papier en kerstboom
- Extra sensorattributen: `days_until` en `friendly_date`

---

## 2026.10.1a

### Gewijzigd
- Afbeeldingsgrootte gewijzigd van 48 naar 32 pixels in de dashboard card
- Afbeeldingen worden nu inline via base64-code aangeroepen in plaats van externe bestanden

---

## 2026.10.0a

### Toegevoegd
- Papier (school/vereniging) toegevoegd aan de dashboard card
- Gekleurde SVG icoontjes voor afvaltypes
- Eerste versie van de dashboard card met afvalcontainers
- Initial commit: projectstructuur en README
