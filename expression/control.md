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

`!WHEN` expression is considerably more powerful than `!IF` expression.
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

## `!MATCH`: Pattern matching {#EXPR-MATCH}

Type: _Mapping_.


### Synopsis

{% highlight yaml %}
!MATCH
what: <what-expression>
with:
  <value>: <expression>
  <value>: <expression>
  ...
else:
  <expression>
{% endhighlight %}

`!MATCH` expression evaluates the `what-expression`, matching the expression's value to a case clause, and executes `expression` associated with that case.

The `else` branch of the `!MATCH` is optional.
The expression fails with error when no matching `<value>` is found and `else` branch is missing.

    
### Example

Example of `!MATCH`:

{% highlight yaml %}
!MATCH
what: 1
with:
  1: "One"
  2: "Two"
  3: "Three"
else:
  "Other number"
{% endhighlight %}

    
Use of `!MATCH` to structure the code:

{% highlight yaml %}
!MATCH
what: !ARG code
with:
  1: !INCLUDE code-1.yaml
  2: !INCLUDE code-2.yaml
else:
  !INCLUDE code-else.yaml
{% endhighlight %}
  
---

## `!TRY`: Execute till first non-error expression  {#EXPR-TRY}


Type: _Sequence_

### Synopsis

{% highlight yaml %}

!TRY
- <expression>
- <expression>
- <expression>
...
{% endhighlight %}

Iterate thru expression (top down), if the expression return non-null (`None`) result, stop iteration and return that value.
Otherwise continue to the next expression.

Returns `None` (error) when end of the list is reached.


Note: The obsoleted name of this expression was `!FIRST`.
It was obsoleted in November 2022.
    
---

## `!MAP`: Apply the expression on each element in a sequence {#EXPR-MAP}

Type: _Mapping_.

### Synopsis

```yaml
!MAP
what: <sequence>
apply: <expression>
```

The `apply` expression is applied on each element in the `what` sequence with the argument `x` containing the respective item value.
The result is a new list with transformed elements.

### Example

```yaml
!MAP
what: [1, 2, 3, 4, 5, 6, 7]
apply:
  !ADD [!ARG x, 10]
```

Result is `[11, 12, 13, 14, 15, 16, 17]`.

---

## `!REDUCE`: Reduce the sequence into a value {#EXPR-REDUCE}

Type: _Mapping_.
    


### Synopsis

```yaml
!REDUCE
what: <expression>
apply: <expression>
initval: <expression>
direction: left
```
    
The `apply` expression is applied on each element in the `what` sequence with the argument `a` containing an aggregation of the reduce operation and argument 'b' containing the respective item value.
    
The `initval` expression provides the initial value for the `a` argument.
    
The `direction` value specifies a direction in which is the `what` sequence iterated; `left` (default value) means from left to right (from a list beginning to the end), `right` implies from right to left (from the list end to the begin).


### Example

```yaml
!REDUCE
what: [1, 2, 3, 4, 5, 6, 7]
initval: -10
apply:
  !ADD [!ARG a, !ARG b]
```

Calculates a sum of the sequence with an initial value -1, result is `18`: `-10 + 1 + 2 + 3 + 4 + 5 + 6 + 7`.
