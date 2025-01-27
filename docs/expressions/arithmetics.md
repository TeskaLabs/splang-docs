---
title: Arithmetic
---

# Arithmetic expressions

## Overview

Arithmetic expressions are used for basic arithmetic operations with data.

* [`!ADD`](#add): Addition
* [`!SUB`](#sub): Subtraction
* [`!MUL`](#mul): Multiplication
* [`!DIV`](#div): Division
* [`!MOD`](#mod): Modulo (remainder after division)
* [`!POW`](#pow): Exponentiation
* [`!ABS`](#abs): Absolute value


---

## `!ADD`

Type: _Sequence_

You can add following types:

 * Numbers (Integers and floats)
 * Strings
 * Lists
 * Sets
 * Tuples
 * Records

!!! example

    ```yaml
    !ADD
    - 4
    - -5
    - 6
    ```

    Calculates `4+(-5)+6`, the result is `5`.

---

## `!SUB`

Type: _Sequence_

!!! example

    ```yaml
    !SUB
    - 3
    - 1
    - -5
    ```

    Calculates `3-1-(-5)`, the result is `7`.

---


## `!MUL`

Type: _Sequence_

!!! example

    ```yaml
    !MUL
    - 7
    - 11
    - 13
    ```

    Calculates `7*11*13`, the result is `1001` (which happens to be the [Scheherazade constant](https://en.wikipedia.org/wiki/Scheherazade)).

---

## `!DIV`

Type: _Sequence_

!!! example

    ```yaml
    !DIV
    - 21
    - 1.5
    ```

    Calculates `21/5`, the result is `14.0`.


### Division by zero

Division by zero produces the error, which can cascade thru the expression.

`!TRY` expression can be used to handle this situation.
The first item in `!TRY` is a `!DIV` that can produce division by zero error.
The second item is a value that will be returned when such an error occurs.

```yaml
!TRY
- !DIV
  - !ARG input
  - 0.0
- 5.0
```

---

## `!MOD`

Type: _Sequence_

Calculate the signed remainder of a division (aka modulo operation).

!!! info

	Read more about [modulo](https://en.wikipedia.org/wiki/Remainder) on Wikipedia.

!!! example

    ```yaml
    !MOD
    - 21
    - 4
    ```

    Calculates `21 mod 4`, the result is `1`.

!!! example

	```yaml
	!MOD
	- -10
	- 3
	```

	Calculates `-10 mod 3`, the result is `2`.

---

## `!POW`

Type: _Sequence_


Calculate the exponent.

!!! example

    ```yaml
    !POW
    - 2
    - 8
    ```

    Calculates `2^8`, the result is `16`.

---

## `!ABS`

Type: _Mapping_

```yaml
!ABS
what: <x>
```

Calculate the absolute value of input `x`, which is the non-negative value of  `x` without regard to its sign.

!!! example

    ```yaml
    !ABS
    what: -8.5
    ```

    The result is a value `8.5`.
