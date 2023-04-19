---
title: SP-Lang Syntax
---

# SP-Lang Syntax

* This will become a table of contents (this text will be scrapped).
{:toc}

---

SP-Lang syntax is using [YAML 1.2](https://yaml.org/spec/1.2)

## Comments

An comment is marked by a `#` indicator. 

```yaml
# This file contains no
# SP-Lang, only comments.
```


## Numbers

### Integer

```yaml
canonical: 12345
positive decimal: +12345
negative decimal: -12345
octal: 0o14
hexadecimal: 0xC
```


### Floating Point

```yaml
fixed: 1230.15
canonical: 1.23015e+3
exponential: 12.3015e+02
negative infinity: -.inf
not a number: .nan
```


## Strings

```yaml
string: '012345'
string without quotes: You can specify string without any quotation as well
emoji: 😀🚀⭐
```

Quoted strings:

```yaml
unicode: "Sosa did fine.\u263A"
control: "\b1998\t1999\t2000\n"
hex esc: "\x0d\x0a is \r\n"

single: '"Howdy!" he cried.'
quoted: ' # Not a ''comment''.'
```

Multiline strings:

```yaml
|
   _____ _____        _                       
  / ____|  __ \      | |                      
 | (___ | |__) |_____| |     __ _ _ __   __ _ 
  \___ \|  ___/______| |    / _` | '_ \ / _` |
  ____) | |          | |___| (_| | | | | (_| |
 |_____/|_|          |______\__,_|_| |_|\__, |
                                         __/ |
                                        |___/ 
```

The literal style (indicated by `|`) preserves initial spaces.

```yaml
>
  Mark McGwire's
  year was crippled
  by a knee injury.
```

The folded style (denoted by `>`) removes eventual YAML indentation.


## Booleans

```yaml
True boolean: true
False boolean: false
```


## Expressions

All SP-Lang expressions (aka functions) starts with `!`, SP-Lang expressions are therefore YAML _tags_ (`!TAG`).

Expressions can be of thee types:

 - _Mapping_
 - _Sequence_
 - _Scalar_


### Mapping expression

Example:

```yaml
!ENDSWITH
what: FooBar
postfix: Bar
```

A _flow_ form example:

```yaml
!ENDSWITH {what: FooBar, postfix: Bar}
```


More at: [YAML specs, 10.2. Mapping Styles](https://yaml.org/spec/1.1/#id932806)


### Sequence expression

Example:

```yaml
!ADD  
- 1  
- 2  
- 3  
```

A _flow_ form example:

```yaml
!ADD [1, 2, 3]  
```

Sequence expression could be defined using `with` argument as well:

```yaml
!ADD
with: [1, 2, 3]
```

_Note: This is actually a mapping form of the sequence expression._


More at: [YAML specs, 10.1. Sequence Styles](https://yaml.org/spec/1.1/#id931088)


### Scalar expressions

Example:  

```yaml
!ITEM EVENT potatoes
```

More at: [YAML specs, Chapter 9. Scalar Styles](https://yaml.org/spec/1.1/#id903915)

_Note: Scalar expressions are not much used._


## Anchors and Aliases

SP-Lang leverages YAML [anchors](https://yaml.org/spec/1.1/#id899912) and [aliases](https://yaml.org/spec/1.1/#id902561).
It means that you may refer to the result of the other expression by the _anchor_.
The anchor is a string starting with "`&`".
The result of the expression annotated by the anchor can then be reused by the _alias_, which is a string starting with "`*`", sharing the anchor's name.
One anchor can be referenced by many aliases.

Example:

```yaml
!ADD
- 1
- &subcount !MUL
  - 2
  - 3
- *subcount
- *subcount
```

Equals to `1+(2*3)+(2*3)+(2*3)` respective `19`.


## Structure of the SP-Lang file

SP-Lang uses three dashes (`---`) to separate expressions from document content.
This also serves to signal the start of a SP-Lang.
Three dots ( “...”) indicate the end of a file without starting a new one, for use in communication channels.

```yaml
# Let's do some basic math
---
!MUL
- 1
- 2
- 3
```

_Hint: Your SP-Lang expression always starts with `---` line._

_Note: One file can contain more expressions using YAML separator (`---`)._
