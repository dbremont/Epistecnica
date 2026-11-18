---
tags: [note, shell, command-line, unix, tool]
---

# viddy

> A modern `watch`: it keeps a history of the output, records and replays it, and highlights the differences between runs.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Monitor |
| **Relation** | `watch` |
| **Main advantage** | History and diff view for repeated commands |

## Typical use

```sh
viddy -d -n 2 'ss -tlnp'
```

## References

- [viddy](https://github.com/sachaos/viddy)
- [watch](/view.html?p=notes/technica/general/watch.md)
