---
tags: [note, shell, command-line, unix, tool]
---

# sort

> Sorts lines of text by one or more keys, numerically or lexically, in memory or with controlled temporary files for large inputs.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Sort |
| **Relation** | `sort` |
| **Main advantage** | Already highly optimised; no replacement is needed |

## Typical use

```sh
sort -t, -k2,2nr data.csv
```

## References

- [sort](https://man7.org/linux/man-pages/man1/sort.1.html)
- [uniq](/view.html?p=notes/technica/general/uniq.md)
