---
title: List
---

# List expressions


The list is one of basic data structures provided by SP-Lang.
The list contains a finite number of ordered item, where the same item may occur more than once.
Items in the list must be of the same type.

!!! note

    The list is sometimes also called inaccurately _an array_.


--- 

## `!LIST`: List of items 

Type:  _Implicit sequence_, _Mapping_.

### Synopsis

```yaml
!LIST
- ...
- ...
```

!!! hint

	Use `!COUNT` to determine number of items in the list.



There are several ways, how a list can be specified in SP-Lang:

!!! example

	```yaml
	!LIST
	- "One"
	- "Two"
	- "Three"
	- "Four"
	- "Five"
	```

!!! example

	Implicit list using [YAML block sequences](https://yaml.org/spec/1.2.2/#821-block-sequences):

	```yaml
	- "One"
	- "Two"
	- "Three"
	- "Four"
	- "Five"
	```

!!! example

	Implicit list using [YAML flow sequences](https://yaml.org/spec/1.2.2/#741-flow-sequences):

	```yaml
	["One", "Two", "Three", "Four", "Five"]
	```

!!! example

	The mapping form:

	```yaml
	!LIST
	with:
	- "One"
	- "Two"
	- "Three"
	- "Four"
	- "Five"
	```

--- 

## `!GET`: Get the item from the list 

Type: _Mapping_.


### Synopsis

```yaml
!GET
what: <index of the item in the list>
from: <list>
```

`index` is an integer (number).

`index` can be negative, in that case, it specifies an item from the end of the list.
Items are indexed from the 0, it means that the first item in the list has an index 0.

If the `index` is out of bound of the list, the statement returns with error.


!!! example

	```yaml
	!GET
	what: 3
	from:
	!LIST
	- 1
	- 5
	- 30
	- 50
	- 80
	- 120
	```

	Returns `50`.


!!! example

	```yaml
	!GET
	what: -1
	from:
	!LIST
	- 1
	- 5
	- 30
	- 50
	- 80
	- 120
	```

	Returns the last item in the list, which is `120`.

