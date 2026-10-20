---
tags: [unit-of-computation]
---

# Task


> The **Task Model** is a **computational framework** that provides a structured way to define, organize, and execute tasks in systems. It emphasizes **granularity**, **composition**, **dependencies**, and **coordination**,  making it a powerful tool for designing and analyzing systems that  involve concurrency, parallelism, and complex workflows. By abstracting 
computational work into tasks, the model enables efficient resource  management, scalability, and fault tolerance in modern computing  systems.
> 

The **Task Model** is a **formal abstraction** that represents **computational work** as a hierarchy of tasks, where:

1. **Tasks** are the fundamental units of computation, defined by their **input**, **output**, and **behavior**.
2. Tasks can be **atomic** (indivisible) or **composite** (composed of smaller tasks).
3. Tasks are organized into **levels of granularity**, from fine-grained (e.g., instructions, functions) to coarse-grained (e.g., workflows, pipelines).
4. Tasks may have **dependencies** (e.g., task A must complete before task B starts) and **constraints** (e.g., resource requirements, timing constraints).
5. Tasks are executed within a **runtime environment** that provides mechanisms for **scheduling**, **synchronization**, and **resource management**.
6. The model supports **concurrency** (multiple tasks executing simultaneously) and **parallelism** (tasks executing across multiple processors or nodes).
7. Tasks can be **stateful** (maintain internal state) or **stateless** (no internal state).
8. The model includes **coordination mechanisms** (e.g., locks, message passing) to manage interactions between tasks.

### Task Granularity

**Fine-Grained Concurrency**:

- Small units of work (e.g., instructions, memory accesses).
- Examples: Instruction-level parallelism (ILP), vector processing.

**Medium-Grained Concurrency**:

- Moderate units of work (e.g., threads, tasks).
- Examples: Multithreading, task parallelism.

**Coarse-Grained Concurrency**:

- Large units of work (e.g., processes, distributed tasks).
    - Examples: Distributed systems, microservices.

## References

- ..