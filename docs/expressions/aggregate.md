---
title: Aggregate
---

# Aggregate expressions

## Overview

An aggregate expression is a type of function that performs calculations on a set of values and returns a single value as a result.
These expressions are commonly used to summarize or condense data.

* [`!COUNT`](#count): Counts the number of items.
* [`!MAX`](#max), [`!MIN`](#min): Calculates the maximum / maximum.
* [`!AVG`](#avg): Calculates the average (arithmetic mean).
* [`!MEDIAN`](#median): Finds the middle value.
* [`!MODE`](#mode): Finds the value that appears most often.
* [`!RANGE`](#range): Finds the difference between the highest and smallest value.


---

## `!COUNT`

Counts the number of items in a list.

Type: _Sequence_

!!! example

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

## `!MAX`

Returns a maximum value from the sequence.

Type: _Sequence_

!!! example

    ```yaml
    !MAX
    - 1.5
    - 2.6
    - 5.1
    - 3.05
    - 4.45
    ```

    The result of this expression is `5.1`.

---

## `!MIN`

Returns a minimum value from the sequence.

Type: _Sequence_

!!! example

    ```yaml
    !MIN
    - 2.6
    - 3.05
    - 4.45
    - 0.5
    - 5.1
    ```

    The result of this expression is `0.5`.

---

## `!AVG`

Calculate the average / arithmetic mean.

Type: _Sequence_

!!! info

    Read more about [Arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean) on Wikipedia.

!!! example

    ```yaml
    !AVG
    - 6
    - 2
    - 4
    ```

    Calculation of the average `(6+2+4)/3`,  the result is `4`.

---

## `!MEDIAN`

The median is the middle value in a list of numbers; half of the values are greater than the median, and half are less than the median.
If the list has an even number of elements, the median is the average of the two middle values.

Type: _Sequence_


!!! info

    Read more about [median](https://en.wikipedia.org/wiki/Median) on Wikipedia.


!!! example

    ```yaml
    !MEDIAN
    - 1
    - 4
    - -1
    - 9
    - 101
    ```

    Returns `4`.

---

## `!MODE`

The mode is the value or values that occur most frequently in a list.
It can be used to represent the central tendency of a data set.

Type: _Sequence_

!!! info

    Read more about [mode](https://en.wikipedia.org/wiki/Mode_%28statistics%29) on Wikipedia.


!!! example

    ```yaml
    !MODE
    - 10
    - 10
    - -20
    - -20
    - 6
    - 10
    ```

    Returns `10`.

---

## `!RANGE`

Calculates the difference between the largest and smallest values.

Type: _Sequence_

!!! info

    Read more about [range](https://en.wikipedia.org/wiki/Range_%28statistics%29) on Wikipedia.

!!! example

    ```yaml
    !RANGE
    - 1
    - 3
    - 4
    - 20
    - -1
    ```

    Returns `21`.
