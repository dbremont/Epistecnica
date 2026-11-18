---
tags: [note, shell, command-line, unix, tool]
---

# pgrep

> Finds process IDs by name, command line, user or other attributes — the scriptable way to select a process before signalling it.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Process management |
| **Relation** | `ps | grep` |
| **Main advantage** | Attribute-based PID lookup |

## Typical use

```sh
pgrep -af nginx
```

## References

- [pgrep](https://man7.org/linux/man-pages/man1/pgrep.1.html)
- [kill-command](/view.html?p=notes/technica/general/kill-command.md)
