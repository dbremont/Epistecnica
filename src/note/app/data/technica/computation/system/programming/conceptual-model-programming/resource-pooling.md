---
tags: [design-idiom, technique]
---

# Resource Pooling


> Maintains a pool of reusable objects for use by a group of clients.
> 

Guiding questions:

- How to evaluate the used of the technique in a certain context?
- How are the  pool usualy implemented? Most resource pools can be modeled as:
    - **Resource Set**: pre-created or lazily created instances
    - **Acquisition Function**: `borrow(resource)`
    - **Release Function**: `return(resource)`
    - **Lifecycle Policy**: creation, validation, eviction, timeout
    - **Scheduling Policy (optional)**: FIFO, LIFO, priority, fair share
    - **Capacity Constraint**: hard or soft limit on concurrent resources

## Instance(s)

| Resource Pool Type | Description |
| --- | --- |
| **Thread Pool** | Manages a fixed or dynamic set of OS threads used to execute queued tasks, amortizing thread creation cost and controlling concurrency. |
| **Connection Pool (DB)** | Maintains reusable database connections to reduce handshake/auth latency and limit backend overload. |
| **Socket Connection Pool (HTTP/TCP)** | Reuses persistent network connections (keep-alive) to avoid repeated TCP/TLS setup costs. |
| **Memory Pool (Fixed / Slab Allocator)** | Pre-allocates memory chunks of fixed size to reduce fragmentation and allocation overhead. |
| **Arena / Region Pool** | Allocates memory in bulk regions and frees everything at once, optimizing allocation speed and locality. |
| **Object Pool** | Reuses expensive-to-create objects instead of instantiating new ones repeatedly (common in games and simulations). |
| **Worker Pool (Generic Compute Pool)** | Abstract execution pool where workers process tasks; may be threads, processes, or fibers. |
| **Process Pool** | Maintains a set of pre-spawned OS processes for parallel execution with isolation (used in Python multiprocessing, web servers). |
| **Coroutine/Fiber Pool** | Lightweight execution units scheduled within threads; reduces context-switch overhead. |
| **GPU Command Pool** | Manages reusable GPU command buffers for efficient submission of rendering or compute workloads. |
| **File Descriptor Pool** | Controls allocation and reuse of OS file descriptors under resource constraints. |
| **Cache Pool (Object Cache / Resource Cache)** | Stores reusable computed or loaded resources (e.g., parsed templates, compiled queries). |
| **Buffer Pool** | Manages reusable I/O buffers to reduce allocation churn in networking or disk systems. |
| **HTTP Client Pool** | Maintains reusable HTTP client sessions with connection reuse and TLS session resumption. |
| **Kubernetes Pod Pool (Node-level abstraction)** | Logical grouping of reusable execution units scheduled on nodes (not a strict pool, but functionally similar in workload management systems). |

## References

- [**Connection Pool**](note.html?n=technica/computation/data-system/data-system-conceptual-model/connection-pool.md)