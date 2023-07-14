---
git_commit_hash: b55fa3f
title: Datum/čas
---

# SP-Lang datum/čas 

Typ `datetime` je hodnota, která reprezentuje datum a čas v UTC s použitím struktury broken time.
Lomený čas znamená, že rok, měsíc, den, hodina, minuta, sekunda a mikrosekunda jsou uloženy ve vyhrazených polích; liší se např. od časového razítka UNIX.

* Časové pásmo: [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)
* Rozlišení: mikrosekundy (šest desetinných míst)


!!! tip "Užitečné nástroje"

	
	
		* [UNIX Timestamp](https://www.unixtimestamp.com)
		* [Převodník UTC na/z místního času](https://www.worldtimebuddy.com)
	
	

## Rozložení bitů

Datum je uloženo v 64bitovém celočíselném formátu bez znaménka (`ui64`); little-endian formát, nativní pro Intel/AMD 64bit.

<img src="../date-time-bit-layout.jpg" alt="Schema of the data/time bit layout" />

<table>
<thead>
	<tr>
		<th>Pozice</th>
		<th>Komponenta</th>
		<th>Bity</th>
		<th>Maska</th>
		<th>Typ*</th>
		<th>Rozsah</th>
		<th>Poznámka</th>
	</tr>
</thead>
<tbody>
	<tr style="border-top: 2px solid gray; background-color: #d0cecf;">
		<td>58-63</td>
		<td></td>
		<td>4</td>
		<td></td>
		<td></td>
		<td>0...15</td>
		<td>OK (0)/Chybný (8)/Vyhrazeno</td>
	</tr>
	<tr style="border-top: 1px solid gray; background-color: #f1ccb1;">
		<td>46-57</td>
		<td>rok</td>
		<td>14</td>
		<td></td>
		<td><code>si16</code></td>
		<td>-8190...8191</td>
		<td></td>
	</tr>
	<tr style="border-top: 1px solid gray; background-color: #fbe6a3;">
		<td>42-45</td>
		<td>měsíc</td>
		<td>4</td>
		<td>0x0F</td>
		<td><code>ui8</code></td>
		<td>1...12</td>
		<td>Indexováno od 1</td>
	</tr>
	<tr style="border-top: 1px solid gray; background-color: #fcf2cf;">
		<td>37-41</td>
		<td>den</td>
		<td>5</td>
		<td>0x1F</td>
		<td><code>ui8</code></td>
		<td>1...31</td>
		<td>Indexováno od 1</td>
	</tr>
	<tr style="border-top: 1px solid gray; background-color: #c1d5ed;">
		<td>32-36</td>
		<td>hodina</td>
		<td>5</td>
		<td>0x1F</td>
		<td><code>ui8</code></td>
		<td>0...24</td>
		<td></td>
	</tr>
	<tr style="border-top: 1px solid gray; background-color: #dfebf7;">
		<td>26-31</td>
		<td>minuta</td>
		<td>6</td>
		<td>0x3F</td>
		<td><code>ui8</code></td>
		<td>0...59</td>
		<td></td>
	</tr>
	<tr style="border-top: 1px solid gray; background-color: #cbe0b9;">
		<td>20-25</td>
		<td>druhý</td>
		<td>6</td>
		<td>0x3F</td>
		<td><code>ui8</code></td>
		<td>0...60</td>
		<td>60 je pro přestupnou sekundu</td>
	</tr>
	<tr style="border-top: 1px solid gray; border-bottom: 1px solid gray; background-color: #e3eedd;">
		<td>0-19</td>
		<td>mikrosekunda</td>
		<td>20</td>
		<td></td>
		<td><code>ui32</code></td>
		<td>0...1000000</td>
		<td></td>
	</tr>
</tbody>
</table>


!!! note

	
	
	
	*) Typ je doporučený/minimální typ zarovnaný na bajty pro příslušnou komponentu.
	
	

## Podrobnosti o časovém pásmu

Informace o časových pásmech pocházejí z [pytz](http://pytz.sourceforge.net), resp. z [IANA Time Zone Database](https://www.iana.org/time-zones).

!!! note

	
	
	
		Databáze časových pásem má přesnost na minuty, to znamená, že sekundy a mikrosekundy zůstávají při převodu z/do UTC nedotčeny _.
	

Data o časových pásmech jsou reprezentována adresářovou strukturou souborového systému, která je běžně umístěna na adrese `/usr/share/splang` nebo na místě určeném proměnnou prostředí `SPLANG_SHARE_DIR`.
Skutečná data časových pásem jsou uložena v podsložce `tzinfo`.
Data časových pásem jsou generována skriptem `generate_datetime_timezones.py` během instalace SPLangu.


!!! example "Příklad složky `tzinfo`"

	
	
		```
		.
		└── tzinfo
		  ├── Evropa
		    │ ├── Amsterdam.sptl
		    │ ├── Amsterdam.sptb
		    │ ├── Andorra.sptl
		    │ ├── Andorra.sptb
		```
	

Soubory `.sptl` a `.sptb` obsahují rychlostně optimalizované binární tabulky, které podporují rychlé vyhledávání pro převody místního času <-> UTC.
Soubor `.sptl` je určen pro little-endian architektury procesorů (x86 a x86-64), soubor `.sptb` je určen pro big-endian architektury.

Soubor je [memory-mapped](https://en.wikipedia.org/wiki/Memory-mapped_file) do paměťového prostoru procesu SP-Lang, zarovnaný na 64bajtovou hranici, takže jej lze přímo použít jako vyhledávač.

### Společné struktury

  * `ym`: Rok a měsíc, `ym = (rok &lt;&lt; 4) + měsíc`
  * `dhm`: Den, hodina a minuta, `dhm = (den &lt;&lt; 11) + (hodina &lt;&lt; 6) + minuta`

Obě struktury jsou bitovými částmi skalární hodnoty `datetime` a lze je z `datetime` extrahovat pomocí `AND` a `SHR`.**

### Záhlaví souboru časových pásem

Délka záhlaví v 64 bajtech.
Neurčené bajty jsou nastaveny na `0` a rezervovány pro budoucí použití.

  * Pozice `00...03`: `SPt` / magický identifikátor
  * Pozice `04`: `<` for little-endian CPU architecture, `>` pro big-endian
  * Pozice `05`: Verze (v současné době `1` ASCII znak)
  * Pozice `08...09`: Minimální rok/měsíc (`min_ym`) v tomto souboru, měsíc MUSÍ BÝT 1
  * Pozice `10...11`: Maximální rok/měsíc (`min_ym`) v tomto souboru
  * Pozice `12...15`: Pozice "tabulky parseru" v souboru, vynásobená 64, obvykle `1`, protože tabulka parseru je uložena přímo za záhlavím.


### Tabulka parseru časových pásem

Tabulka _parser table_ je vyhledávací tabulka používaná pro převod místního data/času na UTC.

<img src="../date-time-ptable.jpg" alt="Organisation of the parser table" style="width: 461px;" />

Tabulka je uspořádána do řádků/let a sloupců/měsíců.
Buňka je široká 4 bajty, řádek je pak dlouhý 64 bajtů.

Prvních 12 buněk jsou "primární buňky parseru" (ve světle modré barvě), jejich počet odráží číslo měsíce (1...12).
Zbývající 4 buňky jsou "další buňky parseru", číslo `nX` je index.

### Primární buňka parseru

Pozice buňky pro dané datum/čas se vypočítá jako `pos = (ym - min_ym) &lt;&lt; 5`, což znamená, že pro lokalizaci buňky se použije rok a měsíc minus minimální hodnota roku&amp;měsíce pro tabulku.

Struktura buňky:
  * `16` bitů: rozsah, 16bitů, `dhm`
  * `3` bity: `next`
  * `7` bitů: hodinový posun od UTC
  * `6` bitů: minutový posun od UTC

`dhm` označuje den, hodinu a minutu v roce/měsíci, kdy dochází ke změně času (např. začátek/konec letního času).
Pro typický měsíc - kdy není pozorována žádná změna času - představuje hodnota `dhm` maximum v daném měsíci.

Pokud je `dhm` pro vstupní datum/čas matematicky nižší než `dhm` z primární buňky, pak se informace `hodina` a `minuta` použijí k úpravě data/času z místního na UTC.

Pokud je `dhm` větší, pak `next` obsahuje číslo "další buňky parseru"; nachází se na konci příslušného řádku tabulky parseru.


### Další buňka parseru

Buňka "parser next" obsahuje "pokračování" informace pro měsíc, ve kterém je pozorována změna času.
"Pokračování" znamená posun od UTC, ke kterému dojde, když místní čas překročí hranici změny času.

Struktura buňky:
  * `16` bitů: rozsah, 16bitů, `dhm`
  * `3` bity: nepoužívají se, nastaví se na 0
  * `7` bitů: hodinový posun od UTC
  * `6` bitů: minutový posun od UTC


`dhm` označuje den, hodinu a minutu v roce/měsíci, kdy je pozorována DALŠÍ změna času (např. začátek/konec letního času).
Protože v současné době podporujeme pouze jednu změnu času v měsíci, je toto pole nastaveno na maximální hodnotu `dhm` pro daný měsíc.

Informace `hodina` a `minuta` slouží k úpravě data/času z místního na UTC.

_Poznámka: v současné době je podporována pouze jedna změna času v měsíci, což se zdá být plně dostačující pro všechny informace v databázi časových zón IANA._

Prázdné/nepoužité další buňky jsou vynulovány.


## Chyby

Pokud je nastaven bit 63 `datetime`, pak hodnota data/času představuje chybu.
Výraz, který tuto hodnotu vytvořil, pravděpodobně nějakým způsobem selhal.

Kód chyby je uložen v dolních 32 bitech.

