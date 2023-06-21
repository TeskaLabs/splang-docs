---
git_commit_hash: b55fa3f
title: Agregát
---

# Souhrnné výrazy

Agregační výraz je typ funkce, která provádí výpočty nad množinou hodnot a jako výsledek vrací jednu hodnotu.
Tyto výrazy se běžně používají k shrnutí nebo zhuštění dat.

---

## `!AVG`: Průměr 

Vypočítá průměr / aritmetický průměr.

Typ: _Posloupnost_

!!! info

	
	
	
	Více informací o [aritmetickém průměru](https://en.wikipedia.org/wiki/Arithmetic_mean) na Wikipedii.
	

!!! example

	
	
	```yaml
	
	!AVG
	- 6
	- 2
	- 4
	```
	
	Výpočet průměru `(6+2+4)/3`, výsledek je `3`.
	

---

## `!MAX`: Maximální 

Vrací maximální hodnotu z posloupnosti.

Typ: _Sequence_

!!! example

	
	
	```yaml
	
	!MAX
	- 1.5
	- 2.6
	- 5.1
	- 3.05
	- 4.45
	```
	
	Výsledek tohoto výrazu je `5,1`.
	

---

## `!MIN`: Minimální 

Vrací minimální hodnotu z posloupnosti.

Typ: _Sequence_

!!! example

	
	
	```yaml
	
	!MIN
	- 2.6
	- 3.05
	- 4.45
	- 0.5
	- 5.1
	```
	
	Výsledek tohoto výrazu je `0,5`.
	

---

## `!COUNT`: Počítejte počet položek 

Spočítá počet položek v kontejneru.

Typ: _Sequence_

!!! example

	
	
	```yaml
	
	!COUNT
	- Frodo Pytlík
	- Sam Gamgee
	- Gandalf
	- Legolas
	- Gimli
	- Aragorn
	- Boromir z Gondoru
	- Smíšek Brandybuck
	- Pipin Took
	```
	
	Vrací `9`.
	

---

## `!MEDIAN`: Střední hodnota 

Medián je prostřední hodnota v seznamu čísel; polovina hodnot je větší než medián a polovina je menší než medián.
Pokud má seznam sudý počet prvků, je medián průměrem dvou středních hodnot.

Typ: Typ: _Posloupnost_


!!! info

	
	
	
	Více informací o [medián](https://en.wikipedia.org/wiki/Median) na Wikipedii.
	
	


!!! example

	
	
	```yaml
	!MEDIAN
	- 1
	- 4
	- -1
	- 9
	- 101
	```
	

---

## `!MODE`: Hodnota, která se objevuje nejčastěji 

Mode je hodnota nebo hodnoty, které se v seznamu vyskytují nejčastěji.
Lze jej použít k vyjádření centrální tendence souboru dat.

Typ: _Posloupnost_

!!! info

	
	
	
	Více informací o [mode](https://en.wikipedia.org/wiki/Mode_%28statistics%29) na Wikipedii.
	
	


!!! example

	
	
	```yaml
	!MODE
	- -10
	- -10
	- -20
	- -20
	- 1
	- 2
	- 3
	- 4
	- 5
	```
	

---

## `!RANGE`: Rozdíl mezi největší a nejmenší hodnotou 

Vypočítá rozdíl mezi největší a nejmenší hodnotou.

Typ: Typ: _Posloupnost_

!!! info

	
	
	
	Více informací o [range](https://en.wikipedia.org/wiki/Range_%28statistics%29) na Wikipedii.
	


!!! example

	
	
	```yaml
	!RANGE
	- 1
	- 3
	- 4
	- 20
	- -1
	```

