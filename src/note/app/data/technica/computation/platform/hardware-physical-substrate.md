# (Hardware) Physical Substrate

> How is computation **instantiated in the Physical Substrate**? How does computation **interact with other Physical Substrate subsystems**? How can Physical Substrate subsystems **interact with actuators**?
> 

> **Computational hardware** refers to the physical components of a computer system, such as processors, memory, storage, and networking devices, that enable the execution of computational tasks and data processing.
> 

## Formulation

> The Computing Physical Substrate refers to the material foundation that enables the representation, transformation, and transmission of information in a computing system.
> 
> 
> It consists of the **actual physical entities**—matter, energy, and their dynamic interactions—that instantiate the abstract structures and operations of computation.
> 
> The **physical substrate** defines the **laws**, **constraints**, and **capacities** under which computation occurs. These include limits of energy, speed, precision, noise, and reliability. Every higher-level computational abstraction ultimately reduces to patterns of **state transitions** in this substrate.
> 

### Dimension

| **Dimension** | **Description** | Note |
| --- | --- | --- |
| **Information Carrier** | The physical medium that holds distinguishable states used to encode information. | Voltage levels in transistors, magnetic orientations, photon polarizations, molecular conformations. |
| **State Dynamics** | The physical processes governing how states evolve or transition over time. | Electrical switching, quantum superposition, chemical reactions. |
| **Energy Flow** | The mechanisms through which computation consumes, dissipates, or transforms energy. | Electric current, heat generation, photon emission. |
| **Noise and Error** | The degree to which physical uncertainty or interference perturbs state transitions. | Thermal noise, bit flips, decoherence. |
| **Scalability** | How the substrate supports larger or denser configurations while preserving fidelity. | Moore scaling, parallel optical links, biological growth. |
| **Topology** | The spatial and causal connectivity of the substrate’s components. | Bus, mesh, network fabric, molecular lattice. |

### Structure

| **Subsystem** | **Role** | **Physical Basis** |
| --- | --- | --- |
| **Processing Substrate** | Executes transformations of encoded states. | Logic gates, quantum gates, neural tissue, chemical reactions. |
| **Memory Substrate** | Stores and retrieves states over time. | Semiconductor cells, magnetic domains, DNA strands. |
| **Communication Substrate** | Transmits states across spatially separated components. | Electrical buses, optical fibers, radio links. |
| **Sensing Substrate** | Converts environmental or analog stimuli into internal signals. | Photodiodes, microphones, ADC circuits. |
| **Actuation Substrate** | Converts internal signals into external physical effects. | Motors, displays, DAC circuits. |

### Computer

> A **Computer** is an electronic system capable of executing instructions to process data. It integrates processing units, memory, storage, and input/output mechanisms to perform computation, run programs, and interact with users or other systems. Computers can range from small embedded devices to large servers.
> 

### Compute Unit

> A **Compute Unit** is a physical hardware component within a computer that performs computation. Examples include CPU cores, GPU cores, TPUs, or FPGAs. Compute Units execute arithmetic, logical, or specialized operations and serve as the fundamental building blocks of computational capacity.
> 

### Virtual Compute Unit

> A **Virtual Compute Unit (vCU)** is an abstraction of a physical compute unit, provided by virtualization or containerization technologies. It represents a share of a physical processor allocated to a virtual machine, container, or cloud workload, allowing multiple workloads to run independently on the same physical hardware.
> 

### Data Center

> A **Data Center** is a facility that houses a large collection of computing resources, including servers, storage systems, networking equipment, and power/cooling infrastructure. Data centers provide the environment for running physical and virtual compute units at scale, supporting enterprise IT operations, cloud services, and high-performance computing workloads.
> 

## Hardware Space

> What are the **constituent elements of the Physical Substrate in Computation**?
> 

> **Controller:** Provides a fixed, integrated hardware interface for connecting a device to the computer system.
> 

> **Adapter:** Provides an external/removable hardware interface for connecting a device to the computer through an expansion slot.
> 

