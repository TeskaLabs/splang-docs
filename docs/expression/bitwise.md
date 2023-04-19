---
title: Bitwise expressions
---

# Bitwise expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

The bit shifts treat a value as a series of bits, the binary digits of the value are moved, or shifted, to the left or right.

_Hint: Left shifts could be used as fast multiplication by 2, 4, 8 and so on._

_Hint: Right shifts could be used as fast division by 2, 4, 8 and so on._

There are also bitwise `!AND`, `!OR` and `!NOT` expression, for details, continue to "Logic" chapter.

--- 

## `!SAL`: Left arithmetic shift {#EXPR-SAL}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!SAL
what: <...>
by: <...>
{% endhighlight %}

### Example

{% highlight yaml %}
!SAL
what: 60
by: 2
{% endhighlight %}


---

## `!SAR`: Right arithmetic shift {#EXPR-SAR}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!SAR
what: <...>
by: <...>
{% endhighlight %}


---

## `!SHL`: Left logical shift {#EXPR-SHL}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!SHL
what: <...>
by: <...>
{% endhighlight %}


---

## `!SHR`: Right logical shift  {#EXPR-SHR}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!SHR
what: <...>
by: <...>
{% endhighlight %}


---

## `!ROL`: Left rotation (circular) shift {#EXPR-ROL}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!ROL
what: <...>
by: <...>
{% endhighlight %}


---

## `!ROR`: Right rotation (circular) shift {#EXPR-ROR}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!ROR
what: <...>
by: <...>
{% endhighlight %}
