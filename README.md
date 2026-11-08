# ha-ximmio-afvalwijzer

Een custom Home Assistant integratie voor het ophalen van afvalkalendergegevens via de Ximmio API, aangevuld met een kant-en-klare dashboard card.

Oorspronkelijk gemaakt voor persoonlijk gebruik als vereenvoudigd alternatief voor de uitgebreide [homeassistant-afvalwijzer](https://github.com/xirixiz/homeassistant-afvalwijzer) integratie. Omdat de Ximmio API door meerdere gemeenten in Nederland wordt gebruikt, werkt deze integratie voor al die gemeenten — zie de lijst hieronder.

---

## Ondersteunde gemeenten

De Ximmio API wordt gebruikt door de volgende afvalinzamelaars en gemeenten:

| Gemeente / Organisatie |
|---|
| ACV Groep |
| Gemeente Almere |
| Area Afval |
| Avalex |
| Avri |
| BAR Afvalbeheer |
| Gemeente Hellendoorn |
| Meerlanden |
| Gemeente Meppel |
| Mijn Blink |
| RAD BV |
| Twente Milieu |
| Waardlanden |
| Gemeente Westland |
| Gemeente Venlo |
| Woerden / Oudewater |

> Staat jouw gemeente er niet tussen? De company code is te achterhalen via de Ximmio API. Zie de technische details onderaan.

---

## Wat doet deze integratie?

- Haalt de eerstvolgende ophaaldatum op per afvaltype via `wasteapi.ximmio.com`
- Maakt automatisch sensoren aan voor restafval, GFT, plastic/pakketjes, papier en kerstboom
- Elke sensor bevat ook `days_until` (dagen tot ophaling) en `friendly_date` (leesbare datum)
- Data wordt elke 8 uur ververst

---

## Installatie via Marketplace

1. Ga in Home Assistant naar **Instellingen → Marketplace**
2. Zoek op **Ximmio Afvalwijzer** en installeer
3. Herstart Home Assistant

---

## Configureren

1. Ga naar **Instellingen → Apparaten & Diensten → Integratie toevoegen**
2. Zoek op **Ximmio Afvalwijzer**
3. Vul in:
   - **Postcode** (bijv. `7500AA`)
   - **Huisnummer** (bijv. `10`)
   - **Toevoeging** (optioneel, bijv. `A`)

---

## Sensoren

Na installatie worden automatisch deze sensoren aangemaakt:

| Sensor | Omschrijving |
|--------|-------------|
| `sensor.restafval_ophaaldag` | Volgende restafval datum |
| `sensor.gft_ophaaldag` | Volgende GFT datum |
| `sensor.verpakkingen_ophaaldag` | Volgende verpakkingen datum |
| `sensor.papier_ophaaldag` | Volgende papier datum |
| `sensor.kerstboom_ophaaldag` | Volgende kerstboom datum |

---

## Dashboard card

De card toont de eerstvolgende ophaling als gekleurd icoontje.

### Card installeren
1. Ga in je dashboard naar **Bewerken → Kaart toevoegen → Handmatige kaart**
2. Plak de inhoud van `afvalwijzer_card.yaml`
3. Sla op

### SVG icoontjes (optioneel)
De card gebruikt standaard base64-encoded icoontjes en werkt zonder extra bestanden. Wil je de SVG-bestanden apart hosten:

1. Kopieer de bestanden uit `images/` naar `/config/www/afvalwijzer/`
2. Pas de `img src` paden aan in de YAML naar `/local/afvalwijzer/...`

---

## Papier via school of vereniging

In sommige wijken wordt papier niet door de gemeente opgehaald, maar door een lokale school of vereniging. Als voorbeeld: elke **3e woensdag van de maand**. De card berekent deze datum automatisch — er is geen sensor voor nodig. De papierregel verschijnt in de card alleen als de ophaling binnen 7 dagen is.

> Dit is een voorbeeld. Pas de dag en/of frequentie aan naar de situatie in jouw wijk.

---

## Technische details

- API: `https://wasteapi.ximmio.com`
- Company code voor Twente Milieu: `8d97bb56-5afd-4cbc-a651-b4f7314264b4`
- Andere company codes zijn op te vragen via een POST naar `/api/FetchAdress` met de juiste company code in de payload
- Postcode en huisnummer worden opgeslagen in de HA config entry — niet in de repository
