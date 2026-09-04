---
title: Lookup
---

# Lookup expressions


## Overview

* [`!LOOKUP`](#lookup): Reference a named lookup table.
* [`!GET`](#get): Get a value from a lookup.
* [`!IN`](#in): Check if a key is in a lookup.

Legacy aliases `!LOOKUP.GET` and `!LOOKUP.CONTAINS` are still accepted.

---

## `!LOOKUP`

Reference a named lookup table.

Type: _Mapping_ or _Scalar_.

Synopsis:

```yaml
!LOOKUP
what: <lookup-name>
```

or shorter form:

```yaml
!LOOKUP <lookup-name>
```

The lookup must be defined in the application configuration.

---

## `!GET`

Get a value from a lookup.

Type: _Mapping_.

Synopsis:

```yaml
!GET
what: <key>
from: !LOOKUP
      what: <lookup-name>
default: <value>
```

- `default` is optional. If the key is not found, `default` is returned. If `default` is omitted, the expression returns `None` (error).
- If `what` is a list, the expression returns the value for the first key from the list that exists in the lookup.

!!! example

    ```yaml
    !GET
    what: foo
    from: !LOOKUP
          what: my_lookup
    ```

---

## `!IN`

Check if a key is in a lookup.

Type: _Mapping_.

Synopsis:

```yaml
!IN
what: <key>
where: !LOOKUP
       what: <lookup-name>
```

- If `what` is a list, the expression returns `true` when any key from the list is present in the lookup.

!!! example

    ```yaml
    !IN
    what: foo
    where: !LOOKUP
           what: my_lookup
    ```

---

## Legacy aliases

### `!LOOKUP.GET`

Backward-compatible alias for `!GET` with lookup specified by `in:`:

```yaml
!LOOKUP.GET
what: foo
in: my_lookup
```

### `!LOOKUP.CONTAINS`

Backward-compatible alias for `!IN` with lookup specified by `in:`:

```yaml
!LOOKUP.CONTAINS
what: foo
in: my_lookup
```
