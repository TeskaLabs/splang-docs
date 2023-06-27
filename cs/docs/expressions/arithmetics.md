---
git_commit_hash: b55fa3f
title: Aritmetické
---

# Aritmetické výrazy


---

## `!ADD`: Sčítání 

Typ: _Sequence_


Výraz je definovaný pro následující typy:

 * Čísla (celá čísla a desetinná čísla)
 * Řetězce
 * Seznamy
 * Množiny
 * Tuples
 * Records (záznamy)


!!! example "Příklad"

	```yaml
	!ADD
	- 4
	- -5
	- 6
	```
	
	Vypočítá `4+(-5)+6`, výsledek je `5`.

---

## `!SUB`: Odčítání

Typ: _Sequence_

!!! example "Příklad"

	```yaml
	!SUB
	- 3
	- 1
	- -5
	```
	
	Vypočítá `3-1-(-5)`, výsledkem je `7`.

---


## `!MUL`: Násobení 

Typ: _Sequence_

!!! example "Příklad"

    ```yaml
    !MUL
    - 7
    - 11
    - 13
    ```
	
	Vypočítá `7*11*13`, výsledkem je `1001` (což je shodou okolností [Šahrazádino číslo](https://cs.wikipedia.org/wiki/Tis%C3%ADc_a_jedna_noc)).

---

## `!DIV`: Dělení

Typ: _Sequence_

!!! example "Příklad"

	```yaml
	!DIV
	- 21
	- 1.5
	```
	
	Vypočítá `21/1.5`, výsledkem je `14.0`.
	

### Dělení nulou

Dělení nulou vede k chybě, která se může kaskádovitě projevit ve výrazu.

Pro řešení této situace lze použít výraz `!TRY`.
První položkou výrazu `!TRY` je `!DIV`, který může způsobit chybu dělení nulou.
Druhou položkou je hodnota, která bude vrácena, pokud k takové chybě dojde.
```yaml

!TRY
- !DIV
  - !ARG input
  - 0.0
- 5.0
```

---

## `!MOD`: Zbytek po dělení (modulo)

Typ: _Sequence_

Vypočítá znaménkový zbytek dělení (neboli výsledek operace modulo).

!!! info

	Více informací o operaci [modulo](https://cs.wikipedia.org/wiki/Zbytek_po_d%C4%9Blen%C3%AD) na Wikipedii.

!!! example "Příklad"

	```yaml
	!MOD
	- 21
	- 4
	```

	Vypočítá `21 mod 4`, výsledkem je `1`.

!!! example "Příklad"

	```yaml
	!MOD
	- -10
	- 3
	```

	Vypočítá `-10 mod 3`, výsledkem je `2`.

---

## `!POW`: Exponentiation 

Typ: _Sequence_

Výpočet exponentu.

!!! example "Příklad"

	```yaml
	!POW
	- 2
	- 8
	```
	
	Vypočítá `2^8`, výsledkem je `16`.

---

## `!ABS`: Absolutní hodnota

Typ: _Mapping_

```yaml

!ABS
what: <x>
```

Vypočítá absolutní hodnotu vstupu `x`, což je nezáporná hodnota `x` bez ohledu na její znaménko.

!!! example "Příklad"

	```yaml
	!ABS
	co: -8,5
	```
	
	Výsledkem je hodnota `8.5`.

