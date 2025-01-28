---
title: Regex
---

# Regex expressions

## Overview

!!! tip

    Use [Regexr](https://regexr.com) to develop and test regular expressions.


* [`!REGEX`](#regex): Regular expression search.
* [`!REGEX.REPLACE`](#regexreplace): Regular expression replace.
* [`!REGEX.SPLIT`](#regexsplit): Split a string by a regular expression.
* [`!REGEX.FINDALL`](#regexfindall): Find all occurrences by a regular expression.
* [`!REGEX.PARSE`](#regexparse): Parse by a regular expression.


---

## `!REGEX`

Regular expression search.

Type: _Mapping_.

Synopsis:

```yaml
!REGEX
what: <string>
regex: <regex>
hit: <hit>
miss: <miss>
```

Scan through `what` string looking for any location where regular expression `regex` produces a match.
If there is a match, then returns `hit`, otherwise `miss` is returned.
  
The expression `hit` is optional, default value is `true`.
  
The expression `miss` is optional, default value is `false`.


!!! example

    ```yaml
    !IF
    test:
      !REGEX
      what: "Hello world!"
      regex: "world"
    then:
      "Yes :-)"
    else:
      "No ;-("
```

!!! example "Another form:"

    ```yaml
    !REGEX
    what: "Hello world!"
    regex: "world"
    hit: "Yes :-)"
    miss: "No ;-("
    ```

--- 

## `!REGEX.REPLACE`

Regular expression replace.

Type: _Mapping_.

Synopsis:

```yaml
!REGEX.REPLACE
what: <string>
regex: <regex>
by: <string>
```

Replace regular expression `regex` matches in `what` by value of `by`.


!!! example

    ```yaml
    !REGEX.REPLACE
    what: "Hello world!"
    regex: "world"
    by: "Mars"
    ```

    Returns: `Hello Mars!`

---

## `!REGEX.SPLIT`

Split a string by a regular expression.

Type: _Mapping_.

Synopsis:

```yaml
!REGEX.SPLIT
what: <string>
regex: <regex>
max: <integer>
```

Split string `what` by regular expression `regex`.

An optional argument `max` specify the maximum number of splits.


!!! example

    ```yaml
    !REGEX.SPLIT
    what: "07/14/2007 12:34:56"
    regex: "[/ :]"
    ```

    Returns: `['07', '14', '2007', '12', '34', '56']`

---

## `!REGEX.FINDALL`

Find all occurrences by a regular expression.

Type: _Mapping_.

Synopsis:

```yaml
!REGEX.FINDALL
what: <string>
regex: <regex>
```

Find all matches of `regex` in the string `what`.

!!! example

    ```yaml
    !REGEX.FINDALL
    what: "Frodo, Sam, Gandalf, Legolas, Gimli, Aragorn, Boromir, Merry, Pippin"
    regex: \w+
    ```

    Returns: `['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Gimli', 'Aragorn', 'Boromir', 'Merry', 'Pippin']`

---

## `!REGEX.PARSE`

Parse by a regular expression.

Type: _Mapping_.

See the chapter [`!PARSE.REGEX`](./parsec/parser.md/#parseregex)
