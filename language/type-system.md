---
layout: default
title: SP-Lang Documentation
---

# SP-Lang Type system

This is detailed description of the type system used in SP-Lang.

* This will become a table of contents (this text will be scrapped).
{:toc}

# Scalar types

## Integers


<table class="table">
<colgroup>
	<col />
	<col />
</colgroup>

<colgroup>
	<col class="bg-gray"/>
	<col class="bg-gray"/>
</colgroup>

<colgroup>
	<col />
	<col />
</colgroup>

<thead>
  <tr class="bg-gray">
    <th>Type</th><th>Name</th>
    <th>Type</th><th>Name</th>
    <th>Bits</th><th>Bytes</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>si8</code></td><td>Signed 8bit integer</td>
    <td><code>ui8</code></td><td>Unsigned 8bit integer</td>
    <td>8</td><td>1</td>
  </tr>
  <tr>
    <td><code>si16</code></td><td>Signed 16bit integer</td>
    <td><code>ui16</code></td><td>Unsigned 16bit integer</td>
    <td>16</td><td>2</td>
  </tr>
  <tr>
    <td><code>si32</code></td><td>Signed 32bit integer</td>
    <td><code>ui32</code></td><td>Unsigned 32bit integer</td>
    <td>32</td><td>4</td>
  </tr>
  <tr>
    <td><code>si64</code></td><td>Signed 64bit integer</td>
    <td><code>ui64</code></td><td>Unsigned 64bit integer</td>
    <td>64</td><td>16</td>
  </tr>
  <tr>
    <td><code>si128</code></td><td>Signed 128bit integer</td>
    <td><code>ui128</code></td><td>Unsigned 128bit integer</td>
    <td>128</td><td>32</td>
  </tr>
  <tr>
    <td><code>si256</code></td><td>Signed 256bit integer</td>
    <td><code>ui256</code></td><td>Unsigned 256bit integer</td>
    <td>256</td><td>64</td>
  </tr>
</tbody>
</table>

A preferred (default) integer type is `si64` (signed 64bit integer), followed by `ui64` (unsigned 64bit integer).
This is because SP-Lang is designed primarily for 64bit CPUs.

`int` is the alias for `si64`.

_Warning: 256bit sizes are not fully supported yet._



## Boolean

`ui1`, alias `bool`

_Note: `si1` exists and it is technically also (kind of) boolean but `ui1` is preferred._



## Floating-Point

<table class="table" style="width: 30em;">
<thead>
  <tr class="bg-gray">
    <th>Type</th><th>Name</th><th>Bytes</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>fp16</code></td><td>16bit Float</td><td>2</td>
  </tr>
  <tr>
    <td><code>fp32</code></td><td>32bit Float</td><td>4</td>
  </tr>
  <tr>
    <td><code>fp64</code></td><td>64bit Float</td><td>8</td>
  </tr>
  <tr>
    <td><code>fp128</code></td><td>128bit Float</td><td>16</td>
  </tr>
</tbody>
</table>

Warning: Alias `float` translates to `fp64` which translates to LLVM `double` (different from alias `float`).

_Warning: `fp16` and `fp128` are not fully supported._


# Complex scalar types

Complex scalar types are designed for values that provides some internal structure (so technically they are records or tuples) but they can fit into a scalar type (e.g. for performance or optimisation purposes).


## Date/Time

`datetime`

This is a value that represents a date and time in the UTC, using broken time structure.
Broken time means that `year`, `month`, `day`, `hour`, `minute`, `second` and `microsecond` are stored in dedicated fields; different from the e.g. UNIX timestamp.

* Timezone: UTC
* Resolution: microseconds (six decimal digits)
* 64bit unsigned integer, aka `ui64`


### Broken time components

* `y` / `year`
* `m` / `month`
* `d` / `day`
* `H` / `hour`
* `M` / `minute`
* `S` / `second`
* `u` / `microsecond`


## IP Address

`ip`

Underlying scalar type: `ui128`

IPv4 are mapped into IPv6 space, using [RFC 4291 "IPv4-Mapped IPv6 Address"](https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.5.2).


## IP Subnetwork

`ipsubnet`

Used to store IP [subnetwork](https://en.wikipedia.org/wiki/Subnetwork), specifically the IP of the network (stored as `ip`) and netmask.


# Generic types

Generic types are used in the early stage of the SP-Lang parsing, optimization and compilation.
The complementary type is "Specific type".
The SP-Lang resolves generic types into specific types by the mechanism called _type inference_.
If generic type cannot be resolved into specific, the compilation will fail and you need to provide more information for a type inference.

The generic type starts with capital `T`.
Also if the container type contains generic type, the _container type_ or _structural type_ itself is considered generic.


# Structural types

A structural type is a kind of composite type, i.e., a type formed by combining other types.


## Tuple


Signature: `(T1, T2, T3, ...)`

It is equivalent to a [structure type](https://llvm.org/docs/LangRef.html#structure-type) in LLVM IR.


## Record

Signature: `(name1: T1, name2: T2, name3: T3, ...)`


It is is equivalent to a C `struct`.


# Container types


## List

`[Ti]`

* `Ti` refers to a type of the item in the list


The list must contain a zero, one or many items of *the same type*.


## Set

`{Ti}`

 * `Ti` refers to a type of the item in the set


## Dictionary

`{Tk:Tv}`

 * `Tk` refers to a type of the key
 * `Tv` refers to a type of the value


# Object types

## String

`str`

Must be in UTF-8 encoding.

_Note: `str` could be casted to `[ui8]` (list of `ui8`) in 'toll-free' manner; it is the binary equivalent._


## Any

`any`

"Any" type can represent any other type.
It shouldn't be used as a primary data type because it has an overhead but it is rather useful for typing of the dictionary that combines types (e.g. `{str:any}`) and other situations where type is not certain in the compile type.


## None

`none`

Represent a `None` type.

_Note: None type is a special in a way, that this represents a failure in the SP-Lang, so basically any function can indicate failure._



## Bytes

Planned.


## Enum

Planned.



## Regex

`regex`

Contains compiled pattern for a regular expression.

If the regex pattern is constant, then it is compiled during the respective expression compile time.
In the case of dynamic regex pattern, the regex compilation happens during the expression evaluation.


## JSON

`json`

Contains record-like JSON object.


# Function Type

## Function


`(arg1:T1,arg2:T2,arg3:T3)->Tr`

* `T1`, `T2`, `T3` are types of functions inputs `arg1`, `arg2` and `arg3` respectively.
* `Tr` specifies the output type of the function


# Pythonic types

Pythonic types are object types that provides interfacing with the Python.


## Python Object

`pyobj`

A generic [Python object](https://docs.python.org/3/c-api/object.html).


## Python Dictionary

`pydict`

A [Python dictionary](https://docs.python.org/3/c-api/dict.html).


## Python List

`pylist`

A [Python list](https://docs.python.org/3/c-api/list.html).



## Python Tuple

`pytuple`



# Casting

Use `!CAST` expression for change of the type of a value.

{% highlight yaml %}
!CAST
what: 1234
type: fp32
{% endhighlight %}

or an equivalent shortcut:

{% highlight yaml %}
!!fp32 1234
{% endhighlight %}

Note: Cast is also a great helper for type inference, it means that it could be used to indicate the the type explicitly, if needed.

