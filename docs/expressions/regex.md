---
title: Regex
---

# Regex expressions


!!! tip

    Use [Regexr](https://regexr.com) to develop and test regular expressions.

--- 

## `!REGEX`: Regular expression search  

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


### Example

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

The above example can be also written as:
  
```yaml
!REGEX
what: "Hello world!"
regex: "world"
hit: "Yes :-)"
miss: "No ;-("
```

--- 

## `!REGEX.REPLACE`: Regular expression replace  

Type: _Mapping_.

Synopsis:

```yaml
!REGEX.REPLACE
what: <string>
regex: <regex>
by: <string>
```

Replace regular expression `regex` matches in `what` by value of `by`.


### Example

```yaml
!REGEX.REPLACE
what: "Hello world!"
regex: "world"
by: "Mars"
```

Returns: `Hello Mars!`

--- 

## `!REGEX.SPLIT`: Split a string by a regular expression  

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


### Example

```yaml
!REGEX.SPLIT
what: "07/14/2007 12:34:56"
regex: "[/ :]"
```

Returns: `['07', '14', '2007', '12', '34', '56']`

--- 

## `!REGEX.FINDALL`: Find all occurences by a regular expression  

Type: _Mapping_.

Synopsis:

```yaml
!REGEX.FINDALL
what: <string>
regex: <regex>
```

Find all matches of `regex` in the string `what`.

### Example

```yaml
!REGEX.FINDALL
what: "Frodo, Sam, Gandalf, Legolas, Gimli, Aragorn, Boromir, Merry, Pippin"
regex: \w+
```

Returns: `['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Gimli', 'Aragorn', 'Boromir', 'Merry', 'Pippin']`

---

## `!REGEX.PARSE`: Parse by a regular expression 

Type: _Mapping_.

