---
title: Řetězce
---

# Výrazy pro řetězce

## Přehled

* [`!IN`](#in): Testuje, zda řetězec obsahuje podřetězec.
* [`!STARTSWITH`](#startswith): Testuje, zda řetězec začíná vybranou předponou.
* [`!ENDSWITH`](#endswith): Testuje, zda řetězec končí vybranou příponou.
* [`!SUBSTRING`](#substring): Extrahuje část řetězce.
* [`!LOWER`](#lower), [`!UPPER`](#upper): Převádí řetězec na malá / velká písmena.
* [`!CUT`](#cut): Vyjme část řetězce a vrátí vybranou část.
* [`!SPLIT`](#split), [`!RSPLIT`](#rsplit): Rozdělí řetězec na seznam.
* [`!JOIN`](#join): Spojí seznam řetězců.

---

## `!IN`

Výraz `!IN` slouží ke kontrole, zda řetězec `what` je podřetězcem `where`, nebo ne.

Typ: _Mapping_.

Synopsis:

```yaml
!IN
what: <...>
where: <...>
```

Pokud najde podřetězec `what` v řetězci `where`, vyhodnotí se jako `true`, v opačném případě jako `false`.


!!! example

    ```yaml
    !IN
    what: "Willy"
    where: "John Willy Boo"
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

* `!IN` -> `true`, `!REGEX` -> `true`: `true`
* `!IN` -> `true`, `!REGEX` -> `false`: `false` (to by měla být menšina případů)
* `!IN` -> `false`, `!REGEX` -> `false`: `false` (předfiltrování, mělo by se jednat o většinu případů)
* `!IN` -> `false`, `!REGEX` -> `true`: této kombinaci se MUSÍTE vyhnout, podle toho přijměte `!IN` a/nebo `!REGEX`.

---

## `!STARTSWITH`

Vrací hodnotu `true`, pokud řetězec `what` začíná předponou `prefix`.

Typ: _Mapping_

Synopsis:

```yaml
!STARTSWITH
what: <...>
prefix: <...>
```


!!! example

    ```yaml
    !STARTSWITH
    what: "FooBar"
    prefix: "Foo"
    ```

### Víceřetězcová varianta

!!! warning "Práce v pokroku"

    Zatím neimplementováno.


```yaml
!STARTSWITH
what: <...>
prefix: [<prefix1>, <prefix2>, ...]
```

Ve víceřetězcové variantě je definován seznam řetězců.
Výraz se vyhodnotí jako `true`, pokud alespoň jeden prefixový řetězec odpovídá začátku řetězce `what`.


---

## `!ENDSWITH`

Vrací hodnotu `true`, pokud řetězec `what` končí příponou `postfix`.

Typ: _Mapping_

Synopsis:

```yaml
!ENDSWITH
what: <...>
postfix: <...>
```


!!! example

    ```yaml
    !ENDSWITH
    what: "autoexec.bat"
    postfix: ".bat"
    ```

### Víceřetězcová varianta

!!! warning "Práce v pokroku"

    Zatím neimplementováno.


```yaml
!ENDSWITH
what: <...>
postfix: [<postfix1>, <postfix2>, ...]
```

Ve víceřetězcové variantě je definován seznam řetězců.
Výraz se vyhodnotí jako `true`, pokud alespoň jeden postfixový řetězec odpovídá konci řetězce `what`.


---

## `!SUBSTRING`

Vrátí část řetězce `what` mezi indexy `from` a `to`.

Typ: _Mapping_

Synopsis:

```yaml
!SUBSTRING
what: <...>
from: <...>
to: <...>
```

!!! info

    První znak řetězce se nachází na pozici `from=0`.


!!! example

    ```yaml
    !SUBSTRING
    what: "FooBar"
    from: 1
    to: 3
    ```

    Vrací `oo`.

---

## `!LOWER`

Převede řetězec nebo seznam řetězců na malá písmena.

Typ: _Mapping_

Synopsis:

```yaml
!LOWER
what: <...>
```


!!! example

    ```yaml
    !LOWER
    what: "FooBar"
    ```

    Vrací `foobar`.


!!! example

    ```yaml
    !LOWER
    what: ["FooBar", "Baz"]
    ```

    Vrací seznam hodnot `["foobar", "baz"]`.

---

## `!UPPER`

Typ: _Mapping_

Synopsis:

```yaml
!UPPER
what: <...>
```


!!! example

    ```yaml
    !UPPER
    what: "FooBar"
    ```

    Vrací `FOOBAR`.

---

## `!CUT`

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


!!! example

    ```yaml
    !CUT
    what: "Apple,Orange,Melon,Citrus,Pear"
    delimiter: ","
    field: 2
    ```

    Vrátí hodnotu "Melon".

!!! example

    ```yaml
    !CUT
    what: "Apple,Orange,Melon,Citrus,Pear"
    delimiter: ","
    field: -2
    ```

    Vrátí hodnotu "Citrus".

  
---

## `!SPLIT`

Rozdělí řetězec na seznam řetězců.

Typ: _Mapping_

Synopsis:

```yaml
!SPLIT
what: <string>
delimiter: <string>
maxsplit: <number>
```

Řetězec argumentu `what` bude rozdělen pomocí argumentu `delimiter`.
Nepovinný argument `maxsplit` určuje, kolik rozdělení se má provést.


!!! example

    ```yaml
    !SPLIT
    what: "hello,world"
    delimiter: ","
    ```

    Výsledkem je seznam: `["hello", "world"]`.

---

## `!RSPLIT`

Rozdělí řetězec zprava (od konce řetězce) do seznamu řetězců.

Typ: _Mapping_

Synopsis:

```yaml
!RSPLIT
what: <string>
delimiter: <string>
maxsplit: <number>
```

Řetězec argumentu `what` bude rozdělen pomocí argumentu `delimiter`.
Nepovinný argument `maxsplit` určuje, kolik rozdělení se má provést.


---

## `!JOIN`

Typ: _Mapping_

Synopsis:

```yaml
!JOIN
items:
  - <...>
  - <...>
delimiter: <string>
miss: ""
```

Výchozí `delimiter` je mezera (" ").

Pokud je položka `None`, použije se hodnota parametru `miss`, ve výchozím nastavení je to prázdný řetězec.
Pokud je `miss` `None` a některá z položek `items` je `None`, výsledkem celého spojení je `None`.

!!! example

    ```yaml
    !JOIN
    items:
      - "Foo"
      - "Bar"
    delimiter: ","
    ```