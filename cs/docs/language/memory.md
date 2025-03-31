---
title: Správa paměti
---

# Správa paměti

Správa paměti v SP-Langu je založena na konceptu paměťových arén - [memory arenas](https://en.wikipedia.org/wiki/Region-based_memory_management).

<img src="../memory-arena.svg" alt="Schéma paměťové arény"/>

_Diagram: Rozložení paměťových arén_

Paměťová aréna je předem alokovaný větší kus paměti, který je k dispozici pro daný životní cyklus (tj. jeden cyklus zpracování události).
Když nějaký kód související se zpracováním událostí potřebuje paměť, požádá o kousek z paměťové arény.
Tento kousek je poskytnut rychle, protože je vždy odebrán ze začátku volného místa v aréně (tzv. offset).
Rozdělení proběhne najednou pro celou arénu. Mluvíme o tzv. "resetu" paměťové arény.
To znamená, že koncept paměťové arény je velmi efektivní, nezavádí fragmentaci paměti a dobře se kombinuje s konceptem statického jedinečného přiřazení SP-Langu.

Paměťová aréna také podporuje seznam destruktorů, který umožňuje integraci s tradičními např. `malloc` alokacemi pro technologie třetích stran, které nejsou kompatibilní s paměťovou arénou (např. knihovna PCRE2).
Destruktory se provádějí při resetu arény.

Paměťová aréna může být rozšířena o další paměťový chunk, pokud je aktuální chunk vyčerpán.