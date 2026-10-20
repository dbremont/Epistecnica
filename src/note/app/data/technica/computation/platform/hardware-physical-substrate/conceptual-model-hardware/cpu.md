# CPU

- [Microarchitecture](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/microarchitecture.md)

> The Central Processing Unit is a highly integrated, synchronous sequential logic circuit functioning as the physical realization of an Instruction Set Architecture (ISA) that utilizes a pipelined, superscalar microarchitecture to orchestrate the fetch-decode-execute cycle by dispatching micro-operations to parallel arithmetic logic units and floating-point units, while mitigating memory latency through speculative execution, dynamic branch prediction, and a coherent multi-level cache hierarchy.
> 

> **Bus Arbitration:** Multiple devices share a common bus, and arbitration determines which device controls the bus at any time.
> 

QA:

- From which hardware systems can the CPU execute instructions?
- How the CPU decides in which core to execute a given instruction?
- How to know which hardware communication model dos a device supports?

## Formulation

![image.png](data/technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/assets/cpu/image.png)

## Structure

| **Category** | **Component** | **Function** | **Description** |
| --- | --- | --- | --- |
| **Control** | **Control Unit (CU)** | Coordinates the execution of instructions. | Decodes instructions from memory and orchestrates sequencing, data flow, and component signaling. |
| **Processing** | **Arithmetic Logic Unit (ALU)** | Executes arithmetic and logical operations. | Performs integer operations like addition, subtraction, comparisons, and bitwise logic. |
| **Processing** | **Floating Point Unit (FPU)** | Executes floating-point operations. | Specialized execution unit for IEEE-754 arithmetic. |
| **Processing** | **Vector/SIMD Unit (AVX/SSE/NEON)** | Executes vectorized operations. | Performs wide parallel operations on vector registers for high-throughput math. |
| **Processing** | **Address Generation Unit (AGU)** | Computes effective memory addresses. | Calculates base + index × scale + offset used by load/store instructions. |
| **Processing** | **Cryptographic Units (AES/SHA)** | Accelerates cryptographic instructions. | Fixed-function hardware for AES, SHA, and similar operations. |
| **Storage** | **Registers** | Fast storage for operands and intermediate values. | Includes GPRs, FPRs, vector registers, segment registers, and status flags. |
| **Storage** | **Physical Register File (PRF)** | Stores physical registers used in OOO execution. | Holds actual integer, floating-point, and vector physical registers. |
| **Storage** | **Register Alias Table (RAT)** | Maps architectural → physical registers. | Enables out-of-order execution by resolving register renaming. |
| **Storage** | **Reorder Buffer (ROB)** | Commits instructions in correct order. | Maintains program order, tracks completion, and handles precise exceptions. |
| **Storage** | **Load Buffer** | Holds pending load operations. | Tracks loads waiting for data, handles speculation and forwarding. |
| **Storage** | **Store Buffer** | Holds pending stores. | Stores data waiting to be written to cache/memory. |
| **Storage** | **Instruction Pointer (IP)** | Points to next instruction. | Same hardware concept as Program Counter. |
| **Storage** | **Program Counter (PC)** | Tracks execution position. | Stores the address of the current or next instruction. |
| **Front-End** | **Fetch Unit** | Retrieves instructions. | Pulls instruction bytes from cache or memory. |
| **Front-End** | **Instruction Queue (IQ/FQ)** | Buffers fetched instructions. | Decouples fetch from decode to maintain throughput. |
| **Front-End** | **Decoding Unit** | Decodes machine instructions. | Converts instruction bytes into micro-ops. |
| **Front-End** | **Micro-op Cache (uop Cache)** | Stores decoded micro-ops. | Allows fetch → execute skipping decode on repeated instructions. |
| **Front-End** | **Microcode Engine** | Expands complex instructions. | Breaks CISC instructions into micro-ops or microcode sequences. |
| **Execution** | **Execution Pipeline** | Processes multiple instructions in overlapping stages. | Implements staged execution: fetch, decode, rename, dispatch, execute, write-back, retire. |
| **Execution** | **Reservation Stations / Issue Queue** | Holds instructions waiting for operands. | Feeds execution units with ready-to-issue micro-ops. |
| **Execution** | **Load/Store Unit (LSU)** | Executes memory operations. | Handles loads, stores, ordering, forwarding, and access hazards. |
| **Performance** | **Branch Prediction Unit** | Predicts branch outcomes. | Reduces stalls by guessing branch directions early. |
| **Performance** | **Return Stack Buffer (RSB)** | Predicts return addresses. | Stack-like predictor for CALL/RET sequences. |
| **Memory** | **Cache (L1, L2, L3)** | Speeds memory access. | Hierarchical caches store recently accessed data and instructions. |
| **Memory** | **TLB (Translation Lookaside Buffer)** | Caches virtual→physical translations. | Speeds address translation performed by the MMU. |
| **Memory** | **Prefetcher** | Loads future cache lines. | Predicts memory access patterns to reduce cache misses. |
| **Memory** | **Write-Back Buffer** | Holds cache lines waiting to be written. | Temporary staging area for dirty lines evicted from cache. |
| **Memory Management** | **Memory Management Unit (MMU)** | Translates virtual addresses. | Performs paging, protection, and privilege checks. |
| **Interface** | **Bus Interface Unit (BIU)** | Handles external communication. | Coordinates data/address/control signals with memory and I/O. |
| **Interface** | **Interconnect Fabric (Ring/Mesh/Crossbar)** | Connects cores and shared caches. | Provides on-chip communication pathways between CPU components. |
| **Coherency** | **Cache Coherency Controller** | Maintains consistency across cores. | Implements MESI/MOESI protocols. |
| **System Management** | **Interrupt Controller** | Manages interrupts. | Prioritizes and routes hardware interrupts to cores. |
| **System Management** | **Clock Unit** | Synchronizes CPU operations. | Distributes timing signals across the processor. |
| **System Management** | **Thermal Control Unit (TCU)** | Manages CPU temperature. | Handles throttling and thermal protection. |
| **Power Management** | **Power Management Unit (PMU)** | Adjusts CPU frequency/voltage. | Controls DVFS, sleep states, and power gating. |
| **Security** | **Secure Enclave / TEE** | Isolates secure computation. | Hardware-enforced protected execution region. |
| **Security** | **Speculation Control Structures** | Manage speculative execution state. | Includes buffers for speculative loads/stores and mitigation logic. |

