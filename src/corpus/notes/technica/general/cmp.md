---
tags: [note, shell, command-line, unix, tool]
---

# cmp

> Compares two files byte by byte and reports the first difference; the tool for binary equality rather than textual difference.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Compare |
| **Relation** | `cmp` |
| **Main advantage** | Byte-level comparison |

## Typical use

```sh
cmp -l a.bin b.bin | head
```

## References

- [cmp](https://man7.org/linux/man-pages/man1/cmp.1.html)
- [diff](/view.html?p=notes/technica/general/diff.md)
