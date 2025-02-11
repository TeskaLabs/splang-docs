---
title: Design
---

# SP-Lang language design

## Properties

* [📜 Declarative language](https://en.wikipedia.org/wiki/Declarative_programming)
* [🔗 Functional language](https://en.wikipedia.org/wiki/Functional_programming)
* [🔀 Stateless language](https://en.wikipedia.org/wiki/Static_single-assignment_form)
* [🔐 Strongly typed language](https://en.wikipedia.org/wiki/Strong_and_weak_typing)
* [💡 Type inference](https://en.wikipedia.org/wiki/Type_inference)
* Syntax is based on [YAML](https://yaml.org/)

!!! question "Compiled or interpreted"
    SP-Lang is both:

    * Compiled by <a href="https://llvm.org/">LLVM</a>
    * Interpreted in <a href="https://www.python.org">Python</a>

## 📜 Declarative

Most computer languages are imperative.
This means that most of the code goes towards explaining to the computer how to execute some task.
SP-Lang, on the other hand, is declarative.
The maker describes “what” they want their logic to do, not exactly “how” or “when” it is to be done.
Then the compiler will figure out how to do it.
This allows the compiler to heavily optimize by deferring work until needed, pre-fetching and reusing cached data, etc.

## 🔗 Functional

SP-Lang favors pure functions without side effects.
This results in logic, which is easier to understand and gives the compiler the most freedom to optimize.

## 🔀 Stateless

There is no state to modify, and therefore are no variables, just constants.
You pass data through various expressions to build the final result.

!!! info "More information"

    * [Static Single Assignment](https://en.wikipedia.org/wiki/Static_single-assignment_form)
    * [Persistent Data Structures](https://en.wikipedia.org/wiki/Persistent_data_structure)

## 🔐 Strongly typed

The types of all the values are known at compile time.
This allows for the early detection of errors and reinforce optimizations.

## 💡 Type inference

Types are derived from their use without being declared.
For example, setting a variable to a number results in that variable's type being established as a number.
This further reduces a complexity for a maker without any performance sacrifice known from interpreted languages.

For advanced users who require more control over the type system, the SP-Lang provide mechanisms to explicitly specify types or interact with the [type system](../language/types/index.md) when necessary.
This flexibility allows advanced users to fine-tune their code for maximum performance and reliability, while still benefiting from the convenience of type inference.

## 🎓Turing completeness

SP-Lang is designed to be [Turing complete](https://en.wikipedia.org/wiki/Turing_completeness).
