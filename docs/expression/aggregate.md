---
title: Aggregate expressions
---

# Aggregate expressions


---

## `!AVG`: Average 

Type: _Sequence_

Calculate the average / arithmetic mean.

[More information](https://en.wikipedia.org/wiki/Arithmetic_mean) (Wikipedia)

### Example

```yaml
!AVG
- 1
- 2
- 3
```

Calculation of the average `(1+2+3)/3`,  the result is `2`.

---

## `!MAX`: Maximum 

Type: _Sequence_

Returns a maximum value from the seqence.


### Example

```yaml
!MAX
- 1.5
- 2.6
- 3.05
- 4.45
- 5.1
```


---

## `!MIN`: Minimum 

Type: _Sequence_

Returns a minimum value from the seqence.

### Example

```yaml
!MIN
- 0.5
- 2.6
- 3.05
- 4.45
- 5.1
```

---

## `!COUNT`: Count number of elements 

Type: _Sequence_

### Example

```yaml
!COUNT
- Frodo Baggins
- Sam Gamgee
- Gandalf
- Legolas
- Gimli
- Aragorn
- Boromir of Gondor
- Merry Brandybuck
- Pippin Took
```

Returns `9`.

---

## `!MEDIAN`: The middle value 

Type: _Sequence_

[More information](https://en.wikipedia.org/wiki/Median) (Wikipedia)


### Example

```yaml
!MEDIAN
- 1
- 4
- -1
- 9
- 101
```

---

## `!MODE`: Value that appears most often 

Type: _Sequence_

[More information](https://en.wikipedia.org/wiki/Mode_%28statistics%29) (Wikipedia)


### Example

```yaml
!MODE
- -10
- -10
- -20
- -20
- 1
- 2
- 3
- 4
- 5
```

---

## `!RANGE`: The difference between the largest and smallest value 

Type: _Sequence_

Calculates the difference between the largest and smallest values.

[More information](https://en.wikipedia.org/wiki/Range_%28statistics%29) (Wikipedia)

### Example

```yaml
!RANGE
- 1
- 3
- 4
- 20
- -1
```
