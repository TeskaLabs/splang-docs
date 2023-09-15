---
title: Functions
---

# Functions expressions



--- 

## `!ARGUMENT`, `!ARG`: Get a function argument  

Type: _Scalar_.

Synopsis:

```yaml
!ARGUMENT name
```

```yaml
!ARG name
```

Provides an access to an argument `name`.

!!! tip

    `!ARG` is an concise version of `!ARGUMENT`.


--- 

## `!FUNCTION`, `!FN`: Define a function 


The `!FUNCTION` expression defines a new function.
It is typically used as a top-level expression.

Type: _Mapping_.


!!! info

    SP-Lang expressions are _implicitly_ placed function definition.
    It means that in a majority of cases, `!FUNCTION` can be skipped, and only `do` section is provided


Synopsis:

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

!!! tip

    `!FN` is an concise version of `!FUNCTION`.


!!! example

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

    This expression defines a function that takes four arguments (`a`, `b`, `c`, and `d`) with respective data types (`si64`, `si32`, `si32`, and `si32`) and returns a result of type `fp64`.
    The function multiplies the four input arguments (`a`, `b`, `c`, and `d`) and returns the product as a floating-point number (`fp64`).

--- 

## `!SELF`: Apply a current function  

The `!SELF` provides an ability to recursively apply "self" aka a current function.

Type: _Mapping_.

Synopsis:

```yaml
!SELF
arg1: <value>
arg2: <value>
...
```

!!! note

    `!SELF` expression is the so called [Y combinator](https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator).


!!! example


	```yaml
	!FUNCTION
	arguments: {x: int}
	returns: int
	do:
	  !IF # value <= 1
	    test: !GT [!ARG x, 1]
	    then: !MUL [!SELF {x: !SUB [!ARG x, 1]}, !ARG x]
	   else: 1
	```

	This expression defines a recursive function that takes a single integer argument `x` and returns an integer result.
	The function calculates the factorial of the input argument `x` using an if-else statement.
	If the input value `x` is greater than 1, the function multiplies `x` by the factorial of (`x` - 1), computed by calling itself recursively.
	If the input value `x` is 1 or less, the function returns 1.
