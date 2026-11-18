---
tags: [note, shell, command-line, unix, tool]
---

# kill

> Sends a signal to a process — `TERM` to ask it to stop, `KILL` to force it, `HUP` to reload — addressed by PID or by job.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Process management |
| **Relation** | `kill` |
| **Main advantage** | The signal interface to the kernel |

## Typical use

```sh
kill -TERM 1234
```

## References

- [kill](https://man7.org/linux/man-pages/man1/kill.1.html)
- [pgrep](/view.html?p=notes/technica/general/pgrep.md)