> **Expansion Slot:** Provides the physical and electrical connection point through which an adapter is attached to the computer.
> 

- NIC Controller
- Wi-Fi Controller
- WWAN ****Controller
- Bluetooth Controller

| **Category** | **Type** | **Description** | **Instance(s)** |
| --- | --- | --- | --- |
| **Processing** | FPGA | Field-programmable gate array for customizable hardware logic. | Xilinx Virtex, Intel Stratix |
|  | ASIC | Application-specific integrated circuit designed for a specific task. | Bitcoin miner ASICs, TPU ASICs |
|  | TPU | Tensor Processing Unit for accelerating ML workloads. | Google TPU |
|  | CPU ALU | Performs arithmetic and logical operations. | Intel CPU ALU, AMD CPU ALU |
|  | Control Unit | Coordinates operations of processing elements. | CPU CU, microcontroller CU |
|  | Quantum Gate | Performs quantum state transformations. | Qubit gate arrays, superconducting qubits |
|  | Neural Circuit | Biological computation units. | Neural tissue circuits, synthetic neuron networks |
| **Networking** | Router | Directs packets across networks. | Cisco ISR, Juniper MX |
|  | Switch | Connects multiple devices within a network. | Cisco Catalyst, HP Aruba |
|  | Modem | Modulates/demodulates signals for network access. | DSL, Cable, Fiber modems |
| **Memory** | Volatile Memory | Temporary storage that loses data when powered off. | DRAM, SRAM |
|  | Non-Volatile Memory | Persistent storage. | Flash memory, magnetic disks, DNA memory |
|  | Cache | High-speed temporary storage close to processing units. | L1/L2/L3 CPU caches |
| **Communication** | Wired Channel | Physical media transmitting signals electrically or optically. | Electrical buses, optical fibers, PCIe links |
|  | Wireless Channel | Transmits signals through electromagnetic waves. | Wi-Fi, Bluetooth, cellular links |
|  | Interface | Device enabling connection to network or other components. | Network Interface Cards (NICs), transceivers |
| **Sensing** | Photonic Sensor | Converts light into electrical signals. | Photodiodes, camera sensors |
|  | Acoustic Sensor | Converts sound waves into signals. | Microphones, ultrasonic sensors |
|  | Thermal Sensor | Measures temperature changes. | Thermistors, infrared sensors |
|  | Motion Sensor | Detects movement or acceleration. | Accelerometers, gyroscopes |
| **Actuation** | Mechanical Actuator | Converts signals into mechanical motion. | Motors, solenoids |
|  | Electrical/Optical Actuator | Converts signals into light or electrical changes. | LEDs, displays, DAC-driven circuits |
|  | Acoustic Actuator | Converts electrical signals into sound. | Speakers, piezo buzzers |
| **Power & Energy** | Power Supply | Provides regulated energy for computation. | PSU, voltage regulators |
|  | Energy Storage | Stores energy for later use. | Batteries, capacitors, fuel cells |
|  | Energy Distribution | Delivers energy across the substrate. | Power rails, busbars |
| **Support & Structure** | Physical Scaffold | Maintains integrity and spatial organization. | PCBs, chip packaging, chip carriers |
|  | Thermal Management | Dissipates heat from processing elements. | Heat sinks, fans, liquid cooling |
|  | Biological Support | Provides physical framework for bio-computation. | Synthetic scaffolds, extracellular matrices |

## Interconnect

> How do different hardware elements connect? How to model **`connection topology`**? Which are the concepts that helps to represent this?
> 

> See more in [**Interconnect**](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/interconnect.md).
> 

## Technology Tree(s)

> What are the computing technologies in the technology tree?
> 

