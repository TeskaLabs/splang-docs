---
layout: default
title: SP-Lang Documentation
---

# SP-Lang

This is the official documentation for SP-Lang. SP-Lang stands for _Stream Processing Language_.


## Purpose of the language

SP-Lang is aimed at people who don’t program, with a comparable simplicity to, e.g. spreadsheet macros.
SP-Lang tries to do as much heavy lifting transparently for the user as possible.

It is a simple language for various [streaming](https://en.wikipedia.org/wiki/Event_stream_processing) tasks such as parsing of logs or other events, data filtering, enrichment, correlations and so on.

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


## Made with ❤️ by TeskaLabs

SP-Lang is the technology built at [TeskaLabs](https://www.teskalabs.com).  
