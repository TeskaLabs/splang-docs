---
git_commit_hash: b55fa3f
title: Směrnice
---

# Směrnice


!!! note

	
	
	
	Směrnice SP-Lang jsou při kompilaci rozšířeny. Nejsou to výrazy.
	

--- 

## `!INCLUDE`: Vložte obsah jiného souboru 

Typ: Typ: Skalární, Směrnice.

Direktiva `!INCLUDE` slouží k vložení obsahu daného souboru do aktuálního souboru.
Pokud není includovaný soubor nalezen, SP-Lang zobrazí chybu.


### Synopse
```yaml

!INCLUDE <filename>
```

`Jméno souboru` je název souboru v knihovně, který má být zahrnut.

Může to být:

* absolutní cesta začínající na `/` z kořene knihovny,
* relativní cesta k umístění souboru obsahujícího příkaz `!INCLUDE`
  
Přípona `.yaml` je nepovinná a bude přidána ke jménu souboru, pokud chybí.

### Příklad
```yaml

!INCLUDE other_file.yaml
```

Jedná se o jednoduché začlenění souboru `other_file.yaml`.
  
```yaml

!MATCH
what: !GET {...}
with:
  'group1': !INCLUDE inc_group1
  'group2': !INCLUDE inc_group2
```

V tomto příkladu se `!INCLUDE` používá k rozkladu většího výrazu na logicky oddělené soubory.
