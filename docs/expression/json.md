---
layout: default
title: SP-Lang documentation
---

# JSON

* This will become a table of contents (this text will be scrapped).
{:toc}

SP-Lang offers a [high-speed access](https://simdjson.org) to JSON data objects.

--- 

## `!GET`: Get the value from a JSON {#EXPR-JSON-GET}

Type: _Mapping_.


### Synopsis

```yaml
!GET
what: <item>
type: <type>
from: <json>
default: <value>
```

Get the item specified by the `what` from the `from` JSON object.
If the item is not found, return `default` or error if `default` is not provided.
`default` is optional.

You may optionally specify the item type by `type`.

### Example

JSON (aka `!ARG jsonmessage`):

```json
{
  "foo.bar": "Example"
}
```

Get the field `foo.bar` from a JSON above:

```yaml
!GET
what: foo.bar
from: !ARG jsonmessage
```


### JSON Pointer

If you want to access the item in the nested JSON, you need to use a [JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901) (e.g. `/foo/bar` o`/foo/bar`) as a `what` for that.

The schema will be applied to infer the type of the item but for more complex access, the `type` argument is recommended.

Nested JSON (aka `!ARG jsonmessage`):

```json
{
  "foo": {
    "bar": "Example"
  }
}
```

Example of extraction of the string from the nested JSON:

```yaml
!GET
what: /foo/bar
type: str
from: !ARG jsonmessage
```

--- 

## `!JSON.PARSE`: Parse JSON {#EXPR-JSON-PARSE}

Type: _Mapping_.

### Synopsis

```yaml
!JSON.PARSE
what: <str>
schema: <schema>
```

Parse JSON string.
The result can be used with e.g. `!GET` operator.

Optional argument `schema` specifies the schema to be applied.
The default schema is build-in `ANY`.


### Example

```yaml
!JSON.PARSE
what: |
  {
    "string1": "Hello World!",
    "string2": "Goodbay ..."
  }
```
