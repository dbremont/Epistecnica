---
tags: [network]
---

# Linux Network Stack

- [Berkeley Socket](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/berkeley-socket.md), [Netlink](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/netlink.md), [Linux Process Management Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-process-management-stack.md)

> **Berkeley Sockets** is an **API Standard** for network communication in Unix-like operating systems that provides a standardized interface for creating and managing sockets to facilitate data exchange between devices over a network.
> 

QA:

- How does the Linux kernel manage network interfaces? Describe the role of netdev and rtnetlink
- How do you configure iptables to allow HTTP traffic while blocking all other incoming connections?
- What is firewalld, and how does it differ from iptables?
- What is the purpose of netstat and ss? How do they differ?
- Explain the concept of network namespaces in Linux and provide an example of how to use them.
- Describe how to set up a VPN on a Linux server. What tools and configurations are typically involved?
- What is tc, and how can it be used for traffic control in Linux? Provide an example scenario.
- How do you optimize network performance in a Linux environment? What parameters can be adjusted?
- What is the role of `CNI` (Container Network Interface) in container networking?
- Explain how to use `Open vSwitch` to manage virtual network interfaces.
- What is the purpose of the `Netlink` socket in Linux networking? Provide an example use case.
- How do you configure and troubleshoot a DHCP server on a Linux system?
- What is `BPF` (Berkeley Packet Filter), and how is it used in packet filtering and network monitoring?
- Explain the purpose of the `ip` command in Linux networking. How does it differ from older tools like `ifconfig` and `route`?
- How can you use `nmap` for network scanning and security assessment? Provide an example command.
- How can you optimize the TCP stack for low-latency applications?
- How do you analyze and optimize the network stack's performance in a high-load scenario?
- How do changes in the network configuration (e.g., MTU size, routing changes) impact existing connections?
- How does the Linux kernel handle network buffer management, and what strategies can be employed to minimize packet loss?
- How can I reduce the network bandwidth of outbound connections to a specific domain?

## Kernel Network Subsystems

> 

| **Kernel-Level Subsystem** | **Description** |
| --- | --- |
| **Network Stack** | The core subsystem responsible for managing network protocols, including TCP/IP. |
| **Socket Layer** | Provides the interface for applications to communicate over the network via sockets. |
| **Protocol Layers** | Implementation of network protocols in the kernel: |
|  | - **TCP (Transmission Control Protocol)**: Reliable, connection-oriented communication. |
|  | - **UDP (User Datagram Protocol)**: Connectionless, fast transmission of datagrams. |
|  | - **IP (Internet Protocol)**: Responsible for addressing and routing packets. |
| **Netfilter** | Framework for packet filtering, NAT, and connection tracking. |
| **Routing Subsystem** | Manages routing tables and algorithms for determining the best paths for packet delivery. |
| **ARP (Address Resolution Protocol)** | Resolves IP addresses to MAC addresses, allowing for communication within local networks. |
| **Network Device Drivers** | Interfaces between the kernel and network hardware, enabling communication with network interfaces. |
| **TCP/IP Offloading** | Offloads TCP/IP processing tasks to network hardware to improve performance. |
| **Virtual Networking** | Supports virtual network interfaces and overlays (e.g., bridges, VLANs) for virtualization. |
| **Network Namespaces** | Allows for the creation of isolated network stacks, enabling multiple virtual networks on a single host. |
| **Quality of Service (QoS)** | Mechanisms for managing bandwidth and prioritizing traffic to ensure performance. |
| **Traffic Control (tc)** | Kernel-level tools for shaping and managing network traffic flow. |
| **Wireless Subsystem** | Manages wireless network interfaces and protocols (e.g., Wi-Fi, Bluetooth) at the kernel level. |
| **IPv6 Support** | Provides kernel-level support for the IPv6 protocol, enabling larger address spaces. |
| **Netlink** | …. |

## Network System Calls

> Network system calls in Linux are crucial for managing and interfacing with the network subsystem. They provide the necessary interface for applications to communicate over a network using various protocols.
> 

> Below is a table summarizing key network-related system calls, their purposes, and typical use cases in Linux.
> 

