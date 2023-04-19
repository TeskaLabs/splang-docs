---
title: Tutorial
---

# SP-Lang Tutorial


## Hello World

Let's start with the simplest example:

```yaml
---
Hello world!
```

Three dashes (`---`) signal a start of the code.

`Hello world!` is a value that you want to return.


## SP-Lang is based on YAML

The SP-Lang is based in the <a href="https://yaml.org">YAML</a>.
The YAML relays heavily on indentation, we recommend to use two spaces, TABs are not supported by YAML.


## Comments

It is a good habit to comment the work.


```yaml
# Hello world in the SP-Lang
---
Hello world!
```


## SP-Lang expressions

This code sums two numbers, specifically it calculates `5+8`.


```yaml
---
!ADD
- 5
- 8
```

The result is `13`.


All SP-Lang expressions starts with `!`.

_Hint: "Expression" is just an alternative term to "function"._ 

`!ADD` is the _expression_ for arithmetic *addition* that can sum provided numbers.

Values for `!ADD` _expression_ are provided as a list, because `!ADD` is so called _Sequence expression_.
It means that it can sum multiple input values:

```yaml
---
!ADD
- 5
- 8
- 9
- 15
```

The list of input values is specified using `- ` in the beginning of the line with the value.
Every line represents an individual item from a list.

You can also use a more concise way of expression notation.
It is called _flow form_ and it can be freely combined with the default style of SP-Lang code:


```yaml
---
!ADD [5, 8, 9, 15]
```


## Mapping expressions

Other type of expressions are called _mapping expressions_.

Instead of list of inputs, you use names of inputs.
These names could be found in the documentation of the expression.

```yaml
---
!ENDSWITH
what: "FooBar"
postfix: "Bar"
```

The `!ENDSWITH` expression tests if the value of an input `what` ends with value of the input `postfix`.
It returns `true` or `false`.

You can also use a _flow form_ for the same expression:

```yaml
---
!ENDSWITH {what: "FooBar", postfix: "Bar"}
```

## Combining expressions

You can combine expressions together to create more powerful solution to your problem.
You simply "plug" output of one expression into an input of other expression.

```yaml
---
!MUL
- 5
- !ADD [6, 2, 3]
- 9
- !SUB [10, 5]
```

This example is equivalent to `5 * (6 + 2 + 3) * 8 * (10 - 5)`.


## Arguments

Arguments are the way, how data are passed into SP-Lang.
Expression can have zero, one or more arguments, depending on the context of the call.
Each argument has its unique name.

You can access vale of the argument by `!ARG` or its longer equivalent `!ARGUMENT`.

Prescribed argument for following expression is a `name`:

```yaml
---
!ADD ["Hi ", !ARG name, "!"]
```
