---
tags: [note, shell, command-line, unix, tool]
---

# scp

> Copies files between hosts over SSH, using the same authentication as a remote shell; simple, and slower than `rsync` for repeated transfers.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Archive/compress |
| **Relation** | `scp` |
| **Main advantage** | Simple remote copy over SSH |

## Typical use

```sh
scp file.txt host:/srv/
```

## References

- [scp](https://man7.org/linux/man-pages/man1/scp.1.html)
- [rsync](/view.html?p=notes/technica/computation/telecom/rsync.md)
