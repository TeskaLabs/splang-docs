---
layout: default
title: SP-Lang Documentation
---

# SP-Lang

This is the official documentation for SP-Lang. SP-Lang stands for _Stream Processing Language_.

_SP-Lang_ is a [functional language](https://en.wikipedia.org/wiki/Functional_programming) that uses the [YAML](https://en.wikipedia.org/wiki/YAML) syntax.

<img src="splang-logo.jpg" alt="SP-lang logo" style="width: 128px;" />


## Purpose of the language

SP-Lang is aimed at people who don’t program, with a comparable simplicity to, e.g. spreadsheet macros or SQL.
SP-Lang tries to do as much heavy lifting transparently for the user as possible.
SP-Lang is a low-code language.

It is a simple language for various [data stream processing](https://en.wikipedia.org/wiki/Event_stream_processing) tasks such as parsing of logs or other events, data filtering, enrichment, correlations and so on.

SP-Lang delivers very high performance because it is compiled to <a href="https://en.wikipedia.org/wiki/Machine_code">the machine code<a>.
This, together with extensive optimizations, gives the performance in the same category as C, Go or Rust; respective the highest possible performance.

For that reason, SP-Lang is a natural candidate for a cost-effective processing of the massive data streams in the cloud or on‑premise applications.


## Hello world!

This is the simple example of "Hello world" expression in SP-Lang:


```yaml
!ADD [Hello, " ", world, "!"]
```

And the same example in the visual SP-Lang:

<img src="visual-hello-world.jpg" alt="Visual Hello world in SP-Lang" style="width: 197px;" />


Your first steps with SP-Lang start [here](tutorial).

## Important features
  
 * [Functional](https://en.wikipedia.org/wiki/Functional_programming)
 * [Declarative](https://en.wikipedia.org/wiki/Declarative_programming)
 * [Strongly typed](https://en.wikipedia.org/wiki/Strong_and_weak_typing)
 * [Type inference](https://en.wikipedia.org/wiki/Type_inference)
 * Interpreted in Python
 * Compiled by [LLVM](https://llvm.org/)
 * Syntax is based on [YAML](https://en.wikipedia.org/wiki/YAML)
  

## Made with ❤️ by TeskaLabs

SP-Lang is the technology built at [TeskaLabs](https://www.teskalabs.com).  
