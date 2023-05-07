---
title: Directives
---

# Directives


NOTE: SP-Lang directives are expanded during compilation. They are not expressions.

--- 

## `!INCLUDE`: Insert the content of another file 

Type: Scalar, Directive.

The `!INCLUDE` directive is used to paste a content of given file into current file.
If included file is not found, SP-Lang renders error.


### Synopsis

```yaml
!INCLUDE <filename>
```

The `filename` is a name of the file in the library to be included.

It could be:

* an absolute path, starting with `/` from the root of the library,
* an relative path to the location of the file containing `!INCLUDE` statement
  
`.yaml` extension is optional and will be added to the `filename` if missing.

### Example

```yaml
!INCLUDE other_file.yaml
```

This is a simple inclusion of the `other_file.yaml`.
  

```yaml
!MATCH
what: !GET {...}
with:
  'group1': !INCLUDE inc_group1
  'group2': !INCLUDE inc_group2
```

In this example, `!INCLUDE` is used to decompose a larger expression into a logically separated files.
