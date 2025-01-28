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
* [!IN](#in): Membership test

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
    !GT
    - !ARG count
    - 5
    ```

    Example of a `count >= 5` test.


---

## `!IN`

Membership test.

Type: _Mapping_.

```yaml
!IN
what: <...>
where: <...>
```

The `!IN` expression is used to check if a value `what` exists in a value `where` or not.
Value `where` is a string, container (list, set, dictionary), structural type etc.
Evaluate to `true` if it finds a value `what` in the specified value `where` and `false` otherwise.

!!! example

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

    Check for a presence of the value `5` in the list `where`. Returns "true".


!!! example

    ```yaml
    !IN
    what: "Willy"
    where: "John Willy Boo"
    ```

    Check for a presence of the substring "Willy" in the `John Willy Boo` value. Returns `true`.
