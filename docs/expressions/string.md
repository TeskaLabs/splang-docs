---
title: String
---

# String expressions

## Overview

* [`!IN`](#in): Tests if a string contains a substring.
* [`!STARTSWITH`](#startswith): Tests whether a string starts with a selected prefix.
* [`!ENDSWITH`](#endswith): Tests whether a string ends with a selected suffix.
* [`!SUBSTRING`](#substring): Extracts part of a string.
* [`!LOWER`](#lower), [`!UPPER`](#upper): Transforms a string into lowercase / uppercase.
* [`!CUT`](#cut): Cuts the string and returns a selected part.
* [`!SPLIT`](#split), [`!RSPLIT`](#rsplit): Splits a string into a list.
* [`!JOIN`](#join): Joins a list of strings.
* [`!LDAP.SID`](#ldapsid): Converts ldap bytes to ldap sid string.

---

## `!IN`

The `!IN` expression is used to check if a string `what` exists in a string `where` or not.

Type: _Mapping_.

Synopsis:

```yaml
!IN
what: <...>
where: <...>
```

Evaluate to `true` if it finds a substring `what` in the string `where` and false otherwise.


!!! example

    ```yaml
    !IN
    what: "Willy"
    where: "John Willy Boo"
    ```

    Check for a presence of the substring "Willy" in the `where` value. Returns `true`.


### Multi-string variant

There is a special variant on `!IN` operator for checking if any of strings provided in `what` value (a list in this case) is in the string. It is efficient, optimized implementation of the multi-string matcher.

```yaml
!IN
what:
  - "John"
  - "Boo"
  - "ly"
where: "John Willy Boo"
```

This is very efficient way of checking if at least one substring is present in the `where` string.
It provides [Incremental String Matching](http://se.ethz.ch/~meyer/publications/string/string_matching.pdf) algorithm for fast pattern matching in strings.
It makes it an ideal tool for complex filtering as a standalone bit or an optimization technique.

!!! example "Example of `!REGEX` optimization by multi-string `!IN`:"

    ```yaml
        !AND
        - !IN
          where: !ARG message
          what:
          - "msgbox"
          - "showmod"
          - "showhelp"
          - "prompt"
          - "write"
          - "test"
          - "mail.com"
        - !REGEX
          what: !ARG message
          regex: "(msgbox|showmod(?:al|eless)dialog|showhelp|prompt|write)|(test[0-9])|([a-z]@mail\.com)
    ```

This approach is recommended from applications in streams, where you need to filter an extensive amount of the data with assumption that only a smaller portion of the data matches the patters.
An application of the `!REGEX` expression directly will slow processing down significantly, because it is complex regular expression.
The idea is to "pre-filter" data with a simpler but faster condition so that only a fraction of the data reaches the expensive `!REGEX`.
The typical performance improvement is 5x-10x.

For that reason, the `!IN` must be a perfect superset of the `!REGEX`, it means:

* `!IN` -> `true`, `!REGEX` -> `true`: `true`
* `!IN` -> `true`, `!REGEX` -> `false`: `false` (this should be a minority of cases)
* `!IN` -> `false`, `!REGEX` -> `false`: `false` (prefiltering, this should be a majority of cases)
* `!IN` -> `false`, `!REGEX` -> `true`: this combination MUST BE avoided, adopt the `!IN` and/or `!REGEX` accordingly.

---

## `!STARTSWITH`

Returns `true` if `what` string begins with `prefix`.

Type: _Mapping_

Synopsis:

```yaml
!STARTSWITH
what: <...>
prefix: <...>
```


!!! example

    ```yaml
    !STARTSWITH
    what: "FooBar"
    prefix: "Foo"
    ```

### Multi-string variant

!!! warning "Work in progress"

    Not implemented yet.


```yaml
!STARTSWITH
what: <...>
prefix: [<prefix1>, <prefix2>, ...]
```

In multi-string variant, a list of strings is defined.
The expression evaluates to `true` if at least one prefix string matches the start of the `what` string.


---

## `!ENDSWITH`

Returns `true` if `what` string ends with `postfix`.

Type: _Mapping_

Synopsis:

```yaml
!ENDSWITH
what: <...>
postfix: <...>
```


!!! example

    ```yaml
    !ENDSWITH
    what: "autoexec.bat"
    postfix: ".bat"
    ```

### Multi-string variant

!!! warning "Work in progress"

    Not implemented yet.


```yaml
!ENDSWITH
what: <...>
postfix: [<postfix1>, <postfix2>, ...]
```

In multi-string variant, a list of strings is defined.
The expression evaluates to `true` if at least one postfix string matches the end of the `what` string.


---

## `!SUBSTRING`

Return part of the string `what`, in between `from` and `to` index.

Type: _Mapping_


Synopsis:

```yaml
!SUBSTRING
what: <...>
from: <...>
to: <...>
```

!!! info

    The first character of the string is located on position `from=0`.


!!! example

    ```yaml
    !SUBSTRING
    what: "FooBar"
    from: 1
    to: 3
    ```

    Returns `oo`.

---

## `!LOWER`

Transform a string or list of strings input to lowercase format.

Type: _Mapping_


Synopsis:

```yaml
!LOWER
what: <...>
```


!!! example

    ```yaml
    !LOWER
    what: "FooBar"
    ```

    Returns `foobar`.


!!! example

    ```yaml
    !LOWER
    what: ["FooBar", "Baz"]
    ```

    Returns list of values `["foobar", "baz"]`.

---

## `!UPPER`

Type: _Mapping_

Synopsis:

```yaml
!UPPER
what: <...>
```


!!! example

    ```yaml
    !UPPER
    what: "FooBar"
    ```

    Returns `FOOBAR`.

---

## `!CUT`

Cut the string by a delimiter and return the piece identified by `field` index (starts with 0).

Type: _Mapping_

Synopsis:

```yaml
!CUT
what: <string>
delimiter: <string>
field: <int>
```

The argument `value` string will be split using a `delimiter` argument.
The argument `field` specifies a number of the split strings to return, starting with 0.  
If the negative `field` is provided, then field is taken from the end of the string, for example -2 means the second last substring.


!!! example

    ```yaml
    !CUT
    what: "Apple,Orange,Melon,Citrus,Pear"
    delimiter: ","
    field: 2
    ```

    Will return value "Melon".

!!! example

    ```yaml
    !CUT
    what: "Apple,Orange,Melon,Citrus,Pear"
    delimiter: ","
    field: -2
    ```

    Will return value "Citrus".

  
---

## `!SPLIT`

Splits a string into a list of strings.

Type: _Mapping_

Synopsis:

```yaml
!SPLIT
what: <string>
delimiter: <string>
maxsplit: <number>
```

The argument `what` string will be split using a `delimiter` argument.
An optional `maxsplit` arguments specifies how many splits to do.


!!! example

    ```yaml
    !SPLIT
    what: "hello,world"
    delimiter: ","
    ```

    The result is a list: `["hello", "world"]`.

---

## `!RSPLIT`

Splits a string from the right (end of the string) into a list of strings.

Type: _Mapping_

Synopsis:

```yaml
!RSPLIT
what: <string>
delimiter: <string>
maxsplit: <number>
```

The argument `what` string will be split using a `delimiter` argument.
An optional `maxsplit` arguments specifies how many splits to do.


---

## `!JOIN`

Type: _Mapping_

Synopsis:

```yaml
!JOIN
items:
  - <...>
  - <...>
delimiter: <string>
miss: ""
```

Default `delimiter` is space (" ").

If the item is `None`, then the value of `miss` parameter is used, by default it is empty string.
If `miss` is `None` and  any of `items` is `None`, the result of the whole join is `None`.

!!! example

    ```yaml
    !JOIN
    items:
      - "Foo"
      - "Bar"
    delimiter: ","
    ```

---

## `!LDAP.SID`

Converts LDAP SID bytes to LDAP SID string representation.

Type: _Mapping_

Synopsis:

```yaml
!LDAP.SID
what: <bytes>
```

??? example "Convert event field with LDAP SID bytes to LDAP SID string"

    _Input string:_ `b"\x01\x05\x00\x00\x00\x00\x00\x05\x15\x00\x00\x00\xa3[Xru\x97\xabh\x05Vt\x9e/'\x02\x00"`

    ```yaml
    !LDAP.SID
    what: !ITEM EVENT ldapbytes
    ```
    _Output:_ `S-1-5-21-1918393251-1756075893-2658424325-141103`

??? example "Convert hex representation of LDAP SID bytes to LDAP SID string"

    ```yaml
    !LDAP.SID
    what: !HEX.BYTES
          what: "010500000000000515000000a35b58727597ab680556749e2f270200"
    ```
    _Output:_ `S-1-5-21-1918393251-1756075893-2658424325-141103`
