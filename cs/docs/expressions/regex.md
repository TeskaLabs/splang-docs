---
git_commit_hash: b55fa3f
title: Regex
---

# Regexové výrazy


!!! tip

    Pomocí [Regexr](https://regexr.com) můžete vytvářet a testovat regulární výrazy.


--- 

## `!REGEX`: Vyhledávání pomocí regulárních výrazů  

Typ: _Mapping_.

Synopsis:

```yaml
!REGEX
what: <string>
regex: <regex>
hit: <hit>
miss: <miss>
```

Projde řetězec `what` a hledá libovolné místo, kde regulární výraz `regex` dává shodu.
Pokud je shoda nalezena, vrátí se `hit`, jinak se vrátí `miss`.
  
Výraz `hit` je nepovinný, výchozí hodnota je `true`.
  
Výraz `miss` je nepovinný, výchozí hodnota je `false`.


!!! example "Příklad"

    ```yaml
    !IF
    test:
      !REGEX
      what: "Hello world!"
      regex: "world"
    then:
      "Yes :-)"
    else:
      "No ;-("
```

!!! example "Jiná forma:"

    ```yaml
    !REGEX
    what: "Hello world!"
    regex: "world"
    hit: "Ano :-)"
    miss: "Ne ;-("
    ```

--- 

## `!REGEX.REPLACE`: Nahrazení regulárním výrazem

Typ: _Mapping_.

Synopsis:

```yaml
!REGEX.REPLACE
what: <string>
regex: <regex>
by: <string>
```

Nahradit regulární výraz `regex` odpovídající hodnotě `what` hodnotou `by`.


!!! example

    ```yaml

    !REGEX.REPLACE
    what: "Hello world!"
    regex: "world"
    by: "Mars"
    ```

    Vrací: `Hello Mars!`

--- 

## `!REGEX.SPLIT`: Rozdělí řetězec pomocí regulárního výrazu  

Typ: _Mapping_.

Synopsis:

```yaml
!REGEX.SPLIT
what: <string>
regex: <regex>
max: <integer>
```

Dělí řetězec `what` regulárním výrazem `regex`.

Nepovinný argument `max` určuje maximální počet rozdělení.


!!! example "Příklad"

    ```yaml
    !REGEX.SPLIT
    what: "07/14/2007 12:34:56"
    regex: "[/ :]"
    ```

    Vrací: `['07', '14', '2007', '12', '34', '56']`

--- 

## `!REGEX.FINDALL`: Najde všechny výskyty podle regulárního výrazu  

Typ: _Mapping_.

Synopsis:

```yaml
!REGEX.FINDALL
what: <string>
regex: <regex>
```

Najde všechny shody `regex` v řetězci `what`.

!!! example "Příklad"

    ```yaml
    !REGEX.FINDALL
    what: "Frodo, Sam, Gandalf, Legolas, Gimli, Aragorn, Boromir, Smíšek, Pipin"
    regex: \w+
    ```

    Vrací: `['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Gimli', 'Aragorn', 'Boromir', 'Smíšek', 'Pipin']`

---

## `!REGEX.PARSE`: Parsování pomocí regulárního výrazu 

Type: _Mapping_.

Viz kapitolu [`!PARSE.REGEX`](../parsec/#parseregex-parsuje-posloupnost-znaku-ktera-odpovida-regularnimu-vyrazu)
