---
title: Record expressions
---

# Record expressions


* This will become a table of contents (this text will be scrapped).
{:toc}

The record is one of basic data structures provided by SP-Lang.
A record is a collection of items, possibly of different types.
Items of a record are named (in a contrast to a tuple) by a label.

_Note: The record is built on top of `!TUPLE`._

--- 

## `!RECORD`: A collection of named items {#EXPR-RECORD}

Type:  _Mapping_.

### Synopsis

{% highlight yaml %}
!RECORD
with:
  item1: <item 1>
  item2: <item 2>
  ...
{% endhighlight %}

`item1` and `item2` are labels of respective items in the record.

There is no limit of the number of items in the record.
The order of the items is preserved.

### Examples

{% highlight yaml %}
!RECORD
with:
  name: John Doe
  age: 37
  height: 175.4
{% endhighlight %}


Use of the YAML flow form:

{% highlight yaml %}
!RECORD {with: {name: John Doe, age: 37, height: 175.4} }
{% endhighlight %}


Use of the `!!record` tag:

{% highlight yaml %}
!!record {name: John Doe, age: 37, height: 175.4}
{% endhighlight %}


Enforce specific type of the item:

{% highlight yaml %}
!RECORD
with:
  name: John Doe
  age: !!ui8 37
  height: 175.4
{% endhighlight %}

Field `age` will have a type `ui8`.


--- 

## `!GET`: Get the item from a record {#EXPR-RECORD-GET}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!GET
what: <name or index of the item>
from: <record>
{% endhighlight %}

If `what` is a string, then it is a name of the field in the record.

If `what` is an integer (number), then it is _index_ in the record.
`what` can be negative, in that case, it specifies an item from the end of the list.
Items are indexed from the 0, it means that the first item in the list has an index 0.
If the `what` is out of bound of the list, the statement returns with error.


### Examples

Using names of items:

{% highlight yaml %}
!GET
what: name
from:
  !RECORD
  with:
    name: John Doe
    age: 32
    height: 127.5
{% endhighlight %}

Returns `John Doe`.


Using the _index_ of items:

{% highlight yaml %}
!GET
what: 1
from:
  !RECORD
  with:
    name: John Doe
    age: 32
    height: 127.5
{% endhighlight %}

Returns `32`, a value of `age` item.


Using the _negative index_ of items:

{% highlight yaml %}
!GET
what: -1
from:
  !RECORD
  with:
    name: John Doe
    age: 32
    height: 127.5
{% endhighlight %}

Returns `127.5`, a value of `height` item.
