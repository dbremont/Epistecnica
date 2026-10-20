# RAM (Random-access Memory)

- [Memory](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/memory.md)

> A concise, structured note about volatile main memory used in modern computing systems. This document summarizes core concepts, internal organization, parallelism, performance characteristics, interfaces, system interactions, and vendor/technology comparisons.
> 

> **Note: Study Strategy** - Used a Set of Software Experiments in Order to **Better Understand RAM** Technical Objects.
> 

Experiments:

- Direct observation
- Latency/bandwidth characterization
- Allocator behavior
- Cache interaction
- Concurrency and contention
- NUMA and system effects
- Systems-level synthesis

Practice:

- Build a cache-aware hashmap
- Build a slab allocator
- Build a bump allocator
- Build a lock-free queue
- Build a memory pool
- Build a columnar data layout engine
- Build a cache simulator
- Build a userspace pager simulator
- Build a concurrent arena allocator
- Build a NUMA-aware work scheduler

## Formulation

**Definition & role.** Random‑Access Memory (RAM) is the primary volatile memory used by a processor to hold code and data that must be accessed with low latency and high bandwidth. RAM provides byte‑addressable storage where any location can be read or written in approximately constant time (subject to timing constraints and refresh for DRAM).

**Operating assumptions.** Typical RAM is volatile (contents lost on power removal), organized into addressable rows/columns within banks, accessed through a memory controller, and subject to electrical and timing constraints. DRAM (Dynamic RAM) dominates commodity systems; SRAM (Static RAM) is used for on‑chip caches.

**Key concepts.**

- *Latency* vs *bandwidth* tradeoff — small, random accesses are latency bound; large sequential transfers are bandwidth bound.
- *Memory hierarchy* — RAM sits between CPU caches (L1/L2/L3) and persistent storage; its behavior determines cache effectiveness and overall system throughput.
- *Logical vs physical addressing* — the OS and MMU abstract physical RAM into virtual memory regions.

## Terminology

| **Term** | **Definition** |
| --- | --- |
| **DRAM (Dynamic RAM)** | Volatile memory using a 1-transistor + 1-capacitor cell; requires refresh; high density, moderate latency; used as main system memory. |
| **SRAM (Static RAM)** | Volatile memory using 6-transistor latch-based cells; no refresh; very low latency, high power/area cost; used in CPU caches. |
| **Cell** | The smallest storage element (bit). DRAM: capacitor; SRAM: transistor latch. |
| **Row** | A horizontal collection of cells activated together; forms the basic DRAM “page” (8–32 KB). |
| **Column** | A vertical slice of a row; used to select which part of an active row is read or written. |
| **Row Buffer (Active Row)** | Local buffer in each DRAM bank that holds the currently open row; repeated accesses here are fastest (row hits). |
| **Bank** | Independent DRAM subarray allowing parallel activates/accesses; multiple banks per rank/module. |
| **Rank** | Group of DRAM chips operating in lockstep to present a single wide data interface. |
| **Channel** | A physical, independent memory interface with its own bus and controller; multiple channels increase bandwidth and concurrency. |
| **Burst Length** | Number of data transfers per column access (e.g., 8 or 16 in DDR); determines how many bytes you get per read/write. |
| **tRCD / tCL / tRP / tRAS** | Key DRAM timing parameters: activate-to-read delay, CAS latency, precharge delay, and minimum row active time. |
| **Refresh** | Periodic operation that restores charge in DRAM cells; increases latency and power consumption. |
| **Memory Controller** | Hardware that schedules DRAM commands, enforces timing constraints, manages refresh, and interfaces with the CPU. |
| **Cache Line** | Fixed-size memory block transferred between RAM and CPU caches (typically 64 bytes); fundamental granularity of caching. |
| **Locality (Spatial & Temporal)** | Patterns of repeated or nearby accesses that exploit cache behavior; row-major matrix access exploits spatial locality. |
| **MLP (Memory-Level Parallelism)** | Number of outstanding memory operations the system can process concurrently across banks/channels. |
| **NUMA (Non-Uniform Memory Access)** | Architecture where memory access latency depends on which CPU socket’s controller holds the data. |
| **ECC (Error-Correcting Code)** | Hardware technique that detects and corrects bit errors in memory using redundant bits; used in servers. |
| **HBM (High Bandwidth Memory)** | 3D-stacked DRAM connected via TSVs to provide extremely high bandwidth and lower power per bit. |
| **GDDR** | Graphics-oriented DRAM optimized for high throughput (GPU memory). |
| **NVM / PCM / ReRAM** | Non-volatile memory technologies (e.g., Phase-Change Memory) used for persistent or hybrid memory designs. |
| **DIMM / SO-DIMM / RDIMM / UDIMM** | Form factors and module types for system memory; differ in size, buffering, and server/workstation features. |
| **Frame** | Physical memory block in RAM that corresponds to a virtual page; the unit into which virtual memory pages are loaded. |

