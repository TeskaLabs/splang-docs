---
title: Bitwise
---

# Bitwise expressions


The bit shifts treat a value as a series of bits, the binary digits of the value are moved, or shifted, to the left or right.


There are also bitwise `!AND`, `!OR` and `!NOT` expression, at [Logic](./logic.md) chapter.

---

## `!SHL`: Left logical shift 

Type: _Mapping_.

```yaml
!SHL
what: <...>
by: <...>
```

!!! tip

	Left shifts could be used as fast multiplication by 2, 4, 8 and so on.


!!! example

	```yaml
	!SHL
	what: 9
	by: 2
	```

	`9` is represented by the binary value `1001`. The left logical shift moves the bits to the left by 2. The result is `100100`, which is `36` in the base-ten system. This is the same result as `9 * (2^2)`.

---

## `!SHR`: Right logical shift  

Type: _Mapping_.

```yaml
!SHR
what: <...>
by: <...>
```

!!! tip

	Right shifts could be used as fast division by 2, 4, 8 and so on.


!!! example

	```yaml
	!SHR
	what: 16
	by: 3
	```

	`16` is represented by `10000`. The logical shift moves the bits to the right by `3`. The result is `10`, which is `2` in base-ten system. This is the same result as `16 / (2^3)`.


--- 

## `!SAL`: Left arithmetic shift 

Type: _Mapping_.

```yaml
!SAL
what: <...>
by: <...>
```

!!! example

	```yaml
	!SAL
	what: 60
	by: 2
	```


---

## `!SAR`: Right arithmetic shift 

Type: _Mapping_.

```yaml
!SAR
what: <...>
by: <...>
```


---

## `!ROL`: Left rotation (circular) shift 

Type: _Mapping_.

```yaml
!ROL
what: <...>
by: <...>
```


---

## `!ROR`: Right rotation (circular) shift 

Type: _Mapping_.

```yaml
!ROR
what: <...>
by: <...>
```
