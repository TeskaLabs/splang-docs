---
git_commit_hash: b55fa3f
title: IP adresy
---

# Výrazy pro IP adresy


IP adresy jsou interně reprezentovány jako 128bitová celá čísla bez znaménka.
Takový typ může obsahovat jak IPv6, tak IPv4.
IPv4 jsou mapovány do prostoru IPv6 pomocí [RFC 4291 "IPv4-Mapped IPv6 Address"](https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.5.2).

--- 

## `!IP.FORMAT`: Převádí IP adresu na řetězec  

Typ: _Mapping_.

### Synopsis

```yaml
!IP.FORMAT
what: <ip>
```

Převádí vnitřní reprezentaci IP adresy na řetězec.


--- 

## `!IP.INSUBNET`: Zkontroluje, zda IP adresa spadá do podsítě 

Typ: _Mapping_.

### Synopsis

```yaml
!IP.INSUBNET
what: <ip>
subnet: <subnet>
```

```yaml
!IP.INSUBNET
what: <ip>
subnet:
  - <string>
  - <string>
  - <string>
```

Testuje, zda `what` IP adresa patří do `subnet` nebo podsítí, vrací `true`, pokud ano, jinak `false`.

!!! example "Příklad s jednou podsítí"

	```yaml
	!IP.INSUBNET
	what: 192.168.1.1
	subnet: 192.168.0.0/16
	```


!!! example "Příklad s více podsítěmi"

	```yaml
	!IP.INSUBNET
	what: 1.2.3.4
	subnet:
	- 10.0.0.0/8
	- 172.16.0.0/12
	- 192.168.0.0/16
	```

	Test, který kontroluje, zda adresa IP pochází z privátního adresního prostoru IPv4, jak je definováno v [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918).

	Kompaktní forma:

	```yaml
	!IP.INSUBNET
	what: 1.2.3.4
	subnet: [10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16]
	```


---

## Parsování IP adresy

IP adresa je automaticky analyzována z řetězce.
V případě potřeby můžete IP adresu z řetězce explicitně převést na typ `ip`:

```yaml
!CAST
type: ip
what: 192.168.1.1
```


## Parsování podsítě IP

IP podsíť je automaticky parsována z řetězce.
V případě potřeby lze explicitně převést IP adresu z řetězce na typ `ipsubnet`:

```yaml
!CAST
type: ipsubnet
what: 192.168.1.1/16
```
