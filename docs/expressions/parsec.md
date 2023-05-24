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

## `!PARSE.DIGIT`

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

## `!PARSE.DIGITS`

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

Parse as much digits as possible:
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


