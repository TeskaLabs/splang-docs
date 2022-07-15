---
layout: default
title: SP-Lang Documentation
---

# Schema

Schemas in SP-Lang describe the type and other properties of fields in dynamically types containers such as JSON or Python dictionaries.

It is important to provide information about the type to the SP-Lang because it is used as an input for a type inference and hence optimal performance.


## Schema definition

A schema is represented as a dictionary describing the argument's attributes such as their data type, unit and field alises (different notations in the declaration):

	{
		"field1": {
			"type": "str",
			"aliases": ["FieldOne"]
		},
		"field2": {
			"type": "ui64",
		},
	}

The schema is passed to the `schemas` list in the function declaration:

	splang.FunctionDeclaration(
		name="main",
		returns="bool",
		arguments={
			'myArgument': 'json'
		},
		schemas={
			'myArgument': {
				"field1": {"type": "str", "aliases": ["FieldOne"]},
			}
		}
	)

Tje key `myArgument` specifies the name of the argument on which the schema will be applied.
Multiple arguments with a different schemas could be specified.

Hence, when using the `!GET` expression for instance, the argument `type` does not need to be specified, since it is going to be loaded automatically from the schema for the given attribute.


## Options

### Option `type`

Defines the data type for the given attribute, such as `str`, `si64` and so on.
Refer to a SP-Lang type system for more information.

This option is mandatory.


### Option `aliases`

Defines field aliases for the given attribute, that can be used in the declaration as a synonymic term.

If an `field1` has a field alias named `FieldOne`, the following declarations are equal if the schema is properly defined:

	!GET
	what: field1
	from: !ARG myArgument

	!GET
	what: FieldOne
	from: !ARG myArgument


### Option `unit`

Defines the unit of the attribute, if needed, such as for timestamps. In this case, the unit can be `auto` for automatical detection, `seconds` and `microseconds`.


## YAML schema

YAML representation of the schema is used eg. in the library:

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

