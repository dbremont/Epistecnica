---
tags: [note, guia]
---

# A Guide to Grep


> `g/re/p` (***g**lobal / **r**egular **e**xpression search **/** and **p**rint*).
> 

> `grep` is a command-line utility used to search for patterns within files and print lines that match those patterns.
> 

[https://pbs.twimg.com/media/GNYGPudWIAAx_hq?format=jpg&name=large](https://pbs.twimg.com/media/GNYGPudWIAAx_hq?format=jpg&name=large)

```bash
grep -ri -C 3 --include="*.cs" Created | wc
grep -ri --include="*.cs" IDontysCrudController | wc
grep -B 3 -A 2 foo README.txt
```

## References

- [Grep](https://en.wikipedia.org/wiki/Grep)
- [grep all .java files in a directory for a particular string](https://superuser.com/questions/3512/grep-all-java-files-in-a-directory-for-a-particular-string)
- [grep: show lines surrounding each match](https://stackoverflow.com/questions/9081/grep-show-lines-surrounding-each-match)
- [https://beyondgrep.com/](https://beyondgrep.com/)
