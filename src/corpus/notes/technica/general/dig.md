---
tags: [note, shell, command-line, unix, tool]
---

# dig

> Queries the Domain Name System: it prints the answer, authority and additional sections, and is the standard way to inspect a record.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Network inspection |
| **Relation** | `dig` |
| **Main advantage** | Detailed DNS answers |

## Typical use

```sh
dig +short example.com A
```

## References

- [dig](https://man7.org/linux/man-pages/man1/dig.1.html)
- [ping](/view.html?p=notes/technica/general/ping.md)
