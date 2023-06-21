---
git_commit_hash: b55fa3f
title: Aritmetika
---

# Aritmetické výrazy


---

## `!ADD`: Sčítání 

Typ: _Sequence_


Můžete přidat následující typy:

 * Čísla (celá čísla a floaty)
 * Řetězce
 * seznamy
 * Sady
 * Tuply
 * Záznamy


!!! example

	
	
	```yaml
	!ADD
	- 4
	- -5
	- 6
	```
	

  Vypočítá `4+(-5)+6`, výsledek je `5`.

---

## `!SUB`: SUB: 

Typ: _Sequence_


!!! example

	
	
	```yaml
	!SUB
	- 3
	- 1
	- -5
	```
	

---


## `!MUL`: Násobení 

Typ: _Sequence_


!!! example

	
	
	```yaml
	!MUL
	- 1.5
	- 5.5
	- 3.2
	```
	

---

## `!DIV`: Division 

Typ: DIV _Sequence_


!!! example

	
	
	```yaml
	!DIV
	- 21
	- 1.5
	```
	
	

### Dělení nulou

Dělení nulou vede k chybě, která se může kaskádovitě projevit ve výrazu.

Pro řešení této situace lze použít výraz `!TRY`.
První položkou výrazu `!TRY` je `!DIV`, který může způsobit chybu dělení nulou.
Druhou položkou je hodnota, která bude vrácena, pokud k takové chybě dojde.
```yaml

!TRY
- !DIV
  - !ARG vstup
  - 0.0
- 5.0
```


---

## `!MOD`: Připomínka 

Typ: _Sequence_


Vypočítá znaménkový zbytek dělení (neboli operace modulo).


!!! example

	
	
	```yaml
	!MOD
	- 21
	- 1.5
	```
	

---

## `!POW`: Exponentiation 

Typ: _Sequence_


Výpočet exponentu.


!!! example

	
	
	```yaml
	!POW
	- 2
	- 8
	```
	

---

## `!ABS`: Absolutní hodnota

Typ: _Mapování_
```yaml

!ABS
co: <x>
```

Vypočítejte absolutní hodnotu vstupu `x`, což je nezáporná hodnota `x` bez ohledu na její znaménko.

!!! example

	
	
	```yaml
	
	!ABS
	co: -8,5
	```
	
	Výsledkem je hodnota `8,5`.

