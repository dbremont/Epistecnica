---
tags: [interconnect]
---

# Interconnect

- [External Hardware Interconnect](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/external-hardware-interconnect.md)

> In this note, we will begin **mapping the interconnection mechanisms** used in **computer hardware**.
> 

> **Guiding Question:** How can the CPU communicate with this node? What is the communication path from the CPU to the node, and how many edges does that path traverse?
> 

> How can we better conceptualized this ‘**Which are the CPU-to-Device (Either  - Directly or Indirectly)  Hardware Communication Path(s)?’?**
> 

> Note:  This nodes suffers from mixing many levels - of elements in one table.
> 

> Hardware communication is a multi-layer phenomenon. A complete communication model must represent the hardware elements participating in communication, their topology, the links connecting them, the physical media and signaling used by those links, the protocols governing communication, the mechanisms used to perform communication operations, and the software abstractions through which the operating system discovers and operates the hardware.
> 

## Formulation

> How do different hardware elements connect? How to model **`connection topology`**? Which are the concepts that helps to represent this?
> 

```bash
Path(A,B) = [N0, E1, N1, E2, N2, ..., Ek, Nk]

where:
    N0 = source
    Nk = destination
    Ei = edge connecting N(i-1) and Ni

EdgeCount(Path) = k
```

### Which terminology should Guide the Note?

| **Concept** | **Description** |
| --- | --- |
| **Computer System** | The complete computational system being modeled. |
| **Computer System Structure** | The organization of the elements and their relationships within a computer system. |
| **Computer System Element** | An entity that constitutes or participates in the structure of a computer system. |
| **Aggregate Element** | A computer system element composed of other computer system elements. |
| **Atomic Element** | A computer system element treated as indivisible at the current level of abstraction. |
| **Link Node Element  (Intermediate Node)** | A computer system element that **mediates communication between other computer system elements**. |
| **Computer System Edge** | A structural relationship representing a connection between computer system elements. |
| **Connection Topology** | The organization of computer system elements and their connecting edges, describing how the elements are interconnected. |
| **Node** | A hardware entity that can be an endpoint, intermediary, resource, or communication participant. |
| **Endpoint Node** | A node that originates or terminates a communication transaction. |
| **Edge** | A relationship between two nodes representing an available communication relationship. |
| **Link** | The concrete communication mechanism associated with an edge. |
| **Path** | An ordered sequence of nodes and edges connecting a source node to a destination node. |
| **Communication Path** | A path that is actually capable of carrying the particular communication being considered. |
| **Path Length** | Number of edges/hops traversed by the selected path under a specified counting rule. |

### Which are the **Aggregate Element in Hardware Space?**

> **Modeling Resolution:** the level at which a hardware system is represented in a particular topology graph.
> 

| **Aggregate Element** | **Description** | **Composition** |
| --- | --- | --- |
| **Computer System** | Complete hardware system providing computational capabilities. | Processor, memory, storage, interconnects, controllers, adapters, I/O devices, power subsystem, etc. |
| **Motherboard** | Primary printed-circuit assembly interconnecting major system components. | CPU socket, DIMM slots, expansion slots, chipset/PCH, controllers, connectors, power circuitry, etc. |
| **Processor Package** | Physical package containing the processor die and package-level interconnects. | Processor die, package substrate, package interconnects, integrated cache, etc. |
| **Memory Module** | Modular hardware assembly providing system memory. | DRAM devices, PCB, SPD device, power-management circuitry, etc. |
| **Storage Device** | Hardware assembly providing persistent storage. | Storage media, storage controller, cache/buffer, interface, power circuitry, etc. |
| **Graphics Card** | Hardware assembly providing graphics and parallel-computing capabilities. | GPU, VRAM, memory controller, PCB, power circuitry, display interfaces, etc. |
| **Expansion Card** | Removable hardware assembly connected through an expansion interface. | PCB, controller(s), memory, connectors, power circuitry, supporting components, etc. |
| **Power Supply** | Hardware assembly that converts and distributes electrical power. | Power-conversion circuitry, regulation circuitry, protection circuitry, cooling system, connectors, etc. |
| **Cooling Assembly** | Hardware assembly responsible for transferring and dissipating heat. | Heat sink, heat pipes/vapor chamber, fan(s), thermal interface material, mounting hardware, etc. |
| **Network Interface** | Hardware assembly providing network connectivity. | Network controller, PHY/transceiver, interface connector, supporting circuitry, etc. |

### Which are the type of **Link Node Element  (Intermediate Node)**?

| **Link Element Class** | **Description** | **Instance Set** |
| --- | --- | --- |
| **Controller** | Hardware element that manages or coordinates communication between a host/system component and one or more functional or peripheral elements. | Host controller, storage controller, display controller, USB controller |
| **Adapter** | Hardware element that enables communication between elements with different interfaces, protocols, electrical characteristics, or physical forms. | Network adapter, bus adapter, protocol adapter |
| **Bridge** | Hardware element that connects two distinct interconnect domains and mediates communication between them. | PCIe bridge, PCI bridge, bus bridge |
| **Switch** | Hardware element that provides multiple connection points and selectively forwards communication between connected elements. | PCIe switch, Ethernet switch, fabric switch |
| **Hub** | Hardware element that connects multiple elements to a shared communication domain and distributes communication within that domain. | USB hub, Ethernet hub |
| **Repeater** | Hardware element that regenerates and retransmits signals to extend or restore a communication path. | Ethernet repeater, PCIe retimer* |
| **Transceiver** | Hardware element capable of transmitting and receiving signals across a communication interface. | Ethernet transceiver, optical transceiver |
| **Multiplexer** | Hardware element that selects one of multiple communication paths and connects it to a shared path. | PHY multiplexer, lane multiplexer |
| **Demultiplexer** | Hardware element that separates a shared communication path into multiple selectable paths. | Demultiplexer, lane demultiplexer |
| **PHY** | Hardware element implementing physical-layer signaling between digital logic and the physical communication medium. | PCIe PHY, Ethernet PHY, USB PHY, SerDes PHY |

### Which are the of **Link Node Element  (Intermediate Node)**?

> **Note:** By *concrete*, we mean the **most specific commercially meaningful product category** that cannot be further subdivided for the purposes of this taxonomy and that **maps directly to identifiable vendor products**.
> 

