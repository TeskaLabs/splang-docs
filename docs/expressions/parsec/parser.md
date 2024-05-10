---
title: Parser expressions
---

# Parser expressions

## Overview

Parser expressions are functions for parsing a certain sequence of characters.

Basic parsers can differentiate between digits, letters and spaces:

- `!PARSE.DIGIT`, `!PARSE.DIGITS`: parse single or multiple digits
- `!PARSE.LETTER`, `!PARSE.LETTERS`: parse single or multiple letters
- `!PARSE.SPACE`, `!PARSE.SPACES`: parse single or multiple whitespace characters
- `!PARSE.CHAR`, `!PARSE.CHARS`: parse single or multiple characters

The following expressions are used for parsing characters from custom set of characters and looking for specific characters in input strings:

- `!PARSE.EXACTLY`: parse only specific sequence of characters 
- `!PARSE.UNTIL`: parse till a specific character is found
- `!PARSE.BETWEEN`: parse between two characters
- `!PARSE.ONEOF`: parse only one of allowed characters
- `!PARSE.NONEOF`: parse every character except forbidden ones
- `!PARSE.REGEX`: parse characters matching a regular expression

The following expressions are used for parsing dates and times in various formats:

- `!PARSE.DATETIME`: parse date and time
- `!PARSE.MONTH`: parse month in various formats
- `!PARSE.FRAC`: parse decimal numbers (which is useful for parsing microseconds)

---

## `!PARSE.DIGIT`: Parse a single digit

Type: _Parser_.

Synopsis:

```yaml
!PARSE.DIGIT
```

!!! example

	_Input string:_ `2`

	```yaml
	!PARSE.DIGIT
	```

---

## `!PARSE.DIGITS`: Parse a sequence of digits

Type: _Parser_.

Synopsis:

```yaml
!PARSE.DIGITS
min: <...>
max: <...>
exactly: <...>
```

- `exactly` specifies the exact number of digits to parse.
- `min` and `max` specify the minimal and maximal number of digits to parse. They cannot be combined with `exactly` parameter.
- If none of fields `min`, `max` and `exactly` is specified, as many digits as possible are parsed.

!!! warning

	`exactly` field can't be used together with `min` or `max` fields. And of course `max` value can't be less than `min` value.


!!! example

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

Synopsis:

```yaml
!PARSE.LETTER
```

!!! example

	_Input string:_ `A`

	```yaml
	!PARSE.LETTER
	```


---

## `!PARSE.LETTERS`: Parse a sequence of letters

Type: _Parser_.

Synopsis:


```yaml
!PARSE.LETTERS
min: <...>
max: <...>
exactly: <...>
```
Fields `min`, `max` and `exactly` are optional.

!!! warning

	`exactly` field can't be used together with `min` or `max` fields. And of course `max` value can't be less than `min` value.

!!! example

	_Input string:_ `cat`

	```yaml
	!PARSE.LETTERS
	max: 4
	```

<details>
  <summary>More examples</summary>

Parse as many letters as possible:
```yaml
!PARSE.LETTERS
```

Parse exactly 3 letters:
```yaml
!PARSE.LETTERS
exactly: 3
```

Parse at least 2 letters, but not more than 4:
```yaml
!PARSE.LETTERS
min: 2
max: 4
```

</details>


---

## `!PARSE.SPACE`: Parse a single space character

Type: _Parser_.

Synopsis:

```yaml
!PARSE.SPACE
```


---

## `!PARSE.SPACES`: Parse a sequence of space characters

Parse as many space symbols as possible:

Type: _Parser_.

Synopsis:

```yaml
!PARSE.SPACES
```


---


## `!PARSE.CHAR`: Parse a single character
Any type of character.

Type: _Parser_.

Synopsis:

```yaml
!PARSE.CHAR
```

!!! example

	_Input string:_ `@`

	```yaml
	!PARSE.CHAR
	```


---

## `!PARSE.CHARS`: Parse a sequence of characters

Type: _Parser_.

Synopsis:

```yaml
!PARSE.CHARS
min: <...>
max: <...>
exactly: <...>
```
Fields `min`, `max` and `exactly` are optional.

!!! warning

	`exactly` field can't be used together with `min` or `max` fields. And of course `max` value can't be less than `min` value.

!!! example

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


## `!PARSE.EXACTLY`: Parse precisely a defined sequence of characters

Type: _Parser_.

Synopsis:

