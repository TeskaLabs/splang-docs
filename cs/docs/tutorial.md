---
git_commit_hash: b55fa3f
title: Výukový program
---

# Výukový program SP-Lang


## Úvod

Vítejte ve výukovém programu SP-Lang.
SP-Lang, zkratka pro _Stream Processing Language_, je doménově specifický jazyk (DSL).
Je založen na YAML, člověkem čitelném jazyku pro serializaci dat.
Cílem tohoto tutoriálu je představit základní prvky jazyka SP-Lang. 


## Hello World

Začneme jednoduchým příkladem:
```yaml

---
Ahoj světe!
```

V jazyce SP-Lang signalizují trojité pomlčky (`---`) začátek kódu.

`Hello world!` zde je hodnota, kterou chcete vrátit.
V tomto případě je to náš přátelský pozdrav "Hello world!".


## SP-Lang je založen na YAMLu

SP-Lang je postaven na <a href="https://yaml.org">YAML</a> (Yet Another Markup Language).
YAML klade důraz na jednoduchost a čitelnost, což z něj činí skvělý základ pro SP-Lang.

!!! important

	
	
	
	Jazyk YAML se ve velké míře spoléhá na odsazení, které je v jeho syntaxi významné.
	Jako osvědčený postup doporučujeme používat pro odsazení dvě mezery.
	Upozorňujeme, že v jazyce YAML nejsou podporovány znaky TAB.
	
	

## Komentáře

Jak postupujete při psaní kódu, je užitečné zanechávat komentáře.
Usnadníte tak ostatním (a svému budoucímu já) pochopit, co váš kód dělá.

```yaml

# Toto je komentář.
---
Ahoj světe!
```

Komentáře v SP-Langu začínají znakem `#`.
SP-Lang ignoruje vše, co následuje za `#` na stejném řádku, což je užitečné pro přidávání poznámek nebo popisování kódu.


## Výrazy SP-Lang

Výrazy v jazyce SP-Lang jsou příkazy, které provádějí operace. Podívejme se na aritmetický příklad:

Tento kód sečte dvě čísla, konkrétně vypočítá `5+8`.

```yaml

---
!ADD
- 5
- 8
```

Výše uvedený výraz sečte dvě čísla, `5` a `8`, a získá výsledek `13`.

Výrazy v jazyce SP-Lang začínají vykřičníkem (`!`).


!!! tip

	
	
	
	Výraz "Expression" je alternativní výraz pro funkci.
	
	

V tomto příkladu je `!ADD` výraz pro aritmetické sčítání, které sečte zadaná čísla.

Čísla, která chcete sečíst, jsou zadána jako seznam, protože `!ADD` je výraz pro posloupnost.
To znamená, že může sčítat více vstupních hodnot:
```yaml

---
!ADD
- 5
- 8
- 9
- 15
```

Tento seznam vstupních hodnot je vytvořen pomocí pomlčky `-` na začátku řádku obsahujícího hodnotu.
Každý řádek představuje jednotlivou položku seznamu.

Výrazy můžete psát také stručněji pomocí formuláře flow, který lze libovolně kombinovat s výchozím stylem kódu SP-Lang:
```yaml

---
!ADD [5, 8, 9, 15]
```


## Mapování výrazů

Dalším typem výrazu je _mapovací výraz_.
Namísto seznamu vstupů používají mapovací výrazy jména vstupů, která lze nalézt v dokumentaci výrazu.
```yaml

---
!ENDSWITH
what: "FooBar"
postfix: "Bar"
```

Výraz `!ENDSWITH` kontroluje, zda hodnota vstupu `what` končí hodnotou vstupu `postfix`. Pokud ano, vrátí `pravdu`, pokud ne, vrátí `nepravdu`.

Formulář flow lze použít také s mapovacími výrazy:
```yaml

---
!ENDSWITH {what: "FooBar", postfix: "Bar"}
```

## Kompozice výrazů

SP-Lang umožňuje kombinovat výrazy a vytvářet tak složitější a výkonnější řešení.
Výstup jednoho výrazu můžete "zapojit" do vstupu jiného výrazu.
```yaml

---
!MUL
- 5
- !ADD [6, 2, 3]
- 9
- !SUB [10, 5]
```

Tento příklad je ekvivalentní aritmetické operaci `5 * (6 + 2 + 3) * 9 * (10 - 5)`.


## Argumenty

Argumenty jsou způsob, jakým jsou data předávána do jazyka SP-Lang.
V závislosti na kontextu volání může mít výraz nula, jeden nebo více argumentů.
Každý argument má jedinečné jméno.

K hodnotě argumentu můžete přistupovat pomocí výrazu `!ARG`.

V následujícím příkladu je předepsaným argumentem výrazu `jméno`:
```yaml

---
!ADD ["Hi ", !ARG name, "!"]
```

To by vzalo hodnotu jména a vložilo ji do řetězce, čímž by se vytvořil osobní pozdrav.


## Závěr

V tomto tutoriálu jsme se seznámili se základy jazyka SP-Lang, včetně toho, jak psát jednoduché výrazy, skládat výrazy a používat argumenty.
S těmito základy jste připraveni začít zkoumat složitější definice zásad v jazyce SP-Lang.
Při dalším pokračování nezapomeňte hojně využívat dokumentaci, abyste porozuměli různým výrazům a jejich požadovaným vstupům.

Šťastné kódování!
