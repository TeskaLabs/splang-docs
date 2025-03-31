---
title: Slovníky
---

# Slovníkové výrazy

## Přehled

**Slovník (dict)** uchovává kolekci dvojic (klíč, hodnota) tak, že každý možný klíč se v kolekci vyskytuje nejvýše jednou. Klíče ve slovníku musí být stejného typu, stejně jako hodnoty.

Položka je dvojice (klíč, hodnota) reprezentovaná jako tuple.

!!! Nápověda

    Tuto strukturu můžete znát pod alternativními názvy "asociativní pole" nebo "mapa".

* [`!DICT`](#dict): Slovník.
* [`!GET`](#get): Získat hodnotu ze slovníku.
* [`!IN`](#in): Test výskytu.

---

## `!DICT`

Slovník.

Typ:  _Mapping_

```yaml
!DICT
with:
  <key1>: <value1>
  <key2>: <value2>
  <key3>: <value3>
  ...
```

!!! nápověda

    Pro zjištění počtu položek ve slovníku použijte [`!COUNT`](./aggregate.md#count).

!!! příklad

    V jazyce SP-Lang lze slovník zadat několika způsoby:

    ```yaml
    !DICT
    with:
      key1: "One"
      key2: "Two"
      key3: "Three"
    ```

    Implicitně zadaný slovník:

    ```yaml
    ---
    key1: "One"
    key2: "Two"
    key3: "Three"
    ```

    Slovník zadaný zkráceně využívaje `!!dict` a flow stylu v YAML:

    ```yaml
    !!dict {key1: "One", key2: "Two", key3: "Three"}
    ```

### Specifikace typu

Typ slovníku se označuje jako `{Tk:Tv}`, kde `Tk` je typ klíče a `Tv` je typ hodnoty. Další informace o typu slovníku naleznete v příslušné kapitole v [typovém systému](../language/types/index.md#dictionary).

Slovník se pokusí odvodit svůj typ na základě přidaných položek. Typ první položky pravděpodobně poskytne typ klíče `Tk` a typ hodnoty `Tv`. Pokud je slovník prázdný, jeho odvozený typ je `{str:si64}`.

Toto lze přepsat pomocí explicitní specifikace typu:

```yaml
!DICT
type: "{str:any}"
with:
  <key1>: <value1>
  <key2>: <value2>
  <key3>: <value3>
  ...
```

`type` je nepovinný argument obsahující řetězec se signaturou slovníku, která bude použita namísto odvozování typu z následníků.

Ve výše uvedeném příkladu je typ slovníku `{str:any}`, typ klíče je `str` a typ hodnot je `any`.

---

## `!GET`

Získat hodnotu ze slovníku.

Typ: _Mapping_.

```yaml
!GET
what: <key>
from: <dict>
default: <value>
```

Získá položku ze slovníku `dict` (slovník) identifikovaného pomocí `key`.

Pokud `key` není nalezen, vrátí `default` nebo chybu, pokud `default` není zadán. `default` je nepovinné.

!!! příklad

    ```yaml
    !GET
    what: 3
    from:
      !DICT
      with:
        1: "One"
        2: "Two"
        3: "Three"
    ```

    Vrátí `Three`.

---

## `!IN`

Test výskytu.

Typ: _Mapping_.

```yaml
!IN
what: <key>
where: <dict>
```

Zkontroluje, zda je `key` přítomen v `dict`.

!!! poznámka

    Výraz `!IN` je popsán v kapitole [Porovnávací výrazy](./comparisons.md#in).

!!! příklad

    ```yaml
    !IN
    what: 3
    where:
      !DICT
      with:
        1: "One"
        2: "Two"
        3: "Three"
    ```