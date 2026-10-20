---
tags: [data-collection]
---

# Profiler

- [Perf](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/perf.md), [Valgrind](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/valgrind.md), [gprof](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/gprof.md), [LTTng](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/lttng.md)

> A **profiler** is a **performance analysis tool** that dynamically monitors a program’s execution to collect detailed runtime statistics about **function calls, execution time, memory usage, and system interactions**. It operates by injecting instrumentation or utilizing hardware and OS-level facilities to **record execution behavior**, allowing developers to analyze performance bottlenecks and optimize system efficiency.
> 

## Uses

> 

| **Profiler Use Case** | **Data Collected** |
| --- | --- |
| **Call Graph Analysis** | Function call relationships, caller-callee pairs, invocation counts. |
| **Execution Time Profiling** | CPU time per function, wall-clock time, time spent in system vs. user mode. |
| **Sampling-Based Profiling** | Program counter (PC) samples, stack traces, frequency of execution in different code regions. |
| **Event-Based Profiling** | System calls, page faults, context switches, memory accesses, I/O operations. |
| **Memory Profiling** | Heap/stack allocations, memory leaks, buffer overflows, garbage collection statistics. |
| **Instruction-Level Profiling** | Cache misses, branch mispredictions, pipeline stalls, instruction throughput. |
| **Thread and Concurrency Profiling** | Thread creation/destruction, mutex contention, lock waits, CPU affinity. |
| **System-Wide Profiling** | Kernel and user-space execution time, hardware performance counters, interrupt handling. |
| **I/O Profiling** | Disk read/write latency, network activity, file descriptor usage. |
| **Energy Profiling** | Power consumption per process, CPU/GPU energy usage, battery impact. |

## Implementation

> 

| **Profiler Type** | **Mechanism** | **Examples** | **Best For** |
| --- | --- | --- | --- |
| **Instrumentation-Based Profilers** | Modifies **binary or source code** to insert profiling hooks at function entry/exit. | `gprof`, `gcc -pg`, `valgrind/callgrind` | Function call tracing, execution time analysis, detailed profiling with high overhead. |
| **Sampling-Based Profilers** | Periodically samples the **program counter (PC), stack traces, or hardware performance counters** to estimate execution behavior. | `perf`, Google `pprof`, `Intel VTune`, `Flamegraphs` | Low-overhead CPU profiling, identifying hot functions, performance bottleneck detection. |
| **Event-Driven Profilers** | Hooks into **OS-level events** (e.g., syscalls, page faults, interrupts) to profile system interactions. | `eBPF`, `perf_events`, `SystemTap` | Kernel-space profiling, tracing system calls, analyzing I/O and memory operations. |
| **Hardware-Assisted Profilers** | Uses CPU **Performance Monitoring Units (PMUs)** to track **cache misses, branch mispredictions, instruction cycles, etc.** | `perf`, `Intel VTune`, `AMD uProf` | Low-level CPU profiling, cache efficiency, branch prediction analysis, and micro-architectural performance tuning. |
| Instruction-Level Profiling | **Profiling**Analyzes **CPU pipeline stalls, branch mispredictions, and cache misses** to optimize low-level execution. |  |  |
| Thread and Concurrency Profiling | Observes **mutex contention, thread switching, and parallel execution efficiency** in multi-threaded programs. |  |  |
| Memory Profiling | Monitors **heap/stack allocations**, detecting memory leaks and excessive memory usage. |  |  |

## References

- https://en.wikipedia.org/wiki/Profiling_(computer_programming)
- [GCC Instrumentation](note.html?n=technica/computation/language-system/conceptual-model-language-system/gcc-gnu-compiler-collection.md)