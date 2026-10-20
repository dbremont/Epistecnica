---
tags: [system]
---

# CSBB: CPU


> 

## Model

> 

### **CPU Architecture**

- **Core Count**: Number of physical cores (single-threaded vs. multi-threaded performance).
- **Clock Speed**: Base and boosted frequencies, often affecting performance.
- **Pipeline Stages**: Depth and structure of the pipeline (e.g., fetch, decode, execute, memory access, write-back).
- **Out-of-Order Execution**: The ability of the CPU to execute instructions non-sequentially to maximize throughput.
- **Speculative Execution & Branch Prediction**: How the CPU handles branch mispredictions and speculatively executes instructions.

### **Cache Hierarchy**

- **L1/L2/L3 Cache**: Size, latency, and hit rates of various cache levels.
- **Cache Misses**: Rate of cache misses (e.g., **L1 miss**, **L2 miss**, **L3 miss**), and how this impacts memory access latency.
- **Cache Coherence**: In multi-core systems, how data is synchronized across cores (e.g., MESI protocol).

### **Execution Units**

- **ALUs & FPUs**: The Arithmetic Logic Units and Floating-Point Units responsible for computation.
- **SIMD Units**: Vector processing units (e.g., AVX or SSE).
- **Dispatch & Issue**: How instructions are dispatched to various execution units.

### **Memory Subsystem**

- **DRAM Access Latency**: Time to access main memory and its impact.
- **NUMA**: Non-Uniform Memory Access, which is relevant for multi-socket systems.
- **Memory Bandwidth**: The amount of data that can be transferred to/from memory per cycle.

### **I/O & Interconnects**

- **Bus Speed**: Latency of communication between CPU and other devices.
- **PCIe Latency**: Latency associated with accessing peripheral devices like GPUs or storage.

## Metrics

- **Instructions Per Cycle (IPC)**: The average number of instructions executed per cycle.
- **Branch Misprediction Rate**: The frequency of branch mispredictions that cause pipeline flushes.
- **Latency Metrics**: CPU latency for different stages (e.g., pipeline stage delays, memory access delays, cache miss penalties).
- **Utilization**: The usage of CPU resources (cores, caches, execution units).
- **Throughput**: The amount of work done in a given time period.
- **Efficiency**: The ratio of useful work done versus wasted work due to stalls, mispredictions, or inefficiencies.

## Analysis

### **Simulation Models:**

- **Cycle-Accurate Simulators**: Models CPU behavior at the cycle level. Example: **gem5**.
- **High-Level Simulators**: Use higher-level abstractions to model performance, such as **SimpleScalar** or **Simulink**.
- **Performance Profiling Tools**: Tools like **perf**, **VTune**, **gprof**, and **Tracy** help gather data from a real CPU to model performance.

### **Analytical Models:**

- **Roofline Model**: A graphical model showing the relationship between performance (e.g., FLOP/s) and available computational resources (e.g., memory bandwidth).
- **Little's Law**: Used to model queuing systems inside CPUs (e.g., instruction pipelines, memory access queues).

### **Performance Counters**

> See more in [Kernel Monitoring and Tracing Facilities](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/kernel-monitoring-and-tracing-facilities.md).
> 

