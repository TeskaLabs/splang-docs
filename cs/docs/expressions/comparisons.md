---
git_commit_hash: b55fa3f
title: Porovnávací
---

# Porovnávací výrazy

Testovací výraz vyhodnotí vstupy a na základě výsledku testu vrátí logickou hodnotu `true` nebo `false`.

---

## `!EQ`: Rovná se 

!!! example "Příklad"

	```yaml
	!EQ
	- !ARG count
	- 3
	```
	
	Porovnává argument `count` s `3`, vrací `count == 3`.


---

## `!NE`: Nerovná se

Typ: _Sequence_.

Jedná se o zápornou obdobu `!EQ`.

!!! example "Příklad"

	```yaml
	!NE
	- !ARG name
	- Frodo
	```

	Porovnává argument `name` s `Frodo`, vrací `name != Frodo`.

---

## `!LT`: Menší než

Typ: _Sequence_.

!!! example "Příklad"

	```yaml
	!LT
	- !ARG count
	- 5
	```
	
	Příklad testu `count < 5`.
	
	

---

## `!LE`: Menší nebo rovno

Typ: _Sequence_.

!!! example "Příklad"

	```yaml
	!LE
	- 2
	- !ARG počet
	- 5
	```
	
	Příklad testu rozsahu `2 <= count <= 5`.


---

## `!GT`: Větší než 

Typ: _Sequence_.

!!! example "Příklad"

	```yaml
	!GT [!ARG count, 5]
	```
	
	Příklad testu `count >  5` pomocí kompaktní formy YAMLu.

---

## `!GE`: Větší nebo rovno

Typ: _Sequence_.

!!! example "Příklad"

	```yaml
	!GT
	- !ARG count
	- 5
	```
	
	Příklad testu `count >= 5`.

---

## `!IN`: Test výskytu

Typ: _Mapping_.

```yaml
!IN
what: <...>
where: <...>
```

Výraz `!IN` se používá ke kontrole, zda hodnota se `what` vyskytuje v hodnotě `where`, nebo ne.
Jako hodnotu `where` lze uvést řetězec, kontejner (seznam, množina, slovník), strukturní typ atd.
Vyhodnotí se na `true`, pokud najde hodnotu `what` v zadané hodnotě `where`, a na `false` v opačném případě.

!!! example "Příklad"

	```yaml
	!IN
	what: 5
	where:
	  - 1
	  - 2
	  - 3
	  - 4
	  - 5
	```
	
	Zkontroluje přítomnost hodnoty `5` v seznamu `where`. Vrátí `true`.


!!! example "Příklad"

	```yaml
	!IN
	what: "Willy"
	where: "John Willy Boo"
	```
	
	Zkontroluje přítomnost podřetězce `Willy` v hodnotě `John Willy Boo`. Vrátí `true`.

