---
git_commit_hash: b55fa3f
title: Direktivy
---

# Direktivy

!!! note

    Direktivy SP-Lang jsou při kompilaci rozšířeny. Nejsou to výrazy.


--- 

## `!INCLUDE`: Vloží obsah jiného souboru

Typ: Skalární, Direktiva.

Direktiva `!INCLUDE` slouží k vložení obsahu daného souboru do aktuálního souboru.
Pokud není vkládaný soubor nalezen, SP-Lang zobrazí chybu.


Synopsis:

```yaml
!INCLUDE <filename>
```

`filename` je název souboru v knihovně, který má být vložen.

Můžeme ho specifikovat pomocí:

* absolutní cesty začínající na `/` z kořene knihovny,
* relativní cesty k umístění souboru obsahujícího příkaz `!INCLUDE`
  
Přípona `.yaml` je nepovinná a bude přidána ke jménu souboru, pokud chybí.

!!! example "Příklad"

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
