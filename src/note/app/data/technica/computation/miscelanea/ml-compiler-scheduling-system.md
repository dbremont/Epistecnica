# ML Compiler Scheduling System


> An ML Compiler Scheduling System is a structured optimization and control system that maps computational representations (e.g., tensor operations, graphs, loop nests, kernels) onto executable execution plans through transformations such as ordering, tiling, fusion, partitioning, vectorization, parallelization, memory placement, and device mapping, with the objective of optimizing performance, efficiency, correctness, or resource utilization on a target execution architecture.
> 

> Note: Quite frankly, the term “optimization” is probably the most accurate high-level characterization of modern ML compiler scheduling systems. The term “scheduling” significantly understates the nature of the problem space, since these systems are not merely organizing execution order, but performing large-scale constrained optimization over execution structures, memory hierarchies, communication patterns, parallel decompositions, tensor layouts, and hardware mappings. In this sense, the schedule itself is better understood as an optimization artifact synthesized from exploration within a vast transformation and execution-design space.
> 

## Optimization Type Space

> Which are the possible optimization spaces that can be explored within an ML Compiler Scheduling System?
> 

| Sub Space | Category | Type | Description |
| --- | --- | --- | --- |
| Loop Organizations | Computation Structure Optimization | Loop Transformation Optimization | Optimization of loop structures through transformations such as tiling, interchange, skewing, strip-mining, unrolling, software pipelining, and fusion to improve locality, parallelism, and execution efficiency. |
| Fusion Strategies | Computation Structure Optimization | Kernel Fusion Optimization | Combination of multiple operations into fewer kernels to reduce memory traffic, synchronization, and launch overhead. |
| Fusion Strategies | Computation Structure Optimization | Kernel Fission Optimization | Decomposition of kernels into smaller units to improve parallelism, resource utilization, occupancy, or scheduling flexibility. |
| Computation Graph Structures | Computation Structure Optimization | Graph-Level Optimization | Optimization over computational graph structure including elimination, folding, canonicalization, pruning, and restructuring. |
| Dependency Structures | Computation Structure Optimization | Dependency Optimization | Reduction or restructuring of dependency constraints to expose additional concurrency or improve scheduling flexibility. |
| Execution Pipelines | Computation Structure Optimization | Pipeline Optimization | Optimization of staged execution pipelines, buffering, overlap, and throughput coordination. |
| Execution Organizations | Computation Structure Optimization | Execution Strategy Optimization | Optimization of the overall operational organization of computation across all transformation layers. |
| Tensor Layouts | Memory System Optimization | Tensor Layout Optimization | Optimization of tensor memory layouts, dimension ordering, blocking formats, alignment, packing, and storage representation to improve access efficiency and vectorization. |
| Memory Hierarchies | Memory System Optimization | Memory Hierarchy Optimization | Optimization of cache usage, shared memory placement, register allocation, prefetching, buffering, and locality management across memory hierarchy levels. |
| Memory Movement Patterns | Memory System Optimization | Data Movement Optimization | Reduction, restructuring, or overlapping of data transfers between memory regions, devices, nodes, or storage systems. |
| Register Usage Structures | Memory System Optimization | Register Allocation Optimization | Optimization of register usage, spilling, lifetime management, and allocation under architectural constraints. |
| Storage Interaction Structures | Memory System Optimization | Storage Optimization | Optimization of persistence, checkpointing, streaming, and external-memory interaction. |
| Parallel Decompositions | Parallel Execution Optimization | Parallelization Optimization | Optimization of task, data, pipeline, SIMD, SIMT, thread, warp, block, and distributed parallel execution structures. |
| Vectorization Schemes | Parallel Execution Optimization | Vectorization Optimization | Transformation of scalar operations into vector operations utilizing SIMD/vector hardware units efficiently. |
| Occupancy Structures | Parallel Execution Optimization | Occupancy Optimization | Optimization of hardware occupancy characteristics such as active warps, threads, or compute units. |
| Synchronization Structures | Parallel Execution Optimization | Synchronization Optimization | Optimization of synchronization structures, barriers, locks, dependencies, and coordination overhead. |
| Distributed Parallel Structures | Parallel Execution Optimization | Distributed Execution Optimization | Optimization of partitioning, sharding, synchronization, replication, and communication across distributed systems. |
| Device Mappings | Hardware Mapping Optimization | Device Placement Optimization | Determination of optimal mapping of operations or subgraphs onto CPUs, GPUs, TPUs, NPUs, FPGAs, or heterogeneous systems. |
| Hardware Capability Utilization | Hardware Mapping Optimization | Hardware-Specific Optimization | Exploitation of architecture-specific capabilities such as tensor cores, systolic arrays, cache topology, or instruction extensions. |
| Instruction Execution Structures | Hardware Mapping Optimization | Instruction Scheduling Optimization | Reorganization of low-level instruction sequences to improve pipeline utilization, latency hiding, and instruction-level parallelism. |
| Resource Allocation Structures | Hardware Mapping Optimization | Resource Utilization Optimization | Improvement of utilization efficiency for compute units, memory bandwidth, caches, interconnects, and accelerators. |
| Communication Strategies | Communication Optimization | Communication Optimization | Optimization of inter-device, inter-node, or inter-process communication patterns, synchronization, and collective operations. |
| Interconnect Topologies | Communication Optimization | Interconnect Optimization | Optimization of topology-aware communication routing, bandwidth utilization, and transfer scheduling. |
| Numerical Representation Structures | Numerical Optimization | Precision Optimization | Optimization of numerical precision formats such as FP32, FP16, BF16, INT8, FP8, or mixed precision execution. |
| Quantized Computational Structures | Numerical Optimization | Quantization Optimization | Transformation of models and operations into lower-precision integer or compressed numerical forms. |
| Sparse Computational Structures | Numerical Optimization | Sparsity Optimization | Exploitation of structured or unstructured sparsity patterns to reduce computation and memory requirements. |
| Numerical Error Structures | Numerical Optimization | Numerical Stability Optimization | Optimization to improve numerical robustness, stability, determinism, and error propagation behavior. |
| Operator Implementation Spaces | Algorithmic Optimization | Operator Selection Optimization | Selection among multiple algorithmic implementations or kernel variants for a computational operator. |
| Computational Method Structures | Algorithmic Optimization | Algorithmic Optimization | Replacement or restructuring of computational algorithms themselves to improve asymptotic or practical performance. |
| Runtime Behavioral Structures | Runtime Optimization | Runtime Adaptation Optimization | Dynamic optimization based on runtime workload characteristics or hardware state. |
| Dynamic Execution Organizations | Runtime Optimization | Dynamic Scheduling Optimization | Runtime adaptation of execution ordering, placement, or resource allocation under changing conditions. |
| Compiler Transformation Structures | Compiler System Optimization | Compilation Pipeline Optimization | Optimization of passes, IR transformations, pass ordering, and compiler subsystem coordination. |
| Compiler Execution Structures | Compiler System Optimization | Compilation-Time Optimization | Optimization of compiler execution cost, autotuning duration, search overhead, or compilation scalability. |
| Intermediate Representation Structures | Compiler System Optimization | Intermediate Representation Optimization | Optimization of IR structure, canonical forms, lowering pathways, and transformation legality. |
| Optimization Search Spaces | Search & Exploration Optimization | Search Space Optimization | Optimization of the optimization process itself, including schedule-space pruning, heuristic guidance, and cost-model learning. |
| Empirical Evaluation Spaces | Search & Exploration Optimization | Autotuning Optimization | Empirical exploration and evaluation of candidate schedules using runtime feedback or benchmarking. |
| Predictive Estimation Structures | Search & Exploration Optimization | Cost Model Optimization | Improvement of predictive models estimating performance, resource usage, or execution cost. |
| Schedule Exploration Structures | Search & Exploration Optimization | Schedule Search Optimization | Optimization of the process used to discover schedules, including evolutionary search, beam search, reinforcement learning, or stochastic exploration. |
| Latency Objective Spaces | Objective Optimization | Latency Optimization | Minimization of execution latency for inference or critical computational paths. |
| Throughput Objective Spaces | Objective Optimization | Throughput Optimization | Maximization of sustained computational throughput under workload constraints. |
| Energy Objective Spaces | Objective Optimization | Energy Optimization | Reduction of power consumption or energy-per-operation. |
| Thermal Constraint Spaces | Objective Optimization | Thermal Optimization | Optimization under thermal constraints or throttling behavior. |
| Constraint Satisfaction Spaces | Objective Optimization | Constraint Optimization | Optimization under formal hardware, memory, timing, correctness, or resource constraints. |
| Multi-Objective Tradeoff Spaces | Objective Optimization | Multi-Objective Optimization | Simultaneous optimization across competing objectives such as latency, throughput, energy, memory, and accuracy. |

## References

- [https://apxml.com/courses/compiler-runtime-optimization-ml/chapter-1-ml-execution-stack-challenges/ml-compiler-runtime-overview](https://apxml.com/courses/compiler-runtime-optimization-ml/chapter-1-ml-execution-stack-challenges/ml-compiler-runtime-overview)