# Performace

> **Note:** This note delves deeper into performance evaluation and provides a comprehensive review of performance metrics for common components of a modern computational software system.
> 

## Formulation

> The performance of a computational software system is quantitatively defined by its ability to optimize resource utilization—such as CPU cycles, memory bandwidth, I/O throughput, and network latency—while minimizing execution tipme, maximizing throughput, maintaining scalability under variable workloads, and ensuring deterministic responsiveness within specified operational constraints.
> 

## System Type Space

> What is the system being analyzed?  What is the performance model used for evaluation? What evaluation workload is being used for testing?
> 

> **System Characterization** is the process of thoroughly understanding and describing the behavior, properties, and performance of a system or component through data analysis, modeling, and assessment.
> 

> A **system model for monitoring** typically consists of sensors and instrumentation for data acquisition, processing units for data analysis, and interfaces for data display and user interaction, all integrated to track and manage the operational status of systems or environments.
> 

> See more in See more in Computational Complexity (Theoretical Performance Model)
> 

> Which are the parts that makes a software system?
> 

| **Category** | **System Component** | **Description** |
| --- | --- | --- |
| **Hardware** | CPU | Executes instructions; core processing unit. |
|  | Memory (RAM) | Volatile storage for active processes and data. |
|  | Storage (Disk/SSD) | Persistent data storage. |
|  | Network Interface | Hardware for communication between systems. |
|  | GPU | Specialized processor for graphics and parallel compute workloads. |
| **OS / Kernel** | Process Scheduler | Manages CPU time among processes. |
|  | Memory Manager | Allocates, tracks, and protects memory usage. |
|  | File System | Organizes and provides access to stored files. |
|  | Device Drivers | Interface between hardware and the OS. |
|  | Networking Stack | Manages communication protocols and sockets. |
| **Middleware / Runtime** | Virtual Machine (JVM, CLR) | Executes managed code in a controlled runtime. |
|  | Interpreter | Directly executes high-level instructions (e.g., Python). |
|  | Runtime Libraries | Provide system calls, I/O handling, math, and OS abstractions. |
|  | Container Runtime | Manages isolated execution (Docker, containerd). |
| **Software Infrastructure** | Library | Reusable precompiled code for common functionality. |
|  | Framework | Structured foundation for building applications (e.g., .NET, Django). |
|  | Package Manager | Installs and manages libraries (npm, pip, NuGet). |
| **Application Layer** | Node (Process/Service) | Individual running instance of an application. |
|  | Microservice | Independent service exposing APIs in a distributed system. |
|  | API | Interface for communication between components. |
|  | UI Component | User-facing interaction elements. |
| **Data Management** | Database | Structured storage and query system. |
|  | Cache | High-speed storage for frequently accessed data. |
|  | Message Queue | Component for async communication (Kafka, RabbitMQ). |
|  | Configuration Store | Holds system/application configuration parameters. |
| **Cross-Cutting** | Logging System | Records events for debugging and monitoring. |
|  | Monitoring/Telemetry | Collects performance and health data. |
|  | Security Layer | Authentication, authorization, encryption modules. |
| **Algorithms** | … | … |

### Networking Stack

> See [Linux Network Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-network-stack.md).
> 

## Performance Model

> How to we evaluate the system? Which are the set of metrics? What is the expected behavior of the system?
> 

### Evaluation Model

