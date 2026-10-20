# Linux Device Model


> A **device model** is a formal abstraction layer within an operating system that defines the structured representation, classification, interaction semantics, lifecycle, and access mechanisms of physical or virtual hardware devices, enabling the kernel and user-space components to uniformly manage device discovery, driver binding, state management, resource control, and I/O operations independently of specific hardware implementations.
> 

> The "Linux Driver Model" is a framework within the Linux kernel that provides standardized interfaces and mechanisms for hardware interaction, device management, and power management, facilitating the development, integration, and runtime control of device drivers.
> 

Organizing Themes:

- CPU → Node → Communication Path
- Communication Mode Set → Memory Map IO, …
- Device Discovery and Mapping - Which are the node discovery mechanisms?

```bash
Node Discovery
│
├── Description
│   ├── ACPI
│   └── Device Tree
│
├── Enumeration
│   ├── PCI/PCIe configuration-space enumeration
│   ├── USB hub enumeration
│   └── SCSI/NVMe discovery
│
├── Probing
│   └── I²C address probing
│
├── Event-driven discovery
│   └── Hot-plug / topology-change events
│
└── Recursive traversal
    └── Follow buses → bridges → switches → endpoints
```

QA:

- How to list the Hardware Ports?
- How to list the map from memory to peripherals?
- How to interact with the devices without the drivers?
- How to see the **IRQ** being send by the mouse? `/proc/interrupts`

## Summary

| **Property** | **Description** |
| --- | --- |
| **Abstraction Interface** | Defines a standard interface (e.g., function tables, virtual file nodes, device objects) that decouples the OS logic from hardware-specific details. |
| **Device Typing & Hierarchy** | Categorizes devices (e.g., character, block, network, GPU) and supports hierarchical or graph-based relationships (e.g., parent bus → child device). |
| **Identification & Naming** | Associates unique identifiers (e.g., device IDs, paths like `/dev/sda`, symlinks, UUIDs) with device instances for referencing and lookup. |
| **Driver Binding** | Specifies rules for associating driver modules to device instances based on descriptors (e.g., vendor/device ID, class code, device tree node). |
| **Lifecycle Management** | Models initialization, operational, suspend/resume, and teardown phases, including hotplug events and error recovery. |
| **Access Semantics** | Defines concurrency-safe mechanisms for access (e.g., open/read/write/ioctl, memory mapping, command queues), typically exposed via syscalls. |
| **Resource Representation** | Associates memory regions, IRQs, DMA channels, or other platform resources with devices using a kernel-internal representation. |
| **User-Kernel Mediation** | Establishes permission, capability, or policy frameworks to safely expose devices to user space, respecting isolation and protection boundaries. |

## Linux Peripherals I/O Models

> In Linux, there are several models by which the kernel can communicate with peripheral devices, each suited for different types of hardware and performance requirements.
> 

| Communication Model | Description | Enabling Hardware Components |
| --- | --- | --- |
| **Programmed I/O (PIO)** | CPU reads/writes device registers or ports directly using special I/O instructions (e.g., IN/OUT on x86) in a separate address space. | CPU, Device I/O ports or registers |
| **Memory-Mapped I/O (MMIO)** | Device exposes registers or buffers mapped in system memory | CPU memory controller, PCIe BAR (Base Address Registers), device MMIO region |
| **Direct Memory Access (DMA)** | Device reads/writes system RAM directly without CPU | Device DMA engine, PCIe bus mastering, system memory controller |
| **Interrupt-driven I/O** | Device signals CPU asynchronously via interrupts | Interrupt controller (APIC), device interrupt lines or MSI capability |
| **Polling** | CPU continuously checks device status registers | CPU, device status registers |
| **Command Queue / Ring Buffer** | CPU submits commands asynchronously via shared buffers | Shared memory buffers, CPU and device memory management units |
| **Message Signaled Interrupts (MSI)** | Device sends interrupts as in-band PCIe messages | PCIe controller, device MSI capability, CPU interrupt controller |
| **Shared Memory / Buffer Sharing** | Host and device share memory buffers for zero-copy data exchange | System memory, PCIe bus, memory mapping hardware in device and CPU |

## References

- [Port-Mapped I/O (PMIO)](https://en.wikipedia.org/wiki/Memory-mapped_I/O_and_port-mapped_I/O)
- [Memory-Mapped I/O (MMIO)](https://en.wikipedia.org/wiki/Memory-mapped_I/O_and_port-mapped_I/O)
- [Direct Memory Access (DMA)](https://en.wikipedia.org/wiki/Direct_memory_access)
- https://linux-kernel-labs.github.io/refs/heads/master/labs/device_model.html
- https://docs.kernel.org/driver-api/driver-model/overview.html
- https://lwn.net/Articles/645810/
- https://linux-kernel-labs.github.io/refs/heads/master/labs/device_model.html
- [Bus](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/bus.md)
- [**Interconnect**](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/interconnect.md)
- [(Hardware) Physical Substrate](note.html?n=technica/computation/platform/hardware-physical-substrate.md)