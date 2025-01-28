---
title: Tutorial
---

# SP-Lang Tutorial

## Introduction

Welcome to the SP-Lang tutorial.
SP-Lang, short for _Stream Processing Language_, is a domain-specific language (DSL).
It's based on YAML, a human-readable data serialization language.
This tutorial aims to introduce the basic elements of SP-Lang.

## Hello World

Let's get started with a simple example:

```yaml
---
Hello world!
```

In SP-Lang, the triple dashes (`---`) signal the start of the code.

`Hello world!` here is a value that you want to return.
In this case, it's our friendly "Hello world!" greeting.

## SP-Lang is based on YAML

SP-Lang is built on the [YAML (Yet Another Markup Language)](https://yaml.org).
YAML emphasizes simplicity and readability, making it a great foundation for SP-Lang.

!!! important

    YAML relies heavily on indentation, which is significant in its syntax.
    As a best practice, we recommend using two spaces for indentation.
    Do note that TABs are not supported in YAML.


## Comments

As you progress with writing your code, it's beneficial to leave comments.
This makes it easier for others (and your future self) to understand what your code does.


```yaml
---
# This is a comment.
Hello world!
```

Comments in SP-Lang begin with a `#`.
SP-Lang ignores anything that follows the `#` on the same line, making it useful for adding notes or describing the code.


## SP-Lang Expressions

Expressions in SP-Lang are commands that perform operations. Let's look at an arithmetic example:

This code sums two numbers, specifically it calculates `5+8`.


```yaml
---
!ADD
- 5
- 8
```

The above expression sums two numbers, `5` and `8`, to get the result `13`.

Expressions in SP-Lang start with an exclamation mark (`!`).


!!! tip

    The term "Expression" is an alternative term for a function.


In this example, `!ADD` is the expression for arithmetic addition that sums up the provided numbers.

The numbers you want to add are provided as a list because `!ADD` is a Sequence expression.
This means that it can sum multiple input values:

```yaml
---
!ADD
- 5
- 8
- 9
- 15
```

This list of input values is created using a dash `-` at the beginning of the line containing the value.
Each line represents an individual item in the list.

You can also write expressions in a more concise way using the flow form, which can be freely combined with the default style of SP-Lang code:

```yaml
---
!ADD [5, 8, 9, 15]
```


## Mapping expressions

Another type of expression is a _mapping expression_.
Instead of a list of inputs, mapping expressions use input names, which can be found in the expression's documentation.

```yaml
---
!ENDSWITH
what: "FooBar"
postfix: "Bar"
```

The `!ENDSWITH` expression checks whether the value of the input `what` ends with the value of the input `postfix`. It returns `true` if it does, and `false` if it doesn't.

The flow form can also be used with mapping expressions:

```yaml
---
!ENDSWITH {what: "FooBar", postfix: "Bar"}
```

## Compose expressions

SP-Lang lets you combine expressions to create more complex and powerful solutions.
You can "plug" the output of one expression into the input of another.

```yaml
---
!MUL
- 5
- !ADD [6, 2, 3]
- 9
- !SUB [10, 5]
```

This example is equivalent to the arithmetic operation `5 * (6 + 2 + 3) * 9 * (10 - 5)`.


## Arguments

Arguments are how data is passed into SP-Lang.
Depending on the context of the call, an expression can have zero, one, or more arguments.
Each argument has a unique name.

You can access vale of the argument by `!ARG` expression.

In the following example, the prescribed argument for the expression is `name`:

```yaml
---
!ADD ["Hi ", !ARG name, "!"]
```

This would take the value of name and insert it into the string, forming a personalized greeting.


## Conclusion

In this tutorial, we've covered the basics of SP-Lang, including how to write simple expressions, compose expressions, and use arguments.
With these basics, you're ready to start exploring more complex policy definitions in SP-Lang.
As you continue, remember to make ample use of the documentation to understand the various expressions and their required inputs.

Happy coding!
