---
tags: [note, shell, command-line, unix, tool]
---

# tail

> Prints the end of a file, and with `-f` keeps reading as it grows — the standard way to watch a log.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Monitor |
| **Relation** | `tail -f` |
| **Main advantage** | The default log follower |

## Typical use

```sh
tail -f /var/log/syslog
```

## References

- [tail](https://man7.org/linux/man-pages/man1/tail.1.html)
- [watch](/view.html?p=notes/technica/general/watch.md)
