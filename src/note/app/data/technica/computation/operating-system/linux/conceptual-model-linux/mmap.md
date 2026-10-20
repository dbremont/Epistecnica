---
tags: [ipc, memory-management, syscall]
---

# mmap

- [Linux Memory Management Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-memory-management-stack.md)

> `mmap` is a system call that creates a **memory-mapped region** by mapping a file or shared memory object into the **virtual address space** of a process. It provides a mechanism for **demand paging**, where the actual loading of data into physical memory is deferred until the memory is accessed (i.e., **page faults** trigger the loading of data). The mapping can be **private** (copy-on-write) or **shared** (changes are visible to other processes mapping the same region).
> 

QA:

- Which are the arguments against using mmap?

## Implementation

> 
1. **Virtual Memory Management**:
    - `mmap` interacts with the OS's **virtual memory subsystem** to allocate a region in the process's virtual address space.
    - The mapped region is backed by the **page cache** for file mappings or by anonymous memory for shared memory mappings.
2. **File System Integration**:
    - For file-backed mappings, `mmap` integrates with the **file system subsystem** to map file contents directly into memory.
    - Reads and writes to the memory region are translated into file I/O operations, with the OS handling **page caching** and **synchronization**.
3. **Page Tables and Page Faults**:
    - The OS sets up **page table entries** (PTEs) for the mapped region, marking pages as **not present** initially.
    - When the process accesses the memory region, a **page fault** occurs, prompting the OS to load the corresponding data from the file or shared memory into physical memory.
4. **Permissions and Protection**:
    - `mmap` allows specifying **memory protection flags** (e.g., `PROT_READ`, `PROT_WRITE`, `PROT_EXEC`) to control access to the mapped region.
    - The OS enforces these permissions using hardware-supported mechanisms (e.g., **MMU**).
5. **Synchronization**:
    - For shared mappings, changes to the memory region are propagated to other processes mapping the same region.
    - The OS ensures consistency through **page cache coherence** and **synchronization primitives**.
6. **Memory-Mapped I/O**:
    - `mmap` can be used for **memory-mapped I/O**, where hardware devices are mapped into memory, allowing direct access to device registers.

## Uses

> 
- **Efficient File I/O**: Large files can be accessed directly in memory, avoiding costly `read`/`write` system calls.
- **Inter-Process Communication (IPC)**: Shared memory regions enable fast data sharing between processes.
- **Memory-Mapped Devices**: Direct access to hardware device registers.
- **Dynamic Loading**: Shared libraries are loaded into memory using `mmap`.

## Case Studies

> `mmap` (memory mapping) is a versatile and powerful system call used in a wide range of applications and systems.
> 

Below are **case studies** of who uses `mmap` and for what purposes, categorized by domain and use case:

**Databases:  D**atabase systems like **PostgreSQL**, **MySQL**, and **Redis**.

- **Memory-mapped files**: Databases use `mmap` to map large data files (e.g., tables, indexes) into memory for efficient access.
- **Shared memory**: For inter-process communication (IPC) between database processes (e.g., shared buffers).
- **Persistence**: Changes to memory-mapped files are automatically written back to disk, ensuring data durability.

**High-Performance Computing (HPC):**  Scientific computing applications, parallel processing frameworks (e.g., **MPI**based programs).

- **Shared memory IPC**: Processes in a parallel application use `mmap` to share large datasets efficiently.
- **Memory-mapped I/O**: Large datasets (e.g., matrices, simulation results) are mapped into memory for fast access and processing.

**Operating Systems>:**  Linux kernel, system libraries (e.g., **glibc**).

- **Dynamic linking**: Shared libraries (e.g., `.so` files) are loaded into memory using `mmap`.
- **Process memory management**: The kernel uses `mmap` to allocate memory regions for processes (e.g., heap, stack).
- **Anonymous mappings**: Used for allocating large memory regions without file backing (e.g., `malloc` for large allocations).

**Multimedia and Gaming:**  Video game engines (e.g., **Unity**, **Unreal Engine**), multimedia frameworks (e.g., **FFmpeg**).

