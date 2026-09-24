# Benvenuti, C. (2005). Understanding Linux Network Internals: Guided Tour to Networking on Linux. O’Reilly Media, Inc.


```jsx
@book{benvenuti2005understanding,
  title={Understanding Linux Network Internals: Guided Tour to Networking on Linux},
  author={Benvenuti, Christian},
  year={2005},
  publisher={O'Reilly Media, Inc.}
}
```

## Notes

---

## Index

## General Background

### Introduction

> This chapter introduces -  a some guidance on how to interact with the codebase - the underlying systems - (via user space tooling).
> 

Terminology:

- Octets: …
- The term *Vector* will be used interchangeably with *Array*.
- TCP/IP Layers  will be refer by
    - **L1** – Physical Layer
    - **L2** – Data Link Layer
    - **L3** – Network Layer
    - **L4** – Transport Layer
    - **L5** – Application Layer
- BH: Bottom Half
- IRQ: Interrupt
- RX: Reception
- TX: Transmission
- ….

Network Code Observation:

- Fair Used of Resources.
- Network code is typically distributed rather than standalone, spanning the kernel, files, modules, and related system components.
- Memory Caches: The kernel uses kmalloc and kfree to allocate and free memory block, respectively.
- **Caching and Hash Tables:** Caches are often implemented using hash tables. It is important to consider the growth and shrink dynamics of the implementation.
- **Reference Counts**:  Manual Garbage Collection Accounting; xxx_hold, xxx_release on elements.
- **Garbage Collection**: How they use the references accounting - to clean unused elements.
- Function Pointers and Virtual Function Tables (VFTs)

### Critical Data Structures

### User-Space-to-Kernel Interface

## System Initialization

### Notification Chains

### Network Device Initialization

### The PCI Layer and Network Interface Cards

### Kernel Infraestructure for Component Initialization

### Device Registration and Initialization

## Transmission and Reception

### Interrupts and Network Drivers

### Frame Reception

### Frame Transmission

### General and Reference Material About Interrupts

### Protocol Handlers

## Bridging

### Bridging: Concepts

### Bridging: The Spanning Tree Protocol

### Bridging: Linux Implementation

### Bridging: Miscellaneous Topics

## Internet Protocol Version 4 (IPV4)

### Concepts

### Linux Foundations and Features

### Forwarding and Local Delivery

### Transmission

### Handling Fragmentation

### Miscellaneous Topics

### Layer Four Protocol and Raw IP Handling

### Internet Control Message Protocol (ICMPv4)

## Neighboring Subsystem

### Concepts

### Infrastructure

### Address Resolution Protocol

### Miscellaneous Topics

## Routing

### Concepts

### Advanced

### Linux Implementation

### The Routing Cache

### Routing Tables

### Lookups

### Miscellaneous Topics
