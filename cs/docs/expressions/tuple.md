---
title: Tuple
---

# Výrazy pro tuple

## Přehled

Tuple (do češtiny přeložitelné asi jako 'pevný seznam') je jednou ze základních datových struktur, které SP-Lang nabízí.
Tuple je kolekce položek, které mohou mít různé typy.

* [`!TUPLE`](#tuple): Kolekce položek.
* [`!GET`](#get): Získá položku z tuple.

---

## `!TUPLE`

Kolekce položek.

Typ:  _Mapping_.

Synopsis:

```yaml
!TUPLE
with:
  - ...
  - ...
  ...
```

Počet položek v tuple není omezen.
Pořadí položek je zachováno.

!!! example "Příklad"

    ```yaml
    !TUPLE
    with:
      - John Doe
      - 37
      - 175.4
    ```

!!! example "Příklad"

    Použití zápisu `!!tuple`:

    ```yaml
    !!tuple
    - 1
    - a
    - 1.2
    ```

!!! example "Příklad"

    Ještě stručnější verze `!!tuple` s použitím flow syntaxe:

    ```yaml
    !!tuple ['John Doe', 37, 175.4]
    ```

!!! example "Příklad"

    Vynucení specifického typu položky:

    ```yaml
    !TUPLE
    with:
      - John Doe
      - !!ui8 37
      - 175.4
    ```

    Položka #1 bude mít typ `ui8`.

---

## `!GET`

Získá položku z tuple.

Typ: _Mapping_.

Synopsis:

```yaml
!GET
what: <index of the item>
from: <tuple>
```

Argument `what` je celé číslo (číslo), které představuje _index_ v tuple.
Může být záporné, v takovém případě určuje položku od konce seznamu.

Položky jsou indexovány od 0, to znamená, že první položka v seznamu má index 0.

Pokud je `what` mimo hranice seznamu, příkaz se vrátí s chybou.

!!! example "Příklad"

    ```yaml
    !GET
    what: 1
    from:
      !TUPLE
      with:
        - John Doe
        - 32
        - 127.5
    ```

    Vrací `32`.

!!! example "Příklad"

    Použití _záporného indexu_ položek:

    ```yaml
    !GET
    what: -1
    from:
      !TUPLE
      with:
        - John Doe
        - 32
        - 127.5
    ```

    Vrací `127,5`.