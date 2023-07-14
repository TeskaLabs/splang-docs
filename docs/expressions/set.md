---
title: Set
---

# Set expression


The set store unique items, without any particular order.
Items in the set must be of the same type.
The set is one of basic data structures provided by SP-Lang.

A set is best suited for a testing value for membership rather than retrieving a specific element from a set.

--- 

## `!SET`: Set of items 

Type:  _Implicit sequence_, _Mapping_.

Synopsis:

```yaml
!SET
- ...
- ...
```

!!! hint

    Use `!COUNT` to determine number of items in the set.

There are several ways, how a set can be specified in SP-Lang:

!!! example

    ```yaml
    !SET
    - "One"
    - "Two"
    - "Three"
    - "Four"
    - "Five"
    ```

!!! example

    [YAML unordered set](https://yaml.org/spec/1.2.2/#example-unordered-sets):

    ```yaml
    !!set
    ? Yellow pork
    ? Pink grass
    ? White snow
    ```

!!! example

    Concise set using [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):

    ```yaml
    !SET ["One", "Two", "Three", "Four", "Five"]
    ```

!!! example
    The mapping form:

    ```yaml
    !SET
    with:
    - "One"
    - "Two"
    - "Three"
    - "Four"
    - "Five"
    ```


--- 

## `!IN`: Membership test 

Type: _Mapping_.

Synopsis:

```yaml
!IN
what: <item>
where: <set>
```

Check if `item` is present in the `set`.

The expression `!IN` is described in the [Comparisons](../comparisons/#in-membership-test) chapter.

!!! example

    ```yaml
    !IN
    what: 3
    where:
      !SET
      with:
        - 1
        - 2
        - 5
        - 8 
    ```
