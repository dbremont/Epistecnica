---
tags: [note, shell, command-line, unix, tool]
---

# stat

> Reports file metadata in detail: size, inode, permissions, ownership, access and modification times, and the filesystem it lives on.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Inspect file metadata |
| **Relation** | `stat` |
| **Main advantage** | The detailed metadata view |

## Typical use

```sh
stat -c '%n %s %y' file
```

## References

- [stat](https://man7.org/linux/man-pages/man1/stat.1.html)
- [file](/view.html?p=notes/technica/general/file.md)
