---
title: Details of container types
---

# Details of container types

## List

The *list* represents a finite number of ordered items, where the same item may occur more than once.

<img src="../container-types-list.svg" alt="List schema"/>


## Set

The *set* is a composition of the *Internal list* and the hash table.

<img src="../container-types-set.svg" alt="Set schema"/>


## Dict

The *dict* (aka dictionary) is a composition of the set (itself a hash table and a list) of keys (called *Key set* with *Key list* ) and a list of values (called *Value list*).

<img src="../container-types-dict.svg" alt="Dict schema"/>


## Hash table

*Set* and *Dict* types uses a [hash table](https://en.wikipedia.org/wiki/Hash_table).

<img src="../container-types-hashtable.svg" alt="Hash table"/>

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
