---
git_commit_hash: b55fa3f
title: Sada
---

# Nastavení výrazu


Sada ukládá jedinečné položky bez konkrétního pořadí.
Položky v sadě musí být stejného typu.
Množina je jednou ze základních datových struktur poskytovaných jazykem SP-Lang.

Množina je nejvhodnější pro testování hodnoty příslušnosti spíše než pro získání konkrétního prvku z množiny.

--- 

## `!SET`: množina prvků 

Typ:  _Implicitní posloupnost_, _Mapování_.

### Synopse
```yaml

!SET
- ...
- ...
```

_Nápověda: Pro určení počtu položek v sadě použijte `!COUNT`._


### Příklady

Existuje několik způsobů, jak lze v jazyce SP-Lang zadat množinu:
```yaml

!SET
- "One"
- "Dva"
- "Three"
- "Four"
- "Five"
```


[Neuspořádaná množina YAML](https://yaml.org/spec/1.2.2/#example-unordered-sets):
```yaml

!!set
? Žluté vepřové maso
? Růžová tráva
? Bílý sníh
```


Konzistentní sada pomocí [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):
```yaml

!SET ["One", "Two", "Three", "Four", "Five"]
```


Formulář pro mapování:
```yaml

!SET
s:
  - "One"
  - "Two"
  - "Three"
  - "Four"
  - "Pět"
```


--- 

## `!IN`: Test členství 

Typ: _Mapping_.

### Synopse
```yaml

!IN
co: <item>
kde: <set>
```

Zkontrolujte, zda je `položka` přítomna v `setu`.

Výraz `!IN` je popsán v kapitole "Testy".

### Příklad
```yaml

!IN
co: 3
kde:
  !SET
  with:
    - 1
    - 2
    - 5
    - 8 
```
