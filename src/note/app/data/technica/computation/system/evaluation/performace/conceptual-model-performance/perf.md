---
tags: [tool]
---

# Perf

- [Profiler](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/profiler.md)

> **Perf** (short for “performance”) refers to measuring and analyzing a program or system's execution speed and resource usage. It involves gathering data on various metrics, such as CPU usage, memory usage, disk I/O, network I/O, and so on, and then analyzing that data to identify performance bottlenecks and areas for improvement. **Perf** typically uses specialized tools such as perf or the Linux Performance Tools (LPT).
> 

```bash
# Install
apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r`
```

```bash
# Profiling a Process
sudo perf record -p [PID] -g -- sleep [duration]
sudo perf record ./hello
sudo perf record --call-graph dwarf -F 99 -g -- ./hello
```

```bash
git clone https://github.com/brendangregg/FlameGraph
cd FlameGraph
```

```bash
# Translate Data 
# This will use the default "perf.data"
sudo perf script > out.perf

# Generate Stack Strace
./stackcollapse-perf.pl ../out.perf | ./flamegraph.pl > flamegraph.svg
```

## References

- [Profiling Python Like a Boss](https://zapier.com/engineering/profiling-python-boss/)
- [Profiling Python in Production](https://www.nylas.com/blog/performance/)
- [Profiling](https://en.wikipedia.org/wiki/Profiling_(computer_programming))
- De Melo, Arnaldo Carvalho. "The new linux’perf’tools." Slides from Linux Kongress. Vol. 18. 2010.
- Gregg, Brendan. *BPF performance tools*. Addison-Wesley Professional, 2019.
- [**perf-tools**](https://github.com/brendangregg/perf-tools)

[FlameGraph](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/flamegraph.md)