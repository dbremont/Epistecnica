# Telecom

> In this note, we will dive a bit deeper into **Telecommunications**, especially **computer networking**.
> 

> "Tele" to mean "distant" (from the Greek *tēle*, meaning "far off"). In this case just separated.
> 

> **Note:** The terminology in **telecommunications** is often highly inconsistent. Terms typically exhibit high semantic variability, so for each term we actually need a shorthand that captures its precise technical meaning, allowing us to detect deviations when we encounter them.
> 
> 
> **A relevant case study is the term *“router.”*** In a home setting, the device commonly called a “router” is not a pure router in the strict networking sense; it is typically a composite system that includes a router, a switch, a wireless access point, and additional networking functions integrated into a single device.
> 

QA:

- How to transmit data using **electrical signal** thought wires?
- How data is send from point a (device a) to device b; a ≠ b?
- What type of **networking performace** does **Networking Needs**?
- How to limit my network velocity specifically the traffic to specific servers?  https://github.com/magnific0/wondershaper

## Foundation

> A **computer network** is a type of communication system that enables the exchange of messages and resources between computers and other network devices. It consists of multiple computers, servers, and other network devices that are connected together using various types of communication channels, such as wired or wireless connections.
> 

> A **telecom system** is a network of hardware, software, and protocols designed to transmit voice, data, and multimedia over distances using wired, wireless, or optical technologies.
> 

![image.png](../assets/note/technica/computation/telecom/image.png)

### Characterize a Computer Network

> To characterize a **computer network**, you can consider several aspects of the network, including:
> 

| **Aspect** | **Description** |
| --- | --- |
| **Network Topology** | The physical and logical arrangement of devices, cables, and other components. Common topologies include bus, star, ring, and mesh. |
| **Network Size** | The number of devices connected to the network ranges from a few devices in a personal network to thousands or millions in an enterprise network. |
| **Network Speed** | The network's data transfer rate, measured in bits per second (bps), varies with the type of network technology used. |
| **Network Protocols** | The rules and standards for communication between devices on the network, such as the TCP/IP protocol suite for internet communication. |
| **Network Security** | Measures in place to protect the network from unauthorized access, including firewalls, encryption, and access controls. |
| **Network Applications** | The software and services run on the network, such as email, file sharing, and web applications. |

### Science

> **Telecom technologies are deeply interdisciplinary**, drawing from multiple branches of physics to enable the design, operation, and optimization of communication systems. Below is a **comprehensive table** that incorporates **all the areas of physics** underlying telecom technologies, including their specific contributions and applications.
> 

| **Area of Physics** | **Key Concepts** | **Relevance to Telecom** | **Applications** |
| --- | --- | --- | --- |
| **Electromagnetism** | Maxwell's equations, wave propagation, antenna theory, transmission line theory. | Governs signal generation, transmission, and reception in wired, wireless, and optical systems. | Wired: Ethernet, DSL. Wireless: Wi-Fi, cellular networks.  Optical: Fiber optics. |
| **Wave Mechanics** | Wave equation, superposition, interference, diffraction, Doppler effect. | Describes how signals propagate and interact with obstacles or other signals. | Wireless: Multipath fading. Optical: Dispersion in fiber optics. |
| **Quantum Mechanics** | Band theory, photoelectric effect, quantum entanglement. | Underlies semiconductor devices (e.g., transistors, lasers) and quantum communication. | Transistors in electronics Quantum cryptography. Lasers in fiber optics. |
| **Optics** | Snell's law, total internal reflection, dispersion, nonlinear optics. | Enables light-based communication systems, such as fiber optics and Li-Fi. | Fiber optic networks.  Li-Fi (light-based wireless communication). |
| **Solid-State Physics** | Bandgap, doping, p-n junctions, semiconductor materials. | Enables the development of electronic and optoelectronic components. | Transistors, diodes, LEDs, lasers.  Integrated circuits in telecom hardware. |
| **Thermodynamics** | Heat transfer, thermal conductivity, energy efficiency. | Manages heat dissipation in electronic devices to ensure reliable operation. | Cooling systems for routers, servers, and base stations. Energy-efficient designs. |
| **Signal Processing** | Fourier transforms, modulation, error correction, data compression. | Provides mathematical tools for encoding, transmitting, and decoding information. | Digital modulation (e.g., QAM, OFDM). Error correction codes (e.g., LDPC, Turbo codes). |
| **Acoustics** | Sound wave propagation, resonance, noise cancellation. | Relevant for voice communication technologies, such as telephony and VoIP. | Microphones, speakers, and audio codecs.  Noise reduction in voice calls. |
| **Plasma Physics** | Ionospheric reflection, plasma antennas. | Affects satellite communication through ionospheric interactions. | Satellite communication.  High-frequency radio wave propagation. |
| **Relativity** | Time dilation, gravitational redshift. | Critical for satellite-based communication (e.g., GPS timing and synchronization). |  GPS and GNSS systems. Satellite networks. |
| **Statistical Mechanics** | Thermal noise, Gaussian distributions, random processes. | Models noise and random processes in communication systems. | Noise modeling in receivers. Signal-to-noise ratio (SNR) optimization. |
| **Nonlinear Dynamics** | Chaos theory, solitons, nonlinear effects. | Addresses signal distortion and nonlinear effects in communication systems. | Solitons in fiber optics.  Mitigating signal distortion in amplifiers. |

### Ontology Map

> Which is the ontology that captures telecom and networking?
> 

