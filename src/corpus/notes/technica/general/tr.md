---
tags: [note, shell, command-line, unix, tool]
---

# tr

> Translates, squeezes or deletes characters in a byte stream: the tool for case conversion and character-class cleanup.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Transform text |
| **Relation** | `tr` |
| **Main advantage** | Character-level translation and deletion |

## Typical use

```sh
tr '[:lower:]' '[:upper:]' < file.txt
```

## References

- [tr](https://man7.org/linux/man-pages/man1/tr.1.html)
- [sed](/view.html?p=notes/technica/general/sed.md)
