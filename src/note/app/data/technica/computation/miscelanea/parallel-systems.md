---
tags: [computer-system, parallelism]
---

# Parallel Systems


> **Parallelism via SIMD (Single Instruction, Multiple Data)**: It focuses on executing the same operation on multiple pieces of data simultaneously, often used in low-level optimization.
> 

> **GPU Parallelism**: Graphics Processing Units (GPUs) are used for parallel processing, especially in applications like graphics rendering and scientific computing.
> 

> **Task-Based Parallelism**: The focus is on decomposing tasks into smaller, manageable units of work that can be executed concurrently.
> 

> **Fork-Join Model**: A parallel programming model where a task is divided into smaller sub-tasks that are executed concurrently and then joined back together.
> 

> **Parallelism**: Many things running at the same time.
> 

## Models

Here's a comparison of parallel computation models presented in a table:

| Parallel Computation Model | Description | Example Applications |
| --- | --- | --- |
| SIMD (Single Instruction, Multiple Data) | Executes the same instruction simultaneously on multiple data elements. It is typically used for vectorized computations where operations can be applied parallel to arrays or vectors' elements. | Image processing, multimedia applications |
| MIMD (Multiple Instruction, Multiple Data) | Allows multiple processors to execute different instructions on different data concurrently, providing flexibility for executing diverse tasks independently or cooperatively. | Distributed computing, parallel algorithms |
| SPMD (Single Program, Multiple Data) | It runs the same program on multiple processors. Still, each processor may execute different parts of the program or process different data, often used in parallel programming frameworks. | High-performance computing, scientific simulations |
| Task Parallelism | Decomposes tasks into smaller, independent units of work that can be executed concurrently on multiple processors, providing fine-grained control over parallel execution and resource utilization. | Parallel algorithms, dynamic load balancing |
| Data Parallelism | Distributes data across multiple processors and executes the same operation simultaneously on each data element, enabling efficient parallel execution of operations on large datasets. | MapReduce, parallel matrix multiplication |
| Hybrid Models | Combines multiple parallel computation models to leverage their strengths, often integrating task and data parallelism to achieve efficient resource utilization and scalability. | MPI + OpenMP, CUDA + MPI |

## References

- State of The Art for Parallelism & Concurrency?
[https://www.reddit.com/r/ProgrammingLanguages/comments/19299ih/state_of_the_art_for_parallelism_concurrency/](https://www.reddit.com/r/ProgrammingLanguages/comments/19299ih/state_of_the_art_for_parallelism_concurrency/)
- - [Data-Parallel Actors: [A Programming Model for Scalable Query Serving Systems]](https://www.micahlerner.com/2022/06/04/data-parallel-actors-a-programming-model-for-scalable-query-serving-systems.html)