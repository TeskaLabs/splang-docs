---
layout: default
title: SP-Lang documentation
---

# Utility expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

---

## `!HASH`: Calculate a digest {#EXPR-HASH}

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

## `!DEBUG`: Debug the expression {#EXPR-DEBUG}

Type: _Mapping_.

Print the content of the input and pass the value unchanged on the output.
