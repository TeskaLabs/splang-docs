---
title: Dictionary
---

# Dictionary expressions

## Overview

The **dict** (aka dictionary) store a collection of (key, value) pairs, such that each possible key appears at most once in the collection.
Keys in the dictionary must be of the same type as well as values.

An item is a (key, value) pair, represented as a tuple.

!!! Hint

    You may know this structure under alternative names "associative array" or "map".

* [`!DICT`](#dict): Dictionary.
* [`!DICT.FORMAT`](#dictformat): Format a dictionary into a string.
* [`!GET`](#get): Get the value from a dictionary.
* [`!IN`](#in): Membership test.

---

## `!DICT`

Dictionary.

Type:  _Mapping_

```yaml
!DICT
with:
  <key1>: <value1>
  <key2>: <value2>
  <key3>: <value3>
  ...
```

!!! hint

    Use [`!COUNT`](./aggregate.md#count) to determine number of items in the dictionary.

!!! example

    There are several ways, how a dictionary can be specified in SP-Lang:

    ```yaml
    !DICT
    with:
      key1: "One"
      key2: "Two"
      key3: "Three"
    ```

    Implicit dictionary:

    ```yaml
    ---
    key1: "One"
    key2: "Two"
    key3: "Three"
    ```

    Concise dictionary using `!!dict` and YAML flow style:

    ```yaml
    !!dict {key1: "One", key2: "Two", key3: "Three"}
    ```

### Type specification

The type of dictionary is denoted as `{Tk:Tv}`, where `Tk` is a type of the key and `Tv` is a type of value.
For more info about the dictionary type, continue to the relevant chapter in a [type system](../language/types/index.md#dictionary).

The dictionary will try to infer its type based on the items added.
The type of the first item will likely provide the key type `Tk` and the value type `Tv`.
If the dictionary is empty, its inferred type is `{str:si64}`.

You can override this by using the explicit type specification:

```yaml
!DICT
type: "{str:any}"
with:
  <key1>: <value1>
  <key2>: <value2>
  <key3>: <value3>
  ...
```

`type` is an optional argument containing a string with the dictionary signature that will be used instead of type inference from children.

In the above example, the type of the dictionary is `{str:any}`, the type of key is `str` and the type of values is `any`.

---

## `!GET`

Get the value from a dictionary.

Type: _Mapping_.


```yaml
!GET
what: <key>
from: <dict>
```

Get the item from the `dict` (dictionary) identified by the `key`.

If the `key` is not found, the expression returns `None` (error).


!!! example

    ```yaml
    !GET
    what: 3
    from:
      !DICT
      with:
        1: "One"
        2: "Two"
        3: "Three"
    ```

    Returns `Three`.

---

## `!IN`

Membership test.

Type: _Mapping_.

```yaml
!IN
what: <key>
where: <dict>
```

Check if a `key` is present in the `where` value.

The expression `!IN` works on dict-like values that support membership, such as the current event (`!EVENT`) or a parsed JSON document.
It is not supported on a native `!DICT` structure.

---

## `!DICT.FORMAT`

Format a dictionary into a string.

Type: _Mapping_.

Synopsis:

```yaml
!DICT.FORMAT
what: <dict>
type: <format>
fields:
  - <field1>
  - <field2>
```

- `type` is optional (default: `kvs`). Supported values:
  * `kvs` — `key=value` pairs separated by spaces
  * `kvdqs` — `key="value"` pairs separated by spaces
  * `cef` — CEF-style `key="value"` or `key=value` pairs
  * `qs` — URL query string
- `fields` is optional. When provided, only the listed fields are formatted.

!!! example

    ```yaml
    !DICT.FORMAT
    what: !EVENT
    type: kvs
    fields:
      - message
    ```