| **Event Name** | **Description** | **Counter Type** | **Usage** |
| --- | --- | --- | --- |
| **CPU Cycles** | Total number of CPU cycles executed | Hardware | Measures the total clock cycles consumed by the CPU. |
| **Instructions** | Number of instructions executed | Hardware | Tracks how many instructions the CPU processes. |
| **Cache References** | Number of cache accesses | Hardware | Counts accesses to the cache hierarchy. |
| **Cache Misses** | Number of cache misses | Hardware | Tracks how many times data is not found in cache, leading to slower memory accesses. |
| **Branch Instructions** | Number of branch instructions executed | Hardware | Counts conditional and unconditional branch instructions. |
| **Branch Misses** | Number of mispredicted branches | Hardware | Tracks incorrect predictions made for branch instructions. |
| **L1 Data Cache Hits** | Number of hits in the L1 data cache | Hardware | Measures the number of cache hits in L1 data cache. |
| **L1 Data Cache Misses** | Number of misses in the L1 data cache | Hardware | Tracks cache misses in L1 data cache. |
| **L1 Instruction Cache Hits** | Number of hits in the L1 instruction cache | Hardware | Counts instruction fetches that hit in the L1 instruction cache. |
| **L2 Cache Hits** | Number of hits in the L2 cache | Hardware | Measures hits in the L2 cache (if available). |
| **L2 Cache Misses** | Number of misses in the L2 cache | Hardware | Tracks misses in the L2 cache (if available). |
| **LLC Misses** | Last-level cache misses (L3 or equivalent) | Hardware | Measures misses in the last-level cache (L3, or the deepest cache level). |
| **Page Faults** | Number of page faults (both minor and major) | Software | Tracks memory access violations where a page is not in memory. |
| **Context Switches** | Number of context switches between tasks | Software | Measures how often the CPU switches between different tasks (processes/threads). |
| **CPU Migrations** | Number of migrations of tasks between CPUs or cores | Software | Counts task migrations across CPU cores. |
| **Interrupts** | Number of interrupts serviced by the CPU | Hardware | Tracks how many hardware or software interrupts the CPU has handled. |
| **CPU Idle Time** | Amount of time the CPU spends in idle states | Software | Measures the time the CPU remains idle and doesn't perform any tasks. |
| **Task Clock** | Total CPU time consumed by tasks (both user and kernel modes) | Software | Measures the CPU time consumed by executing tasks, including user and kernel modes. |
| **CPU Utilization** | Percentage of time the CPU spends in different modes (user, system, idle) | Software | Provides the CPU's time breakdown: user time, system time, idle time. |
| **Memory Accesses** | Number of memory accesses | Hardware | Counts memory accesses performed by the CPU. |
| **DCache Load Misses** | Number of data cache load misses | Hardware | Tracks how many load operations miss the data cache. |
| **DCache Store Misses** | Number of data cache store misses | Hardware | Counts store operations that miss the data cache. |
| **TLB Misses** | Number of misses in the Translation Lookaside Buffer (TLB) | Hardware | Measures how many times memory address translations were not found in the TLB. |
| **Branch Mispredictions** | Number of mispredicted branch instructions | Hardware | Tracks how many branch predictions were incorrect, causing pipeline inefficiencies. |
| **Unhalted CPU Cycles** | Number of CPU cycles when the CPU is not in a halted state | Hardware | Measures active CPU cycles during non-idle states. |
| **Store Buffer** | Number of store buffer operations | Hardware | Tracks store operations buffered before being written to memory. |
| **Memory Bound** | Measures the time spent on memory-bound operations | Software | Identifies workloads bottlenecked by memory latency. |
| **Cache Writebacks** | Number of writebacks from cache to main memory | Hardware | Tracks how many times data is written back from the cache to memory. |
| **DRAM Read/Write** | Number of DRAM read/write operations | Hardware | Tracks the number of memory read/write operations to/from DRAM. |
| **CPU Stall Cycles** | Number of CPU cycles spent stalled waiting for resources | Hardware | Measures CPU cycle stalls due to resource waits (e.g., memory or cache). |
| **Cycles in Active State** | Number of CPU cycles spent in active state (not idle or sleeping) | Hardware | Measures how much time the CPU is actively processing tasks. |
| **L3 Cache Hits** | Number of hits in the L3 cache (if available) | Hardware | Tracks cache hits in the last-level cache (L3). |
| **L3 Cache Misses** | Number of misses in the L3 cache (if available) | Hardware | Measures misses in the last-level cache (L3). |

### **Analytical Frameworks**:

- **Performance Decomposition**: Break down overall performance into **latency**, **bandwidth**, and **contention** components.
- **Dataflow Graphs**: Model the flow of data through the CPU’s pipelines, execution units, and caches.

### Tools

| **Tool** | **Description** | **Use Cases** |
| --- | --- | --- |
| **top** | Displays an ongoing look at processor activity in real-time. | To monitor CPU usage and process statistics. |
| **htop** | An interactive process viewer, similar to top but enhanced. | To view detailed CPU usage with a user-friendly interface. |
| **mpstat** | Part of the sysstat package, reports CPU statistics. | To analyze CPU performance in detail. |
| **perf** | Performance analyzing tool in Linux. | To trace system calls, program execution, and hardware events. |

## Performance Tips

Here's a structured **CPU Performance Optimization Checklist** to help with performance tuning:

### **🔹 CPU Performance Optimization Checklist**

### **1️⃣ Branch Prediction & Control Flow**

✅ Reduce **branch mispredictions** (e.g., avoid unpredictable branches).

✅ Use **loop unrolling** and **if-else restructuring** to favor predictable branches.

✅ Leverage **compiler optimizations** (e.g., GCC’s `-march=native`, `-O3`).

✅ Utilize **likely/unlikely hints** (e.g., `__builtin_expect` in GCC/Clang).

### **2️⃣ Instruction-Level Optimization**

✅ **Minimize pipeline stalls** by reducing dependencies between instructions.

✅ Use **SIMD (Single Instruction, Multiple Data)** for parallel processing (`AVX`, `SSE`).

✅ Avoid **unnecessary memory fences** and excessive synchronization in multithreading.

### **3️⃣ CPU Caching & Memory Hierarchy**

✅ Optimize **data locality** (favor L1/L2 cache usage).

✅ Use **cache-aware algorithms** (e.g., blocking techniques in matrix operations).

✅ Align data structures for **cache line efficiency** (e.g., avoid false sharing in multithreading).

### **4️⃣ Parallelism & Multithreading**

✅ Use **thread affinity** to bind threads to CPU cores for better locality.

✅ Optimize **load balancing** to prevent idle CPU cores.

✅ Reduce **contention on shared resources** (e.g., use lock-free data structures).

### **5️⃣ CPU-Specific Tuning**

✅ Enable **hardware-specific optimizations** (`-march=native`, `-mtune` in GCC/Clang).

✅ Profile code using **perf, VTune, or Tracy** to identify bottlenecks.

✅ Optimize **NUMA (Non-Uniform Memory Access)** for multi-socket systems.

## References

- …