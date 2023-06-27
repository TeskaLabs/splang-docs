---
git_commit_hash: b55fa3f
title: Seznamy
---

# Seznam výrazů


Seznam je jednou ze základních datových struktur, které SP-Lang nabízí.
Seznam obsahuje konečný počet uspořádaných položek, přičemž stejná položka se může vyskytovat vícekrát.
Položky v seznamu musí být stejného typu.

!!! note

	
	
	
	Seznam se někdy nepřesně nazývá také _pole_.
	
	

--- 

## `!LIST`: Seznam položek 

Typ:  _Implicitní posloupnost_, _Mapování_.

### Synopse
```yaml

!LIST
- ...
- ...
```

_Nápověda: Pro určení počtu položek v seznamu použijte `!COUNT`._


### Příklady

Existuje několik způsobů, jak lze v jazyce SP-Lang zadat seznam:
```yaml

!LIST
- "One"
- "Dva"
- "Three"
- "Four"
- "Five"
```


Implicitní seznam pomocí [sekvencí bloků YAML](https://yaml.org/spec/1.2.2/#821-block-sequences):
```yaml

- "One"
- "Dva"
- "Tři"
- "Čtyři"
- "Pět"
```


Implicitní seznam pomocí [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):
```yaml

["Jedna", "Dvě", "Tři", "Čtyři", "Pět"]
```


Formulář mapování:
```yaml

!LIST
s:
  - "One"
  - "Two"
  - "Three"
  - "Four"
  - "Pět"
```

--- 

## `!GET`: Získat položku ze seznamu 

Typ: _Mapping_.


### Synopse
```yaml

!GET
co: <index of the item in the list>
z: <list>
```

`index` je celé číslo (číslo).

`index` může být záporný, v tom případě určuje položku od konce seznamu.
Položky jsou indexovány od 0, to znamená, že první položka v seznamu má index 0.

Pokud je `index` mimo hranice seznamu, příkaz se vrátí s chybou.


### Příklady
```yaml

!GET
co: 3
from:
  !LIST
  - 1
  - 5
  - 30
  - 50
  - 80
  - 120
```

Vrací hodnotu `50`.

```yaml

!GET
what: -1
od:
  !LIST
  - 1
  - 5
  - 30
  - 50
  - 80
  - 120
```

Vrátí poslední položku seznamu, která je `120`.

