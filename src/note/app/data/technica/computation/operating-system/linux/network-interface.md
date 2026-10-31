---
tags: [network]
---

# Network  Interface


> The term **"network interface"** exhibits **polysemy** (multiple meanings) depending on the context in which it is used. See [‣](https://app.notion.com/p/1a1598edb7908059aa60cd275f9f2498?pvs=21).
> 

## **Physical Network Interfaces**

- **Ethernet Interface (`eth0`, `eth1`, etc.)** – Wired network interfaces using Ethernet cables.
- **Wi-Fi Interface (`wlan0`, etc.)** – Wireless network interfaces for connecting via Wi-Fi.
- **Fiber Optic Interface** – High-speed physical interfaces using fiber optics (e.g., SFP, SFP+ modules).

## **Virtual Network Interfaces (VNI)**

- **Loopback Interface (`lo`)** – A virtual interface for internal communication within the same device.
- **Bridge Interface (`br0`, etc.)** – Used to connect multiple network interfaces at Layer 2.
- **VLAN Interface (`eth0.10`, etc.)** – Represents a Virtual LAN (VLAN) over a physical interface.
- **Tunnel Interface (`tun0`, `tap0`)** – Used for VPNs and encapsulated network communication.
- **veth (Virtual Ethernet Pair)** – Paired interfaces used for container networking (e.g., Docker, LXC).

## **Software-Defined & Cloud Network Interfaces**

- **SDN Interfaces** – Software-defined networking (e.g., Open vSwitch, Cisco ACI).
- **Cloud Virtual Interfaces** – Cloud-based network interfaces (e.g., AWS Elastic Network Interface, Azure VNIC).

## References

- https://en.wikipedia.org/wiki/Network_interface