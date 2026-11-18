---
tags: [note, shell, command-line, unix, tool]
---

# tar

> Bundles a directory tree into a single archive, optionally compressed, preserving paths and permissions — the standard tape-archive format.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Archive/compress |
| **Relation** | `tar` |
| **Main advantage** | Tree archiving with metadata |

## Typical use

```sh
tar -czf archive.tar.gz src/
```

## References

- [tar](https://man7.org/linux/man-pages/man1/tar.1.html)
- [gzip](/view.html?p=notes/technica/general/gzip.md)
