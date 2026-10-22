---
tags: [storage-system]
---

# Buffer Manager

- [Relational Data System Storage Management](note.html?n=technica/computation/data-system/data-system-conceptual-model/relational-data-system-storage-management.md)

> How is a database represented in memory, and how is data efficiently transferred between disk and memory?
> 

- Buffer Pool Manager

Control:

- Spacial Control
- Temporal Control

Representation:

- Buffer Pool

Uses:

- The DBMS needs memory for things other than just tuples and indexes.
- These other memory pools may not always backed by disk.  Depends on implementation.
    - Sorting + Join Buffer
    - Query Caches
    - Maintenance Buffers
    - Log Buffers
    - Dictionary Caches

## Buffer Pool Manager

![image.png](../assets/note/technica/computation/data-system/data-system-conceptual-model/buffer-manager/image.png)

### Page Directory

> The page directory is the mapping from page **ids** to page locations in the database files.
> 

### Page Table

> The page table keeps track of pages that currently in memory.
> 

> Metadata: Dirty Flag; Pin / Reference Counter; Access Tracking Information.
> 

### Frame

> A **frame** is a fixed-size slot in the **buffer pool** that temporarily holds a **page loaded from disk**. It serves as the in-memory container for a page, allowing the database system to read, modify, and write data efficiently without directly accessing disk for every operation.
> 

### Buffer Replacement Policy

> A **buffer replacement policy** is the set of rules a database management system (DBMS) uses to decide **which page in the buffer pool (frame) should be evicted** when a new page must be loaded from disk and the buffer pool is full. Efficient policies are crucial for minimizing disk I/O and maintaining high performance.
> 

> **Sequential Flooding** occurs when a database repeatedly reads large sequences of pages (e.g., full table scans) that **do not fit in the buffer pool**, causing frequently used pages to be **evicted prematurely**. This can severely degrade performance because the buffer pool is flooded with pages that are unlikely to be reused soon.
> 

> Circular Ring Buffer: …
> 

> Buffer Flushing: …
> 

| **Policy** | **Description** | **Notes** |
| --- | --- | --- |
| **LRU (Least Recently Used)** | Evicts the page that has been unused for the longest time. Assumes recently used pages are more likely to be accessed again. | Common in many DBMSs; may be approximated with counters or lists. |
| **MRU (Most Recently Used)** | Evicts the most recently accessed page. Useful in workloads with sequential scans. | Rare; sometimes used for special sequential scan optimizations. |
| **Clock / Second-Chance** | Pages are organized in a circular list with a reference bit. Gives a “second chance” to pages recently accessed. | Widely used in PostgreSQL buffer manager. |
| **LFU (Least Frequently Used)** | Evicts the page accessed least frequently over time. | More complex to maintain; sometimes used in caching systems. |
| **Random** | Evicts a randomly selected page. | Simple but can perform poorly in typical workloads; sometimes used as a fallback. |
| **Hybrid / Adaptive** | Combines policies based on workload or access patterns. | Oracle’s DB_CACHE_ADVICE or MySQL’s adaptive replacement algorithms. |
| LRU-K | Tracks the times of the last K references for each page and evicts the page with the oldest K-th reference. Balances recency and frequency. | Useful for workloads with mixed access patterns; reduces impact of sequential flooding. |
| **ARC:** Adaptative Replacement Policy | Dynamically balances recency and frequency by maintaining two LRU lists: one for recently used pages and one for frequently used pages. Pages migrate between lists based on access patterns. | Provides near-optimal cache performance under varying workloads; used in advanced caching systems like ZFS. |

### Optimization

| **Technique** | **Description** |
| --- | --- |
| **Multiple Buffer Pools** | Divides the buffer pool into separate pools for different types of workloads or data (e.g., one for OLTP hot pages, one for large sequential scans) to prevent interference and reduce sequential flooding. |
| **Pre-Fetching** | Reads pages into the buffer pool **before they are actually requested** by a query, often based on sequential access patterns, to hide disk latency and improve query performance. |
| **Scan Sharing** | Allows multiple queries performing the same or overlapping sequential scans to **share pages in memory**, reducing redundant I/O and improving throughput. |
| **Buffer Pool Bypass** | Large sequential scans or temporary operations can **bypass the main buffer pool** to prevent evicting frequently used “hot” pages, reducing cache pollution and improving overall performance. |

## Concurrency Control

| **Abstraction** | **Implementation** | **Description** |
| --- | --- | --- |
| **Lock  (Database Objects)** | Table-level lock, Row-level lock, Shared (S) / Exclusive (X) lock, Intent locks | A **logical mechanism** used to control access to database objects by transactions, ensuring **isolation and consistency**. Prevents conflicts between concurrent reads and writes. Locks can be held for the duration of a transaction (strict 2PL) or released earlier (non-strict 2PL). |
| **Latch (Internal Data Structures)** | Spinlock, Mutex, Reader/Writer latch | A **low-level, short-duration synchronization primitive** used internally by the DBMS to protect **in-memory data structures** (e.g., buffer pool frames, B-tree nodes) from concurrent access. Unlike locks, latches are **not transactional** and are released as soon as the operation completes. |

## Memory Mapping (mmap)

> The DBMS can use memory mapping (mmap) to store the contents of a file into the address space of a program.
> 

> The OS is responsible for moving the pages of the file in and out of memory, so the DBMS doesn’t need to worry about it.
> 

> DBMS (almost) always wants to control things itself and can do a better job than the OS. - Flushing dirty pages to disk in the correct order.
> 
- Specialized prefetching.
- Buffer replacement policy.
- Thread/process scheduling.

## Disk I/O

> See more in …
> 

## QA

- How to bypass OS Page Cache?
- …

## References

- [https://cs186berkeley.net/fa21/resources/static/notes/n04-BufferMgmt.pdf](https://cs186berkeley.net/fa21/resources/static/notes/n04-BufferMgmt.pdf)
- Crotty, Andrew, Viktor Leis, and Andrew Pavlo. "Are you sure you want to use mmap in your database management system?." CIDR. 2022.
- O'neil, Elizabeth J., Patrick E. O'neil, and Gerhard Weikum. "The LRU-K page replacement algorithm for database disk buffering." Acm Sigmod Record 22.2 (1993): 297-306.
- https://wiki.postgresql.org/wiki/Fsync_Errors
- https://www.interdb.jp/pg/index.html