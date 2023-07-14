---
title: Tuple
---

# Tuple expressions


The tuple is one of basic data structures provided by SP-Lang.
A tuple is a collection of items, possibly of different types.

--- 

## `!TUPLE`: A collection of items 

Type:  _Mapping_.

Synopsis:

```yaml
!TUPLE
with:
  - ...
  - ...
  ...
```

There is no limit of the number of items in the tuple.
The order of the items is preserved.


!!! example

    ```yaml
    !TUPLE
    with:
      - John Doe
      - 37
      - 175.4
    ```

!!! example

    Use of the `!!tuple` notation:

    ```yaml
    !!tuple
    - 1
    - a
    - 1.2
    ```

!!! example

    Even more concise version of the `!!tuple` using flow syntax:

    ```yaml
    !!tuple ['John Doe', 37, 175.4]
    ```

!!! example

    Enforce specific type of the item:

    ```yaml
    !TUPLE
    with:
      - John Doe
      - !!ui8 37
      - 175.4
    ```

    Item #1 will have a type `ui8`.


--- 

## `!GET`: Get the item from a tuple 

Type: _Mapping_.

Synopsis:

```yaml
!GET
what: <index of the item>
from: <tuple>
```

`what` is an integer (number), it represent the _index_ in a tuple.
`what` can be negative, in that case, it specifies an item from the end of the list.
Items are indexed from the 0, it means that the first item in the list has an index 0.
If the `what` is out of bound of the list, the statement returns with error.


!!! example

```yaml
!GET
what: 1
from:
  !TUPLE
  with:
    - John Doe
    - 32
    - 127.5
```

    Returns `32`.


!!! example

    Using the _negative index_ of items:

    ```yaml
    !GET
    what: -1
    from:
      !TUPLE
      with:
        - John Doe
        - 32
        - 127.5
    ```

    Returns `127,5`.