## Internal Structure

### Cell-level

- **DRAM cell:** one capacitor + one access transistor; stores charge that represents a bit and requires periodic refresh.
- **SRAM cell:** typically 6 transistors (6T) forming a bistable latch; fast and does not need refresh but consumes more area and static power.

### Array and bank organization

- **Subarray / mat:** small 2D grid of cells sharing local sense amplifiers.
- **Bank:** a larger unit composed of multiple subarrays. Banks can be activated independently to increase parallelism.
- **Ranks & channels:** a rank is a set of devices that present a single wide data bus to the memory controller; multiple ranks per channel and multiple channels per system increase concurrency and bandwidth.

### Peripheral circuits

- **Row decoder / Column decoder** — select wordlines and bitlines respectively.
- **Sense amplifiers** — detect and amplify the small voltages on bitlines during reads and restore cell charge on writes/reads.
- **Row buffer (active row)** — holds the currently activated row; accesses within the same row (page hits) are faster.
- **Precharge & restore circuits** — prepare bitlines and restore cell charge after access.

### Addressing & command flow

- Address multiplexing: many DRAM interfaces split a full address into row address and column address (e.g., RAS/CAS cycles).
- Typical command sequence: ACT (activate row) → READ/WRITE (column accesses, possibly burst) → PRE (precharge) or keep row open for subsequent accesses.

### Fetching Mechanism

> The fetching mechanism describes how a CPU or memory controller retrieves data from RAM. It involves translating a memory request from the CPU or DMA device into a sequence of DRAM commands that access the correct row, column, and bank, then returning the requested data over the memory bus.
> 

1. **Request initiation**
    - The CPU issues a read/write for a specific virtual address.
    - The memory management unit (MMU) translates it into a physical address.
    - The memory controller receives this physical address and determines the corresponding DRAM channel, rank, bank, row, and column.
2. **Row activation (ACT command)**
    - If the target row is not currently open in the bank, the controller issues an ACT command to open the row.
    - The entire row is loaded into the **row buffer** (active row) of the bank.
    - **Latency component:** `tRCD` (row-to-column delay).
3. **Column access (READ/WRITE command)**
    - Once the row is active, the controller issues a READ or WRITE command specifying the column address.
    - Data is transferred in bursts (length defined by the memory interface, e.g., 8 or 16 words for DDR).
    - **Latency component:** `tCL` (CAS latency).
4. **Precharge (PRE command)**
    - If another row in the same bank needs to be accessed, the current row must be closed (precharged) to prepare the bank for a new ACT command.
    - **Latency component:** `tRP` (precharge time).
5. **Data transfer**
    - Data moves from the row buffer to the memory channel over the data bus, synchronized with the memory clock and strobe signals (DQ/DQS).
    - Burst transfers exploit the row buffer to maximize throughput.
6. **Completion & acknowledgment**
    - The memory controller signals the CPU that data is ready (or the write is completed).
    - The CPU receives the data into registers or cache lines, potentially hitting the cache if already prefetched.

## Parallelism

**Forms of memory parallelism.**

- *Bank-level parallelism (BLP):* different banks can service requests independently (assuming independent banks and controller scheduling).
- *Channel-level parallelism:* multiple memory channels (with their own physical buses and controllers) provide aggregate bandwidth and concurrent access.
- *Rank and device interleaving:* OS/BIOS or hardware interleaving can distribute consecutive addresses across ranks/devices to improve throughput.
- *Memory-level parallelism (MLP):* number of outstanding memory operations a system (CPU+controller) can progress concurrently. MLP depends on the memory controller, row buffer hit rate, and request independence.

**Factors that limit or enable parallelism.**

- Timing constraints (e.g., tFAW, tRRD) that limit how many activates or refreshes can overlap.
- Row buffer conflicts: accesses to different rows in the same bank serialize and reduce effective parallelism.
- Command and address bus contention.

**Practical implications.**