| Element | Description | Related To | Instance(s) | Tags |
| --- | --- | --- | --- | --- |
| **Node** | Active computational or forwarding entity that processes, stores, or forwards data; base abstraction for both physical hardware and virtual instances. | Link, Protocol, Service, VNF | `server`, `VM`, `container`, `bare-metal` | `layer:infrastructure`, `role:processing+forwarding`, `stateful` |
| **Router** | Layer 3 device that forwards packets between IP subnets using a routing table (FIB) and routing protocols (OSPF, BGP). | Node, IP, Routing, FIB | `Cisco ASR 9000`, `Juniper MX`, `Linux net.ipv4.ip_forward` | `layer:network`, `role:routing-enforcement`, `stateful` |
| **Switch** | Layer 2 device that forwards frames within a broadcast domain using a MAC address table; does not understand IP. | Node, Ethernet, MAC-table | `Cisco Catalyst`, `Arista 7050`, `OVS bridge` | `layer:link`, `role:frame-forwarding`, `semi-stateful` |
| **Bridge** | Layer 2 device that connects and segments multiple network segments (collision domains) while forwarding based on MAC addresses; similar to a switch but typically with fewer ports and software-based forwarding; can also bridge between different media types (e.g., Ethernet to Wi-Fi). | Switch, MAC-table, Spanning Tree | `Linux bridge`, `Wi-Fi to Ethernet bridge`, `old 2-port bridge` | `layer:link`, `role:segment-connection+frame-forwarding`, `semi-stateful` |
| **Repeater** | Layer 1 physical layer device that regenerates and retransmits electrical or optical signals to extend transmission distance; does not interpret or filter data; operates on bits, not frames or packets. | Link, Fiber Optic | `Ethernet extender`, `optical amplifier`, `hub` | `layer:physical`, `role:signal-regeneration`, `stateless`, `bit-level` |
| **Hub** | Layer 1 device that broadcasts incoming signals to all other ports; no intelligence, no MAC learning; collision domain not segmented; largely obsolete, replaced by switches. | Node, Repeater, Ethernet | `Ethernet hub (10BASE-T)`, `USB hub (different context)` | `layer:physical`, `role:signal-broadcast`, `stateless`, `obsolete` |
| **Modem** | Modulator-Demodulator – converts digital signals from a computer to analog signals for transmission over analog medium (telephone line, cable, DSL) and vice versa. | Link, ISP | `cable modem (DOCSIS)`, `DSL modem`, `dial-up modem (56k)` | `layer:physical`, `role:digital-to-analog-conversion`, `stateless`, `medium:coax/telephone` |
| **Gateway** | Network device that connects networks with different protocols (e.g., LAN to WAN, IPv4 to IPv6, Ethernet to serial); often combines router, NAT, firewall, and DHCP server functions; default gateway is the exit point from a LAN. | Router, NAT, Firewall | `home broadband router`, `default gateway 192.168.1.1`, `IoT gateway`, `API gateway` | `layer:network/application`, `role:protocol-translation+default-exit`, `stateful`, `multi-function` |
| **Base Station** | Wireless access node (eNB/gNB) that bridges mobile devices to the core network and manages radio resources (spectrum, scheduling, handovers). | UE, Spectrum, RAN | `4G eNB`, `5G gNB`, `Wi-Fi AP (in cellular context)` | `layer:access`, `role:radio-interface`, `stateful`, `stochastic` |
| **Relay** | Layer 2-3 device that receives, regenerates, and forwards signals/frames/packets between segments; may update MAC (L2) or decrement TTL (L3); does NOT encapsulate; used in wireless mesh, satellite, coverage extension, and local service exposure (ngrok, Cloudflare Tunnel). | Node, Link, Base Station | `Wi-Fi extender`, `satellite transponder`, `mesh node`, `store-and-forward relay`, `ngrok`, `Cloudflare Tunnel` | `layer:link/network`, `role:forwarding+regeneration`, `no-encapsulation`, `coverage-extension` |
| **Network Interface Card (NIC)** | Hardware component that connects a node to a network medium; provides MAC address and physical interface (Ethernet port, Wi-Fi radio); operates at L1 (physical) and L2 (link). | Node, MAC Address, Link | `Intel Ethernet I350`, `Broadcom BCM5719`, `Realtek RTL8111`, `Wi-Fi 6 card` | `layer:physical/link`, `role:medium-attachment`, `has:MAC-address`, `stateless` |
| **Tunnel** | Virtual point-to-point logical link that encapsulates packets (e.g., GRE, IPsec, VXLAN) to traverse intermediate networks transparently; adds outer header, leaves inner packet unchanged; may include encryption (IPsec, WireGuard) or not (GRE, VXLAN). | Path, VPN, GRE, IPsec, VXLAN | `GRE tunnel`, `IPsec tunnel mode`, `WireGuard`, `VXLAN overlay` | `layer:network/transport`, `role:encapsulation`, `stateless`, `adds-outer-header` |
| **VXLAN** | Virtual Extensible LAN – encapsulates Ethernet frames in UDP (port 4789) with 24-bit VNI; enables 16M isolated L2 segments across L3 networks; **no encryption**; used in trusted data center fabrics for VM mobility and multi-tenancy. | Tunnel, UDP, Switch, VTEP | `Linux VXLAN`, `Cisco NX-OS VXLAN`, `VMware NSX`, `Flannel VXLAN (K8s)` | `layer:overlay`, `role:L2-over-L3-encapsulation`, `stateless`, `VNI:24-bit`, `no-encryption`, `port:4789` |
| **VPN** | Virtual Private Network – uses encrypted tunnels to extend a private network across a public network; provides confidentiality, authentication, and integrity; two main variants: remote access (employee to corp) and site-to-site (office to office). | Tunnel, IPsec, WireGuard, OpenVPN | `NordVPN (consumer)`, `Cisco AnyConnect (enterprise)`, `AWS VPN (site-to-site)` | `role:private-network-extension`, `encrypted`, `authenticated`, `two-variants:remote-access+site-to-site` |
| **VNF** | Virtualized Network Function – software instance of a network function (router, firewall, etc.) running on commodity hardware via hypervisor/container. | Node, Hypervisor, NFVO, MANO | `vRouter`, `vFirewall`, `vEPC`, `Open vSwitch` | `nature:virtual`, `role:network-function`, `lifetime:variable`, `stateful/stateless` |
| **Hypervisor (Container Runtime)** | Virtualization layer that isolates and hosts VNFs on a physical node, managing CPU, memory, and I/O scheduling. | VNF, Node | `KVM`, `ESXi`, `Docker`, `containerd`, `runc` | `layer:infrastructure`, `role:resource-isolation`, `stateful` |
| **Link** | Physical or logical channel connecting two nodes, characterized by bandwidth, latency, and availability. | Node, Path, Queue | `Ethernet cable`, `radio bearer`, `VXLAN tunnel`, `GRE tunnel` | `layer:infrastructure`, `role:transport`, `stateless` |
| **Fiber Optic** | Physical medium using light pulses in glass strands; provides very high bandwidth (THz-scale) and low latency; primarily in core/metro networks. | Link, OLT | `SMF-28e`, `OM4 multimode`, `DWDM span` | `layer:physical`, `role:transport`, `stateless`, `immutable` |
| **Wireless Spectrum** | Shared radio frequency resource (time, frequency, code) regulated and allocated to base stations and devices; inherently stochastic due to interference and fading. | Base Station, UE | `2.4 GHz ISM`, `3.5 GHz CBRS`, `28 GHz mmWave`, `5G NR band n78` | `layer:physical`, `role:shared-medium`, `stateless`, `stochastic` |
| **Queue** | Buffer at a link output that holds packets awaiting transmission, with a scheduling discipline (FIFO, WFQ) and dropping policy (tail-drop, RED, CoDel). | Link, Packet, QoS, AQM | `tc qdisc pfifo_fast`, `Cisco QoS queue`, `Linux fq_codel` | `layer:link/network`, `role:congestion-control`, `stateful` |
| **Network** | Interconnected system of nodes and links that provides data transport services; has a topology, control plane, and management domain. | Topology, Service, Domain | `Internet`, `corporate MPLS VPN`, `5G core`, `home LAN` | `layer:logical`, `role:organization`, `stateful` |
| **Topology** | Structural arrangement of nodes and links in a network, represented as a graph; can be static (planned) or dynamic (after failures). | Network, Graph | `mesh`, `star`, `ring`, `tree`, `fat-tree`, `leaf-spine` | `layer:logical`, `role:connectivity-schema`, `static/dynamic` |
| **Path** | Ordered sequence of links and nodes from source to destination; a concrete instance of a route through the topology. | Link, Node, Route, Tunnel | `AS path in BGP`, `MPLS LSP`, `traceroute result` | `layer:network`, `role:end-to-end-forwarding`, `stateless` |
| **Subnet** | Logical IP partition (CIDR block) where all nodes can communicate directly without a router; defined by network prefix and mask. | IP, Router, DHCP | `192.168.1.0/24`, `10.0.0.0/16`, `2001:db8::/32` | `layer:network`, `role:segmentation`, `config-state` |
| **VLAN** | Layer 2 segmentation that isolates broadcast domains on a switch; assigns ports to virtual LANs identified by 802.1Q tags. | Switch, Subnet, Trunk | `VLAN 10 (Engineering)`, `VLAN 20 (Sales)`, `Native VLAN 1` | `layer:link`, `role:isolation`, `config-state` |
| **Protocol** | Formal set of rules and message formats that govern communication between network entities; defines syntax, semantics, and timing. | Packet, FSM | `RFC 793 (TCP)`, `RFC 791 (IP)`, `IEEE 802.3 (Ethernet)` | `layer:all`, `role:coordination`, `standardized` |
| **TCP** | Connection-oriented transport protocol providing reliable, in-order delivery with flow control (window), congestion control (AIMD), and error recovery (retransmission). | IP, Flow, Queue, Congestion-Control | `TCP Reno`, `TCP Cubic`, `TCP BBR` | `layer:transport`, `role:reliability+flow-control`, `stateful (per-connection)` |
| **UDP** | Connectionless transport protocol with no reliability, ordering, or congestion control; used for real-time or low-latency applications (VoIP, DNS, gaming). | IP, Flow, RTP | `DNS (port 53)`, `RTP (VoIP)`, `QUIC`, `DTLS` | `layer:transport`, `role:fast-transport`, `stateless` |
| **IP** | Network-layer protocol that provides best-effort datagram delivery across heterogeneous networks using hierarchical addressing (IPv4/IPv6). | Router, Packet, FIB | `IPv4`, `IPv6`, `IP-in-IP` | `layer:network`, `role:packet-delivery`, `stateless` |
| **Ethernet** | Link-layer protocol for local area networks; defines framing, MAC addressing (48-bit), CSMA/CD (historically), and switching behavior (learning, flooding, forwarding). | Switch, MAC-address, Frame | `10BASE-T`, `1000BASE-SX`, `10GBASE-SR`, `802.3cg (10BASE-T1L)` | `layer:link`, `role:framing+addressing`, `stateless` |
| **Packet** | Network-layer datagram consisting of a header (control info: src/dst IP, TTL, protocol) and a payload (user data); the fundamental unit of IP forwarding. | Protocol, Queue, Flow | `IPv4 packet`, `IPv6 packet`, `ICMP echo request` | `layer:network`, `role:transfer-unit`, `ephemeral`, `has:header+payload` |
| **Frame** | Link-layer data unit that encapsulates a packet, adding MAC addresses, type/length field, and frame check sequence (CRC) for error detection. | Switch, Ethernet, CRC | `Ethernet frame`, `802.11 frame`, `PPP frame` | `layer:link`, `role:local-delivery`, `ephemeral` |
| **Flow** | Aggregate of packets sharing common properties (usually 5-tuple: src/dst IP, src/dst port, protocol); represents a traffic stream for monitoring and QoS. | Packet, Session, QoS | `NetFlow record`, `sFlow sample`, `TCP flow 5-tuple` | `layer:transport/network`, `role:traffic-identification`, `ephemeral`, `5-tuple` |
| **Session** | Stateful application-layer conversation (e.g., TCP connection, SIP call, QUIC) with identifiable phases: setup, data transfer, teardown. | Flow, TCP, SIP | `TCP socket pair`, `SIP dialog`, `QUIC connection`, `TLS session` | `layer:application/transport`, `role:stateful-interaction`, `ephemeral`, `has:setup/active/teardown` |
| **QoS Profile** | Set of performance constraints (minimum bandwidth, maximum latency, jitter, loss rate) applied to a flow or class; mapped to DSCP or 802.1p priorities. | Flow, SLA, Queue, DSCP | `EF (expedited forwarding)`, `AF41`, `BE (best effort)`, `5G QoS flow 5QI=1` | `layer:network/link`, `role:performance-specification`, `metrics:latency+jitter+loss+bandwidth` |
| **SLA (Service Level Agreement)** | Formal contract between provider and customer specifying guaranteed performance metrics (derived from QoS profiles), measurement intervals, and penalties for violations. | QoS Profile, Service, OSS | `99.999% availability SLA`, `<10ms latency SLA`, `broadband ISP SLA` | `layer:service`, `role:guarantee+remediation`, `legal+technical` |
| **Service** | End-user offering (e.g., VoIP, streaming, VPN, 5G connectivity) delivered over the network, composed of multiple flows and potentially backed by SLAs. | Flow, SLA, VNF, Orchestrator | `VoIP service`, `IPTV`, `5G eMBB`, `enterprise VPN` | `layer:application/service`, `role:value-delivery`, `stateful (subscribers)` |
| **SDN Controller** | Centralized control plane entity that programs forwarding tables of switches (via OpenFlow, P4, or NETCONF) and provides a global network view to applications. | Node, OpenFlow, Switch | `ONOS`, `ODL (OpenDaylight)`, `Floodlight`, `ONAP` | `layer:control`, `role:path-computation+policy-enforcement`, `stateful (network view)` |
| **Orchestrator (NFV MANO)** | Management and orchestration system (ETSI MANO compliant) that automates VNF lifecycle: instantiation, scaling, healing, termination across cloud infrastructure. | VNF, Service, OSS/BSS | `ONAP`, `OSM (Open Source MANO)`, `Cloudify`, `Kubernetes (as orchestrator)` | `layer:management`, `role:lifecycle-management`, `stateful (inventory)` |
| **OSS/BSS** | Operations Support System (network inventory, fault, performance management) and Business Support System (billing, order management, customer care) for telecom providers. | Service, Orchestrator, SLA | `Amdocs`, `Netcracker`, `Cisco NSO`, `Jira+ServiceNow (minimal)` | `layer:management`, `role:provisioning+billing+assurance`, `stateful` |
| **Failure** | Deviation from expected behavior causing service degradation or outage; types include hard failure (link down, crash), soft failure (bit errors, high latency), and Byzantine (arbitrary). | Node, Link, Flow, Anomaly | `link down`, `router crash`, `BGP session reset`, `optical signal loss` | `role:disruption`, `stochastic`, `types:hard+soft+byzantine` |
| **Anomaly** | Statistical deviation from normal traffic or behavior patterns (e.g., DDoS, flash crowd, misconfiguration, routing loop); may indicate security incidents or network issues. | Flow, Failure, Security | `DDoS attack`, `routing loop`, `broadcast storm`, `TCP SYN flood` | `role:indicator`, `statistical`, `detectable (ML)` |
| **IP Address** | Logical 32-bit (IPv4) or 128-bit (IPv6) identifier assigned to a network interface; used for routing and endpoint identification; can be static or dynamic (DHCP). | Node, Subnet, DNS | `192.168.1.1`, `8.8.8.8`, `2001:4860:4860::8888`, `169.254.0.1 (link-local)` | `role:addressing+routing`, `format:32/128-bit`, `static/dynamic` |
| **MAC Address** | Hardware 48-bit identifier burned into a network interface (NIC); used for link-layer addressing within a broadcast domain; locally unique, globally administered. | Node, Switch, ARP | `00:11:22:AA:BB:CC`, `de:ad:be:ef:00:01`, `broadcast: FF:FF:FF:FF:FF:FF` | `role:local-addressing`, `format:48-bit`, `static` |
| **ASN (Autonomous System Number)** | Globally unique 16-bit or 32-bit identifier assigned to an Autonomous System (routing domain) for BGP peering and inter-domain routing. | BGP, Router, Peering | `AS15169 (Google)`, `AS32934 (Facebook/Meta)`, `AS64501 (private)` | `role:routing-domain`, `format:16/32-bit`, `static` |
| **Network Identifier** | Abstract parent class for all network identifiers; not instantiated directly. Provides common attributes: uniqueness scope, assignment method, mutability. | IP Address, MAC Address, ASN | *(abstract – no instances)* | `abstract`, `role:unique-reference` |
| **Control Plane** | Logical partition of network responsible for routing decisions, topology discovery, signaling, and policy; populates forwarding tables used by data plane. | Data Plane, Routing Protocol, SDN Controller | `OSPF process`, `BGP speaker`, `RIP daemon`, `ARP table manager` | `layer:control`, `role:decision-making+signaling`, `stateful`, `conceptual` |
| **Data Plane** | Logical partition of network responsible for actual forwarding of packets/frames based on tables populated by control plane; operates at high speed, minimal logic. | Control Plane, FIB, Switching ASIC | `router FIB lookup`, `switch MAC table`, `Linux netfilter`, `P4 pipeline` | `layer:data`, `role:packet-forwarding`, `stateless or fast-path`, `conceptual` |
| Computer Network | Concrete instantiation of a network: a set of interconnected nodes and links operating under a shared addressing, routing, and control regime; includes both data plane (forwarding) and control plane (decision-making). | Network, Node, Link, Protocol, Control Plane, Data Plane | `home LAN`, `enterprise network`, `ISP backbone`, `Kubernetes CNI network` | `layer:system`, `role:execution-environment`, `stateful`, `composed-of:nodes+links+protocols` |
| Subnet | Logical IP reachability domain defined by a CIDR prefix where nodes consider each other directly reachable (no router hop) and resolve addresses via a local mechanism (e.g., ARP for IPv4, ND for IPv6); induces a link-scope route in each host. | IP Address, Router, ARP, Routing Table, VLAN | `192.168.1.0/24`, `10.0.0.0/16`, `fd00::/64` | `layer:network`, `role:direct-reachability-domain`, `config-state`, `requires:prefix+mask+link-scope-route` |
| **Subnet Mask  (Prefix)** | Bitmask (IPv4) or prefix length (CIDR) that partitions an IP address into network and host portions; used by hosts to decide whether a destination is local (on-link) or requires routing via a gateway. | Subnet, IP Address, Routing Table | `255.255.255.0`, `/24`, `/64 (IPv6)` | `layer:network`, `role:address-partitioning`, `deterministic`, `defines:network-boundary` |
| Broadcast Domain | Set of nodes that receive L2 broadcast frames; typically coincides with a subnet but is technically defined at L2 (can be segmented via VLANs). | Switch, VLAN, ARP, Ethernet | `VLAN 10 broadcast domain`, `home LAN` | `layer:link`, `role:signal-propagation-scope`, `configurable`, `bounded-by:L2 devices` |
| Routing Table (RIB/FIB) | Data structure in a node that determines next-hop decisions; includes connected (link-scope) routes for subnets and default routes for external traffic. | Router, Subnet, IP, Control Plane, Data Plane | `ip route`, `Linux FIB`, `Cisco routing table` | `layer:network`, `role:forwarding-decision`, `stateful`, `contains:connected+static+dynamic routes` |
| OSI Model |  |  |  |  |
| TCP/IP Model |  |  |  |  |
| Network Function Virtualization (NFV) |  |  |  |  |
| Software-Defined Networking (SDN) |  |  |  |  |
| **Port** | A logical endpoint for communication, identified by a number, is used by transport protocols like TCP and UDP to manage multiple connections simultaneously. |  |  | software-abstraction |
| **Socket** | An endpoint for sending and receiving data across a network, combining an IP address and a port number to establish a connection between devices. |  |  | software-abstraction |
| **Protocol** | A set of rules and standards, such as HTTP, FTP, and SMTP, defines how data is transmitted and received over a network. |  |  | software-abstraction |
| **Packet** | A small unit of data transmitted over a network, containing a payload and control information such as source and destination addresses. |  |  | software-abstraction |
| **IP Address** | A unique numerical identifier assigned to each device on a network is used to route packets to their correct destinations. |  |  | software-abstraction |
| **MAC Address** | A unique identifier is assigned to network interfaces for communications at the data link layer, used within local networks. |  |  | software-abstraction |
| **Frame** | A data unit is used in data link layer communications, encapsulating a packet with additional header and trailer information for error checking and control. |  |  | software-abstraction |
| **Datagram** | A basic transfer unit associated with packet-switched networks is typically used in connectionless communications like UDP. |  |  | software-abstraction |
| **Session** | A connection is established between two network devices for the duration of a communication exchange, managed by session protocols like SSL/TLS. |  |  | software-abstraction |
| **Stream** | Communication protocols like TCP use a continuous data flow, which allows data to be sent and received in a steady stream rather than in discrete packets. |  |  | software-abstraction |
| **Virtual Circuit** | A logical connection is created within a network to provide a reliable data transfer service, often used in ATM and Frame Relay networks. |  |  | software-abstraction |
| **Interface** | An abstraction represents the point of interaction between different network components, including network interfaces (NICs) and software interfaces (APIs). |  |  | software-abstraction |
| **Endpoint** | A specific IP address and port number combination is used for network communication, identifying a particular process on a device within a network. |  |  | software-abstraction |
| **Namespace** | A conceptual domain in which names are defined and used, ensuring unique identification of resources such as IP addresses or domain names. |  |  | software-abstraction |
| **Middleware** | Software that provides common services and capabilities to applications outside of what's offered by the operating system, facilitating communication and data management. |  |  | software-abstraction |
| **Service** | A server provides a function or set of functions to a client over a network, often defined by interfaces and protocols. |  |  | software-abstraction |
| **API (Application Programming Interface)** | A set of rules and tools for building software and applications, defining how components should interact and communicate with each other. |  |  | software-abstraction |
| **Network Interface** | A network interface is a connection point between a computer or other network device and a network, enabling communication and data transfer between devices. It can be implemented as hardware, software, or a combination of both. |  |  | software-abstraction |