| **Concrete Link Element** | **Description** | **Communication Arity** | **What does it connect?** | **Vendor Instance(s)** |
| --- | --- | --- | --- | --- |
| **Host Bridge** | Product category implementing the connection between the processor/system interconnect and an external I/O interconnect domain. | 1:N | CPU/System ↔ I/O Fabric | AMD Host Bridge; Intel Host Bridge |
| **PCIe Root Port** | PCIe port product/implementation providing a connection from the host into a downstream PCIe hierarchy. | 1:1 | Host ↔ PCIe Device/Switch | AMD PCIe Root Port; Intel PCIe Root Port |
| **PCIe Endpoint Controller** | PCIe controller product category implementing an endpoint interface for a device. | 1:1 | PCIe Fabric ↔ Device | Intel PCIe Controller; AMD PCIe Controller |
| **PCIe Switch** | Multi-port PCIe switching product forwarding PCIe transactions between ports. | N:N | PCIe Ports ↔ PCIe Ports | Broadcom/PLX PCIe Switch; Microchip PCIe Switch |
| **PCIe-to-PCI Bridge** | Bridge product connecting a PCIe hierarchy to a legacy PCI bus. | 1:1 / 1:N | PCIe ↔ PCI | ASMedia PCIe-to-PCI Bridge |
| **PCIe Retimer** | PCIe signal-integrity product that recovers and retransmits PCIe signals between link segments. | 1:1 | PCIe Link Segment ↔ PCIe Link Segment | Broadcom PCIe Retimer; Astera Labs Retimer |
| **PCIe Redriver** | PCIe signal-conditioning product that electrically retransmits high-speed signals. | 1:1 | PCIe Link Segment ↔ PCIe Link Segment | Texas Instruments PCIe Redriver; Parade PCIe Redriver |
| **USB Host Controller** | Host-controller product/implementation managing communication with USB devices. | 1:N | Host ↔ USB Devices | Intel xHCI; AMD xHCI |
| **USB Hub** | USB hub product expanding one upstream USB connection into multiple downstream ports. | 1:N | USB Upstream ↔ USB Downstream Ports | Microchip USB Hub; VIA Labs USB Hub |
| **USB Device Controller** | USB controller product providing a device-side USB interface. | 1:1 | USB Host ↔ USB Device | NXP USB Controller; Microchip USB Controller |
| **USB-to-SATA Bridge** | Bridge IC converting between USB and SATA interfaces. | 1:1 | USB ↔ SATA | ASMedia ASM1153; ASMedia ASM1351 |
| **SATA Controller** | SATA controller product providing host-side SATA connectivity. | 1:N | Host ↔ SATA Devices | ASMedia SATA Controller; Marvell SATA Controller |
| **SATA Port Multiplier** | SATA switching product allowing multiple SATA devices to share a host connection. | 1:N | SATA Host Port ↔ SATA Devices | ASMedia SATA Port Multiplier |
| **SAS HBA** | Host-bus-adapter product connecting a system to SAS storage devices. | 1:N | Host ↔ SAS Devices | Broadcom/LSI SAS HBA |
| **SAS Expander** | SAS switching/expansion product connecting multiple SAS initiators and targets. | N:N | SAS Initiators ↔ SAS Targets | Broadcom/LSI SAS Expander |
| **RAID Controller** | Storage-controller product providing host connectivity and RAID processing. | 1:N | Host ↔ Storage Devices | Broadcom MegaRAID |
| **NVMe Controller** | Controller product providing PCIe/NVMe connectivity to non-volatile storage media. | 1:1 | PCIe Host ↔ NVMe Media | Samsung NVMe Controller; Phison Controller |
| **Ethernet Network Adapter** | Network-adapter product providing system-side Ethernet connectivity. | 1:1 | System ↔ Ethernet Network | Intel Ethernet Adapter; Realtek Ethernet Adapter |
| **Ethernet Controller** | Ethernet controller product implementing host/network interface functionality. | 1:1 | System ↔ Ethernet PHY/Network | Intel Ethernet Controller; Realtek Ethernet Controller |
| **Ethernet PHY** | Ethernet physical-layer product implementing electrical or optical signaling. | 1:1 | Ethernet MAC ↔ Physical Medium | Marvell Alaska PHY; Realtek PHY |
| **Ethernet Switch** | Ethernet switching product forwarding frames between multiple network ports. | N:N | Ethernet Ports ↔ Ethernet Ports | Broadcom Tomahawk; Broadcom Trident |
| **Ethernet Bridge** | Ethernet bridge product forwarding frames between Ethernet segments. | 1:1 / N:N | Ethernet Segment ↔ Ethernet Segment | Ethernet Bridge Products |
| **Wi-Fi Network Adapter** | Network-adapter product providing system-side wireless LAN connectivity. | 1:1 | System ↔ Wi-Fi Network | Intel AX210; Qualcomm Wi-Fi Adapter |
| **Wi-Fi Controller** | Wi-Fi controller product implementing MAC/control functionality for wireless communication. | 1:1 | System ↔ Wi-Fi Radio | Qualcomm Wi-Fi Controller; MediaTek Wi-Fi Controller |
| **Wi-Fi Radio/PHY** | Wireless radio product implementing RF/baseband physical signaling. | 1:1 | Wi-Fi MAC ↔ Radio Medium | Qualcomm Wi-Fi Radio; MediaTek Wi-Fi Radio |
| **InfiniBand HCA** | Host-channel-adapter product connecting a system to an InfiniBand fabric. | 1:1 / 1:N | Host ↔ InfiniBand Fabric | NVIDIA/Mellanox ConnectX |
| **InfiniBand Switch** | InfiniBand switching product forwarding traffic between InfiniBand ports. | N:N | InfiniBand Ports ↔ InfiniBand Ports | NVIDIA/Mellanox InfiniBand Switch |
| **Fibre Channel HBA** | Host-bus-adapter product connecting a system to a Fibre Channel fabric. | 1:1 / 1:N | Host ↔ Fibre Channel Fabric | Broadcom Emulex HBA |
| **Fibre Channel Switch** | Fibre Channel switching product forwarding frames between FC ports. | N:N | FC Ports ↔ FC Ports | Broadcom/Brocade FC Switch |
| **DisplayPort Interface Controller** | Product/implementation providing a DisplayPort communication interface. | 1:1 | Display Controller ↔ Display | DisplayPort Controller Products |
| **HDMI Interface Controller** | Product/implementation providing an HDMI communication interface. | 1:1 | Display Controller ↔ Display | HDMI Controller Products |
| **DisplayPort-to-HDMI Bridge** | Display-interface bridge product converting DisplayPort to HDMI. | 1:1 | DisplayPort ↔ HDMI | Parade DisplayPort-to-HDMI Bridge; Analog Devices Bridge |
| **HDMI-to-DisplayPort Bridge** | Display-interface bridge product converting HDMI to DisplayPort. | 1:1 | HDMI ↔ DisplayPort | Realtek HDMI-to-DisplayPort Bridge |
| **Display PHY** | Physical-layer product implementing electrical signaling for a display interface. | 1:1 | Display Controller ↔ Physical Medium | DisplayPort PHY; HDMI PHY |
| **DDR Memory Controller** | Memory-controller product/implementation controlling communication with DRAM. | 1:N | CPU/Fabric ↔ DRAM | AMD DDR Memory Controller; Intel DDR Memory Controller |
| **Registered Memory Buffer** | Buffer/register product used between a memory controller and DRAM devices. | 1:N | Memory Controller ↔ DRAM | Registered DIMM Buffer |
| **CXL Memory Device** | CXL product providing host access to memory attached through CXL. | 1:N | CXL Host ↔ Expanded Memory | Samsung CXL Memory; Micron CXL Memory |
| **CXL Switch** | CXL switching product forwarding CXL traffic between multiple ports. | N:N | CXL Hosts ↔ CXL Devices | Microchip CXL Switch; Astera Labs CXL Switch |
| **CXL Host Interface** | Host-side product/implementation providing CXL connectivity to external devices. | 1:N | CPU/Fabric ↔ CXL Devices | Intel CXL Implementation; AMD CXL Implementation |
| **PCIe-to-PCI Adapter** | Adapter product implementing PCIe-to-PCI interconnect conversion. | 1:1 | PCIe ↔ PCI | PCIe-to-PCI Adapter IC |
| **USB-to-SATA Adapter** | Adapter product providing USB-to-SATA connectivity. | 1:1 | USB ↔ SATA | ASMedia USB-to-SATA Adapter |
| **PCIe SerDes** | Commercial SerDes product/component used for high-speed PCIe serial communication. | 1:1 | Digital PCIe Logic ↔ Serial Link | PCIe SerDes Products |
| **Ethernet SerDes** | SerDes product/component implementing high-speed Ethernet serialization. | 1:1 | Ethernet Logic ↔ Serial Link | Broadcom SerDes; Marvell SerDes |
| **Optical Transceiver** | Pluggable transceiver product converting electrical data to/from optical signals. | 1:1 | Electrical Interface ↔ Optical Medium | NVIDIA/Mellanox; Finisar; Coherent |
| **Ethernet Repeater** | Repeater product regenerating Ethernet signals to extend a physical link. | 1:1 | Ethernet Segment ↔ Ethernet Segment | Ethernet Repeater Products |
| **PCIe Lane Multiplexer** | PCIe lane-selection product selecting between multiple PCIe signal paths. | N:1 | Multiple PCIe Paths ↔ Shared Path | PCIe Lane Mux Products |
| **PCIe Lane Demultiplexer** | PCIe lane-distribution product distributing one path among multiple outputs. | 1:N | Shared PCIe Path ↔ Multiple Paths | PCIe Lane Demux Products |
| **Interconnect Crossbar** | Commercial switching/interconnect product providing selectable connections among multiple sources and destinations. | N:N | Multiple Sources ↔ Multiple Destinations | SoC/FPGA Interconnect Products |
| **Fabric Router** | Hardware routing product forwarding packets between nodes of a communication fabric. | N:N | Fabric Nodes ↔ Fabric Nodes | NVIDIA Fabric Router; Broadcom Fabric ASIC |
| **Network Router** | Network routing product forwarding packets between network domains. | N:N | Network ↔ Network | Cisco Router; Juniper Router |
| **Network Gateway** | Gateway product connecting network or protocol domains with potentially different semantics. | N:N | Network Domain ↔ Network Domain | Cisco Gateway; Juniper Gateway |
| **DMA Controller** | Hardware product/implementation performing autonomous data movement between memory and I/O. | N:N | Memory ↔ I/O Interfaces | Intel DMA Controller; AMD DMA Controller |
| **Interrupt Controller** | Interrupt-controller product/implementation collecting, prioritizing, and routing interrupt events. | N:N | Devices ↔ CPU Cores | Intel APIC/IO-APIC; ARM GIC |
| **Clock Buffer** | Clock-distribution product driving multiple downstream clock consumers. | 1:N | Clock Source ↔ Clock Consumers | Renesas Clock Buffer; TI Clock Buffer |
| **Clock Generator** | Clock-generation product producing one or more derived clock signals. | 1:N | Reference Clock ↔ Clock Domains | Renesas Clock Generator; Silicon Labs Clock Generator |
| **Clock Domain Crossing Controller** | Product/implementation providing controlled transfer between independently clocked domains. | 1:1 | Clock Domain ↔ Clock Domain | FPGA/SoC CDC Implementation |
| **PCIe Connector** | Connector product providing detachable PCIe electrical connectivity. | 1:1 | Device ↔ Cable/Board | Molex PCIe Connector; Amphenol PCIe Connector |
| **USB Connector** | Connector product providing detachable USB connectivity. | 1:1 | Device ↔ Cable | USB-C Connector Products |
| **SFP/QSFP Connector** | Pluggable connector/cage product providing an interface for optical or electrical transceiver modules. | 1:1 | Network Device ↔ Transceiver | Molex SFP/QSFP; Amphenol SFP/QSFP |
| **PCIe Cable Assembly** | Manufactured cable product carrying PCIe signals between connectors. | 1:1 | PCIe Connector ↔ PCIe Connector | Amphenol PCIe Cable; Samtec PCIe Cable |
| **Ethernet Cable Assembly** | Manufactured cable product carrying Ethernet signals between network interfaces. | 1:1 | Ethernet Port ↔ Ethernet Port | Belden Ethernet Cable; Amphenol Ethernet Cable |
| **Optical Cable Assembly** | Manufactured fiber-optic cable product carrying optical communication signals. | 1:1 | Optical Transceiver ↔ Optical Transceiver | Corning Optical Cable; Amphenol Optical Cable |
| **Server Backplane** | Board-level interconnection product providing connectivity among pluggable server modules. | N:N | Server Modules ↔ Server Modules | Dell Backplane; HPE Backplane; Supermicro Backplane |
| **Storage Backplane** | Board-level interconnection product providing connectivity between storage drives and storage controllers. | N:N | Storage Drives ↔ Storage Controller | Dell Storage Backplane; Supermicro Storage Backplane |
| Midplane Assembly | Board-level interconnection product connecting modules or boards through a central interconnect structure. | N:N | Boards/Modules ↔ Boards/Modules | Dell PowerEdge MX7000 Midplane; HPE Synergy 12000 Frame Midplane; Supermicro SuperBlade Midplane; Cisco UCS 5108 Midplane; IBM BladeCenter Midplane |