| **Technology** | **Type** | **Description** | **Notes** |
| --- | --- | --- | --- |
| Optical Computing | Computing Paradigm | Uses photons instead of electrons for computation, offering potential for higher speed and lower energy use. | Photonic processors, optical interconnects. |
| Transistor Computer | Classical Computing | Uses transistor-based digital logic to perform computation. Foundation of modern computers. | CPUs, GPUs, ASICs. |
| Quantum Computing | Computing Paradigm | Exploits quantum superposition and entanglement to perform certain computations much faster than classical computers. | Qubits, IBM Q, Google Sycamore. |
| Neuromorphic Computing | Bio-inspired Computing | Mimics the architecture and operation of the human brain to achieve energy-efficient computation for AI tasks. | Intel Loihi, IBM TrueNorth. |
| DNA Computing | Unconventional Computing | Uses DNA molecules for storing and processing information. | DNA-based logic circuits, molecular computing experiments. |
| Molecular Electronics | Nanoelectronics | Uses molecules as electronic components for ultra-small circuits. | Single-molecule transistors. |
| Memristor Computing | Non-volatile Logic | Uses memristors for memory and logic, enabling neuromorphic-like architectures. | HP memristor chips, hybrid memory-compute systems. |

## Performance

> **High-performance hardware technologies** are critical for applications requiring extreme speed, low latency, and scalability, such as **high-performance computing (HPC)**, **AI/ML**, and **big data analytics**.
> 

### Metrics

| **Category** | **Metric** | **Description** |
| --- | --- | --- |
| **Compute Efficiency** | Server Utilization | Percentage of server capacity actively used. |
|  | CPU Utilization | Percentage of CPU capacity in use. |
|  | GPU Utilization | Percentage of GPU capacity in use. |
|  | Virtual Machine (VM) Density | Number of VMs hosted per physical server. |
|  | Task Completion Rate | Number of tasks or jobs completed within a given time frame. |
|  | Instructions Per Cycle (IPC) | Number of instructions executed per CPU clock cycle. |
|  | Instructions Per Second (IPS) | Number of instructions executed per second. |
|  | Clock Speed | Frequency at which the CPU operates (in GHz). |
|  | Branch Prediction Accuracy | Percentage of correctly predicted branches in the CPU pipeline. |
|  | Cache Hit Rate | Percentage of memory requests served by the CPU cache. |
| **GPU Metrics** | **FLOPS (Floating Point Operations Per Second)** | Measures GPU performance for floating-point calculations. |
|  | **Tensor Operations Per Second (TOPS)** | Measures GPU performance for AI/ML workloads. |
|  | **Memory Bandwidth** | Speed at which data can be read from or written to GPU memory. |
|  | **CUDA Core Utilization** | Percentage of CUDA cores actively used in NVIDIA GPUs. |
|  | **Tensor Core Utilization** | Percentage of Tensor cores actively used in NVIDIA GPUs. |
|  | **GPU Memory Utilization** | Percentage of GPU memory in use. |
|  | **GPU Power Consumption** | Amount of power consumed by the GPU. |
| **Storage Efficiency** | Storage Utilization | Percentage of storage capacity in use. |
|  | IOPS (Input/Output Operations Per Second) | Measures storage performance. |
|  | Latency | Time taken for data to be read from or written to storage. |
|  | Data Redundancy | Level of data duplication for fault tolerance. |
|  | Backup Success Rate | Percentage of successful backups completed. |
| **Network Efficiency** | Network Throughput | Amount of data transferred over the network per unit of time. |
|  | Packet Loss Rate | Percentage of data packets lost during transmission. |
|  | Network Latency | Time taken for data to travel across the network. |
|  | Bandwidth Utilization | Percentage of available network bandwidth in use. |
|  | Uptime/Downtime | Percentage of time the network is operational. |
| **Power and Cooling Efficiency** | Power Usage Effectiveness (PUE) | Ratio of total power used to power delivered to IT equipment. |
|  | Data Center Infrastructure Efficiency (DCiE) | Inverse of PUE, expressed as a percentage. |
|  | Cooling Efficiency | Effectiveness of cooling systems in maintaining optimal temperatures. |
|  | Energy Reuse Effectiveness (ERE) | Measures how much energy is reused (e.g., for heating). |
|  | Carbon Usage Effectiveness (CUE) | Measures carbon emissions per unit of IT energy consumption. |
| **Operational Efficiency** | Mean Time Between Failures (MTBF) | Average time between hardware or system failures. |
|  | Mean Time to Repair (MTTR) | Average time taken to repair a failure. |
|  | Incident Response Time | Time taken to respond to and resolve operational issues. |
|  | Change Success Rate | Percentage of successful changes (e.g., updates, upgrades) without issues. |
|  | Resource Allocation Efficiency | How effectively resources (e.g., servers, storage) are allocated. |
| **Cost Efficiency** | Cost per Rack | Total cost of operating a single rack. |
|  | Cost per kW | Cost of power consumed per kilowatt. |
|  | Cost per VM | Cost of running a virtual machine. |
|  | Total Cost of Ownership (TCO) | Total cost of owning and operating the datacenter. |
|  | Return on Investment (ROI) | Profitability of the datacenter relative to its costs. |
| **Capacity and Scalability** | Rack Space Utilization | Percentage of rack space occupied by equipment. |
|  | Power Capacity Utilization | Percentage of available power capacity in use. |
|  | Cooling Capacity Utilization | Percentage of cooling capacity in use. |
|  | Scalability Index | Ability to scale resources (e.g., servers, storage) to meet demand. |
| **Security and Compliance** | Security Incident Rate | Number of security incidents (e.g., breaches, attacks) per month. |
|  | Patch Compliance Rate | Percentage of systems updated with the latest security patches. |
|  | Audit Success Rate | Percentage of successful compliance audits. |
|  | Data Encryption Rate | Percentage of data encrypted at rest and in transit. |
| **Customer and Service Metrics** | SLA Compliance | Percentage of SLA targets met. |
|  | Customer Satisfaction Score | Feedback from customers on datacenter services. |
|  | Ticket Resolution Time | Average time taken to resolve customer support tickets. |
|  | Uptime Availability | Percentage of time services are available to customers. |
| **Sustainability Metrics** | Renewable Energy Usage | Percentage of energy sourced from renewable sources. |
|  | Water Usage Effectiveness (WUE) | Measures water used for cooling per unit of IT energy consumed. |
|  | E-Waste Recycling Rate | Percentage of electronic waste recycled. |
|  | Carbon Footprint | Total greenhouse gas emissions from datacenter operations. |

