---
layout: default
title: SP-Lang documentation
header: Arithmetics expressions
sidebar: splang
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
