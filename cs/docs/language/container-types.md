---
git_commit_hash: b55fa3f
title: Typy kontejnerů
---

# Podrobnosti o typech kontejnerů

## Seznam

*Seznam* představuje konečný počet uspořádaných položek, přičemž stejná položka se může vyskytovat vícekrát.

<img src="../container-types-list.svg" alt="List schema"/>


## Množina

*Set* je složen z *Interního seznamu* a hašovací tabulky.

<img src="../container-types-set.svg" alt="Set schema"/>


## Dict

*dict* (neboli slovník) je složen z množiny (sama o sobě hashovací tabulka a seznam) klíčů (nazývané *Množina klíčů* s *Seznam klíčů* ) a seznamu hodnot (nazývaného *Seznam hodnot*).

<img src="../container-types-dict.svg" alt="Dict schema"/>


## Hašovací tabulka

Typy *Set* a *Dict* používají [hash table](https://en.wikipedia.org/wiki/Hash_table).

<img src="../container-types-hashtable.svg" alt="Hash table"/>

Tabulka *hash* je navržena tak, že mapuje 64bitový hash klíče přímo na index položky.
Strategie [perfect hash](https://en.wikipedia.org/wiki/Perfect_hash_function) je použita tak, že pro zkonstruovanou hash tabulku není implementováno žádné řešení kolizí.
Pokud algoritmus pro konstrukci hašovací tabulky zjistí kolizi, algoritmus se znovu spustí s jinou hodnotou *seed*.
Tento přístup využívá relativně vysokou míru kolizí xxhash64.

Hašovací tabulku lze (líně) generovat pouze tehdy, když je to potřeba (např. pro výrazy `!IN` a `!GET`).
To platí pro objekty vytvářené dynamicky za běhu.
Statické sady a slovníky poskytují připravenou hashovací tabulku.

Hašovací tabulka se prohledává pomocí [binárního vyhledávání](https://en.wikipedia.org/wiki/Binary_search_algorithm).


Použité hašovací funkce jsou:

 * [XXH3 64bit](https://cyan4973.github.io/xxHash/) se semenem pro `str`.
 * `xor` se semenem pro `si64`, `si32`, `si16`, `si8`, `ui64`, `ui32`, `si16`, `ui8`
