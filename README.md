# ha-afvalwijzer

Een simpele Home Assistant markdown card die toont welke container je de volgende keer aan de straat moet zetten. Geen extra HACS installaties nodig.

## Werking

De kaart leest de sensoren van de **Afvalwijzer** integratie (Twente Milieu) en toont de eerstvolgende ophaling als een gekleurd icoontje met tekst. Papier wordt lokaal door een school opgehaald op de 3e woensdag van de maand — dat berekent de kaart zelf, zonder sensor.

### Wat je ziet

- Een gekleurd container-icoontje met darachter: `Vandaag`, `Morgen` of `Over X dagen` + naam
- Een tweede regel met een bruin doosje voor papier, maar alleen als de ophaling binnen 7 dagen is

## Vereisten

### 1. Afvalwijzer integratie

Installeer de [Afvalwijzer](https://github.com/xirixiz/homeassistant-afvalwijzer) integratie via HACS en stel je afvaldienst in. Dit levert de volgende sensoren op:

| Sensor | Omschrijving |
|--------|-------------|
| `sensor.non_recyclable_waste_pickup` | Restafval |
| `sensor.organic_waste_pickup` | GFT |
| `sensor.packages_waste_pickup` | Plastic/Pakketjes |

> Controleer de exacte sensornamen via **Instellingen → Apparaten & Diensten → Entiteiten**.

### 2. SVG icoontjes

Kopieer de bestanden uit de map `images/` naar `/config/www/afvalwijzer/` op je Home Assistant server.

| Bestand | Kleur | Type |
|---------|-------|------|
| `restafval.svg` | Grijs | Container |
| `gft.svg` | Groen | Container |
| `plastic.svg` | Oranje | Container |
| `papier.svg` | Bruin | Doosje |

De makkelijkste manier om bestanden te uploaden is via de **Studio Code Server** add-on.

Na het uploaden zijn de bestanden bereikbaar via `/local/afvalwijzer/restafval.svg` etc.

## Installatie

1. Ga in je dashboard naar **Bewerken → Kaart toevoegen → Handmatige kaart**
2. Plak de inhoud van `afvalwijzer_card.yaml`
3. Sla op

## Papier (school)

Papier wordt niet door Twente Milieu beheerd maar door een lokale school opgehaald, elke **3e woensdag van de maand**. De kaart berekent deze datum automatisch. De papierregel verschijnt alleen als de ophaling binnen 7 dagen is.

## Voorbeeld

```
🗑️ [container]  Over 2 dagen: Restafval
📦 [doosje]     Over 5 dagen: Papier (school)
```
