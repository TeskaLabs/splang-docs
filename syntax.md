---
layout: default
title: SP-Lang Documentation
sidebar: splang
---

# SP-Lang Syntax

* This will become a table of contents (this text will be scrapped).
{:toc}

---

SP-Lang syntax is using [YAML 1.2](https://yaml.org/spec/1.2)


## Numbers

### Integer

{% highlight yaml %}
canonical: 12345
positive decimal: +12345
negative decimal: -12345
octal: 0o14
hexadecimal: 0xC
{% endhighlight %}


### Floating Point

{% highlight yaml %}
fixed: 1230.15
canonical: 1.23015e+3
exponential: 12.3015e+02
negative infinity: -.inf
not a number: .nan
{% endhighlight %}


## Strings

{% highlight yaml %}
string: '012345'
string without quotes: You can specify string without any quotation as well
emoji: 😀🚀⭐
{% endhighlight %}

Quoted strings:

{% highlight yaml %}
unicode: "Sosa did fine.\u263A"
control: "\b1998\t1999\t2000\n"
hex esc: "\x0d\x0a is \r\n"

single: '"Howdy!" he cried.'
quoted: ' # Not a ''comment''.'
{% endhighlight %}

Multiline strings:

{% highlight yaml %}
|
  \//||\/||
  // ||  ||__
{% endhighlight %}

The literal style (indicated by `|`) preserves initial spaces.

{% highlight yaml %}
>
  Mark McGwire's
  year was crippled
  by a knee injury.
{% endhighlight %}

The folded style (denoted by `>`) removes eventual YAML indentation.


## Booleans

{% highlight yaml %}
True boolean: true
False boolean: false
{% endhighlight %}


## Expressions

All SP-Lang expressions (aka functions) starts with `!`, SP-Lang expressions are therefore YAML _tags_ (`!TAG`).

Expressions can be of thee types:

 - _Mapping_
 - _Sequence_
 - _Scalar_


### Mapping expression

Example:

{% highlight yaml %}
!ENDSWITH
what: FooBar
postfix: Bar
{% endhighlight %}

A _flow_ form example:

{% highlight yaml %}
!ENDSWITH {what: FooBar, postfix: Bar}
{% endhighlight %}


More at: [YAML specs, 10.2. Mapping Styles](https://yaml.org/spec/1.1/#id932806)



### Sequence expression

Example:

{% highlight yaml %}
!ADD  
- 1  
- 2  
- 3  
{% endhighlight %}

A _flow_ form example:

{% highlight yaml %}
!ADD [1, 2, 3]  
{% endhighlight %}

Sequence expression could be defined using `with` argument as well:

{% highlight yaml %}
!ADD
with: [1, 2, 3]
{% endhighlight %}

_Note: This is actually a mapping form of the sequence expression._


More at: [YAML specs, 10.1. Sequence Styles](https://yaml.org/spec/1.1/#id931088)


### Scalar expressions

Example:  

{% highlight yaml %}
!ITEM EVENT potatoes
{% endhighlight %}

More at: [YAML specs, Chapter 9. Scalar Styles](https://yaml.org/spec/1.1/#id903915)

_Note: Scalar expressions are not much used._


## Comments

An comment is marked by a `#` indicator. 

{% highlight yaml %}
# This file contains no
# SP-Lang, only comments.
{% endhighlight %}


## Structure of the SP-Lang file

SP-Lang uses three dashes (`---`) to separate expressions from document content.
This also serves to signal the start of a SP-Lang.
Three dots ( “...”) indicate the end of a file without starting a new one, for use in communication channels.

{% highlight yaml %}
# Let's do some basic math
---
!MUL
- 1
- 2
- 3
{% endhighlight %}

_Hint: Your SP-Lang expression always starts with `---` line._

_Note: One file can contain more expressions using YAML separator (`---`)._
