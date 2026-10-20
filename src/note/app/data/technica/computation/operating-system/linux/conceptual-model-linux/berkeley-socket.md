---
tags: [network]
---

# Berkeley Socket

- [Linux Network Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-network-stack.md)

> **Berkeley Sockets** is an **API Standard** for network communication in Unix-like operating systems that provides a standardized interface for creating and managing sockets to facilitate data exchange between devices over a network.
> 

> The **socket abstraction** is a low-level programming interface for network communication, providing a uniform API for inter-process communication (IPC) over various transport protocols (e.g., TCP, UDP, raw IP). It originated in the 4.2BSD UNIX operating system as part of the Berkeley Sockets API and has since become a standard in systems programming.
> 

> **Note:** Truly understanding this requires reasoning about the **`lifecycle`** of the sockets.
> 

## QA

- What makes a socket a **`server socket`**?
- What makes a socket a **`client socket`**?
- After a server calls accept() on a listening socket and obtains a **connected socket** (client_fd), what are the local and remote socket address and port bindings of **client_fd**, and how do they relate to the original listening socket and the client's connect() call? [After a server calls accept() on a listening socket and obtains a connected socket (client_fd), what are the local and remote socket address and port bindings of client_fd, and how do they relate to the original listening socket and the client's connect() call?](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/berkeley-socket.md)
- What are the implications for a server when a single client opens a large number of TCP connections to the server’s listening port and never closes them? [What are the implications for a server when a single client opens a large number of TCP connections to the server’s listening port and never closes them?](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/berkeley-socket.md)
- What Happens When Server Closes a Connected Socket? [What Happens When Server Closes a Connected Socket?](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/berkeley-socket.md)
- What is the TCP connection state progression and resource impact on the server when it closes a connected socket but the client does not close its corresponding socket? [What is the TCP connection state progression and resource impact on the server when it closes a connected socket but the client does not close its corresponding socket?](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/berkeley-socket.md)

## 🔧 Core Abstraction

> At its core, a **socket** is an abstraction over a file descriptor (`int fd`) that represents an endpoint for communication. It supports I/O operations (`read`, `write`, `poll`, `select`, `epoll`) analogous to regular file descriptors, but with semantics defined by underlying transport-layer protocols.
> 

### 🧱 Socket Structure (Kernel-Level)

In Linux, the socket API interfaces with the **VFS (Virtual File System)** layer, and the socket file descriptor maps to a `struct socket`, which contains:

```c
struct socket {
    socket_state        state;
    struct proto_ops    *ops;       // protocol-specific operations
    struct file         *file;
    struct sock         *sk;        // transport-layer socket
    short               type;       // SOCK_STREAM, SOCK_DGRAM, etc.
    unsigned long       flags;
};

```

- `struct proto_ops`: Method table for protocol-specific operations (`connect`, `accept`, `sendmsg`, `recvmsg`, etc.).
- `struct sock`: Represents the protocol-level control block (TCP state, queues, timers, etc.).
    
    ### 🧰Socket API
    
    ```c
    // 🧱 Socket Creation
    int socket(int domain, int type, int protocol); // Create a socket
    
    // 🪝 Server-Side (Passive Socket)
    
    // 📌 Bind to an address/port
    int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
    
    // 🧏 Start listening for incoming connections
    int listen(int sockfd, int backlog);
    
    // 🤝 Accept an incoming connection (returns a new connected socket)
    int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
    
    // 📡 Client-Side (Active Socket)
    
    // 🔗 Connect to a remote server
    int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
    
    // 📨 Data Transfer (Both Sides)
    
    // 📥 Receive data from the socket
    ssize_t recv(int sockfd, void *buf, size_t len, int flags);
    
    // 📤 Send data over the socket
    ssize_t send(int sockfd, const void *buf, size_t len, int flags);
    
    // 🔌 Socket Shutdown and Info
    
    // 🚪 Close the socket
    int close(int sockfd);
    
    // 🔇 Shutdown part of the connection (read, write, or both)
    int shutdown(int sockfd, int how);  // how = SHUT_RD, SHUT_WR, SHUT_RDWR
    
    // 🕵️ Get local address of a socket
    int getsockname(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
    
    // 🕸️ Get peer (remote) address of a socket
    int getpeername(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
    
    // 🛠️ Socket Options
    
    // ⚙️ Set socket options (e.g., timeouts, reuseaddr)
    int setsockopt(int sockfd, int level, int optname, const void *optval, socklen_t optlen);
    
    // 🔍 Get socket options
    int getsockopt(int sockfd, int level, int optname, void *optval, socklen_t *optlen);
    
    ```
    

