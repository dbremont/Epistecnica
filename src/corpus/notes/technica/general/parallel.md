---
tags: [note, shell, command-line, unix, tool]
---

# parallel

> GNU `parallel` runs commands concurrently over a list of inputs, with job control and result ordering — the parallel replacement for `xargs`.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Execute on many files |
| **Relation** | `xargs` |
| **Main advantage** | Parallel execution with job control |

## Typical use

```sh
find . -name '*.log' | parallel gzip
```

## References

- [parallel](https://www.gnu.org/software/parallel/)
- [xargs](/view.html?p=notes/technica/general/xargs.md)
