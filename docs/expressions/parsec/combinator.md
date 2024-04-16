---
title: Combinator expressions
---

# Combinator expressions

## Overview

Combinators are functions for composing parsec expressions (parsers or another combinators) together.
They specify how parsing is applied, what is the output type. They can be used for the flow control of parsing (applying conditional or repeated expressions) and also for lookahead searching in the input string.

**Output selectors** determine the type of output:

- [`!PARSE.KVLIST`](#parsekvlist-parse-list-of-key-value-pairs): Parse sequence of keys and values into [bag type](../../language/types.md#bag).
- [`!PARSE.KV`](#parsekv-parse-key-value-pair): Parse key and value from the input string.
- [`!PARSE.TUPLE`](#parsetuple-parse-list-of-values-to-tuple): Parse into [tuple type](../tuple.md).
- [`!PARSE.RECORD`](#parserecord-parse-list-of-values-to-record-structure)

**Flow control** expressions can perform sequence of parser expressions based on certain conditions:

- [`!PARSE.REPEAT`](#parserepeat-parse-a-repeated-pattern): Performs the same sequence of expressions multiple times, similarly to "for" statement from different languages.
- [`!PARSE.SEPARATED`](#parseseparated-parse-a-sequence-with-a-separator)
- [`!PARSE.OPTIONAL`](#parseoptional-parse-optional-pattern): Adds optional parser function, similarly to "if/else" statement from different languages.
- [`!PARSE.TRIE`](#parsetrie-parse-using-starting-prefix): Performs the sequence of expressions based on the input string prefix.

**Lookahead** expressions:

- [`!PARSE.CHARS.LOOKAHEAD`](#parsecharslookahead-parse-chars-applying-lookahead-group): Parse until certain sequence of characters is found in the string.

---

## `!PARSE.KVLIST`: Parse list of key-value pairs

Type: _Combinator_

Iterating through list of elements `!PARSE.KVLIST` expression collects key-value pairs to [bag](../../language/types.md#bag).

Synopsis:
```yaml
!PARSE.KVLIST
- <...>
- key: <...>
```

Non-key elements are parsed, but not collected:

```yaml
!PARSE.KVLIST
- <...>  # parsed, but not collected
- key1: <...>  # parsed and collected
- key2: <...>  # parsed and collected
```

Nested `!PARSE.KVLIST` expressions are joined to the parent one:

```yaml
!PARSE.KVLIST
- <...>
- !PARSE.KVLIST  # expression is joined to the parent one
  - key3: <...>
  - <...>
- key4: <...>
```

!!! example

	_Input string:_

	```
	<141>May  9 10:00:00 myhost.com notice tmm1[22731]: User 'user' was logged in.
	```

	```yaml
	!PARSE.KVLIST
	- '<'
	- PRI: !PARSE.DIGITS
	- '>'
	- TIMESTAMP: !PARSE.DATETIME
					- month: !PARSE.MONTH 'short'
					- !PARSE.SPACES
					- day: !PARSE.DIGITS # Day
					- !PARSE.SPACES
					- hour: !PARSE.DIGITS # Hours
					- ':'
					- minute: !PARSE.DIGITS # Minutes
					- ':'
					- second: !PARSE.DIGITS # Seconds

	- !PARSE.SPACES
	- HOSTNAME: !PARSE.UNTIL ' '
	- LEVEL: !PARSE.UNTIL ' '
	- PROCESS.NAME: !PARSE.UNTIL '['
	- PROCESS.PID: !PARSE.DIGITS
	- ']:'
	- !PARSE.SPACES
	- MESSAGE: !PARSE.CHARS
	```

	_Output:_ 
	
	```
	[
		(PRI, 141),
		(TIMESTAMP, 140994182325993472),
		(HOSTNAME, myhost.com),
		(LEVEL, notice),
		(PROCESS.NAME, tmm1),
		(PROCESS.PID, 22731),
		(MESSAGE, User 'user' was logged in.)
	]
	```


---

## `!PARSE.KV`: Parse key-value pair

Type: _Combinator_

Parse key and value from a string into key-value pair, with the possibility of adding a certain prefix.

Synopsis:

```yaml
!PARSE.KV
- prefix: <...>
- key: <...>
- value: <...>
- <...> # optional elements
```

- `prefix` is optional. If specified, the prefix will be added to the `key`.
- `key` and `value` are required.


!!! tip
	Use  combination of  `!PARSE.REPEAT` and `!PARSE.KV` to parse repeated key-value pairs. (see examples)

!!! example

	_Input string:_ `eventID= "1011"`

	```yaml
	!PARSE.KV
	- key: !PARSE.UNTIL '='
	- !PARSE.SPACE
	- value: !PARSE.BETWEEN {what: '"'}
	```

	_Output:_ `(eventID, 1011)`

??? example "Parse key and value with a specified prefix"

	_Input string:_ `eventID= "1011"`

	```yaml
	!PARSE.KV
	- key: !PARSE.UNTIL {what: '='}
	prefix: SD.PARAM.
	- !PARSE.SPACE
	- value: !PARSE.BETWEEN {what: '"'}
	```
	_Output:_ `(SD.PARAM.eventID, 1011)`

??? example "Usage together with `!PARSE.REPEAT`"

	_Input string:_ `devid="FEVM020000191439" vd="root" itime=1665629867`

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

	_Output:_
	```
	[
		(devid, FEVM020000191439),
		(vd, root),
		(itime, 1665629867)
	]
	```

---

## `!PARSE.TUPLE`: Parse list of values to tuple

Type: _Combinator_

Iterating through list of elements `!PARSE.TUPLE` expression collects values to [tuple](../tuple.md).

Synopsis:

```yaml
!PARSE.TUPLE
- <...>
- <...>
- <...>

```

!!! example

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

!!! example

	_Input string:_ `<165>1 `

	```yaml
	!PARSE.RECORD
	- '<'
	- severity: !PARSE.DIGITS
	- '>'
	- version: !PARSE.DIGITS
	- ' '
	```

	_Output:_ `{'output.severity': 165, 'output.version': 1}`



## `!PARSE.REPEAT`: Parse a repeated pattern

Type: _Combinator_.

Synopsis:

```yaml
!PARSE.REPEAT
what: <expression>
min: <...>
max: <...>
exactly: <...>
```

- If neither of `min`, `max`, `exactly` is specified, `what` will be repeated as many times as possible.
- `exactly` determines the exact number of repetitions.
- `min` and `max` set minimal and maximal number of repetitions.

!!! example

	_Input string:_ `host:myhost;ip:192.0.0.1;user:root;`

	```yaml
	!PARSE.KVLIST
	- !PARSE.REPEAT
	what: !PARSE.KV
		- key: !PARSE.UNTIL ':'
		- value: !PARSE.UNTIL ';'
	```

	This will repeat the `!PARSE.KV` expression as many times as possible.

	_Output:_
	```
	[
		(host, myhost),
		(ip, 192.0.0.1),
		(user, root)
	]
	```

??? Parse exactly three times

	_Input string:_ `hello hello hello Anna!`

	```yaml
	!PARSE.KVLIST
	- !PARSE.REPEAT
		what: !PARSE.EXACTLY 'hello '
		exactly: 3
	- NAME: !PARSE.UNTIL '!'
	```

	_Output_: `[(NAME, Anna)]`

??? Parse between 2 and 4 times

	_Input strings:_

	```
	hello hello Anna!
	hello hello hello Anna!
	hello hello hello hello Anna!
	```

	```yaml
	!PARSE.KVLIST
	- !PARSE.REPEAT
		what: !PARSE.EXACTLY 'hello '
		min: 2
		max: 4
	- NAME: !PARSE.UNTIL '!'
	```

	_Output_: `[(NAME, Anna)]`

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

- `min` and `max` are optional.
- `end` indicates if trailing separator is required. By default, it is optional.

!!! example
	_Input string:_ `0->1->2->3`

	```yaml
	!PARSE.SEPARATED
	what: !PARSE.DIGITS
	sep: !PARSE.EXACTLY {what: "->"}
	min: 3
	```

	_Output:_ `[0, 1, 2, 3]`

	*Note:* the trailing separator is optional, so input string `0->1->2->3->` is also valid.

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


## `!PARSE.OPTIONAL`: Parse optional pattern

Type: _Combinator_

`!PARSE.OPTIONAL` expression tries to parse the input string using the specified parser.
If the parser fails, starting position rolls back to the initial one.

Synopsis:

```yaml
!PARSE.OPTIONAL
what: <...>
```

or shorter version:

```yaml
!PARSE.OPTIONAL <...>
```


!!! example
	_Input strings:_ 

	```
	mymachine myproc[10]: DHCPACK to
	mymachine myproc[10]DHCPACK to
	```

	```yaml hl_lines="6-8"
	!PARSE.KVLIST
	- HOSTNAME: !PARSE.UNTIL ' ' # mymachine
	- TAG: !PARSE.UNTIL '[' # myproc
	- PID: !PARSE.DIGITS  # 10
	- !PARSE.EXACTLY ']'

	# Parsing of optional characters
	- !PARSE.OPTIONAL ':'
	- !PARSE.OPTIONAL
		what: !PARSE.SPACE

	- NAME: !PARSE.UNTIL ' '
	```


## `!PARSE.TRIE`: Parse using starting prefix

Type: _Combinator_.

`!PARSE.TRIE` expression chooses one of the specified prefixes and parse the rest of the input string using the corresponding parser.
If empty prefix is specified, the corresponding parser will be used in case other prefixes are not matched.

Synopsis:

```yaml
!PARSE.TRIE
- <prefix1>: <...>
- <prefix2>: <...>
...
```

!!! tip
	Use `!PARSE.TRIE` to parse multivariance log messages.

!!! example

	_Input strings:_

	```
	Received disconnect from 10.17.248.1 port 60290:11: disconnected by user
	Disconnected from user root 10.17.248.1 port 60290
	```

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

??? Specify empty prefix for unmatched cases

	_Input string:_ `Failed password for root from 218.92.0.190`

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
	- '': !PARSE.KVLIST
		- tags: ["trie-match-fail"]
	```

	_Output:_ `[(tags, ["trie-match-fail"])]`


---


## `!PARSE.CHARS.LOOKAHEAD`: Parse chars applying lookahead group

Type: _Combinator_

Parse chars until specified lookahead group is found and stop before it.

Synopsis:

```yaml
!PARSE.CHARS.LOOKAHEAD
what:
- <...>
- <...>
- <...>
...
eof: <true/false>
```

- `eof` - indicates if we should parse till the end of the string if `what` lookahead group is not found.
			Possible values: `true`(default) or `false`.


!!! example
	_Input string:_ `Rule Name cs=Proxy `

	```yaml
	!PARSE.CHARS.LOOKAHEAD
	what:
	- " "
	- !PARSE.LETTERS
	- '='
	```

	_Output:_ `Rule Name`