### Failure

> Hardware failure rate refers to the frequency at which hardware components fail over time. It is often measured using metrics like **Mean Time Between Failures (MTBF)** and **Annualized Failure Rate (AFR)**.
> 

| **Hardware Component** | **Failure Rate Metrics** | **Typical Failure Rate** | **Factors Affecting Failure Rate** |
| --- | --- | --- | --- |
| **Hard Disk Drives (HDDs)** | MTBF: 1-1.5 million hours <br> AFR: 2-4% | Higher failure rates due to mechanical parts. | Usage intensity, temperature, vibration, age. |
| **Solid State Drives (SSDs)** | MTBF: 2 million hours <br> AFR: 1-2% | Lower failure rates than HDDs but wear out over time. | Write cycles (endurance), temperature, firmware quality. |
| **Servers** | MTBF: 3-5 years <br> AFR: 5-10% | Failures depend on usage and environmental conditions. | Workload intensity, cooling, power supply quality. |
| **Power Supply Units (PSUs)** | MTBF: 100,000 hours <br> AFR: 1-3% | Failures can cause downtime for entire systems. | Load capacity, heat, voltage fluctuations. |
| **Memory (RAM)** | MTBF: 10+ years <br> AFR: <1% | Low failure rates but sensitive to electrical issues. | Voltage spikes, overheating, manufacturing defects. |
| **GPUs** | MTBF: 3-5 years <br> AFR: 2-5% | Failures increase with heavy workloads (e.g., AI/ML). | Workload intensity, cooling, overclocking. |
| **Networking Equipment** | MTBF: 5+ years <br> AFR: 1-3% | Failures depend on usage and environmental factors. | Traffic load, heat, dust, power surges. |
| **Cooling Systems** | MTBF: 5-10 years <br> AFR: 2-5% | Failures can lead to overheating of other components. | Dust, wear and tear, maintenance quality. |

