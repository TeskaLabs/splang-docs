---
layout: default
title: SP-Lang Documentation
---

# SP-Lang language design


## Properties

 * <a href="https://en.wikipedia.org/wiki/Declarative_programming">Declarative</a>
 * <a href="https://en.wikipedia.org/wiki/Functional_programming">Functional</a>
 * <a href="https://en.wikipedia.org/wiki/Strong_and_weak_typing">Strongly typed</a>
 * <a href="https://en.wikipedia.org/wiki/Type_inference">Type inference</a>
 * Compiled by <a href="https://llvm.org/">LLVM</a>
 * Interpreted in <a href="https://www.python.org">Python</a>
 * Syntax is based on <a href="https://yaml.org/">YAML</a>


## Declarative

Most computer languages are imperative.
This means that most of the code goes towards explaining to the computer how to execute some task.
SP-Lang, on the other hand, is declarative.
The maker describes “what” they want their logic to do, not exactly “how” or “when” it is to be done.
Then the compiler will figure out how to do it.
This allows the compiler to heavily optimize by deferring work until needed, pre-fetching and reusing cached data, etc.

## Functional

SP-Lang favors pure functions without side effects.
This results in logic, which is easier to understand and gives the compiler the most freedom to optimize.

### Employed techniques

 * Static Single Assignment
 * Reduction thru syntax tree


## Stateless

There is no state to modify, and therefore are no variables, just constants.
You pass data through various expressions to build the final result.


## Strongly typed

The types of all the values are known at compile time.
This allows for the early detection of errors and reinforc optimizations.


## Type inference

Types are derived from their use without being declared.
For example, setting a variable to a number results in that variable's type being established as a number.
This further reduces a complexity for a maker without any performance sacrifice known from interpretted languages.


## Turing completeness

SP-Lang is designed to be [Turing complete](https://en.wikipedia.org/wiki/Turing_completeness).