| **Category** | **Component** | **Metric** | **Description** |
| --- | --- | --- | --- |
| **Hardware** | CPU | Utilization % | Portion of CPU cycles actively used. |
|  |  | Instructions per Cycle (IPC) | Efficiency of instruction execution per clock. |
|  |  | Context Switch Cost | Overhead of switching between processes/threads. |
|  | Memory (RAM) | Latency (ns) | Time to access a memory cell. |
|  |  | Bandwidth (GB/s) | Rate of data transfer between CPU and memory. |
|  |  | Page Fault Rate | Frequency of missing required pages in RAM. |
|  |  | Fragmentation % | Inefficient memory allocation waste. |
|  | Storage (Disk/SSD) | IOPS | Number of I/O operations per second. |
|  |  | Throughput (MB/s) | Sustained data transfer rate. |
|  |  | Latency (ms) | Delay in completing an I/O request. |
|  |  | MTBF | Expected durability of the device. |
|  | Network Interface | Bandwidth | Maximum data transfer rate. |
|  |  | Latency | Time for a packet round-trip. |
|  |  | Packet Loss | Percentage of lost packets. |
|  |  | Jitter | Variability in packet delivery time. |
|  | GPU | FLOPS | Floating-point operations per second. |
|  |  | Memory Bandwidth | Data transfer rate between GPU and VRAM. |
|  |  | Utilization % | Active GPU usage percentage. |
|  |  | Kernel Execution Time | Time to complete GPU tasks. |
| **OS** | Process Scheduler | Scheduling Latency | Delay before a process gets CPU time. |
|  |  | Fairness | Distribution balance of CPU among processes. |
|  |  | CPU Utilization Efficiency | Ratio of productive to wasted cycles. |
|  |  | Context Switch Time | Time to switch process states. |
|  | Memory Manager | Allocation Latency | Time to allocate memory. |
|  |  | Page Faults | Rate of secondary storage lookups. |
|  |  | Fragmentation % | Memory wasted due to allocation gaps. |
|  |  | Protection Overhead | Cost of enforcing isolation/security. |
|  | File System | Read Throughput | Speed of reading files. |
|  |  | Write Throughput | Speed of writing files. |
|  |  | Metadata Ops Latency | Cost of operations like open, stat, chmod. |
|  |  | Journal Overhead | Performance cost of journaling. |
|  | Device Drivers | Interrupt Latency | Time to handle hardware interrupts. |
|  |  | CPU Overhead | Extra CPU cycles used by driver ops. |
|  |  | Stability | Reliability and error frequency. |
|  | Networking Stack | Throughput | Packets/bytes per second processed. |
|  |  | Connection Setup Latency | Time to establish TCP/UDP connections. |
|  |  | System Call Overhead | Cost of socket operations. |
|  |  | Error Handling Efficiency | Speed and robustness of recovery. |
| **Langauge System** | VM (JVM, CLR) | Startup Latency | Time to launch runtime. |
|  |  | JIT Compilation Cost | Overhead of runtime code compilation. |
|  |  | GC Pause Time | Delay during garbage collection. |
|  |  | Bytecode Execution Throughput | Instructions executed per second. |
|  | Interpreter | Instruction Rate (ops/sec) | Execution speed of high-level code. |
|  |  | Memory Overhead | RAM used beyond program data. |
|  |  | Function Call Latency | Time to execute high-level function calls. |
|  | Runtime Libraries | Syscall Latency | Delay when invoking OS services. |
|  |  | I/O Efficiency | Performance of read/write helpers. |
|  |  | Error Handling Overhead | Cost of exception or error management. |
|  | Container Runtime | Startup Time | Time to launch a container. |
|  |  | Shutdown Time | Time to stop a container. |
|  |  | Isolation Overhead | Extra resource cost of namespace/cgroup isolation. |
|  |  | Resource Limits Enforcement | Accuracy/efficiency of quota enforcement. |
| **Software Infra** | Library | Load Time | Time to import/init. |
|  |  | Memory Footprint | RAM consumption during usage. |
|  |  | Execution Efficiency | Overhead of abstractions. |
|  | Framework | Request Latency | Time per request served. |
|  |  | Throughput | Requests/sec supported. |
|  |  | Abstraction Overhead | Cost introduced by framework layers. |
|  | Package Manager | Dependency Resolution Speed | Time to resolve versions/dependencies. |
|  |  | Installation Time | Time to install packages. |
|  |  | Cache Efficiency | Speedup from cached downloads. |
| **Application Layer** | Node (Service) | Latency | Time to process a request. |
|  |  | Throughput | Requests/sec per node. |
|  |  | Resource Footprint | CPU/RAM consumption. |
|  |  | Reliability (MTTF) | Average uptime before failure. |
|  | Microservice | Response Time | End-to-end service latency. |
|  |  | Scalability | Requests/sec under scaling. |
|  |  | Inter-service Latency | Delay in service-to-service calls. |
|  |  | Resilience | Recovery speed from failures. |
|  | API | Latency | Request round-trip time. |
|  |  | Error Rate | % of failed requests. |
|  |  | Availability % | Uptime adherence to SLA. |
|  |  | Compliance | Conformance to API contract. |
|  | UI Component | Rendering Latency | Time to display elements. |
|  |  | Interaction Delay | Delay from user input to response. |
|  |  | Resource Usage | CPU/GPU/RAM overhead of UI. |
|  |  | UX Score | User experience quality (measured). |
| **Data Management** | Database | Query Latency | Time per query. |
|  |  | Throughput (TPS) | Transactions per second. |
|  |  | Replication Lag | Delay in replicas updating. |
|  |  | ACID Compliance Cost | Overhead of ensuring guarantees. |
|  | Cache | Hit Ratio | % of requests served from cache. |
|  |  | Eviction Rate | % of entries replaced. |
|  |  | Access Latency | Time to serve from cache. |
|  |  | Memory Footprint | RAM used by cached data. |
|  | Message Queue | Publish Latency | Time to enqueue a message. |
|  |  | Consume Latency | Time to deliver a message. |
|  |  | Throughput (msg/s) | Messages per second handled. |
|  |  | Durability | Guarantee of persistence until delivery. |
|  | Config Store | Access Latency | Time to fetch a config entry. |
|  |  | Consistency | Accuracy of config across replicas. |
|  |  | Fault Tolerance | Availability during failures. |
| **Cross-Cutting** | Logging System | Write Latency | Time to record a log entry. |
|  |  | Overhead per Entry | CPU/memory cost of logging. |
|  |  | Throughput | Log entries/sec handled. |
|  |  | Retention Cost | Storage cost for logs. |
|  | Monitoring/Telemetry | Collection Overhead | Extra CPU/RAM from metrics collection. |
|  |  | Sampling Rate | Frequency of collected metrics. |
|  |  | Accuracy | Precision of reported metrics. |
|  |  | Alert Latency | Time to detect and notify on events. |
|  | Security Layer | Authentication Latency | Time to validate identity. |
|  |  | Encryption Overhead | Performance cost of cryptography. |
|  |  | False Positive Rate | Incorrect security alerts. |
|  |  | False Negative Rate | Undetected security breaches. |

