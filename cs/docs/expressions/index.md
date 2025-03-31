---
title: Výrazy
search:
    boost: 2
---

# SP-Lang Výrazy

Výrazy v SP-Lang jsou psány jako [YAML tagové direktivy](https://yaml.org/spec/1.2.2/#682-tag-directives).

## Seznam výrazů

<!-- TODO: Přesunout to do samostatného, automaticky aktualizovaného souboru! -->

| Výraz | Typ | Kategorie | Popis |
| :---: | :---: | :---: | --- |
| [`!COUNT`](./aggregate.md#count) | sekvence | agregace | Počítá počet položek. |
| [`!MIN`](./aggregate.md#min) | sekvence | agregace | Vypočítá minimum ze seznamu položek. |
| [`!MAX`](./aggregate.md#max) | sekvence | agregace | Vypočítá maximum ze seznamu položek. |
| [`!AVG`](./aggregate.md#avg) | sekvence | agregace | Vypočítá průměr (aritmetický průměr) položek v seznamu. |
| [`!MEDIAN`](./aggregate.md#median) | sekvence | agregace | Najde medián (střední hodnotu) seznamu položek. |
| [`!MODE`](./aggregate.md#mode) | sekvence | agregace | Najde hodnotu, která se objevuje nejčastěji. |
| [`!RANGE`](./aggregate.md#range) | sekvence | agregace | Najde rozdíl mezi nejvyšší a nejnižší hodnotou. |
| [`!ADD`](./arithmetics.md#add) | sekvence | aritmetika | Sčítání. |
| [`!SUB`](./arithmetics.md#sub) | sekvence | aritmetika | Odečítání. |
| [`!MUL`](./arithmetics.md#mul) | sekvence | aritmetika | Násobení. |
| [`!DIV`](./arithmetics.md#div) | sekvence | aritmetika | Dělení. |
| [`!MOD`](./arithmetics.md#mod) | sekvence | aritmetika | Modulo. |
| [`!POW`](./arithmetics.md#pow) | sekvence | aritmetika | Exponenciace. |
| [`!ABS`](./arithmetics.md#abs) | mapování | aritmetika | Absolutní hodnota. |
| [`!SHL`](./bitwise.md#shl) | mapování | bitwise | Levý logický posun. |
| [`!SHR`](./bitwise.md#shr) | mapování | bitwise | Pravý logický posun. |
| [`!SAL`](./bitwise.md#sal) | mapování | bitwise | Levý aritmetický posun. |
| [`!ROL`](./bitwise.md#rol) | mapování | bitwise | Kružnicová rotace vlevo. |
| [`!ROR`](./bitwise.md#ror) | mapování | bitwise | Kružnicová rotace vpravo. |
| [`!EQ`](./comparisons.md#eq) | sekvence | porovnání | Rovná se. |
| [`!NE`](./comparisons.md#ne) | sekvence | porovnání | Není rovno. |
| [`!LT`](./comparisons.md#lt) | sekvence | porovnání | Menší než. |
| [`!LE`](./comparisons.md#le) | sekvence | porovnání | Menší nebo rovno. |
| [`!GT`](./comparisons.md#gt) | sekvence | porovnání | Větší než. |
| [`!GE`](./comparisons.md#ge) | sekvence | porovnání | Větší nebo rovno. |
| [`!IN`](./comparisons.md#in) | mapování | porovnání | Test členství. |
| [`!IF`](./control.md#if) | mapování | ovládání | Jednoduché podmínkové větvení. |
| [`!WHEN`](./control.md#when) | sekvence |  ovládání | Silné větvení. |
| [`!MATCH`](./control.md#match) | mapování | ovládání | Shoda vzoru. |
| [`!TRY`](./control.md#try) | sekvence | ovládání |  Provádí až do prvního výrazu bez chyby. |
| [`!MAP`](./control.md#map) | mapování | ovládání |  Aplikuje výraz na každý prvek v sekvenci. |
| [`!REDUCE`](./control.md#reduce) | mapování | ovládání |  Sníží prvky seznamu na jednu hodnotu. |
| [`!INCLUDE`](./directives.md#include) | skalární | direktivy | Vloží obsah jiného souboru. |
| [`!ARGUMENT`](./function.md#argument-arg) | skalární | funkce | Získá argument funkce. |
| [`!ARG`](./function.md#argument-arg) | skalární | funkce | Získá argument funkce. |
| [`!FUNCTION`](./function.md#function-fn) | mapování | funkce | Definuje novou funkci. |
| [`!FN`](./function.md#function-fn) | mapování | funkce | Definuje novou funkci. |
| [`!SELF`](./function.md#self) | mapování | funkce | Aplikuje aktuální funkci, používá se pro rekurzi. |
| [`!IP.FORMAT`](./ip.md#ipformat) | mapování | ip | Převede IP adresu na řetězec. |
| [`!IP.INSUBNET`](./ip.md#ipinsubnet) | mapování | ip | Zkontroluje, zda IP adresa spadá do podsítě. |
| [`!GET`](./json.md#get) | mapování | json | Získá jednu hodnotu z JSON. |
| [`!JSON.PARSE`](./json.md#jsonparse) | mapování | json | Parsuje JSON. |
| [`!LIST`](./list.md#list) | mapování | seznam |  Vytváří seznam položek. |
| [`!GET`](./list.md#get) | mapování | seznam | Získá jednu položku ze seznamu. |
| [`!AND`](./logic.md#and) | sekvence | logika |  Konjunkce. |
| [`!OR`](./logic.md#or) | sekvence | logika | Disjunkce. |
| [`!NOT`](./logic.md#not) | sekvence | logika | Negace. |
| [`!LOOKUP`](./lookup.md#lookup) | mapování | vyhledávání | Vytváří nové vyhledávání. |
| [`!GET`](./lookup.md#get) | mapování | vyhledávání | Získá položky z vyhledávání. |
| [`IN`](./lookup.md#in) | mapování | vyhledávání | Zkontroluje, zda je položka ve vyhledávání. |
| [`!RECORD`](./record.md#record) | mapování | záznam |  Kolekce pojmenovaných položek. |
| [`!GET`](./record.md#get) | mapování | záznam |  Získá položku ze záznamu. |
| [`!REGEX`](./regex.md#regex) | | regex | Vyhledávání pomocí regulárního výrazu. |
| [`!REGEX.REPLACE`](./regex.md#regexreplace) | mapování | regex | Nahrazení pomocí regulárního výrazu. |
| [`!REGEX.SPLIT`](./regex.md#regexsplit) | mapování | regex | Rozdělí řetězec podle regulárního výrazu. |
| [`!REGEX.FINDALL`](./regex.md#regexfindall) | mapování | regex | Najde všechny výskyty podle regulárního výrazu. |
| [`!REGEX.PARSE`](./regex.md#regexparse) | mapování | regex | Parsuje podle regulárního výrazu. |
| [`!SET`](./set.md#set) | mapování | množina | Množina položek. |
| [`!IN`](./set.md#in) | mapování| množina | Test členství. |
| [`!IN`](./string.md#in) | mapování | řetězec | Testuje, zda řetězec obsahuje podřetězec. |
| [`!STARTSWITH`](./string.md#startswith) | mapování | řetězec | Testuje, zda řetězec začíná vybraným prefixem. |
| [`!ENDSWITH`](./string.md#endswith) | mapování | řetězec | Testuje, zda řetězec končí vybraným sufixem. |
| [`!SUBSTRING`](./string.md#substring) | mapování | řetězec | Extrahuje část řetězce. |
| [`!LOWER`](./string.md#lower) | mapování | řetězec | Převádí řetězec na malá písmena. |
| [`!UPPER`](./string.md#upper) | mapování | řetězec | Převádí řetězec na velká písmena. |
| [`!CUT`](./string.md#cut) | mapování | řetězec | Ořízne řetězec a vrátí vybranou část. |
| [`!SPLIT`](./string.md#split) | mapování | řetězec | Rozdělí řetězec na seznam. |
| [`!RSPLIT`](./string.md#rsplit) | mapování | řetězec | Rozdělí řetězec zprava na seznam. |
| [`!JOIN`](./string.md#join) | mapování | řetězec | Spojí seznam řetězců. |
| [`!TUPLE`](./tuple.md#tuple) | mapování | n-tice |  Kolekce položek. |
| [`!GET`](./tuple.md#get) | mapování | n-tice |  Získá položku z n-tice. |
| [`!CAST`](./utility.md#cast) | mapování | utility | Převede typ argumentu na jiný. |
| [`!HASH`](./utility.md#hash) | mapování | utility | Vypočítá hash. |
| [`!DEBUG`](./utility.md#debug) | mapování | utility | Ladí výraz. |