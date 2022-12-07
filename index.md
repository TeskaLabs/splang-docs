---
layout: default
title: SP-Lang Documentation
---

# SP-Lang Documentation

Welcome to the documentation for SP-Lang. SP-Lang stands for _Stream Processing Language_.
SP-Lang is designed to be intuitive and easy to use language, even for people who don't have experience with programming.
We strive to make it as simple to use as spreadsheet macros or SQL, allowing you to perform powerful data processing tasks with minimal effort.

The key goal of SP-Lang is that it does a lot of the heavy lifting for you, so you can focus on what you want to accomplish rather than worrying about the details of how to implement it.
This low-code approach means that you can get up and running quickly, without having to learn a lot of complex programming concepts.

We hope that this documentation will provide you with all the information you need to get started with our language and start taking advantage of its powerful stream processing capabilities. Thank you for choosing our language, and we look forward to seeing what you can accomplish with it!

<img src="splang-logo.jpg" alt="SP-lang logo" style="width: 128px;" />

_SP-Lang_ is a [functional language](https://en.wikipedia.org/wiki/Functional_programming) that uses the [YAML](https://en.wikipedia.org/wiki/YAML) syntax.

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