### Service Level Agreements (SLAs)

> **Service Level Agreements (SLAs)** are formal contracts between service providers and clients that define the expected level of service, including performance metrics, uptime, response times, and other key service criteria.
> 

## Workload

> 

## Data Collection

> How?  Instrumentation - Benchmarks / Real Time Data Collection /  Off-Line Data Collection
> 

> Telemetry / Monitoring / Observability Tools > Observability System.
> 

> Using `Model of the Computing System` collects the metrics require to create the vivit  imitation of the system.
> 

> **Instrumentation** refers to the development, use, and management of devices and systems designed to measure, monitor, and control physical quantities, processes, and operations.
> 

> **Instrumentation** refers to the process of strategically embedding code and tools within software to monitor, collect, and analyze data about its performance, behavior, and usage.
> 

> **Data Collection Formats (Metrics, Logs, Traces)**: Data collection using formats involves gathering information (from an instrumented data source) in specific structures or types. Metrics represent quantitative measurements, logs capture detailed records of events or transactions, and traces follow a process or transaction flow across a system. Collecting data in these formats is essential for performance monitoring, troubleshooting, and analyzing system behavior.
> 

> ¿What **data to collect** / and how to **collect the data**?
> 

> **Observability Models** refer to the methodologies and practices used to monitor and gain insights into complex systems, such as distributed applications and infrastructure. These models typically consist of key components and principles.
> 

