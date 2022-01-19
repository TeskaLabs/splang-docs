---
layout: default
title: SP-Lang documentation
---

# Regex expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

_Hint: Use [Regexr](https://regexr.com) to develop and test regular expressions._

--- 

## `!REGEX`: Regular expression match  {#EXPR-REGEX}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!REGEX
what: <string>
regex: <regex>
{% endhighlight %}

Provides an access to an argument `name`.


### Example

{% highlight yaml %}
!REGEX
what: "Hello world!"
regex: "world"
{% endhighlight %}

--- 

## `!REGEX.REPLACE`: Regular expression replace  {#EXPR-REGEX-REPLACE}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!REGEX.REPLACE
what: <string>
regex: <regex>
by: <string>
{% endhighlight %}

Replace regular expression `regex` matches in `what` by value of `by`.


### Example

{% highlight yaml %}
!REGEX.REPLACE
what: "Hello world!"
regex: "world"
by: "Mars"
{% endhighlight %}

Returns: `Hello Mars!`

--- 

## `!REGEX.SPLIT`: Split a string by a regular expression  {#EXPR-REGEX-SPLIT}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!REGEX.SPLIT
what: <string>
regex: <regex>
max: <integer>
{% endhighlight %}

Split string `what` by regular expression `regex`.

An optional argument `max` specify the maximum number of splits.


### Example

{% highlight yaml %}
!REGEX.SPLIT
what: "07/14/2007 12:34:56"
regex: "[/ :]"
{% endhighlight %}

Returns: `['07', '14', '2007', '12', '34', '56']`

--- 

## `!REGEX.FINDALL`: Find all occurences by a regular expression  {#EXPR-REGEX-FINDALL}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!REGEX.FINDALL
what: <string>
regex: <regex>
{% endhighlight %}

Find all matches of `regex` in the string `what`.

### Example

{% highlight yaml %}
!REGEX.FINDALL
what: "Frodo, Sam, Gandalf, Legolas, Gimli, Aragorn, Boromir, Merry, Pippin"
regex: \w+
{% endhighlight %}

Returns: `['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Gimli', 'Aragorn', 'Boromir', 'Merry', 'Pippin']`

---

## `!REGEX.PARSE`: Parse by a regular expression {#EXPR-REGEX-PARSE}

Type: _Mapping_.

