---
title: Logic
---

# Logic expressions

## Overview

Logic expressions are commonly used to create more restrictive and precise conditions, such as filtering event, or triggering specific actions based on a set of criteria.
Logic expressions operates with truth values `true` and `false`.

!!! info "Logic expressions are representations of boolean algebra"

    For more information, continue to [boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra) page at Wikipedia.


* [`!AND`](#and): Conjunction.
* [`!OR`](#or): Disjunction.
* [`!NOT`](#not): Negation.

---

## `!AND`

The logical `!AND` expression is  used to combine two or more conditions that must all be true for the entire expression to be true.
It is used to create more restrictive and precise conditions.

Type: _Sequence_

Synopsis:

```yaml
!AND
- <condition 1>
- <condition 2>
- ...
```

In a logical `!AND` expression, conditions (`condition 1`, `condition 2`, ...) can be any expressions that evaluate to a boolean value (true or false).
The conditions are evaluated from top to bottom, and the evaluation process stops as soon as a false condition is found, following the concept of short-circuit evaluation.

!!! info "Logical conjunction"

    For more information, continue to [Logical conjunction](https://en.wikipedia.org/wiki/Logical_conjunction) page at Wikipedia.


!!! example

    ```yaml
    !AND
    - !EQ
        - !ARG vendor
        - TeskaLabs
    - !EQ
        - !ARG product
        - LogMan.io
    - !EQ
        - !ARG version
        - v23.10
    ```

    In this example, if all of the conditions evaluate to true, the entire logical `!AND` expression will be true.
    If any of the conditions are false, the logical `!AND` expression will be false.


### Bitwise `!AND`

When `!AND` is applied on integer types, instead on booleans, it provides a bitwise AND.

!!! example

    ```yaml
    !AND
    - !ARG PRI
    - 7
    ```

    In this example, the argument `PRI` is masked with 7 (in binary `00000111`).

---

## `!OR`

The logical `!OR` expression is used to combine two or more conditions where at least one of the conditions must be true for the entire expression to be true.
It is used to create more flexible and inclusive conditions.

Type: _Sequence_

Synopsis:

```yaml
!OR
- <condition 1>
- <condition 2>
- ...
```

Conditions (`condition 1`, `condition 2`, ...) can be any expressions that evaluate to a boolean value (`true` or `false`).
The conditions are evaluated from top to bottom, and the evaluation process stops as soon as a true condition is found, following the concept of short-circuit evaluation.

!!! info "Logical disjunction"

    For more information, continue to [Logical disjunction](https://en.wikipedia.org/wiki/Logical_disjunction) page at Wikipedia.

!!! example

    ```yaml
    !OR
    - !EQ
        - !ARG description
        - unauthorized access
    - !EQ
        - !ARG reason
        - brute force
    - !EQ
        - !ARG message
        - malware detected
    ```

    In this example, the expression is true when any of the following conditions is met:

    1. The `description` field matches the string "unauthorized access"
    2. The `reason` field matches the string "brute force"
    3. The `message` field matches the string "malware detected"


### Bitwise `!OR`

When `!OR` is applied on integer types, instead on booleans, it provides a bitwise OR.

!!! example

    ```yaml
    !OR
    - 1  # Read access (binary 001, decimal 1)
    - 4  # Execute access (binary 100, decimal 4)
    ```

    In this example, the expression is evaluated to 5.

    This is because, in a bitwise `!OR` operation, each corresponding bit in the binary representation of the two numbers is combined using the `!OR` expression:

    ```
    001 (read access)
    100 (execute access)
    ---
    101 (combined permissions)
    ```

    The expression calculates the permissions with the resulting value (binary 101, decimal 5) from the bitwise OR operation, combining both read and execute access.

---

## `!NOT`

The logical `!NOT` expression is used to invert the truth value of a single condition.
It is used to exclude specific conditions when certain conditions are not met.

Type: _Mapping_.


Synopsis:

```yaml
!NOT
what: <expression>
```

!!! info "Negation"

    For more information, continue to [Negation](https://en.wikipedia.org/wiki/Negation) page at Wikipedia.


### Bitwise `!NOT`

When integer is provided, then `!NOT` returns value with bits of `what` flipped.

!!! tip

    If you want to test that integer is not zero, use `!NE` test expression.
