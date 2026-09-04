---
title: Výrazy pro analýzu
---

# Výrazy pro analýzu

## Přehled

Výrazy pro analýzu jsou funkce pro analýzu určité sekvence znaků.

Základní analyzátory mohou rozlišovat mezi číslicemi, písmeny a mezerami:

- [`!PARSE.DIGIT`](#parsedigit), [`!PARSE.DIGITS`](#parsedigits): Analyzovat jednotlivé nebo více číslic.
- [`!PARSE.LETTER`](#parseletter), [`!PARSE.LETTERS`](#parseletters): Analyzovat jednotlivá nebo více písmen.
- [`!PARSE.SPACE`](#parsespace), [`!PARSE.SPACES`](#parsespaces): Analyzovat jednotlivé nebo více znaků pro mezeru.
- [`!PARSE.CHAR`](#parsechar), [`!PARSE.CHARS`](#parsechars): Analyzovat jednotlivé nebo více znaků.
- [`!PARSE.EOF`](#parseeof): Ověřit, že bylo dosaženo konce vstupního řetězce.

Následující výrazy se používají pro analýzu znaků z vlastního souboru znaků a hledání specifických znaků v vstupních řetězcích:

- [`!PARSE.EXACTLY`](#parseexactly): Analyzovat pouze specifickou sekvenci znaků.
- [`!PARSE.UNTIL`](#parseuntil): Analyzovat do doby, než je nalezen specifický znak.
- [`!PARSE.BETWEEN`](#parsebetween): Analyzovat mezi dvěma znaky.
- [`!PARSE.ONEOF`](#parseoneof): Analyzovat pouze jeden z povolených znaků.
- [`!PARSE.NONEOF`](#parsenoneof): Analyzovat každý znak kromě zakázaných.
- [`!PARSE.REGEX`](#parseregex): Analyzovat znaky odpovídající regulárnímu výrazu.

Následující výrazy se používají pro analýzu dat a časů v různých formátech:

- [`!PARSE.DATETIME`](#parsedatetime): Analyzovat datum a čas.
- [`!PARSE.MONTH`](#parsemonth): Analyzovat měsíc v různých formátech.
- [`!PARSE.FRAC`](#parsefrac): Analyzovat desetinná čísla (což je užitečné pro analýzu mikrosekund).

Následující výrazy se používají pro analýzu specifických typů řetězců:

- [`!PARSE.IP`](#parseip): Analyzovat IP adresu.
- [`!PARSE.MAC`](#parsemac): Analyzovat MAC adresu.

---

## `!PARSE.DIGIT`

Analyzovat jednu číslici.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.DIGIT
```

!!! example

    _Vstupní řetězec:_ `2`

    ```yaml
    !PARSE.DIGIT
    ```

---

## `!PARSE.DIGITS`

Analyzovat sekvenci číslic.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.DIGITS
min: <...>
max: <...>
exactly: <...>
```

- `exactly` určuje přesný počet číslic k analýze.
- `min` a `max` určují minimální a maximální počet číslic k analýze. Nemohou být kombinovány s parametrem `exactly`.
- Pokud není uvedeno žádné z polí `min`, `max` a `exactly`, analyzuje se co nejvíce číslic. Výchozí minimum je `1`.

!!! warning

    Pole `exactly` nelze použít společně s poli `min` nebo `max`. A samozřejmě hodnota `max` nemůže být menší než hodnota `min`.

!!! example

    _Vstupní řetězec:_ `123`

    ```yaml
    !PARSE.DIGITS
    max: 4
    ```

<details>
  <summary>Více příkladů</summary>

Analyzovat co nejvíce číslic:
```yaml
!PARSE.DIGITS
```

Analyzovat přesně 3 číslice:
```yaml
!PARSE.DIGITS
exactly: 3
```

Analyzovat alespoň 2 číslice, ale ne více než 4:
```yaml
!PARSE.DIGITS
min: 2
max: 4
```

</details>

---

## `!PARSE.LETTER`

Analyzovat jedno písmeno.

Pod písmeny máme na mysli latinská písmena od A do Z, jak velká, tak malá.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.LETTER
```

!!! example

    _Vstupní řetězec:_ `A`

    ```yaml
    !PARSE.LETTER
    ```

---

## `!PARSE.LETTERS`

Analyzovat sekvenci písmen.

Pod písmeny máme na mysli latinská písmena od A do Z, jak velká, tak malá.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.LETTERS
min: <...>
max: <...>
exactly: <...>
```

Pole `min`, `max` a `exactly` jsou volitelná. Pokud není uvedeno `min`, výchozí minimum je `1`.

!!! warning

    Pole `exactly` nelze použít společně s poli `min` nebo `max`.
    A samozřejmě hodnota `max` nemůže být menší než hodnota `min`.

!!! example

    _Vstupní řetězec:_ `cat`

    ```yaml
    !PARSE.LETTERS
    max: 4
    ```

<details>
  <summary>Více příkladů</summary>

Analyzovat co nejvíce písmen:
```yaml
!PARSE.LETTERS
```

Analyzovat přesně 3 písmena:
```yaml
!PARSE.LETTERS
exactly: 3
```

Analyzovat alespoň 2 písmena, ale ne více než 4:
```yaml
!PARSE.LETTERS
min: 2
max: 4
```

</details>

---

## `!PARSE.SPACE`

Analyzovat jeden znak pro mezeru.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.SPACE
```

---

## `!PARSE.SPACES`

Analyzovat sekvenci znaků pro mezeru.

Analyzovat co nejvíce znaků pro mezeru:

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.SPACES
```

---

## `!PARSE.CHAR`

Analyzovat jeden znak jakéhokoli typu.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.CHAR
```

!!! example

    Vstupní řetězec: `@`

    ```yaml
    !PARSE.CHAR
    ```

---

## `!PARSE.CHARS`

Analyzovat sekvenci znaků.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.CHARS
min: <...>
max: <...>
exactly: <...>
```

Pole `min`, `max` a `exactly` jsou volitelná. Pokud není uvedeno `min`, výchozí minimum je `1`.

!!! warning

    Pole `exactly` nelze použít společně s poli `min` nebo `max`.
    A samozřejmě hodnota `max` nemůže být menší než hodnota `min`.

!!! example

    Vstupní řetězec:_ `name@123_`

    ```yaml
    !PARSE.CHARS
    max: 8
    ```

!!! tip

    Použijte `!PARSE.CHARS` s výchozími nastaveními pro analýzu až do konce řetězce.

<details>
  <summary>Více příkladů</summary>

Analyzovat co nejvíce znaků:
```yaml
!PARSE.CHARS
```

Analyzovat přesně 3 znaky:
```yaml
!PARSE.CHARS
exactly: 3
```

Analyzovat alespoň 2 znaky, ale ne více než 4:
```yaml
!PARSE.CHARS
min: 2
max: 4
```

</details>

---

## `!PARSE.EOF`

Ověří, že bylo dosaženo konce vstupního řetězce.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.EOF
```

Analyzátor uspěje pouze tehdy, když je aktuální pozice analýzy na konci vstupního řetězce.

!!! example

    _Vstupní řetězec:_ `abc`

    ```yaml
    !PARSE.TUPLE
    - 'abc'
    - !PARSE.EOF
    ```

---

## `!PARSE.EXACTLY`

Analyzovat přesně definovanou sekvenci znaků.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.EXACTLY
what: <...>
```

nebo kratší verze:

```yaml
!PARSE.EXACTLY <...>
```

!!! example

    Vstupní řetězec:_`Hello world!`

    ```yaml
    !PARSE.EXACTLY
    what: "Hello"
    ```

---

## `!PARSE.UNTIL`

Analyzovat sekvenci znaků, dokud není nalezen specifický znak.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.UNTIL
what: <...>
stop: <before/after>
eof: <true/false>
```

nebo kratší verze:

```yaml
!PARSE.UNTIL <...>
```

- `what`: Určuje jeden (a pouze jeden) znak, který se má hledat v vstupním řetězci.

- `stop`: Určuje, zda by měl být zastavovací znak analyzován nebo ne.
            Možné hodnoty: `before` nebo `after` (výchozí).

- `eof`: Určuje, zda bychom měli analyzovat až do konce řetězce, pokud symbol `what` není nalezen.
            Možné hodnoty: `true` nebo `false` (výchozí).

- `escape`: Určuje únikový znak.

!!! info

    Pole `what` musí být jediný znak. Ale některé znaky pro mezeru mohou být také použity, jako například `tab`.
    Pro hledání sekvence znaků viz výraz [`!PARSE.CHARS.LOOKAHEAD`](./combinator.md#parsecharslookahead).

!!! example

    _Vstupní řetězec:_ `60290:11`

    ```yaml
    !PARSE.UNTIL
    what: ":"
    ```

<details>
  <summary>Více příkladů</summary>

Analyzovat do <code>:</code> symbolu a zastavit se před ním:
```yaml
!PARSE.UNTIL
what: ":"
stop: "before"
```

Analyzovat do symbolu mezery a zastavit se po něm:
```yaml
!PARSE.UNTIL ' '
```

Analyzovat do <code>,</code> symbolu nebo analyzovat až do konce řetězce, pokud není nalezen:
```yaml
!PARSE.UNTIL
what: ","
eof: true
```

Analyzovat do <code>tab</code> symbolu:
```yaml
!PARSE.UNTIL
what: 'tab'
```

Analyzovat do svislé čáry, uniknout interní svislé čáry:<br>

<i>Vstupní řetězec:</i><code>CRED_REFR\|success\|fail|</code>

```yaml
!PARSE.UNTIL
what: '|'
escape: '\'
```

</details>

---

## `!PARSE.BETWEEN`

Analyzovat sekvenci znaků mezi dvěma specifickými znaky.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.BETWEEN
what: <...>
start: <...>
stop: <...>
escape: <...>
```

nebo kratší verze:

```yaml
!PARSE.BETWEEN <...>
```

- `what` - určuje mezi kterými stejnými znaky bychom měli analyzovat.

- `start`, `stop` - určuje mezi kterými různými znaky bychom měli analyzovat.

- `escape` - určuje únikový znak.

!!! example

    Vstupní řetězec:_ `[10/May/2023:08:15:54 +0000]`

    ```yaml
    !PARSE.BETWEEN
    start: '['
    stop: ']'
    ```

<details>
  <summary>Více příkladů</summary>

Analyzovat mezi dvojitými uvozovkami:
```yaml
!PARSE.BETWEEN
what: '"'
```

Analyzovat mezi dvojitými uvozovkami, krátká forma:
```yaml
!PARSE.BETWEEN '"'
```

Analyzovat mezi dvojitými uvozovkami, uniknout interním dvojitým uvozovkám:<br>

<i>Vstupní řetězec:</i><code>"one, \"two\", three"</code>

```yaml
!PARSE.BETWEEN
what: '"'
escape: '\'
```
</details>

---

## `!PARSE.ONEOF`

Analyzovat jeden znak z vybraného souboru znaků.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.ONEOF
what: <...>
```
nebo kratší verze:
```yaml
!PARSE.ONEOF <...>
```

!!! example

    _Vstupní řetězce:_

    ```
    process finished with status 0
    process finished with status 1
    process finished with status x
    ```

    ```yaml
    !PARSE.KVLIST
    - "process finished with status "
    - !PARSE.ONEOF
    what: "01x"
    ```

---

## `!PARSE.NONEOF`

Analyzovat jeden znak, který není ve vybraném souboru znaků.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.NONEOF
what: <...>
```

nebo kratší verze:

```yaml
!PARSE.NONEOF <...>
```

!!! example

    Vstupní řetězec:_ `Wow!`

    ```yaml
    !PARSE.NONEOF
    what: ",;:[]()"
    ```

---

## `!PARSE.REGEX`

Analyzovat sekvenci znaků, která odpovídá regulárnímu výrazu.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.REGEX
what: <...>
```

!!! example

    Vstupní řetězec:_ `FTVW23_L-C: Message...`

    _Výstup:_ `FTVW23_L-C`

    ```yaml
    !PARSE.REGEX
    what: '[a-zA-Z0-9_\-0]+'
    ```

---

## `!PARSE.DATETIME`

Analyzovat datum a čas.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.DATETIME
- year: <...>
- month: <...>
- day: <...>
- hour: <...>
- minute: <...>
- second: <...>
- microsecond: <...>
- nanosecond: <...>
- timezone: <...>
```

- Pole `month` a `day` jsou povinná.
- Pole `year` je volitelné. Pokud není uvedeno, bude použita funkce [smart year](#smart-year). Podporovány jsou jak 2, tak 4-místná čísla.
- Pole `hour`, `minute`, `second`,  `microsecond`, `nanosecond` jsou volitelná. Pokud nejsou uvedena, bude použita výchozí hodnota 0.
- Uvedení pole mikrosekund jako `microseconds?` umožňuje analyzovat mikrosekundy nebo ne, v závislosti na jejich přítomnosti ve vstupním řetězci.
- Pole `timezone` je volitelné. Pokud není uvedeno, bude použita výchozí hodnota `UTC`. [Přečtěte si více o analýze časových pásem zde.](#timezone)

!!! tip "Běžné formáty datumu a času"
    Použijte [Zkratky](#shortcuts) pro analýzu formátů datumu a času [`RFC 3339`](#rfc-3339), [`RFC 3164`](#rfc-3164) a [`ISO 8601`](#iso-8601).

!!! tip "UNIX čas"
    Pro analýzu datumu a času v [UNIX čase](https://en.wikipedia.org/wiki/Unix_time) použijte [`!PARSE.DATETIME EPOCH`](#epoch).

!!! tip
    Použijte [`!PARSE.MONTH`](#parsemonth) pro analýzu měsíce.

!!! tip
    Použijte [`!PARSE.FRAC`](#parsefrac) pro analýzu mikrosekund a nanosekund. Všimněte si, že tento výraz spotřebovává `.` a `,` také. Nezpracovávejte je odděleně.

!!! example
    _Vstupní řetězec:_ `2022-10-13T12:34:56.987654`

    ```yaml
    !PARSE.DATETIME
    - year: !PARSE.DIGITS
    - '-'
    - month: !PARSE.MONTH 'number'
    - '-'
    - day: !PARSE.DIGITS
    - 'T'
    - hour: !PARSE.DIGITS
    - ':'
    - minute: !PARSE.DIGITS
    - ':'
    - second: !PARSE.DIGITS
    - microsecond: !PARSE.FRAC
            base: "micro"
    ```

??? example "Dvou-místný rok"

    Analyzovat datum a čas s dvou-místným rokem:

    _Vstupní řetězec:_ `22-10-13T12:34:56.987654`

    ```yaml hl_lines="2"
    !PARSE.DATETIME
    - year: !PARSE.DIGITS
    - '-'
    - month: !PARSE.MONTH "number"
    - '-'
    - day: !PARSE.DIGITS
    - 'T'
    - hour: !PARSE.DIGITS
    - ':'
    - minute: !PARSE.DIGITS
    - ':'
    - second: !PARSE.DIGITS
    - microsecond: !PARSE.FRAC
                base: micro
    ```

### Zkratky

Podporované zkrácené formy (malá i velká písmena):

#### ISO 8601

```yaml
!PARSE.DATETIME ISO8601
```

#### RFC 3339

```yaml
!PARSE.DATETIME RFC3339
```

#### RFC 3164

```yaml
!PARSE.DATETIME RFC3164
```

#### Epoch

```yaml
!PARSE.DATETIME EPOCH
```

---

## `!PARSE.MONTH`

Analyzuje měsíc.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.MONTH
what: <...>
```

nebo kratší verze:

```yaml
!PARSE.MONTH <...>
```

Parametr `what` určuje formát názvu měsíce.
Možné hodnoty:

- `number`: číselná reprezentace, např. `01` pro leden, `12` pro prosinec
- `short`: třípísmenná reprezentace, např. `Jan` pro leden, `Dec` pro prosinec
- `full`: plný název, např. `January`, `December`

!!! tip
    Použijte `!PARSE.MONTH` pro analýzu měsíce jako součásti `!PARSE.DATETIME`.

---

## `!PARSE.FRAC`

Analyzuje desetinnou část.

!!! warn

    Parsování desetinné části zahrnuje i tečku (.) a čárku (,) jako oddělovač.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.FRAC
base: <...>
max: <...>
```

- `base`: Základ desetinné části (`milli`, `micro`, `nano`).
- `max`: Maximální počet číslic podle hodnoty `base`. Výchozí hodnoty jsou `3`, `6`, `9`.

---

## `!PARSE.IP`

Analyzuje IP adresu ve formátu IPv4 i IPv6.

Vrací [číselnou reprezentaci](https://ndocs.teskalabs.com/sp-lang/language/types/#ip-address) IP adresy.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.IP
```

!!! example

    _Vstupní řetězec:_ `193.178.72.2`

    ```yaml
    !PARSE.IP
    ```

---

## `!PARSE.MAC`

Analyzuje MAC adresu v jednom z těchto formátů:

- `XX:XX:XX:XX:XX:XX` — oddělené dvojtečkami
- `XX-XX-XX-XX-XX-XX` — oddělené pomlčkami
- `XXXX.XXXX.XXXX` — oddělené tečkami (Cisco styl)
- `0xXXXXXXXXXXXX` — hex kódování

Vrací [číselnou reprezentaci](https://ndocs.teskalabs.com/sp-lang/language/types/#mac-address) MAC adresy.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.MAC
```

---

## `!PARSE.CEFKV`

Analyzuje záznamy ve formátu CEF (Common Event Format) key-value a extrahuje strukturovaná pole ze vstupního řetězce.

Každé pole má formát `key=value`, `=` je pevný oddělovač a jednotlivé dvojice jsou odděleny jednou mezerou.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.CEFKV
custom_to_kv: <true/false>
```

- `custom_to_kv` je nepovinné (výchozí: `false`). Pokud je `true`, vlastní CEF label pole (`cs1Label`, `cn2Label` a podobně) se převedou na běžné dvojice klíč-hodnota.

---

## `!PARSE.FIELDS`

Analyzuje více polí oddělených určitým znakem a volitelně uzavřených v oddělovačích, které se při parsování odstraní.
Každé pole se přiřadí odpovídajícímu klíči ze seznamu `keys`.

Pokud je zadán parametr `stop`, parsuje se přesně tolik polí, kolik je klíčů.
Poslední pole se čte až do znaku `stop`. Parser se zastaví **před** znakem `stop`.

Parsování selže, pokud počet polí neodpovídá počtu klíčů.

Typ: _Analyzátor_.

Synopse:

```yaml
!PARSE.FIELDS
keys: <...>
separator: <...>
delimiters: <...>
empty: <...>
stop: <...>
```

- `keys` je seznam názvů polí extrahovaných ze vstupního řetězce.
- `separator` je znak oddělující pole.
- `delimiters` je seznam znaků nebo dvojic znaků, které mohou pole obalovat.
- `stop` je nepovinný znak konce posledního pole.
- `empty` je nepovinný boolean (výchozí: `false`), který odstraní prázdná pole z výstupu.

!!! example

    _Vstupní řetězec:_ `<8>,url,,"2024/12/09 19:45:31",99.70.55.200`

    ```yaml
    !PARSE.FIELDS
    keys:
      - pri
      - subtype
      - future_use
      - time_generated
      - src_ip
    separator: ","
    delimiters:
      - '"'
      - "'"
      - ['<', '>']
      - '"""'
    ```

---