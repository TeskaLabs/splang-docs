---
title: Logic expressions
---

# Logic expressions


---

## `!AND`: Conjunction 

Type: _Sequence_

### Synopsis

```yaml
!AND
- <expression 1>
- <expression 2>
- ...
```

### Boolean `!AND`

Boolean conjunction `!AND` is an boolean functional operation on sequence of logical values, that produces a boolean value of "true" if and only if all of its values are true.

### Example

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


### Bitwise  `!AND`

When `!AND` is applied on integers (instead on boolean) types, it provides a bitwise AND.

### Example

```yaml
!AND
- !ARG PRI
- 7
```

In this example, the argument `PRI` is masked with 7 (in binary `00000111`).

---

## `!OR`: Disjunction 

Type: _Sequence_

### Synopsis

```yaml
!OR
- <expression 1>
- <expression 2>
- ...
```

### Example

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


### Boolean `!OR`

Boolean disjunction is a boolean functional operation which returns the boolean value "true" unless all of its arguments are "false".

### Bitwise `!OR`

When `!OR` is applied on integers (instead on boolean) types, it provides a bitwise OR.


---

## `!NOT`: Negation 

Type: _Mapping_.

### Synopsis

```yaml
!NOT
what: <expression>
```

### Boolean `!NOT`

Boolean negation is an operation on one boolean value that produces a boolean value of "true" when its operand is "false", and a value of "false" when its operand is "true".

### Bitwise `!NOT`

When integer is provided, then `!NOT` returns value with bits of `what` flipped.

_Hint: If you want to test that integer is not zero, use `!NE` test expression._
