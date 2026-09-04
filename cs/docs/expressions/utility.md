---
title: Pomocné
---

# Pomocné výrazy

## Přehled

- [`!CAST`](#cast): Převádí typ argumentu na jiný.
- [`!HASH`](#hash): Vypočítá digest.
- [`!DEBUG`](#debug): Ladí výraz.
- [`!HEX.BYTES`](#hexbytes): Převádí hexadecimální řetězec na binární data.

---

## `!CAST`

Převádí typ argumentu na jiný.

Typ: _Mapping_.

Synopsis:

```yaml
!CAST
what: <input>
type: <type>
default: <value>
base: <integer>
```

- `default` je nepovinné. Vrací se při neúspěšné konverzi.
- `base` je nepovinné. Používá se při převodu řetězců na celá čísla (součást číselné soustavy).

Explicitně převádí typ `what` na typ `type`.

SP-Lang automaticky převádí typy argumentů, takže uživatel nemusí na typy vůbec myslet.
Tato funkce se nazývá *implicit casting*.

V případě potřeby explicitní konverze typu použijte výraz `!CAST`.
Jedná se o velmi mocnou metodu, která dělá hodně těžkou práci.

Další podrobnosti najdete v kapitole o [typech](../language/types/index.md).

!!! example "Příklad"

    ```yaml
    !CAST
    what: "10.3"
    type: fp64
    ```

    Jedná se o explicitní převod řetězce na číslo s desetinnou čárkou.

---

## `!HASH`

Vypočítá digest.

Typ: _Mapping_.

Synopsis:

```yaml
!HASH
what: <input>
seed: <integer>
typ: <type of hash>
```

Vypočítá hash pro hodnotu `what` a vrátí digest jako seznam bajtů (`list[ui8]`).

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

## `!DEBUG`

Vypíše obsah vstupu a na výstupu předá nezměněnou hodnotu.

Typ: _Mapping_.

Synopse:

```yaml
!DEBUG
what: <výraz>
```

---

## `!HEX.BYTES`

Převádí hexadecimální řetězec na binární data.

Typ: _Mapping_.

Synopse:

```yaml
!HEX.BYTES
what: <string>
```

!!! example "Příklad"

    ```yaml
    !HEX.BYTES
    what: "8F3A12"
    ```
    _Výstup:_ `b'\x8f:\x12'`