---
git_commit_hash: b55fa3f
title: Tuple
---

# Výrazy pro tuple


Tuple (do češtiny přeložitelné asi jako 'pevný seznam') je jednou ze základních datových struktur, které SP-Lang nabízí.
Tuple je kolekce položek, které mohou mít různé typy.

--- 

## `!TUPLE`: Kolekce položek 

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

## `!GET`: Získá položku z tuple 

Typ: _Mapping_.

Synopsis:

```yaml
!GET
what: <index of the item>
from: <tuple>
```

`what` je celé číslo, které představuje _index_ v tuple.
`what` může být záporné, v takovém případě určuje položku od konce seznamu.
Položky jsou indexovány od 0, to znamená, že první položka v seznamu má index 0.
Pokud je `what` mimo hranice seznamu, příkaz se vrátí s chybou.


!!! example "Příklad"

    ```yaml
    !GET
    what: 1
    from:
      !TUPLE
      with:
        - Doe:: John Doe
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
