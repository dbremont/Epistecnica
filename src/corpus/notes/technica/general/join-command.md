---
tags: [note, shell, command-line, unix, tool]
---

# join

> Joins the lines of two files on a common field, in the manner of a relational join; both inputs must be sorted on the join key.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Join datasets |
| **Relation** | `join` |
| **Main advantage** | The portable relational join for text files |

## Typical use

```sh
join -1 1 -2 1 users.txt orders.txt
```

## References

- [join](https://man7.org/linux/man-pages/man1/join.1.html)
- [sort](/view.html?p=notes/technica/general/sort.md)
