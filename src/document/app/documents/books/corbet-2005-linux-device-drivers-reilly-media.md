# Corbet, J., Rubini, A., & Kroah-Hartman, G. (2005). Linux device drivers. O’Reilly Media, Inc.


```bash
@book{corbet2005linux,
  title={Linux device drivers},
  author={Corbet, Jonathan and Rubini, Alessandro and Kroah-Hartman, Greg},
  year={2005},
  publisher={O'Reilly Media, Inc.}
}
```

## Notes

---

> The **Linux kernel** remains a large and complex body of code, however, and would-be kernel hackers need an entry point where they can approach the code without being overwhelmed by complexity. Often, device drivers provide that gateway.
> 

> They are distinct **“black boxes”** that make a particular piece of hardware respond to a well-defined internal programming interface; they hide completely the details of how the device works.
> 

> A **driver** serves as both a **model** and an **abstraction** that represents a **specific hardware** or software system, managing interactions between that system and the rest of the operating system.
> 

> **Driver**: $D_m → D$.  It creates a device model;
> 

> **Design Ethos**: Mechanism, not policy. **Write Kernel Code** to access the hardware, but don’t force particular policies on the user, since different users have different needs.
> 

> **Driver**: A **Software Layer** that lies between the applications and the **actual device**.
> 

> **Design Technique**: Modularity or decomposition.
> 

> **Linux Naming** Schemes, objects ? … File descriptors …
> 

> **Security is a policy issue**; it should be handled by the drivers.
> 

> **Firmware**: …
> 

![image.png](documents/books/corbet-2005-linux-device-drivers-reilly-media/image.png)

QA:

- How a driver **handle concurrent** used of a **device**?
- Which **abstraction** of a device does the **driver provide**?
- What is the hardware you are driving?
    - What kind of device is it (e.g., USB, PCI, GPIO, etc.)?
    - What protocols does the device use to communicate (e.g., I2C, SPI, HID, etc.)?
    - Does the hardware have any special features, limitations, or quirks that need to be accounted for?
- **Initialization**: How does the driver detect the hardware? What kernel functions are involved in detecting and registering the device?
- **Communication Model**: …
- **Buffers and Queues**: Does the driver use circular buffers, DMA (Direct Memory Access), or other **memory management** techniques?
- **Resource Management**: How does the driver manage hardware resources (e.g., memory, I/O ports, interrupts)?
- How does the driver expose functionality to user-space?
- What happens when the device is initialized and destroyed?
- How does the driver interact with the Linux kernel subsystems?
- Synchronous   Processing
- Asynchronous Processing
- Which types of modules does the kernel supports?
- How to interpret the results of **`ifconfig`**?
- What is a network connection?
- What is a connection?
- How to list the file system types that a given Linux distro supports?
- …

## Index

## An Introduction to Device Drivers

> **Some drivers** come with a set of tools that provide **additional capabilities** not integrated within the driver itself.
> 

> A **driver** serves as both a **model** and an **abstraction** that represents a **specific hardware** or software system, managing interactions between that system and the rest of the operating system.
> 

> **Driver**: $D_m → D$.
> 

> **Design Ethos**: Mechanism, not policy (behavior). **Write Kernel Code** to access the hardware, but don’t force particular policies on the user, since different users have different needs.
> 

> **Driver**: A **Software Layer** that lies between the applications and the **actual device**.
> 

> Hardware Resource: …
> 

> Resource: …
> 

> A **filesystem type** determines how information is organized on a block device in order to represent a tree of directories and files.
> 

> A **file system** is not a hardware driver;  it’s a software mechanism that provides file abstractions. It’s a second order driver.  [File System → Disk Driver → Disk].
> 

> It’s quite unusual for a **programmer** to actually need to write a **file system module**,
because the official kernel already includes code for the most important **file system
types**.
> 

File System Drivers:

- AHCI  File System Driver !!!
- **AHCI** (for SATA drives)
- **NVMe** (for NVMe SSDs)
- **SCSI** (for certain high-performance drives)

**Network Interface** (Hardware / Software):

- `ip link show`
- `ifconfig -a`
- `ls /sys/class/net/`
- `sudo lshw -C network`
- `nmcli device`
- `sudo ethtool -i enp2s0`
- …

Kernel:

- Process Management:  The kernel is in charge of creating and destroying processes and handling their connection to the outside world (input and output).
- Memory Management: The computer’s memory is a major resource, and the policy used to deal with it is a critical one for system performance
- File systems:  Unix is heavily based on the file system concept; almost everything in Unix can
be treated as a file.
- Device control (aka driver): Almost every system operation eventually maps to a physical device. With the
exception to the processor, memory, and a very few other entities, any and all device control operations are performed by code that is specific to the device being addressed.
- Networking: Networking must be managed by the operating system, because most network
operations are not specific to a process: incoming packets are asynchronous events.

Module System (aka Plugin System):

> Mechanisms to extend the Linux Kernel at run time.
> 

Device Models:

> The Linux way of looking at devices distinguishes three fundamental device types. **Char** devices, b**lock** device, or a **network** device.
> 

> Others ways to classify drivers  USB, SCSI, Serial Modules, …
> 

> The network devices is the only not stream oriented device; hard to **map to the file system**.
> 
- **Character devices**:  A character (**char**) device is one that can be accessed as a stream of **bytes** (like a file); a char driver is in charge of implementing this behavior. Such a driver usually implements at least the open, close, read, and write system calls. The text console (`/dev/console`) and the serial ports (`/dev/ttyS0` and friends) are examples of char devices, as they are well represented by the stream abstraction.
- **Block devices**: Like char devices, block devices are accessed by **file system** nodes in the `/dev` directory. They share the fundamental abstraction with **`char devices`.** A block device is a device (e.g., a disk) that can host a file system.
- **Network interfaces**:  Any network transaction is made through an interface, that is, a device that is able to exchange data with other hosts. Usually, an **interface is a hardware**
device, but it might also be a pure software device, like the **loop back** interface.
- …

**Security Considerations:**

- …

**Versioning Numbers:**

- …

## Building and Running Modules

> …
> 

## Char Devices

> …
> 

## Debugging Techniques

> …
> 

## Concurrency and Race Conditions

> …
> 

## Advanced Char Driver Operations

> …
> 

## Time, Delays, and Deferred Work

> …
> 

## Allocation Memory

> …
> 

## Communication with Hardware

> …
> 

## Interrupt Handling

> …
> 

## Data Types in the Kernel

> …
> 

## PCI Drivers

> …
> 

## USB Drivers

> …
> 

## The Linux Device Model

> …
> 

## Memory Mapping and DMA

> …
> 

## Block Drivers

> …
> 

## Network Drivers

> …
> 

## TTY Drivers

> …
> 

## References

- https://en.wikipedia.org/wiki/Device_driver
- https://www.oreilly.com/openbook/linuxdrive3/book/
- https://english.stackexchange.com/questions/56183/origin-of-the-term-driver-in-computer-science
- https://github.com/torvalds/linux/blob/master/include/linux/ata.h
