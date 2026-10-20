---
tags: [discovery]
---

# Mapping


> How to **map a network**? How to list all **devices in the networks**?
> 

## Formulation

> How to think about **network-discovery mapping**?
> 

 **Define a network** as:  $G = (V, E, \mathcal{S})$:

- $V$: devices (hosts, routers, services)
- $E$: connectivity (routes, links)
- $\mathcal{S}$: exposed services (interaction surface)

**Task:**

- Infer $\hat{G} \subseteq G$ from a **partial observation point**

**You are bounded** by:

- **Topology position** (LAN, VPN, internet)
- **Protocol visibility** (L2 vs L3 vs L7)
- **Security controls** (firewalls, NAT, ACLs)

## Technique Space

> ¿Which are the **set of techniques** used to carry **such task**?
> 

| **Category** | **Technique** | **Description** | **Scope** | **Limitation** |
| --- | --- | --- | --- | --- |
| **L2 – Link Discovery** | ARP Scan | Broadcast ARP requests to resolve IP→MAC and enumerate hosts on the same segment | Local subnet (broadcast domain) | Does not cross routers; blocked outside LAN |
| **L2 – Link Discovery** | Passive ARP Observation | Listen for ARP traffic to infer active devices without probing | Local subnet | Only sees active/communicating hosts |
| **L2 – Link Discovery** | Switch CAM Table | Extract MAC→port mappings from switches | Per-switch domain | Requires privileged access to network devices |
| **L3 – Host Discovery** | ICMP Echo Sweep | Send ICMP requests to detect live hosts | Routed networks (LAN/VPN) | ICMP often filtered or rate-limited |
| **L3 – Host Discovery** | TCP SYN Ping | Send SYN packets to common ports to infer host liveness | Routed networks | Biased by firewall rules; partial visibility |
| **L3 – Host Discovery** | UDP Probe | Send UDP packets and infer hosts via ICMP unreachable responses | Routed networks | Unreliable; many systems silently drop UDP |
| **L3 – Topology Discovery** | Traceroute (TTL probing) | Increment TTL to reveal intermediate routers and paths | End-to-end paths | ICMP filtering; asymmetric routing |
| **L3 – Topology Discovery** | Route Table Inspection | Inspect local routing table to identify reachable subnets | Local vantage point | Only shows configured routes, not actual hosts |
| **L4 – Service Discovery** | TCP Port Scan | Enumerate open ports on a host | Per-host | Firewalls, rate limits, IDS detection |
| **L4 – Service Discovery** | UDP Port Scan | Probe UDP services via response behavior | Per-host | High false negatives; protocol ambiguity |
| **L7 – Service Identification** | Banner Grabbing | Read service banners to identify software and versions | Per-service | Banners may be hidden or spoofed |
| **L7 – Service Identification** | Protocol Fingerprinting | Interact with services to infer type/version | Per-service | Requires protocol knowledge; may trigger defenses |
| **L7 – Naming Layer** | DNS Resolution | Query DNS to map names→IPs and discover services | Global / domain scope | Incomplete; internal DNS may be hidden |
| **L7 – Naming Layer** | DNS Brute Enumeration | Guess subdomains/services via wordlists | Domain scope | Noisy; limited by DNS policies |
| **Passive – Traffic Analysis** | Packet Capture | Observe live traffic to infer hosts and services | Any visible interface | Requires traffic presence; partial view |
| **Passive – Traffic Analysis** | Flow Analysis (NetFlow) | Analyze aggregated flows to infer communication patterns | Network-wide (if available) | Requires infrastructure access |
| **Passive – Broadcast/Multicast** | mDNS / SSDP Discovery | Listen to service advertisements on local network | Local subnet | Limited to services that advertise |
| **Overlay – VPN Context** | VPN Subnet Scanning | Discover hosts inside VPN-assigned address space | VPN network | No L2 visibility; depends on VPN policy |
| **Overlay – Reverse Tunnel Context** | Endpoint Enumeration | Interact with exposed endpoints (e.g., via **ngrok**, **cloudflared**) | Single exposed service | No network visibility; topology collapsed |
| **Hybrid – Correlation** | Multi-source Correlation | Combine ARP, scans, DNS, and passive data into a unified graph | Depends on inputs | Requires synthesis; uncertainty remains |

## References

- https://en.wikipedia.org/wiki/Service_discovery
- https://en.wikipedia.org/wiki/Network_mapping