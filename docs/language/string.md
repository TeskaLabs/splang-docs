---
title: Strings
---

# Strings

Strings in SP-Lang uses [UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoding.
The string type representation is `str`.


## String representation

String is represented by a [P-String](https://en.wikipedia.org/wiki/String_%28computer_science%29#Length-prefixed) respective by the record with following items:

 * Length of the string in bytes as 64bit unsigned number.
 * Pointer to the start of a _string data_.


!!! tip "String is also an array of bytes"

    Value of `str` is binary compatible with `[ui8]`, a list of `ui8`.


## Compatibility with Null-terminated strings

Value of `str` MUST NOT end with `\0` (NULL).

The additional `\0` can be placed just after string data but not included in a string length.
It provides direct compatibility with [NULL-terminated string](https://en.wikipedia.org/wiki/Null-terminated_string) systems.
It is however not guaranteed by `str` implicitly.

`NULL` terminated string can be "converted" into `str` by creating new `str` using `strlen()` and actual pointer to a string data.
Alternativelly, the complete copy can be created as well.

## String data

String data is the memory space that contains the actual string value.

The string data could be:

* placed just after `str` structure
* completely independent string buffer (“string view”)

The string data may be shared with many `str` structures, including references to the portions of the string data (aka substrings).
