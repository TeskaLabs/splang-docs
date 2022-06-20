---
layout: default
title: SP-Lang documentation
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

## `!DICT`: Dictionary {#EXPR-DICT}

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


--- 

## `!GET`: Get the value from a dictionary {#EXPR-DICT-GET}

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

## `!IN`: Membership test {#EXPR-DICT-IN}

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