### 🧰 Advanced Features

- **Non-blocking I/O**: Use `fcntl(sockfd, F_SETFL, O_NONBLOCK)`
- **I/O Multiplexing**: `select`, `poll`, `epoll`, `kqueue`
- **Zero-copy**: `sendfile`, `splice` for minimizing context switches and data copies
- **Ancillary Data**: `recvmsg` with control messages (e.g., for file descriptor passing in Unix domain sockets)
- **Socket Options**: `setsockopt`, `getsockopt` for tuning behavior (`SO_REUSEADDR`, `TCP_NODELAY`, etc.)

### 🔒 Sockets and Concurrency

- Multithreaded servers can share a socket file descriptor using `fork` or threads.
- Synchronization handled in-kernel using spinlocks and reference counters (`sk_refcnt`).
- Lockless mechanisms exist in the fast path (e.g., `tcp_recvmsg` uses lockless queues).

### 🧠 Conceptual Layers

1. **Application Layer**: Programmer uses socket API via libc or similar bindings.
2. **System Call Layer**: System calls trap into the kernel (e.g., `sys_socket`, `sys_connect`).
3. **Socket Layer** (net/socket.c): Translates calls to protocol-specific handlers.
4. **Transport Layer** (`tcp.c`, `udp.c`): Implements TCP state machine, congestion control, etc.
5. **Network Layer**: Routes packets, handles IP fragmentation, etc.
6. **Driver Layer**: Enqueues packets for the NIC (Network Interface Controller).

### 🧭 Socket Role Flow

Server (Passive)

```c
socket()   🧱
   ↓
bind()     📌
   ↓
listen()   🧏
   ↓
accept()   🤝 → returns a new connected socket
   ↓
recv()/send()  📨

```

Client (Active)

```c
socket()   🧱
   ↓
connect()  🔗
   ↓
send()/recv()  📨

```

## List of Communication Domains

> A communication domain determines the protocol family that a socket can use. These domains define the protocols available for communication, and each family supports different features, addressing schemes, or scopes.
> 

> Below is a table summarizing common communication domains in Berkeley sockets, along with their descriptions and typical uses.
> 

| **Domain** | **Description** | **Typical Use Cases** |
| --- | --- | --- |
| **AF_INET** | Address family for IPv4. Supports 32-bit IP addresses. | Most internet applications need IP networking. |
| **AF_INET6** | Address family for IPv6. Supports 128-bit IP addresses. | Applications designed to support modern IPv6 networking. |
| **AF_UNIX**, **AF_LOCAL** | Used for local communication between processes on the same system. Uses a file path as its address. | Inter-process communication (IPC) on the same machine. |
| **AF_PACKET** | This is a low-level interface directly to network devices. It allows sending and receiving at the device driver (link) level. | Applications that need to implement custom protocols and network analysis tools. |
| **AF_NETLINK** | Used for communication between the kernel and user-space processes. | Kernel configuration and monitoring, primarily on Linux systems. |
| **AF_X25** | Protocol family for X.25 protocol networks. | Rarely used today, it is historically significant for packet-switched network applications. |
| **AF_AX25** | Amateur radio AX.25 protocol. | Applications involving amateur radio communications. |
| **AF_IPX** | Address family for Novell IPX. | Legacy applications that use Novell NetWare operating systems. |
| **AF_APPLETALK** | Protocol for AppleTalk. | Legacy applications on Apple networks. |
| **AF_BLUETOOTH** | Address family for Bluetooth protocols. | Bluetooth applications for wireless communication between devices. |
| **AF_RDS** |  The AF_RDS domain is used for Reliable Datagram Sockets, designed for high-performance, low-latency communication in clusters and data centers. | … |
| **AF_CAN** | The AF_CAN domain is used for communication over Controller Area Network (CAN) buses, and it is commonly used in automotive and industrial applications. | … |

## **Socket Type / Communication Semantics**

> **Note**: Some families of sockets does not implement all the communication semantics.
> 

> Berkeley sockets provide different types of communication semantics which dictate how data is sent and received over a network. These semantics describe the behavior of the socket, particularly how it handles connections, data flow, and reliability.
> 

> Here's a table summarizing the primary communication semantics available in Berkeley sockets:
> 

