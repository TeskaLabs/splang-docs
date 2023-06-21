---
git_commit_hash: b55fa3f
title: Syntaxe
---

# Syntaxe jazyka SP


!!! info


		Syntaxe SP-Lang používá [YAML 1.2](https://yaml.org/spec/1.2)


## Komentáře

Komentář je označen indikátorem `#`. 
```yaml

# Tento soubor neobsahuje žádný SP-Lang
# Pouze komentáře.
```


## Čísla

### Celé číslo
```yaml

kanonický zápis: 12345
kladné desetinné číslo: +12345
záporné desetinné číslo: -12345
osmičkový zápis: 0o14
hexadecimální zápis: 0xC
```


### Plovoucí čárka
```yaml

pevný zápis: 1230.15
kanonický zápis: 1.23015e+3
exponenciální zápis: 12.3015e+02
záporné nekonečno: -.inf
není číslo: .nan
```


## Řetězce
```yaml
řetězec: '012345'
řetězec bez uvozovek: Řetězec můžete zadat i bez uvozovek.
emoji: 😀🚀⭐
```

Řetězce s uvozovkami:
```yaml

unicode: "\u263A"
control: "\b1998\t1999\t2000\n"
hexadecimální esc: "\x0d\x0a je \r\n"

singl: ""Nazdar!" zvolal.
citováno: # Not a ''comment''.
```

Víceřádkové řetězce:
```yaml
|
   _____ _____        _                       
  / ____|  __ \      | |                      
 | (___ | |__) |_____| |     __ _ _ __   __ _ 
  \___ \|  ___/______| |    / _` | '_ \ / _` |
  ____) | |          | |___| (_| | | | | (_| |
 |_____/|_|          |______\__,_|_| |_|\__, |
                                         __/ |
                                        |___/ 
```

Doslovný styl (označený `|`) zachovává počáteční mezery.
```yaml
>
  Mark McGwire's
  year was crippled
  by a knee injury.
```

Složený styl (označený `>`) odstraňuje případné odsazení YAML.


## Booleans
```yaml

True boolean: true
False boolean: false
```


## Výrazy

Všechny výrazy SP-Lang (alias funkce) začínají na `!`, výrazy SP-Lang jsou tedy _tagy_ YAML (`!TAG`).

Výrazy mohou být těchto typů:

 - _Mapování_
 - _Sequence_
 - _Skalární_


### Mapovací výraz

Příklad:
```yaml

!ENDSWITH
co: FooBar
postfix: Bar
```

Příklad _flow_ formuláře:
```yaml
!ENDSWITH {what: FooBar, postfix: Bar}
```


!!! abstract "Specifikace YAML"

	
	
	Viz kapitola [10.2. Styly mapování](https://yaml.org/spec/1.1/#id932806).
	
	

### Sekvenční výraz

Příklad:
```yaml

!ADD  
- 1 
- 2 
- 3 
```

Příklad formuláře _flow_:
```yaml

!ADD [1, 2, 3]  
```


!!! abstract "Specifikace YAML"

	
	
	Viz kapitola [10.1. Styly sekvencí](https://yaml.org/spec/1.1/#id931088).
	
	

Sekvenční výraz lze definovat také pomocí argumentu `with`:
```yaml

!ADD
with: [1, 2, 3]
```

!!! tip

	
	
	
	Jedná se vlastně o mapovací formu sekvenčního výrazu.
	
	
	

### Skalární výrazy

Příklad:  
```yaml

!ITEM EVENT brambory
```


!!! abstract "Specifikace YAML"


		Viz kapitola [9. Skalární styly](https://yaml.org/spec/1.1/#id903915)	

## Kotvy a aliasy

SP-Lang využívá YAML [kotvy](https://yaml.org/spec/1.1/#id899912) a [aliasy](https://yaml.org/spec/1.1/#id902561).
To znamená, že se můžete odkazovat na výsledek jiného výrazu pomocí _kotvy_.
Kotva je řetězec začínající znakem "`&`".
Výsledek výrazu anotovaného kotvou lze pak znovu použít pomocí _aliasu_, což je řetězec začínající na "`*`", který sdílí jméno kotvy.
Na jednu kotvu se může odkazovat více aliasů.

Příklad:
```yaml

!ADD
- 1
- &subcount !MUL
  - 2
  - 3
- *subcount
- *subcount
```

Rovná se `1+(2*3)+(2*3)+(2*3)` odpovídající `19`.


## Struktura souboru SP-Lang

SP-Lang používá tři pomlčky (`---`) k oddělení výrazů od obsahu dokumentu.
Slouží také k signalizaci začátku SP-Langu.
Tři tečky ("`...`") označují konec souboru bez začátku nového, pro použití v komunikačních kanálech.

Přípona souboru SP-Lang je `.yaml`.

Příklad souboru SP-Lang:


```yaml title="multiplication.yaml"
---
# Proveďme nějaké základní matematické výpočty
!MUL
- 1
- 2
- 3
```


!!! note

	
	
	
	Soubor SP-Lang vždy začíná řádkem `---`.
	
	

!!! info

	
	
	
	Jeden soubor může obsahovat více výrazů pomocí oddělovače YAML (`---`).

