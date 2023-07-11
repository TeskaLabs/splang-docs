---
git_commit_hash: b55fa3f
title: Záznamové
---

# Záznam výrazů



Záznam je jednou ze základních datových struktur poskytovaných SP-Langem.
Záznam je kolekce položek, případně různých typů.
Položky záznamu jsou pojmenovány (na rozdíl od tuplu) pomocí štítku.

!!! note

	
	
	
	Záznam je postaven na `!TUPLE`.
	

--- 

## `!RECORD`: Kolekce pojmenovaných položek 

Typ:  _Mapping_.

### Synopsis
```yaml

!RECORD
with:
  item1: <item 1>
  item2: <item 2>
  ...
```

`item1` a `item2` jsou označení příslušných položek v záznamu.

Počet položek v záznamu není omezen.
Pořadí položek je zachováno.

### Příklady
```yaml

!RECORD
with:
  jméno: John Doe
  věk: 37 let
  výška: 175,4
```


Použití formuláře toku YAML:
```yaml

!RECORD {with: {jméno: John Doe, věk: 37 let, výška: 175,4} }
```


Použití tagu `!!record`:
```yaml

{jméno: John Doe, věk: 37 let, výška: 175,4}
```


Vynucení konkrétního typu položky:
```yaml

!RECORD
with:
  jméno: John Doe
  věk: !!ui8 37
  výška: 175,4
```

Pole `age` bude mít typ `ui8`.


--- 

## `!GET`: Získat položku ze záznamu 

Typ: _Mapping_.

### Synopsis
```yaml

!GET
what: <name or index of the item>
z: <record>
```

Pokud je `what` řetězec, pak je to název pole v záznamu.

Pokud je `what` celé číslo, pak je to _index_ v záznamu.
Hodnota `what` může být záporná, v takovém případě určuje položku z konce seznamu.
Položky jsou indexovány od 0, to znamená, že první položka v seznamu má index 0.
Pokud je `what` mimo hranice seznamu, příkaz se vrátí s chybou.


### Příklady

Použití názvů položek:
```yaml

!GET
what: name
from:
  !RECORD
  with:
    jméno: John Doe
    věk: 32 let
    výška: 127,5
```

Vrátí `John Doe`.


Pomocí _indexu_ položek:
```yaml

!GET
what: 1
od:
  !RECORD
  with:
    jméno: John Doe
    věk: 32 let
    výška: 127,5
```

Vrací `32`, hodnotu položky `age`.


Používá _záporný index_ položek:
```yaml

!GET
what: -1
od:
  !RECORD
  with:
    jméno: John Doe
    věk: 32 let
    výška: 127,5
```

Vrací `127.5`, hodnotu položky `height`.
