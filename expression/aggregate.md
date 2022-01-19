---
layout: default
title: SP-Lang documentation
header: Aggregate expressions
sidebar: splang
---

# Aggregate expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

---

## `!AVG`: Average {#EXPR-AVG}

Type: _Sequence_

Calculate the average / arithmetic mean.

[More information](https://en.wikipedia.org/wiki/Arithmetic_mean) (Wikipedia)

### Example

{% highlight yaml %}
!AVG
- 1
- 2
- 3
{% endhighlight %}

Calculation of the average `(1+2+3)/3`,  the result is `2`.

---

## `!MAX`: Maximum {#EXPR-MAX}

Type: _Sequence_

Returns a maximum value from the seqence.


### Example

{% highlight yaml %}
!MAX
- 1.5
- 2.6
- 3.05
- 4.45
- 5.1
{% endhighlight %}


---

## `!MIN`: Minimum {#EXPR-MIN}

Type: _Sequence_

Returns a minimum value from the seqence.

### Example

{% highlight yaml %}
!MIN
- 0.5
- 2.6
- 3.05
- 4.45
- 5.1
{% endhighlight %}

---

## `!COUNT`: Count number of elements {#EXPR-COUNT}

Type: _Sequence_

### Example

{% highlight yaml %}
!COUNT
- Frodo Baggins
- Sam Gamgee
- Gandalf
- Legolas
- Gimli
- Aragorn
- Boromir of Gondor
- Merry Brandybuck
- Pippin Took
{% endhighlight %}

Returns `9`.

---

## `!MEDIAN`: The middle value {#EXPR-MEDIAN}

Type: _Sequence_

[More information](https://en.wikipedia.org/wiki/Median) (Wikipedia)


### Example

{% highlight yaml %}
!MEDIAN
- 1
- 4
- -1
- 9
- 101
{% endhighlight %}

---

## `!MODE`: Value that appears most often {#EXPR-MODE}

Type: _Sequence_

[More information](https://en.wikipedia.org/wiki/Mode_%28statistics%29) (Wikipedia)


### Example

{% highlight yaml %}
!MODE
- -10
- -10
- -20
- -20
- 1
- 2
- 3
- 4
- 5
{% endhighlight %}

---

## `!RANGE`: The difference between the largest and smallest value {#EXPR-RANGE}

Type: _Sequence_

Calculates the difference between the largest and smallest values.

[More information](https://en.wikipedia.org/wiki/Range_%28statistics%29) (Wikipedia)

### Example

{% highlight yaml %}
!RANGE
- 1
- 3
- 4
- 20
- -1
{% endhighlight %}
