---
git_commit_hash: b55fa3f
title: Kontrolní
---

# Kontrolní výrazy


SP-Lang nabízí celou řadu řídicích výrazů. 

--- 

## `!IF`: Jednoduché podmíněné větvení  

Typ: _Mapování_.


Výraz `!IF` je rozhodovací výraz, který vede vyhodnocení k rozhodování na základě zadaného testu.
```yaml

!IF
test: <expression>
pak: <expression>
else: <expression>
```


Na základě této hodnoty se vyhodnotí větev `then` (pro `true`) nebo `else` (pro `false`).

`then` a `else` musí vracet stejný typ, který bude zároveň typem návratové hodnoty `!IF`.



!!! example

	
	
	```yaml
	!IF
	test:
	  !EQ
	  - !ARG vstup
	  - 2
	pak:
	  To jsou dva.
	else:
	  NENÍ to dva.
	```
	

---

## `!KDYŽ`: Výkonné větvení  

Typ: _Sequence_.

Výraz `!KDYŽ` je podstatně silnější než výraz `!IF`.
Případy mohou odpovídat mnoha různým vzorům, včetně intervalových shod, tuplů atd. 

```yaml

!WHEN
- test: <expression>
  pak: <expression>

- test: <expression>
  pak: <expression>

- test: <expression>
  pak: <expression>

- ...

- else: <expression>
```


Pokud není zadáno `else`, pak `WHEN` vrací `False`.


!!! example

	
	
	
	Příklad použití `!KDYŽ` pro přesnou shodu, shodu rozsahu a nastavenou shodu:
	```yaml
	
	!KDYŽ
	
	# Přesná shoda hodnot
	- test:
	    !EQ
	    - !ARG klíč
	    - 34
	  pak:
	    "Třicet čtyři"
	
	# Shoda rozsahu
	- test:
	    !LT
	    - 40
	    - !ARG klíč
	    - 50
	  pak:
	    "čtyřicet až padesát (výhradně)"
	
	# In-set match
	- test:
	    !IN
	    co: !ARG klíč
	    kde:
	      - 75
	      - 77
	      - 79
	  then:
	    "sedmdesát pět, sedm, devět"
	
	
	- else:
	    "Neznámý"
	```
	

--- 

## `!MATCH`: Porovnávání vzorů 

Typ: _Mapping_.

```yaml

!MATCH
co: <what-expression>
s:
 <value>: <expression>
  <value>: <expression>
  ...
else:
 <expression>
```

Výraz `!MATCH` vyhodnotí výraz `what-expression`, přiřadí hodnotu výrazu k klauzuli case a provede výraz `expression` spojený s tímto případem.

Větev `else` výrazu `!MATCH` je nepovinná.
Výraz selže s chybou, pokud není nalezena žádná odpovídající `<value>` a větev `else` chybí.



!!! example

	
	
	```yaml
	!MATCH
	co: 1
	s:
	  1: "One"
	  2: "Two"
	  3: "Three"
	else:
	  "Jiné číslo"
	```
	
	


!!! hint "Použití `!MATCH` pro strukturování kódu"

	
	
	```yaml
	!MATCH
	co: !ARG kód
	s:
	  1: !INCLUDE code-1.yaml
	  2: !INCLUDE code-2.yaml
	else:
	  !INCLUDE code-else.yaml
	```

  
---

## `!TRY`: Provést do prvního bezchybného výrazu  


Typ: _Sequence_
```yaml


!TRY
- <expression>
- <expression>
- <expression>
...
```

Iterujte výrazem (shora dolů), pokud výraz vrátí nenulový výsledek (`None`), zastavte iteraci a vraťte tuto hodnotu.
V opačném případě pokračujte na další výraz.

Při dosažení konce seznamu vrátí `None` (chyba).


Poznámka: Zastaralý název tohoto výrazu byl `!FIRST`.
Byl zastaralý v listopadu 2022.
    
---

## `!MAP`: Použít výraz na každý prvek v posloupnosti 

Typ: _Mapování_.
```yaml

!MAP
co: <sequence>
apply: <expression>
```

Výraz `apply` se aplikuje na každý prvek v posloupnosti `what` s argumentem `x` obsahujícím příslušnou hodnotu prvku.
Výsledkem je nový seznam s transformovanými prvky.

!!! example

	
	
	```yaml
	
	!MAPA
	co: [1, 2, 3, 4, 5, 6, 7]
	použít:
	  !ADD [!ARG x, 10]
	```
	
	Výsledek je `[11, 12, 13, 14, 15, 16, 17]`.
	

---

## `!REDUCE`: Redukce prvků seznamu na jedinou hodnotu 

Typ: _Mapování_.

```yaml

!REDUCE
co: <expression>
použít: <expression>
initval: <expression>
fold: <left|right>
```

Výraz `apply` se aplikuje na každý prvek v posloupnosti `what` s argumentem `a` obsahujícím agregaci operace reduce a argumentem 'b' obsahujícím příslušnou hodnotu prvku.

Výraz `initval` poskytuje počáteční hodnotu pro argument `a`.

Nepovinná hodnota `fold` určuje "levé skládání" (`left`, výchozí) nebo "pravé skládání" (`right`).


!!! example

	
	
	```yaml
	
	!REDUKCE
	co: [1, 2, 3, 4, 5, 6, 7]
	initval: -10
	apply:
	  !ADD [!ARG a, !ARG b]
	```
	
	Vypočítá součet posloupnosti s počáteční hodnotou -1.  
	Výsledek je `18` = `-10 + 1 + 2 + 3 + 4 + 5 + 6 + 7`.

