---
title: Vyhledávací
---

# Vyhledávací výrazy


## Přehled

* [`!LOOKUP`](#lookup): Odkaz na pojmenovanou lookup tabulku.
* [`!GET`](#get): Získá hodnotu z lookup tabulky.
* [`!IN`](#in): Zkontroluje, zda je klíč v lookup tabulce.

Zpětně kompatibilní aliasy `!LOOKUP.GET` a `!LOOKUP.CONTAINS` jsou stále podporovány.

---

## `!LOOKUP`

Odkaz na pojmenovanou lookup tabulku.

Typ: _Mapping_ nebo _Scalar_.

Synopse:

```yaml
!LOOKUP
what: <název-lookup>
```

nebo kratší forma:

```yaml
!LOOKUP <název-lookup>
```

Lookup musí být definován v konfiguraci aplikace.

---

## `!GET`

Získá hodnotu z lookup tabulky.

Typ: _Mapping_.

Synopse:

```yaml
!GET
what: <klíč>
from: !LOOKUP
      what: <název-lookup>
default: <hodnota>
```

- `default` je nepovinné. Pokud klíč není nalezen, vrátí se `default`. Pokud `default` chybí, výraz vrátí `None` (chyba).
- Pokud je `what` seznam, výraz vrátí hodnotu pro první klíč ze seznamu, který v lookup tabulce existuje.

!!! example

    ```yaml
    !GET
    what: foo
    from: !LOOKUP
          what: my_lookup
    ```

---

## `!IN`

Zkontroluje, zda je klíč v lookup tabulce.

Typ: _Mapping_.

Synopse:

```yaml
!IN
what: <klíč>
where: !LOOKUP
       what: <název-lookup>
```

- Pokud je `what` seznam, výraz vrátí `true`, když je v lookup tabulce přítomen libovolný klíč ze seznamu.

!!! example

    ```yaml
    !IN
    what: foo
    where: !LOOKUP
           what: my_lookup
    ```

---

## Zpětně kompatibilní aliasy

### `!LOOKUP.GET`

Zpětně kompatibilní alias pro `!GET` s lookup zadaným přes `in:`:

```yaml
!LOOKUP.GET
what: foo
in: my_lookup
```

### `!LOOKUP.CONTAINS`

Zpětně kompatibilní alias pro `!IN` s lookup zadaným přes `in:`:

```yaml
!LOOKUP.CONTAINS
what: foo
in: my_lookup
```
