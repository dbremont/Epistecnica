---
tags: [virtualization]
---

# Linux Virtualization Stack


> **KVM (Kernel-based Virtual Machine)**: A virtualization module in the Linux kernel that allows the kernel to function as a hypervisor, enabling the creation of virtual machines (VMs) with full hardware virtualization.
> 

> **LXC (Linux Containers)**: A userspace interface for the Linux kernel containment features that allows the creation and management of lightweight, isolated Linux containers.
> 

## Kernel Support

> Which elements does the Linux kernel provide for virtualization?
> 

| Kernel Element | Purpose | Used For |
| --- | --- | --- |
| **KVM (Kernel-based Virtual Machine)** | Turns Linux into a hypervisor by exposing CPU virtualization extensions (Intel VT-x, AMD-V). | Full virtualization (Virtual Machines) |
| **Namespaces** | Isolate system resources such as processes, network, mount points, IPC, users, and hostnames. | Containers |
| **Control Groups (cgroups)** | Limit and account for CPU, memory, I/O, and other resources. | Containers, resource management |
| **seccomp** | Restricts the system calls a process may invoke. | Container sandboxing |
| **Linux Security Modules (SELinux, AppArmor, Smack)** | Mandatory access control for isolation between workloads. | Containers, VMs |
| **Virtual Network Devices (veth, TAP, TUN, bridges)** | Provide virtual networking infrastructure. | VMs and containers |
| **Overlay Filesystems (OverlayFS)** | Layered filesystems used for efficient container images. | Containers |
| **VFIO** | Safe device passthrough to virtual machines. | PCI/GPU passthrough |
| **virtio** | Standardized paravirtualized devices for guests. | High-performance VM I/O |
| **KSM (Kernel Samepage Merging)** | Deduplicates identical memory pages across VMs. | Memory optimization |
| **hugetlb / Huge Pages** | Large memory pages for improved virtualization performance. | High-performance VMs |
| **Memory Balloon Driver** | Dynamically adjusts guest memory allocation. | VM memory management |

## **Virtualization Management Tool**

- **Libvirt**: A toolkit, API, and management layer for virtualization technologies, providing a consistent interface for managing VMs and containers across different hypervisors (e.g., KVM, QEMU, LXC).
- **QEMU**: An open-source emulator and virtualization software that, when combined with KVM, allows for the emulation of hardware for virtual machines.

## **Networking and Storage**

- **Virtual Networking**: The stack includes virtual network interfaces (vNICs), bridges, and overlays to enable communication between containers and VMs while isolating their traffic.
- **Storage Solutions**: Technologies like Ceph, GlusterFS, and others provide distributed storage options for containers and VMs, ensuring data persistence and availability.

## References

- https://en.wikipedia.org/wiki/Cgroups
- https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine
- https://docs.kernel.org/virt/index.html