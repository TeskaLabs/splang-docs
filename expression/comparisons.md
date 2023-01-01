---
layout: default
title: SP-Lang documentation
---

# Comparisons expressions

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
