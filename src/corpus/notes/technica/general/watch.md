---
tags: [note, shell, command-line, unix, tool]
---

# watch

> Runs a command repeatedly on an interval and redraws its output in place — the simplest way to poll a changing state.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Monitor |
| **Relation** | `watch` |
| **Main advantage** | Repeated in-place execution |

## Typical use

```sh
watch -n 2 'ss -tlnp'
```

## References

- [watch](https://man7.org/linux/man-pages/man1/watch.1.html)
- [viddy](/view.html?p=notes/technica/general/viddy.md)
