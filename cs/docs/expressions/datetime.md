---
git_commit_hash: b55fa3f
title: Datum/čas
---

# Výrazy pro datum a čas


Datum a čas se v SP-Langu vyjadřuje pomocí typu `datetime`.
Má mikrosekundové rozlišení a rozsah od roku 8190 př. n. l. do roku 8191.
Je v časovém pásmu UTC.

!!! info

	
	
	
	Další informace o typu `datatime` najdete [zde](../../language/date-time).
	

---

## `!NOW`: Aktuální datum a čas 

Typ: _Mapping_.

Získání aktuálního data a času.
```yaml

!NOW
```

---

## `!DATETIME`: Zkonstruujte datum/čas 

Typ: _Mapování_.

Konstruuje `datový čas` ze složek, jako je rok, měsíc, den atd.

```yaml

!DATETIME
rok: <year>
měsíc: <month>
den: <day>
hodina: <hour>
minuta: <minute>
hodina: sekunda: <second>
mikrosekunda: <microsecond>
časové pásmo: <timezone>
```

8191: * `rok` je celé číslo v rozsahu -8190 ... 8191.
* `měsíc` je celé číslo v rozsahu 1 ... 12.
* `day` je celé číslo v rozsahu 1 ... 31, odpovídající počtu dní v daném měsíci.
* `hour` je celé číslo v rozsahu 0 ... 24, je nepovinné a výchozí hodnota je `0`.
* `minuta` je celé číslo v rozsahu 0 ... 59, je nepovinné a výchozí hodnota je `0`.
* `sekunda` je celé číslo v rozsahu 0 ... 60, je nepovinné a výchozí hodnota je `0`.
* `mikrosekunda` je celé číslo v rozsahu 0 ... 1000000, je nepovinné a výchozí hodnota je `0`.
* `timezone` je název [IANA Time Zone Database](https://www.iana.org/time-zones) časového pásma. Je nepovinný a výchozí časové pásmo je UTC.



!!! example "Příklad: Datum/čas UTC"

	
	
	```yaml
	!DATETIME
	rok: 2021
	měsíc: 10
	den: 13
	hodina: 12
	minuta: 34
	sekunda: 56
	mikrosekunda: 987654
	```
	


!!! example "Příklad: výchozí hodnoty"

	
	
	```yaml
	!DATETIME
	year: 2021
	měsíc: 10
	den: 13
	```
	
	


!!! example "Příklad: časové pásmo"

	
	
	```yaml
	!DATETIME
	year: 2021
	month: 10
	den: 13
	časové pásmo: Evropa/Praha
	```
	
	```yaml
	!DATETIME
	rok: 2021
	měsíc: 10
	den: 13
	časové pásmo: "+05:00"
	```
	

---

## `!DATETIME.FORMAT`: Formátování data/času 

Typ: _Mapování_.

Formátuje informace o datu a čase na základě `datetime`.

```yaml

!DATETIME.FORMAT
s: <datetime>
format: <format>
timezone: <string>
```

`datetime` obsahuje informace o datech a čase, které se mají použít pro formátování.
`formát` je řetězec, který obsahuje specifikaci formátu výstupu.
`Časové pásmo` je nepovinná informace, pokud je uvedena, bude čas vypsán v místním čase zadaném argumentem, jinak se použije časové pásmo UTC.

### Formát

* `%H`: Hodiny (24hodinové hodiny) jako desetinné číslo doplněné nulou.
* `%M`: Minuta jako desetinné číslo doplněné nulou.
* `%S`: Vteřina jako desetinné číslo s nulovým znaménkem.
* `%f`: Mikrosekunda jako desetinné číslo doplněné nulou na 6 číslic.
* `%I`: Hodina (12hodinové hodiny) jako desetinné číslo doplněné nulou.
* `%p`: Ekvivalent AM nebo PM v místním jazyce.

* `%d`: Den v měsíci jako desetinné číslo s nulou.
* `%m`: Měsíc jako desetinné číslo s nulou.
* `%y`: Rok bez století jako desetinné číslo s nulou.
* `%Y`: Rok se stoletím jako desetinné číslo.

* `%z`: Posun UTC.

* `%a`: Zkrácený název dne v týdnu.
* `%A`: Den v týdnu jako plný název.
* `%w`: Den v týdnu jako desetinné číslo, kde 0 je neděle a 6 je sobota.
* `%b`: Měsíc jako zkrácený název.
* `%B`: Měsíc jako plný název.
* `%j`: Den v roce jako desetinné číslo s nulou.
* `%U`: Číslo týdne v roce (neděle jako první den v týdnu) jako desetinné číslo s nulou. Všechny dny v novém roce předcházející první neděli se považují za dny v týdnu 0.
* `%W`: Číslo týdne v roce (pondělí jako první den týdne) jako desetinné číslo s nulou. Všechny dny v novém roce předcházející prvnímu pondělí se považují za dny v týdnu 0.

* `%c`: Zobrazení data a času.
* `%x`: Reprezentace data.
* `%X`: Reprezentace času.

* `%%`: Doslovný znak '%'.


!!! example

	
	
	```yaml
	
	!DATETIME.FORMAT
	s: !NOW
	format: "%Y-%m-%d %H:%M:%S"
	časové pásmo: "Europe/Prague"
	```
	
	Vypíše aktuální místní čas jako např. `2022-12-31 12:34:56` s použitím časového pásma "Europe/Prague".
	
	

---

## `!DATETIME.PARSE`: Parsování data/času 

Typ: _Mapping_.

Parsování data a času z řetězce.

```yaml

!DATETIME.PARSE
what: <string>
format: <format>
časové pásmo: <timezone>
```

Vstupní řetězec `what` analyzuje pomocí řetězce `format`.
Informace `timezone` je nepovinná, pokud je uvedena, pak určuje místní časové pásmo řetězce `what`.

Další informace o řetězci `format` naleznete v kapitole "Formát" výše.



!!! example

	
	
	```yaml
	!DATETIME.PARSE
	what: "2021-06-29T16:51:43-08"
	format: "%y-%m-%dT%H:%M:%S%z"
	```
	

---

## `!GET`: Získat komponentu datum/čas 

Typ: _Mapping_.

Výběr komponenty data/času, jako je hodina, minuta, den atd. z `datetime`.

```yaml

!GET
co: <string>
z: <datetime>
časové pásmo: <timezone>
```

Výpis složky `what` z `datetime`.
Časová zóna` je nepovinná, pokud není uvedena, použije se časová zóna UTC.

### Komponenty

* `year`, `y`: Year
* `Měsíc`, `m`: Month
* `day`, `d`: Day

* `hour`, `H`: Hodina
* `minute`, `M`: minuta
* `second`, `S`: Second
* `mikrosekunda`, `f`: Microsecond

* `weekday`, `w`: Day of the week

!!! example

	
	
	```yaml
	
	!GET
	co: H
	od: !TEĎ
	časové pásmo: "Europe/Prague"
	```
	
	Získá složku "hours" aktuálního časového razítka s použitím časového pásma "Europe/Prague".
	
	


!!! example "Příklad: Získat aktuální rok"

	
	
	```yaml
	!GET { what: year, from: !NOW }
	```
	

