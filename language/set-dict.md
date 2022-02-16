---
layout: default
title: SP-Lang Documentation
---

# Set and Dictionary details

Set and Dictionary types are implemented using a [hash table](https://en.wikipedia.org/wiki/Hash_table).

<img src = "set-dict-hashtable.svg" alt="Set and Dict schema"/>


## Set

The *set* is a composition of the `list` (called *internal list* aka *intlist* ) and the hash table.


## Dict

The *dict* (aka dictionary) is a composition of the `set` of keys (called *key set* with *keylist* ) and a `list` of values (called *value list*).


## Hash table

The *hash table* is designed so that it maps the 64bit hash of the key directly into an index of the item.
The [perfect hash](https://en.wikipedia.org/wiki/Perfect_hash_function) strategy is applied so no collision resolution is implemented for a constructed hash table.
If a hash table constructing algorithm detects a colision, the algorithm is restarted with a different *seed value*.
This approach leverages relatively rate xxhash64 collision rate.

A hash table can be (lazily) generated only when it is needed (e.g. for `!IN` and `!GET` expressions).
This applies for objects created dynamically during runtime.
Static sets a dictionaries provide a prepared hash table.

A hash table is searched using a [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm).


The used hashing function are:

 * [XXH3 64bit](https://cyan4973.github.io/xxHash/) with seed for `str`
 * `xor` with seed for `si64`, `si32`, `si16`, `si8`, `ui64`, `ui32`, `si16`, `ui8`
 