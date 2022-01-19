---
layout: default
title: SP-Lang documentation
---

# Functions expressions

* This will become a table of contents (this text will be scrapped).
{:toc}


--- 

## `!ARGUMENT`, `!ARG`: Get a function argument  {#EXPR-ARG}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!ARGUMENT name
{% endhighlight %}

Provides an access to an argument `name`.

`!ARG` is an concise version of `!ARGUMENT`.


--- 

## `!FUNCTION`, `!FN`: Define a function {#EXPR-FUNCTION}


Type: _Mapping_.


The `!FUNCTION` expression defines a new function.
It is typically used as a top-level expression.

SP-Lang expressions are by default placed in the implicit function definition.
It means that in a majority of cases, `!FUNCTION` can be skipped, and only `do` section is provided

### Synopsis

{% highlight yaml %}
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
{% endhighlight %}


### Example

{% highlight yaml %}
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
{% endhighlight %}


--- 

## `!SELF`: A current function  {#EXPR-SET}

Type: _Mapping_.

Represents a current function.
The `!SELF` provides an ability to recursivelly call "self".

{% highlight yaml %}
!SELF
  arg1: <value>
  arg2: <value>
  ...
{% endhighlight %}

_Note: Self expression is a [Y combinator](https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator)._


### Example

Factorial calculation in a SP-Lang:

{% highlight yaml %}
---
!FUNCTION
arguments:
  x: int
returns: int

do:
  !IF
  test:
    !LE # value <= 1
    - !ARGUMENT x
    - 1
  then:
    1
  else:
    !MUL
    - !SELF
      x:
        !SUB
        - !ARGUMENT x
        - 1
    - !ARGUMENT x
{% endhighlight %}
