---
git_commit_hash: b55fa3f
title: Parsec
---

# Výrazy PARSEC


Skupina výrazů PARSEC představuje koncept [Parser combinator](https://en.wikipedia.org/wiki/Parser_combinator).

Poskytují způsob, jak kombinovat základní parsery za účelem konstrukce složitějších parserů pro konkrétní pravidla.
V tomto kontextu je parser funkce, která přijímá řetězec jako vstup a vytváří strukturovaný výstup, který indikuje úspěšné parsování nebo poskytuje chybové hlášení, pokud proces parsování selže.

Parsovací výrazy se dělí do dvou skupin: parsery a kombinátory.

*Parsery* lze považovat za základní jednotky nebo stavební bloky. Jsou zodpovědné za rozpoznávání a zpracování konkrétních vzorů nebo prvků ve vstupním řetězci.

*Kombinátory* jsou naproti tomu operátory nebo funkce, které umožňují kombinaci a skládání parserů.

Každý výraz začíná předponou `!PARSE.`.


---

## `!PARSE.DIGIT`: Parsovat jednu číslici

Typ: _Parser_.

### Synopse
```yaml

!PARSE.DIGIT
```


### Příklad
_Input string:_ `2`
```yaml

!PARSE.DIGIT
```

---

## `!PARSE.DIGITS`: Parsování posloupnosti číslic

Typ: _Parser_.

### Synopse

```yaml

!PARSE.DIGITS
min: <...>
max: <...>
přesně: <...>
```
Pole `min`, `max` a `přesně` jsou nepovinná.

!!! warning

	
	
	
	Pole `Exactly` nelze použít společně s poli `min` nebo `max`. A samozřejmě hodnota `max` nesmí být menší než hodnota `min`.
	
	
	

### Příklad
_Input string:_ `123`
```yaml

!PARSE.DIGITS
max: 4
```
<details>

 <summary>Další příklady</summary>

Rozeberte co nejvíce číslic:```yaml

!PARSE.DIGITS
```

Parsovat přesně 3 číslice:```yaml

!PARSE.DIGITS
přesně: 3
```

Parsovat alespoň 2 číslice, ale ne více než 4:```yaml

!PARSE.DIGITS
min: 2
max: 4
```

</details>


---

## `!PARSE.LETTER`: Parsovat jedno písmeno
Latinská písmena od A do Z, malá i velká písmena.

Typ: _Parser_.

### Synopse
```yaml

!PARSE.LETTER
```

### Příklad
_Input string:_ `A`
```yaml

!PARSE.LETTER
```


---

## `!PARSE.CHAR`: Parsování jednoho znaku
Jakýkoli typ znaku.

Typ: _Parser_.

### Synopse
```yaml

!PARSE.CHAR
```

### Příklad
_Input string:_ `@````yaml

!PARSE.CHAR
```


---

## `!PARSE.CHARS`: Parsovat posloupnost znaků

Typ: _Parser_.

### Synopse
```yaml

!PARSE.CHARS
min: <...>
max: <...>
přesně: <...>
```
Pole `min`, `max` a `přesně` jsou nepovinná.

!!! warning

	
	
	
	Pole `Exactly` nelze použít společně s poli `min` nebo `max`. A samozřejmě hodnota `max` nesmí být menší než hodnota `min`.
	

### Příklad
_Vstupní řetězec:_ `jméno@123_`
```yaml

!PARSE.CHARS
max: 8
```
!!! tip

	
	
	
	Pro analýzu až do konce řetězce použijte `!PARSE.CHARS` bez polí.
	
	
<details>

 <summary>Další příklady</summary>

Analyzujte co nejvíce znaků:```yaml

!PARSE.CHARS
```

Parsovat přesně 3 znaky:```yaml

!PARSE.CHARS
přesně: 3
```

Parsujte alespoň 2 znaky, ale ne více než 4:```yaml

!PARSE.CHARS
min: 2
max: 4
```

</details>


---

## `!PARSE.SPACE`: Parsování jednoho znaku mezery

Typ: _Parser_.

### Synopse
```yaml

!PARSE.SPACE
```


---

## `!PARSE.SPACES`: Parsovat posloupnost znaků mezery

Parsování co největšího počtu znaků mezery:

Typ: _Parser_.

### Synopse
```yaml

!PARSE.SPACES
```


---

## `!PARSE.ONEOF`: Parsování jednoho znaku z množiny znaků

Typ: _Parser_.

### Synopse
```yaml

!PARSE.ONEOF
co: <...>
```
nebo kratší verze:```yaml

!PARSE.ONEOF <...>
```

## Příklad
_Input string:_ `Wow`==!==
```yaml

!PARSE.ONEOF
co: "!?"
```


---

## `!PARSE.NONEOF`: Parsování jednoho znaku, který není v množině znaků

Typ: _Parser_.

### Synopse
```yaml

!PARSE.NONEOF
co: <...>
```
nebo kratší verze:```yaml

!PARSE.NONEOF <...>
```

## Příklad
_Input string:_ `Wow`==!==
```yaml

!PARSE.NONEOF
co: ",;:[]()"
```


---

## `!PARSE.UNTIL`: Parsovat posloupnost znaků, dokud není nalezen konkrétní znak.

Typ: _Parser_.

### Synopse
```yaml

!PARSE.UNTIL
co: <...>
stop: &lt;před/po&gt;
eof: &lt;pravda/nepravda&gt;
```
nebo kratší verze:```yaml

!PARSE.UNTIL <...>
```

- `stop` - určuje, zda se má znak stop analyzovat nebo ne.
            Možné hodnoty: `před` nebo `po`(výchozí).

- `eof` - udává, zda máme analyzovat až do konce řetězce, pokud není nalezen symbol `what`.
            Možné hodnoty: `true` nebo `false`(výchozí).


!!! info

	
	
	
	    Pole `what` musí být jednoznakové. Lze však použít i některé bílé znaky, např. `tab`.
	

## Příklad
_Vstupní řetězec:_ `60290:11`
```yaml

!PARSE.UNTIL
what: ":"
```
<details>

 <summary>Další příklady</summary>

Parsujte až do symbolu <code>:</code> a zastavte se před ním:```yaml

!PARSE.UNTIL
co: ":"
stop: "před"
```

Parsování až do symbolu mezery a zastavení za ním:```yaml

!PARSE.UNTIL ' '
```

Parse until <code>,</code> symbol nebo parse until the end of the string if it's not found:```yaml

!PARSE.UNTIL
co: ","
eof: true
```

Parse until symbol <code>tab</code>:```yaml

!PARSE.UNTIL
co: 'tab'
```
</details>


---

## `!PARSE.EXACTLY`: Parsovat přesně definovanou posloupnost znaků

Typ: _Parser_.

### Synopse
```yaml

!PARSE.EXACTLY
co: <...>
```
nebo kratší verze:```yaml

!PARSE.EXACTLY <...>
```

## Příklad
_Input string:_ `Hello world!`
```yaml

!PARSE.EXACTLY
co: "Hello"
```


---

## `!PARSE.BETWEEN`: Parsování posloupnosti znaků mezi dvěma konkrétními znaky

Typ: _Parser_.

### Synopse
```yaml

!PARSE.BETWEEN
co: <...>
start: <...>
stop: <...>
únik: <...>
```
nebo kratší verze:```yaml

!PARSE.BETWEEN <...>
```

- `what` - označuje, mezi kterými stejnými znaky máme provést parsování.

- `start`, `stop` - udává, mezi kterými různými znaky máme provést parsování.

- `escape` - označuje znak escape.


## Příklad
_Input string:_ `[10/May/2023:08:15:54 +0000]`
```yaml

!PARSE.BETWEEN
start: '['
stop: ']'
```
<details>

 <summary>Další příklady</summary>

Rozbor mezi dvojitými uvozovkami:```yaml

!PARSE.BETWEEN
what: '"'
```

Parsování mezi dvojitými uvozovkami, zkrácená forma:```yaml

!PARSE.BETWEEN '"'
```

Parse mezi dvojitými uvozovkami, escape interních dvojitých uvozovek:<br>

<i>Vstupní řetězec:</i><code>"jedna, "dva", tři"</code>
```yaml

!PARSE.BETWEEN
what: '"
escape: '\'
```
</details>


---

## `!PARSE.REGEX`: Parsování posloupnosti znaků, která odpovídá regulárnímu výrazu

Typ: _Parser_.

### Synopse
```yaml

!PARSE.REGEX
co: <...>
```

## Příklad
_Input string:_ `FTVW23_L-C: `

_Output string:_ `FTVW23_L-C`
```yaml

!PARSE.REGEX
co: '[a-zA-Z0-9_\-0]+'
```


---

## `!PARSE.MONTH`: Parse a month name

Typ: _Parser_.

### Synopse
```yaml

!PARSE.MONTH
co: <...>
```
nebo kratší verze:```yaml

!PARSE.MONTH <...>
```

- `what` - udává formát názvu měsíce.
            Možné hodnoty: `číslo`, `krátký`, `úplný`.

!!! tip

	
	
	Pomocí `!PARSE.MONTH` analyzujete název měsíce jako součást `!PARSE.DATETIME`.
	
	

## Příklad
_Input string:_ `10/`==May==`/2023:08:15:54``
```yaml

!PARSE.MONTH
what: 'short'
```
<details>

 <summary>Další příklady</summary>

Rozbor měsíce ve formátu čísla:<br>
<i>Vstupní řetězec</i>:<code><mark>2003-10-11</mark></code>```yaml

!PARSE.MONTH 'číslo'
```

Parsování měsíce v plném formátu:<br>
<i>Vstupní řetězec:</i><code><mark>2003-OCTOBER-11</mark></code>```yaml

!PARSE.MONTH
co: 'full'
```
</details>


---

## `!PARSE.FRAC`: Parse a fraction

Typ: _Parser_.

### Synopse
```yaml

!PARSE.FRAC
base: <...>
max: <...>
```

- `base` - udává základ zlomku.
            Možné hodnoty: `milli`, `micro`, `nano`.
- `max` - udává maximální počet číslic v závislosti na hodnotě `base`.
            Možné hodnoty: `3`, `6`, `9`.

!!! tip

	
	
	Pomocí `!PARSE.FRAC` můžete analyzovat mikrosekundy nebo nanosekundy jako součást `!PARSE.DATETIME`.
	
	

## Příklad
_Vstupní řetězec:_ `Aug 22 05:40:14`==.264==
```yaml

!PARSE.FRAC
base: "micro"
max: 6
```


---

## `!PARSE.DATETIME`: Parsování data v daném formátu

Typ: _Parser_.


### Synopse
```yaml

!PARSE.DATETIME
- year: <...>
- měsíc: <...>
- den: <...>
- den: hodina: <...>
- minuta: <...>
- hodina: sekunda: <...>
- nanosekunda: <...>
- časové pásmo: <...>
```

- Pole `měsíc`, `den` jsou povinná.
- Pole `rok` je nepovinné. Pokud není zadáno, použije se funkce _smart year_.
- Pole `hodina`, `minuta`, `sekunda`, `mikrosekunda`, `nanosekunda` jsou nepovinná. Pokud nejsou zadána, použije se výchozí hodnota 0.
- Zadání pole mikrosekund jako `mikrosekundy?`, umožní analyzovat mikrosekundy nebo ne, záleží na jejich přítomnosti ve vstupním řetězci.
- Pole `časová zóna` je nepovinné. Pokud není zadáno, použije se výchozí hodnota `UTC`.
  - `Časové pásmo` lze zadat ve dvou různých formátech.
    1. `Z`, `+08:00` - analyzuje se ze vstupního řetězce.
    2. `Evropa/Praha` - zadáno jako konstantní hodnota.


### Zkratky
K dispozici jsou tvary zkratek (v obou nižších/vyšších variantách):
```yaml

!PARSE.DATETIME RFC3339
```
```yaml

!PARSE.DATETIME iso8601
```

## Příklad
_Input string:_ `2022-10-13T12:34:56.987654`
```yaml

!PARSE.DATETIME
- rok: !PARSE.DIGITS
- '-'
- měsíc: !PARSE.MONTH 'číslo'
- '-'
- den: !PARSE.DIGITS
- 'T'
- hodina: !PARSE.DIGITS
- ':'
- minuta: !PARSE.DIGITS
- ':'
- sekunda: !PARSE.DIGITS
- mikrosekunda: !PARSE.FRAC
                base: "micro"
                max: 6
- časové pásmo: "Europe/Prague"
```
<details>

 <summary>Další příklady</summary>

Parsování data bez roku, s krátkým tvarem měsíce a volitelnými mikrosekundami:<br>
<i>Vstupní řetězec</i>: <code>Aug 17 06:57:05.189</code>```yaml

!PARSE.DATETIME
- měsíc: !PARSE.MONTH 'short' # Měsíc
- !PARSE.SPACE
- day: !PARSE.DIGITS # Den
- !PARSE.SPACE
- hodina: !PARSE.DIGITS # Hodiny
- !PARSE.EXACTLY { what: ':' }
- minute: !PARSE.DIGITS # Minuty
- !PARSE.EXACTLY { what: ':' }
- second: !PARSE.DIGITS # Sekundy
- microsecond?: !PARSE.FRAC # Mikrosekundy
                base: "micro"
                max: 6
```

Parse datetime s časovou zónou:<br>
<i>Vstupní řetězec:</i> <code>2021-06-29T16:51:43+08:00</code>```yaml

!PARSE.DATETIME
- rok: !PARSE.DIGITS
- '-'
- měsíc: !PARSE.MONTH 'číslo'
- '-'
- den: !PARSE.DIGITS
- 'T'
- hodina: !PARSE.DIGITS
- ':'
- minuta: !PARSE.DIGITS
- ':'
- sekunda: !PARSE.DIGITS
- časové pásmo: !PARSE.CHARS
```

Parse datetime pomocí zkratky:<br>
<i>Vstupní řetězec:</i> <code>2021-06-29T16:51:43Z</code>```yaml

!PARSE.DATETIME RFC3339
```

Parsování datetime pomocí zkratky:<br>
<i>Vstupní řetězec:</i> <code>20201211T111721Z</code>```yaml

!PARSE.DATETIME iso8601
```

Parsování data s nanosekundami:<br>
<i>Vstupní řetězec:</i> <code>2023-03-23T07:00:00.734323900</code>```yaml

!PARSE.DATETIME
- rok: !PARSE.DIGITS
- !PARSE.EXACTLY { what: '-' }
- month: !PARSE.DIGITS
- !PARSE.EXACTLY { what: '-' }
- den: !PARSE.DIGITS
- !PARSE.EXACTLY { what: 'T' }
- hodina: !PARSE.DIGITS
- !PARSE.EXACTLY { what: ':' }
- minuta: !PARSE.DIGITS
- !PARSE.EXACTLY { what: ':' }
- sekunda: !PARSE.DIGITS
- nanosekunda: !PARSE.FRAC
  base: "nano"
  max: 9
```

</details>
