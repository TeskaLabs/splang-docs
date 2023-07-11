---
git_commit_hash: b55fa3f
title: Tuple
---

# Tuplové výrazy


Tuple je jednou ze základních datových struktur, které SP-Lang nabízí.
Tuple je kolekce položek, případně různých typů.

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


### Příklady
```yaml

!TUPLE
with:
  - John Doe
  - 37
  - 175.4
```


Použití zápisu `!!tuple`:
```yaml

!!tuple
- 1
- a
- 1.2
```


Ještě stručnější verze `!!tuple` s použitím syntaxe flow:
```yaml

!!tuple ['John Doe', 37, 175.4]
```


Vynucení specifického typu položky:
```yaml

!TUPLE
with:
  - John Doe
  - !!ui8 37
  - 175.4
```

Položka č. 1 bude mít typ `ui8`.


--- 

## `!GET`: Získat položku z tuple 

Typ: _Mapping_.

Synopsis:
```yaml

!GET
what: <index of the item>
z: <tuple>
```

Je to celé číslo, které představuje _index_ v tuplu.
`what` může být záporné, v takovém případě určuje položku od konce seznamu.
Položky jsou indexovány od 0, to znamená, že první položka v seznamu má index 0.
Pokud je `what` mimo hranice seznamu, příkaz se vrátí s chybou.


### Příklady
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


Použití _záporného indexu_ položek:
```yaml

!GET
what: -1
od:
  !TUPLE
  with:
    - John Doe
    - 32
    - 127.5
```

Vrací `127,5`.
