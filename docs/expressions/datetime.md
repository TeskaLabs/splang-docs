---
title: Date/time
---

# Date/time expressions


Date and time is expressed in SP-Lang by a `datetime` type.
It has a microsecond resolution and a range from year 8190 B.C. to a year 8191.
It is in the UTC timezone.

!!! info

	For more information about `datatime` type, continue [here](../../language/date-time).

---

## `!NOW`: A current date and time 

Type: _Mapping_.

Get a current date and time.

```yaml
!NOW
```

---

## `!DATETIME`: Construct the date/time 

Type: _Mapping_.

Constructs the `datetime` from components such as year, month, day and so on.


```yaml
!DATETIME
year: <year>
month: <month>
day: <day>
hour: <hour>
minute: <minute>
second: <second>
microsecond: <microsecond>
timezone: <timezone>
```

* `year` is an integer number in range -8190 … 8191.
* `month` is an integer number in range 1 … 12.
* `day` is an integer number in range 1 … 31, respective to a number of days in a given month.
* `hour` is an integer number in 0 … 24, it is optional and default value is `0`.
* `minute` is an integer number in 0 … 59, it is optional and default value is `0`.
* `second` is an integer number in 0 … 60, it is optional and default value is `0`.
* `microsecond` is an integer number in 0 … 1000000, it is optional and default value is `0`.
* `timezone` is [IANA Time Zone Database](https://www.iana.org/time-zones) name of the timezone. It is optional and a default timezone is UTC.


!!! example "Example: UTC date/time"

	```yaml
	!DATETIME
	year: 2021
	month: 10
	day: 13
	hour: 12
	minute: 34
	second: 56
	microsecond: 987654
	```

!!! example "Example: default values"

	```yaml
	!DATETIME
	year: 2021
	month: 10
	day: 13
	```


!!! example "Example: timezones"

	```yaml
	!DATETIME
	year: 2021
	month: 10
	day: 13
	timezone: Europe/Prague
	```

	```yaml
	!DATETIME
	year: 2021
	month: 10
	day: 13
	timezone: "+05:00"
	```

---

## `!DATETIME.FORMAT`: Format a date/time 

Type: _Mapping_.

Format a date and time information based on the `datetime`.


```yaml
!DATETIME.FORMAT
with: <datetime>
format: <format>
timezone: <string>
```

The `datetime` contains the information about the data and time to be used for formating.
The `format` is a string that contains specification about the format of the output.
The `timezone` is optional information, if provided, the time will be printed in the local time specified  by the argument, otherwise UTC timezone is used.

### Format

* `%H`: Hour (24-hour clock) as a zero-padded decimal number.
* `%M`: Minute as a zero-padded decimal number.
* `%S`: Second as a zero-padded decimal number.
* `%f`: Microsecond as a decimal number, zero-padded to 6 digits.
* `%I`: Hour (12-hour clock) as a zero-padded decimal number.
* `%p`: Locale’s equivalent of either AM or PM.

* `%d`: Day of the month as a zero-padded decimal number.
* `%m`: Month as a zero-padded decimal number.
* `%y`: Year without century as a zero-padded decimal number.
* `%Y`: Year with century as a decimal number.

* `%z`: UTC offset.

* `%a`: Weekday as abbreviated name.
* `%A`: Weekday as full name.
* `%w`: Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
* `%b`: Month as abbreviated name.
* `%B`: Month as full name.
* `%j`: Day of the year as a zero-padded decimal number.
* `%U`: Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
* `%W`: Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.

* `%c`: Date and time representation.
* `%x`: Date representation.
* `%X`: Time representation.

* `%%`: A literal '%' character.


!!! example

	```yaml
	!DATETIME.FORMAT
	with: !NOW
	format: "%Y-%m-%d %H:%M:%S"
	timezone: "Europe/Prague"
	```

	Prints the current local time as eg. `2022-12-31 12:34:56` using the timezone "Europe/Prague".


---

## `!DATETIME.PARSE`: Parse a date/time 

Type: _Mapping_.

Parse a date and time from a string.


```yaml
!DATETIME.PARSE
what: <string>
format: <format>
timezone: <timezone>
```

Parse `what` string input using `format` string.
The `timezone` information is optional, if provided, then it specifies local timezone of the `what` string.

See "Format" chapter above for more information about `format`.


!!! example

	```yaml
	!DATETIME.PARSE
	what: "2021-06-29T16:51:43-08"
	format: "%y-%m-%dT%H:%M:%S%z"
	```

---

## `!GET`: Get a date/time component 

Type: _Mapping_.

Extract the date/time component such as hour, minute, day etc. from `datetime`.


```yaml
!GET
what: <string>
from: <datetime>
timezone: <timezone>
```

Extract the `what` component from `datetime`.
The `timezone` if optional, if not provided UTC timezone is used.

### Components

* `year`, `y`: Year
* `month`, `m`: Month
* `day`, `d`: Day

* `hour`, `H`: Hour
* `minute`, `M`: Minute
* `second`, `S`: Second
* `microsecond`, `f`: Microsecond

* `weekday`, `w`: Day of the week

!!! example

	```yaml
	!GET
	what: H
	from: !NOW
	timezone: "Europe/Prague"
	```

	Get "hours" component of the current timestamp, using the "Europe/Prague" timezone.


!!! example "Example: Get a current year"

	```yaml
	!GET { what: year, from: !NOW }
	```

