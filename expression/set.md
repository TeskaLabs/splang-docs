---
layout: default
title: SP-Lang documentation
---

# Set expression


* This will become a table of contents (this text will be scrapped).
{:toc}

The set store unique items, without any particular order.
Items in the set must be of the same type.
The set is one of basic data structures provided by SP-Lang.

A set is best suited for a testing value for membership rather than retrieving a specific element from a set.

--- 

## `!SET`: Set of items {#EXPR-SET}

Type:  _Implicit sequence_, _Mapping_.

### Synopsis

{% highlight yaml %}
!SET
- ...
- ...
{% endhighlight %}

_Hint: Use `!COUNT` to determine number of items in the set._


### Examples

There are several ways, how a set can be specified in SP-Lang:

{% highlight yaml %}
!SET
- "One"
- "Two"
- "Three"
- "Four"
- "Five"
{% endhighlight %}


[YAML unordered set](https://yaml.org/spec/1.2.2/#example-unordered-sets):

{% highlight yaml %}
!!set
? Yellow pork
? Pink grass
? White snow
{% endhighlight %}


Consise set using [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):

{% highlight yaml %}
!SET ["One", "Two", "Three", "Four", "Five"]
{% endhighlight %}


The mapping form:

{% highlight yaml %}
!SET
with:
  - "One"
  - "Two"
  - "Three"
  - "Four"
  - "Five"
{% endhighlight %}


--- 

## `!IN`: Membership test

Type: _Mapping_.

The expression `!IN` is described in the "Tests" chapter.

### Example

{% highlight yaml %}
!IN
what: 3
where:
  !SET
  with:
    - 1
    - 2
    - 5
    - 8 
{% endhighlight %}


--- 

## `!GET`: Get the item from the set {#EXPR-SET-GET}

Type: _Mapping_.

The set is also a list, items can be obtains by its numeric index.


### Synopsis

{% highlight yaml %}
!GET
what: <index of the item in the set>
from: <set>
{% endhighlight %}

`index` is an integer (number).

`index` can be negative, in that case, it specifies an item from the end of the set.
Items are indexed from the 0, it means that the first item in the sey has an index 0.

If the `index` is out of bound of the set, the statement returns with error.


### Examples

{% highlight yaml %}
!GET
what: 3
from:
  !SET
  - 1
  - 5
  - 30
  - 50
  - 80
  - 120
{% endhighlight %}

Returns `50`.


{% highlight yaml %}
!GET
what: -1
from:
  !SET
  - 1
  - 5
  - 30
  - 50
  - 80
  - 120
{% endhighlight %}

Returns the last item in the set, which is `120`.

