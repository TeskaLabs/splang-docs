---
layout: default
title: SP-Lang documentation
header: String expressions
sidebar: splang
---

# String expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

---

## `!STARTSWITH`: Test if the string starts with a prefix {#EXPR-STARTSWITH}

Type: _Mapping_

Returns `true` if `what` string begins with `prefix`.

### Synopsis

{% highlight yaml %}
!STARTSWITH
what: <...>
prefix: <...>
{% endhighlight %}


### Example

{% highlight yaml %}
!STARTSWITH
what: "FooBar"
prefix: "Foo"
{% endhighlight %}

---

## `!ENDSWITH`: Test if the string ends with a postfix {#EXPR-ENDSWITH}

Type: _Mapping_

Returns `true` if `what` string ends with `postfix`.

### Synopsis

{% highlight yaml %}
!ENDSWITH
what: <...>
postfix: <...>
{% endhighlight %}


### Example

{% highlight yaml %}
!ENDSWITH
what: "autoexec.bat"
postfix: ".bat"
{% endhighlight %}

---

## `!SUBSTRING`: Extract part of the string {#EXPR-SUBSTRING}

Type: _Mapping_

Return part of the string `what`, in between `from` and `to` index.

### Synopsis

{% highlight yaml %}
!SUBSTRING
what: <...>
from: <...>
to: <...>
{% endhighlight %}


### Example

{% highlight yaml %}
!SUBSTRING
what: "FooBar"
from: 1
to: 3
{% endhighlight %}

Returns `oo`.

---

## `!LOWER`: Transform string to lower-case {#EXPR-LOWER}

Type: _Mapping_


### Synopsis

{% highlight yaml %}
!LOWER
what: <...>
{% endhighlight %}


### Example

{% highlight yaml %}
!LOWER
what: "FooBar"
{% endhighlight %}

Returns `foobar`.


---

## `!UPPER`: Transform string to upper-case {#EXPR-UPPER}

Type: _Mapping_

### Synopsis

{% highlight yaml %}
!UPPER
what: <...>
{% endhighlight %}


### Example

{% highlight yaml %}
!UPPER
what: "FooBar"
{% endhighlight %}

Returns `FOOBAR`.

---

## `!CUT`: Cut portion of the string {#EXPR-CUT}

Type: _Mapping_

Cut the `what` string by a `delimiter` and return the piece identified by `field` index (starts with 0).

### Synopsis

{% highlight yaml %}
!CUT
what: <...>
delimiter: <...>
field: 0
{% endhighlight %}


### Example

{% highlight yaml %}
!CUT
what: "Foo,Bar"
delimiter: ","
field: 0
{% endhighlight %}

---

## `!SPLIT`: Split a string into the list {#EXPR-SPLIT}

Type: _Mapping_

Splits a string into a list based on the separator.

### Synopsis

{% highlight yaml %}
!SPLIT
value: <...>
separator: <...>
{% endhighlight %}


### Example

{% highlight yaml %}
!SPLIT
value: "hello,world"
separator: ","
{% endhighlight %}


---

## `!JOIN`: Join a list of strings {#EXPR-JOIN}

Type: _Mapping_

### Synopsis

{% highlight yaml %}
!JOIN
items:
  - <...>
  - <...>
delimiter: '-'
miss: ''
{% endhighlight %}

Default `delimiter` is space (" ").

If the item is `None`, then the value of `miss` parameter is used, by default it is empty string.
If `miss` is `None` and  any of `items` is `None`, the result of the whole join is `None`.

### Example

{% highlight yaml %}
!JOIN
items:
  - "Foo"
  - "Bar"
delimiter: ','
{% endhighlight %}