### Network Type Set

| **Category** | **Type** | **Description** |
| --- | --- | --- |
| **Based on Size** | Personal Area Network (PAN) | The most minor type of network typically connects devices within a few meters of each other, such as a keyboard, mouse, and printer, to a computer. |
|  | Local Area Network (LAN) | Connects devices within a small geographic area, such as an office building or a campus. |
|  | Metropolitan Area Network (MAN) | Covers a larger area than a LAN, such as a city or a region. |
|  | Wide Area Network (WAN) | It covers a large geographic area, such as a country or even the whole world; the Internet is an example of a WAN. |
| **Based on Topology** | Bus topology | All devices are connected to a single cable called the bus. |
|  | Star topology | All devices are connected to a central hub or switch. |
|  | Ring topology | All devices are connected in a circular ring. |
|  | Mesh topology | All devices are connected directly to each other. |
| **Based on the Technology Used** | Ethernet | A popular LAN technology that uses a bus or a star topology supports data transfer rates of up to 10 Gbps. |
|  | Wi-Fi | A wireless LAN technology that allows devices to connect to the network using radio waves. |
|  | Bluetooth | A wireless PAN technology that allows devices to connect over short distances. |
|  | Cellular network | WANs use radio waves to connect mobile devices to the Internet. |
| **Based on Ownership** | Private network | Owned and operated by an organization for its use. |
|  | Public network | It is owned and operated by a service provider and is accessible to anyone who pays for the service. |
|  | Hybrid network | A combination of private and public networks. |
| **Uncategorized** | Backbone or core network | A part of a computer network that interconnects networks provides a path for exchanging information between different LANs or subnetworks; it usually has greater capacity than the networks. |

