---
git_commit_hash: b55fa3f
title: Množiny
---

# Výrazy pro práci s množinami


Množina (set) ukládá objekty zvané prvky, aniž by si všímala konkrétního pořadí, a každý prvek ukládá pouze jednou.
Prvky v množině musí být stejného typu.
Množina je jednou ze základních datových struktur poskytovaných jazykem SP-Lang.

Množina je vhodnější pro testování výskytu nějakého prvku spíše než pro získání konkrétního prvku.

--- 

## `!SET`: množina prvků 

Typ: _Implicit sequence_, _Mapping_.

Synopsis:

```yaml
!SET
- ...
- ...
```

!!! hint "Nápověda"

    Pro určení počtu položek v sadě použijte `!COUNT`.

Existuje několik způsobů, jak lze v jazyce SP-Lang zadat množinu:

!!! example "Příklad"

    ```yaml
    !SET
    - "One"
    - "Dva"
    - "Three"
    - "Four"
    - "Five"
    ```

!!! example "Příklad"
    [Neuspořádaná množina YAML](https://yaml.org/spec/1.2.2/#example-unordered-sets):

    ```yaml
    !!set
    ? Žluté vepřové maso
    ? Růžová tráva
    ? Bílý sníh
    ```

!!! example "Příklad"

    Kompaktní zápis množiny pomocí [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):

    ```yaml
    !SET ["One", "Two", "Three", "Four", "Five"]
    ```

!!! example "Příklad"
    Formulář pro mapování:

    ```yaml
    !SET
    with:
    - "One"
    - "Two"
    - "Three"
    - "Four"
    - "Five"
    ```


--- 

## `!IN`: Test členství 

Typ: _Mapping_.

Synopsis:

```yaml
!IN
what: <item>
where: <set>
```

Zkontroluje, zda je `item` přítomna v `set`.

Výraz `!IN` je popsán v kapitole [Porovnávací výrazy](../comparisons/#in-test-vyskytu).

!!! example "Příklad"

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
