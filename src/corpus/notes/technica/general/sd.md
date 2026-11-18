---
tags: [note, shell, command-line, unix, tool]
---

# sd

> A simpler find-and-replace tool than `sed`: the pattern and replacement are plain arguments, and the file is edited in place without the stream-editor syntax.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Transform text |
| **Relation** | `sed` |
| **Main advantage** | Simpler substitution syntax |

## Typical use

```sh
sd 'old' 'new' file.txt
```

## References

- [sd](https://github.com/chmln/sd)
- [sed](/view.html?p=notes/technica/general/sed.md)
