---
layout: default
title: SP-Lang documentation
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

## `!MAP`: Transform items in the sequence {#EXPR-MAP}

Type: _Mapping_.

The `apply` expression is applied to all items of a  `on` sequence.

### Synopsis

```yaml
!MAP
apply: <expression>
on: <sequence>
```

`apply` expression is repeatitively called with local argument `a` containing the respective value from `on`.

### Example

```yaml
!MAP
apply: !ADD [!ARG a, 1]
on: [1, 2, 3, 4]
```

Result is `[2, 3, 4, 5]`.



---

## `!REDUCE`: Reduce the sequence into a single value {#EXPR-REDUCE}

Type: _Mapping_.

Iterate through the values in `on` sequence, apply `apply` expression and produce a singular output value.

### Synopsis

```yaml
!REDUCE
apply: <expression>
on: <sequence>
```

`apply` expression is called with local arguments `a` and `b`.


### Example

```yaml
!REDUCE
apply: !ADD [!ARG a, !ARG b]
on: [1, 2, 3, 4]
```

Calculates a sum of the `on` sequence, result is `10`.

