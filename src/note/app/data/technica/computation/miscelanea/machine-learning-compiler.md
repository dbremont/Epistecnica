# Machine Learning Compiler


> In this note we explore Machine Learning Compiler Systems: computational systems that transform high-level machine learning representations into optimized executable programs across heterogeneous hardware targets.
> 

> From tensor representation → graph transformation → scheduling → kernel generation → executable device code.
> 

- Tensor Compiler
- Tensor  …

## Formulation

> A Machine Learning Compiler System is not merely a compiler in the traditional sense.
> 

### Which are the the element that integrated the a ML Compiler Stack?

> See
> 

| Element | Description | Role in the ML Compiler Stack |
| --- | --- | --- |
| **IR Systems** | Intermediate Representation (IR) infrastructures used to represent computation in structured, transformable forms across multiple abstraction levels. Examples include HLO, StableHLO, MLIR dialects, Relay, and Torch FX graphs. | Serve as the central representational substrate for analysis, optimization, lowering, transformation, and target-specific specialization throughout the compilation pipeline. |
| **Graph Rewriting Systems** | Systems that transform computational graphs through algebraic simplification, operator fusion, canonicalization, constant folding, dead code elimination, and pattern-based rewrites. | Optimize computational structure before low-level lowering, reducing execution overhead and improving hardware efficiency. |
| **Scheduling Systems** | Mechanisms that determine execution structure, including loop ordering, tiling, fusion strategy, vectorization, parallel decomposition, memory locality, and execution mapping. | Control how computations are physically organized and executed on hardware, strongly influencing throughput, latency, occupancy, and memory efficiency. |
| **Autotuners** | Adaptive optimization systems that empirically search optimization spaces to discover high-performance execution configurations. Examples include Ansor and AutoTVM. | Automatically explore scheduling and kernel parameter spaces to identify hardware-optimal execution strategies beyond manually engineered heuristics. |
| **Memory Planners** | Systems responsible for allocation planning, buffer reuse, tensor lifetime analysis, layout optimization, and movement minimization across memory hierarchies. | Optimize memory utilization, reduce allocation overhead, minimize data movement, and improve execution efficiency under accelerator memory constraints. |
| **Kernel Generators** | Systems that generate low-level hardware-specific computational kernels, often targeting CUDA, PTX, LLVM IR, SPIR-V, Metal, or accelerator-specific instruction sets. | Translate optimized tensor operations into executable compute kernels specialized for target hardware architectures. |
| **Runtime Systems** | Execution infrastructures responsible for orchestration, device dispatch, synchronization, stream management, dynamic execution, and heterogeneous resource coordination. | Execute and coordinate compiled computational artifacts across CPUs, GPUs, TPUs, and distributed accelerator environments. |
| **Hardware Abstraction Layers** | Interfaces and abstraction mechanisms that decouple compiler infrastructure from hardware-specific implementation details and device APIs. | Provide portability across heterogeneous hardware targets while exposing sufficient architectural information for optimization and specialization. |

### What a ML compiler stack is not?

> This makes modern ML compiler stacks closer to *heterogeneous computational orchestration systems* than classical source-to-binary compilers.
> 

It is usually a composite computational system integrating:

- IR systems,
- graph rewriting systems,
- scheduling systems,
- autotuners,
- memory planners,
- kernel generators,
- runtime systems,
- hardware abstraction layers.

## Case Study

System; Description; Note

## QA

### Is the concept of a ML Compiler just a bad concept?

> It is a pseudo-concept, but still a relevant and operationally useful term that aggregates multiple partially distinct computational systems under a shared engineering abstraction.
> 

> The concept of an “ML Compiler” possesses high epistemic leverage, combinatorial fluidity, and inferential productivity due to its capacity to unify tensor transformation, graph optimization, heterogeneous code generation, and accelerator-oriented execution reasoning within a single engineering abstraction, yet remains ontologically unstable and extensionally diffuse because its intentional boundary systematically collapses multiple partially orthogonal computational strata—IR infrastructures, scheduling systems, autotuners, runtime orchestrators, kernel DSLs, and execution substrates—into a semantically compressed category whose discriminative power and ontological parsimony degrade as modern ML systems increasingly integrate adaptive, distributed, and runtime-specialized computational behaviors beyond the classical compiler-theoretic frame.
> 

