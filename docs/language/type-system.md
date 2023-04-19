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

A Boolean (`bool`) is a type that has one of two possible values denoted `True` and `False`.


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


# Generic types

Generic types are used in the early stage of the SP-Lang parsing, optimization and compilation.
The complementary type is "Specific type".
The SP-Lang resolves generic types into specific types by the mechanism called _type inference_.
If generic type cannot be resolved into specific, the compilation will fail and you need to provide more information for a type inference.

The generic type starts with capital `T`.
Also if the container type contains generic type, the _container type_ or _structural type_ itself is considered generic.


# Container types


## List

`[Ti]`

* `Ti` refers to a type of the item in the list


The list must contain a zero, one or many items of *the same type*.

The type constructor is `!LIST` expression.


## Set

`{Ti}`

 * `Ti` refers to a type of the item in the set

The type constructor is `!SET` expression.


## Dictionary

`{Tk:Tv}`

 * `Tk` refers to a type of the key
 * `Tv` refers to a type of the value

The type constructor is `!DICT` expression.


# Product types

A [product type](https://en.wikipedia.org/wiki/Product_type) is a compounded type, formed by combining other types into a _structure_.


## Tuple


Signature: `(T1, T2, T3, ...)`

The type constructor is `!TUPLE` expression.

It is equivalent to a [structure type](https://llvm.org/docs/LangRef.html#structure-type) in LLVM IR.

_Note:_ A tuple with no members respectively `()` is the [unit](https://en.wikipedia.org/wiki/Unit_type).


## Record

Signature: `(name1: T1, name2: T2, name3: T3, ...)`

The type constructor is `!RECORD` expression.

It is is equivalent to a C `struct`.


# Sum type

A [Sum type](https://en.wikipedia.org/wiki/Tagged_union) is a data structure used to hold a value that could take on several different types.

## Any

`any`

The `any` type is a special type that represents a value that can have any type.

The `any` type shouldn't be used as a preferred type because it has an overhead.
Still, it is rather helpful for typing the dictionary that combines types (e.g. `{str:any}`) and other situations where the type of the value is not known in the compile type.

The value contained in `any` type is always located in the memory (e.g., pool); for this reason, this type is slower than others, which store value preferably in CPU registers.

The `any` is a recursive type; it can contain itself because it contains all other types in the type universe.
For this reason, it is impossible to calculate the generic or even maximum size of the `any` variable.


# Object types

## String

`str`

Must be in UTF-8 encoding.

_Note: `str` could be casted to `[ui8]` (list of `ui8`) in 'toll-free' manner; it is the binary equivalent._


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

`json<SCHEMA>`

JSON object, result of the JSON parsing.
It is schema-based type.


# Function Type

## Function


`(arg1:T1,arg2:T2,arg3:T3)->Tr`

* `T1`, `T2`, `T3` are types of functions inputs `arg1`, `arg2` and `arg3` respectively.
* `Tr` specifies the output type of the function


# Pythonic types

Pythonic types are object types that provides interfacing with the Python.


## Python Dictionary

`pydict<SCHEMA>`

A [Python dictionary](https://docs.python.org/3/c-api/dict.html).
It is a schema-based type.


## Python Object

`pyobj`

A generic [Python object](https://docs.python.org/3/c-api/object.html).


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


# Schema-based types

_Schema_ is the SP-Lang concept of how to bridge schema-less systems such us JSON or Python with strongly-typed SP-Lang.
Schema is basically a directory that maps fields to their types and so on.
For more information, continue to a chapter about SP-Lang [schemas](schema).

SP-Lang Schema-based type specifies the schema by a _schema name_: `json<SCHEMANAME>`.
The _schema name_ is used to locate the schema definition eg. in the library.

List of schema-based types:
 * `pydict<...>`
 * `json<...>`

## Build-in schemas

 * `ANY`: This schema declares any member to be of type `any`.
 * `VOID`: This schema has no member, use in-place type definition to specify types of fields.