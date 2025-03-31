---
title: Seznam
---

# Výraz pro seznamy

## Přehled

Seznam je jednou ze základních datových struktur, které SP-Lang poskytuje.
Seznam obsahuje konečný počet uspořádaných položek, přičemž stejná položka se může vyskytovat vícekrát.
Položky v seznamu musí být stejného typu.

!!! note

    Seznam se někdy nepřesně nazývá také _pole_.

* [`!LIST`](#list): Vytváří seznam položek.
* [`!GET`](#get): Získá jednotlivou položku ze seznamu.

---

## `!LIST`

Vytvoří seznam položek.

Typ:  _Implicitní sekvence_, _Mapování_.

Synopsis:

```yaml
!LIST
- ...
- ...
```

!!! hint

    Použijte `!COUNT` pro určení počtu položek v seznamu.

Existuje několik způsobů, jak lze v jazyce SP-Lang zadat seznam:

!!! example

    ```yaml
    !LIST
    - "One"
    - "Two"
    - "Three"
    - "Four"
    - "Five"
    ```

!!! example

    Implicitní seznam pomocí [sekvencí bloků YAML](https://yaml.org/spec/1.2.2/#821-block-sequences):

    ```yaml
    - "One"
    - "Two"
    - "Three"
    - "Four"
    - "Five"
    ```

!!! example

    Implicitní seznam pomocí [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):

    ```yaml
    ["One", "Two", "Three", "Four", "Five"]
    ```

!!! example

    Formou mapování:

    ```yaml
    !LIST
    with:
    - "One"
    - "Two"
    - "Three"
    - "Four"
    - "Five"
    ```

---

## `!GET`

Získá jednotlivou položku ze seznamu.

Typ: _Mapování_.

Synopsis:

```yaml
!GET
what: <index položky v seznamu>
from: <seznam>
```

`index` je celé číslo (číslo). Může být záporné, v tom případě určuje položku od konce seznamu.
Položky jsou indexovány od 0, to znamená, že první položka v seznamu má index 0.

Pokud je `index` mimo hranice seznamu, příkaz se vrátí s chybou.

!!! example

    ```yaml
    !GET
    what: 3
    from:
        !LIST
        - 1
        - 5
        - 30
        - 50
        - 80
        - 120
    ```

    Vrací `50`.

!!! example

    ```yaml
    !GET
    what: -1
    from:
        !LIST
        - 1
        - 5
        - 30
        - 50
        - 80
        - 120
    ```

    Vrací poslední položku v seznamu, která je `120`.