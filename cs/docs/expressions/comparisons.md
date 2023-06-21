---
git_commit_hash: b55fa3f
title: Srovnání
---

# Porovnávací výrazy


Testovací výraz vyhodnotí vstupy a na základě výsledku testu vrátí logickou hodnotu `pravda` nebo `nepravda`.

---

## `!EQ`: Rovná se 


!!! example

	
	
	```yaml
	
	!EQ
	- !ARG počet
	- 3
	```
	
	Porovná argument `count` s `3`.
	
	

---

## `!NE`: Není rovno 

Typ: _Sequence_.

Jedná se o zápornou obdobu `!EQ`.



!!! example

	
	
	```yaml
	!NE
	- !ARG název
	- Frodo
	```
	
	

---

## `!LT`: Méně než 

Typ: _Sequence_.

!!! example

	
	
	```yaml
	
	!LT
	- !ARG počet
	- 5
	```
	
	Příklad testu `count &lt; 5`.
	
	

---

## `!LE`: Méně než a rovno 

Typ: _Sequence_.


!!! example

	
	
	```yaml
	
	!LE
	- 2
	- !ARG počet
	- 5
	```
	
	Příklad testu rozsahu `2 &lt;= count &lt;= 5`.
	
	

---

## `!GT`: Větší než 

Typ: _Sequence_.

!!! example

	
	
	```yaml
	
	!GT [!ARG count, 5]
	```
	
	Příklad testu `count &gt; 5` pomocí zhuštěného tvaru YAML.
	
	

---

## `!GE`: Větší než a rovná se 

Typ: _Sequence_.

!!! example

	
	
	```yaml
	
	!GT
	- !ARG počet
	- 5
	```
	
	Příklad testu `count &gt;= 5`.
	
	

---

## `!IN`: Test členství 

Typ: _Mapping_.
```yaml

!IN
co: <...>
kde: <...>
```

Výraz `!IN` se používá ke kontrole, zda hodnota `what` existuje v hodnotě `where`, nebo ne.
Hodnota `where` je řetězec, kontejner (seznam, množina, slovník), strukturní typ atd.
Vyhodnotí se na "true", pokud najde hodnotu `what` v zadané hodnotě `where`, a na false v opačném případě.

!!! example

	
	
	```yaml
	
	!IN
	co: 5
	kde:
	  - 1
	  - 2
	  - 3
	  - 4
	  - 5
	```
	
	Zkontroluje přítomnost hodnoty `5` v seznamu `where`. Vrací hodnotu "true".
	
	

!!! example

	
	
	```yaml
	
	!IN
	co: "Willy"
	kde: "John Willy Boo"
	```
	
	Zkontroluje přítomnost podřetězce "Willy" v hodnotě `where`. Vrací hodnotu "true".

