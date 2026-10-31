# Network Packet Abstraction


> **Network packets** are fundamental units of data transmitted over networks. On Linux, the networking stack abstracts packets through different layers, each handling various aspects of packet processing. Below is an overview of how network packets are abstracted on Linux, particularly from a kernel and system programming perspective.
> 

QA:

- Network Package Lifetime
- Network Package Flow
- …

## **Packet Representation in the Kernel**

In the Linux kernel, packets are represented using the `sk_buff` (socket buffer) structure, which encapsulates all the information required for packet processing.

```c
struct sk_buff {
    struct sk_buff *next;      // Next buffer in the queue
    struct sk_buff *prev;      // Previous buffer in the queue
    struct net_device *dev;    // Associated network device
    unsigned int len;          // Total packet length
    unsigned char *head;       // Start of the allocated memory
    unsigned char *data;       // Pointer to actual data
    unsigned char *tail;       // End of data
    unsigned char *end;        // End of allocated buffer
    struct sock *sk;           // Associated socket
};

```

- The `data` pointer refers to the actual payload, while `head` and `end` define the allocated buffer.
- Various helper functions allow kernel modules to manipulate `sk_buff` structures.

## **Packet Abstraction Across Network Layers**

The Linux kernel abstracts packets into layers that correspond to the OSI model. The packet is processed at each layer:

1. **Link Layer (L2) – Ethernet Frame**
    - Packets are received/transmitted as raw Ethernet frames.
    - Ethernet headers (`struct ethhdr`) include MAC addresses and Ethertype.
    - Example: `skb->dev` contains the interface through which the packet arrived.
2. **Network Layer (L3) – IP Packet**
    - After removing the Ethernet header, the packet is treated as an IP datagram.
    - The `struct iphdr` defines the IP header, including source/destination IPs.
    - Routing decisions happen at this layer using `skb->dst`.
3. **Transport Layer (L4) – TCP/UDP Segment**
    - The kernel extracts transport layer headers (`struct tcphdr` / `struct udphdr`).
    - The packet is delivered to the appropriate socket for user-space processing.
4. **Application Layer (L7)**
    - Once a packet reaches the socket buffer, it is accessible to user-space applications via system calls like `recv()` and `send()`.

## **Packet Processing Path**

The Linux kernel processes packets in the following sequence:

### **Incoming Packets (RX Path)**

1. **NIC (Network Interface Card) receives the packet** and places it in a ring buffer.
2. **Interrupt Handler (NAPI)** copies the packet into an `sk_buff` and passes it to the protocol stack.
3. **Netfilter Hooks** (e.g., firewall rules) can inspect, modify, or drop packets.
4. **Routing Subsystem** decides whether the packet is for the local machine or should be forwarded.
5. **Protocol Processing (TCP/IP stack)** extracts headers and hands the payload to sockets.
6. **User-Space Socket Buffer** receives the data for applications.

### **Outgoing Packets (TX Path)**

1. **User-space applications** send data using system calls (`send()`).
2. **Transport Layer (TCP/UDP)** segments the data and attaches headers.
3. **Network Layer (IP routing)** determines the destination.
4. **Link Layer (Ethernet, Wi-Fi, etc.)** encapsulates the packet with MAC headers.
5. **Network Device Driver** sends the packet to the physical network.

## **Kernel APIs for Packet Handling**

### **Raw Sockets (User-Space Packet Access)**

Developers can use raw sockets to capture and inject packets:

```c
int sock = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
recvfrom(sock, buffer, BUFFER_SIZE, 0, (struct sockaddr*)&saddr, &saddr_len);

```

- `AF_PACKET`: Allows direct access to L2 packets.
- `SOCK_RAW`: Provides raw packet access.

### **Netfilter Hooks (Packet Filtering)**

Netfilter allows kernel modules to inspect and modify packets at different processing points.
Example hook:

```c
static unsigned int my_hook_fn(void *priv, struct sk_buff *skb,
                               const struct nf_hook_state *state) {
    struct iphdr *ip_header = ip_hdr(skb);
    printk(KERN_INFO "Packet from: %pI4\n", &ip_header->saddr);
    return NF_ACCEPT; // Accept packet
}

```

### **eBPF (Extended Berkeley Packet Filter)**

eBPF provides high-performance packet filtering and monitoring without modifying kernel code.

## **User-Space Packet Abstraction**

User-space applications can interact with packets using:

1. **PCAP (Packet Capture Library)**: Tools like `tcpdump` and `Wireshark` use `libpcap` for packet inspection.
    
    ```python
    import pyshark
    cap = pyshark.FileCapture('capture.pcap')
    for pkt in cap:
        print(pkt)
    
    ```
    
2. **TUN/TAP Devices**: Virtual network interfaces that allow packet injection and interception.

## References

- https://stackoverflow.com/questions/23937529/understanding-the-process-of-receiving-network-packets
- https://unix.stackexchange.com/questions/688065/how-do-packets-flow-through-the-kernel
- https://dev.to/amrelhusseiny/linux-networking-part-1-kernel-net-stack-180l
- https://wiki.linuxfoundation.org/networking/kernel_flow