### What are the types of physical communication media?

| **Physical Communication Medium** | **Description** |
| --- | --- |
| **PCB Copper Trace** | Conductive copper structure on a printed circuit board used to carry electrical signals between components, connectors, and interfaces. |
| **Copper Wire** | Metallic conductor used to carry electrical signals between hardware elements. |
| **Copper Twisted Pair** | Pair or pairs of insulated copper conductors twisted together to reduce electromagnetic interference and crosstalk. |
| **Coaxial Cable** | Shielded copper conductor structure in which a central conductor is surrounded by dielectric material and an outer conductive shield. |
| **Copper Cable** | Cable assembly containing one or more copper conductors used to carry electrical signals. |
| **Backplane Copper** | Conductive copper structures within a backplane used to interconnect multiple hardware modules. |
| **Package Substrate** | Multilayer substrate inside a semiconductor package providing conductive paths between dies, package interfaces, and external contacts. |
| **Silicon Interconnect** | Conductive structures within a semiconductor die used to transmit electrical signals between integrated-circuit elements. |
| **Silicon Interposer** | Semiconductor interconnect substrate providing high-density electrical connections between dies or chiplets. |
| **Wire Bond** | Fine conductive wire providing an electrical path between a semiconductor die and its package substrate or lead frame. |
| **Solder Bump** | Conductive solder structure providing an electrical connection between a die, package substrate, or circuit board. |
| **Microbump** | Miniaturized conductive bump used for high-density die-to-die or die-to-package electrical connections. |
| **Lead Frame** | Metallic package structure providing conductive paths between a semiconductor die and external package terminals. |
| **Socket Contact** | Conductive contact structure in a socket providing a removable electrical connection between a component and its host assembly. |
| **Connector Contact** | Conductive contact within a connector providing a detachable electrical connection between hardware assemblies. |
| **Optical Fiber** | Dielectric waveguide that carries information using modulated optical signals. |
| **Optical Waveguide** | Structured dielectric path that confines and guides optical signals between optical components. |
| **Free Space** | Open propagation environment through which electromagnetic radiation travels without a physical guiding structure. |
| **Air** | Atmospheric propagation environment through which radio-frequency, microwave, or optical signals can propagate. |
| **Vacuum** | Propagation environment without matter through which electromagnetic signals can travel. |
| **Inductive Coupling** | Short-range electromagne |

