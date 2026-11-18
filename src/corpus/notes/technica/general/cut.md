---
tags: [note, shell, command-line, unix, tool]
---

# cut

> Selects byte, character or field ranges from each line — the quick way to take columns out of a delimited file.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Extract columns |
| **Relation** | `cut` |
| **Main advantage** | The simple column selector |

## Typical use

```sh
cut -d, -f2,4 data.csv
```

## References

- [cut](https://man7.org/linux/man-pages/man1/cut.1.html)
- [awk](/view.html?p=notes/technica/general/awk.md)
