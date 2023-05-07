---
title: Functions expressions
---

# Functions expressions



--- 

## `!ARGUMENT`, `!ARG`: Get a function argument  

Type: _Mapping_.

### Synopsis

```yaml
!ARGUMENT name
```

```yaml
!ARG name
```

Provides an access to an argument `name`.

`!ARG` is an concise version of `!ARGUMENT`.


--- 

## `!FUNCTION`, `!FN`: Define a function 


Type: _Mapping_.


The `!FUNCTION` expression defines a new function.
It is typically used as a top-level expression.

SP-Lang expressions are by default placed in the implicit function definition.
It means that in a majority of cases, `!FUNCTION` can be skipped, and only `do` section is provided

### Synopsis

```yaml
!FUNCTION
name: <name of function>
arguments:
  arg1: <type>
  arg2: <type>
  ...
returns: <type>
schemas: <dictionary of schemas>
do:
  <expression>
```

```yaml
!FN
...
```


### Example

```yaml
!FUNCTION
arguments:
  a: si64
  b: si32
  c: si32
  d: si32
returns: fp64
do:
  !MUL
  - !ARGUMENT a
  - !ARGUMENT b
  - !ARGUMENT c
  - !ARGUMENT d
```


--- 

## `!SELF`: Apply a current function  

Type: _Mapping_.

The `!SELF` provides an ability to recursivelly apply "self" aka a current function.

```yaml
!SELF
arg1: <value>
arg2: <value>
...
```

_Note: Self expression is a [Y combinator](https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator)._


### Example

Factorial calculation in a SP-Lang:

```yaml
---
!FUNCTION
arguments: {x: int}
returns: int
do:
  !IF # value <= 1
  test: !GT [!ARG x, 1]
  then: !MUL [!SELF {x: !SUB [!ARG x, 1]}, !ARG x]
  else: 1
```
