---
tags: [note, shell, command-line, unix, tool]
---

# uniq

> Collapses or filters adjacent duplicate lines, and with `-c` counts how often each run occurs; it requires sorted input, which is why it is almost always paired with `sort`.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Remove duplicates |
| **Relation** | `uniq` |
| **Main advantage** | The simple adjacent-run filter |

## Typical use

```sh
sort ips.txt | uniq -c | sort -rn
```

## References

- [uniq](https://man7.org/linux/man-pages/man1/uniq.1.html)
- [sort](/view.html?p=notes/technica/general/sort.md)