- Software can improve effective parallelism by structuring memory accesses (stride, blocking) to reduce bank conflicts and increase row buffer locality.
- Hardware prefetchers, out‑of‑order CPUs, and memory controllers attempt to increase MLP by reordering and coalescing requests.

## Timing & Performance

**Latency components (DRAM-centric terms).**

- *Activation latency (tRCD):* time from ACT to first column access.
- *CAS latency (tCL):* delay from READ command to first data available.
- *Precharge time (tRP):* time to close a row and prepare for the next activation.
- *Row active time (tRAS):* minimum time a row must remain active after ACT.

**Bandwidth & throughput.**

- Determined by data rate (transfers per clock, e.g., DDR), bus width (bits), number of channels and ranks, and effective utilization (contending factors and refresh overhead).
- Achievable bandwidth differs for random small accesses vs large sequential bursts; sustained streaming gets close to peak bandwidth.

**Refresh overhead.**

- DRAM requires periodic refresh cycles for all rows; refresh consumes time and can stall or delay accesses depending on controller policy and refresh mode (per-bank refresh, all-bank refresh, self-refresh in low power states).

**Power & thermal behavior.**

- Active accesses incur dynamic power; background refresh and termination resistors add steady consumption.
- Higher frequency modules increase power and thermal dissipation requirements.

**Metrics & measurement.**

- Latency: measured in ns (or cycles) for random reads/writes.
- Bandwidth: GB/s measured for streaming workloads.
- MLP: often measured experimentally (see references) — important to understand how many concurrent requests the platform can sustain.

**Benchmarks:**

