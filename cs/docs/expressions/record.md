---
title: Záznam
---

# Výrazy pro záznam

Záznam (record) je jednou ze základních datových struktur poskytovaných SP-Langem.
Jedná se o kolekci položek, které mohou mít různé typy.
Položky záznamu jsou pojmenovány (na rozdíl od tuple) pomocí štítku (label).

!!! note "Poznámka"

	Záznam je postaven na `!TUPLE`.

* [`!RECORD`](#record): Kolekce pojmenovaných položek.
* [`!GET`](#get): Získá položku ze záznamu.

---

## `!RECORD`: Kolekce pojmenovaných položek 

Typ:  _Mapping_.

Synopsis:

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

!!! example "Příklad"

	```yaml
	!RECORD
	with:
	  jméno: John Doe
	  věk: 37 let
	  výška: 175,4
	```

!!! example "Příklad ve flow-formě:"

	```yaml
	!RECORD {with: {jméno: John Doe, věk: 37 let, výška: 175,4} }
	```

!!! example "Použití tagu `!!record`:"

	```yaml
	!!record {jméno: John Doe, věk: 37 let, výška: 175,4}
	```

!!! example "Vynucení konkrétního typu položky:"

	```yaml
	!RECORD
	with:
	  jméno: John Doe
	  věk: !!ui8 37
	  výška: 175,4
	```

	Pole `age` bude mít typ `ui8`.

---

## `!GET`: Získá položku ze záznamu

Typ: _Mapping_.

Synopsis:

```yaml
!GET
what: <name or index of the item>
from: <record>
```

Pokud je `what` řetězec, pak je to název pole v záznamu.

Pokud je `what` celé číslo, pak je to _index_ v záznamu.
Hodnota `what` může být záporná, v takovém případě určuje položku z konce seznamu.
Položky jsou indexovány od 0, to znamená, že první položka v seznamu má index 0.
Pokud je `what` mimo hranice seznamu, příkaz se vrátí s chybou.

!!! example "Příklad použití názvů položek:"

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

!!! example "Použití _indexu_ položek:"

	```yaml
	!GET
	what: 1
	from:
	  !RECORD
	-  with:
	    name: John Doe
	    age: 32
	    height: 127.5
	```

	Vrací `32`, hodnotu položky `age`.

!!! example "Použití _záporného indexu_ položek:"

	```yaml
	!GET
	what: -1
	from:
	  !RECORD
	  with:
		name: John Doe
		age: 32
		height: 127.5
	```

	Vrací `127.5`, hodnotu položky `height`.