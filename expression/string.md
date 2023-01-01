---
layout: default
title: SP-Lang documentation
---

# String expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

---

## `!IN`: Test if the string contains a substring {#EXPR-IN}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!IN
what: <...>
where: <...>
{% endhighlight %}

The `!IN` expression is used to check if a string `what` exists in a string `where` or not.
Evaluate to "true" if it finds a substring `what` in the string `where` and false otherwise.

### Example

{% highlight yaml %}
!IN
what: "Willy"
where: "John Willy Boo"
{% endhighlight %}

Check for a presence of the substring "Willy" in the `where` value. Returns "true".


### Multi-string variant

There is a special variant on `!IN` operator for checking if any of strings provided in `what` value (a list in this case) is in the string. It is efficient, optimized implementation of the multi-string matcher.

{% highlight yaml %}
!IN
what:
  - "John"
  - "Boo"
  - "ly"
where: "John Willy Boo"
{% endhighlight %}

This is very efficient way of checking if at least one substring is present in the `where` string.
It provides [Incremental String Matching](http://se.ethz.ch/~meyer/publications/string/string_matching.pdf) algorithm for fast pattern matching in strings.
It makes it an ideal tool for complex filtering as a standalone bit or an optimization technique.

Example of `!REGEX` optimization by multi-string `!IN`:

{% highlight yaml %}
!AND
- !IN
  where: !ARG message
  what:
  - "msgbox"
  - "showmod"
  - "showhelp"
  - "prompt"
  - "write"
  - "test"
  - "mail.com"
- !REGEX
  what: !ARG message
  regex: '(msgbox|showmod(?:al|eless)dialog|showhelp|prompt|write)|(test[0-9])|([a-z]@mail\.com)'
{% endhighlight %}

This approach is recommended from applications in streams, where you need to filter an extensive amount of the data with assumption that only a smaller portion of the data matches the patters.
An application of the `!REGEX` expression directly will slow processing down significantly, because it is complex regular expression.
The idea is to "pre-filter" data with a simplier but faster condition so that only a fraction of the data reaches the expensive `!REGEX`.
The typical performance improvement is 5x-10x.

For that reason, the `!IN` must be a perfect superset of the `!REGEX`, it means:

* `!IN` -> `true`, `!REGEX` -> `true`: `true`
* `!IN` -> `true`, `!REGEX` -> `false`: `false` (this should be a minority of cases)
* `!IN` -> `false`, `!REGEX` -> `false`: `false` (prefiltering, this should be a majority of cases)
* `!IN` -> `false`, `!REGEX` -> `true`: this combination MUST BE avoided, adopt the `!IN` and/or `!REGEX` accordingly.

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

Cut the string by a delimiter and return the piece identified by `field` index (starts with 0).

### Synopsis

{% highlight yaml %}
!CUT
what: <string>
delimiter: <string>
field: <int>
{% endhighlight %}

The argument `value` string will be split using a `delimiter` argument.
The argument `field` specifies a number of the splited strings to return, starting with 0.  
If the negative `field` is provided, then field is taken from the end of the string, for example -2 means the second last substring.


### Example

{% highlight yaml %}
!CUT
what: "Apple,Orange,Melon,Citrus,Pear"
delimiter: ","
field: 2
{% endhighlight %}

Will return value "Melon".


{% highlight yaml %}
!CUT
what: "Apple,Orange,Melon,Citrus,Pear"
delimiter: ","
field: -2
{% endhighlight %}

Will return value "Citrus".

  
---

## `!SPLIT`: Split a string into the list {#EXPR-SPLIT}

Type: _Mapping_

Splits a string into a list of strings.

### Synopsis

{% highlight yaml %}
!SPLIT
what: <string>
delimiter: <string>
maxsplit: <number>
{% endhighlight %}

The argument `what` string will be split using a `delimiter` argument.
An optional `maxsplit` arguments specifies how many splits to do.


### Example

{% highlight yaml %}
!SPLIT
what: "hello,world"
delimiter: ","
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
delimiter: <string>
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
