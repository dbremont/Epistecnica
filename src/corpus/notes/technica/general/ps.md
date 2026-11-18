---
tags: [note, shell, command-line, unix, tool]
---

# ps

> Takes a snapshot of the process table: PID, parent, state, CPU and memory, and the command line.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Process management |
| **Relation** | `ps` |
| **Main advantage** | The portable process snapshot |

## Typical use

```sh
ps aux --sort=-%mem | head
```

## References

- [ps](https://man7.org/linux/man-pages/man1/ps.1.html)
- [procs](/view.html?p=notes/technica/general/procs.md)
