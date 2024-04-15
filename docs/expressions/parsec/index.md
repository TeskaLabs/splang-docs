---
title: Parsec
---

# PARSEC expressions

Parsec expressions group represents the concept of [parser combinator](https://en.wikipedia.org/wiki/Parser_combinator).

They provide a way to combine basic parsers in order to construct more complex parsers for specific rules.
In this context, **a parser** is a function that takes a single string as input and produces a structured output,
that indicates successful parsing or provide an error message if the parsing process fails.

Parsec expressions are divided into two groups: parsers and combinators.

**Parsers** can be seen as the fundamental units or building blocks. They are responsible for recognizing and processing specific patterns or elements within the input string.

**Combinators** are operators (higher order functions) that allow the combination and composition of parsers.

Every expression starts with `!PARSE.` prefix.

