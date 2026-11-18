---
tags: [note, shell, command-line, unix, tool]
---

# locate

> Finds files by name from a pre-built index rather than by walking the filesystem, so a query returns in milliseconds; the index is refreshed by `updatedb`, which is why the answer can be stale.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Find files |
| **Relation** | `find` |
| **Main advantage** | Instant name lookup from an index |

## Typical use

```sh
locate nginx.conf
```

## References

- [locate](https://man7.org/linux/man-pages/man1/locate.1.html)
- [plocate](/view.html?p=notes/technica/general/plocate.md)
