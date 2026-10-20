---
tags: [technique]
---

# Technique


> 

QA:

- …

## Compression

> Use a faster compression algorithm like **LZ4** or **Snappy** to improve application performance.
> 

> Use GZIP compression to compress HTML, CSS, and JavaScript files.
> 

## **Encryption**

> Use a faster encryption algorithm like AES-GCM to improve application performance.
> 

## Data Structures

> Immutable data structures improve application performance by reducing the overhead of object copying.
> 

### **Augmented Data Structure**

> **Augmented data structures** are standard data structures that have been enhanced with additional information or capabilities to support more efficient queries, updates, or specific computations.
> 

## **Parallelization**

> Distributes processes or tasks across multiple processing units to run simultaneously.
> 

> Use asynchronous programming to improve application performance by allowing tasks to run concurrently.
> 

## **Memoization**

> Use memoization to improve application performance by caching function results.
> 

## **Lazy Loading**

> Delays the initialization of an object or data until it is actually needed to improve startup time.
> 

## **Code Minimization**

> Removes unnecessary code lines and combines statements to shorten and speed up execution.
> 

## **Loop Unrolling**

> Expands a loop into multiple iterations within the loop body to reduce the loop control overhead.
> 

## **Inlining**

> Replaces a function call with the function code itself to eliminate the overhead of the call.
> 

## **Pooling**

> Reuses objects from a set of initialized objects called a "pool" instead of creating new ones.
> 

## **Lazy Evaluation**

> Delaying the evaluation of an expression until its value is needed
> 

## Networking

> Use a faster network protocol like HTTP/2 to improve application performance.
> 

> Use a faster network card to improve application performance.
> 

## Distributed System

> Use load balancing to distribute traffic across multiple servers and improve website performance.
> 

> Use a **message queue** to improve application performance by decoupling **tasks** and enhancing scalability.
> 

## Catching

> The caching pattern avoids expensive re-acquisition of resources by retaining them in fast-access storage for repeated use.
> 

> Use a distributed cache to improve application performance by storing frequently accessed data in memory.
> 

## Operating System

> **Kernel Bypassing**:  Bypass the operating system kernel to reduce latency and increase performance in specific high-speed networking scenarios.
> 

> 

## Databases System

> Optimize Queries:   Optimize database queries to retrieve only the necessary data.
> 

> Use prepared statements to avoid SQL injection attacks and improve query performance.
> 

> Use connection pooling to reduce the overhead of opening and closing database connections. See more in [**Connection Pool**](note.html?n=technica/computation/data-system/data-system-conceptual-model/connection-pool.md).
> 

## DNS System

> Optimize DNS lookups to reduce the time it takes to resolve domain names.
> 

### **Use a Local DNS Cache** 🏠

- Configure **nscd (Name Service Cache Daemon)** or **systemd-resolved** to cache DNS queries.
- Use **Unbound** or **dnsmasq** for a lightweight local DNS cache.
- Reduces redundant queries and speeds up domain resolution.

### **Reduce Unnecessary Lookups** 🚀

- Avoid repeated queries by using **persistent connections** or **keep-alive** in web applications.
- Pre-resolve common domain names on application startup.

### **Use Faster DNS Resolvers** ⚡

- Switch to high-performance DNS servers like:
    - **Google DNS** (8.8.8.8, 8.8.4.4)
    - **Cloudflare DNS** (1.1.1.1)
    - **Quad9** (9.9.9.9)
    - **OpenDNS** (208.67.222.222)

### **Optimize TTL (Time-To-Live) Settings** ⏳

- Reduce TTL for dynamic domains (e.g., **CDNs, failover systems**).
- Increase TTL for stable domains to minimize query frequency.

### **Implement DNS Prefetching** 🔍

- **For browsers**: Use `<link rel="dns-prefetch" href="https://example.com">` to resolve domains before they're needed.
- **For applications**: Pre-resolve critical domain names at startup.

### **Use Anycast DNS for Global Optimization** 🌍

- Services like **Cloudflare, Google, and AWS Route 53** use Anycast to route queries to the nearest DNS server.
- Reduces latency by directing requests to the closest available resolver.

### **Minimize CNAME Chains** 🔗

- Excessive **CNAME (Canonical Name) records** add multiple resolution steps.
- Flatten DNS records where possible to avoid unnecessary lookups.

### **Optimize System-Level DNS Configuration** 🛠

- Edit **/etc/resolv.conf** to prioritize faster resolvers.
- Set `options rotate` and `options timeout` for better failover handling.

## Java Virtual Machine Performance Tips

> Optimize JVM performance by tuning GC algorithms (G1GC, ZGC), leveraging tiered JIT compilation (C1, C2, Graal), adjusting heap memory allocation (`-Xms`, `-Xmx`), enabling class data sharing (CDS), minimizing synchronization overhead with lock-free data structures, and utilizing profiling tools (JFR, Async Profiler) for runtime optimization.
> 

[Java HotSpot Virtual Machine](note.html?n=technica/computation/language-system/conceptual-model-language-system/java-hotspot-virtual-machine.md)

## Browser

> Use browser caching to store static files on the user’s browser and reduce server requests.
> 

## Programming Language

> Use **intrinsics** to improve application performance by accessing low-level hardware instructions.
> 

## Image

> Optimize images to reduce their size and improve loading times.
> 

## CPU

> Use a faster processor to improve application performance.
> 

> Use SIMD instructions to improve application performance by executing multiple operations in parallel.
> 

> Use vectorization to improve application performance by executing operations on arrays in parallel.
> 

## Pooling

> Object pooling improves application performance by reusing objects and reducing object creation overhead.
> 

> Thread pools can improve application performance by reusing threads and reducing thread creation overhead.
> 

## Compiler

### **Tail Call Optimization (TCO)**

> **Tail Call Optimization (TCO)** is a technique used by some programming languages and compilers to **optimize recursive function calls**, especially when the recursive call is the **last operation** in a function — called a **tail call**.
> 

> A **tail call** is when a function **calls another function (or itself)** and then **immediately returns** the result of that call — without doing any more computation afterward.
> 

Example in pseudocode:

```python
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n - 1, acc * n)  # <-- tail call
```

In this version of `factorial`, the recursive call is the last thing executed.

🧹 What’s the Optimization?

> Normally, every function call gets its own *stack frame* (used to track variables, return addresses, etc.). With **TCO**, the compiler **reuses the current function’s stack frame** instead of creating a new one, because nothing is left to do in the current function.
> 

> This avoids **stack growth** and prevents **stack overflow,** even for deep recursion.
> 

✅ When is TCO possible?

Only when:

- The recursive call is in **tail position** (nothing else is done afterward).
- There are **no pending operations** on the return value.
- The compiler/runtime **supports TCO** (e.g., Scheme, Haskell, some implementations of C, and with tricks in others like JavaScript or Python).

References

- https://news.ycombinator.com/item?id=43523741
- …

## References

- [Linux Process Management Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-process-management-stack.md)
- [‣](https://app.notion.com/p/1cbc0f5171ec8054998ddf3212e4916b?pvs=21)