---
title: Comparisons
---

# Comparisons expressions

## Overview


Test expression evaluates inputs and returns boolean value `true` or `false` based on the result of the test.

* [!EQ](#eq): Equal
* [!NE](#ne): Not equal
* [!LT](#lt): Less than
* [!LE](#le): Less than or equal to
* [!GT](#gt): Greater than
* [!GE](#ge): Greater than or equal to

---

## `!EQ`

Equal to.

Type: _Sequence_.

!!! example

    ```yaml
    !EQ
    - !ARG count
    - 3
    ```

    This compares `count` argument with `3`, returns `count == 3`

---

## `!NE`

Not equal to.

Type: _Sequence_.

This is negative counterpart to `!EQ`.


!!! example

    ```yaml
    !NE
    - !ARG name
    - Frodo
    ```

    This compares `name` argument with `Frodo`, returns `name != Frodo`.

---

## `!LT`

Less than.

Type: _Sequence_.

!!! example

    ```yaml
    !LT
    - !ARG count
    - 5
    ```

    Example of a `count < 5` test.


---

## `!LE`

Less than or equal to.

Type: _Sequence_.


!!! example

    ```yaml
    !LE
    - 2
    - !ARG count
    - 5
    ```

    Example of a range `2 <= count <= 5` test.


---

## `!GT`

Greater than.

Type: _Sequence_.

!!! example

    ```yaml
    !GT [!ARG count, 5]
    ```

    Example of a `count > 5` test using a compacted YAML form.


---

## `!GE`

Greater than or equal to.

Type: _Sequence_.

!!! example

    ```yaml
    !GE
    - !ARG count
    - 5
    ```

    Example of a `count >= 5` test.


---
