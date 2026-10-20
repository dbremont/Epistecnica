---
tags: [system]
---

# CSBB: File System


> Use a faster disk like an SSD to improve application performance.
> 

QA:

- File System Performance Modelling
- Disk Performance Metrics
- Which benchmarks to used?
- Which workloads to used?’
- How fast can you open 1000 files? https://lemire.me/blog/2025/03/01/how-fast-can-you-open-1000-files/   ‣https://github.com/csiglab/cs-analyst-labs

## Benchmarking Tools

- `fio` (Flexible I/O Tester)
- `iozone` Tests read/write performance with various access patterns.
- `bonnie++` Good for measuring file system throughput and metadata operations.
- `fs_mark` Designed to test metadata performance.

## **Comparing File Systems**

> To compare different file systems (e.g., `ext4`, `xfs`, `btrfs`), format a partition and rerun the benchmarks.
> 

```
mkfs.ext4 /dev/sdb1
mount /dev/sdb1 /mnt/test
```

## Comparison

> 

## References

- [File System](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/file-system.md)
- [On Benchmarking Popular File Systems](https://people.computing.clemson.edu/~jzwang/pub/fbench.pdf)
- http://web.cs.ucla.edu/classes/winter13/cs111/scribe/10c/
- https://en.wikipedia.org/wiki/High_Performance_File_System
- [The Dos and Don'ts of File System Benchmarking](https://freebsdfoundation.org/wp-content/uploads/2016/03/The-Dos-and-Donts-of-File-System-Benchmarking.pdf)
- https://arxiv.org/html/2408.01805v1
- https://stackoverflow.com/questions/1356240/file-system-performance-testing/1356986#1356986
- https://docs.gitlab.com/administration/operations/filesystem_benchmarking/
- https://serverfault.com/questions/95791/does-a-file-system-lose-performance-as-it-fills-up
- https://dl.acm.org/doi/10.1145/1367829.1367831
- https://www.linux-magazine.com/Online/Features/Filesystems-Benchmarked
- Tarasov, V., Bhanage, S., Zadok, E., & Seltzer, M. (2011). 
Benchmarking File System Benchmarking: It {* IS*} Rocket Science. In *13th Workshop on Hot Topics in Operating Systems (HotOS XIII)*.
-