### Which are the type of **communication** signal used?

> A **communication signal** is a physical representation of information, control, state, timing, or synchronization that propagates through a communication medium.
> 

| **Signal Domain** | **Concrete Communication Signal** | How is data encoded? | Instance(s) |
| --- | --- | --- | --- |
| **Electrical** | **Single-Ended Voltage Signal** | Voltage of one conductor relative to a reference/ground | GPIO, UART |
| **Electrical** | **Differential Voltage Signal** | Voltage difference between two conductors | PCIe, USB, Ethernet |
| **Electrical** | **Single-Ended Current Signal** | Current through a conductor | Current-loop interfaces |
| **Electrical** | **Differential Current Signal** | Difference between currents in paired conductors | Specialized high-speed links |
| **Electrical** | **Digital Pulse Signal** | Discrete voltage transitions/pulses | GPIO, clock, reset |
| **Electrical** | **Multi-Level Electrical Signal** | Multiple discrete voltage levels | PAM-4 Ethernet/PCIe-related high-speed signaling |
| **Electrical** | **Analog Electrical Waveform** | Continuously varying voltage/current waveform | Analog audio, sensor interfaces |
| **Optical** | **Optical Intensity Signal** | Optical power/light intensity | Ethernet over fiber |
| **Optical** | **Optical Phase Signal** | Phase of an optical carrier | Coherent optical communication |
| **Optical** | **Optical Wavelength Signal** | Optical carrier wavelength | WDM optical communication |
| **RF / EM** | **RF Electromagnetic Wave** | Time-varying electromagnetic field propagating through space | Wi-Fi, Bluetooth, cellular |
| **RF / EM** | **Microwave Electromagnetic Wave** | High-frequency electromagnetic field | Radar, microwave links |
| **RF / EM** | **Millimeter-Wave Signal** | Electromagnetic wave in the mmWave frequency range | 5G mmWave, automotive radar |
| **Magnetic** | **Magnetic-Field Signal** | Controlled magnetic-field variation | Inductive communication, magnetic coupling |
| **Acoustic** | **Acoustic Pressure Wave** | Mechanical pressure variation in a medium | Ultrasonic communication |

### How to characterized an edged?

> Note: The Physical Interface does not matter because we treat those just as nodes.
> 

| **Dimension** | **Description** |
| --- | --- |
| **Endpoints** | The hardware elements connected by the edge. |
| **Connection Role** | The architectural role of the connection, such as communication, power delivery, control, synchronization, or mechanical attachment. |
| **Connection Mechanism** | The mechanism by which the endpoints exchange energy, signals, or information, such as conductive, optical, capacitive, inductive, or radiative coupling. |
| **Communication Medium** | The physical medium carrying the signal, such as PCB copper trace, copper wire, optical fiber, or free space. |
| **Signal** | The concrete physical signal propagated through the medium, such as differential electrical signaling, optical intensity modulation, or an RF electromagnetic wave. |
| **Protocol** | The communication protocol governing the exchange, such as PCIe, USB, Ethernet, I²C, SPI, or IEEE 802.11. |
| **Signaling Scheme** | The electrical, optical, or electromagnetic encoding/signaling technique used to represent information on the medium. |
| **Directionality** | Whether communication is unidirectional, bidirectional, half-duplex, or full-duplex. |
| **Topology** | The structural relationship formed by the connection, such as point-to-point, shared bus, ring, star, tree, or mesh. |
| **Logical Channel** | The logical communication channel carried by the physical connection, when multiple channels share the same physical link. |
| **Data Flow** | The type and direction of information exchanged, such as data, commands, status, control, interrupts, or synchronization. |
| **Bandwidth** | The frequency range or nominal information-carrying capacity available to the connection. |
| **Data Rate** | The rate at which information or symbols are transmitted over the connection. |
| **Latency** | The time required for a signal or communicated information to traverse the connection. |
| **Reliability** | The expected ability of the connection to transfer information correctly and remain operational. |
| **Error Control** | Mechanisms used to detect, correct, or recover from transmission errors. |
| **Synchronization** | Mechanisms used to establish timing, clocking, framing, or coordination between endpoints. |
| **Power Relationship** | Whether the connection also supplies or transfers electrical power between endpoints. |
| **Physical Scope** | The physical architectural level at which the connection exists, such as intra-chip, chip-to-chip, board-level, module-level, or device-to-device. |
| **Persistence** | Whether the connection is permanent, removable, dynamically established, or switched. |
| **Multiplicity** | Number of physical or logical communication channels composing the edge. |

### Which are the communication protocol or standards?

