---
git_commit_hash: b55fa3f
title: Řetězcové
---

# Řetězcové výrazy


---

## `!IN`: Test, zda řetězec obsahuje podřetězec 

Výraz `!IN` slouží ke kontrole, zda řetězec `what` existuje v řetězci `where`, nebo ne.

Typ: Typ: _Mapování_.

Synopsis:
```yaml

!IN
what: <...>
kde: <...>
```

V opačném případě se vyhodnotí jako `true`, pokud najde podřetězec `what` v řetězci `where`, a false.


### Příklad
```yaml

!IN
what: "Willy"
kde: "John Willy Boo"
```

Zkontroluje přítomnost podřetězce "Willy" v hodnotě `where`. Vrací hodnotu `true`.


### Víceřetězcová varianta

Existuje speciální varianta operátoru `!IN` pro kontrolu, zda je některý z řetězců uvedených v hodnotě `what` (v tomto případě seznam) v řetězci. Jedná se o efektivní, optimalizovanou implementaci víceřetězcového matcheru.
```yaml

!IN
what:
  - "John"
  - "Boo"
  - "ly"
kde: "John Willy Boo"
```

Jedná se o velmi efektivní způsob kontroly, zda je v řetězci `where` přítomen alespoň jeden podřetězec.
Poskytuje [Incremental String Matching](http://se.ethz.ch/~meyer/publications/string/string_matching.pdf) algoritmus pro rychlé porovnávání vzorů v řetězcích.
Díky tomu je ideálním nástrojem pro komplexní filtrování jako samostatný bit nebo jako optimalizační technika.

Příklad optimalizace `!REGEX` pomocí víceřetězcového `!IN`:
```yaml

!AND
- !IN
  kde: !ARG zpráva
  what:
  - "msgbox"
  - "showmod"
  - "showhelp"
  - "prompt"
  - "write"
  - "test"
  - "mail.com"
- !REGEX
  what: !ARG zpráva
  regex: "(msgbox|showmod(?:al|eless)dialog|showhelp|prompt|write)|(test[0-9])|([a-z]@mail\.com)
```

Tento přístup se doporučuje z aplikací v proudech, kde je třeba filtrovat rozsáhlé množství dat s předpokladem, že pouze menší část dat odpovídá vzorům.
Přímá aplikace výrazu `!REGEX` výrazně zpomalí zpracování, protože se jedná o složitý regulární výraz.
Jde o to "předfiltrovat" data jednodušší, ale rychlejší podmínkou tak, aby se k drahému `!REGEX` dostal jen zlomek dat.
Typické zlepšení výkonu je 5x-10x.

Z tohoto důvodu musí být `!IN` dokonalou nadmnožinou `!REGEX`, to znamená:

* `!IN` -&gt; `true`, `!REGEX` -&gt; `true`: `true`
* `!IN` -&gt; `true`, `!REGEX` -&gt; `false`: `false` (to by měla být menšina případů).
* `!IN` -&gt; `false`, `!REGEX` -&gt; `false`: `false` (předfiltrování, mělo by se jednat o většinu případů)
* `!IN` -&gt; `false`, `!REGEX` -&gt; `true`: této kombinaci se MUSÍTE vyhnout, podle toho přijměte `!IN` a/nebo `!REGEX`.

---

## `!STARTSWITH`: Otestujte, zda řetězec začíná předponou 

Vrací hodnotu `true`, pokud řetězec `what` začíná předponou `prefix`.

Typ: _Mapování_

Synopsis:
```yaml

!STARTSWITH
what: <...>
prefix: <...>
```


### Příklad
```yaml

!STARTSWITH
what: "FooBar"
prefix: "Foo"
```

### Víceřetězcová varianta


!!! warning "Probíhající práce"

	
	
	Zatím neimplementováno.
	
	
```yaml

!STARTSWITH
what: <...>
prefix: ]: [<prefix1>, <prefix2>, ...]
```

Ve víceřetězcové variantě je definován seznam řetězců.
Výraz se vyhodnotí jako `pravdivý`, pokud alespoň jeden prefixový řetězec odpovídá začátku řetězce `co`.


---

## `!ENDSWITH`: Testuje, zda řetězec končí postfixem 

Vrací hodnotu `true`, pokud řetězec `what` končí znakem `postfix`.

Typ: _Mapování_


Synopsis:
```yaml

!ENDSWITH
what: <...>
postfix: <...>
```


### Příklad
```yaml

!ENDSWITH
what: "autoexec.bat"
postfix: "bat"
```

### Víceřetězcová varianta


!!! warning "Probíhající práce"

	
	
	Zatím neimplementováno.
	
	
```yaml

!ENDSWITH
what: <...>
postfix: [<postfix1>, <postfix2>, ...]
```

Ve víceřetězcové variantě je definován seznam řetězců.
Výraz se vyhodnotí jako `true`, pokud alespoň jeden postfixový řetězec odpovídá konci řetězce `what`.


---

## `!SUBSTRING`: Výpis části řetězce 

Vrátí část řetězce `what` mezi indexy `from` a `to`.

Typ: Typ: _Mapování_


Synopsis:
```yaml

!SUBSTRING
what: <...>
od: <...>
do: <...>
```

!!! info

	
	
	
	První znak řetězce se nachází na pozici `from=0`.
	
	

### Příklad
```yaml

!SUBSTRING
what: "FooBar"
from: 1
do: 3
```

Vrací `oo`.

---

## `!LOWER`: Převede řetězec na malá písmena 

Typ: _Mapování_


Synopsis:
```yaml

!LOWER
what: <...>
```


### Příklad
```yaml

!LOWER
what: "FooBar"
```

Vrací `foobar`.


---

## `!UPPER`: Transformovat řetězec na velká písmena 

Typ: _Mapování_

Synopsis:
```yaml

!UPPER
what: <...>
```


### Příklad
```yaml

!UPPER
what: "FooBar"
```

Vrací `FOOBAR`.

---

## `!CUT`: Vyjmout část řetězce 

Rozřízne řetězec oddělovačem a vrátí část identifikovanou indexem `pole` (začíná 0).

Typ: _Mapování_

Synopsis:
```yaml

!CUT
what: <string>
oddělovač: <string>
pole: <int>
```

Řetězec argumentu `hodnota` bude rozdělen pomocí argumentu `oddělovač`.
Argument `pole` určuje počet rozdělených řetězců, které se mají vrátit, počínaje 0.  
Pokud je uveden záporný údaj `pole`, pak se pole bere od konce řetězce, například -2 znamená předposlední podřetězec.


### Příklad
```yaml

!CUT
what: "Jablko,Pomeranč,Meloun,Citrus,Hruška"
oddělovač: ","
pole: 2
```

Vrátí hodnotu "Melon".

```yaml

!CUT
what: "Apple,Orange,Melon,Citrus,Pear"
oddělovač: ","
pole: -2
```

Vrátí hodnotu "Citrus".

  
---

## `!SPLIT`: Rozdělí řetězec do seznamu 

Rozdělí řetězec na seznam řetězců.

Typ: _Mapování_

Synopsis:
```yaml

!SPLIT
what: <string>
oddělovač: <string>
maxsplit: <number>
```

Řetězec argumentu `what` bude rozdělen pomocí argumentu `delimiter`.
Nepovinný argument `maxsplit` určuje, kolik rozdělení se má provést.


### Příklad
```yaml

!SPLIT
what: "hello,world"
delimiter: ","
```

Výsledkem je seznam: `["hello", "world"]`.

---

## `!JOIN`: Spojení seznamu řetězců 

Typ: _Mapování_

Synopsis:
```yaml

!JOIN
položek:
  - <...>
  - <...>
delimiter: <string>
miss: ''
```

Výchozím `oddělovačem` je mezera (" ").

Pokud je položka `None`, použije se hodnota parametru `miss`, ve výchozím nastavení je to prázdný řetězec.
Pokud je `miss` `None` a některá z položek `items` je `None`, výsledkem celého spojení je `None`.

### Příklad
```yaml

!JOIN
items:
  - "Foo"
  - "Bar"
oddělovač: ','
```
