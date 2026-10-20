---
tags: [model-of-computation]
---

# External Memory Model of Computation


> In this note, we will explore a highly relevant model of computation: the **external-memory model of computation**, a key model for describing the computational behavior of **data systems**.
> 

> How to map  a set data computation into a  subset-data based computation?
> 

## Formulation

### What `technical problem` does the `External Memory Model of Computation` Solves?

> The **External-Memory Model of Computation** addresses the problem of computing over datasets whose size exceeds the capacity of fast internal memory.
> 

> Instead of assuming that the entire computational state is simultaneously and randomly accessible in working memory, the model assumes a **bounded internal memory** connected to a much larger **external memory** through a relatively expensive transfer mechanism.
> 

The central problem therefore becomes:

> **How can a computation whose logical input and state exceed working-memory capacity be executed correctly and efficiently through a sequence of data transfers between internal and external memory?**
> 

### How computation looks like?

> In-memory computation reformulated as staged computation over partial data. $f(D)⟶{f_1(D_1),f_2(D_2),…,f_n(D_n)}⟶\text{Compose}(⋯)$.
> 

> Computation operates over a large external data state through a bounded internal working state.
> 

> Data is **transferred in blocks**, computation is performed over the resident subset, intermediate state may be **materialized externally**, and subsequent computation retrieves additional subsets as required.
> 

> A global computation is therefore realized as an **orchestrated sequence of local computations and data transfers**.
> 

A general schema for computations in this model looks like:

```jsx
COMPUTE(D):
    C ← REFORMULATE(D)

    for each c in C:
        r[c] ← EXECUTE(c)

    return COMPOSE(r)
```

### What kinds of computations fit?

Computations with strong **locality, associativity, decomposability, or mergeability** characteristics:

- scanning
- filtering
- projection
- aggregation
- sorting
- grouping
- joins with appropriate partitioning
- external graph processing
- batch transformations
- indexing
- histogram construction
- large-scale statistical computation
- many dynamic-programming formulations
- divide-and-conquer algorithms

### **What kinds of computations do not fit easily?**

The difficult cases are computations where the result for one subset depends strongly on simultaneously observing arbitrary elements of other subsets.

> Can the global dependency structure be transformed into a sequence of externally materialized states without changing the computation's semantics?
> 

Examples include computations characterized by:

- extensive random access
- large mutable shared state
- global dependencies
- irregular access patterns
- non-decomposable intermediate state
- strong ordering dependencies
- algorithms whose working set intrinsically exceeds M

### What kinds of computations fit, but with major compromises?

These are computations that **can be externalized**, but only by accepting substantial changes in the execution strategy or cost profile.

Typical compromises include:

- multiple passes over the data;
- extensive intermediate materialization;
- large numbers of I/O operations;
- repartitioning or redistribution;
- external indexing;
- synchronization between stages;
- recomputation;
- increased latency;
- reduced parallelism;
- approximation or weaker semantics.

### What kinds of computations fit at all, even with compromises?

> The model is Turing-complete: every computation expressible in the RAM model can, in principle, also be expressed in the External-Memory Model (or Partial-Data Model).
> 

## Implementation

### What is the taxonomy of strategies (technical elements) used to carry out computation over subset-based data?

| Strategy Category | Element Set | Description |
| --- | --- | --- |
| **Decomposition** | Partitioning, range partitioning, hash partitioning, key partitioning, blocking, tiling | Decomposes a logically global dataset into subsets that can be processed within available resources. |
| **Data Access** | Scanning, indexed access, block access, sequential access, random access | Determines how subsets are located and made available for computation. |
| **Data Movement** | Block transfer, prefetching, buffering, caching, eviction | Moves and manages subsets between external storage and working memory. |
| **Local Computation** | Map, filter, projection, local sort, local aggregation | Performs computation independently over a memory-resident subset. |
| **Intermediate State** | Materialization, spilling, temporary storage, external state | Preserves partial computational state outside the bounded working memory. |
| **Repartitioning** | Shuffle, redistribution, repartitioning, reorganization | Changes the distribution of data when the next computation requires different subsets or co-location of related data. |
| **Recombination** | Merge, reduce, aggregation, join, concatenation | Combines independently computed partial results into a larger or final result. |
| **Execution Staging** | Stages, tasks, pipelines, execution boundaries, dependency graphs | Organizes partial computations into an executable sequence or dependency structure. |
| **Scheduling** | Task scheduling, partition ordering, data-local scheduling, cost-based scheduling | Determines when and in what order subsets and computational stages are processed. |
| **Memory Management** | Buffer pools, working sets, memory allocation, replacement policies, eviction | Controls the bounded internal memory available to active computation. |
| **Persistence** | Files, pages, segments, immutable runs, persistent structures | Represents computational state in external persistent storage. |
| **Recovery** | Checkpoints, logging, lineage, recomputation, replication | Allows computation to continue or recover when intermediate execution state is lost. |
| **Parallelism** | Data parallelism, task parallelism, partition parallelism, pipelining | Executes independent or partially independent subset computations concurrently. |
| **Synchronization** | Barriers, locks, latches, dependency coordination, commit points | Coordinates partial computations that have ordering or shared-state depende |

