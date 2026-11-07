# ha-ximmio-afvalwijzer

Twee onderdelen voor Home Assistant om afvalophalingen via de Ximmio API te tonen:

1. **`custom_components/ximmio_afvalwijzer/`** — een eigen HA integratie die rechtstreeks de ximmio API aanroept, zonder afhankelijkheid van Afvalwijzer
2. **`afvalwijzer_card.yaml`** — een markdown card die de sensoren van de integratie toont met gekleurde icoontjes

---

## 1. Integratie installeren

### Via HACS (aanbevolen)
1. Ga in HACS naar **Integraties → ⋮ → Aangepaste repositories**
2. Voeg toe: `https://github.com/unclekoen/ha-ximmio-afvalwijzer` als type **Integratie**
3. Zoek op "Ximmio Afvalwijzer" en installeer
4. Herstart Home Assistant

### Handmatig
1. Kopieer de map `custom_components/ximmio_afvalwijzer/` naar `/config/custom_components/ximmio_afvalwijzer/` op je HA server
2. Herstart Home Assistant

### Configureren
1. Ga naar **Instellingen → Apparaten & Diensten → Integratie toevoegen**
2. Zoek op **Ximmio Afvalwijzer**
3. Vul in:
   - **Postcode** (bijv. `7500AA`)
   - **Huisnummer** (bijv. `10`)
   - **Toevoeging** (optioneel, bijv. `A`)

### Sensoren
Na installatie worden automatisch deze sensoren aangemaakt:

| Sensor | Omschrijving |
|--------|-------------|
| `sensor.restafval_ophaaldag` | Volgende restafval datum |
| `sensor.gft_ophaaldag` | Volgende GFT datum |
| `sensor.plastic_pakketjes_ophaaldag` | Volgende plastic/pakketjes datum |
| `sensor.papier_ophaaldag` | Volgende papier datum |
| `sensor.kerstboom_ophaaldag` | Volgende kerstboom datum |

Elke sensor heeft ook extra attributen: `days_until` en `friendly_date`.

---

## 2. Dashboard card

De card toont de eerstvolgende ophaling als gekleurd icoontje. Papier (school) wordt berekend op basis van de 3e woensdag van de maand — geen sensor nodig.

### SVG icoontjes (optioneel)
De card kan ook zonder de SVG bestanden werken als je base64 gebruikt (standaard). Wil je de bestanden toch apart hosten:

1. Kopieer de bestanden uit `images/` naar `/config/www/afvalwijzer/`
2. Pas de `img src` paden aan in de YAML naar `/local/afvalwijzer/...`

### Card installeren
1. Ga in je dashboard naar **Bewerken → Kaart toevoegen → Handmatige kaart**
2. Plak de inhoud van `afvalwijzer_card.yaml`
3. Sla op

---

## Papier (school)

Papier wordt in sommige wijken niet door de gemeente opgehaald maar door een lokale school, elke **3e woensdag van de maand**. De card berekent deze datum automatisch. De papierregel verschijnt alleen als de ophaling binnen 7 dagen is.

---

## Technische details

- De integratie roept de **ximmio API** aan (`wasteapi.ximmio.com`)
- Company code: `8d97bb56-5afd-4cbc-a651-b4f7314264b4`
- Data wordt elke 8 uur ververst
- Postcode en huisnummer worden opgeslagen in de HA config entry — niet in de repository
