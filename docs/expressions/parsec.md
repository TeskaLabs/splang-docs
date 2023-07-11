---
title: Parsec
---

# PARSEC expressions


Parsec expressions group represents the concept of [Parser combinator](https://en.wikipedia.org/wiki/Parser_combinator).

They provide a way to combine basic parsers in order to construct more complex parsers for specific rules.
In this context, a parser is a function that takes string as input and produces a structured output, that indicates successful parsing or provide an error message if the parsing process fails.

Parsec expressions are divided into two groups: parsers and combinators.

_Parsers_ can be seen as the fundamental units or building blocks. They are responsible for recognizing and processing specific patterns or elements within the input string.

_Combinators_, on the other hand, are operators or functions that allow the combination and composition of parsers.

Every expression starts with `!PARSE.` prefix.


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
Fields `min`, `max` and `exactly` are optional.

!!! warning

	`Exactly` field can't be used together with `min` or `max` fields. And of course `max` value can't be less than `min` value.

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

	`Exactly` field can't be used together with `min` or `max` fields. And of course `max` value can't be less than `min` value.

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

	_Input string:_ `Wow!`

	```yaml
	!PARSE.ONEOF
	what: "!?."
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

- `stop` - indicates whether the stop character should be parsed or not.
			Possible values: `before` or `after`(default).

- `eof` - indicates if we should parse till the end of the string if `what` symbol is not found.
			Possible values: `true` or `false`(default).


!!! info

		Field `what` must be a single character. But some whitespace characters can also be used such as `tab`.

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

- `what` - indicates a format of the month name. Possible values: `number`, `short`, `full`.

!!! tip
	Use `!PARSE.MONTH` to parse month name as part of `!PARSE.DATETIME`.


!!! example

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

Synopsis:

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


!!! example

	_Input string:_ `Aug 22 05:40:14`==.264==

	```yaml
	!PARSE.FRAC
	base: "micro"
	max: 6
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
- nanosecond: <...>
- timezone: <...>
```

- Fields `month`, `day` are required.
- Field `year` is optional. If not specified, the _smart year_ function will be used.
- Fields `hour`, `minute`, `second`,  `microsecond`, `nanosecond` are optional. If not specified, the default value 0 will be used.
- Specifying microseconds field like `microseconds?`, allow to parse microseconds or not  depends on their present in the input string.
- Field `timezone` is optional. If not specified, the default value `UTC` will be used. It can be specified in two different formats.
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


---

## `!PARSE.REPEAT`: Parse a repeated pattern

Type: _Combinator_.

Synopsis:

```yaml
!PARSE.REPEAT
what: <...>
min: <...>
max: <...>
exactly: <...>
```

Fields `min`, `max` and `exactly` are optional. If none of them is specified, `what` will be repeated as many times as possible.


## Example
_Input string:_ `abc_abc`

```yaml
!PARSE.REPEAT
what: !PARSE.ONEOF "abc"
exactly: 3
```

_Output:_ `['a', 'b', 'c']`

<details>
  <summary>More examples</summary>

Parse <code>what</code> pattern as many as possible:
```yaml
!PARSE.REPEAT
what: !PARSE.EXACTLY 'hello'
```

Parse <code>what</code> pattern at least 2 times, but not more than 4:
```yaml
!PARSE.REPEAT
what: !PARSE.EXACTLY 'hello'
min: 2
max: 4
```

</details>


---

## `!PARSE.SEPARATED`: Parse a sequence with a separator

Type: _Combinator_.

Synopsis:

```yaml
!PARSE.SEPARATED
what: <...>
sep: <...>
min: <...>
max: <...>
end: <...>
```

Fields `max` and `end` are optional. 

- `end` - indicates if trailing separator is required. By default, it is optional.

  
## Example
_Input string:_ `0->1->2->3`

_Note:_ trailing separator is optional, so  input string `0->1->2->3->` is also valid.

```yaml
!PARSE.SEPARATED
what: !PARSE.DIGITS
sep: !PARSE.EXACTLY {what: "->"}
min: 3
```

_Output:_ `[0, 1, 2, 3]`

<details>
  <summary>More examples</summary>

Parse <code>what</code> values separated by <code>sep</code> in <code>[min;max]</code> interval, trailing separator is required:<br>
<i>Input string:</i> <code>11,22,33,44,55,66,</code>
```yaml
!PARSE.SEPARATED
what: !PARSE.DIGITS
sep: !PARSE.EXACTLY {what: ","}
end: True
min: 3
max: 7
```

Parse <code>what</code> values separated by <code>sep</code> in <code>[min;max]</code> interval, trailing separator is not presented:<br>
<i>Input string:</i> <code>0..1..2..3</code>
```yaml
!PARSE.SEPARATED
what: !PARSE.DIGITS
sep: !PARSE.EXACTLY {what: ".."}
end: False
min: 3
max: 5
```

</details>


---

## `!PARSE.TRIE`: Parse using starting prefix

Type: _Combinator_.

`!PARSE.TRIE` expression chooses one of the specified prefixes and parse the rest of the input string using the corresponding parser.

Synopsis:

```yaml
!PARSE.TRIE
- <prefix1>: <...>
- <prefix2>: <...>
...
```

!!!tip
	Use `!PARSE.TRIE` to parse multivariance log messages.
  
## Example
_Input string:_ `Received disconnect from 10.17.248.1 port 60290:11: disconnected by user`

```yaml
!PARSE.TRIE
- 'Received disconnect from ': !PARSE.KVLIST
	- CLIENT_IP: !PARSE.UNTIL ' '
	- 'port '
	- CLIENT_PORT: !PARSE.DIGITS
	- ':'
	- !PARSE.CHARS
- 'Disconnected from user ': !PARSE.KVLIST
	- USERNAME: !PARSE.UNTIL ' '
	- CLIENT_IP: !PARSE.UNTIL ' '
	- 'port '
	- CLIENT_PORT: !PARSE.DIGITS
```


---

## `!PARSE.OPTIONAL`: Parse optional pattern

Type: _Combinator_

`!PARSE.OPTIONAL` expression tries to parse the input string using the specified parser. If the parser fails, starting position rolls back to the initial one.


Synopsis:

```yaml
!PARSE.OPTIONAL
what: <...>
```
or shorter version:
```yaml
!PARSE.OPTIONAL <...>
```
  
## Example
_Input strings:_ 

- `mymachine myproc[10]: DHCPACK to ` 
- `mymachine myproc[10]DHCPACK to `

```yaml hl_lines="6-8"
!PARSE.KVLIST
- HOSTNAME: !PARSE.UNTIL {what: ' '} # mymachine
- TAG: !PARSE.UNTIL {what: '['} # myproc
- PID: !PARSE.DIGITS  # 10
- !PARSE.EXACTLY {what: ']'}
- !PARSE.OPTIONAL ':'
- !PARSE.OPTIONAL
	what: !PARSE.SPACE
- NAME: !PARSE.UNTIL {what: ' '}
```


---

## `!PARSE.KV`: Parse key-value pair

Type: _Combinator_


Synopsis:

```yaml
!PARSE.KV
- key: <...>
  prefix: <...>
- value: <...>
- <...> # optional elements
```

!!!tip
	Use  combination of  `!PARSE.REPEAT` and `!PARSE.KV` to parse repeated key-value pairs. (see examples)
 
## Example
_Input string:_ `eventID= "1011"`

```yaml
!PARSE.KV
- key: !PARSE.UNTIL {what: '='}
- !PARSE.SPACE
- value: !PARSE.BETWEEN {what: '"'}
```

_Output:_ `(eventID, 1011)`


<details>
  <summary>More examples</summary>

<i>Input string:</i> <code>eventID= "1011"</code>
```yaml
!PARSE.KV
- key: !PARSE.UNTIL {what: '='}
  prefix: SD.PARAM.
- !PARSE.SPACE
- value: !PARSE.BETWEEN {what: '"'}
```
<i>Output:</i> <code>(SD.PARAM.eventID, 1011)</code><br>
<br>

<i>Input string:</i> <code>devid="FEVM020000191439" vd="root" itime=1665629867</code>
```yaml
!PARSE.REPEAT
what: !PARSE.KV
	- !PARSE.OPTIONAL
	  what: !PARSE.SPACE
	- key: !PARSE.UNTIL '='
	- value: !TRY
			- !PARSE.BETWEEN '"'
			- !PARSE.UNTIL { what: ' ', eof: true}
```
<i>Output:</i> <code>[(devid, FEVM020000191439), (vd, root), (itime, 1665629867)]</code>
</details>


---

## `!PARSE.KVLIST`: Parse list of key-value pairs

Iterating through list of elements `!PARSE.KVLIST` expression collects key-value pairs to list of tuples. Non-key elements are parsed, but not collected.
Nested `!PARSE.KVLIST` expressions are joined to the parent one.

Type: _Combinator_


Synopsis:

```yaml
!PARSE.KVLIST
- <...>
- key1: <...>
- key2: <...>
- <...> 
- !PARSE.KVLIST
  - key3: <...>
  - <...>
- key4: <...>
```

## Example
_Input string:_ `<141>May  9 10:00:00 VUW-DC-F5-P2R1.source-net.com notice tmm1[22731]: 01490500:5: /Common/Citrix_Receiver..`

```yaml
  !PARSE.KVLIST
  # parse Syslog_RFC5424
  - '<'
  - log.syslog.priority: !PARSE.DIGITS
  - '>'
  - '@timestamp': !PARSE.DATETIME
				- month: !PARSE.MONTH 'short'
				- !PARSE.SPACES
				- day: !PARSE.DIGITS # Day
				- !PARSE.SPACES
				- hour: !PARSE.DIGITS # Hours
				- ':'
				- minute: !PARSE.DIGITS # Minutes
				- ':'
				- second: !PARSE.DIGITS # Seconds
				- timezone: "Europe/Prague"
  - !PARSE.SPACES
  - host.hostname: !PARSE.UNTIL ' '
  - log.level: !PARSE.UNTIL ' '
  - log.syslog.appname: !PARSE.UNTIL '['
  - process.pid: !PARSE.DIGITS
  - ']: '
  - message: !PARSE.CHARS
```

_Output:_ `[(log.syslog.priority, 141), (@timestamp, 140994182325993472), (host.hostname, VUW-DC-F5-P2R1.source-net.com), (log.level, notice), (log.syslog.appname, tmm1), (process.pid, 22731), (message, 01490500:5: /Common/Citrix_Receiver..)]`


---

## `!PARSE.TUPLE`: Parse list of values to tuple

Iterating through list of elements `!PARSE.TUPLE` expression collects values to tuple.

Type: _Combinator_


Synopsis:

```yaml
!PARSE.TUPLE
- <...>
- <...>
- <...>

```

## Example
_Input string:_ `Hello world!`

```yaml
!PARSE.TUPLE
- 'Hello'
- !PARSE.SPACE
- 'world'
- '!'
```

_Output:_ `('Hello', ' ', 'world', '!')`



---

## `!PARSE.RECORD`: Parse list of values to record structure

Iterating through list of elements `!PARSE.RECORD` expression collects values to record structure.

Type: _Combinator_


Synopsis:

```yaml
!PARSE.RECORD
- <...>
- element1: <...>
- element2: <...>
- <...>

```

## Example
_Input string:_ `<165>1 `

```yaml
!PARSE.RECORD
- !PARSE.EXACTLY {what: '<'}
- severity: !PARSE.DIGITS
- !PARSE.EXACTLY {what: '>'}
- version: !PARSE.DIGITS
- !PARSE.EXACTLY {what: ' '}
```

_Output:_ `{'output.severity': 165, 'output.version': 1}`