> **Instrumentation** refers to the development, use, and management of devices and systems designed to measure, monitor, and control physical quantities, processes, and operations.
> 

### Principle

- [ ]  Rule: Always measure one level deeper.

### Technique

> 

## Data Analysis

> Using `Model of the Computing System`  and the data collected / create a  a vivit imitation of the system; that allows supervisors to make sentence.
> 

## Performance Problem

> Here's an updated version of the **Software Performance Issues Taxonomy**, incorporating **Contention** as a key issue under the **Multithreading and Concurrency** category.
> 

| **Category** | **Performance Issue** | **Description** |
| --- | --- | --- |
| **Computational Efficiency** | **Algorithm Complexity** | Inefficient algorithms lead to high time complexity, slowing performance. |
|  | **Excessive Computation** | Unnecessary or redundant calculations impact the overall system performance. |
|  | **Inefficient Data Structures** | Poorly chosen data structures increase time complexity for data access and manipulation. |
| **Memory Usage** | **Memory Leaks** | Memory is not properly deallocated, causing the system to run out of memory. |
|  | **Excessive Memory Consumption** | The application consumes more memory than necessary, leading to slowdowns or crashes. |
|  | **Fragmentation** | Memory fragmentation can occur, resulting in inefficient memory allocation. |
| **Input/Output (I/O) Performance** | **Disk I/O Bottleneck** | Slow reading/writing of data from/to disk, impacting performance especially with large datasets. |
|  | **Network I/O Bottleneck** | Inefficient handling of network communication causes delays or congestion. |
|  | **Database Access** | Slow database queries, poor indexing, or unoptimized database connections affect response times. |
| **Multithreading and Concurrency** | **Race Conditions** | Improper synchronization in multi-threaded environments leads to unpredictable behavior. |
|  | **Deadlocks** | Threads are unable to proceed because they are waiting for resources held by each other. |
|  | **Thread Overhead** | Overhead caused by excessive threads, leading to context switching and reduced performance. |
|  | **Synchronization Bottlenecks** | Poor synchronization design leads to contention and slows down parallel execution. |
|  | **Contention** | Multiple threads or processes compete for shared resources (e.g., CPU, memory, locks), leading to delays and performance bottlenecks. |
| **Latency** | **High Latency** | Long delay between action and response due to inefficient operations or network conditions. |
|  | **Long Response Time** | Delay between a user's request and the system's response, often caused by unoptimized code or resources. |
| **Power and Energy Consumption** | **Excessive Power Usage** | High energy consumption, especially in mobile and embedded systems, can reduce battery life. |
|  | **Inefficient Resource Usage** | Wasting CPU cycles, memory, or network resources, leading to increased energy consumption. |
| **Scalability** | **Horizontal Scalability Bottleneck** | Problems in distributing workloads across multiple machines or resources, reducing the ability to scale out. |
|  | **Vertical Scalability Bottleneck** | Issues with the system's ability to scale up (increasing resources on a single machine). |
| **System Configuration** | **Improper Hardware Utilization** | Poor configuration of system resources (e.g., CPU, memory, disk, network) prevents optimal performance. |
|  | **Configuration Misalignment** | Incorrect software or hardware configuration leads to performance degradation. |
| **Code-Level Inefficiency** | **Unoptimized Code** | Code that is not optimized, such as redundant loops, inefficient algorithms, or lack of caching. |
|  | **Inefficient Libraries or APIs** | Using third-party libraries or APIs that are not optimized for performance. |
| **Compilation Issues** | **Compiler Optimizations** | Lack of or incorrect compiler optimizations (e.g., missing flags, incorrect settings) lead to suboptimal code performance. |
| **External System Dependencies** | **Third-Party Service Latency** | External services or APIs that introduce delays in communication, impacting overall performance. |
|  | **Cloud Resource Overhead** | Latency or performance degradation due to reliance on cloud services or virtualization. |