### Technology

| **Technology** | **Description** | **Key Features** | **Applications** |
| --- | --- | --- | --- |
| **InfiniBand** | A high-speed, low-latency networking technology for HPC and data centers. | - Speeds up to 400 Gbps (HDR). <br> - Ultra-low latency (sub-microsecond). <br> - Scalable and RDMA support. | HPC clusters, AI/ML, big data, cloud computing. |
| **NVLink** | NVIDIA’s high-speed interconnect for GPUs and CPUs. | - Bandwidth up to 600 GB/s. <br> - Direct GPU-to-GPU communication. <br> - Low latency. | AI/ML, deep learning, HPC. |
| **PCIe (Peripheral Component Interconnect Express)** | A high-speed serial computer expansion bus standard. | - PCIe 5.0 offers 32 GT/s per lane. <br> - Scalable bandwidth. <br> - Low latency. | GPUs, SSDs, network cards, accelerators. |
| **CXL (Compute Express Link)** | An open standard for high-speed CPU-to-device and CPU-to-memory interconnects. | - Memory coherency. <br> - Low latency. <br> - High bandwidth. | Memory expansion, accelerators, HPC. |
| **Optane Memory (3D XPoint)** | Intel’s high-speed, non-volatile memory technology. | - Faster than NAND SSDs. <br> - High endurance. <br> - Low latency. | Caching, persistent memory, high-performance storage. |
| **NVMe (Non-Volatile Memory Express)** | A protocol for accessing high-speed storage media. | - Speeds up to 7 GB/s (PCIe 4.0). <br> - Low latency. <br> - High IOPS. | High-performance SSDs, data centers, real-time analytics. |
| **FPGA (Field-Programmable Gate Array)** | Reconfigurable hardware for custom logic and acceleration. | - Parallel processing. <br> - Low latency. <br> - Customizable. | AI/ML, signal processing, cryptography. |
| **TPU (Tensor Processing Unit)** | Google’s custom ASIC for AI/ML workloads. | - Optimized for tensor operations. <br> - High TOPS (Trillions of Ops/sec). | AI/ML, deep learning, neural networks. |
| **Quantum Computing Hardware** | Hardware leveraging quantum mechanics for computation. | - Qubits for parallel processing. <br> - Exponential speedup for specific tasks. | Cryptography, optimization, drug discovery. |
| **HBM (High Bandwidth Memory)** | High-speed memory stacked on GPUs or CPUs. | - Bandwidth up to 1 TB/s. <br> - Low power consumption. <br> - Compact design. | GPUs, AI/ML, HPC. |
| **RoCE (RDMA over Converged Ethernet)** | A protocol for RDMA over Ethernet networks. | - Low latency. <br> - High throughput. <br> - Compatible with Ethernet. | Data centers, cloud computing, storage networks. |
| **Silicon Photonics** | Technology using light for data transmission in chips. | - High bandwidth. <br> - Low latency. <br> - Energy-efficient. | Data centers, HPC, interconnects. |
| **DPU (Data Processing Unit)** | A specialized processor for offloading networking and storage tasks. | - High throughput. <br> - Low latency. <br> - Offloads CPU tasks. | Data centers, cloud computing, network acceleration. |
| **ARM-based CPUs** | High-efficiency CPUs based on ARM architecture. | - Low power consumption. <br> - Scalable performance. <br> - Customizable. | Mobile devices, servers, edge computing. |
| **Exascale Computing Systems** | Supercomputers capable of at least one exaflop (10^18 FLOPS). | - Massive parallelism. <br> - High-speed interconnects. <br> - Advanced cooling. | Scientific research, climate modeling, nuclear simulations. |

### Limitation

