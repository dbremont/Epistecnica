---
tags: [note, shell, command-line, unix, tool]
---

# fd

> A fast, user-friendly alternative to `find`: it walks the tree with a syntax closer to a search query than to an expression language, ignores `.gitignore` patterns by default, and parallelises the walk.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Find files |
| **Relation** | `find` |
| **Main advantage** | Much faster, simpler syntax |

## Typical use

```sh
fd -e md 'pattern'
```

## References

- [fd](https://github.com/sharkdp/fd)
- [find](/view.html?p=notes/technica/general/find.md)
