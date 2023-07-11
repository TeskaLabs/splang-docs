---
git_commit_hash: b55fa3f
title: JSON
---

# JSON


SP-Lang nabízí [vysokorychlostní přístup](https://simdjson.org) k datovým objektům JSON.

--- 

## `!GET`: Získá hodnotu z JSON 

Typ: _Mapping_.


Synopsis:

```yaml

!GET
what: <item>
typ: <type>
od: <json>
výchozí: <value>
```

Získat položku zadanou pomocí `what` z JSON objektu `from`.
Pokud položka není nalezena, vrátí `default` nebo chybu, pokud není zadáno `default`.
`default` je nepovinné.

Volitelně můžete zadat typ položky pomocí `type`.

!!! example "Příklad"

	JSON (`!ARG jsonmessage`):

	```json
	{
	"foo.bar": "Příklad"
	}
	```

	Pro získání pole `foo.bar` z výše uvedeného JSON:

	```yaml

	!GET
	what: foo.bar
	from: !ARG jsonmessage
	```


### JSON Pointer

Pro přístup k položce ve vnořeném JSONu je třeba použít [JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901) (např. `/foo/bar` o`/foo/bar`) jako `what`.

Pro odvození typu položky se použije schéma, ale pro složitější přístup doporučujeme použít argument `type`.

!!! example "Příklad"

	Vnořený JSON (`!ARG jsonmessage`):

	```json
	{
	"foo": {
		"bar": "Příklad"
	}
	}
	```

	Příklad extrakce řetězce z vnořeného JSON:

	```yaml
	!GET
	what: /foo/bar
	type: str
	from: !ARG jsonmessage
	```

--- 

## `!JSON.PARSE`: Parsuje JSON 

Typ: _Mapping_.

Synopsis:

```yaml

!JSON.PARSE
what: <str>
schéma: <schema>
```

Parsuje JSON řetězec.
Výsledek lze použít např. pomocí operátoru `!GET`.

Nepovinný argument `schema` určuje schéma, které se má použít.
Výchozím schématem je vestavěné schéma `ANY`.


!!! example "Příklad"

	```yaml

	!JSON.PARSE
	what: |
	{
		"string1": "Hello World!",
		"string2": "Goodby ..."
	}
	```
