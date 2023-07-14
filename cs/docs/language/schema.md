---
git_commit_hash: b55fa3f
title: Schéma
---

# Schéma

Schémata v SP-Langu popisují typ a další vlastnosti polí v dynamicky typovaných kontejnerech, jako jsou JSON nebo slovníky Pythonu.

Je důležité poskytnout SP-Langu informace o typu, protože se používají jako vstup pro typovou inferenci, a tedy optimální výkon.


## Definice schématu

Reprezentace schématu ve formátu YAML:
```yaml

---
define:
  typ: splang/schema

pole:
  field1:
    typ: str
    aliasy: field:: pole1: ["FieldOne"]
  
  field2:
    typ: ui64
```


## Options

### Možnost `type`

Definuje datový typ daného atributu, například `str`, `si64` a podobně.
Další informace naleznete v SP-Lang [type system](types).

Tato volba je povinná.


### Možnost `aliases`

Definuje aliasy polí pro daný atribut, které lze použít v deklaraci jako synonymní výraz.

Pokud má pole `field1` alias pole s názvem `FieldOne`, jsou následující deklarace rovny, pokud je schéma správně definováno:
```yaml

!GET
what: field1
from: !ARG input
```
```yaml

!GET
what: FieldOne
from: !ARG input
```

### Možnost `unit`

Definuje jednotku atributu, pokud je potřeba, například pro časové značky. V tomto případě může být jednotka `auto` pro automatickou detekci, `sekundy` a `mikrosekundy`.


## Deklarace funkce (Python)

Příklad deklarace funkce SP-Lang, která používá `MYSCHEMA.yaml`:
```python

splang.FunctionDeclaration(
	name="main",
	returns="bool",
	arguments={
		'myArgument': 'json<MYSCHEMA>'
	},
)
```

a samotný soubor `MYSCHEMA.yaml`:
```yaml

---
define:
  typ: splang/schema

pole:
  field1:
    typ: str

  field2:
    typ: ui64
```

### In-place schémata

SP-Lang umožňuje specifikovat schéma přímo v kódu `FunctionDeclaration` jazyka Python:
```python

splang.FunctionDeclaration(
	name="main",
	returns="bool",
	arguments={
		'myArgument': 'json<INPLACESCHEMA>'
	},
	schemas=[
		("INPLACESCHEMA", {
			"field1": "str",
			"field2": "si32",
			"field3": "ui64",
		})
	]
)
```

Provádí se pomocí `tuple`, první položka je název schématu, druhá je slovník s poli.