## Performance Optimization

> **Performance Tuning** refers to the process of optimizing a system or application to achieve better efficiency, responsiveness, and resource utilization.
> 

> **Performance Optimization** follows a process where a **system model** is created to define the architecture and components, **data is collected** through monitoring and profiling tools, and **analytics** are applied to assess the data, identify bottlenecks, and guide improvements to enhance overall system efficiency.
> 

### Principle

> 

### Technique

> See more in [Technique](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/technique.md).
> 

| **Category** | **Sub-Category** | **Tip** | **Description** |
| --- | --- | --- | --- |
| **Hardware** | CPU | Cache-friendly coding | Arrange data and loops to maximize spatial/temporal locality and reduce cache misses. |
|  | CPU | Vectorization (SIMD) | Use compiler/vector instructions to process multiple data elements in parallel. |
|  | Memory | NUMA awareness | Allocate memory close to the CPU node accessing it to reduce latency. |
|  | Memory | Huge pages | Use larger page sizes to reduce TLB misses and improve memory throughput. |
|  | Storage | SSD/NVMe adoption | Replace HDDs with SSDs or NVMe for faster random and sequential I/O. |
|  | Storage | I/O scheduler tuning | Configure Linux I/O scheduler (e.g., `noop`, `mq-deadline`) for workload characteristics. |
|  | Network | Batch requests | Combine multiple small network requests into fewer larger ones to reduce latency. |
|  | Network | Compression | Use lightweight compression to save bandwidth when CPU cost is low. |
| **OS/Kernel** | Scheduling | Adjust priorities | Assign real-time or higher priorities to latency-sensitive tasks. |
|  | Memory Mgmt | Swap minimization | Reduce or disable swapping for performance-critical processes. |
|  | File System | FS selection | Choose FS tuned to workload (e.g., XFS for large files, ext4 for general). |
|  | Networking | Kernel bypass | Use frameworks like DPDK or `io_uring` for low-latency networking. |
| **Runtime/Language** | Code | Algorithmic optimization | Replace inefficient algorithms with lower-complexity alternatives. |
|  | Code | Inlining small functions | Inline frequently called short functions to avoid call overhead. |
|  | Code | CPU Cost of Abstraction | …. |
|  | Memory | Object pooling | Reuse objects to reduce garbage collection or allocation overhead. |
|  | Memory | Fragmentation reduction | Use custom allocators to reduce fragmentation in memory-intensive apps. |
|  | Concurrency | Lock-free structures | Prefer atomic operations and lock-free queues/maps to avoid contention. |
|  | Concurrency | Async I/O | Use event-driven async instead of blocking threads for high scalability. |
| **Application/Architecture** | Database | Index optimization | Add missing indexes but avoid over-indexing that slows writes. |
|  | Database | Query caching | Cache results of frequently used queries to reduce load. |
|  | Caching | Multi-layer caching | Combine in-process, distributed, and edge caching (e.g., Redis + CDN). |
|  | Load Balancing | Sharding/partitioning | Distribute data across servers to prevent bottlenecks. |
|  | Communication | Binary protocols | Use compact formats (Protobuf, Avro) instead of verbose JSON/XML. |
| **Algorithmic** | Complexity | Better asymptotics | Replace O(n²) algorithms with O(n log n) when possible. |
|  | Communication | Minimize overhead | Reduce inter-process or network communication to improve efficiency. |
|  | Approximation | Heuristics | Use approximation algorithms when exact solutions are too expensive. |
|  | Compression | Storage/bandwidth trade-off | Apply compression when I/O is the bottleneck and CPU can spare cycles. |

### Representation

