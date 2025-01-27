---
git_commit_hash: b55fa3f
title: Schéma
---

# Schéma

Schémata v SP-Langu popisují typ a další vlastnosti polí v dynamicky typovaných kontejnerech, jako je JSON nebo pythonovské slovníky.

Je důležité poskytnout SP-Langu informace o typu, protože se používají jako vstup pro typovou inferenci, a tedy pro optimální výkon.


## Definice schématu

Reprezentace schématu ve formátu YAML:

```yaml
---
define:
  type: splang/schema

fields:
  field1:
    type: str
    aliases: ["FieldOne"]
  
  field2:
    type: ui64
```


## Možnosti

### Možnost `type`

Definuje datový typ daného atributu, například `str`, `si64` a podobně.
Další informace naleznete v [typovém systému](../types.md) SP-Langu.

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
  type: splang/schema

fields:
  field1:
    type: str

  field2:
    type: ui64
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
