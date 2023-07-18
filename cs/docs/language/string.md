---
git_commit_hash: b55fa3f
title: Řetězce
---

# Řetězce

Řetězce v SP-Langu používají kódování [UTF-8](https://en.wikipedia.org/wiki/UTF-8).
Reprezentace typu řetězce je `str`.


## Reprezentace řetězce

Řetězec je reprezentován [P-Stringem](https://en.wikipedia.org/wiki/String_%28computer_science%29#Length-prefixed) příslušným záznamem s následujícími položkami:

 * Délka řetězce v bajtech jako 64bitové číslo bez znaménka.
 * Pointer na začátek _řetězcových dat_.



!!! tip "Řetězec je také pole bajtů"

	Hodnota `str` je binárně kompatibilní s `[ui8]`, seznamem `ui8`.


## Kompatibilita s řetězci ukončenými nulou

Hodnota `str` NESMÍ končit znakem `\0` (NULL).

Dodatečné `\0` může být umístěno hned za údaji řetězce, ale nesmí být zahrnuto do délky řetězce.
Zajišťuje přímou kompatibilitu se systémy [NULL-terminated string](https://en.wikipedia.org/wiki/Null-terminated_string).
Není však implicitně zaručena pomocí `str`.

`NULL` ukončený řetězec lze "převést" na `str` vytvořením nového `str` pomocí `strlen()` a skutečného ukazatele na data řetězce.
Alternativně lze vytvořit i úplnou kopii.

## Data řetězce

Data řetězce je paměťový prostor, který obsahuje skutečnou hodnotu řetězce.

Řetězcová data mohou být:

* umístit hned za strukturu `str`
* zcela samostatný řetězcový buffer ("string view")

Řetězcová data mohou být sdílena s mnoha strukturami `str`, včetně odkazů na části řetězcových dat (tzv. podřetězce).