| **Data Format** | **Precision (Bits)** | **Use Case** | **Context / Application** |
| --- | --- | --- | --- |
| **FP32 (Single Precision Floating Point)** | 32 bits | General-purpose computation, graphics | Widely used in HPC, simulations, and scientific computations; standard format for GPUs. |
| **FP64 (Double Precision Floating Point)** | 64 bits | High-precision scientific computing, simulations | Used in applications that require higher precision, such as physics simulations, numerical analysis, and large-scale scientific computing. |
| **BF16 (Bfloat16)** | 16 bits | AI and Machine Learning training, HPC | Used in deep learning and AI training, provides a good balance of range and precision. |
| **TF32 (Tensor Float 32)** | 32 bits (similar to FP32 but with a modified exponent) | AI, Machine Learning, tensor operations | Optimized for tensor operations in machine learning, offering a balance between performance and precision. |
| **FP16 (Half Precision Floating Point)** | 16 bits | Machine Learning, AI inference, lower precision computations | Used in deep learning and AI workloads, especially in training and inference tasks to improve performance. |
| **INT8 (8-bit Integer)** | 8 bits | AI inference, image processing, lower precision computations | Common in AI inference tasks, especially in neural networks where lower precision is acceptable for efficiency gains. |
| **INT16 (16-bit Integer)** | 16 bits | Signal processing, image processing | Used in applications like digital signal processing (DSP) and image processing for efficient computation with higher dynamic range than INT8. |
| **INT32 (32-bit Integer)** | 32 bits | General-purpose computation, indexing, matrix operations | Used in standard computations requiring integer precision, such as indexing and numerical algorithms. |
| **INT64 (64-bit Integer)** | 64 bits | Large numerical computations, high-precision indexing | Used in applications that need to handle very large integers, such as database management systems or certain scientific simulations. |

### Memory Performance

> If you are have to process a lot of data (data science, video games, and so forth), textbook software design approaches are counterproductive to performance. You want to first get your data layout right, and write the code from the layout.
> 

> Design-by-UML entices you to organize your data around your logic. For performance, do it in reverse: data-oriented programming.
> 

> This comes naturally when your work is designed around a database. But the further you go from the data layout, the more likely you are to fall into performance traps.
> 

> But how do you know the proper data layout? You do not, at least not at first. But you also do not know how your logic should be organized at first. You learn.
> 

![image.png](data/technica/computation/system/evaluation/assets/performace/image.png)

## Case Study

| Software System | Instrumentation Model | **Data to Collect** | **Method of Data Collection** |
| --- | --- | --- | --- |
| Web Server (e.g., Apache) | Performance Monitoring | Traffic data, error rates, response times | Log analysis, real-time polling |
| Database (e.g., MySQL) | Query Performance | Query execution times, error logs, throughput | Event-driven, log parsing |
| Application Server (e.g., Tomcat) | Application Performance | Memory usage, thread counts, response times | JMX beans, real-time polling |
| Operating System (Linux) | System Resource Monitoring | CPU usage, memory usage, disk I/O, network traffic | System calls, perf tools |
| Network Infrastructure | Network Performance | Packet loss, latency, throughput, error rates | SNMP, NetFlow |
| Cloud Infrastructure (e.g., AWS) | Cloud Resource Monitoring | Instance performance, API calls, service metrics | API monitoring, cloud-native tools |
| Custom Application | Business Process Monitoring | Transaction times, system interactions, error rates | Custom probes, log files |

## QA