- **Texture and asset loading**: Game engines use `mmap` to load large assets (e.g., textures, models) directly into memory.
- **Video processing**: Multimedia applications map video files into memory for efficient frame-by-frame processing.

**File Systems and Storage:**  File systems (e.g., **ext4**, **ZFS**), storage applications (e.g., **SQLite**).

- **Efficient I/O**: File systems use `mmap` to cache frequently accessed files in memory, reducing disk I/O.
- **Journaling**: File systems map journal files into memory for fast writes and recovery.

**Real-Time Systems:**  Financial trading platforms, embedded systems, real-time operating systems (RTOS).

- **Low-latency IPC**: Real-time systems use `mmap` for shared memory communication between processes to minimize latency.
- **Memory-mapped hardware**: Embedded systems map hardware registers into memory for direct access (e.g., GPIO, DMA).

**Web Servers and Applications:**  Web servers (e.g., **Nginx**, **Apache**), web applications.

- **File serving**: Web servers use `mmap` to map static files (e.g., HTML, CSS, images) into memory for fast serving.
- **Caching**: Frequently accessed data is mapped into memory to reduce disk I/O.

**Machine Learning and Big Data:**  Machine learning frameworks (e.g., **TensorFlow**, **PyTorch**), big data tools (e.g., **Apache Spark**).

- **Large dataset processing**: Machine learning frameworks use `mmap` to map large datasets (e.g., training data) into memory for efficient access.
- **Shared memory IPC**: Distributed computing frameworks use `mmap` for fast data sharing between processes.

## Which are the arguments against using mmap?

> While `mmap` (memory mapping) is a powerful tool and is used in some database systems (e.g., MongoDB, SQLite), it is **not universally adopted** in database implementations. Many databases avoid using `mmap` due to several technical and practical limitations.
> 

 Below are the **key arguments against using `mmap` for databases**:

**Lack of Explicit Control Over I/O**

- **Problem**: `mmap` relies on the operating system's **page cache** and **demand paging** mechanisms, which means the database has no direct control over when data is read from or written to disk.
- **Impact**:
    - **Unpredictable performance**: The OS may evict critical pages from memory under memory pressure, leading to sudden performance degradation.
    - **Difficulty in prioritizing I/O**: Databases often need to prioritize certain operations (e.g., writing logs for durability), but `mmap` does not allow fine-grained control over I/O scheduling.

**Difficulty Handling Errors**

- **Problem**: `mmap` does not provide robust error handling mechanisms. For example, if a page fault occurs due to a corrupted file or disk error, the process may receive a **SIGBUS** or **SIGSEGV** signal, which is difficult to handle gracefully.
- **Impact**:
    - **Crash-prone**: Databases need to be highly reliable, but `mmap` can cause crashes if errors are not handled properly.
    - **Complex error recovery**: Recovering from memory-mapped file errors is more complex than handling traditional `read`/`write` errors.

**Memory Overhead**

- **Problem**: `mmap` maps entire files or large regions into memory, which can lead to **memory bloat** if the database accesses only small portions of the file.
- **Impact**:
    - **Inefficient memory usage**: Unused portions of the mapped file still consume virtual memory, which can lead to resource exhaustion.
    - **Increased swap pressure**: If the system runs low on memory, the OS may swap out parts of the mapped file, degrading performance.

**Portability Issues**

- **Problem**: The behavior of `mmap` can vary across different operating systems and file systems, leading to inconsistent performance and reliability.
- **Impact**:
    - **Cross-platform challenges**: Databases designed to run on multiple platforms may face difficulties ensuring consistent behavior with `mmap`.
    - **File system limitations**: Some file systems (e.g., network file systems like NFS) do not support `mmap` well, leading to errors or poor performance.

**Complexity of Synchronization**

