---
title: Parsec
---

# PARSEC výrazy

Skupina Parsec výrazů představuje koncept [parser combinator](https://en.wikipedia.org/wiki/Parser_combinator).

Poskytují způsob, jak kombinovat základní parsery za účelem konstrukce složitějších parserů pro specifická pravidla. V tomto kontextu **parser** je funkce, která přijímá jediný řetězec jako vstup a produkuje strukturovaný výstup, který indikuje úspěšné zpracování nebo poskytuje chybovou zprávu, pokud proces zpracování selže.

Parsec výrazy jsou rozděleny do dvou skupin: parsery a kombinátory.

[**Parsers**](./parser.md) mohou být považovány za základní jednotky nebo stavební bloky. Jsou odpovědné za rozpoznávání a zpracování specifických vzorců nebo prvků v rámci vstupního řetězce.

[**Combinators**](./combinator.md) jsou operátory (funkce vyššího řádu), které umožňují kombinaci a skládání parserů.

Každý výraz začíná prefixem ```!PARSE.```