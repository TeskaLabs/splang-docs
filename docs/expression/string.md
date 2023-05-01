---
title: String expressions
---

# String expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

---

## `!IN`: Test if the string contains a substring 

Type: _Mapping_.

### Synopsis

```yaml
!IN
what: <...>
where: <...>
```

The `!IN` expression is used to check if a string `what` exists in a string `where` or not.
Evaluate to "true" if it finds a substring `what` in the string `where` and false otherwise.

### Example

```yaml
!IN
what: "Willy"
where: "John Willy Boo"
```

Check for a presence of the substring "Willy" in the `where` value. Returns "true".


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

Example of `!REGEX` optimization by multi-string `!IN`:

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
  regex: '(msgbox|showmod(?:al|eless)dialog|showhelp|prompt|write)|(test[0-9])|([a-z]@mail\.com)'
```

This approach is recommended from applications in streams, where you need to filter an extensive amount of the data with assumption that only a smaller portion of the data matches the patters.
An application of the `!REGEX` expression directly will slow processing down significantly, because it is complex regular expression.
The idea is to "pre-filter" data with a simplier but faster condition so that only a fraction of the data reaches the expensive `!REGEX`.
The typical performance improvement is 5x-10x.

For that reason, the `!IN` must be a perfect superset of the `!REGEX`, it means:

* `!IN` -> `true`, `!REGEX` -> `true`: `true`
* `!IN` -> `true`, `!REGEX` -> `false`: `false` (this should be a minority of cases)
* `!IN` -> `false`, `!REGEX` -> `false`: `false` (prefiltering, this should be a majority of cases)
* `!IN` -> `false`, `!REGEX` -> `true`: this combination MUST BE avoided, adopt the `!IN` and/or `!REGEX` accordingly.

---

## `!STARTSWITH`: Test if the string starts with a prefix 

Type: _Mapping_

Returns `true` if `what` string begins with `prefix`.

### Synopsis

```yaml
!STARTSWITH
what: <...>
prefix: <...>
```


### Example

```yaml
!STARTSWITH
what: "FooBar"
prefix: "Foo"
```

---

## `!ENDSWITH`: Test if the string ends with a postfix 

Type: _Mapping_

Returns `true` if `what` string ends with `postfix`.

### Synopsis

```yaml
!ENDSWITH
what: <...>
postfix: <...>
```


### Example

```yaml
!ENDSWITH
what: "autoexec.bat"
postfix: ".bat"
```

---

## `!SUBSTRING`: Extract part of the string 

Type: _Mapping_

Return part of the string `what`, in between `from` and `to` index.

### Synopsis

```yaml
!SUBSTRING
what: <...>
from: <...>
to: <...>
```


### Example

```yaml
!SUBSTRING
what: "FooBar"
from: 1
to: 3
```

Returns `oo`.

---

## `!LOWER`: Transform string to lower-case 

Type: _Mapping_


### Synopsis

```yaml
!LOWER
what: <...>
```


### Example

```yaml
!LOWER
what: "FooBar"
```

Returns `foobar`.


---

## `!UPPER`: Transform string to upper-case 

Type: _Mapping_

### Synopsis

```yaml
!UPPER
what: <...>
```


### Example

```yaml
!UPPER
what: "FooBar"
```

Returns `FOOBAR`.

---

## `!CUT`: Cut portion of the string 

Type: _Mapping_

Cut the string by a delimiter and return the piece identified by `field` index (starts with 0).

### Synopsis

```yaml
!CUT
what: <string>
delimiter: <string>
field: <int>
```

The argument `value` string will be split using a `delimiter` argument.
The argument `field` specifies a number of the splited strings to return, starting with 0.  
If the negative `field` is provided, then field is taken from the end of the string, for example -2 means the second last substring.


### Example

```yaml
!CUT
what: "Apple,Orange,Melon,Citrus,Pear"
delimiter: ","
field: 2
```

Will return value "Melon".


```yaml
!CUT
what: "Apple,Orange,Melon,Citrus,Pear"
delimiter: ","
field: -2
```

Will return value "Citrus".

  
---

## `!SPLIT`: Split a string into the list 

Type: _Mapping_

Splits a string into a list of strings.

### Synopsis

```yaml
!SPLIT
what: <string>
delimiter: <string>
maxsplit: <number>
```

The argument `what` string will be split using a `delimiter` argument.
An optional `maxsplit` arguments specifies how many splits to do.


### Example

```yaml
!SPLIT
what: "hello,world"
delimiter: ","
```

---

## `!JOIN`: Join a list of strings 

Type: _Mapping_

### Synopsis

```yaml
!JOIN
items:
  - <...>
  - <...>
delimiter: <string>
miss: ''
```

Default `delimiter` is space (" ").

If the item is `None`, then the value of `miss` parameter is used, by default it is empty string.
If `miss` is `None` and  any of `items` is `None`, the result of the whole join is `None`.

### Example

```yaml
!JOIN
items:
  - "Foo"
  - "Bar"
delimiter: ','
```
