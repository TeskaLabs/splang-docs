---
title: Množiny
---

# Výrazy pro práci s množinami

## Přehled

Množina ukládá unikátní prvky, aniž by si všímala konkrétního pořadí. 
Prvky v množině musí být stejného typu. 
Množina je jednou ze základních datových struktur poskytovaných jazykem SP-Lang.

Množina je nejvhodnější pro testování přítomnosti hodnoty než pro získání konkrétního prvku z množiny.

* [`!SET`](#set): Množina prvků.
* [`!IN`](#in): Test členství.

---

## `!SET`

Množina prvků.

Typ:  _Implicit sequence_, _Mapping_.

Synopsis:

```yaml
!SET
- ...
- ...
```

!!! hint

    Použijte `!COUNT` pro určení počtu prvků v množině.

Existuje několik způsobů, jak lze v jazyce SP-Lang zadat množinu:

!!! example

    ```yaml
    !SET
    - "One"
    - "Dva"
    - "Three"
    - "Four"
    - "Five"
    ```

!!! example "Neuspořádaná množina"

    [Neuspořádaná množina YAML](https://yaml.org/spec/1.2.2/#example-unordered-sets):

    ```yaml
    !!set
    ? Žluté vepřové maso
    ? Růžová tráva
    ? Bílý sníh
    ```

!!! example "YAML flow sequences"

    Kompaktní zápis množiny pomocí [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):

    ```yaml
    !SET ["One", "Dva", "Three", "Four", "Five"]
    ```

!!! example
    Formulář pro mapování:

    ```yaml
    !SET
    with:
    - "One"
    - "Dva"
    - "Three"
    - "Four"
    - "Five"
    ```

---

## `!IN`

Test členství.

Typ: _Mapping_.

Synopsis:

```yaml
!IN
what: <item>
where: <set>
```

Zkontroluje, zda je `item` přítomna v `set`.

Výraz `!IN` je popsán v kapitole [Porovnávací výrazy](./comparisons.md#in).

!!! example

    ```yaml
    !IN
    what: 3
    where:
      !SET
      with:
        - 1
        - 2
        - 5
        - 8 
    ```