## Data Path

> The data path is the set of microarchitectural hardware structures—such as functional units, register files, bypass networks, ALUs, load/store units, and pipeline latches—that transport, transform, and temporally stage operand values as they flow through the instruction execution pipeline.
> 

> Note: The idea of Data Path Is Only Internally to the CPU.
> 

## External Transport Interface

> The CPU external interface that transports data is the system bus or interconnect, a high-speed, protocol-defined signaling fabric that carries data, addresses, and control transactions between the processor, memory subsystem, and I/O devices.
> 

> **External Data Transport Line Capacity** is the physical width (in bits) of the CPU’s external data bus or interconnect, defining how many bits can be transferred per bus transaction between the processor and the memory subsystem or chipset, independently of the ISA word size and often implemented as wide, multi-channel, or burst-capable interfaces to maximize sustained bandwidth.
> 

| **Line** | **Description** | **Capacity** |
| --- | --- | --- |
| **Data Lines (Data Bus Width)** | Parallel conductors that carry raw data words between the CPU and the memory subsystem or chipset. | **32–256 bits** per transfer (typical: 64 bits per memory channel). |
| **Address Lines (Address Bus)** | Lines that encode the physical memory address or I/O address for each transaction. | **32–52 bits** depending on CPU generation. |
| **Control Lines** | Sideband signals that coordinate transaction type, timing, read/write indicators, and bus arbitration. | Usually **dozens of lines** (protocol-dependent, not measured in bits). |
| **Channel Lines** | Independent sets of data/address/control lines forming separate memory channels. | **1–8 channels**, each typically **64 bits** wide. |
| **Burst Transfer Path** | Logical multi-beat sequence used to transfer several data units per transaction. | **512–1024 bits** per burst (DDR4/DDR5 typical). |
| **Serial Interconnect Lanes (PCIe/QPI/UPI)** | High-speed differential pairs that transport packetized data for CPU–I/O or CPU–CPU communication. | **1 bit per lane per symbol**, aggregated over **x1–x16** or more lanes. |

