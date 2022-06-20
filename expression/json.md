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
what: <jsonpath>
type: <type>
from: <json>
default: <value>
```

Get the item from the `json`  using JSONPath `jsonpath`.
You may specify the item type by `type`.

If the `jsonpath` is not found, return `default` or error if `default` is not provided.
`default` is optional.

### Example

```yaml
!GET
what: /string3
type: str
from: !ARG json
default: "?"
```

--- 

## `!JSON.PARSE`: Parse JSON {#EXPR-JSON-PARSE}

Type: _Mapping_.

### Synopsis

```yaml
!JSON.PARSE
what: <str>
```

Parse JSON string.
The result can be used with e.g. `!GET` operator.


### Example

```yaml
!JSON.PARSE
what: |
  {
    "string1": "Hello World!",
    "string2": "Goodbay ..."
  }
```
