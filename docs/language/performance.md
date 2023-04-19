---
title: SP-Lang Performance
---

# SP-Lang Performance

* This will become a table of contents (this text will be scrapped).
{:toc}

# Introduction

SP-Lang is designed to deliver a very high performance.

Internally, it compiles provided expressions into a machine code, using [LLVM IR](https://llvm.org) and large degree of optimizations that are possible thanks to a functional structure of the language.
It offers extremelly high single CPU core throughput with a seamless ability to scale procesing to available CPU cores and take full benefits of modern CPU architectures.

Performance tests measures throughput in _EPS_, Events per seconds.
Events per second is a term used in IT management to define the number of events that are processed by SP-Lang expression in one second.
EPS is measured for a single CPU core.

Performance tests are automated using CI/CD framework and therefore completely reproducible.


# Multi-string matching

This expression locates elements of a finite set of strings within an input text.
It is suited for eg. classification of the malicious URLs (provided by a blocklist) in the output of the firewall.

```yaml
!IN
  where: !ARG url
  what:
  - ".000a.biz"
  - ".001edizioni.com"
  < 64 domains in total >
  - ".2win-tech.com"
  - ".2zzz.ru"
```
The list is provided by the [blackweb](https://github.com/maravento/blackweb) project.

* Single CPU Core on `HW-M1-20`: 1423686 EPS
* Single CPU Core on `HW-I7-15`: 807685 EPS


# JSON parsing

```yaml
!JSON.PARSE
what: |
  {
  	< https://github.com/TeskaLabs/cysimdjson/blob/main/perftest/jsonexamples/test.json >
  }
```

_Note: Fast JSON parsing is powered by [cysimdjson](https://github.com/TeskaLabs/cysimdjson) respectively [simdjson](https://simdjson.org) projects._

* Single CPU Core on `HW-M1-20`: 968502 EPS
* Single CPU Core on `HW-I7-15`: 562862 EPS


# IETF Syslog parsing

This is the IETF Syslog aka [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424) parser implemented in SP-Lang:

```yaml
!PARSE.TUPLE # Header
- !PARSE.EXACTLY {what: '<'}
- !PARSE.DIGITS
- !PARSE.EXACTLY {what: '>'}
- !PARSE.DIGITS
- !PARSE.EXACTLY {what: ' '}

- !PARSE.TUPLE # Timestamp
  - !PARSE.DIGITS # Year
  - !PARSE.EXACTLY {what: '-'}
  - !PARSE.DIGITS # Month
  - !PARSE.EXACTLY {what: '-'}
  - !PARSE.DIGITS # Day
  - !PARSE.EXACTLY {what: 'T'}
  - !PARSE.DIGITS # Hours
  - !PARSE.EXACTLY {what: ':'}
  - !PARSE.DIGITS # Minutes
  - !PARSE.EXACTLY {what: ':'}
  - !PARSE.DIGITS # Seconds
  - !PARSE.EXACTLY {what: '.'}
  - !PARSE.DIGITS # Subseconds
  - !PARSE.EXACTLY {what: 'Z'}

- !PARSE.EXACTLY {what: ' '} # HOSTNAME
- !PARSE.UNTIL   {what: ' '}

- !PARSE.EXACTLY {what: ' '} # APP-NAME
- !PARSE.UNTIL   {what: ' '}
 
- !PARSE.EXACTLY {what: ' '} # PROCID
- !PARSE.UNTIL   {what: ' '}

- !PARSE.EXACTLY {what: ' '} # MSGID
- !PARSE.UNTIL   {what: ' '}

- !PARSE.EXACTLY {what: ' '} # STRUCTURED-DATA
- !PARSE.OPTIONAL
  what: !PARSE.TUPLE
    - !PARSE.EXACTLY {what: '['}
    - !PARSE.UNTIL   {what: ' '} # SD-ID
    - !PARSE.REPEAT  
      what:
      !PARSE.TUPLE # SD-PARAM
      - !PARSE.EXACTLY {what: ' '}
      - !PARSE.UNTIL   {what: '='} # PARAM-NAME
      - !PARSE.EXACTLY {what: '='}
      - !PARSE.BETWEEN 
         what: '"'
         escaped: '\\"]'
```

* Single CPU Core on `HW-M1-20`: 304004 EPS
* Single CPU Core on `HW-I7-15`: 181494 EPS



# Reference Hardware

## HW-M1-20

* Machine: MacBook Air (M1, 2020)
* CPU: [Apple M1](https://en.wikipedia.org/wiki/Apple_M1), Launched at 2020

## HW-I7-15

* Machine: MacBook Pro (15-inch, 2016)
* CPU: 2.6 GHz Quad-Core Intel Core i7, [I7-6700HQ](https://ark.intel.com/content/www/us/en/ark/products/88967/intel-core-i76700hq-processor-6m-cache-up-to-3-50-ghz.html), Launched at 2015
