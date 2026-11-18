---
tags: [note, shell, command-line, unix, tool]
---

# datamash

> A command-line tool for statistical and aggregation operations over columns — sums, means, medians, grouped statistics — without writing an `awk` program.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Aggregate |
| **Relation** | `awk` |
| **Main advantage** | Ready-made column statistics |

## Typical use

```sh
datamash -t, mean 2 sum 3 < data.csv
```

## References

- [datamash](https://www.gnu.org/software/datamash/)
- [awk](/view.html?p=notes/technica/general/awk.md)