| **Communication Protocol - Standard** | **Description** | **Usage** |
| --- | --- | --- |
| **PCI Express (PCIe)** | High-speed serial interconnect standard for point-to-point communication between processors, controllers, and peripheral devices. | GPUs, NVMe SSDs, network adapters, expansion devices |
| **Compute Express Link (CXL)** | High-speed coherent interconnect standard built on the PCIe physical layer for communication between processors, memory, and accelerators. | CPUs, accelerators, memory expanders, memory pooling |
| **USB** | Serial bus standard for connecting host systems to peripheral devices. | Keyboards, mice, storage devices, cameras, hubs, phones |
| **SATA** | Serial interface standard for connecting storage devices to host controllers. | HDDs, SATA SSDs, optical drives |
| **SAS** | Serial storage interface standard supporting high-reliability storage connectivity. | Enterprise HDDs, SSDs, storage enclosures |
| **NVMe** | Protocol for accessing non-volatile memory storage over high-speed interfaces, commonly PCIe. | NVMe SSDs |
| **DDR SDRAM** | Memory interface standard defining communication between memory controllers and DRAM. | System RAM |
| **I²C** | Two-wire synchronous serial bus specification using shared clock and data lines. | Sensors, EEPROMs, PMICs, low-speed peripherals |
| **I3C (MIPI I3C)** | Two-wire serial bus standard developed by MIPI that provides higher performance and more advanced device-management capabilities than I²C while maintaining substantial compatibility. | Sensors, embedded peripherals, mobile and automotive systems |
| **SPI** | Synchronous serial communication interface using clock, data, and device-select signals. | Flash memory, ADCs, DACs, sensors, controllers |
| **UART** | Asynchronous serial communication interface using transmitted and received serial data streams. | Debug consoles, embedded devices, serial peripherals |
| **I²S** | Synchronous serial interface designed primarily for transferring digital audio between audio components. | Audio codecs, DACs, ADCs, DSPs, SoCs |
| **TDM (Time-Division Multiplexing)** | Communication technique that multiplexes multiple independent data channels into sequential time slots over a shared serial interface. | Multichannel digital audio, codecs, DSPs, telephony |
| **AC'97** | Intel-defined digital audio interface specification connecting audio codecs with host audio controllers. | Legacy PC audio hardware, audio codecs |
| **CAN** | Multi-master serial communication protocol designed for robust communication over shared bus networks. | Automotive and industrial control systems |
| **Ethernet (IEEE 802.3)** | Family of wired LAN communication standards defining physical and data-link communication. | LANs, switches, routers, network interfaces |
| **Wi-Fi (IEEE 802.11)** | Family of wireless LAN standards defining communication over radio-frequency electromagnetic signals. | Wireless networking |
| **Bluetooth** | Short-range wireless communication standard for personal-area networking. | Headsets, keyboards, mice, peripherals, sensors |
| **DisplayPort** | Digital display interface standard for transmitting video, audio, and auxiliary data. | GPUs, monitors, docking stations |
| **HDMI** | Digital audio/video interface standard for transmitting audiovisual data. | GPUs, monitors, televisions, projectors |
| **MIPI CSI-2** | Camera serial interface standard for transferring image data from cameras to processors. | Cameras, smartphones, embedded vision systems |
| **MIPI DSI** | Display serial interface standard for transferring display data from processors to display panels. | Mobile and embedded displays |
| **SD / SDIO** | Standards for removable flash storage and peripheral communication over SD interfaces. | SD cards, embedded storage, peripherals |
| **eMMC** | Standardized embedded storage device interface combining flash memory and a controller. | Embedded storage |
| **UFS** | High-performance serial storage interface standard for embedded flash storage. | Smartphones, embedded systems |
| **IEEE 1394 (FireWire)** | Serial bus standard supporting high-speed peripheral communication. | Legacy cameras, multimedia peripherals |
| **Thunderbolt** | High-speed interconnect technology combining protocols such as PCIe and DisplayPort over a single connection. | Docking stations, displays, external storage, peripherals |
| **InfiniBand** | High-performance switched fabric standard for low-latency, high-bandwidth communication. | HPC systems, servers, data centers |
| **Fibre Channel** | High-speed networking standard designed primarily for storage-area networks. | Enterprise storage networks |
| **Modbus** | Industrial communication protocol for exchanging data between controllers and devices. | Industrial automation |
| **PROFINET** | Industrial Ethernet communication standard for real-time industrial automation. | PLCs, industrial controllers, I/O systems |
| **EtherCAT** | Real-time Ethernet-based fieldbus standard optimized for deterministic industrial control. | Motion control, industrial automation |

### Which are the edged?

> Note: The edges here does not cover Networking Device (Router, etc), with other Networking Devices - just the Computing System.
> 

| **Dimension** | **Description** |
| --- | --- |
| **Edge** | The connection relationship between hardware elements. |
| Description | A concise semantic description of what the edge represents. |
| **Link Element Set** | The set of hardware elements connected by the edge. |
| **Edge Characterization** | The essential properties defining how the connected elements communicate: **Physical Communication Medium, Communication Signal, Communication Protocol, and Directionality**. |

