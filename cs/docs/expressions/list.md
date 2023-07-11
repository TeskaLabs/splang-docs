---
git_commit_hash: b55fa3f
title: Seznamy
---

# Výraz pro seznamy


Seznam (list) je jednou ze základních datových struktur, které SP-Lang nabízí.
Seznam obsahuje konečný počet uspořádaných položek, přičemž stejná položka se může vyskytovat vícekrát.
Položky v seznamu musí být stejného typu.

!!! note "Poznámka"

	Seznam se někdy nepřesně nazývá také _pole_.


--- 

## `!LIST`: Seznam položek 

Typ:  _Implicit sequence_, _Mapping_.

### Synopsis

```yaml

!LIST
- ...
- ...
```
!!! hint "Nápověda"

	Pro určení počtu položek v seznamu použijte `!COUNT`.


### Příklady

Existuje několik způsobů, jak lze v jazyce SP-Lang zadat seznam:

!!! example
	```yaml

	!LIST
	- "One"
	- "Two"
	- "Three"
	- "Four"
	- "Five"
	```

!!! example

	Implicitní seznam pomocí [sekvencí bloků YAML](https://yaml.org/spec/1.2.2/#821-block-sequences):

	```yaml
	- "One"
	- "Two"
	- "Three"
	- "Four"
	- "Five"
	```

!!! example

	Implicitní seznam pomocí [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):

	```yaml

	["One", "Dvě", "Three", "Four", "Five"]
	```

!!! example

	Formou mapování:

	```yaml
	!LIST
	with:
	- "One"
	- "Two"
	- "Three"
	- "Four"
	- "Five"
	```

--- 

## `!GET`: Získá položku ze seznamu 

Typ: _Mapping_.


### Synopsis

```yaml

!GET
what: <index of the item in the list>
z: <list>
```

`index` je celé číslo (číslo).

`index` může být záporný, v tom případě určuje položku od konce seznamu.
Položky jsou indexovány od 0, to znamená, že první položka v seznamu má index 0.

Pokud je `index` mimo hranice seznamu, příkaz se vrátí s chybou.


!!! example "Příklad"

	```yaml

	!GET
	what: 3
	from:
	!LIST
	- 1
	- 5
	- 30
	- 50
	- 80
	- 120
	```

	Vrací hodnotu `50`.

!!! example "Příklad"

	```yaml

	!GET
	what: -1
	od:
	!LIST
	- 1
	- 5
	- 30
	- 50
	- 80
	- 120
	```

	Vrací poslední položku seznamu, která je `120`.

