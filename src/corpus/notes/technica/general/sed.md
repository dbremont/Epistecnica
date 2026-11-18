---
tags: [note, shell, command-line, unix, tool]
---

# sed

> The stream editor: it applies a script of commands — most often a substitution — to each line of a stream, without opening an editor.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Transform text |
| **Relation** | `sed` |
| **Main advantage** | Scripted, streaming line editing |

## Typical use

```sh
sed -i 's/old/new/g' file.txt
```

## References

- [sed](https://man7.org/linux/man-pages/man1/sed.1.html)
- [sd](/view.html?p=notes/technica/general/sd.md)
