---
git_commit_hash: b55fa3f
title: Regex
---

# Regexové výrazy


!!! tip

	
	
	
	Pomocí [Regexr](https://regexr.com) můžete vytvářet a testovat regulární výrazy.
	

--- 

## `!REGEX`: Vyhledávání pomocí regulárních výrazů  

Typ: Typ: _Mapování_.

### Synopse
```yaml

!REGEX
co: <string>
regex: <regex>
trefa: <hit>
REGEX: chybí: <miss>
```

Projde řetězec `what` a hledá libovolné místo, kde regulární výraz `regex` dává shodu.
Pokud je shoda nalezena, vrátí se `hit`, jinak se vrátí `miss`.
  
Výraz `hit` je nepovinný, výchozí hodnota je `true`.
  
Výraz `miss` je nepovinný, výchozí hodnota je `false`.


### Příklad
```yaml

!IF
test:
  !REGEX
  what: "Hello world!"
  regex: "world"
then:
  "Ano :-)"
else:
  "Ne ;-("
```

Výše uvedený příklad lze zapsat také jako:
 ```yaml

!REGEX
co: "Hello world!"
regex: "world"
hit: "Ano :-)"
miss: "Ne ;-("
```

--- 

## `!REGEX.REPLACE`: Regulární výraz nahradit  

Typ: Typ: _Mapování_.

### Synopse
```yaml

!REGEX.REPLACE
co: <string>
regex: <regex>
by: <string>
```

Nahradit regulární výraz `regex` odpovídající hodnotě `what` hodnotou `by`.


### Příklad
```yaml

!REGEX.REPLACE
co: "Hello world!"
regex: "world"
by: "Mars"
```

Vrací: `Hello Mars!`

--- 

## `!REGEX.SPLIT`: Rozdělí řetězec pomocí regulárního výrazu  

Typ: Typ: _Mapování_.

### Synopse
```yaml

!REGEX.SPLIT
co: <string>
regex: <regex>
max: <integer>
```

Dělí řetězec `what` regulárním výrazem `regex`.

Nepovinný argument `max` určuje maximální počet rozdělení.


### Příklad
```yaml

!REGEX.SPLIT
co: "07/14/2007 12:34:56"
regex: "[/ :]"
```

Vrací: `['07', '14', '2007', '12', '34', '56']`

--- 

## `!REGEX.FINDALL`: Najde všechny výskyty podle regulárního výrazu  

Typ: Typ: _Mapování_.

### Synopse
```yaml

!REGEX.FINDALL
co: <string>
regex: <regex>
```

Najít všechny shody `regex` v řetězci `what`.

### Příklad
```yaml

!REGEX.FINDALL
co: "Frodo, Sam, Gandalf, Legolas, Gimli, Aragorn, Boromir, Smíšek, Pipin"
regex: \w+
```

Vrací: `['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Gimli', 'Aragorn', 'Boromir', 'Merry', 'Pippin']`

---

## `!REGEX.PARSE`: Parsování pomocí regulárního výrazu 

Typ: _Mapování_.