| **System Call** | **Purpose** | **Typical Use Cases** |
| --- | --- | --- |
| `socket()` | Creates a new socket. | Starting a network communication session. |
| `bind()` | Binds a socket to a network address. | Assigning a specific local address to a socket. |
| `listen()` | Prepares the socket to accept incoming connections. | Setting up a socket to accept incoming server connections. |
| `accept()` | Accepts an incoming connection on a socket. | Handling new client connections in a server application. |
| `connect()` | Initiates a connection on a socket to a remote host. | Connecting to a server socket from a client. |
| `send()`, `sendto()`, `sendmsg()` | Sends data on a socket. | Transmitting data over a connection (TCP or UDP). |
| `recv()`, `recvfrom()`, `recvmsg()` | Receives data from a socket. | Receiving data from a connection. |
| `setsockopt()` | Sets options on a socket. | Configuring socket operations (e.g., timeouts, buffering). |
| `getsockopt()` | Retrieves options from a socket. | Getting current socket configurations. |
| `shutdown()` | Shuts down socket send and receive operations. | Disabling further send and/or receive operations. |
| `close()` | Closes a socket. | Releasing the socket descriptor and its resources. |
| `getpeername()` | Retrieves the address of the remote peer connected to a socket. | Obtaining the network address of the connected peer. |
| `getsockname()` | Retrieves the address to which the socket is bound. | Getting the local binding of the socket (IP address and port). |
| `select()`, `poll()`, `epoll()` | Monitors multiple file descriptors to see if I/O is possible on any of them. | Multiplexing input/output over multiple sockets. |

## Linux Network Stack Components

> This table provides a structured overview of the critical elements involved in Linux's network management.
> 

| **Component** | **Data Models/Structures** |
| --- | --- |
| **Socket Layer** | `socket`, `sock`, `proto_ops` |
| **Protocol Layer** | `sk_buff`, `inet_sock` |
| **Interface Layer** | `net_device` |
| **Routing** | `rtable`, `fib_table` |
| **Network Drivers** | Device-specific structures |
| **Netfilter** | `nf_hook_ops` |
| **TCP/IP** | `tcp_sock`, `ip_options`, `icmp_sock` |
| **Queuing** | `Qdisc`, `tc_block` |
| **Security** | `xfrm_policy`, `xfrm_state` |

## Linux Socket Abstraction

> The **Berkeley Socket** is a foundational **API** for network communication originally developed as part of the **Berkeley Software Distribution (BSD)** operating system. This **API** provides a set of function calls that enable applications to send and receive data over a network, supporting various network protocols and data transmission modes. It is widely used across different operating systems, including **Unix**, **Linux**, and **Windows**, due to its versatility and robustness in handling network communications. The **Berkeley Socket API** abstracts the complexities of direct network protocol interaction, offering a simplified interface for developers to create network-aware applications. It supports multiple communication protocols, including **TCP** for connection-oriented streams and **UDP** for connectionless datagrams, among others.
> 

> How to listen in two applications to the same socket? **Linux Kernel Automatic Load Balancing**
> 

## Network Buffer

> **Network Buffers**: Managed by the kernel to handle incoming and outgoing packets. These buffers are structured using `sk_buff` (socket buffer) structures that store packet data and metadata.
> 

## **Traffic Control (tc)**

> Provides tools for managing bandwidth and quality of service (QoS) for network traffic.
> 

## Network Routing Table

> **Routing Table**: Maintains routes to different networks and is used for forwarding packets to their destinations.
> 

## **Networking Subsystems**

- **Network Namespace**: Isolates network resources (like interfaces, routing tables, firewall rules) for different containers or processes, enabling multiple network stacks on the same system.
- **Bridge**: Allows for the creation of virtual network segments by connecting multiple network interfaces.
- **VLAN (Virtual Local Area Network)**: Supports the segmentation of a network into smaller, isolated networks over a shared physical medium.
- **Tun/Tap Devices**: Virtual network devices that provide userspace programs with a way to send and receive packets directly.
- Traffic Control (tc)
- **Netfilter**
- **Network Namespace**
- **Routing Subsystem**
- **MPLS (Multiprotocol Label Switching)**
- **Link Layer (LL) Subsystem**
- Netlink Subsystem
- **TUN/TAP Devices**
- **Bridge Networking**
- **Bonding and Teaming**:

## Linux TCP/IP Protocols

> The TCP/IP stack, also known as the internet protocol suite, defines a set of networking protocols that enable computers to communicate over a network. The stack is divided into four layers, each containing various protocols that serve different functions.
> 

