---
tags: [storage-system]
---

# Share Memory Systems


Here's an exploration of different shared memory systems models presented in a table format:

| Share Memory Systems Model | Description | Examples |
| --- | --- | --- |
| Uniform Memory Access (UMA) | A memory architecture where all processors access memory with approximately the same latency, providing uniform access times regardless of the processor's proximity to memory modules. UMA systems typically use a single memory bus or interconnect, leading to symmetric access patterns. | Multiprocessor systems with a single memory bus, Symmetric Multiprocessor (SMP) systems, Some multicore processors architectures |
| Non-Uniform Memory Access (NUMA) | A memory architecture where memory access times may vary depending on the processor's proximity to memory modules. NUMA systems use multiple memory nodes or banks interconnected by high-speed interconnects, allowing processors to access local memory faster than remote memory. | NUMA servers, Enterprise servers with multiple memory banks, Some multicore processors with hierarchical memory organization |
| Cache Coherent NUMA (ccNUMA) | An extension of NUMA architecture where hardware mechanisms such as cache coherence protocols maintain memory consistency across multiple processor caches and memory modules. ccNUMA systems provide the illusion of a single shared memory space while still leveraging local memory access advantages. | Modern high-performance servers, Large-scale multiprocessor systems, Enterprise-grade servers with distributed memory architecture |
| Distributed Shared Memory (DSM) | A software-based approach to shared memory where the operating system or runtime system manages the illusion of a single shared memory space across physically distributed memory modules. DSM systems use coherence protocols and communication mechanisms to synchronize memory accesses. | DSM libraries and frameworks (e.g., TreadMarks, OpenMP DSM), Cluster computing systems, Some high-performance computing (HPC) systems |

These shared memory systems models provide different mechanisms for managing shared memory access in multiprocessor and multicore systems, each offering scalability, performance, and complexity trade-offs. Choosing the appropriate model depends on factors such as the workload characteristics, system architecture, and application performance requirements.

## References

- [Distributed Shared Memory](https://en.wikipedia.org/wiki/Distributed_shared_memory)
- https://en.wikipedia.org/wiki/Shared_memory