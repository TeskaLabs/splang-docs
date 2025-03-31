---
title: Řídicí
---

# Řídicí výrazy

## Přehled

SP-Lang nabízí celou řadu řídicích výrazů.

* [`!IF`](#if): Jednoduché podmíněné větvení.
* [`!WHEN`](#when): Silné větvení.
* [`!MATCH`](#match): Porovnávání vzorů.
* [`!TRY`](#try): Provádění do prvního bezchybného výrazu.
* [`!MAP`](#map): Aplikace výrazu na každý prvek v posloupnosti.
* [`!REDUCE`](#reduce): Redukce prvků seznamu na jedinou hodnotu.

---

## `!IF`

Jednoduché podmíněné větvení.

Typ: _Mapping_.

Výraz `!IF` je rozhodovací výraz, který vede vyhodnocení k rozhodování na základě zadaného testu.

```yaml
!IF
test: <expression>
then: <expression>
else: <expression>
```

Na základě hodnoty `test` se vyhodnotí větev:

* `then` v případě `test !EQ true`
* `else` v případě `test !EQ false`

Oba případy `then` a `else` musejí vracet stejný typ, který bude zároveň typem návratové hodnoty `!IF`.

!!! example

    ```yaml
    !IF
    test:
      !EQ
      - !ARG input
      - 2
    then:
      Je to dva.
    else:
      Není to dva.
    ```

---

## `!WHEN`  

Silné větvení.

Typ: _Sequence_.

Výraz `!WHEN` je podstatně silnější než výraz `!IF`.
Jednotlivé případy mohou odpovídat mnoha různým vzorům, včetně intervalových shod, tuples atd. 

```yaml
!WHEN
- test: <expression>
  then: <expression>

- test: <expression>
  then: <expression>

- test: <expression>
  then: <expression>

- ...

- else: <expression>
```

Pokud není zadáno `else`, pak `WHEN` vrací `False`.

!!! example

    Příklad použití `!WHEN` pro přesnou shodu, shodu rozsahu a nastavenou shodu:

    ```yaml
    !WHEN

    # Přesná shoda hodnot
    - test:
        !EQ
        - !ARG key
        - 34
      then:
        "třicet čtyři"

    # Shoda rozsahu
    - test:
        !LT
        - 40
        - !ARG key
        - 50
      then:
        "čtyřicet až padesát (bez krajních hodnot)"

    # In-set match
    - test:
        !IN
        what: !ARG key
        where:
          - 75
          - 77
          - 79
      then:
        "sedmdesát pět, sedm, devět"

    - else:
        "neznámý"
    ```

---

## `!MATCH`

Porovnávání vzorů.

Typ: _Mapping_.

```yaml
!MATCH
what: <what-expression>
with:
  <value>: <expression>
  <value>: <expression>
  ...
else:
  <expression>
```

Výraz `!MATCH` vyhodnotí výraz `what-expression`, přiřadí hodnotu výrazu k klauzuli case a provede výraz `expression` spojený s tímto případem.

Větev `else` výrazu `!MATCH` je nepovinná.
Výraz selže s chybou, pokud není nalezena žádná odpovídající `<value>` a větev `else` chybí.

!!! example

    ```yaml
    !MATCH
    what: !ARG value
    with:
        1: "jedna"
        2: "dva"
        3: "tři"
    else:
        "jiné číslo"
    ```

!!! hint "Použití `!MATCH` pro strukturování kódu"

    ```yaml
    !MATCH
    what: !ARG kód
    with:
        1: !INCLUDE code-1.yaml
        2: !INCLUDE code-2.yaml
    else:
        !INCLUDE code-else.yaml
    ```

---

## `!TRY`

Provádění do prvního bezchybného výrazu.

Typ: _Sequence_

```yaml
!TRY
- <expression>
- <expression>
- <expression>
...
```

Iteruje jednotlivými výrazy (odshora dolů), pokud výraz vrátí nenulový výsledek (`None`), zastaví iteraci a vrátí tuto hodnotu.
V opačném případě pokračuje k dalšímu výrazu.

Při dosažení konce seznamu vrátí `None` (chyba).

Poznámka: Zastaralý název tohoto výrazu byl `!FIRST`. Nepoužívá se od listopadu 2022.

---

## `!MAP`

Použít výraz na každý prvek v posloupnosti.

Typ: _Mapping_.

```yaml
!MAP
what: <sequence>
apply: <expression>
```

Výraz `apply` se aplikuje na každý prvek v posloupnosti `what` s argumentem `x` obsahujícím příslušnou hodnotu prvku.
Výsledkem je nový seznam s transformovanými prvky.

!!! example

    ```yaml
    !MAP
    what: [1, 2, 3, 4, 5, 6, 7]
    apply:
        !ADD [!ARG x, 10]
    ```

    Výsledek je `[11, 12, 13, 14, 15, 16, 17]`.

---

## `!REDUCE`

Redukce prvků seznamu na jedinou hodnotu.

Typ: _Mapping_.

```yaml
!REDUCE
what: <expression>
apply: <expression>
initval: <expression>
fold: <left|right>
```

Výraz `apply` se aplikuje na každý prvek v posloupnosti `what` s argumentem `a` obsahujícím agregaci operace reduce a argumentem `b` obsahujícím příslušnou hodnotu prvku.

Výraz `initval` poskytuje počáteční hodnotu pro argument `a`.

Nepovinná hodnota `fold` určuje "levé skládání" (`left`, výchozí) nebo "pravé skládání" (`right`).

!!! example

    ```yaml
    !REDUCE
    what: [1, 2, 3, 4, 5, 6, 7]
    initval: -10
    apply:
      !ADD [!ARG a, !ARG b]
    ```

    Vypočítá součet posloupnosti s počáteční hodnotou `-10`.  
    Výsledek je `18 = -10 + 1 + 2 + 3 + 4 + 5 + 6 + 7`.