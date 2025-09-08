---
title: Parser expressions
---

# Parser expressions

## Overview

Parser expressions are functions for parsing a certain sequence of characters.

Basic parsers can differentiate between digits, letters and spaces:

- [`!PARSE.DIGIT`](#parsedigit), [`!PARSE.DIGITS`](#parsedigits): Parse single or multiple digits.
- [`!PARSE.LETTER`](#parseletter), [`!PARSE.LETTERS`](#parseletters): Parse single or multiple letters.
- [`!PARSE.SPACE`](#parsespace), [`!PARSE.SPACES`](#parsespaces): Parse single or multiple whitespace characters
- [`!PARSE.CHAR`](#parsechar), [`!PARSE.CHARS`](#parsechars): Parse single or multiple characters.

The following expressions are used for parsing characters from custom set of characters and looking for specific characters in input strings:

- [`!PARSE.EXACTLY`](#parseexactly): Parse only specific sequence of characters.
- [`!PARSE.UNTIL`](#parseuntil): Parse till a specific character is found.
- [`!PARSE.BETWEEN`](#parsebetween): Parse between two characters.
- [`!PARSE.ONEOF`](#parseoneof): Parse only one of allowed characters.
- [`!PARSE.NONEOF`](#parsenoneof): Parse every character except forbidden ones.
- [`!PARSE.REGEX`](#parseregex): Parse characters matching a regular expression.

The following expressions are used for parsing dates and times in various formats:

- [`!PARSE.DATETIME`](#parsedatetime): Parse date and time.
- [`!PARSE.MONTH`](#parsemonth): Parse month in various formats.
- [`!PARSE.FRAC`](#parsefrac): Parse decimal numbers (which is useful for parsing microseconds).

The following expressions are used for parsing specific types of strings:

- [`!PARSE.IP`](#parseip): Parse IP address.
- [`!PARSE.MAC`](#parsemac): Parse MAC address.

---

## `!PARSE.DIGIT`

Parse a single digit.

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

## `!PARSE.DIGITS`

Parse a sequence of digits.

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

## `!PARSE.LETTER`

Parse a single letter.

By letters, we mean latin letters from A to Z, both uppercase and lowercase.

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

## `!PARSE.LETTERS`

Parse a sequence of letters.

By letters, we mean latin letters from A to Z, both uppercase and lowercase.

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

    `exactly` field can't be used together with `min` or `max` fields.
    And of course `max` value can't be less than `min` value.

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

## `!PARSE.SPACE`

Parse a single space character.

Type: _Parser_.

Synopsis:

```yaml
!PARSE.SPACE
```

---

## `!PARSE.SPACES`

Parse a sequence of space characters.

Parse as many space symbols as possible:

Type: _Parser_.

Synopsis:

```yaml
!PARSE.SPACES
```

---

## `!PARSE.CHAR`

Parse a single character of any type.

Type: _Parser_.

Synopsis:

```yaml
!PARSE.CHAR
```

!!! example

    Input string: `@`

    ```yaml
    !PARSE.CHAR
    ```

---

## `!PARSE.CHARS`

Parse a sequence of characters.

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

    `exactly` field can't be used together with `min` or `max` fields.
    And of course `max` value can't be less than `min` value.

!!! example

    Input string:_ `name@123_`

    ```yaml
    !PARSE.CHARS
    max: 8
    ```

!!! tip

    Use `!PARSE.CHARS` with default settings to parse till the end of the string.


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

## `!PARSE.EXACTLY`

Parse a precisely defined sequence of characters.

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

    Input string:_`Hello world!`

    ```yaml
    !PARSE.EXACTLY { what: Hello }
    ```

    Shorter version:

    ```yaml
    !PARSE.EXACTLY Hello
    ```

!!! tip

    When using `!PARSE.EXACTLY` inside `!PARSE.KVLIST`, you can also use the shortest form:

    Input string: `<260>`


    ```yaml
    !PARSE.KVLIST
    - "<"  # instead of !PARSE.EXACTLY "<"
    - value: !PARSE.DIGITS
    - ">"  # instead of !PARSE.EXACTLY ">"
    ```

---

## `!PARSE.UNTIL`

Parse a sequence of characters until a specific character is found.

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

- `escape`: Indicates escape character.


!!! info

    Field `what` must be a single character. But some whitespace characters can also be used such as `tab`.
    To search for a sequence of characters, see the expression [`!PARSE.CHARS.LOOKAHEAD`](./combinator.md#parsecharslookahead).

!!! example

    Input string:_ `60290:11`

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

Parse until <code>tab</code> symbol (upper and lower case are supported):
```yaml
!PARSE.UNTIL TAB
```

Parse until <code>newline</code> symbol (upper and lower case are supported):
```yaml
!PARSE.UNTIL NEWLINE
```

Parse until vertical slash, escape internal vertical slashes:<br>

<i>Input string:</i><code>CRED_REFR\|success\|fail|</code>

```yaml
!PARSE.UNTIL
what: '|'
escape: '\'
```


</details>


---

## `!PARSE.BETWEEN`

Parse a sequence of characters between two specific characters.

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
!PARSE.BETWEEN <what>
```

- `what`: Specifies the character to parse between when both the start and end delimiters are the same (e.g., double quotes).

- `start`, `stop`: Specify different characters to use as the start and end delimiters, respectively.

- `escape`: Defines the escape character to allow inclusion of delimiter characters within the parsed sequence.


!!! example

    Input string:_`[10/May/2023:08:15:54 +0000]`

    ```yaml
    !PARSE.BETWEEN { start: '[', stop: ']' }
    ```

<details>
  <summary>More examples</summary>

Parse between double-quotes:
```yaml
!PARSE.BETWEEN { what: '"' }
```

Parse between double-quotes, short form:
```yaml
!PARSE.BETWEEN '"'
```

Parse between double-quotes, escape internal double-quotes:<br>

<i>Input string:</i><code>"one, \"two\", three"</code>

```yaml
!PARSE.BETWEEN { what: '"', escape: '\'}
```

</details>

---

## `!PARSE.ONEOF`

Parse a single character from a selected set of characters.

Type: _Parser_.

Synopsis:

```yaml
!PARSE.ONEOF
what: <...>
```

or shorter version:

```yaml
!PARSE.ONEOF <what>
```

!!! example

    Input strings:_

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

## `!PARSE.NONEOF`

Parse a single character that is not in a selected set of characters.

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

    Input string:_ `Wow!`

    ```yaml
    !PARSE.NONEOF
    what: ",;:[]()"
    ```

---

## `!PARSE.REGEX`

Parse a sequence of characters that matches a regular expression.

Type: _Parser_.

Synopsis:

```yaml
!PARSE.REGEX
what: <...>
```

!!! example

    Input string:_ `FTVW23_L-C: Message...`

    _Output:_ `FTVW23_L-C`

    ```yaml
    !PARSE.REGEX
    what: '[a-zA-Z0-9_\-0]+'
    ```

---

## `!PARSE.DATETIME`

Parse datetime.

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
- period: <...>
```

- Fields `month` and `day` are required.
- Field `year` is optional. If not specified, the [smart year](#smart-year) function will be used. Both 2 and 4-digit numbers are supported.
- Fields `hour`, `minute`, `second`,  `microsecond`, `nanosecond` are optional. If not specified, the default value 0 will be used.
- Specifying microseconds field like `microseconds?` allows you to parse microseconds or not, depending on their presence in the input string.
- Field `timezone` is optional. If not specified, the default value `UTC` will be used. [Read more about timezone parsing here.](#timezone)
- Field `period` is optional. If not specified, the 24-hour format will be used. The period value is case-insensitive.

!!! tip "Common datetime formats"
    Use [Shortcuts](#shortcuts) for parsing datetime formats [`RFC 3339`](#rfc-3339), [`RFC 3164`](#rfc-3164) and [`ISO 8601`](#iso-8601).

!!! tip "UNIX time"
    For parsing datetime in [UNIX time](https://en.wikipedia.org/wiki/Unix_time), use [`!PARSE.DATETIME EPOCH`](#epoch).

!!! tip
    Use [`!PARSE.MONTH`](#parsemonth) for parsing a month.

!!! tip
    Use [`!PARSE.FRAC`](#parsefrac) for parsing microseconds and nanoseconds. Note that this expression consumes `.` and `,` as well. Do not parse them separately.

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

??? example "Two-digit year"

    Parse datetime with two-digit year:

    _Input string:_ `22-10-13T12:34:56.987654`

    ```yaml hl_lines="2"
    !PARSE.DATETIME
    - year: !PARSE.DIGITS  # Year can be either 4-digit or 2-digit
    - '-'
    - month: !PARSE.MONTH "number"
    - '-'
    - day: !PARSE.DIGITS
    - 'T'
    - hour: !PARSE.DIGITS
    - ':'
    - minute: !PARSE.DIGITS
    - ':'
    - second: !PARSE.DIGITS
    - microsecond: !PARSE.FRAC
                base: micro
    ```

??? example "No year, optional microseconds"

    Parse datetime without a year, with short month form and optional microseconds:

    _Input strings:_ 
    
    ```
    Aug 17 12:00:00
    Aug 17 12:00:00.123
    Aug 17 12:00:00.123456
    ```

    ```yaml hl_lines="2 12"
    !PARSE.DATETIME
    # There is no year in input string, smart year function is used.
    - month: !PARSE.MONTH 'short'
    - !PARSE.SPACE
    - day: !PARSE.DIGITS
    - !PARSE.SPACE
    - hour: !PARSE.DIGITS
    - ":"
    - minute: !PARSE.DIGITS
    - ":"
    - second: !PARSE.DIGITS
    - microsecond?: !PARSE.FRAC  # Parsing of microseconds is optional here
                    base: "micro"
                    max: 6
    ```

    In this case, `year` is automatically determined by the _smart year_ function, which basically means that the current year is used.

??? example "Milliseconds"

    Parse datetime with milliseconds:

    _Input string:_ `2023-03-23T07:00:00.734`

    ```yaml hl_lines="13-15"
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
    - microsecond: !PARSE.FRAC
                base: milli
                max: 3
    ```

??? example "Nanoseconds"

    Parse datetime with nanoseconds:

    _Input string:_ `2023-03-23T07:00:00.734323900`

    ```yaml hl_lines="13-15"
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

??? example "Period"

    Parse datetime with period (AM/PM):

    _Input string:_ `7/24/2025 4:27:44 AM`

    ```yaml hl_lines="14"
    !PARSE.DATETIME
    - month: !PARSE.MONTH "number"
    - "/"
    - day: !PARSE.DIGITS
    - "/"
    - year: !PARSE.DIGITS
    - !PARSE.SPACE
    - hour: !PARSE.DIGITS
    - ":"
    - minute: !PARSE.DIGITS
    - ":"
    - second: !PARSE.DIGITS
    - !PARSE.SPACE
    - period: !PARSE.CHARS
    ```

### Timezone

Timezone can be either specified in the log or it can be missing. There are two approaches for that:

1. Timezone is parsed from the input string. In that case, use the suitable parsing expression for the timezone part.

    ```yaml
    !PARSE.DATETIME
    - timezone: !PARSE.UNTIL " "
    ```

    Permissible formats of timezones are: `Z`, `UTC`, `CET`, `CEST`, `+02:00`, `-0600`.

2. Timezone is fixed. In that case, specify it as [IANA timezone](https://www.iana.org/time-zones).

    ```yaml
    !PARSE.DATETIME
    - timezone: "Europe/Prague"
    ```

    This will come handy when the timezone is missing in the log or when it is used incorrectly.


??? example "Timezone from input"

    Parse datetime which contains timezone in input strings.

    _Input strings_:

	```
	2024-04-15T12:00:00+04:00 ...(other log content)
	2024-04-15T12:00:00-02:00 ...
	2024-04-15T12:00:00Z ...
	```

    ```yaml hl_lines="13"
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
    - timezone: !PARSE.UNTIL " "  # Read timezone from '+04:00', '+02:00', etc.
    ```

    _Input strings_:

	```
	2024-04-15T12:00:00 CET ...(other log content)
	2024-04-15T12:00:00 UTC ...
	```

    ```yaml hl_lines="14"
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
    - !PARSE.SPACE
    - timezone: !PARSE.UNTIL " "  # Read timezone from '+04:00', '+02:00', etc.
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

#### Epoch

```yaml
!PARSE.DATETIME EPOCH
```

```yaml
!PARSE.DATETIME epoch
```

This expression parses datetimes defined by [Unix time](https://en.wikipedia.org/wiki/Unix_time).
Expression allows parsing for different Unix datetime representations, such as seconds, milliseconds, microseconds and seconds
with micro/milliseconds floating point.

Example of datetimes that can be parsed using the shortcut:

```
1731410205 - seconds
1727951634.687 - seconds with microseconds floating point
1728564383160 - milliseconds
```

---

## `!PARSE.MONTH`

Parse a month.

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

    Input string:_ `10/`==Jan==`/2023:08:15:54`

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

## `!PARSE.FRAC`

Parse a fraction.

!!! warn

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
    Default values `3`, `6`, `9` will be applied if `max` parameter is not specified.

!!! tip
    Use `!PARSE.FRAC` to parse microseconds or nanoseconds as part of [`!PARSE.DATETIME`](#parsedatetime).


!!! example

    Input strings:

    ```
    Aug 22 05:40:14.264
    Aug 22 05:40:14.264023
    ```

    ```yaml
    !PARSE.FRAC
    base: "micro"
    ```

    or the full form:

    ```yaml
    !PARSE.FRAC
    base: "micro"
    max: 6
    ```

---

## `!PARSE.IP`

Parse IP address in both IPv4 and IPv6 formats.

Returns [numeric representation](https://ndocs.teskalabs.com/sp-lang/language/types/#ip-address) of the IP address.

Type: _Parser_.

Synopsis:

```yaml
!PARSE.IP
```

!!! example

    Input string:_ `193.178.72.2`

    ```yaml
    !PARSE.IP
    ```


---

## `!PARSE.MAC`

Parse MAC address in the format `XX:XX:XX:XX:XX:XX`.

Returns [numeric representation](https://ndocs.teskalabs.com/sp-lang/language/types/#mac-address) of the MAC address.


Type: _Parser_.

Synopsis:

```yaml
!PARSE.MAC
```

!!! example

    Input string:_ `4d:3b:4c:bc:e5:6d`

    ```yaml
    !PARSE.MAC
    ```

---

## `!PARSE.CEFKV`

Parse log entries in CEF (Common Event Format) key-value format, extracting structured fields from input string.

Each field is in the format `key=value`, with `=` as the fixed key-value separator, and a single space separating each key-value pair.

The expression can correctly handle values that contain spaces, as long as each key-value pair is properly formatted.

The fields extracted by !PARSE.CEFKV correspond to those defined in the CEF standard field reference. For a full list of supported fields and detailed format specifications, refer to the official documentation:

[Implementing ArcSight Common Event Format (CEF) - Version 26](https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-8.4/pdfdoc/cef-implementation-standard/cef-implementation-standard.pdf)


Type: _Parser_.

Synopsis:

```yaml
!PARSE.CEFKV
```

!!! example

    _Input string:_ `start=1731934886000 end=1731934886000 ahost=aac-ax-01 agt=192.168.57.141 agentZoneURI=/All Zones/ArcSight System IPv4/Private Address Space Zones/RFC1918: 192.168.0.0-192.168.255.255 amac=00-50-56-8C-85-D4 av=8.4.6.9408.1 atz=Europe/Prague at=syslog dvchost=pfsense1data.local dvc=192.168.51.2 dtz=Europe/Prague geid=3293577591578960401 parserVersion= parserIdentifier= _cefVer=1.0`

    ```yaml
    !PARSE.CEFKV
    ```

    _Output:_

    ```
    [
        ('start', '1731934886000'),
        ('end', '1731934886000'),
        ('ahost', 'aac-ax-01'),
        ('agt', '192.168.57.141'),
        ('agentZoneURI', '/All Zones/ArcSight System IPv4/Private Address Space Zones/RFC1918: 192.168.0.0-192.168.255.255'),
        ('amac', '00-50-56-8C-85-D4'),
        ('av', '8.4.6.9408.1'),
        ('atz', 'Europe/Prague'),
        ('at', 'syslog'),
        ('dvchost', 'pfsense1data.local'),
        ('dvc', '192.168.51.2'),
        ('dtz', 'Europe/Prague'),
        ('geid', '3293577591578960401'),
        ('parserVersion', ''),
        ('parserIdentifier', ''),
        ('_cefVer', '1.0')
    ]
    ```

---
