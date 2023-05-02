---
title: Bitwise expressions
---

# Bitwise expressions


The bit shifts treat a value as a series of bits, the binary digits of the value are moved, or shifted, to the left or right.

_Hint: Left shifts could be used as fast multiplication by 2, 4, 8 and so on._

_Hint: Right shifts could be used as fast division by 2, 4, 8 and so on._

There are also bitwise `!AND`, `!OR` and `!NOT` expression, for details, continue to "Logic" chapter.

--- 

## `!SAL`: Left arithmetic shift 

Type: _Mapping_.

### Synopsis

```yaml
!SAL
what: <...>
by: <...>
```

### Example

```yaml
!SAL
what: 60
by: 2
```


---

## `!SAR`: Right arithmetic shift 

Type: _Mapping_.

### Synopsis

```yaml
!SAR
what: <...>
by: <...>
```


---

## `!SHL`: Left logical shift 

Type: _Mapping_.

### Synopsis

```yaml
!SHL
what: <...>
by: <...>
```


---

## `!SHR`: Right logical shift  

Type: _Mapping_.

### Synopsis

```yaml
!SHR
what: <...>
by: <...>
```


---

## `!ROL`: Left rotation (circular) shift 

Type: _Mapping_.

### Synopsis

```yaml
!ROL
what: <...>
by: <...>
```


---

## `!ROR`: Right rotation (circular) shift 

Type: _Mapping_.

### Synopsis

```yaml
!ROR
what: <...>
by: <...>
```