```yaml
!PARSE.EXACTLY
what: <...>
```
or shorter version:
```yaml
!PARSE.EXACTLY <...>
```

!!! example

	_Input string:_ `Hello world!`

	```yaml
	!PARSE.EXACTLY
	what: "Hello"
	```


---

## `!PARSE.UNTIL`: Parse a sequence of characters until a specific character is found

Type: _Parser_.

Synopsis:

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

- `what`: Specifies one (and only one) character to search for in the input string.

- `stop`: Indicates whether the stop character should be parsed or not.
			Possible values: `before` or `after` (default).

- `eof`: Indicates if we should parse till the end of the string if `what` symbol is not found.
			Possible values: `true` or `false` (default).


!!! info

	Field `what` must be a single character. But some whitespace characters can also be used such as `tab`.
	To search for a sequence of characters, see the expression [`!PARSE.CHARS.LOOKAHEAD`](./combinator.md#parsecharslookahead-parse-chars-applying-lookahead-group).

!!! example

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


## `!PARSE.BETWEEN`: Parse a sequence of characters between two specific characters

Type: _Parser_.

Synopsis:

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


!!! example

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

## `!PARSE.ONEOF`: Parse a single character from a set of characters

Type: _Parser_.

Synopsis:

```yaml
!PARSE.ONEOF
what: <...>
```
or shorter version:
```yaml
!PARSE.ONEOF <...>
```

!!! example

	_Input strings:_

	```
	process finished with status 0
	process finished with status 1
	process finished with status x
	```

	```yaml
	!PARSE.KVLIST
	- "process finished with status "
	- !PARSE.ONEOF
	what: "01x"
	```


---

## `!PARSE.NONEOF`: Parse a single character that is not in a set of characters

Type: _Parser_.

Synopsis:

```yaml
!PARSE.NONEOF
what: <...>
```
or shorter version:
```yaml
!PARSE.NONEOF <...>
```

!!! example

	_Input string:_ `Wow!`

	```yaml
	!PARSE.NONEOF
	what: ",;:[]()"
	```


---

## `!PARSE.REGEX`: Parse a sequence of characters that matches a regular expression

Type: _Parser_.

Synopsis:

```yaml
!PARSE.REGEX
what: <...>
```

!!! example

	_Input string:_ `FTVW23_L-C: Message...`

	_Output:_ `FTVW23_L-C`

	```yaml
	!PARSE.REGEX
	what: '[a-zA-Z0-9_\-0]+'
	```


---


## `!PARSE.DATETIME`: Parse datetime in a given format

Type: _Parser_.


Synopsis:

```yaml
!PARSE.DATETIME
- year: <...>
- month: <...>
- day: <...>
- hour: <...>
- minute: <...>
- second: <...>
- microsecond: <...>
- nanosecond: <...>
- timezone: <...>
```

- Fields `month` and `day` are required.
- Field `year` is optional. If not specified, the [smart year](#smart-year) function will be used. Two digit year option is supported.
- Fields `hour`, `minute`, `second`,  `microsecond`, `nanosecond` are optional. If not specified, the default value 0 will be used.
- Specifying microseconds field like `microseconds?` allows you to parse microseconds or not, depending on their presence in the input string.
- Field `timezone` is optional. If not specified, the default value `UTC` will be used. It can be specified in two different formats.
    1. `Z`, `+08:00` - parsed from the input string.
    2. `Europe/Prague` - specified as a constant value.


There are also shortcuts for time formats `RFC 3331` and `ISO 8601`, see [Shortcuts](#shortcuts).

!!! example
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
	```


??? example "Parse without year and with optional microseconds"

	Parse datetime without year, with short month form and optional microseconds:

	_Input strings:_ 
	
	```
	Aug 17 12:00:00
	Aug 17 12:00:00.123
	Aug 17 12:00:00.123456
	```

	```yaml
	!PARSE.DATETIME
	- month: !PARSE.MONTH 'short' # Month
	- !PARSE.SPACE
	- day: !PARSE.DIGITS # Day
	- !PARSE.SPACE
	- hour: !PARSE.DIGITS # Hour
	- ":"
	- minute: !PARSE.DIGITS # Minutes
	- ":"
	- second: !PARSE.DIGITS # Seconds
	- microsecond?: !PARSE.FRAC # Microseconds
					base: "micro"
					max: 6
	```

	In this case, `year` is automatically determined by the _smart year_ function, which basically means that the current year is used.

??? example "Parse timezone"

	Parse datetime with timezone.

	_Input strings_:

	```
	2024-04-15T12:00:00+04:00
	2024-04-15T12:00:00+02:00
	2024-04-15T12:00:00+00:00
	2024-04-15T12:00:00-02:00
	```

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

??? example "Parse two digit year"

	Parse datetime with two digit year:

	_Input string:_ `22-10-13T12:34:56.987654`

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
	```

??? example "Parse nanoseconds"

	Parse datetime with nanoseconds:

	_Input string:_ `2023-03-23T07:00:00.734323900`

	```yaml
	!PARSE.DATETIME
	- year: !PARSE.DIGITS
	- "-"
	- month: !PARSE.DIGITS
	- "-"
	- day: !PARSE.DIGITS
	- "T"
	- hour: !PARSE.DIGITS
	- ":"
	- minute: !PARSE.DIGITS
	- ":"
	- second: !PARSE.DIGITS
	- nanosecond: !PARSE.FRAC
				base: "nano"
				max: 9
	```
### Smart year

The `smart year` function is designed to predict the complete year from a provided month by taking into account the
current year and month to determine the most likely corresponding four-digit year.

### Shortcuts
Shortcut forms are available (in both lower/upper variants):


#### ISO 8601

```yaml
!PARSE.DATETIME ISO8601
```

This expression parses datetimes defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).
Timezone can be parsed from the input string or, if not present, it can be set in the lmio-parsec configuration.

Example of datetimes that can be parsed using the shortcut:

```
2024-04-12T10:16:21Z
20240412T101621Z
2024-12-11T11:17:21.123456+00:00
2024-04-12T03:16:21−07:00
2024-04-12T03:16:21
```

#### RFC 3339

```yaml
!PARSE.DATETIME RFC3339
```

This expression parses datetimes defined by [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339).
Timezone is always parsed from the input string.

Example of datetimes that can be parsed using the shortcut:

```
1985-04-12T23:20:50.52Z
1996-12-19T16:39:57-08:00
2021-06-29 16:51:43.987654+02:00
```

#### RFC 3164

```yaml
!PARSE.DATETIME RFC3164
```

This expression parses datetimes defined by [RFC 3164](https://www.rfc-editor.org/rfc/rfc3164).
Year is provided by the [smart year](#smart-year) function. Timezone must be set in LogMan.io Parsec configuration, otherwise considered as UTC.

Example of datetimes that can be parsed using the shortcut:

```
Apr 24 15:25:20
Oct  3 20:33:02
AUG  4 10:20:20
```

---


## `!PARSE.MONTH`: Parse a month name

Type: _Parser_.

Synopsis:

```yaml
!PARSE.MONTH
what: <...>
```
or shorter version:
```yaml
!PARSE.MONTH <...>
```

Parameter `what` indicates format of the month name.
Possible values are:

- `number`: numbered representation, e.g. `01` for January, `12` for December
- `short`: three letters representation, e.g. `Jan` for January, `Dec` for December
- `full`: full name representation, e.g. `January`, `December`

!!! tip
	Use `!PARSE.MONTH` to parse month name as part of `!PARSE.DATETIME`.


!!! example

	_Input string:_ `10/`==Jan==`/2023:08:15:54`

	```yaml
	!PARSE.MONTH 'short'
	```

	_Input string:_ `10/`==01==`/2023:08:15:54`

	```yaml
	!PARSE.MONTH 'number'
	```

	_Input string:_ `10/`==January==`/2023:08:15:54`

	```yaml
	!PARSE.MONTH 'full'
	```

---

## `!PARSE.FRAC`: Parse a fraction
Fraction parsing includes parsing of a dot (.) and a comma (,) separator.

Type: _Parser_.

Synopsis:

```yaml
!PARSE.FRAC
base: <...>
max: <...>
```

- `base`: Indicates a base of the fraction.
	Possible values are:

	* `milli` for `10^-3` base
	* `micro` for `10^-6` base
	* `nano` for `10^-9` base

- `max`: Indicates a maximum number of digits depending on the `base` value.
	Default values `3`, `6`, `9` will be applied if `max` parametr is not specified.

!!! tip
	Use `!PARSE.FRAC` to parse microseconds or nanoseconds as part of `!PARSE.DATETIME`.


!!! example

	_Input string:_ `Aug 22 05:40:14`==.264==

	```yaml
	!PARSE.FRAC
	base: "micro"
	```

	or full form:

	```yaml
	!PARSE.FRAC
	base: "micro"
	max: 6
	```

---
