---
layout: default
title: SP-Lang documentation
header: Control expressions
sidebar: splang
---

# Control expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

SP-Lang provides a variety of control flow statements. 

--- 

## `!IF`: Simple conditional branching  {#EXPR-IF}

Type: _Mapping_.


The `!IF` expression is a decision-making expression that guides the evaluation to make decisions based on specified test.

### Synopsis

{% highlight yaml %}
!IF
test: <expression>
then: <expression>
else: <expression>
{% endhighlight %}


`test` should provide boolean value, based on this value `then` (for `true`) or `else` (for `false`) branch is evaluated.

`then` and `else` have to return the same type, which will be also the type of the `!IF` return value.


### Example

{% highlight yaml %}
!IF
test:
  !EQ
  - !ARG input
  - 2
then:
  It is two.
else:
  It is NOT two.
{% endhighlight %}


---

## `!WHEN`: Powerful branching  {#EXPR-WHEN}

Type: _Sequence_.

`!WHEN` expression is condiderably more powerful than `!IF` expression.
Cases can match many different patterns, including interval matches, tuples, and so on. 


### Synopsis

{% highlight yaml %}
!WHEN
- test: <expression>
  then: <expression>

- test: <expression>
  then: <expression>

- test: <expression>
  then: <expression>

- ...

- else: <expression>
{% endhighlight %}


If `else` is not provided, then `WHEN` returns `False`.


### Example

Example of `!WHEN` use for exact match, range match and set match:

{% highlight yaml %}
!WHEN

# Exact value match
- test:
    !EQ
    - !ARG key
    - 34
  then:
    "Thirty four"

# Range match
- test:
    !LT
    - 40
    - !ARG key
    - 50
  then:
    "fourty to fifty (exclusive)"

# In-set match
- test:
    !IN
    what: !ARG key
    where:
      - 75
      - 77
      - 79
  then:
    "seventy five, seven, nine"


- else:
    "Unknown"
{% endhighlight %}

--- 

## `!FIRST`: Execute till first non-error expression  {#EXPR-WHEN}


Type: _Sequence_

### Synopsis

{% highlight yaml %}

!FIRST
- <expression>
- <expression>
- <expression>
...
{% endhighlight %}

Iterate thru expression (top down), if the expression return non-null (`None`) result, stop iteration and return that value. Otherwise continue to the next expression.

Returns `None` (error) when end of the list is reached.


---

## `!MAP`: TODO  {#EXPR-MAP}

Type: _Mapping_.

Apply `do` for each item in `each`.


### Synopsis

{% highlight yaml %}
!FOR
  each: <...>
  do: <...>
{% endhighlight %}
