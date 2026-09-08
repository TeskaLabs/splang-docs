---
title: Set
---

# Set expressions

## Overview

The set store unique items, without any particular order.
Items in the set must be of the same type.
The set is one of basic data structures provided by SP-Lang.

A set is best suited for a testing value for membership rather than retrieving a specific element from a set.

* [`!SET`](#set): Set of items.
* [`!IN`](#in): Membership test.

---

## `!SET`

Set of items.

Type:  _Implicit sequence_, _Mapping_.

Synopsis:

```yaml
!SET
- ...
- ...
```

!!! hint

    Use `!COUNT` to determine number of items in the set.

There are several ways, how a set can be specified in SP-Lang:

!!! example

    ```yaml
    !SET
    - "One"
    - "Two"
    - "Three"
    - "Four"
    - "Five"
    ```

!!! example "Unordered set"

    [YAML unordered set](https://yaml.org/spec/1.2.2/#example-unordered-sets):

    ```yaml
    !!set
    ? Yellow pork
    ? Pink grass
    ? White snow
    ```

!!! example "YAML flow sequences"

    Concise set using [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):

    ```yaml
    !SET ["One", "Two", "Three", "Four", "Five"]
    ```

!!! example
    The mapping form:

    ```yaml
    !SET
    with:
    - "One"
    - "Two"
    - "Three"
    - "Four"
    - "Five"
    ```

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

The `!IN` expression is described for the individual container types in the following chapters:

- [List](./list.md#in)
- [Dictionary](./dict.md#in)
- [String](./string.md#in)
- [Lookup](./lookup.md#in)

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

    Check for a presence of the value `5` in the list `where`. Returns `true`.


!!! example

    ```yaml
    !IN
    what: "Willy"
    where: "John Willy Boo"
    ```

    Check for a presence of the substring "Willy" in the `John Willy Boo` value. Returns `true`.

!!! example

    ```yaml
    !IN
    what: 3
    where:
      !SET
      with:
        - 1
        - 2
        - 5
        - 8 
    ```

    Check for a presence of the value `3` in the set `where`. Returns `false`.
