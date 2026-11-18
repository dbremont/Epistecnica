---
tags: [note, shell, command-line, unix, tool]
---

# pushd

> Pushes the current directory onto a stack and changes to another, so `popd` can return — the shell's own bookmarks for a working session.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Navigate directories |
| **Relation** | `cd` |
| **Main advantage** | A directory stack with return |

## Typical use

```sh
pushd /tmp && popd
```

## References

- [pushd](https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html)
- [zoxide](/view.html?p=notes/technica/general/zoxide.md)
