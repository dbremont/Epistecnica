---
tags: [note, como]
---

# How to get the command line args passed to a running process on Unix/Linux Systems?


> …
> 

```bash
PID=...
ps -fp $PID
cat /proc/$PID/cmdline | sed -e "s/\x00/ /g"; echo
```

## References

- [How to get the command line args passed to a running process on unix/linux systems?](https://stackoverflow.com/questions/821837/how-to-get-the-command-line-args-passed-to-a-running-process-on-unix-linux-syste)
