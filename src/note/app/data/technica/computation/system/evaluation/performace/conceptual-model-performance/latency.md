# Latency


> Latency catalog & back of the guestimation.
> 

> Time ($ns$): Represents time measured in nanoseconds ($ns$).
> 

> Time ($μs$): Represents time measured in microseconds ($μs$).
> 

> Note: Every system under study should have it’s **latency profile**.
> 

QA:

- …

## Latency Catalog

> 

| **Category** | **Operation** | **Time (ns)** | **Time (μs)** | **Equivalent Human Time*** |
| --- | --- | --- | --- | --- |
|  | **L1 cache reference** | 0.5 ns | 0.0005 μs | 0.5 sec |
|  | **L2 cache reference** | 7 ns | 0.007 μs | 7 sec |
|  | **L3 cache reference** | 20 ns | 0.02 μs | 20 sec |
|  | **Main memory access (RAM)** | 100 ns | 0.1 μs | 1 min 40 sec |
|  | **Compress 1KB with Zippy** | 3,000 ns | 3 μs | 1.4 hours |
|  | **Send 1 KB over 1 Gbps network** | 10,000 ns | 10 μs | 4.6 hours |
|  | **Read from SSD** | 150,000 ns | 150 μs | 1.7 days |
|  | **Read from HDD** | 10,000,000 ns | 10 ms | 1 year |
|  | **Send packet CA → Netherlands** | 150,000,000 ns | 150 ms | 15 years |
|  | **Context Switch** | 1,000,000 ns | 1 ms | 1 week |
|  | **Process creation** | 20,000,000 ns | 20 ms | 3 months |
|  | **Disk I/O operation** | 100,000,000 ns | 100 ms | 10 years |
|  | **TCP handshake** | 150,000,000 ns | 150 ms | 15 years |
|  | **Select (syscall)** | 2,000,000 ns | 2 ms | 2 months |
|  | **Cache miss (L1 → L2)** | 20 ns | 0.02 μs | 20 sec |
|  | **Pipeline stall (1 cycle)** | 0.5 ns | 0.0005 μs | 0.5 sec |
| **Data Systems** | **Database query execution (simple)** | 100,000 ns | 100 μs | 1.7 days |
|  | **Database query execution (complex)** | 1,000,000 ns | 1 ms | 1 week |
|  | **Disk seek time (HDD)** | 5,000,000 ns | 5 ms | 2 hours |
| **Browsers** | **DOM manipulation (basic)** | 20,000 ns | 20 μs | 2.3 minutes |
|  | **CSS rendering** | 100,000 ns | 100 μs | 1.7 days |
|  | **JavaScript execution (single line)** | 50,000 ns | 50 μs | 12 minutes |
|  | **HTTP request round trip (local network)** | 200,000 ns | 200 μs | 2.3 days |
| **Java** | **Object creation** | 20,000 ns | 20 μs | 2.3 minutes |
|  | **Method call (local)** | 50,000 ns | 50 μs | 12 minutes |
|  | **Garbage collection (minor)** | 500,000 ns | 500 μs | 1.4 hours |
|  | **Garbage collection (major)** | 10,000,000 ns | 10 ms | 1 year |
| **C++** | **Function call (local)** | 50,000 ns | 50 μs | 12 minutes |
|  | **New object allocation (heap)** | 100,000 ns | 100 μs | 1.7 days |
|  | **Virtual function call** | 200,000 ns | 200 μs | 2.3 days |
|  | **Copy constructor (simple object)** | 200,000 ns | 200 μs | 2.3 days |
| **C** | **Function call (local)** | 20,000 ns | 20 μs | 2.3 minutes |
|  | **Malloc allocation** | 50,000 ns | 50 μs | 12 minutes |
|  | **Pointer dereferencing** | 10 ns | 0.01 μs | 1.2 seconds |
|  | **Stack allocation** | 10,000 ns | 10 μs | 4.6 hours |
| **Process Management** | **Thread creation (empty)** | 1,000,000 ns | 1 ms | 1 week |
|  | **Thread destruction** | 1,000,000 ns | 1 ms | 1 week |
|  | **Thread context switch (local)** | 10,000,000 ns | 10 ms | 1 year |
|  | **Thread context switch (remote)** | 50,000,000 ns | 50 ms | 5.7 days |
|  | **Thread synchronization (mutex lock acquire)** | 100,000,000 ns | 100 ms | 10 years |
|  | **Thread synchronization (mutex lock release)** | 50,000,000 ns | 50 ms | 5.7 days |
|  | **Thread synchronization (condition variable wait)** | 200,000,000 ns | 200 ms | 2.3 years |
|  | **Thread synchronization (semaphore wait)** | 50,000,000 ns | 50 ms | 5.7 days |
| **Atomic Operations** | **Atomic compare-and-swap (CAS)** | 50,000 ns | 50 μs | 12 minutes |
|  | **Atomic fetch-and-add** | 100,000 ns | 100 μs | 1.7 days |
|  | **Atomic increment** | 10,000 ns | 10 μs | 4.6 hours |
| **Interrupt Handling** | **Interrupt latency** (CPU reaction time) | 1,000 ns | 1 μs | 1.4 minutes |
|  | **Interrupt handling overhead** | 10,000 ns | 10 μs | 4.6 hours |
|  | **Interrupt vector table lookup** | 500 ns | 0.5 μs | 0.7 seconds |
|  | **Interrupt context switch** | 2,000,000 ns | 2 ms | 2 months |
|  | **Interrupt service routine execution** | 50,000 ns | 50 μs | 12 minutes |
| **I/O Operations** | **Disk read (HDD)** | 10,000,000 ns | 10 ms | 1 year |
|  | **Disk write (HDD)** | 20,000,000 ns | 20 ms | 3 months |
|  | **Network packet receive (100 Mbps)** | 100,000 ns | 100 μs | 1.7 days |
|  | **Network packet send (100 Mbps)** | 100,000 ns | 100 μs | 1.7 days |
| **File System** | **File system metadata access (seek time)** | 50,000 ns | 50 μs | 12 minutes |
|  | **File read operation (small)** | 150,000 ns | 150 μs | 1.7 days |
|  | **File write operation (small)** | 200,000 ns | 200 μs | 2.3 days |
|  | **File system mount** | 1,000,000 ns | 1 ms | 1 week |
| **Memory Management** | **Page fault (minor)** | 200,000 ns | 200 μs | 2.3 days |
|  | **Page fault (major)** | 10,000,000 ns | 10 ms | 1 year |
|  | **Memory allocation (malloc)** | 50,000 ns | 50 μs | 12 minutes |
|  | **Memory deallocation (free)** | 10,000 ns | 10 μs | 4.6 hours |
|  | **Memory paging swap in** | 1,000,000 ns | 1 ms | 1 week |
|  | **Memory paging swap out** | 1,500,000 ns | 1.5 ms | 1.4 weeks |
| **Scheduler** | **Process scheduling (preemptive)** | 10,000,000 ns | 10 ms | 1 year |
|  | **Process scheduling (non-preemptive)** | 1,000,000 ns | 1 ms | 1 week |
|  | **Time slice expiration** | 100,000 ns | 100 μs | 1.7 days |

## References

- https://en.wikipedia.org/wiki/Latency_(engineering)