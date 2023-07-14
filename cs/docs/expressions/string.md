---
git_commit_hash: b55fa3f
title: Řetězce
---

# Výrazy pro řetězce


---

## `!IN`: Testuje, zda řetězec obsahuje podřetězec 

Výraz `!IN` slouží ke kontrole, zda řetězec `what` je podřetězcem `where`, nebo ne.

Typ: _Mapping_.

Synopsis:

```yaml
!IN
what: <...>
where: <...>
```

Pokud najde podřetězec `what` v řetězci `where`, vyhodnotí se jako `true`, v opačném případě jako `false`.


!!! example "Příklad"

    ```yaml
    !IN
    what: "Willy"
    kde: "John Willy Boo"
    ```

    Zkontroluje přítomnost podřetězce "Willy" v hodnotě `where`. Vrátí hodnotu `true`.


### Varianta pro více řetězců

Existuje speciální varianta operátoru `!IN` pro kontrolu, zda je některý z řetězců uvedených v hodnotě `what` (v tomto případě seznam) v řetězci. Jedná se o efektivní, optimalizovanou implementaci víceřetězcového matcheru.

```yaml
!IN
what:
  - "John"
  - "Boo"
  - "ly"
where: "John Willy Boo"
```

Jedná se o velmi efektivní způsob kontroly, zda je v řetězci `where` přítomen alespoň jeden podřetězec.
Podporuje [Incremental String Matching](http://se.ethz.ch/~meyer/publications/string/string_matching.pdf) algoritmus pro rychlé porovnávání vzorů v řetězcích.
Díky tomu je ideálním nástrojem pro komplexní filtrování jako samostatný bit nebo jako optimalizační technika.

!!! example "Příklad optimalizace `!REGEX` pomocí víceřetězcového `!IN`:"

    ```yaml
        !AND
        - !IN
          where: !ARG message
          what:
          - "msgbox"
          - "showmod"
          - "showhelp"
          - "prompt"
          - "write"
          - "test"
          - "mail.com"
        - !REGEX
          what: !ARG message
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

## `!STARTSWITH`: Otestuje, zda řetězec začíná předponou 

Vrací hodnotu `true`, pokud řetězec `what` začíná předponou `prefix`.

Typ:  _Mapping_

Synopsis:

```yaml
!STARTSWITH
what: <...>
prefix: <...>
```


!!! example "Příklad"

    ```yaml
    !STARTSWITH
    what: "FooBar"
    prefix: "Foo"
    ```

### Víceřetězcová varianta


!!! warning "Work in progress"

	Zatím neimplementováno.


```yaml
!STARTSWITH
what: <...>
prefix: [<prefix1>, <prefix2>, ...]
```

Ve víceřetězcové variantě je definován seznam řetězců.
Výraz se vyhodnotí jako `true`, pokud alespoň jeden prefixový řetězec odpovídá začátku řetězce `what`.


---

## `!ENDSWITH`: Testuje, zda řetězec končí příponou

Vrací hodnotu `true`, pokud řetězec `what` končí příponou `postfix`.

Typ: _Mapping_

Synopsis:

```yaml
!ENDSWITH
what: <...>
postfix: <...>
```


!!! example "Příklad"

    ```yaml
    !ENDSWITH
    what: "autoexec.bat"
    postfix: "bat"
    ```

### Víceřetězcová varianta


!!! warning "Work in progress"

	Zatím neimplementováno.


```yaml
!ENDSWITH
what: <...>
postfix: [<postfix1>, <postfix2>, ...]
```

Ve víceřetězcové variantě je definován seznam řetězců.
Výraz se vyhodnotí jako `true`, pokud alespoň jeden postfixový řetězec odpovídá konci řetězce `what`.


---

## `!SUBSTRING`: Extrahuje část řetězce 

Vrátí část řetězce `what` mezi indexy `from` a `to`.

Typ: _Mapping_


Synopsis:

```yaml
!SUBSTRING
what: <...>
od: <...>
do: <...>
```

!!! info

    První znak řetězce se nachází na pozici `from=0`.


!!! example "Příklad"

    ```yaml
    !SUBSTRING
    what: "FooBar"
    from: 1
    do: 3
    ```

    Vrací `oo`.

---

## `!LOWER`: Převede řetězec na malá písmena 

Typ: _Mapping_


Synopsis:

```yaml
!LOWER
what: <...>
```


!!! example "Příklad"

    ```yaml
    !LOWER
    what: "FooBar"
    ```

    Vrací `foobar`.


---

## `!UPPER`: Převede řetězec na velká písmena 

Typ: _Mapping_

Synopsis:

```yaml
!UPPER
what: <...>
```


!!! example "Příklad"

    ```yaml
    !UPPER
    what: "FooBar"
    ```

    Vrací `FOOBAR`.

---

## `!CUT`: Vyjmout část řetězce 

Rozdělí řetězec oddělovačem a vrátí část identifikovanou indexem `field` (začíná 0).

Typ: _Mapping_

Synopsis:

```yaml
!CUT
what: <string>
delimiter: <string>
field: <int>
```

Řetězec argumentu `value` bude rozdělen pomocí argumentu `delimiter`.
Argument `field` určuje počet rozdělených řetězců, které se mají vrátit, počínaje 0.  
Pokud je uveden záporný údaj `field`, pak se pole bere od konce řetězce, například -2 znamená předposlední podřetězec.


!!! example "Příklad"

    ```yaml
    !CUT
    what: "Apple,Orange,Melon,Citrus,Pear"
    delimiter: ","
    field: 2
    ```

    Vrátí hodnotu "Melon".

!!! example "Příklad"

    ```yaml
    !CUT
    what: "Apple,Orange,Melon,Citrus,Pear"
    delimiter: ","
    field: -2
    ```

    Vrátí hodnotu "Citrus".

  
---

## `!SPLIT`: Rozdělí řetězec do seznamu 

Rozdělí řetězec na seznam řetězců.

Typ: _Mapping_

Synopsis:

```yaml
!SPLIT
what: <string>
oddělovač: <string>
maxsplit: <number>
```

Řetězec argumentu `what` bude rozdělen pomocí argumentu `delimiter`.
Nepovinný argument `maxsplit` určuje, kolik rozdělení se má provést.


!!! example "Příklad"

    ```yaml
    !SPLIT
    what: "hello,world"
    delimiter: ","
    ```

    Výsledkem je seznam: `["hello", "world"]`.

---

## `!RSPLIT`: Rozdělí řetězec do seznamu zprava

Rozdělí řetězec zprava (od konce řetězce) do seznamu řetězců.

Type: _Mapping_

Synopsis:

```yaml
!RSPLIT
what: <string>
delimiter: <string>
maxsplit: <number>
```

Argument `what` se rozdělí podle `delimeter`. Nepovinný argument `maxsplit` určuje, kolik rozdělení se má provést.

---

## `!JOIN`: Spojí seznam řetězců 

Typ: _Mapping_

Synopsis:

```yaml
!JOIN
items:
  - <...>
  - <...>
delimiter: <string>
miss: ''
```

Výchozí `delimiter` je mezera (" ").

Pokud je položka `None`, použije se hodnota parametru `miss`, ve výchozím nastavení je to prázdný řetězec.
Pokud je `miss` `None` a některá z položek `items` je `None`, výsledkem celého spojení je `None`.

!!! example "Příklad"

    ```yaml
    !JOIN
    items:
      - "Foo"
      - "Bar"
    delimiter: ','
    ```