- **Problem**: When using `mmap` for shared memory between processes, databases must implement additional synchronization mechanisms (e.g., locks, semaphores) to avoid race conditions.
- **Impact**:
    - **Increased complexity**: Managing shared memory regions adds significant complexity to the database implementation.
    - **Performance overhead**: Synchronization mechanisms can introduce latency, reducing the benefits of using `mmap`.

**Durability and Atomicity Challenges**

- **Problem**: Ensuring durability and atomicity of writes is difficult with `mmap` because changes to memory-mapped regions are not immediately written to disk.
- **Impact**:
    - **Data loss risk**: If the system crashes before dirty pages are flushed to disk, data may be lost.
    - **Complex write ordering**: Databases often need to enforce strict write ordering (e.g., write-ahead logging), but `mmap` does not provide guarantees about when writes are flushed to disk.

**Performance Issues with Large Databases**

- **Problem**: For very large databases, `mmap` can lead to **address space exhaustion** or **TLB (Translation Lookaside Buffer) thrashing**.
- **Impact**:
    - **Address space limitations**: On 32-bit systems, the virtual address space is limited, making `mmap` unsuitable for large datasets.
    - **TLB thrashing**: Frequent page table updates can degrade performance due to TLB misses.

**Lack of Support for Advanced Features**

- **Problem**: `mmap` does not support advanced database features like **compression**, **encryption**, or **checksumming** at the memory-mapped level.
- **Impact**:
    - **Additional overhead**: Databases must implement these features outside of `mmap`, reducing its efficiency.
    - **Reduced flexibility**: `mmap` cannot be easily integrated with custom storage engines or advanced data structures.

**Debugging and Maintenance Challenges**

- **Problem**: Debugging issues related to `mmap` (e.g., memory corruption, page faults) is more difficult than debugging traditional I/O operations.
- **Impact**:
    - **Increased development effort**: Database developers must invest significant time in debugging and maintaining `mmap`based code.
    - **Harder to diagnose issues**: Problems like memory leaks or corruption may be harder to trace when using `mmap`.

**Alternative Approaches Are Often Better**

- **Problem**: Many databases achieve better performance and reliability using **direct I/O** (e.g., `O_DIRECT` in Linux) or custom memory management instead of `mmap`.
- **Impact**:
    - **Fine-grained control**: Direct I/O allows databases to manage their own caching and I/O scheduling.
    - **Better performance**: Custom memory management can be optimized for specific workloads, outperforming `mmap` in many cases.

## Alternatives

> 

| **Alternative** | **Use Case** | **Pros** | **Cons** |
| --- | --- | --- | --- |
| **`read()` / `write()`** | Standard file I/O | Simple, portable | Requires manual copying of data |
| **`posix_fadvise()`** | Optimized file access | Improves caching, reduces page faults | Still requires `read()` / `write()` |
| **`madvise()` + `malloc()`** | Memory optimization | Helps optimize memory access patterns | No automatic file mapping |
| **Shared Memory (`shm_open()`, `shmget()`)** | Inter-process communication (IPC) | Fast, avoids unnecessary copying | Complex setup, requires synchronization |
| **Direct I/O (`O_DIRECT`)** | High-performance file access | Bypasses **page cache,** efficient for large reads | Requires aligned buffers, manual handling |
| **Memory Pooling (`jemalloc`, `tcmalloc`)** | Custom memory management | Reduces fragmentation, faster allocation | More complex than `malloc()` |
| **Direct Kernel Access (`syscall(SYS_pread64)`)** | Low-level file I/O | Lower overhead, avoids libc overhead | Less portable, requires careful handling |

## Performace

> 

## References

- https://en.wikipedia.org/wiki/MmapIPC
- https://stackoverflow.com/questions/78405249/performance-cost-of-keeping-a-mmap-of-a-huge-in-memory-file-around-400mb-versu
- https://db.cs.cmu.edu/mmap-cidr2022/
- https://news.ycombinator.com/item?id=25701959
- https://news.ycombinator.com/item?id=12566063
- https://github.com/freebsd/freebsd-src/tree/master/tools/tools/syscall_timing
- https://github.com/ArshanKhanifar/mmap-microbenchmark