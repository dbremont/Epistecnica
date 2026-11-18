---
tags: [note, shell, command-line, unix, tool]
---

# xargs

> Builds argument lists from standard input and runs a command on them, turning a stream of names into one or more invocations.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Execute on many files |
| **Relation** | `find -exec` |
| **Main advantage** | The portable batch executor |

## Typical use

```sh
find . -name '*.md' -print0 | xargs -0 wc -l
```

## References

- [xargs](https://man7.org/linux/man-pages/man1/xargs.1.html)
- [parallel](/view.html?p=notes/technica/general/parallel.md)