## Architecture

> **Network Segmentation**: A **network segment** is a portion of a computer network that is separated from other parts of the network by devices like **routers**, **bridges**, or **switches**. It can refer to either a physical or logical division (subnets,  vlan) of a network.
> 

## Plane

> 

> Management Plane → Control Plane → Data Plane.
> 

### Management Plane

> The management plane is responsible for managing the network as a whole, including tasks such as network monitoring, security, and performance management. It is typically implemented through software tools and interfaces.
> 

> Management Plane → Control Plane → Data Plane.
> 

### Control Plane

> The control plane is responsible for managing the network infrastructure, including network devices such as routers and switches. It is responsible for routing and forwarding decisions, as well as network configuration and management.
> 

### Data Plane

> The data plane, also known as the forwarding plane, is responsible for the actual transmission of data between network devices. It is responsible for processing and forwarding data packets, and is typically implemented in hardware.
> 

## Connectivity

> Connecting multiple independent networks into a larger composite network while preserving end-to-end communication.
> 

> Which are the implementation models? Relay, Virtual Circuit Model, Encapsulation (Tunneling Model),  Translation (Gateway Model),  Overlay Network Model, etc.
> 

> See [Network Connectivity](note.html?n=technica/computation/telecom/telecom-conceptual-model/network-connectivity.md).
> 

