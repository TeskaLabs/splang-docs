---
title: Kombinátorové výrazy
---

# Kombinátorové výrazy

## Přehled

Kombinátory jsou funkce pro skládání parsec výrazů (parserů nebo jiných kombinátorů) dohromady. Specifikují, jak se provádí analýza, jaký je typ výstupu. Mohou být použity pro řízení toku analýzy (aplikaci podmínkových nebo opakovaných výrazů) a také pro hledání předběžného výrazu ve vstupním řetězci.

**Výběr výstupu** určuje typ výstupu:

- [`!PARSE.KVLIST`](#parsekvlist): Analyzuje sekvenci klíčů a hodnot do [typu tašky](../../language/types/index.md#bag).
- [`!PARSE.KV`](#parsekv): Analyzuje klíč a hodnotu ze vstupního řetězce.
- [`!PARSE.TUPLE`](#parsetuple): Analyzuje do [typu n-tice](../tuple.md).
- [`!PARSE.RECORD`](#parserecord)

**Výrazy pro řízení toku** mohou provádět sekvenci parserových výrazů na základě určitých podmínek:

- [`!PARSE.REPEAT`](#parserepeat): Provádí stejnou sekvenci výrazů vícekrát, podobně jako příkaz "for" z různých jazyků.
- [`!PARSE.SEPARATED`](#parseseparated)
- [`!PARSE.OPTIONAL`](#parseoptional): Přidává volitelnou parserovou funkci, podobně jako příkaz "if/else" z různých jazyků.
- [`!PARSE.TRIE`](#parsetrie): Provádí sekvenci výrazů na základě předpony vstupního řetězce.

**Předběžné výrazy**:

- [`!PARSE.CHARS.LOOKAHEAD`](#parsecharslookahead): Analyzuje, dokud není nalezena určitá sekvence znaků ve řetězci.

---

## `!PARSE.KVLIST`

Analyzuje seznam párů klíč-hodnota.

Iterováním přes seznam prvků výraz `!PARSE.KVLIST` shromažďuje páry klíč-hodnota do [tašky](../../language/types/index.md#bag).

Typ: _Kombinátor_

Synopse:

```yaml
!PARSE.KVLIST
- <...>
- key: <...>
```

Prvky, které nejsou klíčem, jsou analyzovány, ale nejsou shromažďovány:

```yaml
!PARSE.KVLIST
- <...>  # analyzováno, ale ne shromážděno
- key1: <...>  # analyzováno a shromážděno
- key2: <...>  # analyzováno a shromážděno
```

Vnořené výrazy `!PARSE.KVLIST` jsou spojeny s nadřazeným:

```yaml
!PARSE.KVLIST
- <...>
- !PARSE.KVLIST  # výraz je spojen s nadřazeným
  - key3: <...>
  - <...>
- key4: <...>
```

!!! example

    Vstupní řetězec:

    ```
    <141>May  9 10:00:00 myhost.com notice tmm1[22731]: User 'user' was logged in.
    ```

    ```yaml
    !PARSE.KVLIST
    - '<'
    - PRI: !PARSE.DIGITS
    - '>'
    - TIMESTAMP: !PARSE.DATETIME
                    - month: !PARSE.MONTH 'short'
                    - !PARSE.SPACES
                    - day: !PARSE.DIGITS # Den
                    - !PARSE.SPACES
                    - hour: !PARSE.DIGITS # Hodiny
                    - ':'
                    - minute: !PARSE.DIGITS # Minuty
                    - ':'
                    - second: !PARSE.DIGITS # Sekundy

    - !PARSE.SPACES
    - HOSTNAME: !PARSE.UNTIL ' '
    - LEVEL: !PARSE.UNTIL ' '
    - PROCESS.NAME: !PARSE.UNTIL '['
    - PROCESS.PID: !PARSE.DIGITS
    - ']:'
    - !PARSE.SPACES
    - MESSAGE: !PARSE.CHARS
    ```

    _Výstup:_
    
    ```
    [
        (PRI, 141),
        (TIMESTAMP, 140994182325993472),
        (HOSTNAME, myhost.com),
        (LEVEL, notice),
        (PROCESS.NAME, tmm1),
        (PROCESS.PID, 22731),
        (MESSAGE, User 'user' was logged in.)
    ]
    ```

---

## `!PARSE.KV`

Analyzuje klíč a hodnotu ze řetězce do páru klíč-hodnota, s možností přidání určité předpony.

Typ: _Kombinátor_

Synopse:

```yaml
!PARSE.KV
- prefix: <...>
- key: <...>
- value: <...>
- <...> # volitelné prvky
```

- `prefix` je volitelný. Pokud je specifikován, předpona bude přidána k `key`.
- `key` a `value` jsou povinné.

!!! tip
    Použijte kombinaci `!PARSE.REPEAT` a `!PARSE.KV` pro analýzu opakovaných párů klíč-hodnota. (viz příklady)

!!! example

    _Vstupní řetězec:_ `eventID= "1011"`

    ```yaml
    !PARSE.KV
    - key: !PARSE.UNTIL '='
    - !PARSE.SPACE
    - value: !PARSE.BETWEEN {what: '"'}
    ```

    _Výstup:_ `(eventID, 1011)`

??? example "Analyzovat klíč a hodnotu se specifikovanou předponou"

    _Vstupní řetězec:_ `eventID= "1011"`

    ```yaml
    !PARSE.KV
    - key: !PARSE.UNTIL {what: '='}
    prefix: SD.PARAM.
    - !PARSE.SPACE
    - value: !PARSE.BETWEEN {what: '"'}
    ```
    _Výstup:_ `(SD.PARAM.eventID, 1011)`

??? example "Použití spolu s `!PARSE.REPEAT`"

    _Vstupní řetězec:_ `devid="FEVM020000191439" vd="root" itime=1665629867`

    ```yaml
    !PARSE.REPEAT
    what: !PARSE.KV
        - !PARSE.OPTIONAL
        what: !PARSE.SPACE
        - key: !PARSE.UNTIL '='
        - value: !TRY
                - !PARSE.BETWEEN '"'
                - !PARSE.UNTIL { what: ' ', eof: true}
    ```

    _Výstup:_
    ```
    [
        (devid, FEVM020000191439),
        (vd, root),
        (itime, 1665629867)
    ]
    ```

---

## `!PARSE.TUPLE`

Typ: _Kombinátor_

Analyzuje seznam hodnot do n-tice.

Iterováním přes seznam prvků výraz `!PARSE.TUPLE` shromažďuje hodnoty do [n-tice](../tuple.md).

Synopse:

```yaml
!PARSE.TUPLE
- <...>
- <...>
- <...>

```

!!! example

    Vstupní řetězec:_`Ahoj světe!`

    ```yaml
    !PARSE.TUPLE
    - 'Ahoj'
    - !PARSE.SPACE
    - 'světe'
    - '!'
    ```

    _Výstup:_ `('Ahoj', ' ', 'světe', '!')`

---

## `!PARSE.RECORD`

Analyzuje seznam hodnot do struktury záznamu.

Iterováním přes seznam prvků výraz `!PARSE.RECORD` shromažďuje hodnoty do struktury záznamu.

Typ: _Kombinátor_

Synopse:

```yaml
!PARSE.RECORD
- <...>
- element1: <...>
- element2: <...>
- <...>

```

!!! example

    _Vstupní řetězec:_ `<165>1 `

    ```yaml
    !PARSE.RECORD
    - '<'
    - severity: !PARSE.DIGITS
    - '>'
    - version: !PARSE.DIGITS
    - ' '
    ```

    _Výstup:_ `{'output.severity': 165, 'output.version': 1}`

## `!PARSE.REPEAT`

Analyzuje opakovaný vzor.

Typ: _Kombinátor_.

Synopse:

```yaml
!PARSE.REPEAT
what: <výraz>
min: <...>
max: <...>
exactly: <...>
```

- Pokud není specifikováno ani `min`, `max`, `exactly`, bude `what` opakováno co nejvíce.
- `exactly` určuje přesný počet opakování.
- `min` a `max` nastavují minimální a maximální počet opakování.

!!! example

    Vstupní řetězec:_ `host:myhost;ip:192.0.0.1;user:root;`

    ```yaml
    !PARSE.KVLIST
    - !PARSE.REPEAT
    what: !PARSE.KV
        - key: !PARSE.UNTIL ':'
        - value: !PARSE.UNTIL ';'
    ```

    To opakuje výraz `!PARSE.KV` co nejvíce.

    _Výstup:_
    ```
    [
        (host, myhost),
        (ip, 192.0.0.1),
        (user, root)
    ]
    ```

??? Analyzovat přesně třikrát

    Vstupní řetězec:_ `ahoj ahoj ahoj Anna!`

    ```yaml
    !PARSE.KVLIST
    - !PARSE.REPEAT
        what: !PARSE.EXACTLY 'ahoj '
        exactly: 3
    - NAME: !PARSE.UNTIL '!'
    ```

    _Výstup_: `[(NAME, Anna)]`

??? Analyzovat mezi 2 a 4 krát

    Vstupní řetězce:

    ```
    ahoj ahoj Anna!
    ahoj ahoj ahoj Anna!
    ahoj ahoj ahoj ahoj Anna!
    ```

    ```yaml
    !PARSE.KVLIST
    - !PARSE.REPEAT
        what: !PARSE.EXACTLY 'ahoj '
        min: 2
        max: 4
    - NAME: !PARSE.UNTIL '!'
    ```

    _Výstup_: `[(NAME, Anna)]`

---

## `!PARSE.SEPARATED`

Analyzuje sekvenci s oddělovačem.

Typ: _Kombinátor_.

Synopse:

```yaml
!PARSE.SEPARATED
what: <...>
sep: <...>
min: <...>
max: <...>
end: <...>
```

- `min` a `max` jsou volitelné.
- `end` určuje, zda je požadován koncový oddělovač. Ve výchozím nastavení je volitelný.

!!! example
    _Vstupní řetězec:_ `0->1->2->3`

    ```yaml
    !PARSE.SEPARATED
    what: !PARSE.DIGITS
    sep: !PARSE.EXACTLY {what: "->"}
    min: 3
    ```

    _Výstup:_ `[0, 1, 2, 3]`

    *Poznámka:* koncový oddělovač je volitelný, takže vstupní řetězec `0->1->2->3->` je také platný.

<details>
  <summary>Více příkladů</summary>

Analyzovat <code>what</code> hodnoty oddělené <code>sep</code> v <code>[min;max]</code> intervalu, koncový oddělovač je požadován:<br>
<i>Vstupní řetězec:</i> <code>11,22,33,44,55,66,</code>
```yaml
!PARSE.SEPARATED
what: !PARSE.DIGITS
sep: !PARSE.EXACTLY {what: ","}
end: True
min: 3
max: 7
```

Analyzovat <code>what</code> hodnoty oddělené <code>sep</code> v <code>[min;max]</code> intervalu, koncový oddělovač není přítomen:<br>
<i>Vstupní řetězec:</i> <code>0..1..2..3</code>
```yaml
!PARSE.SEPARATED
what: !PARSE.DIGITS
sep: !PARSE.EXACTLY {what: ".."}
end: False
min: 3
max: 5
```

</details>

---

## `!PARSE.OPTIONAL`

Analyzuje volitelný vzor.

Typ: _Kombinátor_

Výraz `!PARSE.OPTIONAL` se pokouší analyzovat vstupní řetězec pomocí specifikovaného parseru. Pokud parser selže, počáteční pozice se vrátí na počáteční.

Synopse:

```yaml
!PARSE.OPTIONAL
what: <...>
```

nebo kratší verze:

```yaml
!PARSE.OPTIONAL <...>
```


!!! example
    _Vstupní řetězce:_

    ```
    mymachine myproc[10]: DHCPACK to
    mymachine myproc[10]DHCPACK to
    ```

    ```yaml hl_lines="6-8"
    !PARSE.KVLIST
    - HOSTNAME: !PARSE.UNTIL ' ' # mymachine
    - TAG: !PARSE.UNTIL '[' # myproc
    - PID: !PARSE.DIGITS  # 10
    - !PARSE.EXACTLY ']'

    # Analýza volitelných znaků
    - !PARSE.OPTIONAL ':'
    - !PARSE.OPTIONAL
        what: !PARSE.SPACE

    - NAME: !PARSE.UNTIL ' '
    ```


## `!PARSE.TRIE`

Typ: _Kombinátor_.

Analyzuje pomocí počáteční předpony.

Výraz `!PARSE.TRIE` vybírá jednu ze specifikovaných předpon a analyzuje zbytek vstupního řetězce pomocí odpovídajícího parseru. Pokud je specifikována prázdná předpona, bude použit odpovídající parser, pokud nejsou shodnuty jiné předpony.

Synopse:

```yaml
!PARSE.TRIE
- <prefix1>: <...>
- <prefix2>: <...>
...
```

!!! tip
    Použijte `!PARSE.TRIE` pro analýzu multivariačních logových zpráv.

!!! example

    Vstupní řetězce:

    ```
    Přijato odpojení z 10.17.248.1 port 60290:11: odpojeno uživatelem
    Odpojeno od uživatele root 10.17.248.1 port 60290
    ```

    ```yaml
    !PARSE.TRIE
    - 'Přijato odpojení z ': !PARSE.KVLIST
                                - CLIENT_IP: !PARSE.UNTIL ' '
                                - 'port '
                                - CLIENT_PORT: !PARSE.DIGITS
                                - ':'
                                - !PARSE.CHARS
    - 'Odpojeno od uživatele ': !PARSE.KVLIST
                                - USERNAME: !PARSE.UNTIL ' '
                                - CLIENT_IP: !PARSE.UNTIL ' '
                                - 'port '
                                - CLIENT_PORT: !PARSE.DIGITS
    ```

??? Specifikujte prázdnou předponu pro neodpovídající případy

    _Vstupní řetězec:_`Selhalo přihlášení pro root z 218.92.0.190`

    ```yaml
    !PARSE.TRIE
    - 'Přijato odpojení z ': !PARSE.KVLIST
                                - CLIENT_IP: !PARSE.UNTIL ' '
                                - 'port '
                                - CLIENT_PORT: !PARSE.DIGITS
                                - ':'
                                - !PARSE.CHARS
    - 'Odpojeno od uživatele ': !PARSE.KVLIST
                                - USERNAME: !PARSE.UNTIL ' '
                                - CLIENT_IP: !PARSE.UNTIL ' '
                                - 'port '
                                - CLIENT_PORT: !PARSE.DIGITS
    - '': !PARSE.KVLIST
        - tags: ["trie-match-fail"]
    ```

    _Výstup:_ `[(tags, ["trie-match-fail"])]`

---

## `!PARSE.CHARS.LOOKAHEAD`

Analyzuje znaky s použitím skupiny předběžného výrazu.

Analyzuje znaky, dokud není nalezena specifikovaná skupina předběžného výrazu, a zastaví se před ní.

Typ: _K