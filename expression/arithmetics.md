---
layout: default
title: SP-Lang documentation
---

# Arithmetics expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

---

## `!ADD`: Addition {#EXPR-ADD}

Type: _Sequence_

### Overview

You can add following types:

 * Numbers (Integers and floats)
 * Strings
 * Lists
 * Sets
 * Tuples
 * Records


### Example

{% highlight yaml %}
!ADD
- 4
- -5
- 6
{% endhighlight %}

Calculates `4+(-5)+6`, so the result is `5`.

---

## `!SUB`: Substraction {#EXPR-SUB}

Type: _Sequence_

### Example

{% highlight yaml %}
!SUB
- 3
- 1
{% endhighlight %}

---


## `!MUL`: Multiplication {#EXPR-MUL}

Type: _Sequence_

### Example

{% highlight yaml %}
!MUL
- 1.5
- 5.5
{% endhighlight %}

---


## `!DIV`: Division {#EXPR-DIV}

Type: _Sequence_

### Example

{% highlight yaml %}
!DIV
- 21
- 1.5
{% endhighlight %}


### Division by zero

Division by zero produces the error, which can cascade thru the expression.

`!TRY` expression can be used to handle this situation.
The first item in `!TRY` is a `!DIV` that can produce division by zero error.
The second item is a value that will be returned when such an error occurs.

{% highlight yaml %}
!TRY
- !DIV
  - !ARG input
  - 0.0
- 5.0
{% endhighlight %}

---


## `!POW`: Power {#EXPR-POW}

Type: _Sequence_

### Overview

Power or exponent.

### Example

{% highlight yaml %}
!POW
- 2
- 8
{% endhighlight %}
