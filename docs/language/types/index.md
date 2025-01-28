---
title: Types
---

# SP-Lang data types

In the SP-Lang, [type system](https://en.wikipedia.org/wiki/Type_system) plays a critical role in ensuring the correctness and efficiency of expression execution.
SP-Lang employs type inference.
It means that the _type system_ operates behind the scenes, delivering high performance without burdening the user with its complexities.
This approach allows for a seamless and user-friendly experience, where advanced users can access the type system for more fine-grained control and optimization.


!!! info

    A type system is a set of rules that define how data types are classified, combined, and manipulated in a language.
    It helps catch potential errors early on, improving code reliability, and ensures that operations are performed only on compatible data types.


## Scalar types

Scalar types are the basic building blocks of a language, which represent single values.
They are essential for working with different kinds of data and performing various operations.

### Integers

Integers are whole numbers, like -5, 0, or 42, that can be used for counting or simple arithmetic operations.
Integers could be signed or unsigned.

|Type|Name|Type|Name|Bits|Bytes|
|:----|:----|:----|:----|:----|:----|
|`si8`|Signed 8bit integer|`ui8`|Unsigned 8bit integer|8|1|
|`si16`|Signed 16bit integer|`ui16`|Unsigned 16bit integer|16|2|
|`si32`|Signed 32bit integer|`ui32`|Unsigned 32bit integer|32|4|
|`si64`|Signed 64bit integer|`ui64`|Unsigned 64bit integer|64|16|
|`si128`|Signed 128bit integer|`ui128`|Unsigned 128bit integer|128|32|
|`si256`|Signed 256bit integer|`ui256`|Unsigned 256bit integer|256|64|

A preferred (default) integer type is `si64` (signed 64bit integer), followed by `ui64` (unsigned 64bit integer).
This is because SP-Lang is designed primarily for 64bit CPUs.

`int` is the alias for `si64`.

!!! warning

    256bit sizes are not fully supported yet.


### Boolean

A Boolean (`bool`) is a type that has one of two possible values denoted `True` and `False`.


### Floating-Point

Floating-point numbers are decimal numbers, such as 3.14 or -0.5, that are useful for calculations involving fractions or more precise values.

|Type|Name|Bytes|
|:----|:----|:----|
|`fp16`|16bit float|2|
|`fp32`|32bit float|4|
|`fp64`|64bit float|8|
|`fp128`|128bit float|16|


!!! warning

    `fp16` and `fp128` are not fully supported.


!!! warning

    Alias `float` translates to `fp64` which translates to LLVM `double` (different from alias `float`).



## Complex scalar types

Complex scalar types are designed for values that provides some internal structure (so technically they are records or tuples) but they can fit into a scalar type (e.g. for performance or optimization purposes).


### Date/Time

`datetime`

This is a value that represents a date and time in the UTC, using broken time structure.
Broken time means that `year`, `month`, `day`, `hour`, `minute`, `second` and `microsecond` are stored in dedicated fields; different from the e.g. UNIX timestamp.

* Timezone: UTC
* Resolution: microseconds (six decimal digits)
* 64bit unsigned integer, aka `ui64`


!!! info "Broken time components"

    * `y` / `year`
    * `m` / `month`
    * `d` / `day`
    * `H` / `hour`
    * `M` / `minute`
    * `S` / `second`
    * `u` / `microsecond`

More detailed description of date/time is [here](./date-time.md).


### IP Address

This data type contains IPv4 or IPv6 address.

`ip`

Underlying scalar type: `ui128`

!!! abstract "RFC 4291"

    IPv4 are mapped into IPv6 space as prescribed in [RFC 4291 "IPv4-Mapped IPv6 Address"](https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.5.2).  
    For example, the IPv4 address `12.23.45.67` will be mapped into IPv6 address `::ffff:c17:2d43`.


### MAC Address

This data type contains [MAC address](https://en.wikipedia.org/wiki/MAC_address), (EUI-48).

!!! note "What is MAC Address?"

    A MAC address (short for medium access control address) is a unique identifier assigned to a network card etc.

`mac`

Underlying scalar type: `ui64`, only 6 octets are used in EUI-48.


### Geographical coordinate

This type represents geographical coordinate, specifically longitude and latitude.

`geopoint`

Underlying scalar type: `u64`

More detailed description of geopoint is [here](./geopoint.md).


## Generic types

Generic types are used in the early stage of the SP-Lang parsing, optimization and compilation.
The complementary type is _Specific type_.
The SP-Lang resolves generic types into specific types by the mechanism called _type inference_.
If generic type cannot be resolved into specific, the compilation will fail and you need to provide more information for a type inference.

The generic type starts with capital `T`.
Also if the container type contains generic type, the _container type_ or _structural type_ itself is considered generic.


## Container types


### List

`[Ti]`

* `Ti` refers to a type of the item in the list


The list must contain a zero, one or many items of *the same type*.

The type constructor is `!LIST` expression.


### Set

`{Ti}`

 * `Ti` refers to a type of the item in the set

The type constructor is `!SET` expression.


### Dictionary

`{Tk:Tv}`

 * `Tk` refers to a type of the key
 * `Tv` refers to a type of the value

The type constructor is `!DICT` expression.


### Bag


`[(Tk,Tv)]`

 * `Tk` refers to a type of the key
 * `Tv` refers to a type of the value

A bag (aka multimap) is a container that allows duplicate keys, unlike a dictionary, which only allows unique keys.

!!! tip

    The bag is essentially a list of 2-tuples (couples).


## Product types

A [product type](https://en.wikipedia.org/wiki/Product_type) is a compounded type, formed by combining other types into a _structure_.


### Tuple


Signature: `(T1, T2, T3, ...)`

The type constructor is `!TUPLE` expression.

It is equivalent to a [structure type](https://llvm.org/docs/LangRef.html#structure-type) in LLVM IR.

!!! tip

    A tuple with no members respectively `()` is the [unit](https://en.wikipedia.org/wiki/Unit_type).


### Record

Signature: `(name1: T1, name2: T2, name3: T3, ...)`

The type constructor is `!RECORD` expression.

It is is equivalent to a C `struct`.


## Sum type

A [Sum type](https://en.wikipedia.org/wiki/Tagged_union) is a data structure used to hold a value that could take on several different types.

### Any

`any`

The `any` type is a special type that represents a value that can have any type.


!!! warning

    The `any` type shouldn't be used as a preferred type because it has an overhead.
    Still, it is rather helpful for typing the dictionary that combines types (e.g. `{str:any}`) and other situations where the type of the value is not known in the compile type.

    The value contained in `any` type is always located in the memory (e.g., memory pool); for this reason, this type is slower than others, which store value preferably in CPU registers.

The `any` is a recursive type; it can contain itself because it contains all other types in the type universe.
For this reason, it is impossible to calculate the generic or even maximum size of the `any` variable.


## Object types

### String

`str`

Must be in UTF-8 encoding.

!!! note

    `str` could be casted to `[ui8]` (list of `ui8`) in 'toll-free' manner; it is the binary equivalent.


### Bytes

!!! warning "Work in progress"

    Planned


### Enum

!!! warning "Work in progress"

    Planned



### Regex

`regex`

Contains compiled pattern for a regular expression.

If the regex pattern is constant, then it is compiled during the respective expression compile time.
In the case of dynamic regex pattern, the regex compilation happens during the expression evaluation.


### JSON

`json<SCHEMA>`

JSON object, result of the JSON parsing.
It is schema-based type.


## Function Type

### Function


`(arg1:T1,arg2:T2,arg3:T3)->Tr`

* `T1`, `T2`, `T3` are types of functions inputs `arg1`, `arg2` and `arg3` respectively.
* `Tr` specifies the output type of the function


## Pythonic types

Pythonic types are object types that provides interfacing with the Python.


### Python Dictionary

`pydict<SCHEMA>`

A [Python dictionary](https://docs.python.org/3/c-api/dict.html).
It is a schema-based type.


### Python Object

`pyobj`

A generic [Python object](https://docs.python.org/3/c-api/object.html).


### Python List

`pylist`

A [Python list](https://docs.python.org/3/c-api/list.html).



### Python Tuple

`pytuple`


## Casting

Use `!CAST` expression for change of the type of a value.

```yaml
!CAST
what: 1234
type: fp32
```

or an equivalent shortcut:

```yaml
!!fp32 1234
```

!!! note

    Cast is also a great helper for type inference, it means that it could be used to indicate the the type explicitly, if needed.


## Schema-based types

_Schema_ is the SP-Lang concept of how to bridge schema-less systems such us JSON or Python with strongly-typed SP-Lang.
Schema is basically a directory that maps fields to their types and so on.
For more information, continue to a chapter about SP-Lang [schemas](../schema.md).

SP-Lang Schema-based type specifies the schema by a _schema name_: `json<SCHEMANAME>`.
The _schema name_ is used to locate the schema definition eg. in the library.

List of schema-based types:
 * `pydict<...>`
 * `json<...>`

### Build-in schemas

 * `ANY`: This schema declares any member to be of type `any`.
 * `VOID`: This schema has no member, use in-place type definition to specify types of fields.
