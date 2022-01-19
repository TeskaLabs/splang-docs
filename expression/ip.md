---
layout: default
title: SP-Lang documentation
---

# IP Address expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

IP addresses are represented internally as a number, 128bit unsigned integer.
Such a type can contain both IPv6 and IPv4.
IPv4 are mapped into IPv6 space, using [RFC 4291 "IPv4-Mapped IPv6 Address"](https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.5.2).

--- 

## `!IP.FORMAT`: Convert an IP address into a string  {#EXPR-IP-FORMAT}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!IP.FORMAT
what: <ip>
{% endhighlight %}

Convert the internal representation of the IP address into a string.


### Example

{% highlight yaml %}
!IP.FORMAT
what:
  67305985
{% endhighlight %}

Returns `0:0:0:0:0:0:403:201`.

--- 

## `!IP.INSUBNET`: Check if IP address falls into a subnet {#EXPR-IP-INSUBNET}

Type: _Mapping_.

### Synopsis

{% highlight yaml %}
!IP.FORMAT
what: <ip>
subnet: <string>
{% endhighlight %}

Test if `what` IP address belongs to a `subnet`.


### Example

{% highlight yaml %}
!IP.INSUBNET
what:
  192.168.1.1
subnet:
  192.168.0.0/16
{% endhighlight %}

--- 

## `!IP.PARSE`: Parse a string into the IP address {#EXPR-IP-PARSE}

