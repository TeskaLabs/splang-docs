---
title: Design jazyka
---

# Design jazyka SP-Lang

## Vlastnosti

* [📜 Deklarativní jazyk](https://en.wikipedia.org/wiki/Declarative_programming)
* [🔗 Funkční jazyk](https://en.wikipedia.org/wiki/Functional_programming)
* [🔀 Bezstavový jazyk](https://en.wikipedia.org/wiki/Static_single-assignment_form)
* [🔐 Silně typovaný jazyk](https://en.wikipedia.org/wiki/Strong_and_weak_typing)
* [💡 Odvozování typů](https://en.wikipedia.org/wiki/Type_inference)
* Syntaxe je založena na [YAMLu](https://yaml.org/)

!!! question "Kompilace anebo interpretace"
    SP-Lang je:

    * jednak kompilován pomocí <a href="https://llvm.org/">LLVM</a>
    * druhak interpretován v jazyce <a href="https://www.python.org">Python</a>

## 📜 Deklarativní

Většina počítačových jazyků je imperativní.  
To znamená, že většina kódu směřuje k tomu, aby počítači vysvětlila, jak má provést nějakou úlohu.  
Naproti tomu SP-Lang je deklarativní.  
Tvůrce popisuje, "co" chce, aby jeho logika udělala, nikoliv přesně "jak" nebo "kdy" to má být provedeno.  
Překladač pak vymyslí, jak to provést.  
To kompilátoru umožňuje silně optimalizovat tím, že odkládá práci, dokud není potřeba, předem načítá a znovu používá data z mezipaměti atd.

## 🔗 Funkční

SP-Lang upřednostňuje čisté funkce bez vedlejších efektů.  
Výsledkem je logika, která je srozumitelnější a dává kompilátoru největší volnost při optimalizaci.

## 🔀 Bezstavový

Neexistuje žádný stav, který by bylo možné modifikovat, a proto nejsou žádné proměnné, pouze konstanty.  
Data procházíte různými výrazy a sestavujete konečný výsledek.

!!! info "Více informací"

    * [Statické jednoduché přiřazení](https://en.wikipedia.org/wiki/Static_single-assignment_form)
    * [Trvalé datové struktury](https://en.wikipedia.org/wiki/Persistent_data_structure)

## 🔐 Silně typovaný

Typy všech hodnot jsou známy v době kompilace.  
To umožňuje včasné odhalení chyb a posílení optimalizace.

## 💡 Podpora odvozování typů

Typy jsou odvozeny z jejich použití, aniž by byly deklarovány.  
Například nastavení proměnné na číslo vede k tomu, že typ této proměnné je stanoven jako číslo.  
To dále snižuje složitost pro tvůrce bez oběti na výkonu známé z interpretovaných jazyků.

Pro pokročilé uživatele, kteří vyžadují větší kontrolu nad typovým systémem, poskytuje SP-Lang mechanismy pro explicitní určení typů nebo interakci s [typovým systémem](../language/types/index.md) v případě potřeby.  
Tato flexibilita umožňuje pokročilým uživatelům vyladit svůj kód pro maximální výkon a spolehlivost a zároveň využívat pohodlí typové inference.

## 🎓 Turingovsky úplný

SP-Lang je navržen tak, aby byl [turingovsky úplný](https://en.wikipedia.org/wiki/Turing_completeness).