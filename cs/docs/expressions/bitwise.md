---
git_commit_hash: b55fa3f
title: Bitově
---

# Bitové výrazy


Bitové posuny zachází s hodnotou jako s řadou bitů, binární číslice hodnoty jsou přesunuty nebo posunuty doleva nebo doprava.


Existují také bitové výrazy `!AND`, `!OR` a `!NOT`, v kapitole [Logika](../logika).

---

## `!SHL`: Levý logický posun 

Typ: _Mapování_.
```yaml

!SHL
co: <...>
by: <...>
```

!!! tip

	
	
	
	Levý posun lze použít jako rychlé násobení čísly 2, 4, 8 atd.
	
	

!!! example

	
	
	```yaml
	
	!SHL
	co: 60
	podle: 2
	```
	
	Výsledek je: `240 = (60*2^2)`, `2^2 = 4`.
	

---

## `!SHR`: Pravý logický posun  

Typ: _Mapování_.
```yaml

!SHR
co: <...>
by: <...>
```

!!! tip

	
	
	
	Pravý posun lze použít jako rychlé dělení číslem 2, 4, 8 atd.
	
	

!!! example

	
	
	```yaml
	
	!SHR
	co: 2048
	by: 4
	```
	
	Výsledek je: `128 = (2048/2^4)`, `2^4 = 16`.
	
	

--- 

## `!SAL`: Levý aritmetický posun 

Typ: _Mapping_.
```yaml

!SAL
co: <...>
by: <...>
```


!!! example

	
	
	```yaml
	!SAL
	co: 60
	podle: 2
	```
	
	

---

## `!SAR`: Pravý aritmetický posun 

Typ: _Mapping_.
```yaml

!SAR
co: <...>
by: <...>
```


---

## `!ROL`: (kruhový) posun doleva 

Typ: _Mapping_.
```yaml

!ROL
co: <...>
by: <...>
```


---

## `!ROR`: Pravý rotační (kruhový) posun 

Typ: _Mapping_.
```yaml

!ROR
co: <...>
by: <...>
```
