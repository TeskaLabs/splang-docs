---
title: Arithmetics
---

# Arithmetics expressions


---

## `!ADD`: Addition 

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

## `!SUB`: Substraction 

Type: _Sequence_

!!! example

    ```yaml
    !SUB
    - 3
    - 1
    - -5
    ```

---


## `!MUL`: Multiplication 

Type: _Sequence_

!!! example

    ```yaml
    !MUL
    - 1.5
    - 5.5
    - 3.2
    ```

---

## `!DIV`: Division 

Type: _Sequence_

!!! example

    ```yaml
    !DIV
    - 21
    - 1.5
    ```


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

## `!MOD`: Reminder 

Type: _Sequence_


Calculate the signed remainder of a division (aka modulo operation).

!!! example

    ```yaml
    !MOD
    - 21
    - 1.5
    ```

---

## `!POW`: Exponentiation 

Type: _Sequence_


Calculate the exponent or power.

!!! example

    ```yaml
    !POW
    - 2
    - 8
    ```

---

## `!ABS`: Absolute value

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
