---
title: Expressions
---

# SP-Lang Expressions

Expressions in SP-Lang are written as [YAML tags directives](https://yaml.org/spec/1.2.2/#682-tag-directives).

## Aggregate

| Expression | Type | Description |
| --- | --- | --- |
| `!COUNT`| sequence | Counts the number of items. |
| `!MIN` | sequence | Calculates the minimum from a list of items. |
| `!MAX` | sequence | Calculates the maximum from a list of items. |
| `!AVG` | sequence | Calculates the average (arithmetic mean) of items in a list. |
| `!MEDIAN` | sequence | Finds the median (middle value) of a list of items. |
| `!MODE` | sequence | Finds the value that appears most often. |
| `!RANGE` | sequence | Finds the difference between the highest and smallest value. |

## Arithmetic

| Expression | Type | Description |
| --- | --- | --- |
| `!ADD` | sequence | Addition. |
| `!SUB` | sequence | Subtraction. |
| `!MUL` | sequence | Multiplication. |
| `!DIV` | sequence | Division. |
| `!MOD` | sequence | Modulo. |
| `!POW` | sequence | Exponentiation. |
| `!ABS` | mapping | Absolute value. |

## Bitwise

| Expression | Type | Description |
| --- | --- | --- |
| `!SHL` | mapping | Left logical shift. |
| `!SHR` | mapping | Right logical shift. |
| `!SAL` | mapping | Left arithmetic shift. |
| `!ROL` | mapping | Circular rotation to the left. |
| `!ROR` | mapping | Circular rotation to the right. |

## Comparisons

| Expression | Type | Description |
| --- | --- | --- |
| `!EQ` | sequence | Equal to. |
| `!NE` | sequence | Not equal to. |
| `!LT` | sequence | Less than. |
| `!LE` | sequence | Less than or equal to. |
| `!GT` | sequence | Greater than. |
| `!GE` | sequence | Greater than or equal to. |
| `!IN` | mapping | Membership test. |

## Control

| Expression | Type | Description |
| --- | --- | --- |
| `!IF` | mapping | Simple conditional branching. |
| `!WHEN` | sequence | Powerful branching. |
| `!MATCH` | mapping | Pattern matching. |
| `!TRY` | sequence | Execute till first non-error expression. |
| `!MAP` | mapping | Apply the expression on each element in a sequence. |
| `!REDUCE` | mapping | Reduce the elements of an list into a single value. |