| **Communication Type** | **Socket Type** | **Description** | **Common Usage** |
| --- | --- | --- | --- |
| **Stream** | `SOCK_STREAM` | Provides a reliable, two-way, connection-based byte stream. Does not preserve record boundaries. | TCP is typically used, and it is ideal for HTTP, FTP, etc. |
| **Datagram** | `SOCK_DGRAM` | Supports data grams (connectionless, unreliable messages of a fixed maximum length). | UDP is typically used and is suitable for streaming media and DNS lookups. |
| **Sequential Packet** | `SOCK_SEQPACKET` | Provides a sequence of packets with a reliable, connection-oriented, fixed maximum length record service. | Used in scenarios where message boundaries are preserved, like SCTP. |
| **Raw** | `SOCK_RAW` | Provides raw network protocol access. | Used by applications that need access to the underlying transport protocols, such as ICMP. |
| **Reliable Datagram** | `SOCK_RDM` | Delivers messages reliably and preserves message boundaries but does not guarantee ordering. | Rarely used; applicable for specialized network services where message boundaries and reliability are required without connection overhead. |

## Protocols

Here’s a table summarizing common protocol values for the `socket()` function in C, specifically for the third argument `__protocol`:

| **Protocol Value** | **Description** | **Common Socket Types** |
| --- | --- | --- |
| **0** | Default protocol for the specified socket type. The system automatically selects the appropriate protocol. | Used with `SOCK_STREAM`, `SOCK_DGRAM`, etc. |
| **IPPROTO_TCP** | Specifies the Transmission Control Protocol (TCP) for reliable, ordered, and error-checked delivery of data. | Used with `SOCK_STREAM`. |
| **IPPROTO_UDP** | Specifies the User Datagram Protocol (UDP) for connectionless, low-latency communication without guaranteed delivery. | Used with `SOCK_DGRAM`. |
| **IPPROTO_ICMP** | Specifies the Internet Control Message Protocol (ICMP) for sending error messages and operational information. | Typically used with raw sockets. |
| **IPPROTO_IP** | Specifies the Internet Protocol (IP) for low-level IP communications. | Used with raw sockets to manipulate IP packets directly. |
| **IPPROTO_RAW** | Specifies a raw socket interface that allows sending and receiving IP packets without any protocol interpretation. | Used for low-level packet manipulation. |
| **IPPROTO_SCTP** | Specifies the Stream Control Transmission Protocol (SCTP) for message-oriented communication with multi-streaming capabilities. | Used with `SOCK_STREAM` or `SOCK_SEQPACKET`. |
| **IPPROTO_DCCP** | Specifies the Datagram Congestion Control Protocol (DCCP) for congestion-controlled transport of datagrams. | Used with `SOCK_DGRAM` or `SOCK_SEQPACKET`. |
| **IPPROTO_IPV6** | Specifies the Internet Protocol version 6 (IPv6) for communication over IPv6 networks. | Used with sockets that handle IPv6. |
| **IPPROTO_ESP** | Specifies the Encapsulating Security Payload (ESP) for providing confidentiality, authentication, and integrity. | Used with raw sockets for IPsec. |
| **IPPROTO_AH** | Specifies the Authentication Header (AH) for providing connectionless integrity and data origin authentication. | Used with raw sockets for IPsec. |
| **NETLINK_ROUTE** | Used for interacting with the routing tables and network interfaces; allows communication with the kernel for network configuration. |  |
| **NETLINK_CRT** | Used for managing Control Plane packets; useful for managing routing and network configurations. |  |
| **NETLINK_FAMILY** | A protocol for managing and configuring network namespaces; allows manipulation of network namespaces in a system. |  |
| **NETLINK_NFLOG** | Used for logging packets through the netfilter framework; allows user-space applications to receive notifications about network events. |  |

## Alternative Networking Frameworks