- How to measure things?
- 
- How to analyze systems written in **`x`** language? Go to the section on that language—there must be an analysis section there; if not, add one.
- How to get the size of the executable memory in linux? `pmap -x <pid> | grep 'r-x'`
- How can I intercept and reuse an existing database connection file descriptor in a running process? [How can I intercept and reuse an existing database connection file descriptor in a running process?](https://app.notion.com/p/How-can-I-intercept-and-reuse-an-existing-database-connection-file-descriptor-in-a-running-process-1b9c0f5171ec80e09390e9b284af87d6?pvs=21)
- What is the latency of a DB Read?
- What is the latency of a DB Write?
- What is the cost of accessing **heap memory** compared to **stack memory**? How can we **simulate** and **measure** it

Conceptual Model: Performance

## References

- [CPU](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/cpu.md)
- García-Risueño, Pablo, and Pablo E. Ibáñez. "A review of High Performance Computing foundations for scientists." International journal of modern physics C 23.07 (2012): 1230001.
- Schroeder, Bianca, and Garth A. Gibson. "A large-scale study of failures in high-performance computing systems." IEEE transactions on Dependable and Secure Computing 7.4 (2009): 337-350.
- [OpenMP](https://hpc-tutorials.llnl.gov/openmp/)
- [Guide to High-Performance Computing](https://acmiitr.medium.com/guide-to-high-performance-computing-b2d9c9a2f77e)
- Srinivasa, K. G., and Anil Kumar Muppalla. "Guide to high performance distributed computing." Computer Communications and Networks. Springer International Publishing, Cham (2015).
- Dongarra, Jack, et al. "High-performance computing: clusters, constellations, MPPs, and future directions." Computing in Science & Engineering 7.2 (2005): 51-59.
- [General-purpose computing on graphics processing units (gpgpu)](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units)
- Arthur S. Bland, Ricky A. Kendall, Douglas B. Kothe, James H. Rogers, Galen M. Shipman, “Jaguar: The World’s Most Powerful Computer”
- “What are the Modeling Requirements for Seamless Prediction of Weather and Climate from Days to Decades? The Known, the Unknown and the Unknowable.” Report of a Sloan Foundation Workshop (December 1-2, 2007; The Royal Society, U.K.).
- J. Shalf, D. Quinlan, C. Janssen, "Rethinking Hardware-Software Codesign for Exascale Systems," Computer , vol.44, no.11, pp.22-30, Nov. 2011 doi: 10.1109/MC.2011.300
- Wayne Joubert and Shi-Quan Su. 2012. An analysis of computational workloads for the ORNL Jaguar system. In Proceedings of the 26th ACM international conference on Supercomputing (ICS '12). ACM, New York, NY, USA, 247-256.
- https://en.wikipedia.org/wiki/Computational_science
- https://www.gromacs.org/
- https://www.comsol.com/
- https://freefem.org/
- https://fenicsproject.org/
- https://www.simscale.com/
- https://www.freecad.org/
- https://dwsim.org/
- https://www.paraview.org/
- https://gmsh.info/
- https://www.blender.org/
- https://www.gempy.org/
- [`Scikit-learn`](https://app.notion.com/p/Scikit-learn-f2f49a145e7348608b5341bb902f877c?pvs=21)
- [**Simple DirectMedia Layer** (**SDL**)](note.html?n=technica/computation/graphical-heterogeneous-high-performance-computing-system/graphical-computing-system/simple-directmedia-layer-sdl.md)
- https://github.com/csiglab/performance-labs
- https://github.com/csiglab/cs-analyst-labs
- https://github.com/csiglab/networking-labs
- https://github.com/csiglab/language-system-labs
- https://github.com/csiglab/data-system-labs
- https://github.com/csiglab/distributed-system-lab
- https://github.com/dbremont/isa-labs
- https://github.com/dbremont/linux-api-labs
- [GPU](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/gpu.md)
- [Numpy](https://app.notion.com/p/Numpy-b254722a30ce4401ab0ecd49f59aec7d?pvs=21)
- [Pandas](https://app.notion.com/p/Pandas-8640191e6b994831b1633753d8c43271?pvs=21)
- [OpenCL](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/opencl.md)
- [Matplotlib](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/matplotlib.md)
- [ ]  [‣](https://app.notion.com/p/1be598edb79080da9af2c8fdc0428eb7?pvs=21)
- [ ]  https://arxiv.org/abs/2503.05116
- https://colin-scott.github.io/personal_website/research/interactive_latency.html
- https://news.ycombinator.com/item?id=39657675