| **Edge** | **Description** | **Link Element Set** | **Edge Characterization** |
| --- | --- | --- | --- |
| **PCIe Connection — PCI Express** | High-speed serial interconnect used to connect processors, controllers, expansion devices, and other PCIe endpoints. | High-speed differential electrical signaling over PCB traces, package wiring, or cable | Root Complex ↔ Endpoint / Switch |
| **USB Connection — USB** | Serial peripheral interconnect used to connect a host controller with external and internal peripheral devices. | Differential electrical signaling over copper conductors | USB Host ↔ USB Device / Hub |
| **SATA Connection — SATA** | Serial storage interconnect used to connect a host storage controller with SATA storage devices. | Differential electrical signaling over copper conductors | SATA Controller ↔ Storage Device |
| **SAS Connection — SAS** | Serial storage interconnect providing communication between storage controllers, drives, and expanders. | Differential electrical signaling over copper or optical media | SAS Controller ↔ Storage Device / Expander |
| **NVMe over PCIe Connection — NVMe + PCIe** | Storage connection in which the NVMe protocol operates over a PCIe interconnect to provide access to non-volatile storage. | PCIe electrical signaling | NVMe Controller ↔ PCIe Root Complex |
| **DDR Memory Connection — DDR/LPDDR** | Memory interconnect used by a memory controller to communicate with DRAM devices. | Parallel/semi-parallel electrical signaling over PCB/package interconnects | Memory Controller ↔ DRAM |
| **CPU Memory-Bus Connection — DDR-family** | Processor memory interface providing communication between the processor's memory controller and system memory. | Electrical signaling through package/PCB traces | CPU / Memory Controller ↔ DIMM |
| **CPU Interconnect — AMD Infinity Fabric / Intel UPI / proprietary** | Processor-level interconnect used to exchange data, coherence information, control information, or memory traffic between processor components. | High-speed electrical signaling | CPU ↔ CPU / Die ↔ Die / Controller |
| **Chiplet Interconnect — UCIe / proprietary** | Package-level interconnect used to communicate between separately fabricated chiplets within a processor package. | Package-level electrical signaling | Chiplet ↔ Chiplet |
| **On-Chip Interconnect — NoC / proprietary** | Interconnect implemented within an integrated circuit to connect processor cores, caches, memory controllers, accelerators, and other IP blocks. | On-die electrical signaling | IP Block ↔ IP Block |
| **AXI Connection — AMBA AXI** | On-chip transaction interconnect used to connect high-performance processing, memory, DMA, and peripheral components. | On-chip electrical signaling | CPU / DMA / Accelerator ↔ Memory / Peripheral |
| **AHB Connection — AMBA AHB** | On-chip bus interconnect used for communication between processors, memories, and peripherals. | On-chip electrical signaling | Processor ↔ Peripheral / Memory |
| **APB Connection — AMBA APB** | Low-complexity on-chip peripheral interconnect used for control and configuration registers. | On-chip electrical signaling | Bus Bridge ↔ Peripheral |
| **Ethernet Connection — IEEE 802.3** | Network interconnect used to exchange Ethernet frames between network interfaces or network infrastructure devices. | Electrical or optical signaling | Ethernet Interface ↔ Ethernet Interface |
| **Ethernet PHY Connection — Ethernet PHY** | Physical-layer connection carrying Ethernet signaling between a MAC-side interface and a physical transceiver or between physical interfaces. | Electrical/optical physical signaling | MAC ↔ PHY / PHY ↔ PHY |
| **USB-C Connection — USB / USB-C** | Physical connection interface supporting USB communication and, depending on implementation, other alternate modes and power delivery. | Electrical signaling through connector conductors | Device ↔ Device / Host ↔ Peripheral |
| **Thunderbolt Connection — Thunderbolt** | High-speed external interconnect carrying PCIe and display-related traffic between a host and peripheral devices. | High-speed differential electrical signaling over copper or optical media | Host ↔ Peripheral |
| **DisplayPort Connection — DisplayPort** | Digital display interconnect used to transport video, audio, and auxiliary control information between a display source and sink. | High-speed differential electrical signaling | GPU / Display Adapter ↔ Monitor |
| **HDMI Connection — HDMI** | Digital audiovisual interconnect used to transport video, audio, and control information between source and display devices. | TMDS/FRL electrical signaling over copper | GPU / Display Adapter ↔ Display |
| **DVI Connection — DVI** | Digital or analog display interconnect used to transmit video from a graphics device to a display. | Differential electrical signaling | Display Adapter ↔ Display |
| **VGA Connection — VGA** | Analog display interconnect used to transmit RGB video and synchronization signals. | Analog electrical signaling | Display Adapter ↔ Display |
| **I²C Connection — I²C** | Low-speed serial control interconnect used for communication between controllers and peripheral or management devices. | Open-drain electrical signaling over SDA/SCL | Controller ↔ Peripheral |
| **SMBus Connection — SMBus** | System-management interconnect derived from I²C and used for monitoring, configuration, and management communication. | Electrical signaling over SMBus lines | Controller ↔ Management Device |
| **SPI Connection — SPI** | Synchronous serial interconnect commonly used for short-distance communication with peripherals and controllers. | Single-ended electrical signaling over clock/data/select lines | Controller ↔ Peripheral |
| **UART Connection — UART** | Asynchronous serial communication mechanism used to exchange character-oriented or byte-oriented data between devices. | Asynchronous electrical signaling | Controller ↔ Serial Device |
| **RS-232 Connection — RS-232** | Point-to-point serial communication interface defining electrical signaling and communication characteristics for serial devices. | Electrical signaling over copper | Serial Interface ↔ Serial Device |
| **RS-485 Connection — RS-485** | Differential serial physical-layer interconnect designed to support communication over relatively long copper connections and multidrop configurations. | Differential electrical signaling | Controller ↔ Controller / Device |
| **CAN Connection — CAN** | Multi-node control-network interconnect designed for reliable real-time communication between distributed controllers and devices. | Differential electrical signaling over twisted pair | CAN Controller ↔ CAN Nodes |
| **LIN Connection — LIN** | Low-cost single-wire serial interconnect used primarily for communication among automotive control devices. | Single-wire electrical signaling | Controller ↔ Automotive Nodes |
| **Bluetooth Connection — Bluetooth** | Short-range wireless interconnect used to exchange data between Bluetooth-enabled devices. | 2.4-GHz RF signaling | Bluetooth Radio ↔ Bluetooth Radio |
| **Wi-Fi Connection — IEEE 802.11** | Wireless LAN interconnect used to exchange network frames between wireless stations and network infrastructure. | RF electromagnetic signaling | Wi-Fi Station ↔ Access Point / Station |
| **WWAN Connection — 3GPP cellular standards** | Wide-area wireless interconnect providing communication between a cellular modem and a cellular network. | RF electromagnetic signaling | Cellular Modem ↔ Base Station |
| **NFC Connection — NFC / ISO/IEC 14443** | Very-short-range wireless interconnect used for communication between compatible devices, cards, and tags. | Near-field electromagnetic coupling | NFC Device ↔ NFC Device / Tag |
| **Zigbee Connection — IEEE 802.15.4 + Zigbee** | Low-power wireless interconnect used to connect distributed sensor, control, and automation devices. | RF signaling | Radio Node ↔ Radio Node |
| **Copper Cable Connection — Protocol-dependent** | Physical communication connection implemented using copper conductors and carrying a protocol-specific electrical signal. | Electrical signaling through copper conductors | Interface ↔ Interface |
| **PCB Trace Connection — Protocol-dependent** | Electrical connection implemented by conductive traces on a printed circuit board between components or interfaces. | Electrical signaling through PCB traces | Component ↔ Component |
| **Package Interconnect — Protocol-dependent** | Electrical connection within or across a semiconductor package used to connect dies, chiplets, or package interfaces. | Electrical signaling through package substrate / bumps | Die ↔ Die / Die ↔ Package |
| **Wire Bond Connection — Protocol-dependent** | Physical electrical connection between a semiconductor die and package substrate implemented using wire bonds. | Electrical signaling through bond wires | Die ↔ Package |
| **Bump / Microbump Connection — Protocol-dependent** | High-density physical connection between semiconductor dies or between a die and package substrate using conductive bumps. | Electrical signaling through solder/microbumps | Die ↔ Die / Die ↔ Substrate |

## CPU–Device Communication

### How can the CPU communicate with this node? What is the communication path from the CPU to the node, and how many edges does that path traverse?

> Aka. Communication Chain.
> 

> This is a key guiding question in this node.
> 

> Take The Case - CPU - Monitor:   **CPU → I/O/Fabric → Root Complex → PCIe Root Port → PCIe Link → GPU Endpoint → GPU Display Engine → Display Transmitter → DisplayPort/HDMI Link → Monitor Receiver → Display Panel**.
> 

### **Which are the CPU-to-Device (Either  - Directly or Indirectly)  Hardware Communication Strategy?**

> **Hardware Communication Strategy:** The strategy by which information is transferred between a source hardware element and a destination hardware element, specifying whether the communication occurs directly between the endpoints or indirectly through an intermediate hardware element or shared communication resource.
> 

> There are two major strategies: **direct communication through a communication path (link/edge path), or indirect communication through an intermediate hardware element or shared resource (e.g., DMA or shared memory).**
> 

> Note:  In order to connect node a → node b, they can be multiple strategies, paths, etc.
> 

| **Strategy** | **Description** | **Communication Path** | **Usage** | **Variations** |
| --- | --- | --- | --- | --- |
| **Direct Communication** | Source and destination exchange information through a direct communication relationship/path without an intermediate communication agent performing the transfer. | **Source → Communication Path → Destination** | Direct control, register access, direct data exchange | MMIO, PMIO, direct point-to-point communication |
| **Mediated Communication** | Source and destination communicate through an intermediate hardware element that participates in, manages, or performs the transfer. | **Source → Intermediate Element → Destination** | Autonomous data movement, protocol conversion, routing, switching | DMA, bridge-mediated, controller-mediated, switch-mediated |
| **Shared-Resource Communication** | Source and destination communicate by independently accessing a shared hardware resource rather than transferring information directly between one another. | **Source → Shared Resource ← Destination** | Shared buffers, queues, command/completion exchange | Shared memory, memory-resident queues, ring buffers |
| **Message-Mediated Communication** | Source communicates by sending an explicit message that is received and processed by an intermediate communication or management element. | **Source → Message Interface → Intermediate Element → Destination** | Commands, control, management, asynchronous requests | Mailbox, message queue, command processor |
| **Notification-Mediated Communication** | One element communicates a state change or event through an intermediate notification mechanism rather than transferring the underlying data through the notification path. | **Source → Notification Mechanism → Destination** | Completion, event notification, synchronization | Interrupt, MSI/MSI-X, GPIO interrupt, doorbell |
| **Peer-to-Peer Communication** | Two devices exchange data directly without requiring the CPU to perform the data transfer. | **Device A → Interconnect → Device B** | GPU-to-GPU, NIC-to-device, storage-to-device transfers | PCIe P2P, device DMA, fabric-mediated P2P |