### How are the operators - that can composed any computation in this model implemented?

| Operator Category | Operator | Description | Implementation Technical Element Set |
| --- | --- | --- | --- |
| **Logical** | **Select (Filter)** | Selects elements satisfying a predicate. | Scan; predicate evaluation; block iterator |
| **Logical** | **Projection** | Selects or derives attributes from elements. | Record transformation; expression evaluation; block iterator |
| **Logical** | **Distinct** | Eliminates duplicate elements. | Hashing; sorting; duplicate elimination |
| **Logical** | **Sort** | Produces an ordered representation of the data. | External merge sort; run generation; multiway merge |
| **Logical** | **Join** | Combines elements from multiple datasets according to a matching condition. | Nested-loop join; hash join; sort-merge join |
| **Logical** | **Group By** | Organizes elements into groups according to a key. | Hash grouping; sorting; grouping iterator |
| **Logical** | **Aggregate (Reduce)** | Combines multiple elements into a smaller result. | Accumulator; aggregation function; hash aggregation; sort-based aggregation |
| **Execution** | **Partition** | Decomposes data into subsets for independent or staged processing. | Hash partitioning; range partitioning; partition metadata |
| **Execution** | **Stage** | Defines a bounded unit of execution. | Execution stage; task; pipeline; dependency graph |
| **Execution** | **Transfer** | Moves data between internal and external memory. | Block I/O; page read/write; DMA; I/O queue |
| **Execution** | **Buffer** | Maintains a memory-resident working region. | Buffer pool; memory frames; queues; double buffering |
| **Execution** | **Materialize** | Persists intermediate computational state externally. | Temporary files; spill files; pages; persistent data structures |
| **Execution** | **Merge** | Recombines independently produced intermediate results. | Merge iterator; multiway merge; stream merge |
| **Execution** | **Schedule** | Determines the order and timing of execution stages. | Execution plan; scheduler; dependency graph; task queue |
| **Execution** | **Synchronize** | Coordinates execution with inter-stage or concurrent dependencies. | Barrier; latch; lock; dependency constraint |
| **Execution** | **Checkpoint** | Persists execution state for recovery or continuation. | Snapshot; checkpoint record; log; recovery metadata |
| **Execution** | **Recompute** | Regenerates an intermediate state rather than retrieving it. | Execution lineage; deterministic computation; recomputation plan |
| **Execution** | **Cache** | Retains externally stored data in internal memory for reuse. | Buffer pool; cache; replacement policy |
| **Execution** | **Evict** | Removes resident data to make working memory available. | Replacement policy; page eviction; write-back |

## Performance

> How to model the computation complexity in this `model of computation`?
> 

> The External-Memory Model extends computational complexity with an explicit cost for data movement. Its primary complexity measure is the number of block transfers required to realize a computation as a function of input size N, internal-memory capacity M, and block size B.
> 

A general abstract cost model can be  ${\mathcal{K}( W,Q,S,P,L) }$ where:

- $W$ = computational work;
- $Q$ = block transfers / I/O complexity;
- $S$ = external storage and intermediate-state volume;
- $P$ = number of passes/stages;
- $L$ = locality/access behavior.
- K  means **computational cost.**

## QA

### Which are the related concepts?

- Expressivity
- Transformation
- Cost
- Semantics
- Scheduling
- Persistence
- Fault tolerance
- Locality
- Parallelism
- Storage topology
- Verification
- Evolution

### Which storage structures best support specific workload classes?

### How do concurrency, fault tolerance, and transactional guarantees interact with external-memory constraints?

### How do hardware trends (NVMe, persistent memory, disaggregated storage) reshape this computational paradigm?

## References

- Aggarwal, A., & Vitter, J. S. (1988). The input/output complexity of sorting and related problems. *Communications of the ACM, 31*(9), 1116–1127. [https://doi.org/10.1145/48529.48535](https://doi.org/10.1145/48529.48535)
- Vitter, J. S. (2001). External memory algorithms and data structures: Dealing with massive data. *ACM Computing Surveys, 33*(2), 209–271. https://doi.org/10.1145/384192.384193
- Arge, L., Goodrich, M. T., & Vitter, J. S. (2008). External memory algorithms. In J. E. Goodman & J. O'Rourke (Eds.), *Handbook of discrete and computational geometry* (2nd ed., pp. 1003–1017). Chapman & Hall/CRC.
- Garcia-Molina, H., Ullman, J. D., & Widom, J. (2009). *Database systems: The complete book* (2nd ed.). Pearson.
- Ramakrishnan, R., & Gehrke, J. (2003). *Database management systems* (3rd ed.). McGraw-Hill.