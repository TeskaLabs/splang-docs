---
title: Geografická souřadnice
---

# SP-Lang geopoint

Typ geopoint je složený datový typ navržený k efektivnímu ukládání a reprezentaci geografických souřadnic, konkrétně délky a šířky, v kompaktním binárním formátu. Kombinuje délku a šířku do jednoho 64bitového celého čísla, přičemž využívá kódování s pevnou desetinnou čárkou, aby zajistilo přesnost a efektivní ukládání. Typ geopoint poskytuje rovnováhu mezi přesností a efektivitou ukládání, což z něj činí ideální volbu pro moderní architektury CPU s 64 bity.

## Formát

<img src="../geopoint.drawio.png" alt="Schéma bitového uspořádání geopointu" />

Vyšších 32 bitů reprezentuje _zakódovanou délku_, a nižších 32 bitů reprezentuje _zakódovanou šířku_. Obě, délka i šířka, jsou zakódovány jako *nepodsigned* 32bitová celá čísla (ui32).

### Délka

Měřítko pro délku je: (2^32 / 360) = ~11930464.711

Kódování: encoded_longitude = (longitude + 180) * (2^32 / 360)

Dekódování: longitude = (encoded_longitude / (2^32 / 360)) - 180

### Šířka

Měřítko pro šířku je: (2^32 / 180) = ~23860929.422

Kódování: encoded_latitude = (latitude + 90) * (2^32 / 180)

Dekódování: latitude = (encoded_latitude / (2^32 / 180)) - 90

## Přesnost

Zakódovaná délka má přesnost přibližně 4.76 metrů na rovníku.

Zakódovaná šířka má přesnost přibližně 1.19 metrů.