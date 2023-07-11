---
git_commit_hash: b55fa3f
title: Parsec
---

# Výrazy pro PARSEC


Skupina výrazů PARSEC reprezentuje koncept [Parser combinator](https://en.wikipedia.org/wiki/Parser_combinator).

Poskytuje způsob, jak kombinovat základní parsery za účelem konstrukce složitějších parserů na základě určitých pravidel.
V tomto kontextu je parser funkce, která přijímá řetězec jako vstup a vytváří strukturovaný výstup, který indikuje úspěšné parsování nebo poskytuje chybové hlášení, pokud proces parsování selže.

Parsovací výrazy se dělí do dvou skupin: parsery a kombinátory.

_Parsery_ lze považovat za základní jednotky nebo stavební bloky. Jsou zodpovědné za rozpoznávání a zpracování konkrétních vzorů nebo prvků ve vstupním řetězci.

_Kombinátory_ jsou naproti tomu operátory nebo funkce, které umožňují kombinaci a skládání parserů.

Každý výraz pro parsování začíná předponou `!PARSE.`.


---

## `!PARSE.DIGIT`: Parsuje jednu číslici

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.DIGIT
```


!!! example

	_Vstupní řetězec:_ `2`

	```yaml
	!PARSE.DIGIT
	```

---

## `!PARSE.DIGITS`: Parsuje více číslic

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.DIGITS
min: <...>
max: <...>
exactly: <...>
```

Pole `min`, `max` a `exactly` jsou nepovinná.

!!! warning "Varování"

	Pole `Exactly` nelze použít společně s poli `min` nebo `max`. A samozřejmě hodnota `max` nesmí být menší než hodnota `min`.

!!! example "Příklad"

	_Vstupní řetězec:_ `123`

	```yaml
	!PARSE.DIGITS
	max: 4
	```
<details>

 <summary>Další příklady</summary>

Parsování co nejvíce číslic:

```yaml
!PARSE.DIGITS
```

Parsování přesně tří číslic:

```yaml
!PARSE.DIGITS
exactly: 3
```

Parsování alespoň dvou číslic, ale ne více než čtyř:

```yaml
!PARSE.DIGITS
min: 2
max: 4
```

</details>


---

## `!PARSE.LETTER`: Parsuje jedno písmeno
Latinská písmena od A do Z, malá i velká písmena.

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.LETTER
```

!!! example "Příklad"

	_Vstupní řetězec:_ `A`

	```yaml
	!PARSE.LETTER
	```


---

## `!PARSE.CHAR`: Parsuje jeden znak
Jakýkoli typ znaku.

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.CHAR
```

!!! example "Příklad"

	_Vstupní řetězec:_ `@`

	```yaml
	!PARSE.CHAR
	```


---

## `!PARSE.CHARS`: Parsuje posloupnost znaků

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.CHARS
min: <...>
max: <...>
exactly: <...>
```
Pole `min`, `max` a `přesně` jsou nepovinná.

!!! warning "Varování"

	Pole `Exactly` nelze použít společně s poli `min` nebo `max`. A samozřejmě hodnota `max` nesmí být menší než hodnota `min`.


!!! example "Příklad"

	_Vstupní řetězec:_ `jméno@123_`

	```yaml
	!PARSE.CHARS
	max: 8
	```

!!! tip

	Pro analýzu až do konce řetězce použijte `!PARSE.CHARS` bez polí.


<details>

 <summary>Další příklady</summary>

Parsování co nejvíce znaků:

```yaml
!PARSE.CHARS
```

Parsování přesně 3 znaků:

```yaml
!PARSE.CHARS
exactly: 3
```

Parsováníe alespoň 2 znaků, ale ne více než 4:

```yaml
!PARSE.CHARS
min: 2
max: 4
```

</details>


---

## `!PARSE.SPACE`: Parsuje jednu mezeru

Typ: _Parser_.

### Synopsis
```yaml

!PARSE.SPACE
```


---

## `!PARSE.SPACES`: Parsuje více mezer

Parsování co největšího počtu znaků mezery:

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.SPACES
```


---

## `!PARSE.ONEOF`: Parsuje jeden znak z množiny znaků

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.ONEOF
what: <...>
```
nebo kratší verze:

```yaml
!PARSE.ONEOF <...>
```

!!! example "Příklad"

	_Vstupní řetězec:_ `Wow!`

	```yaml
	!PARSE.ONEOF
	what: "!?"
	```


---

## `!PARSE.NONEOF`: Parsuje jeden znak, který není v množině znaků

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.NONEOF
what: <...>
```
nebo kratší verze:
```yaml
!PARSE.NONEOF <...>
```

!!! example "Příklad"

	_Vstupní řetězec:_ `Wow!`

	```yaml
	!PARSE.NONEOF
	what: ",;:[]()"
	```


---

## `!PARSE.UNTIL`: Parsuje posloupnost znaků, dokud není nalezen konkrétní znak

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.UNTIL
what: <...>
stop: <before/after>
eof: <true/false>
```
nebo kratší verze:

```yaml
!PARSE.UNTIL <...>
```

- `stop` - určuje, zda se má znak stop analyzovat nebo ne.
			Možné hodnoty: `before` nebo `after`(výchozí).

- `eof` - udává, zda máme analyzovat až do konce řetězce, pokud není nalezen symbol `what`.
			Možné hodnoty: `true` nebo `false`(výchozí).


!!! info

		Pole `what` musí být jednoznakové. Lze však použít i některé bílé znaky, jako např. `tab`.
	

!!! example "Příklad"

	_Vstupní řetězec:_ `60290:11`

	```yaml
	!PARSE.UNTIL
	what: ":"
	```

<details>

 <summary>Další příklady</summary>

Parsování až do symbolu <code>:</code> a zastavení před ním:

```yaml
!PARSE.UNTIL
what: ":"
stop: "před"
```

Parsování až do symbolu mezery a zastavení za ním:

```yaml
!PARSE.UNTIL ' '
```

Parsování až do symbolu <code>,</code> symbol nebo do konce řetězce, pokud není symbol nalezen.

```yaml
!PARSE.UNTIL
what: ","
eof: true
```

Parsování do symbolu <code>tab</code>:

```yaml
!PARSE.UNTIL
what: 'tab'
```
</details>


---

## `!PARSE.EXACTLY`: Parsovat přesně definovanou posloupnost znaků

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.EXACTLY
what: <...>
```

nebo kratší verze:

```yaml
!PARSE.EXACTLY <...>
```

!!! example "Příklad"

	_Vstupní řetězec:_ `Hello world!`

	```yaml
	!PARSE.EXACTLY
	what: "Hello"
	```


---

## `!PARSE.BETWEEN`: Parsuje posloupnost znaků mezi dvěma konkrétními znaky

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.BETWEEN
what: <...>
start: <...>
stop: <...>
escape: <...>
```

nebo kratší verze:

```yaml
!PARSE.BETWEEN <...>
```

- `what` - označuje, mezi kterými stejnými znaky máme provést parsování.

- `start`, `stop` - udává, mezi kterými různými znaky máme provést parsování.

- `escape` - označuje znak escape.


!!! example "Příklad"

	_Vstupní řetězec:_ `[10/May/2023:08:15:54 +0000]`
	```yaml

	!PARSE.BETWEEN
	start: '['
	stop: ']'
	```
	<details>

 <summary>Další příklady</summary>

Parsování mezi dvojitými uvozovkami:

```yaml
!PARSE.BETWEEN
what: '"'
```

Parsování mezi dvojitými uvozovkami, zkrácená forma:

```yaml
!PARSE.BETWEEN '"'
```

Parsování mezi dvojitými uvozovkami, přeskakuje interní dvojité uvozovky:<br>

<i>Vstupní řetězec:</i><code>"jedna, "dva", tři"</code>

```yaml
!PARSE.BETWEEN
what: '"'
escape: '\'
```
</details>


---

## `!PARSE.REGEX`: Parsuje posloupnost znaků, která odpovídá regulárnímu výrazu

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.REGEX
what: <...>
```

!!! example "Příklad"

	_Vstupní řetězec:_ `FTVW23_L-C: Message...`

	_Výstupní řetězec:_ `FTVW23_L-C`

	```yaml
	!PARSE.REGEX
	what: '[a-zA-Z0-9_\-0]+'
	```


---

## `!PARSE.MONTH`: Parsuje jméno měsíce

Typ: _Parser_.

### Synopsis

```yaml
!PARSE.MONTH
what: <...>
```

nebo kratší verze:

```yaml
!PARSE.MONTH <...>
```

- `what` - udává formát názvu měsíce. Možné hodnoty: `number`, `short`, `full`.

!!! tip

	Pomocí `!PARSE.MONTH` analyzujete název měsíce jako součást `!PARSE.DATETIME`.


!!! example "Příklad"

	_Vstupní řetězec:_ `10/`==May==`/2023:08:15:54`

	```yaml
	!PARSE.MONTH
	what: 'short'
	```

<details>

 <summary>Další příklady</summary>

Parsování měsíce v číselném formátu:<br>
<i>Vstupní řetězec</i>:<code><mark>2003-10-11</mark></code>

```yaml
!PARSE.MONTH 'číslo'
```

Parsování měsíce v plném formátu:<br>
<i>Vstupní řetězec:</i><code><mark>2003-OCTOBER-11</mark></code>

```yaml
!PARSE.MONTH
what: 'full'
```
</details>


---

## `!PARSE.FRAC`: Parsuje zlomek

Typ: _Parser_.

### Synopsis
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

	Pomocí `!PARSE.FRAC` lze analyzovat mikrosekundy nebo nanosekundy jako součást `!PARSE.DATETIME`.

!!! example "Příklad"

	_Vstupní řetězec:_ `Aug 22 05:40:14`==.264==

	```yaml
	!PARSE.FRAC
	base: "micro"
	max: 6
	```


---

## `!PARSE.DATETIME`: Parsování data v daném formátu

Typ: _Parser_.


### Synopsis

```yaml
!PARSE.DATETIME
- year: <...>
- month: <...>
- day: <...>
- hour: <...>
- minute: <...>
- second: <...>
- nanosecond: <...>
- timezone: <...>
```

- Pole `month`, `day` jsou povinná.
- Pole `year` je nepovinné. Pokud není zadáno, použije se funkce _smart year_.
- Pole `hour`, `minute`, `second`, `microsecond`, `nanosecond` jsou nepovinná. Pokud nejsou zadána, použije se výchozí hodnota 0.
- Zadání pole mikrosekund jako `microsecond?`, umožní parsovat mikrosekundy, pokud se vyskytují ve vstupním řetězci, a jinak ne.
- Pole `timezone` je nepovinné. Pokud není zadáno, použije se výchozí hodnota `UTC`. Lze jej zadat ve dvou různých formátech.
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

!!! example "Příklad"

	_Vstupní řetězec:_ `2022-10-13T12:34:56.987654`
	```yaml

	!PARSE.DATETIME
	- year: !PARSE.DIGITS
	- '-'
	- month: !PARSE.MONTH 'číslo'
	- '-'
	- day: !PARSE.DIGITS
	- 'T'
	- hour: !PARSE.DIGITS
	- ':'
	- minute: !PARSE.DIGITS
	- ':'
	- second: !PARSE.DIGITS
	- microsecond: !PARSE.FRAC
					base: "micro"
					max: 6
	- timezone: "Europe/Prague"
	```

<details>
  <summary>Další příklady</summary>

Parsování data bez roku, s krátkým tvarem měsíce a volitelnými mikrosekundami:

<br>

<i>Vstupní řetězec</i>: <code>Aug 17 06:57:05.189</code>

```yaml
!PARSE.DATETIME
- month: !PARSE.MONTH 'short' # Měsíc
- !PARSE.SPACE
- day: !PARSE.DIGITS # Den
- !PARSE.SPACE
- hour: !PARSE.DIGITS # Hodiny
- !PARSE.EXACTLY { what: ':' }
- minute: !PARSE.DIGITS # Minuty
- !PARSE.EXACTLY { what: ':' }
- second: !PARSE.DIGITS # Sekundy
- microsecond?: !PARSE.FRAC # Mikrosekundy
				base: "micro"
				max: 6
```

Parse datetime s časovou zónou:
<br>
<i>Vstupní řetězec:</i> <code>2021-06-29T16:51:43+08:00</code>

```yaml
!PARSE.DATETIME
- year: !PARSE.DIGITS
- '-'
- month: !PARSE.MONTH 'číslo'
- '-'
- day: !PARSE.DIGITS
- 'T'
- hour: !PARSE.DIGITS
- ':'
- minute: !PARSE.DIGITS
- ':'
- second: !PARSE.DIGITS
- timezone: !PARSE.CHARS
```

Parse datetime pomocí zkratky:<br>
<i>Vstupní řetězec:</i> <code>2021-06-29T16:51:43Z</code>

```yaml
!PARSE.DATETIME RFC3339
```

Parsování datetime pomocí zkratky:<br>
<i>Vstupní řetězec:</i> <code>20201211T111721Z</code>

```yaml
!PARSE.DATETIME iso8601
```

Parsování data s nanosekundami:<br>
<i>Vstupní řetězec:</i> <code>2023-03-23T07:00:00.734323900</code>

```yaml
!PARSE.DATETIME
- year: !PARSE.DIGITS
- !PARSE.EXACTLY { what: '-' }
- month: !PARSE.DIGITS
- !PARSE.EXACTLY { what: '-' }
- day: !PARSE.DIGITS
- !PARSE.EXACTLY { what: 'T' }
- hour: !PARSE.DIGITS
- !PARSE.EXACTLY { what: ':' }
- minute: !PARSE.DIGITS
- !PARSE.EXACTLY { what: ':' }
- second: !PARSE.DIGITS
- nanosekunda: !PARSE.FRAC
  base: "nano"
  max: 9
```

</details>
