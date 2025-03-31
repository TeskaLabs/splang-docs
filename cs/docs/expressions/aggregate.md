---
title: Agregační
---

# Agregační výrazy

Agregační výraz je typ funkce, která provádí výpočty nad množinou hodnot a jako výsledek vrací jednu hodnotu.
Tyto výrazy se běžně používají k shrnutí nebo zhuštění dat.

* [`!COUNT`](#count): Počítá počet položek.
* [`!MAX`](#max), [`!MIN`](#min): Vypočítává maximum / minimum.
* [`!AVG`](#avg): Vypočítává průměr (aritmetický průměr).
* [`!MEDIAN`](#median): Najde prostřední hodnotu.
* [`!MODE`](#mode): Najde hodnotu, která se vyskytuje nejčastěji.
* [`!RANGE`](#range): Najde rozdíl mezi nejvyšší a nejnižší hodnotou.

---

## `!COUNT`

Spočítá počet položek v seznamu.

Typ: _Sequence_

!!! example

    ```yaml
    !COUNT
    - Frodo Pytlík
    - Samvěd Křepelka
    - Gandalf
    - Legolas
    - Gimli
    - Aragorn
    - Boromir z Gondoru
    - Smělmír Brandorád
    - Pipin Bral
    ```

    Vrací `9`.

---

## `!MAX`

Vrací maximální hodnotu z posloupnosti.

Typ: _Sequence_

!!! example

    ```yaml
    !MAX
    - 1.5
    - 2.6
    - 5.1
    - 3.05
    - 4.45
    ```

    Výsledek tohoto výrazu je `5.1`.

---

## `!MIN`

Vrací minimální hodnotu z posloupnosti.

Typ: _Sequence_

!!! example

    ```yaml
    !MIN
    - 2.6
    - 3.05
    - 4.45
    - 0.5
    - 5.1
    ```

    Výsledek tohoto výrazu je `0.5`.

---

## `!AVG`

Vypočítá aritmetický průměr.

Typ: _Sequence_

!!! info

    Více informací o [aritmetickém průměru](https://cs.wikipedia.org/wiki/Aritmetick%C3%BD_pr%C5%AFm%C4%9Br) na Wikipedii.

!!! example

    ```yaml
    !AVG
    - 6
    - 2
    - 4
    ```

    Výpočet průměru `(6+2+4)/3`, výsledek je `4`.

---

## `!MEDIAN`

Medián je prostřední hodnota v seznamu čísel; polovina hodnot je větší než medián a polovina je menší než medián.
Pokud má seznam sudý počet prvků, je medián aritmetickým průměrem dvou prostředních hodnot.

Typ: _Sequence_

!!! info

    Více informací o [medián](https://cs.wikipedia.org/wiki/Medi%C3%A1n) na Wikipedii.

!!! example

    ```yaml
    !MEDIAN
    - 1
    - 4
    - -1
    - 9
    - 101
    ```

    Vrací `4`.

---

## `!MODE`

Modus je označení pro hodnotu nebo hodnoty, které se v seznamu vyskytují nejčastěji.
Lze ji použít k vyjádření centrální tendence souboru dat.

Typ: _Sequence_

!!! info

    Více informací o [mode](https://cs.wikipedia.org/wiki/Modus) na Wikipedii.

!!! example

    ```yaml
    !MODE
    - 10
    - 10
    - -20
    - -20
    - 6
    - 10
    ```

    Vrací `10`.

---

## `!RANGE`

Vypočítává rozdíl mezi největší a nejmenší hodnotou.

Typ: _Sequence_

!!! info

    Více informací o [range](https://cs.wikipedia.org/wiki/Varia%C4%8Dn%C3%AD_rozp%C4%9Bt%C3%AD) na Wikipedii.

!!! example

    ```yaml
    !RANGE
    - 1
    - 3
    - 4
    - 20
    - -1
    ```