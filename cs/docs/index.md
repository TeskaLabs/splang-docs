---
git_commit_hash: b55fa3f
title: Vítejte!
---

# Dokumentace SP-Langu

Vítejte u dokumentace SP-Langu. SP-Lang je zkratka pro _Stream Processing Language_.
SP-Lang je navržen jako intuitivní a snadno použitelný jazyk i pro lidi, kteří nemají zkušenosti s programováním.
Snažíme se, aby jeho používání bylo stejně jednoduché jako používání maker v tabulkovém procesoru nebo jazyka SQL, což vám umožní provádět výkonné úlohy zpracování dat s minimálním úsilím.

Hlavním cílem jazyka SP-Lang je, aby za vás udělal mnoho těžké práce, takže se můžete soustředit na to, čeho chcete dosáhnout, a ne se starat o detaily, jak to realizovat.
Tento nízkoúrovňový přístup vám umožní rychle začít pracovat, aniž byste se museli učit spoustu složitých programovacích konceptů.

Doufáme, že vám tato dokumentace poskytne všechny informace, které potřebujete k tomu, abyste mohli začít pracovat s naším jazykem a začít využívat jeho výkonné možnosti proudového zpracování. Děkujeme, že jste si vybrali náš jazyk, a těšíme se na to, co s ním dokážete!


!!! quote "Vyrobeno s :octicons-heart-fill-24:{ .heart } v TeskaLabs"

	
	
	SP-Lang je technologie vytvářená ve společnosti [TeskaLabs](https://www.teskalabs.com).  
	

<!-- <img src="splang-logo.jpg" alt="SP-lang logo" style="width: 128px;" /> -->


## Úvod

_SP-Lang_ je [funkcionální jazyk](https://cs.wikipedia.org/wiki/Funkcionální_programování), který používá syntaxi [YAML](https://cs.wikipedia.org/wiki/YAML).

SP-Lang poskytuje velmi vysoký výkon, protože je zkompilován do [strojového kódu](https://cs.wikipedia.org/wiki/Strojový_kód).
To mu spolu s rozsáhlými optimalizacemi dává výkon srovnatelný s jazyky jako jsou C, Go nebo Rust; tedy nejvýše dosažitelný.

Z tohoto důvodu je SP-Lang přirozeným kandidátem na nákladově efektivní zpracování masivních datových toků v cloudu nebo v on-premise aplikacích.


!!! example "Hello world! v jazyce SP"

	```yaml
	!ADD
	- Hello
	- " "
	- world
	- "!"
	```


!!! example "Stejný příklad ve vizuální podobě SP-Langu"


	<img src="visual-hello-world.jpg" alt="Visual Hello world in SP-Lang" style="width: 197px;" />

**Pro první seznámení s jazykem SP-Lang vyzkoušejte náš [tutoriál](./tutorial.md).**

## Vlastnosti jazyka SP-Lang

* [📜 Deklarativní jazyk](https://cs.wikipedia.org/wiki/Deklarativní_programování)
* [🔗 Funkcionální jazyk](https://cs.wikipedia.org/wiki/Funkcionální_programování)
* [🔐 Silně typovaný](https://en.wikipedia.org/wiki/Strong_and_weak_typing)
* [💡 Typová inference](https://cs.wikipedia.org/wiki/Typová_inference)
* 🐍 Interpretován v jazyce Python
* 🚀 Kompilován pomocí [LLVM](https://llvm.org/)
* Syntaxe je založena na [YAML](https://en.wikipedia.org/wiki/YAML)
