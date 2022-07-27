---
layout: default
title: SP-Lang Documentation
---

# Schema

Schemas in SP-Lang describe the type and other properties of fields in dynamically types containers such as JSON or Python dictionaries.

It is important to provide information about the type to the SP-Lang because it is used as an input for a type inference and hence optimal performance.


## Schema definition

YAML representation of the schema:

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


## Options

### Option `type`

Defines the data type for the given attribute, such as `str`, `si64` and so on.
Refer to a SP-Lang [type system](type-system) for more information.

This option is mandatory.


### Option `aliases`

Defines field aliases for the given attribute, that can be used in the declaration as a synonymic term.

If an `field1` has a field alias named `FieldOne`, the following declarations are equal if the schema is properly defined:

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

### Option `unit`

Defines the unit of the attribute, if needed, such as for timestamps. In this case, the unit can be `auto` for automatical detection, `seconds` and `microseconds`.


## Function declaration (Python)

The example of the SP-Lang function declaration that uses `MYSCHEMA.yaml`:

```python
splang.FunctionDeclaration(
	name="main",
	returns="bool",
	arguments={
		'myArgument': 'json<MYSCHEMA>'
	},
)
```

and `MYSCHEMA.yaml` itself:

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

### In-place schemas

SP-Lang allows to specify schema directly in the `FunctionDeclaration` Python code:

```python
splang.FunctionDeclaration(
	name="main",
	returns="bool",
	arguments={
		'myArgument': 'json<INPLACESCHEMA>'
	},
	schemas=[
		('INPLACESCHEMA', {
			"field1": "str",
			"field2": "si32",
			"field3": "ui64",
		})
	]
)
```

It is done by using `tuple`, the first item is a schema name, the second is a dictionary with fields.
