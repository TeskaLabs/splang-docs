---
title: Logika
---

# Logické výrazy

## Přehled

Logické výrazy se běžně používají k vytváření přísnějších a přesnějších podmínek, jako je filtrování událostí nebo spouštění konkrétních akcí na základě souboru kritérií. Logické výrazy pracují s pravdivostními hodnotami `true` a `false`.

!!! info "Logické výrazy jsou reprezentací logické algebry"

    Další informace naleznete na stránce [boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra) na Wikipedii.

* [`!AND`](#and): Konjunkce.
* [`!OR`](#or): Disjunkce.
* [`!NOT`](#not): Negace.

---

## `!AND`

Logický výraz `!AND` se používá ke spojení dvou nebo více podmínek, které musí být všechny pravdivé, aby byl celý výraz pravdivý. Používá se k vytváření přísnějších a přesnějších podmínek.

Typ: _Sequence_

Synopsis:

```yaml
!AND
- <condition 1>
- <condition 2>
- ...
```

V logickém výrazu `!AND` mohou být podmínky (`condition 1`, `condition 2`, ...) libovolné výrazy, které se vyhodnotí jako logická hodnota (true nebo false). Podmínky jsou vyhodnocovány shora dolů a proces vyhodnocování se zastaví, jakmile je nalezena nepravdivá podmínka, podle konceptu zkratového vyhodnocování.

!!! info "Logická konjunkce"

    Další informace naleznete na stránce [Logical conjunction](https://en.wikipedia.org/wiki/Logical_conjunction) na Wikipedii.

!!! example

    ```yaml
    !AND
    - !EQ
        - !ARG vendor
        - TeskaLabs
    - !EQ
        - !ARG product
        - LogMan.io
    - !EQ
        - !ARG version
        - v23.10
    ```

    V tomto příkladu, pokud se všechny podmínky vyhodnotí jako pravdivé, bude celý logický výraz `!AND` pravdivý. Pokud je některá z podmínek nepravdivá, bude logický výraz `!AND` nepravdivý.

### Bitové `!AND`

Pokud se `!AND` použije na celočíselné typy místo na logické, vytvoří se bitové AND.

!!! example

    ```yaml
    !AND
    - !ARG PRI
    - 7
    ```

    V tomto příkladu je argument `PRI` maskován číslem 7 (binárně `00000111`).

---

## `!OR`

Logický výraz `!OR` se používá ke spojení dvou nebo více podmínek, přičemž alespoň jedna z podmínek musí být pravdivá, aby byl celý výraz pravdivý. Používá se k vytváření flexibilnějších a komplexnějších podmínek.

Typ: _Sequence_

Synopsis:

```yaml
!OR
- <condition 1>
- <condition 2>
- ...
```

Podmínky (`condition 1`, `condition 2`, ...) mohou být libovolné výrazy, které se vyhodnotí jako logická hodnota (`true` nebo `false`). Podmínky jsou vyhodnocovány shora dolů a proces vyhodnocování se zastaví, jakmile je nalezena pravdivá podmínka, podle konceptu zkráceného vyhodnocování.

!!! info "Logická disjunkce"

    Další informace naleznete na stránce [Logical disjunction](https://en.wikipedia.org/wiki/Logical_disjunction) na Wikipedii.

!!! example

    ```yaml
    !OR
    - !EQ
        - !ARG description
        - neoprávněný přístup
    - !EQ
        - !ARG reason
        - hrubá síla
    - !EQ
        - !ARG message
        - Zjištěn malware
    ```

    V tomto příkladu je výraz pravdivý, pokud je splněna některá z následujících podmínek:

    1. Pole `description` odpovídá řetězci "unauthorized access".
    2. Pole `reason` odpovídá řetězci "brute force".
    3. Pole `message` odpovídá řetězci "malware detected".

### Bitové `!OR`

Pokud se `!OR` použije na celočíselné typy místo na logické, poskytuje bitové OR.

!!! example

    ```yaml
    !OR
    - 1  # Read access (binární 001, desítková 1)
    - 4  # Execute access (binární 100, desítkově 4)
    ```

    V tomto příkladu je výraz vyhodnocen jako 5.

    Je to proto, že při bitové operaci `!OR` se každý odpovídající bit v binární reprezentaci obou čísel kombinuje pomocí výrazu `!OR`:

    ```
    001 (přístup pro čtení)
    100 (přístup pro spuštění)
    ---
    101 (kombinovaná oprávnění)
    ```

    Výraz vypočítá oprávnění s výslednou hodnotou (binární 101, desítková 5) z operace bitového OR, která kombinuje přístup ke čtení i ke spouštění.

---

## `!NOT`

Logický výraz `!NOT` se používá k obrácení pravdivostní hodnoty podmínky. Používá se k vyloučení určitých podmínek, pokud nejsou splněny jiné podmínky.

Typ: _Mapping_.

Synopsis:

```yaml
!NOT
what: <expression>
```

!!! info "Negace"

    Další informace naleznete na stránce [Negation](https://en.wikipedia.org/wiki/Negation) na Wikipedii.

### Bitové `!NOT`

Pokud je zadáno celé číslo, pak `!NOT` vrátí hodnotu s převrácenými bity `what`.

!!! tip

    Pokud chcete otestovat, že celé číslo není nula, použijte testovací výraz `!NE`.