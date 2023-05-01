---
title: Utility expressions
---

# Utility expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

---

## `!CAST`: Convert type of the argument into another 

Type: _Mapping_.

### Synopsis

```yaml
!CAST
what: <input>
type: <type>
```

Explicitly convert type of `what` into the type of `type`.

SP-Lang automatically converts types of arguments so that the user doesn't need to think about types at all.
This feature is called *implicit casting*.

In case of explicit need for a type conversion, use `!CAST` expression.
It is very powerful method that do a lot of heavylifting.

For more details about types, see Type System chapter.

### Example

```yaml
!CAST
what: "10.3"
type: fp64
```

This is an explicit casting of the string into a floating-point number.

---

## `!HASH`: Calculate a digest 

Type: _Mapping_.

### Synopsis

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

* `XXH64`: xxHash, 64bit, non-cryptografic, extremely fast hash algorithm
* `XXH3`: xxHash, 64bit, non-cryptografic, futher optimized for small inputs

More information about xxHash are here: http://www.xxhash.com/


### Example

```yaml
!HASH
what: "Hello world!"
seed: 5
```


---

## `!DEBUG`: Debug the expression 

Type: _Mapping_.

Print the content of the input and pass the value unchanged on the output.