### MMIO and PMIO are abstract device-access mechanisms. What is their physical realization in the hardware?

> **MMIO and PMIO do not have a unique physical realization of their own.** They are **architectural access mechanisms** that are realized through an underlying interconnect and its physical signaling.
> 

Cases:

- MMIO → PCIe Memory Transaction → PCIe electrical signaling → PCB copper traces
- PMIO → PCIe I/O Transaction → PCIe electrical signaling → PCB copper traces

MMIO Realization:

```bash
CPU Node
   │
   │ Link
   │ Host / CPU interconnect
   ▼
PCIe Root Complex Node
   │
   │ Link
   │ PCIe
   ▼
RTL8821CE Wi-Fi Controller Node
```

PMIO Realization:

```bash
CPU Node
   │
   │ Link
   │ Host / I/O interconnect
   ▼
PCIe Root Complex Node
   │
   │ Link
   │ PCIe
   ▼
RTL8821CE Wi-Fi Controller Node
```

### If the communication path is essentially the same, what distinguishes MMIO from PMIO?

> If the communication path is essentially the same, **MMIO and PMIO are distinguished by the CPU/ISA-level addressing and transaction semantics—memory-address-space load/store operations versus a separate I/O-port address space with dedicated I/O operations—which the host bridge/interconnect translates into the corresponding device-access transactions.**
> 

### How can the CPU communicate with this the Wifi Router Node? What is the communication path from the CPU to the node, and how many edges does that path traverse? Which are the the communication strategies?

```bash
CPU
 │
 │  Edge 1: CPU ↔ I/O interconnect / Root Complex
 ▼
PCIe Root Complex
 │
 │  Edge 2: PCIe link
 ▼
Wi-Fi Adapter / Controller
 │
 │  Edge 3: RF interface + antenna + wireless medium
 ▼
Wi-Fi Router Node
```

 Which are the the communication strategies? It’s usually MMIO.

## How does the operating system recognize the underlying complex, `multi rooted hardware` substrate interconnection mechanisms, and how does it operationalize them?

> A topology interpreter and operational coherence layer for heterogeneous hardware communication systems.
> 

> How does the **`Kernel Creates`**  ‘Unified Abstract Machine’?
> 

> The kernel transforms: electrical connectivity → into: software topology.
> 

> The kernel traverses hardware fabrics recursively.
> 

> Which communication endpoints exist behind this interconnect node?
> 

| Interconnect | Enumeration Mechanism |
| --- | --- |
| PCIe | Configuration-space scanning |
| USB | Hub interrogation |
| ACPI | Namespace traversal |
| Device Tree | Tree parsing |
| NVMe | Controller discovery |
| SCSI | Bus scan |
| I2C | Address probing |
| SPI | Controller-managed discovery |

Internally, the kernel constructs a graph-like model.

```jsx
CPU Complex
 ├── Memory Controller
 ├── PCIe Root Complex
 │     ├── GPU
 │     ├── NVMe SSD
 │     └── USB Controller
 │            ├── Keyboard
 │            └── Webcam
 └── Interrupt Controller
```

## QA

### Is there a main system bus? Is there a root in the whole set of interconnect mechanisms?

> Modern computer systems are organized as hierarchical interconnect architectures composed of multiple nested communication domains, protocol fabrics, controllers, bridges, and switching mechanisms rather than a single centralized system bus.
> 

```jsx
                ┌────────────┐
                │ CPU Cores  │
                └─────┬──────┘
                      │
             Coherence / NoC Fabric
                      │
      ┌───────────────┼───────────────┐
      │               │               │
 Memory Ctrl      PCIe Root       Accelerator
      │            Complex           Fabric
      │               │               │
    DRAM         PCIe Devices      GPUs/NPUs
```

### How to map the interconnect topology of my Linux Computer System?

- tree /sys/devices
- lspci -tv (PCIe Topology)
- lsusb -t
- lspci -k (Show Kernel Driver Association)
- lsmod (Shoew Some Drivers) (Are all drivers kernel modules?)
- lscpu ()
- cat /proc/interrupts (Interrupt Topology)
- cat /proc/iomem (...)

### Which is the space of controller & adapters?

| Type | Name | Description |
| --- | --- | --- |
| **Controller** | USB Controller | Controls and manages communication over the USB interconnect. |
| **Controller** | SATA Controller | Controls communication between the system and SATA storage devices. |
| **Controller** | NVMe Controller | Provides the control interface between the system and NVMe storage. |
| **Controller** | Ethernet Controller | Implements and controls Ethernet network communication. |
| **Controller** | Wi-Fi Controller | Implements and controls wireless LAN communication. |
| **Adapter** | Ethernet Adapter | Hardware interface exposing Ethernet connectivity to the system. |
| **Adapter** | Wi-Fi Adapter | Hardware interface providing Wi-Fi connectivity. |
| **Adapter** | Bluetooth Adapter | Hardware interface providing Bluetooth connectivity. |
| **Adapter** | WWAN Adapter | Hardware interface providing cellular/WWAN connectivity. |
| **Adapter** | Display Adapter | Hardware interface providing connection to a display subsystem. |

### How does the OS discovers and model the Interconnect Topology?

> The OS discovers and models interconnect topology by **combining firmware-provided descriptions (ACPI/Device Tree), bus- and fabric-specific enumeration and probing (PCIe, USB, I²C, SPI, etc.), and hardware identification/configuration mechanisms to recursively discover communication domains, controllers, bridges, switches, buses, and endpoints, reconstruct their parent–child and interconnection relationships into a kernel-managed device/resource topology, bind each discovered element to its appropriate driver and resources (MMIO, I/O ports, IRQs, DMA/IOMMU, power), and thereby transform a heterogeneous, physically distributed hardware interconnect substrate into a coherent software-operational model through which the kernel can address, configure, communicate with, and manage devices.
> 

```bash
                    COMPUTER SYSTEM
                          │
             ┌────────────┴────────────┐
             │                         │
       HARDWARE SPACE             SOFTWARE SPACE
             │                         │
      Physical / Logical         Kernel Device Model
       Hardware Topology               │
             │                         ├── Devices
             │                         ├── Buses
             │                         ├── Drivers
             │                         ├── Resources
             │                         ├── IRQs
             │                         ├── DMA/IOMMU
             │                         └── Power
             │
             ▼
      Communication Paths
             │
             ▼
      Hardware Transactions
```

### **Which communication paths (link-node-element paths) are used to deliver interrupts?**

> The communication path used by an interrupt **does not have to be an interrupt-specific link**; an interrupt may either use a dedicated signaling path or be transported over an existing data/interconnect path.
> 