Here’s a table that summarizes the primary protocols within each layer of the **TCP/IP** stack:

| **Layer** | **Protocols** | **Description** |
| --- | --- | --- |
| **Application** | HTTP, HTTPS, FTP, SMTP, POP3, IMAP, SSH, Telnet, SNMP, DNS, SIP, RTP | Protocols that support application-specific services for file transfers, email, web browsing, and other higher-level network processes. |
| **Transport** | TCP, UDP, SCTP, DCCP | Protocols that provide host-to-host communication services for applications including reliable (TCP) and fast (UDP) data delivery. |
| **Internet** | IP (IPv4/IPv6), ICMP, ARP, RARP, OSPF, BGP, IGMP | Core protocols that handle packet forwarding and routing through internetworks, addressing, and diagnostics. |
| **Link** | Ethernet, Wi-Fi, ARP, PPP, MPLS | Protocols that operate on the hardware link (network interfaces, cables, etc.), dealing with the physical aspects of sending and receiving data. |
|  |  |  |

## Linux Kernel Networking Frameworks

> In Linux, the kernel provides several networking frameworks that enable robust network management, traffic control, and security features.
> 

> Below is a table summarizing the key networking frameworks provided by the Linux kernel, including their roles and functionalities:
> 

| **Framework** | **Description** |
| --- | --- |
| **Netfilter** | A powerful framework within the Linux kernel for network packet filtering, NAT, and packet mangling. |
| **nftables** | A newer packet classification framework intended to replace iptables with a more efficient and flexible architecture. |
| **IPTables** | Predecessor to nftables, providing a robust set of tools for packet filtering and NAT. |
| **IPSec** | Framework for implementing IP security protocols in the Linux kernel for encrypting and authenticating IP packets. |
| **Traffic Control (TC)** | Subsystem for controlling network traffic management in Linux, providing various queuing disciplines (qdiscs). |
| **Bridge** | Software used to create and manage ethernet bridges, allowing multiple network interfaces to act as a single segment. |

## Linux Network Tools

> Below is a table that **organizes** and presents various **network tools** available to **network administrators** and **users**, summarizing their primary **functions** and **applications**:
> 

| **Tool** | **Description** |
| --- | --- |
| **Ping** | Tests connectivity between two network devices by sending ICMP echo requests and waiting for responses, useful for diagnosing network reachability. |
| **Traceroute** | Traces the path packets take from a source to a destination across a network, identifying each hop and the time taken to reach it, useful for path analysis. |
| **Wireshark** | A comprehensive network protocol analyzer that captures and displays network traffic in real-time, used for network troubleshooting and analysis. |
| **Nmap** | A network scanner used to discover devices and services on a network, identify open ports, and perform security audits. |
| **Netstat** | Displays network connections, routing tables, interface statistics, masquerade connections, and multicast memberships. |
| **Tcpdump** | A command-line packet analyzer used for capturing and analyzing network traffic, often used for network troubleshooting and packet inspection. |
| **Fping** | Similar to `ping` but can target multiple hosts simultaneously, allowing for bulk status checks of network connectivity. |
| **SNMP Tools** | Tools for managing and monitoring network equipment via the Simple Network Management Protocol, including performance data collection and device configuration. |
| **DNS Tools** | Tools such as `nslookup`, `dig`, and `host` for querying DNS servers to resolve domain names, check DNS records, and diagnose DNS-related issues. |
| **Remote Desktop Tools** | Includes tools like RDP, VNC, and TeamViewer for remotely accessing and managing networked devices, providing capabilities for remote support and server management. |
| **ip** | A versatile tool to manage IP addresses, network interfaces, and routing tables, replacing the older `ifconfig` in many Linux distributions. |
| **ifconfig** | An older tool for configuring and displaying network interface parameters and IP addresses, still used in many systems for network configuration. |
| **route** | Manages the kernel's IP routing tables, used for setting up and modifying network routes to control IP packet forwarding. |
| **dig** | A DNS lookup utility that queries DNS servers directly, useful for troubleshooting DNS problems and inspecting DNS records. |
| **host** | Resolves domain names into IP addresses and vice versa, helping diagnose DNS issues and ensuring correct DNS configurations. |
| **iptables** | Administers Linux kernel packet filtering rules for setting up firewalls, managing inbound and outbound traffic rules, and performing NAT. |
| **ss** | A utility to investigate sockets, it displays information about network connections, listening ports, and is replacing `netstat` in many distributions. |
| **tcpdump** | Captures and analyzes network packets, useful for deep network analysis and troubleshooting. |
| **iPerf** | Measures network bandwidth performance by generating traffic between hosts, commonly used in performance tests. |
| **ssh** | Secure Shell protocol for secure remote login from one computer to another, providing encrypted communications and command execution over insecure networks. |
| **scp** | Secure Copy Protocol tool for securely transferring files between hosts on a network, leveraging SSH for data transfer security. |
| **sftp** | Secure File Transfer Protocol, providing secure file access, transfer, and management over a reliable data stream. |
| **telnet** | An older protocol used for accessing remote computers but considered insecure for transferring sensitive information. |
| fuser |  Display process IDs currently using files or sockets. |

