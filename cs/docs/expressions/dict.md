---
git_commit_hash: b55fa3f
title: Slovník
---

# Slovníkový výraz


Dict (neboli slovník) uchovává kolekci dvojic (klíč, hodnota) tak, že každý možný klíč se v kolekci vyskytuje nejvýše jednou.
Klíče ve slovníku musí být stejného typu, stejně jako hodnoty.
Množina je jednou ze základních datových struktur poskytovaných jazykem SP-Lang.

Položka je dvojice (klíč, hodnota) reprezentovaná jako tuple.

Tip: Tuto strukturu můžete znát pod alternativními názvy "asociativní pole" nebo "mapa".

--- 

## `!DICT`: Dictionary 

Typ:  _Mapping_
```yaml

!DICT
s:
 <key1>: <value1>
  <key2>: <value2>
  <key3>: <value3>
  ...
```

!!! hint

	
	
	
	Pro zjištění počtu položek ve slovníku použijte `!COUNT`.
	
	

!!! example

	
	
	
	V jazyce SP-Lang lze slovník zadat několika způsoby:
	```yaml
	
	!DICT
	s:
	  klíč1: "One"
	  key2: "Two"
	  key3: "Three"
	```
	
	Implicitní slovník:
	```yaml
	
	---
	key1: "One"
	key2: "Two"
	key3: "Three"
	```
	
	Konzistentní slovník používající `!!dict` a styl toku YAML:
	```yaml
	
	!!dict {key1: "Jedna", key2: "Dvě", key3: "Tři"}
	```
	

### Specifikace typu

Typ slovníku se označuje jako `{Tk:Tv}`, kde `Tk` je typ klíče a `Tv` je typ hodnoty.
Další informace o typu slovníku naleznete v příslušné kapitole v [typovém systému](../jazyk/typy#slovníku).

Slovník se pokusí odvodit svůj typ na základě přidaných položek.
Typ první položky pravděpodobně poskytne typ klíče `Tk` a typ hodnoty `Tv`.
Pokud je slovník prázdný, jeho odvozený typ je `{str:si64}`.

Toto můžete přepsat pomocí explicitní specifikace typu:
```yaml

!DICT
typ: "{str:any}"
with:
 <key1>: <value1>
  <key2>: <value2>
  <key3>: <value3>
  ...
```

`type` je nepovinný argument obsahující řetězec se signaturou slovníku.
Tato signatura bude použita pro tuto signaturu namísto odvození typu z childs.

Ve výše uvedeném příkladu je typ slovníku `{str:any}`, typ klíče je `str` a typ hodnot je `any`.


--- 

## `!GET`: Získat hodnotu ze slovníku 

Typ: _Mapping_.

```yaml

!GET
co: <key>
z: <dict>
výchozí: <value>
```

Získat položku ze slovníku `dict` (slovník) identifikovaného pomocí `key`.

Pokud `klíč` není nalezen, vrátí `default` nebo chybu, pokud `default` není zadán.
`default` je nepovinné.


!!! example

	
	
	```yaml
	
	!GET
	co: 3
	od:
	  !DICT
	  s:
	    1: "One"
	    2: "Two"
	    3: "Three"
	```
	
	Vrací `Three`.
	

--- 

## `!IN`: Test členství 

Typ: _Mapping_.
```yaml

!IN
co: <key>
kde: <dict>
```

Zkontrolujte, zda je `key` přítomen v `dict`.

Poznámka: Výraz `!IN` je popsán v kapitole "Testy".


!!! example

	
	
	```yaml
	!IN
	co: 3
	kde:
	  !DICT
	  s:
	    1: "One"
	    2: "Two"
	    3: "Three"
	```

