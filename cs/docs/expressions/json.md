---
git_commit_hash: b55fa3f
title: JSON
---

# JSON


SP-Lang nabízí [vysokorychlostní přístup](https://simdjson.org) k datovým objektům JSON.

--- 

## `!GET`: Získat hodnotu z JSON 

Typ: _Mapping_.


### Synopse
```yaml

!GET
co: <item>
typ: <type>
od: <json>
výchozí: <value>
```

Získat položku zadanou pomocí `what` z JSON objektu `from`.
Pokud položka není nalezena, vrátí `default` nebo chybu, pokud není zadáno `default`.
`default` je nepovinné.

Volitelně můžete zadat typ položky pomocí `type`.

### Příklad

JSON (také známý jako `!ARG jsonmessage`):
```json

{
  "foo.bar": "Příklad"
}
```

Získání pole `foo.bar` z výše uvedeného JSON:
```yaml

!GET
co: foo.bar
from: !ARG jsonmessage
```


### JSON Pointer

Pokud chcete přistupovat k položce ve vnořeném JSON, musíte použít [JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901) (např. `/foo/bar` o`/foo/bar`) jako `what` pro tento účel.

Pro odvození typu položky se použije schéma, ale pro složitější přístup se doporučuje použít argument `type`.

Vnořený JSON (aka `!ARG jsonmessage`):
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
co: /foo/bar
typ: str
from: !ARG jsonmessage
```

--- 

## `!JSON.PARSE`: Parse JSON 

Typ: _Mapping_.

### Synopse
```yaml

!JSON.PARSE
what: <str>
schéma: <schema>
```

Parsovat JSON řetězec.
Výsledek lze použít např. pomocí operátoru `!GET`.

Nepovinný argument `schema` určuje schéma, které se má použít.
Výchozím schématem je vestavěné schéma `ANY`.


### Příklad
```yaml

!JSON.PARSE
what: |
  {
    "string1": "Hello World!",
    "string2": "Goodbay ..."
  }
```
