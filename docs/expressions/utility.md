---
title: Utility
---

# Utility expressions

## Overview

- [`!CAST`](#cast): Converts type of the argument into another.
- [`!HASH`](#hash): Calculates a digest.
- [`!DEBUG`](#debug): Debugs the expression.

---

## `!CAST`

Convert type of the argument into another.

Type: _Mapping_.

Synopsis:

```yaml
!CAST
what: <input>
type: <type>
```

Explicitly convert type of `what` into the type of `type`.

SP-Lang automatically converts types of arguments so that the user doesn't need to think about types at all.
This feature is called _implicit casting_.

In case of explicit need for a type conversion, use `!CAST` expression.
It is very powerful method that do a lot of heavy-lifting.

For more details, see chapter about [types](../language/types/index.md).

!!! example

    ```yaml
    !CAST
    what: "10.3"
    type: fp64
    ```

    This is an explicit casting of the string into a floating-point number.

---

## `!HASH`

Calculate a digest.

Type: _Mapping_.

Synopsis:

```yaml
!HASH
what: <input>
seed: <integer>
type: <type of hash>
```

Calculate the hash for an `what` value.

`seed` specifies the initial hash seed.

`type` specifies a hashing function, the default value is `XXH64`.


### Supported hashing functions

* `XXH64`: xxHash, 64bit, non-cryptographic, extremely fast hash algorithm
* `XXH3`: xxHash, 64bit, non-cryptographic, further optimized for small inputs

More information about xxHash are at [xxhash.com](http://www.xxhash.com/).


!!! example

    ```yaml
    !HASH
    what: "Hello world!"
    seed: 5
    ```

---

## `!DEBUG`

Print the content of the input and pass the value unchanged on the output.

Type: _Mapping_.
