---
tags: [note, shell, command-line, unix, tool]
---

# journalctl

> Queries the systemd journal: filter by unit, priority, time or boot, and follow the log in real time.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Monitor |
| **Relation** | `tail -f` on log files |
| **Main advantage** | Structured, queryable system logs |

## Typical use

```sh
journalctl -u nginx -f
```

## References

- [journalctl](https://man7.org/linux/man-pages/man1/journalctl.1.html)
- [tail](/view.html?p=notes/technica/general/tail.md)
