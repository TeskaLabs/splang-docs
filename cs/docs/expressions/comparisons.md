---
title: Porovnání
---

# Porovnávací výrazy

Testovací výraz vyhodnotí vstupy a na základě výsledku testu vrátí logickou hodnotu `true` nebo `false`.

* [!EQ](#eq): Rovná se
* [!NE](#ne): Nerovná se
* [!LT](#lt): Menší než
* [!LE](#le): Menší nebo rovno
* [!GT](#gt): Větší než
* [!GE](#ge): Větší nebo rovno
* [!IN](#in): Test výskytu

---

## `!EQ`

Rovná se.

Typ: _Sekvence_.

!!! example

    ```yaml
    !EQ
    - !ARG count
    - 3
    ```

    Porovnává argument `count` s `3`, vrací `count == 3`.

---

## `!NE`

Nerovná se.

Typ: _Sekvence_.

Jedná se o zápornou obdobu `!EQ`.

!!! example

    ```yaml
    !NE
    - !ARG name
    - Frodo
    ```

    Porovnává argument `name` s `Frodo`, vrací `name != Frodo`.

---

## `!LT`

Menší než.

Typ: _Sekvence_.

!!! example

    ```yaml
    !LT
    - !ARG count
    - 5
    ```

    Příklad testu `count < 5`.

---

## `!LE`

Menší nebo rovno.

Typ: _Sekvence_.

!!! example

    ```yaml
    !LE
    - 2
    - !ARG count
    - 5
    ```

    Příklad testu rozsahu `2 <= count <= 5`.

---

## `!GT`

Větší než.

Typ: _Sekvence_.

!!! example

    ```yaml
    !GT [!ARG count, 5]
    ```

    Příklad testu `count > 5` pomocí kompaktní formy YAMLu.

---

## `!GE`

Větší nebo rovno.

Typ: _Sekvence_.

!!! example

    ```yaml
    !GT
    - !ARG count
    - 5
    ```

    Příklad testu `count >= 5`.

---

## `!IN`

Test výskytu.

Typ: _Mapování_.

```yaml
!IN
what: <...>
where: <...>
```

Výraz `!IN` se používá ke kontrole, zda hodnota `what` vyskytuje v hodnotě `where`, nebo ne.
Hodnota `where` může být řetězec, kontejner (seznam, množina, slovník), strukturní typ atd.
Vyhodnotí se na `true`, pokud najde hodnotu `what` v zadané hodnotě `where`, a na `false` v opačném případě.

!!! example

    ```yaml
    !IN
    what: 5
    where:
      - 1
      - 2
      - 3
      - 4
      - 5
    ```

    Zkontroluje přítomnost hodnoty `5` v seznamu `where`. Vrátí `true`.

!!! example

    ```yaml
    !IN
    what: "Willy"
    where: "John Willy Boo"
    ```

    Zkontroluje přítomnost podřetězce `Willy` v hodnotě `John Willy Boo`. Vrátí `true`.