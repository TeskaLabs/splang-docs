---
title: Řetězce
---

# Řetězce

Řetězce v SP-Lang používají [UTF-8](https://en.wikipedia.org/wiki/UTF-8) kódování.
Reprezentace typu řetězce je `str`.


## Reprezentace řetězce

Řetězec je reprezentován [P-String](https://en.wikipedia.org/wiki/String_%28computer_science%29#Length-prefixed) odpovídajícím záznamu s následujícími položkami:

 * Délka řetězce v bajtech jako 64bitové nezáporné číslo.
 * Ukazatel na začátek _dat řetězce_.


!!! tip "Řetězec je také pole bajtů"

    Hodnota `str` je binárně kompatibilní s `[ui8]`, seznamem `ui8`.


## Kompatibilita s řetězci ukončenými NULL

Hodnota `str` NESMÍ končit s `\0` (NULL).

Další `\0` může být umístěno hned za daty řetězce, ale nesmí být zahrnuto do délky řetězce.
To poskytuje přímou kompatibilitu se systémy [řetězců ukončených NULL](https://en.wikipedia.org/wiki/Null-terminated_string).
Není však implicitně zaručeno `str`.

Řetězec ukončený `NULL` může být "převeden" na `str` vytvořením nového `str` pomocí `strlen()` a aktuálního ukazatele na data řetězce.
Alternativně může být také vytvořena úplná kopie.

## Data řetězce

Data řetězce jsou paměťový prostor, který obsahuje skutečnou hodnotu řetězce.

Data řetězce mohou být:

* umístěna hned za strukturou `str`
* zcela nezávislý vyrovnávací paměť řetězce (“pohled na řetězec”)

Data řetězce mohou být sdílena s mnoha strukturami `str`, včetně referencí na části dat řetězce (tj. podřetězce).