| **Category** | **Limit** | **Description** | **Implications** |
| --- | --- | --- | --- |
| **Theoretical Limits** | **Turing Completeness** | A system can compute any computable function given enough time and resources. | Defines the boundary of what is theoretically computable. |
|  | **Halting Problem** | It is impossible to determine if an arbitrary program will halt or run forever. | Limits the ability to predict program behavior. |
|  | **P vs NP Problem** | Whether problems solvable in polynomial time $P$ are the same as those verifiable in polynomial time (NP). | Unsolved; impacts cryptography, optimization, and algorithm design. |
|  | **Church-Turing Thesis** | Any computable function can be computed by a Turing machine. | Establishes the foundation of classical computation. |
| **Physical Limits** | **Landauer’s Principle** | Erasing one bit of information requires a minimum energy of $kT \ln 2$. | Sets a lower bound on energy consumption for computation. |
|  | **Bremermann’s Limit** | Maximum computational speed of a physical system:$1.36 \times 10^{50}$ bits per second per kg. | Limits the speed of computation based on mass and energy. |
|  | **Margolus-Levitin Theorem** | Maximum number of operations per second: $2E/h$, where $E$ is energy. | Limits the speed of quantum computations. |
|  | **Heisenberg Uncertainty Principle** | Limits the precision of measuring quantum states. | Affects quantum computing and error correction. |
| **Technological Limits** | **Moore’s Law** | The number of transistors on a chip doubles every 18-24 months. | Facing physical and economic limits as transistors approach atomic scales. |
|  | **Heat Dissipation** | Increasing density of transistors leads to higher heat generation. | Limits the miniaturization and speed of processors. |
|  | **Speed of Light** | Information cannot travel faster than the speed of light. | Limits the speed of communication and computation in distributed systems. |
| **Quantum Limits** | **Decoherence** | Quantum states lose coherence due to interaction with the environment. | Limits the duration of quantum computations. |
|  | **No-Cloning Theorem** | Quantum information cannot be perfectly copied. | Limits error correction and data replication in quantum systems. |
|  | **Quantum Error Correction** | Requires significant overhead to correct errors in quantum computations. | Increases the complexity and resource requirements for quantum computing. |
| **Mathematical Limits** | **Gödel’s Incompleteness Theorems** | In any formal system, there are true statements that cannot be proven. | Limits the completeness of mathematical systems and algorithms. |
|  | **Kolmogorov Complexity** | Measures the complexity of a string as the length of the shortest program that produces it. | Limits the compressibility of information. |
| **Practical Limits** | **Algorithmic Efficiency** | Some problems require exponential time or space to solve. | Limits the feasibility of solving certain problems with classical computers. |
|  | **Memory and Storage** | Physical limits on the amount of data that can be stored and accessed. | Limits the scale of data processing and storage. |
|  | **Energy Consumption** | Practical limits on the energy available for computation. | Impacts the sustainability and scalability of large-scale computing. |
| **Biological Limits** | **Human Brain Capacity** | Estimated computational capacity of the human brain: $10^{16}$ ops/sec. | Sets a benchmark for artificial intelligence and cognitive computing. |
|  | **Neural Signal Speed** | Speed of neural signals in the brain: ~120 m/s. | Limits the speed of biological computation and information processing. |

**Factors Influencing Hardware Failure and Depreciation**

| **Factor** | **Impact on Failure Rate** | **Impact on Depreciation** |
| --- | --- | --- |
| **Usage Intensity** | Higher usage increases wear and tear, leading to higher failure rates. | Higher usage accelerates depreciation. |
| **Environmental Conditions** | Heat, dust, and humidity can increase failure rates. | Poor conditions reduce the useful life of hardware, increasing depreciation. |
| **Maintenance Quality** | Regular maintenance reduces failure rates. | Proper maintenance extends useful life, slowing depreciation. |
| **Technological Obsolescence** | Newer technologies can make older hardware obsolete, increasing failure rates. | Obsolescence accelerates depreciation. |
| **Workload Type** | Heavy workloads (e.g., AI/ML) increase failure rates. | Heavy workloads reduce useful life, increasing depreciation. |

