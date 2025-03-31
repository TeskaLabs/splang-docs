---
title: Tutoriál
---

# Tutoriál k SP-Langu

## Úvod

Vítejte u tutoriálu k SP-Langu.
SP-Lang, zkratka pro _Stream Processing Language_, je doménově specifický jazyk (DSL).
Je založen na YAML, člověkem čitelném jazyku pro serializaci dat.
Cílem tohoto tutoriálu je představit základní prvky jazyka SP-Lang.

## Hello World

Začneme jednoduchým příkladem:

```yaml
---
Hello world!
```

V jazyce SP-Lang signalizují trojité pomlčky (`---`) začátek kódu.

`Hello world!` zde je hodnota, kterou chcete vrátit.
V tomto případě je to náš přátelský pozdrav "Hello world!".

## SP-Lang je založen na YAMLu

SP-Lang je postaven na [YAML (Yet Another Markup Language)](https://yaml.org).
YAML klade důraz na jednoduchost a čitelnost, což z něj činí skvělý základ pro SP-Lang.

!!! important

    Jazyk YAML ve velké míře stojí na odsazování, které je významné v jeho syntaxi.
    Jako osvědčený postup doporučujeme používat pro odsazení dvě mezery.
    Upozorňujeme, že v jazyce YAML nejsou podporovány znaky TAB.

## Komentáře

Při psaní kódu je užitečné zanechávat komentáře.
Usnadníte tak ostatním (a svému budoucímu já) pochopit, co váš kód dělá.

```yaml
---
# Toto je komentář.
Hello world!
```

Komentáře v SP-Langu začínají znakem `#`.
SP-Lang ignoruje vše, co následuje za `#` na stejném řádku, což je užitečné pro přidávání poznámek nebo popisování kódu.

## Výrazy SP-Lang

Výrazy v jazyce SP-Lang jsou příkazy, které provádějí operace. Podívejme se na příklad s aritmetickými výrazy:

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

Výrazy můžete psát také stručněji pomocí "flow formy", kterou lze libovolně kombinovat s výchozím stylem kódu SP-Lang:

```yaml
---
!ADD [5, 8, 9, 15]
```

## Mapovací výrazy

Dalším typem výrazu je _mapovací výraz_.
Namísto seznamu vstupů používají mapovací výrazy jména vstupů, která lze nalézt v dokumentaci výrazu.

```yaml
---
!ENDSWITH
what: "FooBar"
postfix: "Bar"
```

Výraz `!ENDSWITH` kontroluje, zda hodnota zadaná na vstupu `what` končí hodnotou zadanou na vstupu `postfix`. Pokud ano, vrátí `true`, pokud ne, vrátí `false`.

I na mapovací výrazy lze použít flow formu:

```yaml
---
!ENDSWITH {what: "FooBar", postfix: "Bar"}
```

## Skládání výrazů

SP-Lang umožňuje kombinovat výrazy a vytvářet tak složitější a výkonnější řešení.
Výstup jednoho výrazu můžete vzít za základ pro vstup do jiného výrazu.

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

Argumenty jsou způsob, jakým do jazyka SP-Lang předáváme data.
V závislosti na kontextu volání může mít výraz žádný, jeden nebo více argumentů.
Každý argument má jedinečné jméno.

K hodnotě argumentu můžete přistupovat pomocí výrazu `!ARG`.

V následujícím příkladu je argumentem výraz `name`:

```yaml
---
!ADD ["Hi ", !ARG name, "!"]
```

Tento výraz bere hodnotu `name` a vloží ji do řetězce, čímž se vytvoří pozdrav.

## Závěr

V tomto tutoriálu jsme se seznámili se základy jazyka SP-Lang, včetně toho, jak psát jednoduché výrazy, složené výrazy a jak používat argumenty.
S těmito základy jste připraveni začít prozkoumávat složitější definice v jazyce SP-Lang.
Při dalším pokračování nezapomeňte hojně využívat dokumentaci, abyste porozuměli různým výrazům a jejich požadovaným vstupům.

Mnoho zdaru při programování!