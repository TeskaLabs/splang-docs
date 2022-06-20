---
layout: default
title: SP-Lang documentation
---

# IP Address expressions

* This will become a table of contents (this text will be scrapped).
{:toc}

IP addresses are represented internally as a number, 128bit unsigned integer.
Such a type can contain both IPv6 and IPv4.
IPv4 are mapped into IPv6 space, using [RFC 4291 "IPv4-Mapped IPv6 Address"](https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.5.2).

--- 

## `!IP.FORMAT`: Convert an IP address into a string  {#EXPR-IP-FORMAT}

Type: _Mapping_.

### Synopsis

```yaml
!IP.FORMAT
what: <ip>
```

Convert the internal representation of the IP address into a string.


--- 

## `!IP.INSUBNET`: Check if IP address falls into a subnet {#EXPR-IP-INSUBNET}

Type: _Mapping_.

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

Test if `what` IP address belongs to a `subnet` or subnets , returns `true` if yes otherwise `false`.

### Example with a single subnet

```yaml
!IP.INSUBNET
what: 192.168.1.1
subnet: 192.168.0.0/16
```


### Example with multiple subnets

```yaml
!IP.INSUBNET
what: 1.2.3.4
subnet:
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
```

The test that check if IP address is from IPv4 private address space.


More compact form:

```yaml
!IP.INSUBNET
what: 1.2.3.4
subnet: [10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16]
```


---

## Parse of the IP address

IP address is parsed automatically from a string.
If needed, you may explicitly cast string-based IP address into the `ip` type:

```yaml
!CAST
type: ip
what: 192.168.1.1
```


## Parse of the IP subnet

IP subnet is parsed automatically from a string.
If needed, you may explicitly cast string-based IP address into the `ipsubnet` type:

```yaml
!CAST
type: ipsubnet
what: 192.168.1.1/16
```
