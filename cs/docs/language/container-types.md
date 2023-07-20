---
git_commit_hash: b55fa3f
title: Typy kontejnerů
---

# Podrobnosti o typech kontejnerů

## List (seznam)

*List* je uspořádaný seznam konečného počtu položek, přičemž stejná položka se může vyskytovat vícekrát.

<img src="../container-types-list.svg" alt="List schema"/>


## Set (množina)

*Set* je složen z *Interního seznamu* (*Internal list*) a hašovací tabulky.

<img src="../container-types-set.svg" alt="Set schema"/>


## Dict (slovník)

*dict* je kombinací množiny (která je složena z hašovací tabulky a seznamu) klíčů (nazývané *Key set* s *Key list* ) a seznamu hodnot (nazývaného *Value list*).

<img src="../container-types-dict.svg" alt="Dict schema"/>


## Hash table (hašovací tabulka)

Typy *Set* a *Dict* používají [hash table](https://en.wikipedia.org/wiki/Hash_table).

<img src="../container-types-hashtable.svg" alt="Hash table"/>

*Hash table* je navržena tak, že mapuje 64bitový hash klíče přímo na index položky.
Podporuje strategii [perfect hash](https://en.wikipedia.org/wiki/Perfect_hash_function), takže pro zkonstruovanou hašovací tabulku není implementováno žádné řešení kolizí.
Pokud algoritmus pro konstrukci hašovací tabulky zjistí kolizi, algoritmus se znovu spustí s jinou hodnotou *seed*.
Tento přístup využívá relativně vysokou míru kolizí xxhash64.

Hašovací tabulku lze generovat pouze tehdy, když je to potřeba (např. pro výrazy `!IN` a `!GET`).
To platí pro objekty vytvářené dynamicky za běhu.
Statické množiny a slovníky poskytují připravenou hašovací tabulku.

Hašovací tabulka se prohledává pomocí [binárního vyhledávání](https://en.wikipedia.org/wiki/Binary_search_algorithm).


Použité hašovací funkce jsou:

 * [XXH3 64bit](https://cyan4973.github.io/xxHash/) se seedem pro `str`.
 * `xor` se seedem pro `si64`, `si32`, `si16`, `si8`, `ui64`, `ui32`, `si16`, `ui8`
