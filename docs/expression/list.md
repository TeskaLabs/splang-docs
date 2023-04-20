---
title: List expressions
---

# List expressions


* This will become a table of contents (this text will be scrapped).
{:toc}

The list is one of basic data structures provided by SP-Lang.
The list contains a finite number of ordered item, where the same item may occur more than once.
Items in the list must be of the same type.

_Note: The list is sometimes also called an array (inaccurately)._


--- 

## `!LIST`: List of items {#EXPR-LIST}

Type:  _Implicit sequence_, _Mapping_.

### Synopsis

{% highlight yaml %}
!LIST
- ...
- ...
{% endhighlight %}

_Hint: Use `!COUNT` to determine number of items in the list._


### Examples

There are several ways, how a list can be specified in SP-Lang:

{% highlight yaml %}
!LIST
- "One"
- "Two"
- "Three"
- "Four"
- "Five"
{% endhighlight %}


Implicit list using [YAML block sequences](https://yaml.org/spec/1.2.2/#821-block-sequences):

{% highlight yaml %}
- "One"
- "Two"
- "Three"
- "Four"
- "Five"
{% endhighlight %}


Implicit list using [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):

{% highlight yaml %}
["One", "Two", "Three", "Four", "Five"]
{% endhighlight %}


The mapping form:

{% highlight yaml %}
!LIST
with:
  - "One"
  - "Two"
  - "Three"
  - "Four"
  - "Five"
{% endhighlight %}

--- 

## `!GET`: Get the item from the list {#EXPR-LIST-GET}

Type: _Mapping_.


### Synopsis

{% highlight yaml %}
!GET
what: <index of the item in the list>
from: <list>
{% endhighlight %}

`index` is an integer (number).

`index` can be negative, in that case, it specifies an item from the end of the list.
Items are indexed from the 0, it means that the first item in the list has an index 0.

If the `index` is out of bound of the list, the statement returns with error.


### Examples

{% highlight yaml %}
!GET
what: 3
from:
  !LIST
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
  !LIST
  - 1
  - 5
  - 30
  - 50
  - 80
  - 120
{% endhighlight %}

Returns the last item in the list, which is `120`.