## Communication (Interaction Through a Connectivity Mechanism)

> **Communication is the process by which two or more entities exchange information through a connectivity mechanism that enables the transfer, synchronization, or coordination of states, signals, or messages.**
> 

> A **connectivity mechanism** provides the technical means by which entities become reachable to each other and can establish an interaction path. Communication then occurs through the exchange of structured information over that path.
> 

> A **Web API (Application Programming Interface)** is a set of rules and protocols for building and interacting with web-based applications, allowing different software systems to communicate over the internet using HTTP methods.
> 

> See more in [Interaction Protocol](note.html?n=technica/computation/distributed-computing/multi-node-processing-system-conceptual-model/interaction-protocol.md)
> 

| **Communication Method** | **Description** | **Key Features** | **Use Cases** |
| --- | --- | --- | --- |
| **HTTP/HTTPS (RESTful APIs)** | Architectural style for networked applications using HTTP requests to specific URLs for resource manipulation. | Stateless, uses standard HTTP methods (GET, POST, PUT, DELETE). | Web services, APIs, client-server communication. |
| **WebSocket** | Provides full-duplex, bidirectional communication channels over a single TCP connection. | Real-time data exchange, persistent connection. | Real-time applications, chat, online gaming. |
| **GraphQL** | Allows clients to request exactly the data they need through structured queries to a GraphQL endpoint. | Flexible data querying, reduces over-fetching. | Complex APIs, applications with varied data needs. |
| **gRPC** | Remote Procedure Call framework developed by Google, using Protocol Buffers for service contracts. | Supports multiple languages, efficient binary serialization. | Microservices, high-performance applications. |
| **Message Queues (e.g., RabbitMQ, Apache Kafka)** | Asynchronous communication between clients and servers using message brokers. | Event-driven architecture, distributed processing. | Task queues, event-driven systems, distributed processing. |
| **SOAP (Simple Object Access Protocol)** | Protocol for exchanging structured information, typically using XML for message format. | Strict rules for message structure, protocol-based. | Enterprise applications, web services with strict standards. |
| **XML-RPC and JSON-RPC** | RPC protocols using XML or JSON for message format, allowing remote procedure calls. | Lightweight communication, simple protocol. | Interfacing between different systems, remote method invocation. |
| **Remote Method Invocation (RMI)** | Java-specific protocol for invoking methods on remote Java objects. | Java-based, remote object method invocation. | Distributed Java applications. |
| **CORBA (Common Object Request Broker Architecture)** | Middleware specification for distributed systems, allowing remote method invocations. | Supports multiple languages, middleware-based. | Distributed systems requiring cross-language interoperability. |
| **WebSockets with [Socket.io](http://socket.io/)** | Builds on WebSockets to offer an abstracted real-time communication library with fallback mechanisms. | Simplified real-time communication, fallback support. | Real-time web applications, cross-browser real-time communication. |
| **Meteor DDP (Distributed Data Protocol)** | Protocol for real-time data synchronization in Meteor framework applications. | Real-time data sync, uses WebSockets or other transport mechanisms. | Real-time web applications developed with Meteor. |
| **JSON-Rest** | Simple JSON-based protocol combining JSON and REST principles. | Lightweight, uses JSON for communication. | Lightweight APIs, mobile applications. |
| **Server-Sent Events (SSE)** | Protocol for one-way streaming of events from server to client over a single HTTP connection. | Simple event streaming, server push. | Real-time updates, notifications. |
| **HTTP/2 and HTTP/3 (QUIC)** | Modern HTTP versions with improvements in performance and efficiency. | Multiplexing, header compression, performance enhancements. | High-performance web applications, improved client-server interactions. |
| **JSON-P (JSON with Padding)** | Method for cross-domain requests using script tags to fetch JSON data. | Overcomes same-origin policy restrictions. | Cross-domain requests in web applications. |
| **Request-Response (Synchronous)** | Clients send requests and wait for immediate responses. | Immediate feedback, synchronous communication. | Traditional web applications, simple client-server interactions. |
| **Publish-Subscribe (Asynchronous)** | Servers broadcast events to clients who have subscribed to specific topics or channels. | Asynchronous, real-time notifications. | Event-driven systems, real-time updates. |
| **WebSocket (Full-Duplex)** | Persistent, bidirectional communication channel between clients and servers. | Real-time, low-latency data exchange. | Chat applications, online gaming, financial trading. |
| **Message Queues (Asynchronous)** | Communication using a shared message queue or broker for asynchronous, loosely coupled interactions. | Asynchronous, scalable communication. | Distributed processing, background job processing. |
| **Serverless (Function as a Service - FaaS)** | Clients trigger serverless functions to execute tasks without managing servers. | Event-driven, scalable, managed execution environment. | Event-driven architectures, microservices. |
| **P2P (Peer-to-Peer)** | Clients communicate directly with each other, bypassing centralized servers. | Direct communication, decentralized. | File sharing, VoIP applications. |
| **Long Pooling** | … | … | .. |

## Protocol

> A network protocol is a formal specification of the messages, formats, states, behaviors, and procedures required for two or more networked systems to achieve communication and coordination.
> 

> A **network protocol** is a set of rules and conventions that define how data is transmitted and received over a network, ensuring proper communication between devices.
> 

| **OSI Layer** | **Category** | **Protocol** | **Description** |
| --- | --- | --- | --- |
| **Application** | Web | HTTP, HTTPS, QUIC | Web browsing, secure & fast communication |
|  | Messaging / Chat | XMPP, IRC, SIP, Matrix, MQTT, AMQP | Real-time messaging, VoIP, IoT pub/sub |
|  | File Transfer | FTP, FTPS, SFTP, TFTP, SCP, WebDAV | Transfer files between systems |
|  | Email | SMTP, IMAP, POP3, MAPI | Sending and receiving email |
|  | Remote Access | SSH, Telnet, RDP, VNC, NX | Remote terminal or GUI access |
|  | Name Services | DNS, mDNS, DoH, DoT | Domain name resolution, secure DNS |
|  | Directory Services | LDAP, LDAPS, NIS | User and device directory services |
|  | Time Sync | NTP, PTP | Synchronize clocks across networked systems |
|  | Network Management | SNMP, NETCONF, RESTCONF | Monitoring and managing devices |
|  | Information | QOTD, TIME, DAYTIME | Return text or time data |
|  | Printing | LPD, IPP | Network printing services |
|  | Software Updates | WSUS, SUC | Update and patch software |
|  | File Sharing | SMB, NFS, AFP | Share files over a network |
|  | Streaming | RTSP, RTP, HLS, DASH | Stream audio/video data |
|  | Configuration | DHCP, BOOTP | Assign IP & config info dynamically |
|  | SCADA / Industrial | Modbus, BACnet, DNP3, OPC UA | Industrial automation and control |
|  | Blockchain | LibP2P, Ethereum Wire, Bitcoin P2P | Peer-to-peer crypto/blockchain networks |
| **Presentation** | Encoding / Security | TLS, SSL, ASCII, JPEG, MPEG, ASN.1, JSON, XML | Data format, compression, encryption |
| **Session** | Session / Tunneling | NetBIOS, SMB Session, PPTP, RPC, SOCKS | Manage sessions and tunnels |
| **Transport** | Reliable Transport | TCP, SCTP, MPTCP | Ordered, reliable transmission |
|  | Unreliable / Fast Transport | UDP, DCCP, RUDP | Faster delivery, no guarantees |
|  | Secure Transport | TLS (over TCP), DTLS (over UDP) | Encrypted data transport |
| **Network** | Addressing / Routing | IP (v4/v6), BGP, OSPF, RIP, IS-IS, EIGRP | Routing and forwarding packets |
|  | Error Reporting | ICMP, ICMPv6 | Diagnostics (e.g., ping), error handling |
|  | Multicast | IGMP, MLD | Multicast group management |
|  | Mobility / Tunnels | Mobile IP, GRE, L2TP | Seamless roaming, encapsulation |
|  | Security | IPsec, AH, ESP | Authentication and encryption at IP layer |
| **Data Link** | LAN/WAN | Ethernet, VLAN, PPP, Frame Relay, HDLC | Framing, data transmission |
|  | Address Resolution | ARP, RARP, NDP | Resolve MAC/IP addresses |
|  | Loop Prevention | STP, RSTP, MSTP | Prevent switching loops |
|  | Discovery | CDP, LLDP, FDP | Network device and topology discovery |
|  | Wireless / IoT | IEEE 802.11, Bluetooth, Zigbee, Z-Wave | Wireless local and sensor networks |
|  | Metro/Carrier | MPLS, QinQ | High-performance transport in ISP networks |
| **Physical** | Media | Cat5/6, Fiber, Coax, DSL, RS-232, Wi-Fi, 5G | Transmit bits over physical media |
|  | Modulation | NRZ, QAM, BPSK, OFDM | Convert data into transmittable signals |

## Technical Element Set Modulo

> 

| **Category** | **Subcategory** | **Technology** | Year | **Description** |
| --- | --- | --- | --- | --- |
| **Historical Technologies** | **Early Communication** | Telegraph |  | Early electrical communication system for transmitting text messages over wires. |
|  |  | Telephone |  | Alexander Graham Bell's invention for voice communication over wires. |
|  |  | Radio |  | Wireless communication using radio waves for broadcasting and point-to-point communication. |
| **Wireless Communication** | **Short-Range Wireless** | Wi-Fi (IEEE 802.11) |  | Wireless LAN technology for local internet access. |
|  |  | Bluetooth |  | Short-range wireless communication for personal area networks (PANs). |
|  |  | Zigbee |  | Low-power wireless protocol for IoT and mesh networks. |
|  |  | Z-Wave |  | Wireless protocol for smart home devices and IoT. |
|  |  | NFC (Near Field Communication) |  | Short-range wireless communication for contactless payments and data exchange. |
|  | **Long-Range Wireless** | Cellular Networks (2G, 3G, 4G LTE, 5G) |  | Mobile communication technologies for voice and data. |
|  |  | LoRaWAN |  | Low-power wide-area network for IoT applications. |
|  |  | Sigfox |  | Ultra-narrowband technology for IoT communication. |
|  | **Satellite Communication** | Geostationary Satellites (GEO) |  | Satellites for global communication and broadcasting. |
|  |  | Low Earth Orbit Satellites (LEO) |  | Satellites for low-latency communication (e.g., Starlink). |
|  |  | GNSS (GPS, Galileo) |  | Satellite systems for global navigation and positioning. |
|  | **Microwave Communication** | Microwave Links |  | High-frequency wireless communication for point-to-point connections. |
| **Wired Communication** | **Ethernet and LAN** | Ethernet (IEEE 802.3) |  | Standard for wired local area networks (LANs). |
|  | **Broadband over Copper** | DSL (Digital Subscriber Line) |  | Technology for high-speed internet over telephone lines. |
|  | **Fiber Optic Communication** | Fiber Optic Networks (FTTH, OTN) |  | High-speed data transmission using light through optical fibers. |
|  | **Coaxial Cable Networks** | DOCSIS (Data Over Cable) |  | Technology for high-speed data over cable TV systems. |
|  | **Powerline Communication** | HomePlug |  | Technology for data transmission over electrical wiring. |
|  |  | [G.hn](http://g.hn/) |  | Standard for high-speed networking over power lines, phone lines, and coaxial cables. |
| **Optical Communication** | **Fiber Optics** | Single-Mode Fiber |  | Optical fiber for long-distance communication. |
|  |  | Multi-Mode Fiber |  | Optical fiber for shorter-distance communication. |
|  | **Light-Based Wireless** | Li-Fi (Light Fidelity) |  | Wireless communication using visible light for high-speed data transmission. |
|  | **Optical Amplification** | EDFA (Erbium-Doped Fiber Amplifiers) |  | Amplifiers for boosting optical signals in fiber networks. |
|  | **Wavelength Division Multiplexing** | WDM, DWDM (Dense WDM) |  | Technology for transmitting multiple data streams over a single optical fiber. |
| **Internet and Networking** | **Networking Protocols** | TCP/IP |  | Core protocols for internet communication. |
|  |  | HTTP/HTTPS |  | Protocols for web communication and secure data transfer. |
|  |  | SMTP |  | Protocol for email communication. |
|  | **Voice over IP** | VoIP (Voice over IP) |  | Technology for voice communication over the internet. |
|  |  | SIP (Session Initiation Protocol) |  | Protocol for initiating and managing VoIP sessions. |
|  | **Network Virtualization** | SDN (Software-Defined Networking) |  | Technology for flexible and programmable network management. |
|  |  | NFV (Network Function Virtualization) |  | Virtualization of network functions for scalability and efficiency. |
|  | **Content Delivery** | CDN (Content Delivery Networks) |  | Distributed networks for efficient content delivery to users. |
| **IoT and LPWAN** | **Cellular IoT** | NB-IoT (Narrowband IoT) |  | Cellular technology for low-power, wide-area IoT communication. |
|  |  | LTE-M (Long-Term Evolution for Machines) |  | Cellular technology for IoT devices with moderate data requirements. |
|  | **Non-Cellular LPWAN** | LoRaWAN |  | Low-power, wide-area network for IoT applications. |
|  |  | Sigfox |  | Ultra-narrowband technology for IoT communication. |
|  | **Short-Range IoT** | Zigbee |  | Wireless protocol for short-range IoT communication. |
|  |  | Z-Wave |  | Wireless protocol for smart home devices and IoT. |
| **Signal Processing** | **Modulation Techniques** | OFDM (Orthogonal Frequency-Division Multiplexing) |  | Technique for encoding data onto multiple carrier frequencies. |
|  |  | QAM (Quadrature Amplitude Modulation) |  | Modulation technique for high-data-rate transmission. |
|  | **Error Correction** | LDPC (Low-Density Parity-Check) |  | Error correction code for reliable data transmission. |
|  |  | Turbo Codes |  | Error correction code for high-performance communication systems. |
| **Antenna and Propagation** | **Advanced Antennas** | MIMO (Multiple Input Multiple Output) |  | Technology for improving signal strength and capacity using multiple antennas. |
|  |  | Beamforming |  | Technique for directing signals toward specific devices. |
|  |  | Phased Array Antennas |  | Antennas for steering signals electronically. |
|  | **Propagation Models** | Path Loss Models |  | Models for predicting signal attenuation over distance. |
|  |  | Multipath Fading Models |  | Models for predicting signal interference due to reflections. |
| **Emerging Technologies** | **Next-Gen Wireless** | 6G |  | Future wireless technology for ultra-high-speed communication. |
|  |  | Terahertz Communication |  | Technology for communication using terahertz frequencies. |
|  | **Quantum Communication** | Quantum Key Distribution (QKD) |  | Secure communication using quantum mechanics principles. |
|  | **Holographic Communication** | Holographic Displays |  | Technology for immersive 3D communication experiences. |
| **Telecom Infrastructure** | **Network Hardware** | Routers |  | Devices for forwarding data between networks. |
|  |  | Switches |  | Devices for connecting devices within a network. |
|  |  | Base Stations |  | Equipment for wireless communication in cellular networks. |
|  |  | Optical Transceivers |  | Devices for transmitting and receiving optical signals. |
|  | **Amplification and Repeaters** | Repeaters |  | Devices for boosting signals in wired and wireless networks. |
|  |  | Amplifiers |  | Devices for increasing signal strength. |
|  | **Network Interface Cards** | NICs (Network Interface Cards) |  | Hardware for connecting devices to networks. |
| **Telecom Security** | **Encryption** | AES (Advanced Encryption Standard) |  | Symmetric encryption algorithm for securing data. |
|  |  | RSA (Rivest-Shamir-Adleman) |  | Asymmetric encryption algorithm for secure communication. |
|  | **Network Security** | VPN (Virtual Private Network) |  | Technology for secure communication over public networks. |
|  |  | Firewalls |  | Systems for blocking unauthorized access to networks. |
|  |  | IDS (Intrusion Detection Systems) |  | Tools for detecting and preventing network attacks. |
|  | **Protocol Security** | TLS/SSL (Transport Layer Security/Secure Sockets Layer) |  | Protocols for secure communication over the internet. |
| **Telecom Software** | **Operational Support** | OSS (Operational Support Systems) |  | Software for managing and monitoring telecom networks. |
|  | **Business Support** | BSS (Business Support Systems) |  | Software for billing, customer management, and service provisioning. |
|  | **Network Management** | NMS (Network Management Systems) |  | Tools for managing network performance and troubleshooting. |
|  | **Unified Communications** | Unified Communications Platforms |  | Platforms integrating voice, video, and messaging services. |
| **Telecom Applications** | **Voice and Video** | VoIP (Voice over IP) |  | Technology for voice communication over the internet. |
|  |  | Video Conferencing (e.g., Zoom) |  | Applications for real-time video communication. |
|  | **Streaming** | Streaming Services (e.g., Netflix) |  | Platforms for delivering audio and video content over the internet. |
|  | **Cloud Communication** | Cloud Communication Platforms (e.g., Twilio) |  | Platforms for building communication applications in the cloud. |
|  | **Messaging** | Messaging Apps (e.g., WhatsApp) |  | Applications for instant messaging and file sharing. |
| **Testing and Measurement** | **Signal Analysis** | Spectrum Analyzers |  | Tools for analyzing signal quality and frequency spectrum. |
|  |  | Network Analyzers |  | Tools for analyzing network performance and traffic. |
|  | **Signal Generation** | Signal Generators |  | Devices for generating test signals for network validation. |
|  | **Protocol Analysis** | Protocol Analyzers |  | Tools for analyzing and debugging network protocols. |
|  | **Fiber Optic Testing** | OTDR (Optical Time-Domain Reflectometer) |  | Equipment for testing and troubleshooting fiber optic networks. |

## Infrastructure

## Operation

## Performance

## Security

## Standard

| **Standard** | **IEEE Number** | **Year** | **Description** |
| --- | --- | --- | --- |
| **Ethernet** | IEEE 802.3 | 1983 | A standard for wired LANs that specifies the physical and data link layer protocols for Ethernet. |
| **Wi-Fi** | IEEE 802.11 | 1997 | A family of wireless LAN standards that specify the protocols for transmitting data over radio waves. |
| **Bluetooth** | IEEE 802.15.1 | 2002 | A wireless PAN standard that specifies how devices can communicate over short distances. |
| **ZigBee** | IEEE 802.15.4 | 2003 | A low-power wireless mesh networking standard designed for home automation, industrial control, and other applications. |
| **Token Ring** | IEEE 802.5 | 1985 | A LAN standard specifies Token Ring networks' physical and data link layer protocols. |
| **Fiber Distributed Data Interface (FDDI)** | IEEE 802.6 | 1987 | A standard for fiber optic LANs that specifies the physical and data link layer protocols for FDDI networks. |
| **Transmission Control Protocol/Internet Protocol (TCP/IP)** | IEEE 802.1 | 1983 | The protocol suite used by the Internet and most LANs specifies how data is transmitted over the network and how devices communicate. |
| **Virtual LANs (VLANs)** | IEEE 802.1Q | 1998 | A standard that defines how to create VLANs, which allow multiple LANs to share the same physical network infrastructure. |
| **Simple Network Management Protocol (SNMP)** | IEEE 802.1X | 2001 | A protocol used for managing and monitoring network devices that specifies how devices can be queried and how alerts can be generated. |
| **Network Address Translation (NAT)** | IEEE 802.1N | 2006 | A standard that specifies how NAT can be used to translate private IP addresses to public IP addresses for communication over the Internet. |
| **Quality of Service (QoS)** | IEEE 802.1P | 1998 | A standard that specifies how to prioritize and manage network traffic based on the type of data being transmitted. |
| **Power over Ethernet (PoE)** | IEEE 802.3af (2003), IEEE 802.3at | 2003, 2009 | A standard that allows devices to receive power over Ethernet cables, eliminating the need for a separate power supply. |
| **Internet Protocol version 6 (IPv6)** | IEEE 802.3aq | 2006 | A standard specifies a new Internet Protocol (IP) version that supports larger address spaces and other enhancements. |
| **Wireless Personal Area Networks (WPANs)** | IEEE 802.15 | 2003 | A family of standards that specify how devices can communicate over short distances using various wireless technologies. |
| **Media Access Control (MAC)** | IEEE 802.3z | 1998 | A standard specifies how to access the physical medium in a LAN and how data is transmitted over the network. |

## Case Study Set

## QA

### What is the difference between the Control Plane and the Management Plane?

> The **Control Plane** determines how traffic should be handled, while the Management Plane determines how the network device itself is configured, monitored, and administered.
> 

> The Control Plane governs network behavior according to the configuration and policies defined by the Management Plane.
> 

### How to decide that interaction mechanism to used `SSE vs Websockets`?

> Here’s the comparison in markdown table format:
> 

| Criteria | Server-Sent Events (SSE) | WebSockets |
| --- | --- | --- |
| **Use Cases** | Server-to-Client Updates | Bidirectional Communication |
|  | Event Streaming | Low Latency |
|  | Unidirectional Data Flow | Complex Interactions |
|  | Simplicity and Ease of Use | Reduced Polling |
|  | Compatibility | Custom Protocols |
|  | Reduced Overhead | Scalability |
| **Communication Direction** | Server-to-Client | Bidirectional (Client-to-Server and Server-to-Client) |
| **Latency** | Higher latency due to one-way communication | Lower latency due to bidirectional communication |
| **Complexity** | Simpler to implement and maintain | More complex, but offers greater flexibility |
| **Use in Applications** | Event-driven architectures, notifications | Real-time chat, online gaming, interactive apps |
| **Connection Maintenance** | Single HTTP connection per client | Persistent WebSocket connection |
| **Custom Protocols** | Limited flexibility for custom protocols | Flexibility to define custom communication protocols |
| **Scalability** | Suitable for moderate-scale applications | Scalable, suitable for high-concurrency scenarios |

### What is a Dongle?

> [**Dongle](https://en.wikipedia.org/wiki/Dongle) (Adaptador):** A dongle is a small piece of computer hardware that connects to a port on another device to provide it with additional functionality, or enable a pass-through to such a device that adds functionality.
> 

### Which are the set of user objetives acomplish by telecom technical domain?

| **User Goal** | **Telecom Solution** |
| --- | --- |
| **Communication** | Enable exchange of information between people, systems, or devices through voice, text, data, or signals. |
| **Real-Time Communication** | Provide low-latency interactive communication such as voice calls, video calls, conferencing, and online collaboration. |
| **Information Access** | Provide connectivity to retrieve, publish, and consume information from remote systems and services. |
| **Data Transfer** | Move digital information reliably between distributed endpoints. |
| **Remote Interaction** | Allow users to control, operate, or interact with distant systems and devices. |
| **Content Distribution** | Deliver digital content (video, audio, files, applications) from providers to many consumers. |
| **Streaming System** | Continuously deliver time-based data streams over a network with controlled latency, buffering, and quality adaptation. |
| **Multimedia Streaming** | Deliver synchronized audio, video, and interactive media experiences over communication networks. |
| **Collaboration** | Support shared activities between distributed users through messaging, conferencing, shared systems, and collaborative platforms. |
| **Mobility** | Maintain communication while users or devices change physical location through wireless and cellular networks. |
| **Device Connectivity** | Connect machines, sensors, and embedded devices for monitoring and automation (IoT/M2M). |
| **Resource Sharing** | Allow remote users and systems to access shared computing, storage, and network resources. |
| **Transaction and Service Access** | Enable remote access to financial, commercial, governmental, and enterprise services. |
| **Presence and Awareness** | Provide information about availability, status, location, or state of users and devices. |
| **Broadcast and Mass Communication** | Distribute information from one source to many receivers (radio, television, multicast, emergency alerts). |

## References

Telecom: Conceptual Model

- [Apache APISIX](note.html?n=technica/computation/enterprise-information-system-eis/conceptual-model-enterprise-system/apache-apisix.md)
- [Berkeley Socket](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/berkeley-socket.md)
- [Linux Network Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-network-stack.md)
- [Network Interface Card (NICs)](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/network-interface-card-nics.md)
- [Sending ethernet packet to a device with a specific mac address](https://serverfault.com/questions/988050/sending-ethernet-packet-to-a-device-with-a-specific-mac-address)
- [Sending raw Ethernet frames from Python](https://csl.name/post/raw-ethernet-frames/)
- [Computer network](https://en.wikipedia.org/wiki/Computer_network)
- [1,000,000 Concurrent Connections](https://josephmate.github.io/2022-04-14-max-connections/)
- [On the Design of Application Protocols](https://www.rfc-editor.org/rfc/rfc3117.txt)
- Benvenuti, C. (2006). *Understanding Linux Network Internals*. “ O’Reilly Media, Inc.”
- [Physical Layer](https://en.wikipedia.org/wiki/Physical_layer)
- [How do I send a raw ethernet frame in python?](https://stackoverflow.com/questions/12229155/how-do-i-send-a-raw-ethernet-frame-in-python)
- Dordal, P. L. (2014). An Introduction to Computer Networks.
- Hall, B. B. (2001). [Beej’s Guide](https://beej.us/guide/bgnet/html/split/) to Network Programming: Using Internet Sockets.
- [Port forwarding (azirevpn.com)](https://news.ycombinator.com/item?id=36381181)
- [WebSockets vs Server-Sent-Events vs Long-Polling vs WebRTC vs WebTransport](https://rxdb.info/articles/websockets-sse-polling-webrtc-webtransport.html)
- [Web API](https://en.wikipedia.org/wiki/Web_API)
- [Stable APIs are a Pipe Dream](https://note89.github.io/pipe-dream/)
- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [Network Virtualization](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/network-virtualization.md)
- https://github.com/alex/what-happens-when
- https://en.wikipedia.org/wiki/Telecommunications
- [Electromagnetism](https://app.notion.com/p/Electromagnetism-ecb3d9ce10f0425a85326aa81634a0d9?pvs=21)
- [**Antenna**](note.html?n=technica/computation/telecom/telecom-conceptual-model/antenna.md)
- [Solid State Phenomena](https://app.notion.com/p/Solid-State-Phenomena-1aec0f5171ec808eb99af6ab105bb046?pvs=21)
- [**Optical Phenomena**](https://app.notion.com/p/Optical-Phenomena-1aec0f5171ec802fb93dcbff1f95a8a1?pvs=21)
- [**Acoustics P**henomena](https://app.notion.com/p/Acoustics-Phenomena-1aec0f5171ec806fb1f2e35f9adfd2fb?pvs=21)
- [Information](https://app.notion.com/p/Information-17ac0f5171ec813d813ff6055c98fe7d?pvs=21)
- [Security](https://app.notion.com/p/Security-abe7b617157f43099a19bee382dd5996?pvs=21)
- Journals
    - https://arxiv.org/list/cs.NI/recent
    - [Journal of Network and Computer Applications](https://www.sciencedirect.com/journal/journal-of-network-and-computer-applications)
    - [IEEE Transactions on Communications](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=26)
    - [IEEE/ACM Transactions on Networking](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=90)
    - [Journal of Computer Networks and Communications](https://dl.acm.org/journal/jcnc)
    - …
- Labs
    - [Communications and Networking Research Group](https://cnrg.mit.edu/)
    - https://www.microsoft.com/en-us/research/group/networking-research/
    - 
- [‣](https://app.notion.com/p/196598edb790809a8001e2e941372d87?pvs=21)
- [‣](https://app.notion.com/p/10e598edb7908137bc5dcfec66e8fc29?pvs=21)
- https://www.kegel.com/c10k.html
- https://en.wikipedia.org/wiki/VNC