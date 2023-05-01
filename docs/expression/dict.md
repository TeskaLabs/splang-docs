---
title: Dictionary expression
---

# Dictionary expression


* This will become a table of contents (this text will be scrapped).
{:toc}

The dict (aka dictionary) store a collection of (key, value) pairs, such that each possible key appears at most once in the collection.
Keys in the dictionary must be of the same type as well as values.
The set is one of basic data structures provided by SP-Lang.

An item is a (key, value) pair, represented as a tuple.

Hint: You may know this structure under alernative names "associative array" or "map".

--- 

## `!DICT`: Dictionary 

Type:  _Mapping_

### Synopsis

```yaml
!DICT
with:
  <key1>: <value1>
  <key2>: <value2>
  <key3>: <value3>
  ...
```

_Hint: Use `!COUNT` to determine number of items in the dictionary._


### Examples

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

Consise dictionary using `!!dict` and YAML flow style:

```yaml
!!dict {key1: "One", key2: "Two", key3: "Three"}
```

### Type specification

The type of dictionary is denoted as `{Tk:Tv}`, where `Tk` is a type of the key and `Tv` is a type of value.
For more info about the dictionary type, continue to the relevant chapter in a [type system](../language/type-system#dictionary).

The dictionaty will try to infere its type based on the items added.
The type of the first item will likely provide the key type `Tk` and the value type `Tv`.
If the dictionary is empty, its infered type is `{str:si64}`.

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

`type` is an optional argument containing a string with the dictionary signature.
This signature will be used for this signature instead of type inference from childs.

In the above example, the type of the dictionary is `{str:any}`, the type of key is `str` and the type of values is `any`.


--- 

## `!GET`: Get the value from a dictionary 

Type: _Mapping_.


### Synopsis

```yaml
!GET
what: <key>
from: <dict>
default: <value>
```

Get the item from the `dict` (dictionary) identified by the `key`.

If the `key` is not found, return `default` or error if `default` is not provided.
`default` is optional.

### Examples

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

## `!IN`: Membership test 

Type: _Mapping_.

### Synopsis

```yaml
!IN
what: <key>
where: <dict>
```

Check if `key` is present in the `dict`.

Note: The expression `!IN` is described in the "Tests" chapter.

### Example

```yaml
!IN
what: 3
where:
  !DICT
  with:
    1: "One"
    2: "Two"
    3: "Three"
```