## Tool

> Here is a table of tools in Linux that deal with hardware:
> 

| **Tool** | **Description** | **Usage** | **Common Options** |
| --- | --- | --- | --- |
| **lshw** | Displays detailed information about the hardware configuration of the system. | `lshw` | `-short`, `-class`, `-sanitize`, `-html` |
| **lspci** | Lists all PCI devices in the system, providing information on the PCI bus and devices. | `lspci` | `-v`, `-vv`, `-k`, `-nn`, `-s` |
| **lsusb** | Lists all USB devices connected to the system. | `lsusb` | `-v`, `-t`, `-s`, `-D` |
| **lsblk** | Lists information about all available or the specified block devices. | `lsblk` | `-f`, `-d`, `-a`, `-o`, `-J`, `-P` |
| **dmidecode** | Dumps the system's DMI (Desktop Management Interface) table contents, which includes information about the system's hardware components. | `dmidecode` | `-t`, `-u`, `-q`, `-s` |
| **hdparm** | A command-line utility to view and set hardware parameters of hard disk drives. | `hdparm <device>` | `-I`, `-t`, `-T`, `--security-set-pass` |
| **smartctl** | Controls and monitors S.M.A.R.T. (Self-Monitoring, Analysis, and Reporting Technology) for hard drives. | `smartctl <device>` | `-a`, `-H`, `-t`, `-i`, `-q`, `-c` |
| **inxi** | Provides detailed information about the system's hardware and software. | `inxi` | `-F`, `-b`, `-t`, `-G`, `-D`, `-A`, `-S` |
| **hwinfo** | Provides detailed information about the hardware. | `hwinfo` | `--short`, `--all`, `--cpu`, `--disk` |
| **lscpu** | Displays information about the CPU architecture. | `lscpu` | `-p`, `-e`, `-b`, `-s`, `-x` |
| **lsdev** | Lists all devices and their resources, including IRQs, DMA channels, and I/O ports. | `lsdev` | N/A |
| **lsscsi** | Lists all SCSI devices and their properties. | `lsscsi` | `-s`, `-l`, `-g`, `-c`, `-k` |
| **i2cdetect** | Detects and lists all I2C devices connected to the system. | `i2cdetect <bus>` | `-y`, `-a`, `-r`, `-F` |

## QA

### To which class of hardware do an `adapter` and a `controller` belong?

> A good name will be  `External Hardware Interconnect Interface`.
> 

> **Interface Mechanism:** Hardware that enables a device to connect to and interact with the computer system.
> 

### How to list the `External Hardware Interconnect Interfaces`  present on my Computer System?

> 

|

## References

Conceptual Model: Hardware

- [Time](note.html?n=technica/computation/miscelanea/time.md)
- [Energy](https://app.notion.com/p/Energy-39f21c7cc02545e289e03578281bd13f?pvs=21)
- [Workload](note.html?n=technica/computation/system/design/computer-system-design-conceptual-model/workload.md)
- https://en.wikipedia.org/wiki/InfiniBand
- [Cloud Computing System](note.html?n=technica/computation/platform/cloud-computing-system.md)
- https://en.wikipedia.org/wiki/Computer_hardware
- https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet
- [Operating System](note.html?n=technica/computation/operating-system.md)
- [Operation](note.html?n=technica/computation/system/operation.md)
- [Virtualization](note.html?n=technica/computation/platform/virtualization.md)
- https://modal.com/gpu-glossary
- https://en.wikipedia.org/wiki/Remote_direct_memory_access
- [‣](https://app.notion.com/p/289598edb79080359cb0e8e7f900da96?pvs=21)
- https://en.wikipedia.org/wiki/Optical_computing
- [‣](https://app.notion.com/p/10e598edb790815f897cd8ad952c6e93?pvs=21)
- [Telecom](note.html?n=technica/computation/telecom.md)
- Renting GPU’s https://www.reddit.com/r/LocalLLaMA/comments/1na3f1s/renting_gpus_is_hilariously_cheap/