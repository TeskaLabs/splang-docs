---
layout: default
title: SP-Lang Documentation
sidebar: splang
---

# SP-Lang Tutorial


## Hello World

Let's start with the simplest example:

{% highlight yaml %}
---
Hello world!
{% endhighlight %}

Three dashes (`---`) signal a start of the code.

`Hello world!` is a value that you want to return.



## SP-Lang is based on YAML

The SP-Lang is based in the <a href="https://yaml.org">YAML</a>.
The YAML relays heavily on indentation, we recommend to use two spaces, TABs are not supported by YAML.

## Comments

It is a good habit to comment the work.


{% highlight yaml %}
# Hello world in the SP-Lang
---
Hello world!
{% endhighlight %}


## SP-Lang expressions

This code sums two numbers, specifically it calculates `5+8`.


{% highlight yaml %}
---
!ADD
- 5
- 8
{% endhighlight %}

The result is `13`.


All SP-Lang functions starts with `!`.

`!ADD` is the _expression_ for arithmetic *addition* that can sum provided numbers.

Inputs for `!ADD` _expression are provided as a list, because `!ADD` is so called _Sequence expression_.
It means that it can sum multiple input values.

_Hint: "Expression" is just an alternative term to "function"._ 

The list of input values is specified using `- ` in the beginning of the line with the value.
Every line represents an individual item from a list.

{% highlight yaml %}
---
!ADD
- 5
- 8
- 9
- 15
{% endhighlight %}

This is the example of how to provide more inputs for a sequence expression.



## Combining expressions


{% highlight yaml %}
---
!ADD
- 5
- !MUL
  - 6
  - 2
  - 3
- 9
- !SUB
  - 10
  - 5
{% endhighlight %}



## Floating point numbers


{% highlight yaml %}
---
!ADD
- 5.5
- !MUL
  - 6.1
  - 2.2
  - 3.5
- 9
- !SUB
  - 10
  - 5
{% endhighlight %}


