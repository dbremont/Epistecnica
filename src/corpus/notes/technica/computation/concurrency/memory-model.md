---
tags: [note]
---

# Memory Model

- [Implicit Coordination Mechanism](/view.html?p=notes/technica/computation/concurrency/implicit-coordination-mechanism.md)

> A **memory model** is the contract between the program and the machine about which orderings of shared memory accesses a program may observe. It is what makes a concurrent program's correctness statable: the hardware and the compiler may reorder accesses, and the model fixes which reorderings are invisible and which must be excluded by explicit ordering.

## Memory Ordering

> In C++ and Rust the ordering is chosen per atomic operation. The five orderings are a lattice, not a menu:

| Ordering | Guarantees | Typical use |
| --- | --- | --- |
| `relaxed` | Atomicity only — no ordering with other accesses | Counters, statistics, flags where only the value matters |
| `acquire` | No later read or write may move before it | A lock's entry, a flag that publishes data |
| `release` | No earlier read or write may move after it | A lock's exit, the store that publishes data |
| `acq_rel` | Both, on a read-modify-write | The exchange that both reads and writes |
| `seq_cst` | A single total order over all sequentially consistent operations | The default; the strongest and the most expensive |

> A lock needs only `acquire` on entry and `release` on exit, and the asymmetry is the point: **the critical section is ordered by the pair, not by each operation being strongly ordered**. Under the default `seq_cst`, the unlock is compiled as a second locked read-modify-write; with `release` it is a plain store. On x86 that difference alone halves the cost of an uncontended lock and takes a four-thread contended one from 246 ns to 131 ns, with the energy falling from 64.9 J to 34.5 J.

> There is a second asymmetry, easier to miss: the loads in a **failed** spin can be `relaxed`. What orders the critical section is the exchange that *succeeds*, not the reads that fail — the failed reads only need to eventually see the new value, which is atomicity, not ordering. Ordering every attempt is what turns a test-and-test-and-set loop back into a line-thrashing one.

> The general rule: the model is a contract about *observable* orderings, so the cheapest correct ordering is the weakest one that excludes the reorderings on which the argument depends. Choosing `seq_cst` everywhere is correct and slow; choosing `relaxed` everywhere is fast and wrong.

## References

- https://en.wikipedia.org/wiki/Memory_model_(programming)
- [Optimizing a Spin-Lock](https://david.alvarezrosa.com/posts/optimizing-a-spin-lock/) — the acquire/release, test-and-test-and-set and backoff ladder measured in nanoseconds and joules
- [Atomic](/view.html?p=notes/technica/computation/concurrency/atomic.md) — atomicity without ordering
- [Concurrency](/view.html?p=notes/technica/computation/concurrency/concurrency.md) — the mechanism space these orderings serve
