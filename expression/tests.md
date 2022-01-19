---
layout: default
title: SP-Lang documentation
---

# Comparisons and Test expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

Test expression evaluates inputs and returns boolean value `true` or `false` based on the result of the test.

---

## `!EQ`: Equal {#EXPR-EQ}

Type: _Sequence_.


### Example

```yaml
!EQ
- !ARG count
- 3
```

This compares `count` argument with `3`.


---

## `!NE`: Not equal {#EXPR-NE}

Type: _Sequence_.

This is negative counterpart to `!EQ`.


### Example

{% highlight yaml %}
!NE
- !ARG name
- Frodo
{% endhighlight %}


---

## `!LT`: Less than {#EXPR-LT}

Type: _Sequence_.

### Example

{% highlight yaml %}
!LT
- !ARG count
- 5
{% endhighlight %}

Example of a `count < 5` test.


---

## `!LE`: Less than and equal {#EXPR-LE}

Type: _Sequence_.


### Example

{% highlight yaml %}
!LE
- 2
- !ARG count
- 5
{% endhighlight %}

Example of a range `2 <= count <= 5` test.


---

## `!GT`: Greater than {#EXPR-GT}

Type: _Sequence_.

### Example

{% highlight yaml %}
!GT [!ARG count, 5]
{% endhighlight %}

Example of a `count > 5` test using a compacted YAML form.


---

## `!GE`: Greater than  and equal {#EXPR-GE}

Type: _Sequence_.

### Example

{% highlight yaml %}
!GT
- !ARG count
- 5
{% endhighlight %}

Example of a `count >= 5` test.


---

## `!IN`: Membership test {#EXPR-IN}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!IN
what: <...>
where: <...>
{% endhighlight %}

The `!IN` expression is used to check if a value `what` exists in a value `where` or not.
Value `where` is a string, container (list, set, dictionary), structural type etc.
Evaluate to "true" if it finds a value `what` in the specified value `where` and false otherwise.

### Examples

{% highlight yaml %}
!IN
what: 5
where:
  - 1
  - 2
  - 3
  - 4
  - 5
{% endhighlight %}

Check for a presence of the value `5` in the list `where`. Returns "true".


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