## Hardware I/O

| **Category** | **Communication Model** | **Description** | **Primary Use** |
| --- | --- | --- | --- |
| **Memory Access** | **Memory-Mapped I/O (MMIO)** | Memory addresses are assigned to I/O devices, allowing the CPU to interact with them as though they were memory. | Efficient, low-latency communication between the CPU and hardware devices, such as graphics cards and network interfaces. |
|  | **Port-Mapped I/O (PMIO)** | I/O devices are accessed through special ports, not memory addresses. | Older communication model for legacy devices, such as serial and parallel ports. |
| **Data Transfer** | **Direct Memory Access (DMA)** | Peripherals can access system memory directly, bypassing the CPU to improve data transfer efficiency. | High-throughput peripherals like hard drives, network interfaces, and sound cards. |
| **Interrupts** | **Interrupts** | Hardware devices can interrupt the CPU to signal the need for attention. | Real-time responses and event-driven programming for peripherals, timers, and user inputs. |
| **Multi-Core Systems** | **Cache Coherence Protocols** | Ensures all cores in multi-core systems have a consistent view of memory. | Maintains memory synchronization across caches to prevent stale or inconsistent data. |
| **Memory Systems** | **Memory Hierarchy** | Organizes various types of memory (e.g., L1, L2, L3 caches, RAM) to optimize data access and performance. | Minimizes latency and optimizes throughput by prioritizing faster memory types. |
| **Data Transfer** | **Bus Systems** | A communication pathway for transferring data between the CPU and system components. | Transfers data and control signals between the CPU, memory, and I/O devices like GPUs, network interfaces, and SSDs. |
|  | **PCI Express (PCIe)** | High-speed serial bus interface standard for communication between the CPU and high-performance peripherals. | Connecting high-bandwidth devices like GPUs, SSDs, and network cards to the CPU. |
|  | **Serial Communication** | Devices communicate over a single data line, sending bits serially in sequence. | Long-distance communication, typically for embedded systems or lower-speed devices. |
|  | **Parallel Communication** | Multiple bits are transmitted simultaneously across multiple data lines. | Faster data transfer within short-distance communication, such as with memory buses or parallel ports. |
| **Power Management** | **System Management Bus (SMBus)** | Two-wire communication protocol used for managing and monitoring power-related components. | Power management, battery charging, and sensor monitoring in laptops and embedded systems. |
| **Memory Architecture** | **Uniform Memory Access (UMA)** | All CPUs share a single memory pool, allowing access to memory from any processor. | Symmetric multiprocessing (SMP) systems where all processors have equal access to memory. |
|  | **Non-Uniform Memory Access (NUMA)** | Memory access latency varies based on processor proximity to memory, with local memory for each CPU. | High-performance computing clusters and large-scale database systems where processors have dedicated memory regions. |
| **Processor Interconnect** | **Direct CPU Interconnect** | High-speed, low-latency interconnect linking processors, memory, and other components. | Connecting CPUs, memory controllers, and I/O devices within the same socket or across multiple sockets. |
| **Virtualization** | **Hypervisor / Virtualization** | Virtual machines run on the hardware, with the hypervisor allocating CPU resources to multiple VMs. | Resource allocation and isolation for multiple operating systems running on the same physical hardware. |

## Toolbox

