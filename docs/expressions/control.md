---
title: Control
---

# Control expressions

## Overview

SP-Lang provides a variety of control flow statements.

* [`!IF`](#if): Simple conditional branching.
* [`!WHEN`](#when): Powerful branching.
* [`!MATCH`](#match): Pattern matching.
* [`!TRY`](#try): Execute till first non-error expression.
* [`!FOR`](#for): Apply an expression to each item in a sequence.

---

## `!IF`

Simple conditional branching.

Type: _Mapping_.

The `!IF` expression is a decision-making expression that guides the evaluation to make decisions based on specified test.

```yaml
!IF
test: <expression>
then: <expression>
else: <expression>
```

Based on the value of `test`, the branch is evaluated:

* `then` in case of `test !EQ true`
* `else` in case of `test !EQ false`

Both `then` and `else` have to return the same type, which will be also the type of the `!IF` return value.


!!! example

    ```yaml
    !IF
    test:
      !EQ
      - !ARG input
      - 2
    then:
      It is two.
    else:
      It is NOT two.
    ```

---

## `!WHEN`  

Powerful branching.

Type: _Sequence_.

`!WHEN` expression is considerably more powerful than `!IF` expression.
Cases can match many different patterns, including interval matches, tuples, and so on. 


```yaml
!WHEN
- test: <expression>
  then: <expression>

- test: <expression>
  then: <expression>

- test: <expression>
  then: <expression>

- ...

- else: <expression>
```

If `else` is not provided, then `!WHEN` returns `None` (error).


!!! example

    Example of `!WHEN` use for exact match, range match and set match:

    ```yaml
    !WHEN

    # Exact value match
    - test:
        !EQ
        - !ARG key
        - 34
      then:
        "thirty four"

    # Range match
    - test:
        !LT
        - 40
        - !ARG key
        - 50
      then:
        "forty to fifty (exclusive)"

    # In-set match
    - test:
        !IN
        what: !ARG key
        where:
          - 75
          - 77
          - 79
      then:
        "seventy five, seven, nine"

    - else:
        "unknown"
    ```

---

## `!MATCH`

Pattern matching.

Type: _Mapping_.

```yaml
!MATCH
what: <what-expression>
with:
  <value>: <expression>
  <value>: <expression>
  ...
else:
  <expression>
```

`!MATCH` expression evaluates the `what-expression`, matching the expression's value to a case clause, and executes `expression` associated with that case.

The `else` branch of the `!MATCH` is optional.
The expression fails with error when no matching `<value>` is found and `else` branch is missing.


!!! example

    ```yaml
    !MATCH
    what: !ARG value
    with:
        1: "one"
        2: "two"
        3: "three"
    else:
        "other number"
    ```

!!! hint "Use of `!MATCH` to structure the code"

    ```yaml
    !MATCH
    what: !ARG code
    with:
        1: !INCLUDE code-1.yaml
        2: !INCLUDE code-2.yaml
    else:
        !INCLUDE code-else.yaml
    ```

---

## `!TRY`

Execute till first non-error expression.

Type: _Sequence_

```yaml
!TRY
- <expression>
- <expression>
- <expression>
...
```

Iterate thru expression (top down), if the expression return non-null (`None`) result, stop iteration and return that value.
Otherwise continue to the next expression.

Returns `None` (error) when end of the list is reached.


Note: `!FIRST` is a legacy alias for `!TRY` and is still accepted.


---

## `!FOR`

Apply an expression to each item in a sequence.

Type: _Mapping_.

```yaml
!FOR
each: <sequence>
do: <expression>
```

Returns a list with the result of `do` evaluated once for each item in `each`.

The current item from `each` is not passed into `do` as an argument.
