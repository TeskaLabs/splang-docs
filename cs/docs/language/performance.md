---
git_commit_hash: b55fa3f
title: Výkon
---

# Výkon jazyka SP-Lang


## Úvod

SP-Lang je navržen tak, aby poskytoval velmi vysoký výkon.

Interně kompiluje poskytnuté výrazy do strojového kódu pomocí [LLVM IR](https://llvm.org) a velkého stupně optimalizací, které jsou možné díky funkcionální struktuře jazyka.
Nabízí extrémně vysokou propustnost jednoho jádra procesoru s bezproblémovou schopností škálovat zpracování podle dostupných jader procesoru a plně využívat výhod moderních architektur procesorů.

Výkonnostní testy měří propustnost v _EPS_, událostech za sekundu.
Události za sekundu je termín používaný ve správě IT pro definici počtu událostí, které jsou zpracovány výrazem SP-Lang za jednu sekundu.
EPS se měří pro jedno jádro procesoru.

Výkonnostní testy jsou automatizovány pomocí rámce CI/CD, a proto jsou zcela reprodukovatelné.


## Porovnávání více řetězců

Tento výraz vyhledává prvky konečné množiny řetězců ve vstupním textu.
Hodí se např. pro klasifikaci škodlivých adres URL (poskytnutých blokovým seznamem) ve výstupu firewallu.

```yaml
!IN
  where: !ARG url
  what:
  - ".000a.biz"
  - ".001edizioni.com"
 < 64 domains in total >
  - ".2win-tech.com"
  - ".2zzz.ru"
```
Tento seznam poskytuje projekt [blackweb](https://github.com/maravento/blackweb).

* Jádro jednoho procesoru na `HW-M1-20`: 1423686 EPS
* Jedno jádro CPU na `HW-I7-15`: 807685 EPS


## Parsování JSON
```yaml

!JSON.PARSE
what: |
  {
  	&lt; https://github.com/TeskaLabs/cysimdjson/blob/main/perftest/jsonexamples/test.json &gt;
  }
```

!!! note "Poznámka"
	Rychlé parsování JSON je zajištěno projekty [cysimdjson](https://github.com/TeskaLabs/cysimdjson), resp. [simdjson](https://simdjson.org)._.

* Jedno jádro procesoru na `HW-M1-20`: 968502 EPS
* Jedno jádro CPU na `HW-I7-15`: 562862 EPS


## Parsování IETF Syslogu

Toto je parser IETF Syslog aka [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424) implementovaný v SP-Langu:
```yaml

# Hlavička
- !PARSE.EXACTLY {what: '<'}
- !PARSE.DIGITS
- !PARSE.EXACTLY {what: '>'}
- !PARSE.DIGITS
- !PARSE.EXACTLY {what: ' '}

- !PARSE.TUPLE # Časové razítko
  - !PARSE.DIGITS # Rok
  - !PARSE.EXACTLY {what: '-'}
  - !PARSE.DIGITS # Měsíc
  - !PARSE.EXACTLY {what: '-'}
  - !PARSE.DIGITS # Den
  - !PARSE.EXACTLY {what: 'T'}
  - !PARSE.DIGITS # Hodiny
  - !PARSE.EXACTLY {what: ':'}
  - !PARSE.DIGITS # Minuty
  - !PARSE.EXACTLY {what: ':'}
  - !PARSE.DIGITS # Sekundy
  - !PARSE.EXACTLY {what: '.'}
  - !PARSE.DIGITS # Subsekundy
  - !PARSE.EXACTLY {what: 'Z'}

- !PARSE.EXACTLY {what: ' '} # HOSTNAME
- !PARSE.UNTIL {what: ' '}

- !PARSE.EXACTLY {what: ' '} # APP-NAME
- !PARSE.UNTIL {what: ' '}
 
- !PARSE.EXACTLY {what: ' '} # PROCID
- !PARSE.UNTIL {what: ' '}

- !PARSE.EXACTLY {what: ' '} # MSGID
- !PARSE.UNTIL {what: ' '}

- !PARSE.EXACTLY {what: ' '} # STRUCTURED-DATA
- !PARSE.OPTIONAL
  what: !PARSE.TUPLE
    - !PARSE.EXACTLY {what: '['}
    - !PARSE.UNTIL {what: ' '} # SD-ID
    - !PARSE.REPEAT  
      what:
      !PARSE.TUPLE # SD-PARAM
      - !PARSE.EXACTLY {what: ' '}
      - !PARSE.UNTIL {what: '='} # PARAM-NAME
      - !PARSE.EXACTLY {what: '='}
      - !PARSE.BETWEEN 
         what: '"'
         escaped: '\\"]'
```

* Jádro jednoho procesoru na `HW-M1-20`: 304004 EPS
* Jedno jádro CPU na `HW-I7-15`: 181494 EPS



## Referenční hardware

### HW-M1-20

* Stroj: MacBook Air (M1, 2020)
* CPU: [Apple M1](https://en.wikipedia.org/wiki/Apple_M1), uveden na trh v roce 2020

### HW-I7-15

* Stroj: MacBook Pro (15palcový, 2016)
* CPU: [I7-6700HQ](https://ark.intel.com/content/www/us/en/ark/products/88967/intel-core-i76700hq-processor-6m-cache-up-to-3-50-ghz.html), uveden na trh v roce 2015.
