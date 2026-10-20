---
tags: [model-of-computation]
---

# Von Neumann Model of Computation


> A sequential, imperative computational architecture characterized by a unified memory model in which instructions and data share the same address space, and execution is governed by a central processing unit (CPU) operating over a fetch-decode-execute cycle.
> 

The model includes:

- A **processing unit** (arithmetic logic unit + control unit),
- A **single read-write random-access memory** (RAM),
- A **program counter** (PC) to track instruction sequence,
- An **input/output subsystem** for external interaction,
- And a **linear instruction stream**, where both control flow and data dependencies are explicitly managed via memory and registers.

The Von Neumann model assumes a **global state** that is mutable over time, with computation defined as a **sequence of state transitions** induced by executing machine instructions. It underpins most classical computing architectures and is subject to the **Von Neumann bottleneck**, which limits performance due to the shared bus between instruction and data fetch.

## References

- https://en.wikipedia.org/wiki/Von_Neumann_architecture