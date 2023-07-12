---
git_commit_hash: b55fa3f
title: Pomocné
---

# Pomocné výrazy


---

## `!CAST`: Převádí typ argumentu na jiný 

Typ: _Mapping_.

Synopsis:

```yaml
!CAST
what: <input>
typ: <type>
```

Explicitně převádí typ `what` na typ `type`.

SP-Lang automaticky převádí typy argumentů, takže uživatel nemusí na typy vůbec myslet.
Tato funkce se nazývá *implicit casting*.

V případě potřeby explicitní konverze typu použijte výraz `!CAST`.
Jedná se o velmi mocnou metodu, která dělá hodně těžkou práci.

Další podrobnosti najdete v kapitole o [typech](../../language/types).

!!! example "Příklad"

	```yaml
	!CAST
	what: "10.3"
	type: fp64
	```

	Jedná se o explicitní převod řetězce na číslo s desetinnou čárkou.

---

## `!HASH`: Vypočítá digest

Typ: _Mapping_.

Synopsis:

```yaml
!HASH
what: <input>
seed: <integer>
typ: <type of hash>
```

Vypočítá hash pro hodnotu `what`.

`seed` určuje počáteční hash seed.

`type` určuje hašovací funkci, výchozí hodnota je `XXH64`.


### Podporované hašovací funkce

* `XXH64`: xxHash, 64bitový, nekryptografický, extrémně rychlý hashovací algoritmus.
* `XXH3`: xxHash, 64bit, nekryptografický, optimalizovaný pro malé vstupy

Více informací o xxHash naleznete na adrese [xxhash.com](http://www.xxhash.com/).


!!! example "Příklad"

	```yaml
	!HASH
	what: "Hello world!"
	seed: 5
	```


---

## `!DEBUG`: Ladění výrazů 

Vypíše obsah vstupu a na výstupu předá nezměněnou hodnotu.

Typ: _Mapping_.

