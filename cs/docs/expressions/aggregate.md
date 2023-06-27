---
git_commit_hash: b55fa3f
title: Agregační
---

# Agregační výrazy

Agregační výraz je typ funkce, která provádí výpočty nad množinou hodnot a jako výsledek vrací jednu hodnotu.
Tyto výrazy se běžně používají k shrnutí nebo zhuštění dat.

---

## `!AVG`: Průměr (aritmetický průměr)

Vypočítá aritmetický průměr.

Typ: _Sequence_

!!! info

	Více informací o [aritmetickém průměru](https://cs.wikipedia.org/wiki/Aritmetick%C3%BD_pr%C5%AFm%C4%9Br) na Wikipedii.
	

!!! example "Příklad"

	```yaml
	
	!AVG
	- 6
	- 2
	- 4
	```
	
	Výpočet průměru `(6+2+4)/3`, výsledek je `4`.

---

## `!MAX`: Maximum

Vrací maximální hodnotu z posloupnosti.

Typ: _Sequence_

!!! example "Příklad"

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

## `!MIN`: Minimum

Vrací minimální hodnotu z posloupnosti.

Typ: _Sequence_

!!! example "Příklad"

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

## `!COUNT`: Počet položek

Spočítá počet položek v seznamu.

Typ: _Sequence_

!!! example "Příklad"

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
	
	Výsledek tohoto výrazu je `9`.
	

---

## `!MEDIAN`: Medián (prostřední hodnota)

Medián je prostřední hodnota v seznamu čísel; polovina hodnot je větší než medián a polovina je menší než medián.
Pokud má seznam sudý počet prvků, je medián aritmetickým průměrem dvou prostředních hodnot.

Typ: _Sequence_


!!! info

	Více informací o [medián](https://cs.wikipedia.org/wiki/Medi%C3%A1n) na Wikipedii.
	

!!! example "Příklad"

	```yaml
	!MEDIAN
	- 1
	- 4
	- -1
	- 9
	- 101
	```
	
	Výsledek výrazu je `4`.

---

## `!MODE`: Modus (hodnota vyskytující se nejčastěji)

Modus je označení pro hodnotu nebo hodnoty, které se v seznamu vyskytují nejčastěji.
Lze ji použít k vyjádření centrální tendence souboru dat.

Typ: _Sequence_

!!! info

	Více informací o [mode](https://cs.wikipedia.org/wiki/Modus) na Wikipedii.


!!! example "Příklad"

	```yaml
	!MODE
	- 10
	- 10
	- -20
	- -20
	- 6
	- 10
	```

	Výsledek výrazu je `10`.
	

---

## `!RANGE`: Rozdíl mezi největší a nejmenší hodnotou 

Range určuje rozdíl mezi největší a nejmenší hodnotou. V češtině je pro něj též užívaný termín "variační rozpětí".

Typ: _Sequence_

!!! info

	Více informací o [range](https://cs.wikipedia.org/wiki/Varia%C4%8Dn%C3%AD_rozp%C4%9Bt%C3%AD) na Wikipedii.
	

!!! example "Příklad"

	```yaml
	!RANGE
	- 1
	- 3
	- 4
	- 20
	- -1
	```
