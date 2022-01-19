---
layout: default
title: SP-Lang documentation
header: Tuple expression
sidebar: splang
---

# Tuple expressions


* This will become a table of contents (this text will be scrapped).
{:toc}

The tuple is one of basic data structures provided by SP-Lang.
A tuple is a collection of items, possibly of different types.

--- 

## `!TUPLE`: A collection of items {#EXPR-TUPLE}

Type:  _Mapping_.

### Synopsis

{% highlight yaml %}
!TUPLE
with:
  - ...
  - ...
  ...
{% endhighlight %}

There is no limit of the number of items in the tuple.
The order of the items is preserved.


### Examples

{% highlight yaml %}
!TUPLE
with:
  - John Doe
  - 37
  - 175.4
{% endhighlight %}


Use of the `!!tuple` notation:

{% highlight yaml %}
!!tuple
- 1
- a
- 1.2
{% endhighlight %}


Even more concise version of the `!!tuple` using flow syntax:

{% highlight yaml %}
!!tuple ['John Doe', 37, 175.4]
{% endhighlight %}


Enforce specific type of the item:

{% highlight yaml %}
!TUPLE
with:
  - John Doe
  - !!ui8 37
  - 175.4
{% endhighlight %}

Item #1 will have a type `ui8`.


--- 

## `!GET`: Get the item from a tuple {#EXPR-TUPLE-GET}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!GET
what: <index of the item>
from: <tuple>
{% endhighlight %}

`what` is an integer (number), it represent the _index_ in a tuple.
`what` can be negative, in that case, it specifies an item from the end of the list.
Items are indexed from the 0, it means that the first item in the list has an index 0.
If the `what` is out of bound of the list, the statement returns with error.


### Examples

{% highlight yaml %}
!GET
what: 1
from:
  !TUPLE
  with:
    - John Doe
    - 32
    - 127.5
{% endhighlight %}

Returns `32`.


Using the _negative index_ of items:

{% highlight yaml %}
!GET
what: -1
from:
  !TUPLE
  with:
    - John Doe
    - 32
    - 127.5
{% endhighlight %}

Returns `127.5`.
