---
title: Typy
---

# Datové typy SP-Lang

V SP-Lang hraje [typový systém](https://en.wikipedia.org/wiki/Type_system) klíčovou roli při zajišťování správnosti a efektivity vykonávání výrazů.  
SP-Lang využívá odvozování typů.  
To znamená, že _typový systém_ funguje na pozadí, poskytuje vysoký výkon, aniž by zatěžoval uživatele svými složitostmi.  
Tento přístup umožňuje bezproblémový a uživatelsky přívětivý zážitek, kde pokročilí uživatelé mohou přistupovat k typovému systému pro jemnější kontrolu a optimalizaci.

!!! info

    Typový systém je soubor pravidel, která definují, jak jsou datové typy klasifikovány, kombinovány a manipulovány v jazyce.  
    Pomáhá odhalit potenciální chyby již na začátku, zlepšuje spolehlivost kódu a zajišťuje, že operace jsou prováděny pouze na kompatibilních datových typech.

## Skalarové typy

Skalarové typy jsou základními stavebními kameny jazyka, které představují jednotlivé hodnoty.  
Jsou nezbytné pro práci s různými druhy dat a provádění různých operací.

### Celá čísla

Celá čísla jsou celá čísla, jako -5, 0 nebo 42, která mohou být použita pro počítání nebo jednoduché aritmetické operace.  
Celá čísla mohou být podepsaná nebo nepodepsaná.

|Typ|Název|Typ|Název|Bity|Byty|
|:----|:----|:----|:----|:----|:----|
|`si8`|Podepsané 8bitové celé číslo|`ui8`|Nepodepsané 8bitové celé číslo|8|1|
|`si16`|Podepsané 16bitové celé číslo|`ui16`|Nepodepsané 16bitové celé číslo|16|2|
|`si32`|Podepsané 32bitové celé číslo|`ui32`|Nepodepsané 32bitové celé číslo|32|4|
|`si64`|Podepsané 64bitové celé číslo|`ui64`|Nepodepsané 64bitové celé číslo|64|8|
|`si128`|Podepsané 128bitové celé číslo|`ui128`|Nepodepsané 128bitové celé číslo|128|16|
|`si256`|Podepsané 256bitové celé číslo|`ui256`|Nepodepsané 256bitové celé číslo|256|32|

Preferovaný (výchozí) typ celého čísla je `si64` (podepsané 64bitové celé číslo), následované `ui64` (nepodepsané 64bitové celé číslo).  
To je proto, že SP-Lang je navržen primárně pro 64bitové CPU.

`int` je alias pro `si64`.

!!! warning

    256bitové velikosti zatím nejsou plně podporovány.

### Booleovský

Booleovský (`bool`) je typ, který má jednu ze dvou možných hodnot označených jako `True` a `False`.

### Čísla s plovoucí desetinnou čárkou

Čísla s plovoucí desetinnou čárkou jsou desetinná čísla, jako 3.14 nebo -0.5, která jsou užitečná pro výpočty zahrnující zlomky nebo přesnější hodnoty.

|Typ|Název|Byty|
|:----|:----|:----|
|`fp16`|16bitové float|2|
|`fp32`|32bitové float|4|
|`fp64`|64bitové float|8|
|`fp128`|128bitové float|16|

!!! warning

    `fp16` a `fp128` nejsou plně podporovány.

!!! warning

    Alias `float` se překládá na `fp64`, což se překládá na LLVM `double` (odlišné od aliasu `float`).

## Složené skalarové typy

Složené skalarové typy jsou navrženy pro hodnoty, které poskytují nějakou vnitřní strukturu (takže technicky jsou to záznamy nebo n-tice), ale mohou se vejít do skalarového typu (např. pro účely výkonu nebo optimalizace).

### Datum/Čas

`datetime`

Toto je hodnota, která představuje datum a čas v UTC, pomocí rozbité struktury času.  
Rozbitý čas znamená, že `rok`, `měsíc`, `den`, `hodina`, `minuta`, `sekunda` a `mikrosekunda` jsou uloženy v dedikovaných polích; odlišně od např. UNIX timestamp.

* Časové pásmo: UTC
* Rozlišení: mikrosekundy (šest desetinných míst)
* 64bitové nepodepsané celé číslo, aka `ui64`

!!! info "Složky rozbitého času"

    * `y` / `rok`
    * `m` / `měsíc`
    * `d` / `den`
    * `H` / `hodina`
    * `M` / `minuta`
    * `S` / `sekunda`
    * `u` / `mikrosekunda`

Podrobnější popis data/času je [zde](./date-time.md).

### IP Adresa

Tento datový typ obsahuje adresu IPv4 nebo IPv6.

`ip`

Základní skalarový typ: `ui128`

!!! abstract "RFC 4291"

    IPv4 jsou mapovány do IPv6 prostoru, jak je předepsáno v [RFC 4291 "IPv4-Mapped IPv6 Address"](https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.5.2).  
    Například, IPv4 adresa `12.23.45.67` bude mapována do IPv6 adresy `::ffff:c17:2d43`.

### MAC Adresa

Tento datový typ obsahuje [MAC adresu](https://en.wikipedia.org/wiki/MAC_address), (EUI-48).

!!! note "Co je MAC adresa?"

    MAC adresa (zkratka pro medium access control address) je jedinečný identifikátor přiřazený síťové kartě atd.

`mac`

Základní skalarový typ: `ui64`, pouze 6 oktetů je použito v EUI-48.

### Geografická souřadnice

Tento typ představuje geografickou souřadnici, konkrétně délku a šířku.

`geopoint`

Základní skalarový typ: `u64`

Podrobnější popis geopointu je [zde](./geopoint.md).

## Obecné typy

Obecné typy se používají v rané fázi analýzy, optimalizace a kompilace SP-Lang.  
Doplnkový typ je _Specifický typ_.  
SP-Lang převádí obecné typy na specifické typy pomocí mechanismu zvaného _odvozování typů_.  
Pokud nelze obecný typ převést na specifický, kompilace selže a je potřeba poskytnout více informací pro odvozování typů.

Obecný typ začíná velkým `T`.  
Také pokud typ kontejneru obsahuje obecný typ, _typ kontejneru_ nebo _strukturní typ_ sám je považován za obecný.

## Typy kontejnerů

### Seznam

`[Ti]`

* `Ti` se odkazuje na typ položky v seznamu

Seznam musí obsahovat nula, jednu nebo více položek *stejného typu*.

Typový konstruktor je `!LIST` výraz.

### Množina

`{Ti}`

* `Ti` se odkazuje na typ položky v množině

Typový konstruktor je `!SET` výraz.

### Slovník

`{Tk:Tv}`

* `Tk` se odkazuje na typ klíče
* `Tv` se odkazuje na typ hodnoty

Typový konstruktor je `!DICT` výraz.

### Taška

`[(Tk,Tv)]`

* `Tk` se odkazuje na typ klíče
* `Tv` se odkazuje na typ hodnoty

Taška (aka multimap) je kontejner, který umožňuje duplicitní klíče, na rozdíl od slovníku, který umožňuje pouze jedinečné klíče.

!!! tip

    Taška je v podstatě seznam 2-nic (párů).

## Produktové typy

[Produktový typ](https://en.wikipedia.org/wiki/Product_type) je složený typ, vytvořený kombinováním jiných typů do _struktury_.

### N-tice

Podpis: `(T1, T2, T3, ...)`

Typový konstruktor je `!TUPLE` výraz.

Je ekvivalentní k [strukturnímu typu](https://llvm.org/docs/LangRef.html#structure-type) v LLVM IR.

!!! tip

    N-tice bez členů, respektive `()`, je [unit](https://en.wikipedia.org/wiki/Unit_type).

### Záznam

Podpis: `(name1: T1, name2: T2, name3: T3, ...)`

Typový konstruktor je `!RECORD` výraz.

Je ekvivalentní k C `struct`.

## Součet typ

[Součet typ](https://en.wikipedia.org/wiki/Tagged_union) je datová struktura používaná k uchování hodnoty, která může mít několik různých typů.

### Jakýkoliv

`any`

Typ `any` je speciální typ, který představuje hodnotu, která může mít jakýkoliv typ.

!!! warning

    Typ `any` by neměl být používán jako preferovaný typ, protože má dodatečné náklady.  
    Přesto je spíše užitečný pro typování slovníku, který kombinuje typy (např. `{str:any}`) a další situace, kde není typ hodnoty znám v době kompilace.

    Hodnota obsažená v typu `any` je vždy umístěna v paměti (např. paměťovém poolu); z tohoto důvodu je tento typ pomalejší než ostatní, které preferují ukládání hodnot v registrech CPU.

Typ `any` je rekurzivní typ; může obsahovat sám sebe, protože obsahuje všechny ostatní typy v typovém vesmíru.  
Z tohoto důvodu je nemožné vypočítat obecnou nebo dokonce maximální velikost proměnné `any`.

## Typy objektů

### Řetězec

`str`

Musí být v kódování UTF-8.

!!! note

    `str` může být převeden na `[ui8]` (seznam `ui8`) bez ztráty; je to binární ekvivalent.

### Byty

`binary`

Obsahuje binární data.


### Enum

!!! warning "Práce v pokroku"

    Plánováno

### Regex

`regex`

Obsahuje zkompilovaný vzor pro regulární výraz.

Pokud je vzor regexu konstantní, pak je zkompilován během příslušné doby kompilace výrazu.  
V případě dynamického vzoru regexu se kompilace regexu provádí během vyhodnocení výrazu.

### JSON

`json<SCHEMA>`

JSON objekt, výsledek JSON analýzy.  
Je to typ založený na schématu.

## Typ funkce

### Funkce

`(arg1:T1,arg2:T2,arg3:T3)->Tr`

* `T1`, `T2`, `T3` jsou typy vstupů funkcí `arg1`, `arg2` a `arg3` respektive.  
* `Tr` specifikuje výstupní typ funkce.

## Pythonické typy

Pythonické typy jsou typy objektů, které poskytují rozhraní s Pythonem.

### Python Slovník

`pydict<SCHEMA>`

[Python slovník](https://docs.python.org/3/c-api/dict.html).  
Je to typ založený na schématu.

### Python Objekt

`pyobj`

Obecný [Python objekt](https://docs.python.org/3/c-api/object.html).

### Python Seznam

`pylist`

[Python seznam](https://docs.python.org/3/c-api/list.html).

### Python N-tice

`pytuple`

## Přetypování

Použijte `!CAST` výraz pro změnu typu hodnoty.

```yaml
!CAST
what: 1234
type: fp32
```

nebo ekvivalentní zkrácenou verzi:

```yaml
!!fp32 1234
```

!!! note

    Přetypování je také skvělým pomocníkem pro odvozování typů, což znamená, že může být použito k explicitnímu označení typu, pokud je to potřeba.

## Typy založené na schématu

_Schéma_ je koncept SP-Lang, jak propojit systémy bez schématu, jako je JSON nebo Python, s pevně typovaným SP-Lang.  
Schéma je v podstatě adresář, který mapuje pole na jejich typy a tak dále.  
Pro více informací pokračujte do kapitoly o SP-Lang [schématech](../schema.md).

Typ založený na schématu SP-Lang specifikuje schéma pomocí _názvu schématu_: `json<SCHEMANAME>`.  
_Název schématu_ se používá k nalezení definice schématu např. v knihovně.

Seznam typů založených na schématu:
 * `pydict<...>`
 * `json<...>`

### Vestavěná schémata

 * `ANY`: Toto schéma deklaruje, že jakýkoliv člen má být typu `any`.  
 * `VOID`: Toto schéma nemá žádného člena, použijte definici typu na místě pro specifikaci typů polí.