### What is the other related type of software?

| Category | Description |
| --- | --- |
| Deep Learning Frameworks | User-facing ML programming systems |
| Array Frameworks | Tensor/array computation abstractions |
| Graph Compilers | Computational graph optimization systems |
| Kernel DSLs | Languages for expressing GPU kernels |
| Accelerator Runtimes | Hardware execution/runtime layers |
| Distributed ML Systems | Multi-node training/execution systems |
| Autodiff Systems | Automatic differentiation engines |
| Numerical Computing Systems | General tensor/numerical computation platforms |

### Which is  a set of problem that can be used to upgrade my skill in the ML Compiler Stack Technical Element Set?

| Phase | Category | Problem | Description | Level | Role in Skill Development |
| --- | --- | --- | --- | --- | --- |
| **Phase I: Computational Representation Foundations** | Tensor IR | Build a Minimal Tensor IR | Design a small SSA-style tensor IR supporting tensor operations and matrix multiplication. | Beginner | Develops computational representation engineering skills. |
| Phase I: Computational Representation Foundations | Tensor IR | Implement Shape Inference | Add symbolic shape propagation across tensor operations. | Beginner | Builds tensor analysis and static reasoning capability. |
| Phase I: Computational Representation Foundations | Tensor IR | Construct an IR Printer | Serialize IR graphs into readable textual form. | Beginner | Improves IR introspection and debugging ability. |
| Phase I: Computational Representation Foundations | Tensor IR | Implement Graph Visualization | Export IR graphs into DOT/Graphviz form. | Beginner | Develops structural graph reasoning. |
| Phase I: Computational Representation Foundations | Tensor IR | Build an IR Parser | Parse a small tensor DSL into IR form. | Intermediate | Introduces frontend and lowering mechanics. |
| Phase I: Computational Representation Foundations | Tensor IR | Add Type Systems | Implement dtype and rank verification. | Intermediate | Develops compiler verification intuition. |
| Phase I: Computational Representation Foundations | Tensor IR | Implement SSA Transformation | Convert mutable representations into SSA form. | Intermediate | Introduces canonical compiler architecture principles. |
| **Phase II: Graph Transformation & Optimization Systems** | Graph Rewriting | Constant Folding Pass | Replace constant subgraphs with precomputed values. | Beginner | Introduces graph simplification mechanics. |
| Phase II: Graph Transformation & Optimization Systems | Graph Rewriting | Dead Node Elimination | Remove unused tensor operations. | Beginner | Develops dependency and reachability analysis. |
| Phase II: Graph Transformation & Optimization Systems | Graph Rewriting | Operator Fusion | Fuse chains of tensor operations into unified kernels. | Intermediate | Builds locality and execution optimization intuition. |
| Phase II: Graph Transformation & Optimization Systems | Graph Rewriting | Common Subexpression Elimination | Detect duplicated tensor subgraphs. | Intermediate | Develops equivalence reasoning over computational graphs. |
| Phase II: Graph Transformation & Optimization Systems | Graph Rewriting | Algebraic Simplification | Simplify tensor expressions symbolically. | Intermediate | Builds symbolic optimization capability. |
| Phase II: Graph Transformation & Optimization Systems | Graph Rewriting | Layout Transformation Pass | Transform tensor memory layouts. | Advanced | Develops hardware-aware graph optimization reasoning. |
| Phase II: Graph Transformation & Optimization Systems | Graph Rewriting | Dynamic Shape Rewriting | Rewrite graphs with partially symbolic dimensions. | Advanced | Introduces dynamic compilation complexity. |
| **Phase III: Scheduling & Execution Geometry** | Scheduling | Implement Loop Tiling | Tile matrix multiplication iteration spaces. | Beginner | Introduces locality optimization and execution geometry reasoning. |
| Phase III: Scheduling & Execution Geometry | Scheduling | Add Vectorization | Emit SIMD/vectorized loop structures. | Intermediate | Develops hardware execution-width reasoning. |
| Phase III: Scheduling & Execution Geometry | Scheduling | Parallel Loop Scheduling | Parallelize tiled computations with threading. | Intermediate | Builds concurrency-aware scheduling competence. |
| Phase III: Scheduling & Execution Geometry | Scheduling | Shared Memory Tiling | Implement GPU-style shared-memory tiling. | Advanced | Develops GPU memory hierarchy intuition. |
| Phase III: Scheduling & Execution Geometry | Scheduling | Operator Fusion Scheduler | Schedule fused kernels under dependency constraints. | Advanced | Builds global execution planning capability. |
| Phase III: Scheduling & Execution Geometry | Scheduling | Tensor Core Scheduling | Map tiled GEMMs to tensor-core-style execution. | Advanced | Introduces accelerator-oriented scheduling techniques. |
| Phase III: Scheduling & Execution Geometry | Scheduling | Polyhedral Scheduling Prototype | Implement affine loop transformation analysis. | Expert | Develops formal scheduling theory competence. |
| **Phase IV: Backend Lowering & Kernel Generation** | Kernel Generation | Generate Naive CUDA Kernels | Emit CUDA kernels from tensor IR. | Intermediate | Introduces backend code generation systems. |
| Phase IV: Backend Lowering & Kernel Generation | Kernel Generation | LLVM IR Codegen | Lower tensor operations into LLVM IR. | Intermediate | Builds low-level compiler backend understanding. |
| Phase IV: Backend Lowering & Kernel Generation | Kernel Generation | Triton Kernel Authoring | Write optimized Triton kernels. | Intermediate | Develops GPU kernel DSL proficiency. |
| Phase IV: Backend Lowering & Kernel Generation | Kernel Generation | PTX Inspection | Analyze emitted PTX assembly. | Advanced | Builds microarchitectural execution awareness. |
| Phase IV: Backend Lowering & Kernel Generation | Kernel Generation | Kernel Fusion Backend | Generate fused kernels from optimized graphs. | Advanced | Connects graph optimization to backend lowering. |
| Phase IV: Backend Lowering & Kernel Generation | Kernel Generation | Register Pressure Optimization | Reduce register spilling and optimize usage. | Advanced | Develops hardware resource optimization intuition. |
| Phase IV: Backend Lowering & Kernel Generation | Kernel Generation | Warp-Level Optimization | Optimize warp synchronization and memory access. | Expert | Introduces GPU execution topology reasoning. |
| **Phase V: Memory Planning & Data Movement Systems** | Memory Planning | Tensor Lifetime Analysis | Compute tensor allocation lifetimes. | Intermediate | Develops allocation scheduling understanding. |
| Phase V: Memory Planning & Data Movement Systems | Memory Planning | Buffer Reuse Planner | Reuse buffers across non-overlapping tensors. | Intermediate | Builds memory optimization intuition. |
| Phase V: Memory Planning & Data Movement Systems | Memory Planning | Arena Allocator | Build a tensor arena allocator. | Intermediate | Introduces low-overhead allocation systems. |
| Phase V: Memory Planning & Data Movement Systems | Memory Planning | Memory Cost Estimator | Estimate graph memory consumption. | Advanced | Develops resource modeling capability. |
| Phase V: Memory Planning & Data Movement Systems | Memory Planning | Layout Optimization | Optimize tensor layouts for locality. | Advanced | Introduces data-movement optimization reasoning. |
| Phase V: Memory Planning & Data Movement Systems | Memory Planning | Activation Checkpointing | Trade computation for memory savings. | Advanced | Develops memory-compute tradeoff understanding. |
| **Phase VI: Autotuning & Optimization Search Systems** | Autotuning | Tile Size Search | Search for optimal tile configurations. | Intermediate | Introduces empirical optimization systems. |
| Phase VI: Autotuning & Optimization Search Systems | Autotuning | Benchmark Harness | Build kernel benchmarking infrastructure. | Intermediate | Develops measurement and profiling discipline. |
| Phase VI: Autotuning & Optimization Search Systems | Autotuning | Scheduling Search Space | Represent scheduling choices formally. | Advanced | Builds optimization-space engineering capability. |
| Phase VI: Autotuning & Optimization Search Systems | Autotuning | Genetic Schedule Search | Use evolutionary search for schedule optimization. | Advanced | Introduces heuristic optimization systems. |
| Phase VI: Autotuning & Optimization Search Systems | Autotuning | Cost Model Construction | Predict kernel performance statistically. | Advanced | Develops compiler-performance modeling skills. |
| Phase VI: Autotuning & Optimization Search Systems | Autotuning | Reinforcement-Based Tuning | Use RL to optimize scheduling strategies. | Expert | Introduces ML-driven compiler optimization techniques. |
| **Phase VII: Runtime Orchestration & Execution Systems** | Runtime Systems | Build a Tensor Executor | Execute tensor graphs dynamically. | Intermediate | Introduces runtime orchestration systems. |
| Phase VII: Runtime Orchestration & Execution Systems | Runtime Systems | Device Dispatcher | Dispatch kernels across CPU/GPU backends. | Intermediate | Develops heterogeneous execution management skills. |
| Phase VII: Runtime Orchestration & Execution Systems | Runtime Systems | Asynchronous Execution Engine | Implement dependency-aware async execution. | Advanced | Builds execution scheduling competence. |
| Phase VII: Runtime Orchestration & Execution Systems | Runtime Systems | Stream Scheduler | Simulate GPU-style stream scheduling. | Advanced | Develops concurrency orchestration understanding. |
| Phase VII: Runtime Orchestration & Execution Systems | Runtime Systems | Distributed Tensor Runtime | Execute tensor graphs across multiple devices. | Expert | Introduces distributed execution systems. |
| Phase VII: Runtime Orchestration & Execution Systems | Runtime Systems | Fault-Tolerant Runtime | Recover from execution and device failures. | Expert | Develops resilient runtime infrastructure capability. |
| **Phase VIII: Integrated ML Compiler System Construction** | Integration | Build a Tiny ML Compiler | Implement an end-to-end tensor compiler prototype. | Advanced | Integrates all compiler stack layers. |
| Phase VIII: Integrated ML Compiler System Construction | Integration | Implement PyTorch Backend | Build a lowering backend for PyTorch FX graphs. | Advanced | Connects framework IRs to compiler systems. |
| Phase VIII: Integrated ML Compiler System Construction | Integration | Create a Tensor DSL | Design a DSL for tensor kernels and scheduling. | Advanced | Develops language/compiler co-design intuition. |
| Phase VIII: Integrated ML Compiler System Construction | Integration | Build a TVM-Style Scheduler | Recreate a simplified scheduling API and engine. | Expert | Deepens scheduling systems expertise. |
| Phase VIII: Integrated ML Compiler System Construction | Integration | Dynamic Shape Compiler | Compile graphs with symbolic tensor dimensions. | Expert | Introduces modern adaptive compilation systems. |
| Phase VIII: Integrated ML Compiler System Construction | Integration | Heterogeneous Runtime Stack | Coordinate execution across CPUs, GPUs, and accelerators. | Expert | Develops full-stack computational orchestration competence. |

## References

- https://docs.tinygrad.org/
- https://www.bremontix.xyz/lab/pro/Catalog/Good/Software/#text-editor (Need to Add More ML Production Tooling There)
- https://github.com/openxla/xla
- https://tvm.apache.org/
- https://mlir.llvm.org/
- https://openxla.org/
- [Concept](https://app.notion.com/p/Concept-71cc7d0f0ebc419abc49a9051d352579?pvs=21)