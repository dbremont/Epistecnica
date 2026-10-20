---
tags: [technique]
---

# Lock-Free Data Structure

- [Representation Problem: Associative Data](note.html?n=technica/computation/representation/conceptual-model-computational-representation/representation-problem-associative-data.md)

> A **lock-free data structure** is designed to allow multiple threads to operate on its elements concurrently without using mutual exclusions (locks), thus preventing threads from blocking each other and ensuring system-wide progress.
> 

## References

- [Non-blocking Algorithm](https://en.wikipedia.org/wiki/Non-blocking_algorithm)
- Cederman, Daniel, et al. "Lock‐Free Concurrent Data Structures." Programming multi‐core and many‐core computing systems (2017): 59-79.
- Timnat, Shahar, and Erez Petrank. "A practical wait-free simulation for lock-free data structures." ACM SIGPLAN Notices 49.8 (2014): 357-368.
- [A collection of lock-free data structures written in standard C++11](https://github.com/DNedic/lockfree)
- Fraser, Keir, and Tim Harris. "Concurrent programming without locks." ACM Transactions on Computer Systems (TOCS) 25.2 (2007): 5-es.
- …