---
layout: default
title: SP-Lang documentation
---

# Logic expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

---

## `!AND`: Conjunction {#EXPR-AND}

Type: _Sequence_

### Boolean `!AND`

Boolean conjunction `!AND` is an boolean functional operation on sequence of logical values, that produces a boolean value of "true" if and only if all of its values are true.

### Bitwise  `!AND`

When `!AND` is applied on integers (instead on boolean) types, it provides a bitwise AND.


---

## `!OR`: Disjunction {#EXPR-OR}

Type: _Sequence_

### Boolean `!OR`

Boolean disjunction is a boolean functional operation which returns the boolean value "true" unless all of its arguments are "false".

### Bitwise `!OR`

When `!OR` is applied on integers (instead on boolean) types, it provides a bitwise OR.


---

## `!NOT`: Negation {#EXPR-NOT}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!NOT
what: <expression>
{% endhighlight %}

### Boolean `!NOT`

Boolean negation is an operation on one boolean value that produces a boolean value of "true" when its operand is "false", and a value of "false" when its operand is "true".

### Bitwise `!NOT`

When integer is provided, then `!NOT` returns value with bits of `what` flipped.

_Hint: If you want to test that integer is not zero, use `!EQ` test expression._