## Linux Network Stack Analysis

> See more in [Performace](note.html?n=technica/computation/system/evaluation/performace.md).
> 

### Network Performance Tool Set

| Tool (Framework) | Description |
| --- | --- |
| `ip` | Modern Linux networking utility used to configure and inspect network interfaces, IP addresses, routes, tunnels, VLANs, and policy routing. |
| `ifconfig` | Legacy network interface configuration tool used to view and modify interface parameters. |
| `ss` | Socket statistics utility that displays active TCP, UDP, UNIX, and raw socket connections. |
| `netstat` | Legacy network statistics tool for viewing connections, routing tables, interface statistics, and listening ports. |
| `ping` | Sends ICMP Echo Request packets to test host reachability and measure network latency. |
| `traceroute` | Discovers the sequence of network hops between a source and destination host. |
| `iperf` | Generates network traffic to measure throughput, bandwidth, jitter, and packet loss. |
| `tcpdump` | Command-line packet analyzer used to capture and inspect network traffic. |
| `Wireshark` | Graphical protocol analyzer used for deep inspection and analysis of captured packets. |
| `dig` | DNS query tool used to retrieve and troubleshoot DNS records and name resolution. |
| `nslookup` | Utility for querying DNS servers and resolving hostnames to IP addresses. |
| `tc` | Traffic Control utility used to implement Quality of Service (QoS), traffic shaping, bandwidth limits, and packet scheduling. |
| `vnStat` | Lightweight network traffic monitor that collects and reports bandwidth usage statistics. |
| `NetworkManager` | Network management service that automates configuration and management of network connections. |
| `netplan` | Declarative network configuration system that generates backend configurations from YAML files. |
| `fail2ban` | Security tool that monitors logs and automatically blocks IP addresses exhibiting suspicious behavior. |
| `iptables` | User-space utility for configuring firewall rules through the Linux Netfilter framework. |
| `nftables` | Modern packet filtering and firewall management framework that supersedes `iptables`. |
| **Netfilter** | Linux kernel framework responsible for packet filtering, network address translation (NAT), connection tracking, and firewall processing. |
| **BPF (Berkeley Packet Filter)** | Kernel-level packet filtering technology that enables efficient packet capture and filtering. |
| **eBPF (Extended Berkeley Packet Filter)** | General-purpose in-kernel execution framework used for networking, observability, tracing, performance analysis, and security. |
| `Scapy` | Python framework for crafting, manipulating, transmitting, and analyzing network packets. |
| `route` | Legacy utility used to display and modify the system routing table. |

## Linux Network Performance Tuning

> To optimize networking performance in the Linux kernel, you can consider the following:
> 
- Adjusting TCP settings (e.g., window size, congestion control algorithms).
- Tuning network buffer sizes (`/proc/sys/net/core/rmem_max`, `/proc/sys/net/core/wmem_max`).
- Utilizing features like offloading (e.g., TCP offload, checksum offload) in network interface cards (NICs).
- Using `tc` to manage traffic shaping and prioritization.

## References

