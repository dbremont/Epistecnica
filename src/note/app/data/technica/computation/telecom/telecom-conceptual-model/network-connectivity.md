---
tags: [internetworking]
---

# Network Connectivity

- [Overlay Network](note.html?n=technica/computation/telecom/telecom-conceptual-model/overlay-network.md), [Relay Network](note.html?n=technica/computation/telecom/telecom-conceptual-model/relay-network.md), [Network Address Translation (NAT)](note.html?n=technica/computation/telecom/telecom-conceptual-model/network-address-translation-nat.md), [Interactive Connectivity Establishment (ICE)](note.html?n=technica/computation/telecom/telecom-conceptual-model/interactive-connectivity-establishment-ice.md)

> A General concept - to denote - a communication channel between two devices.
> 

> Technical Definition of `Network Connectivity`
> 

Guiding Questions:

- What is the nature of inter-networking? ‘Connect’ computer  two nodes in ‘different’ ‘networks’.
- Which are the technical objects, techniques, and mechanisms, strategies used to implement Internet-working?
- What is the inter-networking  nature ‘cloudflared’?
- How to expose a local service to the network?
- What is the difference between NAT and Port Forwarding?
- Which network component implements Network Address Translation (NAT)?

## What kind of technical element is **`Network Connectivity`**?

> **Network Connectivity** is the engineering **Objective (Goal) (Purpose)** of establishing and maintaining a usable communication path between communicating endpoints.
> 

## Which concrete set of network connectivity problems need to be solved in computer networking?

| Connectivity Problem | Purpose |
| --- | --- |
| **Endpoint Identification** | Identify the communicating entities. |
| **Address Assignment** | Assign unique network addresses to endpoints. |
| **Name Resolution** | Resolve human-readable names into network addresses. |
| **Neighbor Discovery** | Discover directly reachable peers on the local network. |
| **Address Resolution** | Map network-layer addresses to link-layer addresses (e.g., IP → MAC). |
| **Reachability Determination** | Determine whether a destination is currently reachable. |
| **Route Computation** | Compute an end-to-end path through the network. |
| **Packet Forwarding** | Forward packets correctly at each network hop. |
| **Path Selection** | Select the most appropriate route among alternatives. |
| **Connection Establishment** | Establish a transport-layer communication channel. |
| **Session Establishment** | Establish an application-layer communication session when required. |
| Direct Reachability Problem | … |
| **Traversal** |  |
| **NAT Traversal** | Enable communication across Network Address Translators. |
| **Firewall Traversal** | Communicate through filtering devices while respecting policy. |
| **Reliability** | Ensure data is delivered correctly despite loss or corruption. |
| **Flow Control** | Prevent overwhelming the receiver. |
| **Congestion Control** | Prevent overloading the network. |
| **Error Detection and Recovery** | Detect and recover from transmission errors. |
| **Fragmentation / MTU Handling** | Accommodate differing packet size limits. |
| **Security Establishment** | Authenticate peers and protect communication. |
| **Mobility Management** | Maintain connectivity while endpoints change networks or addresses. |
| **Multihoming / Multipath Management** | Maintain communication across multiple interfaces or paths. |
| **Service Discovery** | Discover available services on the network. |
| **Quality of Service (QoS)** | Meet latency, bandwidth, jitter, or reliability requirements. |
| **Connection Maintenance** | Detect failures and keep long-lived connections alive. |
| **Connection Recovery** | Re-establish communication after interruptions or path changes. |

## Reachability Problem Map

> **Note:** The term **relay** is used to refer to an intermediary that forwards communication between endpoints.
> 

> A lot of technical objects that solves  Reachability  Problems will used a kind of realty - mechanism - proxy, etc.
> 

| **Problem Type** | **Description** | **Implementation Technical Element Set** |
| --- | --- | --- |
| **Direct Reachability** | Two endpoints cannot establish a direct end-to-end communication path. | Direct routing, route advertisement, address assignment, connection establishment |
| **NAT Reachability** | Endpoints are unreachable because one or more Network Address Translators hide private addresses. | ICE, STUN, UDP hole punching, TCP hole punching, TURN (relay) |
| **Firewall Reachability** | Network traffic is blocked by packet-filtering or stateful firewalls. | Firewall rule configuration, outbound connection initiation, hole punching, HTTP CONNECT, SOCKS, TLS tunneling, relay |
| **Addressability Reachability** | The destination cannot be identified or resolved into a usable network address. | DNS, mDNS, DNS-SD, ARP, Neighbor Discovery Protocol (NDP) |
| **Routing Reachability** | No valid network path exists between the communicating endpoints. | Static routing, dynamic routing (OSPF, BGP, RIP), route redistribution, path selection |
| **Transport Reachability** | The transport-layer connection cannot be established. | TCP three-way handshake, QUIC connection establishment, SCTP association establishment |
| **Mobility Reachability** | Endpoint addresses or attachment points change during communication. | Mobile IP, MPTCP, connection migration, dynamic DNS |
| **Overlay Reachability** | Endpoints belong to different logical or isolated networks. | VPN, GRE tunneling, IP-in-IP, VXLAN, WireGuard, IPsec tunnel mode |
| **Relay Reachability** | A direct path is impossible, requiring an intermediary to forward traffic. | TURN, application relay, proxy, reverse proxy |

## QA

- Why is it called a **`reverse proxy`**?
- How to use ssh as a **`reverse proxy`**?

### **What is the difference between a tunneling technique and a reverse proxy technique?**

> A `tunneling technique` is a network communication technique that addresses communication encapsulation and transport problems by carrying one protocol or data stream inside another communication channel.
> 

> A `reverse proxy technique` is a network communication technique that intermediates client requests by receiving them on behalf of one or more backend services and forwarding them to the appropriate destination.
> 

### Which categories of `network connectivity` problems does `Cloudflare` address, and what `techniques` does it employ to solve them?

| **Connectivity Problem** | **Technique Family** | **Examples Used by Cloudflare** |
| --- | --- | --- |
| Reachability | Relay | Cloudflare edge forwards requests to the origin |
| NAT / Firewall Traversal | Reverse tunneling | Cloudflare Tunnel (`cloudflared`) establishes an outbound tunnel |
| Secure Transport | Encryption | TLS, QUIC |
| Service Exposure | Reverse proxy | Cloudflare edge acts as the public endpoint for origin services |
| Request Distribution | Load balancing | Selects among multiple origin servers |
| Name Resolution | DNS | Cloudflare DNS |
| Content Optimization | Caching | Edge cache, CDN |
| Availability | Failover | Health checks and origin failover |
| Traffic Management | Request routing | Host-based, path-based, and policy-based routing |

## References

- https://en.wikipedia.org/wiki/Internet_access
- https://en.wikipedia.org/wiki/Computer_network
- https://en.wikipedia.org/wiki/Hole_punching_(networking)
- https://datatracker.ietf.org/doc/html/rfc5245