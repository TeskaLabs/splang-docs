---
git_commit_hash: b55fa3f
title: IP adresa
---

# Vyjádření IP adresy


IP adresy jsou interně reprezentovány jako číslo, 128bitové celé číslo bez znaménka.
Takový typ může obsahovat jak IPv6, tak IPv4.
IPv4 jsou mapovány do prostoru IPv6 pomocí [RFC 4291 "IPv4-Mapped IPv6 Address"](https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.5.2).

--- 

## `!IP.FORMAT`: Převést IP adresu na řetězec  

Typ: _Mapování_.

### Synopse
```yaml

!IP.FORMAT
co: <ip>
```

Převést vnitřní reprezentaci IP adresy na řetězec.


--- 

## `!IP.INSUBNET`: Zkontrolujte, zda IP adresa spadá do podsítě 

Typ: _Mapping_.

### Synopse
```yaml

!IP.INSUBNET
co: <ip>
subnet: <subnet>
```
```yaml

!IP.INSUBNET
co: <ip>
subnet:
  - <string>
  - <string>
  - <string>
```

Testuje, zda `jaká` IP adresa patří do `podsítě` nebo podsítí , vrací `pravdu`, pokud ano, jinak `nepravdu`.

### Příklad s jednou podsítí
```yaml

!IP.INSUBNET
co: 192.168.1.1
podsíť: 192.168.0.0/16
```


### Příklad s více podsítěmi
```yaml

!IP.INSUBNET
co: 1.2.3.4
podsíť:
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
```

Test, který kontroluje, zda adresa IP pochází z privátního adresního prostoru IPv4, jak je definováno v [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918).


Kompaktnější podoba:
```yaml

!IP.INSUBNET
co: 1.2.3.4
podsíť: [10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16]
```


---

## Rozbor IP adresy

IP adresa je automaticky analyzována z řetězce.
V případě potřeby můžete IP adresu z řetězce explicitně převést na typ `ip`:
```yaml

!CAST
typ: ip
co: 192.168.1.1
```


## Rozbor podsítě IP

IP podsíť je automaticky analyzována z řetězce.
V případě potřeby můžete explicitně převést IP adresu z řetězce na typ `ipsubnet`:
```yaml

!CAST
typ: ipsubnet
co: 192.168.1.1/16
```
