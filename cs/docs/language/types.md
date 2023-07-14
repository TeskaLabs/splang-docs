---
git_commit_hash: b55fa3f
title: Typy
---

# Datové typy SP-Lang

V SP-Langu hraje [typový systém](https://en.wikipedia.org/wiki/Type_system) zásadní roli při zajišťování správnosti a efektivity provádění výrazů.
SP-Lang používá typovou inferenci.
To znamená, že _typový systém_ pracuje v zákulisí a poskytuje vysoký výkon, aniž by uživatele zatěžoval svou složitostí.
Tento přístup umožňuje bezproblémové a uživatelsky přívětivé prostředí, kde mohou pokročilí uživatelé přistupovat k typovému systému pro jemnější kontrolu a optimalizaci.


!!! info

	
	
	
	Systém typů je soubor pravidel, která definují, jak se v jazyce klasifikují, kombinují a manipulují datové typy.
	Pomáhá včas zachytit potenciální chyby, zvyšuje spolehlivost kódu a zajišťuje, aby se operace prováděly pouze nad kompatibilními datovými typy.
	
	

## Skalární typy

Skalární typy jsou základními stavebními kameny jazyka, které reprezentují jednotlivé hodnoty.
Jsou nezbytné pro práci s různými druhy dat a provádění různých operací.

### Celá čísla

Celá čísla jsou celá čísla, jako například -5, 0 nebo 42, která lze použít pro počítání nebo jednoduché aritmetické operace.
Celá čísla mohou být se znaménkem nebo bez znaménka.

|Typ|Jméno|Typ|Jméno|Bity|Bajty|.
|:----|:----|:----|:----|:----|:----|
|`si8`|Signed 8bit integer|`ui8`|Unsigned 8bit integer|8|1|
|`si16`|Podepsané 16bitové celé číslo|`ui16`|Nepodepsané 16bitové celé číslo|16|2|
|`si32`|Signed 32bit integer|`ui32`|Unsigned 32bit integer|32|4|
|`si64`|Signed 64bit integer|`ui64`|Unsigned 64bit integer|64|16|
|`si128`|Signed 128bit integer|`ui128`|Unsigned 128bit integer|128|32|
|`si256`|Podepsané 256bitové celé číslo|`ui256`|Nezapsané 256bitové celé číslo|256|64|

Preferovaným (výchozím) typem celého čísla je `si64` (64bitové celé číslo se znaménkem), následované `ui64` (64bitové celé číslo bez znaménka).
Je to proto, že SP-Lang je primárně určen pro 64bitové procesory.

`int` je alias pro `si64`.

!!! warning

	
	
	
	256bitové velikosti zatím nejsou plně podporovány.
	
	

### Boolean

Boolean (`bool`) je typ, který má jednu ze dvou možných hodnot označených jako `True` a `False`.


### Floating-Point

Čísla s pohyblivou řádovou čárkou jsou desetinná čísla, například 3,14 nebo -0,5, která jsou užitečná pro výpočty zahrnující zlomky nebo přesnější hodnoty.

|Typ|Název|Bajtů|
|:----|:----|:----|
|`fp16`|16bit float|2|
|`fp32`|32bit float|4|
|`fp64`|64bit float|8|
|`fp128`|128bit float|16|


!!! warning

	
	
	
	`fp16` a `fp128` nejsou plně podporovány.
	
	

!!! warning

	
	
	
	Alias `float` se překládá na `fp64`, který se překládá na LLVM `double` (odlišný od aliasu `float`).
	
	
	

## Složené skalární typy

Komplexní skalární typy jsou určeny pro hodnoty, které poskytují nějakou vnitřní strukturu (technicky vzato jsou to tedy záznamy nebo tuply), ale mohou se vejít do skalárního typu (např. z důvodu výkonu nebo optimalizace).


### Datum/čas

`datetime`

Jedná se o hodnotu, která reprezentuje datum a čas v UTC s využitím struktury broken time.
Lomený čas znamená, že `rok`, `měsíc`, `den`, `hodina`, `minuta`, `sekunda` a `mikrosekunda` jsou uloženy ve vyhrazených polích; liší se např. od časového razítka UNIX.

* Časové pásmo: UTC
* Rozlišení: mikrosekundy (šest desetinných míst)
* 64bitové celé číslo bez znaménka, také známé jako `ui64`



!!! info "Zlomené časové komponenty"

	
	
	* `y` / `year`
	* `m` / `měsíc`
	* `d` / `day`
	* `H` / `hour`
	* `M` / `minuta`
	* `S` / `sekunda`
	* `u` / `mikrosekunda`
	

Podrobnější popis data/času je [zde](../date-time).


### IP adresa

Tento datový typ obsahuje adresu IPv4 nebo IPv6.

`ip`

Základní skalární typ: `ui128`


!!! abstract "RFC 4291"

	
	
	IPv4 jsou mapovány do prostoru IPv6, jak je předepsáno v [RFC 4291 "IPv4-Mapped IPv6 Address"](https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.5.2).
	
	

## Obecné typy

Generické typy se používají v počáteční fázi parsování, optimalizace a kompilace SP-Langu.
Doplňujícím typem je _Specifický typ_.
SP-Lang převádí generické typy na specifické typy pomocí mechanismu zvaného _type inference_.
Pokud generický typ nelze převést na specifický, kompilace selže a je třeba poskytnout další informace pro typovou inferenci.

Generický typ začíná velkým písmenem `T`.
Také pokud typ kontejneru obsahuje generický typ, je samotný _kontejnerový typ_ nebo _strukturální typ_ považován za generický.


## Typy kontejnerů


### Seznam

`[Ti]`

* `Ti` označuje typ položky v seznamu


Seznam musí obsahovat nulu, jednu nebo více položek *stejného typu*.

Typem konstruktoru je výraz `!LIST`.


### Set

`{Ti}`

 * `Ti` odkazuje na typ položky v množině

Typem konstruktoru je výraz `!SET`.


### Slovník

`{Tk:Tv}`

 * `Tk` odkazuje na typ klíče
 * `Tv` označuje typ hodnoty

Konstruktor typu je výraz `!DICT`.


### Bag


`[(Tk,Tv)]`

 * `Tk` odkazuje na typ klíče
 * `Tv` označuje typ hodnoty

Bag (neboli multimap) je kontejner, který umožňuje duplicitní klíče, na rozdíl od slovníku, který umožňuje pouze jedinečné klíče.

!!! tip

	
	
	
	Sáček je v podstatě seznamem 2 dvojic (párů).
	
	

## Typy produktů

[Typ produktu](https://en.wikipedia.org/wiki/Product_type) je složený typ, který vznikl spojením jiných typů do _struktury_.


### Tuple


Signatura: `(T1, T2, T3, ...)`

Konstruktor typu je výraz `!TUPLE`.

Je ekvivalentní [typu struktury](https://llvm.org/docs/LangRef.html#structure-type) v LLVM IR.

!!! tip

	
	
	
	Tuple bez členů respektive `()` je [jednotka](https://en.wikipedia.org/wiki/Unit_type).
	
	

### Záznam

Signatura: `(name1: T1, name2: T2, name3: T3, ...)`

Typem konstruktoru je výraz `!RECORD`.

Je ekvivalentní výrazu `struct` jazyka C.


## Součtový typ

Typ [Sum](https://en.wikipedia.org/wiki/Tagged_union) je datová struktura používaná k uchování hodnoty, která může nabývat několika různých typů.

### libovolný

`any`

Typ `any` je speciální typ, který představuje hodnotu, která může mít libovolný typ.


!!! warning

	
	
	
	Typ `any` by neměl být používán jako preferovaný typ, protože má režijní náklady.
	Přesto je poměrně užitečný při psaní slovníku, který kombinuje typy (např. `{str:any}`), a v dalších situacích, kdy typ hodnoty není při kompilaci znám.
	
	Hodnota obsažená v typu `any` je vždy umístěna v paměti (např. v paměťovém fondu); z tohoto důvodu je tento typ pomalejší než ostatní, které hodnotu ukládají přednostně do registrů procesoru.
	

Typ `any` je rekurzivní typ; může obsahovat sám sebe, protože obsahuje všechny ostatní typy v typovém univerzu.
Z tohoto důvodu nelze vypočítat obecnou nebo dokonce maximální velikost proměnné `any`.


## Objektové typy

### String

`str`

Musí být v kódování UTF-8.

!!! note

	
	
	
	`str` by mohl být předáván do `[ui8]` (seznam `ui8`) způsobem 'toll-free'; jedná se o binární ekvivalent.
	
	

### Bajty


!!! warning "Work in progress"

	
	
	Plánované
	
	

### Enum


!!! warning "Nedokončená výroba"

	
	
	Plánované
	
	
	

### Regex

`regex`

Obsahuje zkompilovaný vzor regulárního výrazu.

Pokud je vzor regexu konstantní, je zkompilován v době kompilace příslušného výrazu.
V případě dynamického regexového vzoru probíhá kompilace regexu během vyhodnocování výrazu.


### JSON

`json<SCHEMA>`

JSON objekt, výsledek parsování JSON.
Jedná se o typ založený na schématu.


## Typ funkce

### Funkce


`(arg1:T1,arg2:T2,arg3:T3)-&gt;Tr`

* `T1`, `T2`, `T3` jsou typy vstupů funkcí `arg1`, `arg2` a `arg3`.
* `Tr` udává typ výstupu funkce


## Pythonovské typy

Pythonovské typy jsou objektové typy, které poskytují rozhraní s jazykem Python.


### Python Dictionary

`pydict<SCHEMA>`

Slovník [Pythonu](https://docs.python.org/3/c-api/dict.html).
Jedná se o typ založený na schématu.


### Python Object

`pyobj`

Obecný [Python objekt](https://docs.python.org/3/c-api/object.html).


### Python List

`pylist`

Seznam [Python](https://docs.python.org/3/c-api/list.html).



### Python Tuple

`pytuple`


## Casting

Pro změnu typu hodnoty použijte výraz `!CAST`.
```yaml

!CAST
what: 1234
typ: fp32
```

nebo ekvivalentní zkratka:
```yaml

!!fp32 1234
```

!!! note

	
	
	
	Cast je také skvělým pomocníkem pro typovou inferenci, to znamená, že jej lze v případě potřeby použít k explicitnímu určení typu.
	
	

## Typy založené na schématu

_Schema_ je koncept SP-Langu, jak propojit systémy bez schémat, jako je JSON nebo Python, se silně typizovaným SP-Langem.
Schéma je v podstatě adresář, který mapuje pole na jejich typy atd.
Další informace najdete v kapitole o SP-Langu [schémata](../schema).

Typ založený na schématu SP-Lang specifikuje schéma pomocí _jména schématu_: `json<SCHEMANAME>`.
Název _schema_ slouží k vyhledání definice schématu např. v knihovně.

Seznam typů založených na schématu:
 * `pydict<...>`
 * `json<...>`

### Sestavená schémata

 * ` `ANY`: Toto schéma deklaruje, že každý člen je typu `any`.
 * `VOID`: Toto schéma nemá žádný člen, pro určení typů polí použijte definici typu na místě.
