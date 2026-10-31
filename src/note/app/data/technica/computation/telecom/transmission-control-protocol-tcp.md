---
tags: [computer-network, protocol]
---

# Transmission Control Protocol (TCP)

- [HTTP](note.html?n=technica/computation/telecom/http.md)

> **Transmission Control Protocol (TCP)** is a core protocol of the Internet protocol suite that provides reliable, ordered, and error-checked delivery of a stream of bytes between applications running on hosts communicating via an IP network.
> 

> TCP is a stateful, reliable, stream-oriented transport protocol that uses sequence numbering, acknowledgments, timers, windowing, and congestion control to provide robust communication over inherently unreliable IP networks.
> 

> TCP is stateful, maintaining **per-connection state** in the form of **Transmission Control Blocks (TCBs)**, which store all relevant connection parameters (e.g., sequence numbers, window sizes, timers).
> 

![image.png](../assets/note/technica/computation/telecom/transmission-control-protocol-tcp/image.png)

QA:

- What happens to a **TCP** connection if a process is abruptly shut down, let's say with `kill -9`?
- How to monitor all data flowing thought a TCP Socket?

### Technical Definition:

> TCP is a **connection-oriented**, **byte-stream**, **full-duplex**, **transport-layer protocol** defined in [RFC 793](https://datatracker.ietf.org/doc/html/rfc793) and updated by multiple subsequent RFCs. It operates atop the Internet Protocol (IP) and establishes a **virtual circuit** using a **three-way handshake** mechanism for connection establishment, involving the SYN, SYN-ACK, and ACK segments.
> 

TCP provides:

1. **Reliable Data Transfer**
    
    Data is segmented into TCP segments, each encapsulated with a header containing sequence and acknowledgment numbers. TCP ensures in-order delivery via:
    
    - **Sequence numbers** for each byte.
    - **Acknowledgment numbers** confirming receipt.
    - **Retransmission** of lost segments via timeout or duplicate ACKs (e.g., Fast Retransmit).
    - **Checksums** for error detection over the segment.
2. **Flow Control**
    
    Implemented using a **sliding window protocol**, where the receiver advertises a window size (in bytes) indicating how much data it can buffer. This prevents the sender from overwhelming the receiver.
    
3. **Congestion Control**
    
    TCP dynamically adjusts its sending rate based on perceived network congestion using algorithms such as:
    
    - **Slow Start**
    - **Congestion Avoidance**
    - **Fast Retransmit**
    - **Fast Recovery**
        
        These are standardized in algorithms like **TCP Reno**, **TCP NewReno**, and **CUBIC**.
        
4. **Multiplexing and Demultiplexing**
    
    TCP uses **16-bit port numbers** to allow multiple connections between endpoints. A TCP connection is uniquely identified by a 4-tuple: *(source IP, source port, destination IP, destination port)*.
    
5. **Header Structure**
    
    TCP segments have a minimum 20-byte header containing fields such as:
    
    - Source and destination ports
    - Sequence number
    - Acknowledgment number
    - Data offset
    - Flags (e.g., SYN, ACK, FIN, RST)
    - Window size
    - Checksum
    - Urgent pointer
    - Optional fields (e.g., SACK, timestamp)

## Analysis

- [ ]  https://github.com/dachad/tcpgoon
- [ ]  netstat / ss
- [ ]  lsof
- [ ]  tcpdump
- [ ]  strace
- [ ]  nethogs / iftop / bmon
- [ ]  conntrack
- [ ]  tcpflow
- [ ]  iperf3
- [ ]  hping3
- [ ]  socat
- [ ]  /proc/net/tcp
- [ ]  socket, psutil, scapy, pyshark, asyncio
- [ ]  https://sandbox.ws/en/tcp-client

## References

- [Transmission Control Protocol](https://www.ietf.org/rfc/rfc793.txt)
- [TCP Flow Control](https://www.brianstorti.com/tcp-flow-control/)
- [TCP congestion control](https://en.wikipedia.org/wiki/TCP_congestion_control)
- [Sending variable sized packets over the network using TCP/IP](https://stackoverflow.com/questions/40415864/sending-variable-sized-packets-over-the-network-using-tcp-ip)
- Alizadeh, M., Greenberg, A., Maltz, D. A., Padhye, J., Patel, P., Prabhakar, B., Sengupta, S., & Sridharan, M. (2010). Data Center TCP (DCTCP). 63–74.
- TCP/IP Connection Primer https://levelup.gitconnected.com/linux-kernel-tuning-for-high-performance-networking-5999a13b3fb4
- When can two TCP sockets share a local address? (cloudflare.com) https://news.ycombinator.com/item?id=35231276
- Keepalive https://www.wikiwand.com/en/Keepalive
- [A TCP port redirector for UNIX](https://github.com/troglobit/redir)
- [The physical layer puts bits and bytes on the wire - between two nodes. The data link layer frames them and directs the frames to the local destination](https://networkengineering.stackexchange.com/questions/76219/why-in-the-tcp-ip-model-the-link-physical-are-one)
- [Deep-Dive into TCP Connection Establishment Process](https://medium.com/@wrong.about/deep-dive-into-tcp-connection-establishment-process-f6cfb7b4e8e1)
- [Multipath TCP](https://en.wikipedia.org/wiki/Multipath_TCP)
- https://enhancedformysql.github.io/animation/handshake.html
- https://www.saminiir.com/lets-code-tcp-ip-stack-1-ethernet-arp/
- https://news.ycombinator.com/item?id=10654285
- https://doingfedtime.com/new-interactive-tcp-handshake-visualization-tool-free/