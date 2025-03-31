---
title: Datum/čas
---

# Výrazy pro datum a čas

## Přehled

Datum a čas se v SP-Langu vyjadřují pomocí typu `datetime`.
Má mikrosekundové rozlišení a rozsah od roku 8190 př.n.l. do roku 8191.
Je v časovém pásmu UTC.

!!! info

    Další informace o typu `datetime` najdete [zde](../language/types/date-time.md).

* [`!NOW`](#now): Aktuální datum a čas.
* [`!DATETIME`](#datetime): Konstrukce nového `datetime`.
* [`!DATETIME.FORMAT`](#datetimeformat): Formátování `datetime`.
* [`!GET`](#get): Získání komponenty `datetime`.

---

## `!NOW`

Typ: _Mapping_.

Získá aktuální datum a čas.

```yaml
!NOW
```

---

## `!DATETIME`

Typ: _Mapping_.

Konstruuje `datetime` z komponent jako je rok, měsíc, den atd.

```yaml
!DATETIME
year: <year>
month: <month>
day: <day>
hour: <hour>
minute: <minute>
second: <second>
microsecond: <microsecond>
timezone: <timezone>
```

* `year` je celé číslo v rozsahu -8190 … 8191.
* `month` je celé číslo v rozsahu 1 … 12.
* `day` je celé číslo v rozsahu 1 … 31, odpovídající počtu dní v daném měsíci.
* `hour` je celé číslo v rozsahu 0 … 24, je nepovinné a výchozí hodnota je `0`.
* `minute` je celé číslo v rozsahu 0 … 59, je nepovinné a výchozí hodnota je `0`.
* `second` je celé číslo v rozsahu 0 … 60, je nepovinné a výchozí hodnota je `0`.
* `microsecond` je celé číslo v rozsahu 0 … 1000000, je nepovinné a výchozí hodnota je `0`.
* `timezone` je název časového pásma podle [IANA Time Zone Database](https://www.iana.org/time-zones). Je nepovinné a výchozí časové pásmo je UTC.

!!! example "Příklad: Datum/čas v UTC"

    ```yaml
    !DATETIME
    year: 2021
    month: 10
    day: 13
    hour: 12
    minute: 34
    second: 56
    microsecond: 987654
    ```

!!! example "Příklad: výchozí hodnoty"

    ```yaml
    !DATETIME
    year: 2021
    month: 10
    day: 13
    ```

!!! example "Příklad: časová pásma"

    ```yaml
    !DATETIME
    year: 2021
    month: 10
    day: 13
    timezone: Europe/Prague
    ```

    ```yaml
    !DATETIME
    year: 2021
    month: 10
    day: 13
    timezone: "+05:00"
    ```

---

## `!DATETIME.FORMAT`

Typ: _Mapping_.

Formátuje informace o datu a čase na základě `datetime`.

```yaml
!DATETIME.FORMAT
with: <datetime>
format: <format>
timezone: <string>
```

`datetime` obsahuje informace o datech a čase, které se mají použít pro formátování.
`format` je řetězec, který obsahuje specifikaci formátu výstupu.
`timezone` je nepovinná informace. Pokud je uvedena, bude čas vypsán v místním čase zadaném argumentem, jinak se použije časové pásmo UTC.

### Formát

| Direktiva | Komponenta |
| --- | --- |
|`%H`| Hodiny (24hodinové hodiny) jako desetinné číslo doplněné nulou.|
|`%M`| Minuta jako desetinné číslo doplněné nulou.|
|`%S`| Vteřina jako desetinné číslo doplněné nulou.|
|`%f`| Mikrosekunda jako desetinné číslo doplněné nulou na 6 číslic.|
|`%I`| Hodina (12hodinové hodiny) jako desetinné číslo doplněné nulou.|
|`%p`| Ekvivalent AM nebo PM v místním jazyce. |
|`%d`| Den v měsíci jako desetinné číslo doplněné nulou.|
|`%m`| Měsíc jako desetinné číslo doplněné nulou.|
|`%y`| Rok bez století jako desetinné číslo doplněné nulou.|
|`%Y`| Rok se stoletím jako desetinné číslo.|
|`%z`| Posun UTC.|
|`%a`| Zkrácený název dne v týdnu.|
|`%A`| Den v týdnu jako plný název.|
|`%w`| Den v týdnu jako desetinné číslo, kde 0 je neděle a 6 je sobota.|
|`%b`| Měsíc jako zkrácený název.|
|`%B`| Měsíc jako plný název.|
|`%j`| Den v roce jako desetinné číslo doplněné nulou.|
|`%U`| Číslo týdne v roce (neděle jako první den v týdnu) jako desetinné číslo doplněné nulou. Všechny dny v novém roce předcházející první neděli se považují za dny v týdnu 0.|
|`%W`| Číslo týdne v roce (pondělí jako první den v týdnu) jako desetinné číslo doplněné nulou. Všechny dny v novém roce předcházející prvnímu pondělí se považují za dny v týdnu 0.|
|`%c`| Reprezentace data a času.|
|`%x`| Reprezentace data.|
|`%X`| Reprezentace času.|
|`%%`| Doslovný znak '%'.|

!!! example

    ```yaml
    !DATETIME.FORMAT
    with: !NOW
    format: "%Y-%m-%d %H:%M:%S"
    timezone: "Europe/Prague"
    ```

    Vypíše aktuální místní čas jako např. `2022-12-31 12:34:56` s použitím časového pásma "Europe/Prague".

---

## `!DATETIME.PARSE`

Typ: _Mapping_.

Parsuje datum a čas z řetězce.

```yaml
!DATETIME.PARSE
what: <string>
format: <format>
timezone: <timezone>
```

Vstupní řetězec `what` analyzuje pomocí řetězce `format`.
Informace `timezone` je nepovinná. Pokud je uvedena, určuje místní časové pásmo řetězce `what`.

Další informace o řetězci `format` naleznete v kapitole [Formát](#format) výše.

!!! example

    ```yaml
    !DATETIME.PARSE
    what: "2021-06-29T16:51:43-08"
    format: "%y-%m-%dT%H:%M:%S%z"
    ```

---

## `!GET`

Typ: _Mapping_.

Extrahuje z `datetime` komponenty data/času, jako je hodina, minuta, den atd.

```yaml
!GET
what: <string>
from: <datetime>
timezone: <timezone>
```

Vybere komponentu `what` z `datetime`.
`timezone` je nepovinná, pokud není uvedena, použije se časová zóna UTC.

### Komponenty

| Direktiva | Komponenta |
| --- | --- |
|`year`, `y`| Rok |
| `month`, `m`| Měsíc |
| `day`, `d`| Den |
| `hour`, `H`| Hodina |
| `minute`, `M`| Minuta |
| `second`, `S`| Sekunda |
| `microsecond`, `f`| Mikrosekunda |
| `weekday`, `w`| Den v týdnu |

!!! example

    Získá komponentu `hours` aktuálního časového razítka s použitím časového pásma "Europe/Prague".

    ```yaml
    !GET
    what: H
    from: !NOW
    timezone: "Europe/Prague"
    ```

!!! example "Příklad: Aktuální rok"

    ```yaml
    !GET { what: year, from: !NOW }
    ```