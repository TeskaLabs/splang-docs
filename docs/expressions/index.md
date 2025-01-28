---
title: Expressions
search:
    boost: 2
---

# SP-Lang Expressions

Expressions in SP-Lang are written as [YAML tags directives](https://yaml.org/spec/1.2.2/#682-tag-directives).

## List of expressions

<!-- TODO: Move this to a separate, automatically updated file! -->

| Expression | Type | Category | Description |
| :---: | :---: | :---: | --- |
| [`!COUNT`](./aggregate.md#count) | sequence | aggregate | Counts the number of items. |
| [`!MIN`](./aggregate.md#min) | sequence | aggregate | Calculates the minimum from a list of items. |
| [`!MAX`](./aggregate.md#max) | sequence | aggregate | Calculates the maximum from a list of items. |
| [`!AVG`](./aggregate.md#avg) | sequence | aggregate | Calculates the average (arithmetic mean) of items in a list. |
| [`!MEDIAN`](./aggregate.md#median) | sequence | aggregate | Finds the median (middle value) of a list of items. |
| [`!MODE`](./aggregate.md#mode) | sequence | aggregate | Finds the value that appears most often. |
| [`!RANGE`](./aggregate.md#range) | sequence | aggregate | Finds the difference between the highest and smallest value. |
| [`!ADD`](./arithmetics.md#add) | sequence | arithmetic | Addition. |
| [`!SUB`](./arithmetics.md#sub) | sequence | arithmetic | Subtraction. |
| [`!MUL`](./arithmetics.md#mul) | sequence | arithmetic | Multiplication. |
| [`!DIV`](./arithmetics.md#div) | sequence | arithmetic | Division. |
| [`!MOD`](./arithmetics.md#mod) | sequence | arithmetic | Modulo. |
| [`!POW`](./arithmetics.md#pow) | sequence | arithmetic | Exponentiation. |
| [`!ABS`](./arithmetics.md#abs) | mapping | arithmetic | Absolute value. |
| [`!SHL`](./bitwise.md#shl) | mapping | bitwise | Left logical shift. |
| [`!SHR`](./bitwise.md#shr) | mapping | bitwise | Right logical shift. |
| [`!SAL`](./bitwise.md#sal) | mapping | bitwise | Left arithmetic shift. |
| [`!ROL`](./bitwise.md#rol) | mapping | bitwise | Circular rotation to the left. |
| [`!ROR`](./bitwise.md#ror) | mapping | bitwise | Circular rotation to the right. |
| [`!EQ`](./comparisons.md#eq) | sequence | comparisons | Equal to. |
| [`!NE`](./comparisons.md#ne) | sequence | comparisons | Not equal to. |
| [`!LT`](./comparisons.md#lt) | sequence | comparisons | Less than. |
| [`!LE`](./comparisons.md#le) | sequence | comparisons | Less than or equal to. |
| [`!GT`](./comparisons.md#gt) | sequence | comparisons | Greater than. |
| [`!GE`](./comparisons.md#ge) | sequence | comparisons | Greater than or equal to. |
| [`!IN`](./comparisons.md#in) | mapping | comparisons | Membership test. |
| [`!IF`](./control.md#if) | mapping | control | Simple conditional branching. |
| [`!WHEN`](./control.md#when) | sequence |  control | Powerful branching. |
| [`!MATCH`](./control.md#match) | mapping | control | Pattern matching. |
| [`!TRY`](./control.md#try) | sequence | control |  Execute till first non-error expression. |
| [`!MAP`](./control.md#map) | mapping | control |  Apply the expression on each element in a sequence. |
| [`!REDUCE`](./control.md#reduce) | mapping | control |  Reduce the elements of an list into a single value. |
| [`!INCLUDE`](./directives.md#include) | scalar | directives | Inserts the content of another file. |
| [`!ARGUMENT`](./function.md#argument-arg) | scalar | function | Gets a function argument. |
| [`!ARG`](./function.md#argument-arg) | scalar | function | Gets a function argument. |
| [`!FUNCTION`](./function.md#function-fn) | mapping | function | Defines a new function. |
| [`!FN`](./function.md#function-fn) | mapping | function | Defines a new function. |
| [`!SELF`](./function.md#self) | mapping | function | Applies the current function, used for recursion. |
| [`!IP.FORMAT`](./ip.md#ipformat) | mapping | ip | Converts an IP address into a string. |
| [`!IP.INSUBNET`](./ip.md#ipinsubnet) | mapping | ip | Check if IP address falls into a subnet. |
| [`!GET`](./json.md#get) | mapping | json | Gets a single value from JSON. |
| [`!JSON.PARSE`](./json.md#jsonparse) | mapping | json | Parses JSON. |
| [`!LIST`](./list.md#list) | mapping | list |  Creates a list of items. |
| [`!GET`](./list.md#get) | mapping | list | Gets a single item from a list. |
| [`!AND`](./logic.md#and) | sequence | logic |  Conjunction. |
| [`!OR`](./logic.md#or) | sequence | logic | Disjunction. |
| [`!NOT`](./logic.md#not) | sequence | logic | Negation. |
| [`!LOOKUP`](./lookup.md#lookup) | mapping | lookup | Creates a new lookup. |
| [`!GET`](./lookup.md#get) | mapping | lookup | Gets items from a lookup. |
| [`IN`](./lookup.md#in) | mapping | lookup | Checks if an item is in a lookup. |
| [`!RECORD`](./record.md#record) | mapping | record |  A collection of named items. |
| [`!GET`](./record.md#get) | mapping | record |  Gets the item from a record. |
| [`!REGEX`](./regex.md#regex) | | regex | Regular expression search. |
| [`!REGEX.REPLACE`](./regex.md#regexreplace) | mapping | regex | Regular expression replace. |
| [`!REGEX.SPLIT`](./regex.md#regexsplit) | mapping | regex | Split a string by a regular expression. |
| [`!REGEX.FINDALL`](./regex.md#regexfindall) | mapping | regex | Find all occurrences by a regular expression. |
| [`!REGEX.PARSE`](./regex.md#regexparse) | mapping | regex | Parse by a regular expression. |
| [`!SET`](./set.md#set) | mapping | set | Set of items. |
| [`!IN`](./set.md#in) | mapping| set | Membership test. |
| [`!IN`](./string.md#in) | mapping | string | Tests if a string contains a substring. |
| [`!STARTSWITH`](./string.md#startswith) | mapping | string | Tests whether a string starts with a selected prefix. |
| [`!ENDSWITH`](./string.md#endswith) | mapping | string | Tests whether a string ends with a selected suffix. |
| [`!SUBSTRING`](./string.md#substring) | mapping | string | Extracts part of a string. |
| [`!LOWER`](./string.md#lower) | mapping | string | Transforms a string into lowercase. |
| [`!UPPER`](./string.md#upper) | mapping | string | Transforms a string into  uppercase. |
| [`!CUT`](./string.md#cut) | mapping | string | Cuts the string and returns a selected part. |
| [`!SPLIT`](./string.md#split) | mapping | string | Splits a string into a list. |
| [`!RSPLIT`](./string.md#rsplit) | mapping | string | Splits a string from right into a list. |
| [`!JOIN`](./string.md#join) | mapping | string | Joins a list of strings. |
| [`!TUPLE`](./tuple.md#tuple) | mapping | tuple |  A collection of items. |
| [`!GET`](./tuple.md#get) | mapping | tuple |  Get item from a tuple. |
| [`!CAST`](./utility.md#cast) | mapping | utility | Converts type of the argument into another. |
| [`!HASH`](./utility.md#hash) | mapping | utility | Calculates a digest. |
| [`!DEBUG`](./utility.md#debug) | mapping | utility | Debugs the expression. |