- [STREAMS](https://en.wikipedia.org/wiki/STREAMS)
- [Network.framework: A modern alternative to sockets](https://developer.apple.com/videos/play/wwdc2018/715/) ([developer.apple.com](https://news.ycombinator.com/from?site=developer.apple.com))

## Implementation

> See https://github.com/vibhorvatsa/xv6-networking-stack - https://github.com/pandax381/xv6-net - https://pdos.csail.mit.edu/6.828/2019/labs/net.html.
> 

## ❔QA

### After a server calls accept() on a listening socket and obtains a connected socket (client_fd), what are the local and remote socket address and port bindings of client_fd, and how do they relate to the original listening socket and the client's connect() call?

> 

### What are the implications for a server when a single client opens a large number of TCP connections to the server’s listening port and never closes them?

> Note: Discuss the effects on server resources, possible system limits encountered, TCP connection states, and mitigation strategies.
> 

### What Happens When Server Closes a Connected Socket?

1. **Close System Call (`close(client_fd)`)**
    - The server’s TCP stack initiates the **active close** procedure.
    - The TCP connection enters the **FIN-WAIT-1** state on the server side.
2. **TCP FIN Segment Sent**
    - The server sends a **FIN (finish)** packet to the client, indicating it wants to close the connection gracefully.
    - The client receives the FIN and acknowledges it (ACK), then typically enters **CLOSE-WAIT**.
3. **Half-Close State**
    - At this point, the server has closed its **write** side; it can no longer send data.
    - The client can still send data until it also closes.
4. **Client Response**
    - If the client respects TCP, it will eventually call `close()` or shutdown its socket.
    - The client sends its own FIN, and the server moves through **FIN-WAIT-2** and finally **TIME-WAIT**.
    - The connection is fully closed after the TIME-WAIT timeout.
5. **Resource Cleanup**
    - Server’s kernel frees resources associated with the socket after TIME-WAIT.
    - The file descriptor `client_fd` becomes invalid in the server process.

⚠️ Special Cases

- If the server calls `close()` but the client does not respond (e.g., crashed or network failure), the socket remains in TIME-WAIT or may time out eventually.
- If the server calls `shutdown()` before `close()`, it can partially close (read or write side) without fully closing the socket.
- If the server calls `close()` without reading all pending data, the unread data is discarded.

### What is the TCP connection state progression and resource impact on the server when it closes a connected socket but the client does not close its corresponding socket?

> **Note**:  Include the implications of half-closed connections and how the server handles incoming data in this scenario.
> 

1. …
2. If the client **never sends FIN**:
    - Server remains in **FIN-WAIT-2** indefinitely (or until timeout).
    - This can lead to **resource leakage** on the server side (half-closed connection).
3. **Timeouts and Keep-Alives**
    - Operating systems often implement **TCP keepalive probes** to detect dead peers.
    - If the client crashes or disappears without closing, the server will detect the broken connection after keepalive retries and free resources.

## References

- [Berkeley sockets](https://en.wikipedia.org/wiki/Berkeley_sockets)
- [connect.c](https://codebrowser.dev/glibc/glibc/sysdeps/unix/sysv/linux/connect.c.html)
- [How bind works internally in kernel space?](https://stackoverflow.com/questions/32273581/how-bind-works-internally-in-kernel-space)
- The Socket API https://www.unf.edu/~sahuja/cnt5505/socketnotes.html
- socket https://man7.org/linux/man-pages/man2/socket.2.html
- The Linux Kernel documentation https://docs.kernel.org/index.html
- What is a socket? https://unix.stackexchange.com/questions/16311/what-is-a-socket
- Send data to a port via linux command https://stackoverflow.com/questions/11564841/send-data-to-a-port-via-linux-command
- Inet Socket: - https://elixir.bootlin.com/linux/latest/source/net/ipv4/af_inet.c#L458
- https://stackoverflow.com/questions/25656846/understand-struct-proto-and-struct-proto-ops-in-the-kernel
- inet_bind: - https://elixir.bootlin.com/linux/latest/source/net/ipv4/af_inet.c#L433
- https://codebrowser.dev/glibc/glibc/sysdeps/unix/sysv/linux/bind.c.html
- https://elixir.bootlin.com/linux/latest/source/net/socket.c#L1789
- https://stackoverflow.com/questions/13760017/addition-of-a-new-network-protocol-in-the-linux-kernel
- protws: https://elixir.bootlin.com/linux/latest/source/net/dccp/ipv6.c#L1135 -> proto_ops
- https://codebrowser.dev/glibc/glibc/sysdeps/unix/sysv/linux/connect.c.html
- Why this is bad? sudo chmod 666 /var/run/docker.sock
- [TCP Socket Listen: A Tale of Two Queues (2022)](http://arthurchiao.art/blog/tcp-listen-a-tale-of-two-queues/)
- [TCP Retransmission May Be Misleading (2023)](http://arthurchiao.art/blog/tcp-retransmission-may-be-misleading/)
- …