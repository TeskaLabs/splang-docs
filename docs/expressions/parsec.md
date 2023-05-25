---
title: Parsec
---

# PARSEC expressions


Parsec expressions group represents the concept of [Parser combinator](https://en.wikipedia.org/wiki/Parser_combinator).

They provide a way to combine basic parsers in order to construct more complex parsers for specific rules.
In this context, a parser is a function that takes string as input and produces a structured output, that indicates successful parsing or provide an error message if the parsing process fails.

Parsec expressions are divided into two groups: parsers and combinators.

*Parsers* can be seen as the fundamental units or building blocks. They are responsible for recognizing and processing specific patterns or elements within the input string.

*Combinators*, on the other hand, are operators or functions that allow the combination and composition of parsers.

Every expression starts with `!PARSE.` prefix.


---

## `!PARSE.DIGIT`: Parse a single digit

Type: _Parser_.

### Synopsis

```yaml
!PARSE.DIGIT
```


### Example
_Input string:_ `2`

```yaml
!PARSE.DIGIT
```

---

## `!PARSE.DIGITS`: Parse a sequence of digits

Type: _Parser_.

### Synopsis


```yaml
!PARSE.DIGITS
min: <...>
max: <...>
exactly: <...>
```
Fields `min`, `max` and `exactly` are optional.

!!! warning

	`Exactly` field can't be used together with `min` or `max` fields. And of course `max` value can't be less than `min` value.



### Example
_Input string:_ `123`

```yaml
!PARSE.DIGITS
max: 4
```

<details>
  <summary>More examples</summary>

Parse as many digits as possible:
```yaml
!PARSE.DIGITS
```

Parse exactly 3 digits:
```yaml
!PARSE.DIGITS
exactly: 3
```

Parse at least 2 digits, but not more than 4:
```yaml
!PARSE.DIGITS
min: 2
max: 4
```

</details>


---

## `!PARSE.LETTER`: Parse a single letter
Latin letters from A to Z, both uppercase and lowercase.

Type: _Parser_.

### Synopsis

```yaml
!PARSE.LETTER
```

### Example
_Input string:_ `A`

```yaml
!PARSE.LETTER
```


---

## `!PARSE.CHAR`: Parse a single character
Any type of character.

Type: _Parser_.

### Synopsis

```yaml
!PARSE.CHAR
```

### Example
_Input string:_ `@`
```yaml
!PARSE.CHAR
```


---

## `!PARSE.CHARS`: Parse a sequence of characters

Type: _Parser_.

### Synopsis

```yaml
!PARSE.CHARS
min: <...>
max: <...>
exactly: <...>
```
Fields `min`, `max` and `exactly` are optional.

!!! warning

	`Exactly` field can't be used together with `min` or `max` fields. And of course `max` value can't be less than `min` value.

### Example
_Input string:_ `name@123_`

```yaml
!PARSE.CHARS
max: 8
```
!!! tip

    Use `!PARSE.CHARS` without fields to parse till the end of the string.


<details>
  <summary>More examples</summary>

Parse as many chars as possible:
```yaml
!PARSE.CHARS
```

Parse exactly 3 chars:
```yaml
!PARSE.CHARS
exactly: 3
```

Parse at least 2 chars, but not more than 4:
```yaml
!PARSE.CHARS
min: 2
max: 4
```

</details>


---

## `!PARSE.SPACE`: Parse a single space character

Type: _Parser_.

### Synopsis

```yaml
!PARSE.SPACE
```


---

## `!PARSE.SPACES`: Parse a sequence of space characters

Parse as many space symbols as possible:

Type: _Parser_.

### Synopsis

```yaml
!PARSE.SPACES
```


---

## `!PARSE.ONEOF`: Parse a single character from a set of characters

Type: _Parser_.

### Synopsis

```yaml
!PARSE.ONEOF
what: <...>
```
or shorter version:
```yaml
!PARSE.ONEOF <...>
```

## Example
_Input string:_ `Wow`==!==

```yaml
!PARSE.ONEOF
what: "!?."
```


---

## `!PARSE.NONEOF`: Parse a single character that is not in a set of characters

Type: _Parser_.

### Synopsis

```yaml
!PARSE.NONEOF
what: <...>
```
or shorter version:
```yaml
!PARSE.NONEOF <...>
```

## Example
_Input string:_ `Wow`==!==

```yaml
!PARSE.NONEOF
what: ",;:[]()"
```


---

## `!PARSE.UNTIL`: Parse a sequence of characters until a specific character is found

Type: _Parser_.

### Synopsis

```yaml
!PARSE.UNTIL
what: <...>
stop: <before/after>
eof: <true/false>
```
or shorter version:
```yaml
!PARSE.UNTIL <...>
```

- `stop` - indicates whether the stop character should be parsed or not.
            Possible values: `before` or `after`(default).

- `eof` - indicates if we should parse till the end of the string if `what` symbol is not found.
            Possible values: `true` or `false`(default).


!!! info

        Field `what` must be a single character. But some whitespace characters can also be used  ex: `tab`

## Example
_Input string:_ `60290:11`

```yaml
!PARSE.UNTIL
what: ":"
```

<details>
  <summary>More examples</summary>

Parse until <code>:</code> symbol and stop before it:
```yaml
!PARSE.UNTIL
what: ":"
stop: "before"
```

Parse until space symbol and stop after it:
```yaml
!PARSE.UNTIL ' '
```

Parse until <code>,</code> symbol or parse till the end of the string if it's not found:
```yaml
!PARSE.UNTIL
what: ","
eof: true
```

Parse until <code>tab</code> symbol:
```yaml
!PARSE.UNTIL
what: 'tab'
```
</details>


---

## `!PARSE.EXACTLY`: Parse precisely a defined sequence of characters

Type: _Parser_.

### Synopsis

```yaml
!PARSE.EXACTLY
what: <...>
```
or shorter version:
```yaml
!PARSE.EXACTLY <...>
```

## Example
_Input string:_ `Hello world!`

```yaml
!PARSE.EXACTLY
what: "Hello"
```


---

## `!PARSE.BETWEEN`: Parse a sequence of characters between two specific characters

Type: _Parser_.

### Synopsis

```yaml
!PARSE.BETWEEN
what: <...>
start: <...>
stop: <...>
escape: <...>
```
or shorter version:
```yaml
!PARSE.BETWEEN <...>
```

- `what` - indicates between which same characters we should parse.

- `start`, `stop` - indicates between which different characters we should parse.

- `escape` - indicates escape character.


## Example
_Input string:_ `[10/May/2023:08:15:54 +0000]`

```yaml
!PARSE.BETWEEN
start: '['
stop: ']'
```

<details>
  <summary>More examples</summary>

Parse between double-quotes:
```yaml
!PARSE.BETWEEN
what: '"'
```

Parse between double-quotes, short form:
```yaml
!PARSE.BETWEEN '"'
```

Parse between double-quotes, escape internal double-quotes:<br>

<i>Input string:</i><code>"one, "two", three"</code>

```yaml
!PARSE.BETWEEN
what: '"'
escape: '\'
```
</details>


---

## `!PARSE.REGEX`: Parse a sequence of characters that matches a regular expression

Type: _Parser_.

### Synopsis

```yaml
!PARSE.REGEX
what: <...>
```

## Example
_Input string:_ `FTVW23_L-C: Message..`

_Output string:_ `FTVW23_L-C`

```yaml
!PARSE.REGEX
what: '[a-zA-Z0-9_\-0]+'
```


---

## `!PARSE.MONTH`: Parse a month name

Type: _Parser_.

### Synopsis

```yaml
!PARSE.MONTH
what: <...>
```
or shorter version:
```yaml
!PARSE.MONTH <...>
```

- `what` - indicates a format of the month name.
            Possible values: `number`, `short`, `full`.

!!! tip
    Use `!PARSE.MONTH` to parse month name as part of `!PARSE.DATETIME`.


## Example
_Input string:_ `10/`==May==`/2023:08:15:54`

```yaml
!PARSE.MONTH
what: 'short'
```

<details>
  <summary>More examples</summary>

Parse month in number format:<br>
<i>Input string:</i><code>2003-<mark>10</mark>-11</code>
```yaml
!PARSE.MONTH 'number'
```

Parse month in full format:<br>
<i>Input string:</i><code>2003-<mark>OCTOBER</mark>-11</code>
```yaml
!PARSE.MONTH
what: 'full'
```
</details>


---

## `!PARSE.FRAC`: Parse a fraction

Type: _Parser_.

### Synopsis

```yaml
!PARSE.FRAC
base: <...>
max: <...>
```

- `base` - indicates a base of the fraction.
            Possible values: `milli`, `micro`, `nano`.
- `max` - indicates a maximum number of digits depending on the `base` value.
            Possible values: `3`, `6`, `9` respectively.

!!! tip
    Use `!PARSE.FRAC` to parse microseconds or nanoseconds as part of `!PARSE.DATETIME`.


## Example
_Input string:_ `Aug 22 05:40:14`==.264==

```yaml
!PARSE.FRAC
base: "micro"
max: 6
```


---

## `!PARSE.DATETIME`: Parse datetime in a given format

Type: _Parser_.


### Synopsis

```yaml
!PARSE.DATETIME
- year: <...>
- month: <...>
- day: <...>
- hour: <...>
- minute: <...>
- second: <...>
- nanosecond: <...>
- timezone: <...>
```

- Fields `month`, `day` are required.
- Field `year` is optional. If not specified, the _smart year_ function will be used.
- Fields `hour`, `minute`, `second`,  `microsecond`, `nanosecond` are optional. If not specified, the default value 0 will be used.
- Specifying microseconds field like `microseconds?`, allow to parse microseconds or not  depends on their present in the input string.
- Field `timezone` is optional. If not specified, the default value `UTC` will be used.
  - `timezone` can be specified in two different formats.
    1. `Z`, `+08:00` - parsed from the input string.
    2. `Europe/Prague` - specified as a constant value.


### Shortcuts
Shortcut forms are available (in both lower/upper variants):

```yaml
!PARSE.DATETIME RFC3339
```

```yaml
!PARSE.DATETIME iso8601
```

## Example
_Input string:_ `2022-10-13T12:34:56.987654`

```yaml
!PARSE.DATETIME
- year: !PARSE.DIGITS
- '-'
- month: !PARSE.MONTH 'number'
- '-'
- day: !PARSE.DIGITS
- 'T'
- hour: !PARSE.DIGITS
- ':'
- minute: !PARSE.DIGITS
- ':'
- second: !PARSE.DIGITS
- microsecond: !PARSE.FRAC
                base: "micro"
                max: 6
- timezone: "Europe/Prague"
```

<details>
  <summary>More examples</summary>

Parse datetime without year, with short month form and optional microseconds:<br>
<i>Input string:</i> <code>Aug 17 06:57:05.189</code>
```yaml
!PARSE.DATETIME
- month: !PARSE.MONTH 'short' # Month
- !PARSE.SPACE
- day: !PARSE.DIGITS # Day
- !PARSE.SPACE
- hour: !PARSE.DIGITS # Hours
- !PARSE.EXACTLY { what: ':' }
- minute: !PARSE.DIGITS # Minutes
- !PARSE.EXACTLY { what: ':' }
- second: !PARSE.DIGITS # Seconds
- microsecond?: !PARSE.FRAC # Microseconds
                base: "micro"
                max: 6
```

Parse datetime with timezone:<br>
<i>Input string:</i> <code>2021-06-29T16:51:43+08:00</code>
```yaml
!PARSE.DATETIME
- year: !PARSE.DIGITS
- '-'
- month: !PARSE.MONTH 'number'
- '-'
- day: !PARSE.DIGITS
- 'T'
- hour: !PARSE.DIGITS
- ':'
- minute: !PARSE.DIGITS
- ':'
- second: !PARSE.DIGITS
- timezone: !PARSE.CHARS
```

Parse datetime using shortcut:<br>
<i>Input string:</i> <code>2021-06-29T16:51:43Z</code>
```yaml
!PARSE.DATETIME RFC3339
```

Parse datetime using shortcut:<br>
<i>Input string:</i> <code>20201211T111721Z</code>
```yaml
!PARSE.DATETIME iso8601
```

Parse datetime with nanoseconds:<br>
<i>Input string:</i> <code>2023-03-23T07:00:00.734323900</code>
```yaml
!PARSE.DATETIME
- year: !PARSE.DIGITS
- !PARSE.EXACTLY { what: '-' }
- month: !PARSE.DIGITS
- !PARSE.EXACTLY { what: '-' }
- day: !PARSE.DIGITS
- !PARSE.EXACTLY { what: 'T' }
- hour: !PARSE.DIGITS
- !PARSE.EXACTLY { what: ':' }
- minute: !PARSE.DIGITS
- !PARSE.EXACTLY { what: ':' }
- second: !PARSE.DIGITS
- nanosecond: !PARSE.FRAC
  base: "nano"
  max: 9
```

</details>
