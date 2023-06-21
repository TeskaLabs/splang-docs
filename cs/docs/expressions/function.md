---
git_commit_hash: b55fa3f
title: Funkce
---

# Výrazy funkcí



--- 

## `!ARGUMENT`, `!ARG`: Získat argument funkce  

Typ: _Scalar_.

### Synopse
```yaml

!ARGUMENT name
```
```yaml

!ARG name
```

Umožňuje přístup k argumentu `name`.

!!! tip

	
	
	
	`!ARG` je stručnou verzí `!ARGUMENT`.
	
	

--- 

## `!FUNCTION`, `!FN`: Definice funkce 


Výraz `!FUNCTION` definuje novou funkci.
Obvykle se používá jako výraz nejvyšší úrovně.

Typ: _Mapování_.


!!! info

	
	
	
	Výrazy SP-Lang jsou _implicitně_ umístěné definice funkcí.
	To znamená, že ve většině případů lze `!FUNCTION` přeskočit a je uvedena pouze sekce `do`.
	
	

### Synopse
```yaml

!FUNCTION
name: <name of function>
argumenty:
  argument1: <type>
  arg2: <type>
  ...
vrací: <type>
schémata: Argumenty: Argumenty: Argumenty: Argumenty: Argumenty: arg: <dictionary of schemas>
do:
 <expression>
```

!!! tip

	
	
	
	`!FN` je zkrácená verze `!FUNCTION`.
	
	

### Příklad
```yaml

!FUNCTION
argumenty:
  a: si64
  b: si32
  c: si32
  d: si32
vrací: fp64
do:
  !MUL
  - !ARGUMENT a
  - !ARGUMENT b
  - !ARGUMENT c
  - !ARGUMENT d
```

Tento výraz definuje funkci, která přijímá čtyři argumenty (`a`, `b`, `c` a `d`) s příslušnými datovými typy (`si64`, `si32`, `si32` a `si32`) a vrací výsledek typu `fp64`.
Funkce vynásobí čtyři vstupní argumenty (`a`, `b`, `c` a `d`) a vrátí součin jako číslo s pohyblivou řádovou čárkou (`fp64`).

--- 

## `!SELF`: Použijte aktuální funkci  

Příkaz `!SELF` umožňuje rekurzivně použít "self" alias aktuální funkci.

Typ: _Mapování_.

### Synopse
```yaml

!SELF
arg1: <value>
arg2: <value>
...
```

!!! note

	
	
	
	Výraz `!SELF` je kombinátor [Y](https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator).
	
	

### Příklad

```yaml

!FUNCTION
argumenty: {x: int}
vrací: int
do:
  !IF # hodnota &lt;= 1
  test: !GT [!ARG x, 1]
  potom: !MUL [!SELF {x: !SUB [!ARG x, 1]}, !ARG x]
  else: 1
```

Tento výraz definuje rekurzivní funkci, která přijímá jeden celočíselný argument `x` a vrací celočíselný výsledek.
Funkce vypočítá faktoriál vstupního argumentu `x` pomocí příkazu if-else.
Pokud je vstupní hodnota `x` větší než 1, funkce vynásobí `x` faktoriálem (`x` - 1), který vypočítá rekurzivním voláním sebe sama.
Pokud je vstupní hodnota `x` menší nebo rovna 1, funkce vrátí 1.
