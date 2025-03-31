---
title: Funkce
---

# Výrazy pro funkce

## Přehled

* [`!ARGUMENT`, `!ARG`](#argument-arg): Získá argument funkce.
* [`!FUNCTION`, `!FN`](#function-fn): Definuje novou funkci.
* [`!SELF`](#self): Aplikuje aktuální funkci, používá se pro rekurzi.

---

## `!ARGUMENT`, `!ARG`

Umožňuje přístup k argumentu `name`.

Typ: _Scalar_.

Synopsis:

```yaml
!ARGUMENT name
```

nebo

```yaml
!ARG name
```

!!! tip

    `!ARG` je zkrácená verze `!ARGUMENT`.

---

## `!FUNCTION`, `!FN`

Výraz `!FUNCTION` definuje novou funkci.
Obvykle se používá jako top-level expression.

Typ: _Mapping_.

!!! info

    Výrazy SP-Lang jsou _implicitně_ umístěné definice funkcí.
    To znamená, že ve většině případů lze `!FUNCTION` přeskočit a je uvedena pouze sekce `do`.

Synopsis:

```yaml
!FUNCTION
name: <název funkce>
arguments:
  arg1: <typ>
  arg2: <typ>
  ...
returns: <typ>
schemas: <slovník schémat>
do:
  <výraz>
```

!!! tip

    `!FN` je zkrácená verze `!FUNCTION`.

!!! example

    ```yaml
    !FUNCTION
    arguments:
      a: si64
      b: si32
      c: si32
      d: si32
    returns: fp64
    do:
      !MUL
      - !ARGUMENT a
      - !ARGUMENT b
      - !ARGUMENT c
      - !ARGUMENT d
    ```

    Tento výraz definuje funkci, která přijímá čtyři argumenty (`a`, `b`, `c` a `d`) s příslušnými datovými typy (`si64`, `si32`, `si32` a `si32`) a vrací výsledek typu `fp64`.
    Funkce vynásobí čtyři vstupní argumenty (`a`, `b`, `c` a `d`) a vrátí součin jako číslo s desetinou čárkou (`fp64`).

---

## `!SELF`

Příkaz `!SELF` umožňuje rekurzivně použít "self" alias aktuální funkci.

Typ: _Mapping_.

Synopsis:

```yaml
!SELF
arg1: <hodnota>
arg2: <hodnota>
...
```

!!! note

    Výraz `!SELF` je tzv. [Y kombinátor](https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator).

!!! example

    ```yaml
    !FUNCTION
    arguments: {x: int}
    returns: int
    do:
      !IF # hodnota <= 1
        test: !GT [!ARG x, 1]
        then: !MUL [!SELF {x: !SUB [!ARG x, 1]}, !ARG x]
       else: 1
    ```

    Tento výraz definuje rekurzivní funkci, která přijímá jeden celočíselný argument `x` a vrací celočíselný výsledek.
    Funkce vypočítá faktoriál vstupního argumentu `x` pomocí příkazu if-else.
    Pokud je vstupní hodnota `x` větší než 1, funkce vynásobí `x` faktoriálem (`x` - 1), který vypočítá rekurzivním voláním sebe sama.
    Pokud je vstupní hodnota `x` menší nebo rovna 1, funkce vrátí 1.