---
layout: default
title: SP-Lang Documentation
---

# Schema

Schemas in SP-Lang describe the function's arguments and their attributes.


## Schema definition

A schema is represented by a dictionary describing the argument's attributes such as their data type, unit and field alises (different notations in the declaration):

	'myArgument': {
		"attribute1": {"type": "str", "unit": "auto", "aliases": ["attr1", "Attr1"]},
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
				"attribute1": {"type": "str", "unit": "auto", "aliases": ["attr1", "Attr1"]},
			}
		}
	)

Hence, when using the `!GET` expression for instance, the argument `type` does not need to be specified, since it is going to be loaded automatically from the schema for the given attribute.


### Option `type`

Defines the data type for the given attribute, such as `str`, `si64` and so on. The data type is automatically used in `!GET` expression.


### Option `unit`

Defines the unit of the attribute, if needed, such as for timestamps. In this case, the unit can be `auto` for automatical detection, `seconds` and `microseconds`.


### Option `aliases`

Defines field aliases for the given attribute, that can be used in the declaration as a synonymic term.

If an `attribute1` has a field alias named `attr1`, the following declarations are equal if the schema is properly defined:

	!GET
	what: attribute1
	from: !ARG myArgument

	!GET
	what: attr1
	from: !ARG myArgument
