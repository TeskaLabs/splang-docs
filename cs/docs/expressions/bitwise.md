---
git_commit_hash: b55fa3f
title: Bitové
---

# Bitové operace

Bitové posuny ("bit shifts") zachází s hodnotou jako se sérií bitů, umožňuje přesunout nebo posunout binární číslice doleva nebo doprava.


Existují také bitové výrazy `!AND`, `!OR` a `!NOT`, viz kapitolu [Logické výrazy](../logic).

---

## `!SHL`: Logický posun doleva 

Typ: _Mapping_.

```yaml
!SHL
what: <...>
by: <...>
```

!!! tip

	Levý posun lze použít jako rychlé násobení čísly 2, 4, 8 atd.

!!! example "Příklad"

	```yaml
	!SHL
	what: 9
	by: 2
	```

	`9` je reprezentovaná binární hodnotou `1001`. Levý logický posun posune bity doleva o 2 pozice. Výsledkem je `100100`, což je v desítkovém zápise `36`. To je  `9 * (2^2)`. To je stejný výsledek jako `9 * (2^2)`.
	

---

## `!SHR`: Logický posun doprava 

Typ: _Mapping_.

```yaml

!SHR
what: <...>
by: <...>
```

!!! tip

	Pravý posun lze použít jako rychlé dělení čísly 2, 4, 8 atd.


!!! example "Příklad"

	```yaml
	!SHR
	what: 16
	by: 3
	```

	`16` je reprezentovaná `10000`. Logický posun posune bity doprava o `3`. Výsledkem je `10`, tedy `2` v desítkovém zápisu. To je stejný výsledek jako `16 / (2^3)`.

--- 

## `!SAL`: Aritmetický posun doleva

Typ: _Mapping_.

```yaml
!SAL
what: <...>
by: <...>
```

!!! example "Příklad"

	```yaml
	!SAL
	what: 60
	by: 2
	```


---

## `!SAR`: Pravý aritmetický posun 

Typ: _Mapping_.
```yaml

!SAR
what: <...>
by: <...>
```


---

## `!ROL`: Kruhový posun doleva 

Typ: _Mapping_.
```yaml

!ROL
what: <...>
by: <...>
```


---

## `!ROR`: Kruhový posun doprava

Typ: _Mapping_.
```yaml

!ROR
what: <...>
by: <...>
```