- [Are sockets the wave of the future?](https://groups.google.com/g/comp.protocols.tcp-ip/c/mVnR2OSXHBY/m/tjdkK1OBtCEJ?pli=11) - [STREAMS](https://en.wikipedia.org/wiki/STREAMS)
- [How TCP Sockets Work](https://eklitzke.org/how-tcp-sockets-work)
- [socket](https://man7.org/linux/man-pages/man2/socket.2.html)
- [Beyond socket options: making the Linux TCP stack truly extensible](https://www.info.ucl.ac.be/~tranviet/tcp-ebpf.pdf)
- [The Journey of a Packet Through the Linux Network Stack](https://www.cs.dartmouth.edu/~sergey/netreads/path-of-packet/Lab9_modified.pdf)
- [Linux Kernel Tutorial Networking](https://linux-kernel-labs.github.io/refs/heads/master/labs/networking.html)
- [Addition of a new network protocol in the linux kernel](https://stackoverflow.com/questions/13760017/addition-of-a-new-network-protocol-in-the-linux-kernel)
- [Add a new protocol to Linux Kernel](https://linuxwarrior.wordpress.com/2008/12/02/add-a-new-protocol-to-linux-kernel/)
- [Linux Networking Part 1 : Kernel Net Stack](https://amrelhusseiny.github.io/blog/004_linux_0001_understanding_linux_networking/004_linux_0001_understanding_linux_networking_part_1/)
- [Linux Network Stack](https://www.cs.dartmouth.edu/~sergey/netreads/path-of-packet/Lab9_modified.pdf)
- [Networking Protocols](https://lwn.net/Kernel/Index/#Networking-Protocols)
- [Review: Understanding Linux Network Internals](https://lwn.net/Articles/168894/)
- [jserv / nstack](https://github.com/jserv/nstack)
- [Userspace TCP/IP stack for Linux](https://github.com/jserv/nstack)
- [linux-network-performance-parameters](https://github.com/leandromoreira/linux-network-performance-parameters)
- [Use io_uring for network I/O (redhat.com)](https://news.ycombinator.com/item?id=35547316)
- RTL8139 Driver https://wiki.osdev.org/RTL8139
- lwIP - A Lightweight TCP/IP stack https://savannah.nongnu.org/projects/lwip/
- On writing a network stack (1/2) https://williamdurand.fr/2022/02/17/on-writing-a-network-stack-part-1/
- On writing a network stack (2/2) https://williamdurand.fr/2022/04/11/on-writing-a-network-stack-part-2/
- Add a new protocol to Linux Kernel https://linuxwarrior.wordpress.com/2008/12/02/add-a-new-protocol-to-linux-kernel/
- Linux System Calls https://thevivekpandey.github.io/posts/2017-09-25-linux-system-calls.html
- [Monitoring Linux Network Stack](http://arthurchiao.art/blog/monitoring-network-stack/)
- [OVS](http://arthurchiao.art/blog/ovs-deep-dive-0-overview/) / [https://en.wikipedia.org/wiki/Open_vSwitch](https://en.wikipedia.org/wiki/Open_vSwitch)
- [‣](https://app.notion.com/p/1a4d38c7497c80db82cbf8a1b2f67a34?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081cfbf92f8e556b7dff4?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081ab84e9e9dc4dccbb00?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081939958c6eccaee1767?pvs=21)
- [‣](https://app.notion.com/p/10e598edb790814f8b5decec0b50a811?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081f0a73fc8e2de28944f?pvs=21)
- [‣](https://app.notion.com/p/10e598edb790817c98a9fe7b1c8f25a3?pvs=21)
- [‣](https://app.notion.com/p/10e598edb7908175a061dcc88330f698?pvs=21)
- TCP/IP Illustrated The Implementation Volume 2 Understanding Linux Network Internals
- [HTTP](note.html?n=technica/computation/telecom/http.md)
- https://zenodo.org/records/14179366
- Jain, M., & Dovrolis, C. (2002). End-to-end available bandwidth: Measurement methodology, dynamics, and relation with TCP throughput. 32(4), 295–308.
- Nagle, J. (1984). Congestion control in IP/TCP internetworks. 14(4), 11–17.
- Padhye, J., Firoiu, V., Towsley, D., & Kurose, J. (1998). Modeling TCP throughput: A simple model and its empirical validation. 303–314.
- [Measurement, Measurement, Modeling Modeling and Analysis Analysis of the Internet](https://pages.cs.wisc.edu/~pb/ima_tutorial.pdf)
- [Linux Network Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-network-stack.md)
- [Berkeley Socket](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/berkeley-socket.md)
- [Telecom](note.html?n=technica/computation/telecom.md)
- https://github.com/kbandla/dpkt
- https://man7.org/linux/man-pages/man8/tc.8.html
- https://friskfrysefrugt.github.io/awesome-networking/
- https://linux.die.net/man/1/socat