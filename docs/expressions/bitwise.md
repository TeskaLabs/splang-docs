---
title: Bitwise
---

# Bitwise expressions


The bit shifts treat a value as a series of bits, the binary digits of the value are moved, or shifted, to the left or right.


There are also bitwise `!AND`, `!OR` and `!NOT` expression, at [Logic](../logic) chapter.

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
	what: 60
	by: 2
	```

	The result is: `240 = (60*2^2)`, `2^2 = 4`.

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
	what: 2048
	by: 4
	```

	The result is: `128 = (2048/2^4)`, `2^4 = 16`.


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
