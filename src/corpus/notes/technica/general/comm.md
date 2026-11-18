---
tags: [note, shell, command-line, unix, tool]
---

# comm

> Compares two sorted files and prints the lines unique to each or common to both — a set operation on sorted text.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Compare |
| **Relation** | `comm` |
| **Main advantage** | Set comparison on sorted input |

## Typical use

```sh
comm -12 <(sort a.txt) <(sort b.txt)
```

## References

- [comm](https://man7.org/linux/man-pages/man1/comm.1.html)
- [diff](/view.html?p=notes/technica/general/diff.md)