- [**lmbench**](https://github.com/intel/lmbench) – microbenchmarks for latency and bandwidth.
- [**mbw**](https://github.com/raas/mbw) – measures memory copy bandwidth.
- [**sysbench**](https://github.com/akopytov/sysbench) – general-purpose performance tests including memory.
- [**likwid**](https://github.com/RRZE-HPC/likwid) – advanced memory and cache benchmarking, per-channel analysis.

## Interface

**Physical and electrical interface.**

- *Modules:* DIMM/SO‑DIMM/UDIMM/other form factors exposing address/command/data pins.
- *Signaling:* DDR variants use double data rate signaling with strobes (DQS) and data lines (DQ). Modern topologies may use point‑to‑point (e.g., DDR4/DDR5 with fly‑by or point‑to‑point topologies) and differential signaling for command/address in some designs.

**Protocol and command set.**

- Fundamental DRAM commands include: ACT (activate), READ, WRITE, PRE (precharge), REF (refresh), and power management commands.
- Burst transfers: once a column is addressed, a multi‑beat burst supplies a sequence of data words (the burst length is an interface parameter).

**Memory controller responsibilities.**

- Translate CPU/cache requests into DRAM commands honoring timing constraints.
- Schedule requests to maximize throughput and fairness (schedulers: FRFCFS, QoS-aware variants, hazard avoidance).
- Manage refresh, low‑power transitions, and error handling (e.g., ECC integration).

## Interaction with Other Systems

**CPU and cache hierarchy.**

- CPU issues loads/stores which may hit in caches; misses generate memory requests to RAM. Cache line size, associativity, and replacement policy affect memory request patterns.
- Coherence protocols and memory ordering rules define visibility between multiple cores and I/O devices.

**Operating System & virtual memory.**

- OS manages physical page allocation, swapping/paging, and memory protection.
- Virtual memory adds indirection; page faults can cause large latency penalties.

**DMA / I/O devices / accelerators (GPU, NIC).**

- Devices may perform DMA into physical RAM regions; coherency and cache flush/invalidate semantics must be observed.
- GPUs sometimes have their own memory (GDDR or HBM); in unified memory systems, coherence between CPU and GPU memory domains is managed by driver/hardware.

**NUMA & multi-controller systems.**

- In NUMA architectures, access latency/bandwidth depends on which memory controller and channel owns a region. Proper allocation and thread placement are necessary to achieve locality.

**Security considerations.**

- Rowhammer-like phenomena: repeated activation patterns can lead to bit flips in adjacent rows; mitigations include increased refresh, targetted ECC, or architectural changes.
- DMA and physical memory access require IOMMU or driver protections to prevent unauthorized access.

## Technical Object

> Which are the types of memories?
> 

| **Technical Object Class** | **Description** | **Characterization** | **Evaluation** | **Usage** |
| --- | --- | --- | --- | --- |
| **DRAM (Dynamic RAM)** | Main system memory; stores code and data accessed by CPU | Moderate latency (~10–20 ns), high density, volatile, requires refresh | Measured by latency (tCL/tRCD/tRP), bandwidth (GB/s), refresh overhead, energy | General-purpose system memory in desktops, servers, laptops |
| **SRAM (Static RAM)** | Cache memory on CPU or in specialized devices | Very low latency (~1–5 ns), no refresh, lower density, higher power/area | Access time, stability under voltage/temperature variations, power consumption | L1/L2/L3 caches, small embedded buffers, register files |
| **HBM (High Bandwidth Memory)** | 3D-stacked DRAM for accelerators | Extremely high bandwidth, low per-bit energy, lower capacity per stack | Bandwidth per stack (GB/s), thermal performance, TSV reliability | GPUs, AI accelerators, HPC systems |
| **GDDR (Graphics DRAM)** | Specialized DRAM for high throughput | Optimized for sequential transfers, higher frequency than DDR, moderate latency | Bandwidth, frequency scaling, power per bit | GPU memory, graphics rendering, game consoles |
| **NVM / Persistent DRAM (PMEM, PCM, ReRAM)** | Non-volatile or hybrid memory | Retains data on power loss, lower endurance (for some types), higher latency than DRAM | Endurance, latency, bandwidth, persistence reliability | Fast persistence, hybrid main memory + storage systems, caching layers |
| **ECC Memory** | Error-correcting memory | Can detect/correct single-bit errors, optional multi-bit correction | Error detection/correction rate, latency overhead | Servers, mission-critical systems, high-reliability applications |
| **DIMM / SO-DIMM / RDIMM / UDIMM** | Physical modules hosting DRAM | Different ranks, buffered/unbuffered, standard form factors | Capacity, speed, number of ranks, ECC support | Desktop, server, laptop, embedded system memory expansion |
| **Memory + Computation (Processing-In-Memory / PIM)  (UPMEM - HBM‑PIM - GDDR6‑AiM)** | Memory devices capable of performing computations directly in memory | Reduces data movement, combines storage and logic, usually limited compute capability per cell | Measured by throughput for in-memory operations, energy savings vs traditional CPU/GPU, latency reduction | HPC, AI accelerators, data-intensive workloads, graph processing, real-time analytics |

## Vendor

| Model (example) | Description | Characterization | Technology | Vendor |
| --- | --- | --- | --- | --- |
| DDR4‑3200 UDIMM | Commodity desktop/server DIMM | Moderate latency, wide adoption, standard ECC/non‑ECC variants | DRAM (DDR4) | Various (Micron, Samsung, SK Hynix) |
| DDR5‑4800 RDIMM | Higher throughput, channel features (same/dual channel) | Higher bandwidth, on‑die ECC, power management improvements | DRAM (DDR5) | Major DRAM vendors |
| HBM2e (stacked) | High‑bandwidth stacked memory for accelerators | Very high bandwidth per package, low capacity per stack, interposer integration | 3D‑stacked DRAM, TSV | SK Hynix, Samsung, Micron |
| NVDIMM‑PM / NVDIMM‑N | Persistent/backup capable memory modules | Provides persistence or DRAM + NAND hybrid; used for fast persistence | DRAM + NAND / PMEM technologies | Vendor specific implementations |

## Practical

> 

### Performance Tip(s)

> Which performance tips are useful for a Software System Designer?
> 

| **Category** | **Tip** | **Description** |
| --- | --- | --- |
| **Program-Level** | Maximize spatial locality | Access memory sequentially; prefer arrays; group related fields to improve cache use. |
|  | Maximize temporal locality | Reuse recently accessed data; use **loop tiling/blocking** where applicable. |
|  | Align data | Align structs and arrays to cache line or SIMD boundaries. |
|  | Reduce pointer chasing | Minimize indirections; consider SoA layouts for better locality. |
|  | Improve branch predictability | Keep control flow predictable to avoid pipeline flushes. |
|  | Use SIMD / vector loads | Use vector instructions to move and process data in wide chunks. |
| **DRAM-Level (Software-Influenced)** | Avoid row buffer misses | Access memory with locality to increase the probability of row hits. |
|  | Exploit bank-level parallelism | Interleave data structures to spread accesses across memory banks indirectly. |
|  | Avoid bank conflicts | Design access patterns that don’t hammer the same physical memory region. |
|  | Use huge pages | Reduce TLB pressure and improve contiguity via huge pages (where appropriate). |
| **OS-Level Control** | NUMA-aware allocation | Allocate memory on the node where threads run; avoid remote memory. |
|  | Disable swapping / use `mlock()` | Prevent unexpected latency in real-time or critical loads. |
|  | Transparent Huge Pages (THP) | Decide whether THP helps or harms the workload; tune accordingly. |
| **Design Patterns** | Batch operations | Reduce overhead by operating on chunks instead of individual items. |
|  | Prefetching (manual/auto) | Use compiler or intrinsic prefetches to reduce wait time on critical loops. |
|  | Limit working set size | Keep hot data small enough to fit in cache levels. |
|  | Stream sequentially | Sequential memory access yields the highest effective DRAM throughput. |

### Toolbox

> Tools for analyzing memory hierarchy behavior, cache efficiency, DRAM performance, NUMA effects, and CPU microarchitectural bottlenecks.
> 

| **Tool** | **Description** | **Usage** | **Common Use Cases** |
| --- | --- | --- | --- |
| **perf** | Linux performance profiler for hardware counters and microarchitectural events. | `perf stat`, `perf record`, `perf report` to measure cache misses, stalls, IPC. | Identifying cache-thrashing, bad locality, pipeline stalls, branch mispredicts. |
| **Intel VTune Profiler** | Full-featured CPU, memory, and threading analyzer. | GUI or CLI to inspect memory-bound code, vectorization, threading, bandwidth. | HPC tuning, NUMA diagnosis, bandwidth bottlenecks, SIMD analysis. |
| **Valgrind (Cachegrind)** | Cache simulator modeling memory access patterns. | Run program under simulation; inspect I/D cache stats, function-level breakdown. | Finding poor locality, AoS→SoA conversions, struct layout problems. |
| **LIKWID** | Lightweight toolkit for reading counters and probing topology. | `likwid-perfctr`, `likwid-bench`, `likwid-topology`. | NUMA locality checks, bandwidth measurement, hardware topology inspection. |
| **numastat / numactl** | Tools for inspecting and controlling NUMA allocation. | Check cross-node memory access; bind memory or processes to nodes. | Avoiding remote NUMA access, improving latency in multi-socket systems. |
| **hwloc** | Hardware topology visualizer (sockets, cores, caches, NUMA). | Build system maps; decide thread pinning strategies. | Thread placement, memory-bound task scheduling, topology-aware design. |
| **pmu-tools (Intel)** | Tools for advanced hardware performance counter analysis. | “toplev.py” automatic bottleneck identification. | Determining if workload is Core-bound, Memory-bound, Frontend-bound, etc. |
| **perfetto** | Chrome/Android system tracing tool; also supports Linux tracing. | Record trace events over time; analyze scheduling, stalls, CPU use. | Real-time analysis, long-running server bottlenecks, OS-level latency. |
| **gprof / callgrind** | Traditional profilers for call graphs and CPU cycles. | Analyze hot paths and call structure. | Identifying functions responsible for most memory traffic. |
| **MSR Tools** | Read model-specific registers for hardware-level tuning. | `rdmsr` / `wrmsr` on Linux. | Low-level CPU inspection (advanced). |

## QA

### What is the optimal way to access a matrix in memory?

> When reading a matrix in RAM, **you should access it in *row-major order*** (left-to-right, then top-to-bottom) **if the language stores matrices in row-major format** (C, C++, Python/NumPy by default, Rust, Go, Java, etc.).
> 

This pattern aligns with how data is laid out in memory, allowing the CPU to use:

- **sequential memory accesses**
- **cache line prefetching**
- **spatial locality**
- **fewer cache misses**

## References

- https://en.wikipedia.org/wiki/Data-oriented_design
- https://en.wikipedia.org/wiki/AoS_and_SoA
- https://en.wikipedia.org/wiki/Random-access_memory
- https://en.wikipedia.org/wiki/Memory-level_parallelism
- https://en.wikipedia.org/wiki/Memory_access_pattern
- [‣](https://app.notion.com/p/289598edb79080359cb0e8e7f900da96?pvs=21)
- https://stackoverflow.com/questions/78489555/memory-level-parallelism-mlp-measurement
- https://lemire.me/blog/2018/11/05/measuring-the-memory-level-parallelism-of-a-system-using-a-small-c-program/
- [‣](https://app.notion.com/p/10e598edb790815f897cd8ad952c6e93?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081afb18bf2014c7f2e43?pvs=21)