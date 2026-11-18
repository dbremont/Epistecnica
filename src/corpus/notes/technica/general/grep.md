---
tags: [note, shell, command-line, unix, tool]
---

# grep

> The POSIX line-oriented search tool: it reads input line by line and prints the lines that match a regular expression, with recursive and context options.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Search content |
| **Relation** | `grep` |
| **Main advantage** | The portable baseline every system has |

## Typical use

```sh
grep -RIn 'TODO' src/
```

## References

- [grep](https://man7.org/linux/man-pages/man1/grep.1.html)
- [rg](/view.html?p=notes/technica/general/rg.md)