```bash
Interrupt Source
      │
      │
      ▼
[Interrupt Signal]
      │
      │ carried by
      ▼
[Communication Path]
      │
      ├── Edge
      ├── Link Element
      ├── Edge
      ├── Link Element
      └── ...
      │
      ▼
Interrupt Controller
      │
      ▼
CPU
```

| **Interrupt Delivery Mechanism** | **Interrupt Source** | **Communication Path (Link- Node- Element Path)** | **Content** | **Dedicated Interrupt Path?** |
| --- | --- | --- | --- | --- |
| **Legacy INTx — PCI/PCIe** | PCI/PCIe device | Device → Interrupt Line → **IO-APIC** → Interrupt Routing → **Local APIC** → CPU | Dedicated interrupt signaling | **Yes** |
| **MSI — PCIe** | PCIe endpoint | Device → **PCIe Endpoint** → PCIe Link → **PCIe Root Complex/Fabric** → Interrupt Controller → CPU | PCIe memory-write transaction | **No** |
| **MSI-X — PCIe** | PCIe endpoint | Device → **PCIe Endpoint** → PCIe Link → PCIe Fabric/Root Complex → Interrupt Controller → CPU | PCIe MSI-X message transaction | **No** |
| **GPIO Interrupt** | GPIO-connected peripheral | Peripheral → GPIO Signal → **GPIO Controller / Interrupt Controller** → CPU | Electrical interrupt signal | **Yes** |
| **SoC Peripheral Interrupt** | SoC peripheral | Peripheral → On-Chip Interrupt Connection → **Interrupt Router / GIC** → CPU | On-chip interrupt signaling | **Usually** |
| **GIC SPI — ARM** | Peripheral | Peripheral → **GIC Distributor** → **GIC CPU Interface** → CPU | Interrupt signal/state | **Logical dedicated path** |
| **GIC PPI — ARM** | CPU-local peripheral | CPU-local peripheral → **GIC CPU Interface** → CPU | Interrupt signal | **Yes / local** |
| **GIC SGI / IPI — ARM** | CPU core | CPU → GIC → CPU | Interrupt message/signal | **Logical** |
| **APIC IPI — x86** | CPU core | CPU → **Local APIC / APIC fabric** → destination CPU | Interrupt message | **Logical** |
| **IO-APIC Interrupt — x86** | Platform peripheral | Peripheral → **IO-APIC** → **APIC system** → Local APIC → CPU | Interrupt signal + interrupt message | **Yes at source** |
| **USB Interrupt Transfer** | USB device | USB Device → USB Link → **USB Hub(s)** → **USB Host Controller** → PCIe/SoC interconnect → Interrupt Controller → CPU | USB transaction + host-controller interrupt | **No dedicated CPU path** |
| **USB Host-Controller MSI** | USB device / host controller | USB Device → USB Link → USB Host Controller → **PCIe/SoC Fabric** → Interrupt Controller → CPU | USB transaction + MSI | **No** |
| **NVMe MSI/MSI-X** | NVMe controller | NVMe Controller → PCIe Endpoint → PCIe Link → **PCIe Root Complex/Fabric** → Interrupt Controller → CPU | PCIe MSI/MSI-X transaction | **No** |
| **Network NIC MSI-X** | Ethernet NIC | NIC → PCIe Endpoint → PCIe Link → **PCIe Root Complex/Fabric** → Interrupt Controller → CPU | PCIe MSI-X transaction | **No** |
| **GPU MSI/MSI-X** | GPU | GPU → PCIe Endpoint → PCIe Link → **PCIe Root Complex/Fabric** → Interrupt Controller → CPU | PCIe MSI/MSI-X transaction | **No** |
| **I²C Peripheral Interrupt** | I²C peripheral | Peripheral → Dedicated Interrupt Signal → **GPIO/Interrupt Controller** → CPU | Electrical interrupt signal | **Yes** |
| **SPI Peripheral Interrupt** | SPI peripheral | Peripheral → Dedicated Interrupt Signal → **GPIO/Interrupt Controller** → CPU | Electrical interrupt signal | **Yes** |
| **UART Interrupt** | UART controller | UART Controller → Interrupt Signal → **Interrupt Controller** → CPU | Electrical/on-chip interrupt signal | **Usually** |
| **Timer Interrupt** | Hardware timer | Timer → **Interrupt Controller** → CPU | On-chip interrupt signal | **Logical dedicated path** |
| **DMA Completion Interrupt** | DMA controller | DMA Controller → **Interrupt Controller** → CPU | Interrupt signal/message | **Usually** |
| **Storage Controller Interrupt** | Storage controller | Controller → Interrupt Controller → CPU | Interrupt signal or MSI/MSI-X | **Depends** |
| **Ethernet MAC Interrupt** | Ethernet MAC | MAC → Interrupt Controller → CPU | Interrupt signal or MSI/MSI-X | **Depends** |
| **Coherent Device Interrupt — CXL** | CXL device | CXL Device → CXL Link/Fabric → Host/CXL Root → Interrupt Mechanism → CPU | CXL/PCIe-derived message mechanism | **Usually no** |
| **Virtual Interrupt — VM** | Virtual device / vCPU | Virtual Device → Hypervisor/VMM → Virtual Interrupt Controller → vCPU | Software-mediated virtual interrupt | **No physical path** |
| **Posted Interrupt — Virtualization** | Physical device | Device → PCIe/Interrupt mechanism → IOMMU/Interrupt Remapping → Posted-Interrupt mechanism → vCPU | Hardware interrupt message | **No dedicated wire** |
| **External Interrupt — x86** | External hardware | Device → Interrupt Controller → CPU | Interrupt signal/message | **Depends** |
| **Interrupt via Dedicated SoC Fabric** | SoC peripheral | Peripheral → **Interrupt Router** → **GIC/APIC** → CPU | Dedicated on-chip signaling | **Logical** |
| **Fabric-Mediated Interrupt** | Fabric-attached device | Device → Fabric Endpoint → **Fabric/Switch/Root** → Interrupt Controller → CPU | Fabric message/transaction | **No** |

## References

- [OS Dev Page](http://wiki.osdev.org/Expanded_Main_Page)
- https://en.wikipedia.org/wiki/Input/output
- https://en.wikipedia.org/wiki/Input_device
- https://en.wikipedia.org/wiki/Device_driver
- https://en.wikipedia.org/wiki/Bus_(computing)
- https://en.wikipedia.org/wiki/Network_on_a_chip
- https://en.wikipedia.org/wiki/Harvard_architecture
- https://en.wikipedia.org/wiki/MultiProcessor_Specification
- https://en.wikipedia.org/wiki/Input%E2%80%93output_memory_management_unit
- https://en.wikipedia.org/wiki/Memory-mapped_I/O_and_port-mapped_I/O
- https://en.wikipedia.org/wiki/I2C
- https://en.wikipedia.org/wiki/Root_complex
- [Linux Device Model](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/linux-device-model.md)
- https://en.wikipedia.org/wiki/Interrupt_request
- https://en.wikipedia.org/wiki/Message_Signaled_Interrupts
- https://en.wikipedia.org/wiki/Interrupt_handler