- **mpstat:** Report processor's related statistics.
- …

## QA

### From which hardware subsystems does the CPU fetch the instructions it executes?

| **Category** | **Hardware System** | **Description** | **Mechanism (How Instructions Reach the CPU)** |
| --- | --- | --- | --- |
| **Caches** | **L1 Instruction Cache (L1I)** | Smallest and fastest instruction store, holding the most recently used instruction bytes. | CPU uses the Program Counter (PC) to index into L1I. On hit → instruction bytes flow directly into the decoder. On miss → request cascades to L2/L3. |
|  | **Unified L2 / L3 Cache** | Larger, slower caches storing both code and data. | Serves instruction requests on L1I misses. On hit → returns line to L1I and frontend. On miss → forwards to main memory controller. |
| **Main Memory** | **DRAM (System RAM)** | Primary storage location for program text segments. | On a last-level-cache (LLC) miss, the memory controller fetches the instruction line from DRAM → fills the cache hierarchy → CPU frontend receives the line. |
| **Read-Only Regions** | **Boot ROM / Mask ROM** | Immutable, hardwired read-only firmware used at power-on. | At reset the PC begins in ROM; instructions are fetched through the memory bus and enter caches normally. |
|  | **Flash / Firmware Storage (NOR, SPI Flash)** | Non-volatile memory storing firmware or bootloader code. | CPU fetches via execute-in-place (XIP) when memory-mapped, or after copying firmware into RAM during early boot. |
| **Microarchitectural Sources** | **Instruction Queue / Prefetch Buffer** | Temporary frontend buffers holding already-fetched instruction bytes. | Not a primary storage source; only receives bytes from L1I or lower and provides them to the decoder. |
|  | **µOP Cache / Decode Cache (e.g., Intel DSB)** | Stores *decoded* micro-operations for reuse. | On µOP-cache hit → frontend supplies µops directly, bypassing instruction fetch and decode. |
| **Address Translation Support** | **Instruction TLB (iTLB)** | Cache of virtual→physical address translations. | Not a storage source; ensures the PC’s virtual address can be translated. On miss → page walk → fetch proceeds using resolved physical address. |
| **External Memory Sources** | **External Flash (XIP)** | Used in MCUs/SoCs to execute directly from external NOR flash. | PC-driven access over external memory bus → optional caching → decoded by CPU frontend. |
| **Non-Standard** | **MMIO Regions** | Memory-mapped I/O regions; executable but almost always disabled due to risk and slow access. | CPU treats the region as memory; fetches occur through device bus → extremely high latency; used only in special MCUs or debugging. |
|  | **Network Boot (PXE)** | Not an instruction source by itself. | NIC retrieves bootloader into RAM; CPU then fetches instructions from RAM. |
|  | **JTAG / Hardware Debug Interface** | External debug tools can halt, single-step, or inject instructions. | Debugger manipulates PC and instruction register (IR); not used during normal program execution. |

### How the CPU Decides Which Core to Execute a Given Instruction?

> In modern multi-core processors, the decision of which core will execute a given instruction is managed by the **Operating System (OS)** in coordination with the CPU's **hardware scheduling mechanisms**. The CPU itself does not decide which core to use for each instruction directly. Instead, it follows a process driven by **thread scheduling**, **load balancing**, and **core affinity** policies set by the OS.
> 

## References

- https://github.com/OpenXiangShan/XiangShan
- https://www.youtube.com/watch?v=HyznrdDSSGM
- https://www.youtube.com/playlist?list=PLilenfQGj6CEG6iZ4TQJ10PI7pCWsy1AO
- Why do CPUs have multiple cache levels? (2016) ([fgiesen.wordpress.com](http://fgiesen.wordpress.com/))
[https://news.ycombinator.com/item?id=40365248](https://news.ycombinator.com/item?id=40365248)
- https://www.youtube.com/watch?v=dX9CGRZwD-w&t=154s
- https://news.ycombinator.com/item?id=42576242