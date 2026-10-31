---
tags: [computer-network, standard]
---

# Ethernet

- [Open Systems Interconnection (OSI) Model](note.html?n=technica/computation/telecom/open-systems-interconnection-osi-model.md), [Wire Data Transmission](note.html?n=technica/computation/telecom/wire-data-transmission.md)

> **Ethernet** is a deterministic, contention-based, **packet-switched** networking technology defined by the IEEE 802.3 standard, operating at the data link (Layer 2) and physical (Layer 1) layers of the OSI model, utilizing MAC addresses for frame addressing, Carrier Sense Multiple Access with Collision Detection (CSMA/CD) for medium access control in half-duplex mode, and supporting full-duplex operation with switch-based point-to-point links.
> 

> **Ethernet** is a family of evolving **IEEE 802.3** standards that define **wired networking technologies** for **LANs**, continuously updated to support higher speeds, new transmission media, and enhanced communication methods while maintaining interoperability with earlier versions.
> 

> Ethernet is a family of **frame-based networking technologies** standardized under the IEEE 802.3 series, primarily used for **Local Area Networks (LANs)**. It defines the physical and data link layers of the OSI model, enabling devices to communicate over a shared or switched medium.
> 

QA:

- Is there any relation between **Ethernet** and **WIFI**?
- Which are the set of technologies tha tpower the Ethernet Standard?

## **Ethernet Standards**

> Ethernet has evolved over decades, with various standards supporting different speeds and media:
> 

| Standard | Speed | Media | Description |
| --- | --- | --- | --- |
| **10BASE-T** | 10 Mbps | Twisted Pair (Cat3) | Early Ethernet standard. |
| **100BASE-TX** | 100 Mbps | Twisted Pair (Cat5) | Fast Ethernet. |
| **1000BASE-T** | 1 Gbps | Twisted Pair (Cat5e/Cat6) | Gigabit Ethernet. |
| **10GBASE-T** | 10 Gbps | Twisted Pair (Cat6a/Cat7) | 10 Gigabit Ethernet. |
| **40GBASE-SR4** | 40 Gbps | Fiber Optic | 40 Gigabit Ethernet. |
| **100GBASE-LR4** | 100 Gbps | Fiber Optic | 100 Gigabit Ethernet. |

## **Ethernet Frame Structure**

> The Ethernet frame is the fundamental unit of data transmission in Ethernet networks. It consists of the following fields:
> 

| Field | Size (Bytes) | Description |
| --- | --- | --- |
| **Preamble** | 7 | A sequence of alternating 1s and 0s (10101010...) for synchronization. |
| **Start Frame Delimiter (SFD)** | 1 | Marks the start of the frame (10101011). |
| **Destination MAC Address** | 6 | The hardware address of the intended recipient. |
| **Source MAC Address** | 6 | The hardware address of the sender. |
| **EtherType/Length** | 2 | Indicates the protocol type (e.g., IPv4, IPv6) or the length of the payload. |
| **Payload/Data** | 46–1500 | The actual data being transmitted (e.g., IP packet). |
| **Frame Check Sequence (FCS)** | 4 | A CRC-32 checksum for error detection. |

## **MAC Addressing**

- Each Ethernet device has a unique **Media Access Control (MAC) address**, a 48-bit identifier typically represented in hexadecimal (e.g., `00:1A:2B:3C:4D:5E`).
- The first 24 bits are the **Organizationally Unique Identifier (OUI)**, assigned by the IEEE.
- The last 24 bits are assigned by the manufacturer.

## **Ethernet Physical Layer**

Ethernet operates over various physical media, including:

- **Coaxial Cable** (obsolete, used in early Ethernet standards like 10BASE5 and 10BASE2).
- **Twisted Pair Cable** (e.g., Cat5e, Cat6, Cat7 for 100BASE-TX, 1000BASE-T, etc.).
- **Fiber Optic Cable** (e.g., 10GBASE-SR, 40GBASE-LR4 for high-speed and long-distance links).

## **Encoding and Signaling**

- Ethernet uses **line coding** schemes to encode data for transmission:
    - **Manchester Encoding** (used in 10BASE-T).
    - **4B/5B Encoding** (used in 100BASE-TX).
    - **8B/10B Encoding** (used in Gigabit Ethernet).
    - **64B/66B Encoding** (used in 10 Gigabit Ethernet and beyond).

## **Ethernet Topologies**

- **Bus Topology**: Early Ethernet used a shared coaxial cable (e.g., 10BASE5).
- **Star Topology**: Modern Ethernet uses switches or hubs to connect devices in a star configuration.
- **Point-to-Point**: Direct links between two devices (common in fiber Ethernet).

## **Ethernet Protocols**

- **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**:
    - Used in half-duplex Ethernet to detect and recover from collisions.
    - Devices listen to the medium before transmitting and retransmit if a collision is detected.
    - Largely obsolete in modern full-duplex Ethernet.
- **Auto-Negotiation**:
    - Allows devices to automatically select the highest common speed and duplex mode (e.g., 100 Mbps full-duplex).

## **Ethernet Switching**

- **Switches** operate at Layer 2 (Data Link Layer) and use MAC addresses to forward frames to the correct port.
- **MAC Address Table**: Switches maintain a table mapping MAC addresses to ports for efficient forwarding.
- **VLANs (Virtual LANs)**: Switches can segment networks into multiple broadcast domains using VLAN tagging (IEEE 802.1Q).

## **Ethernet Extensions**

- **Jumbo Frames**: Frames larger than 1500 bytes (up to 9000 bytes) for improved efficiency in high-throughput networks.
- **Power over Ethernet (PoE)**: Delivers power alongside data over Ethernet cables (IEEE 802.3af/at/bt).
- **Ethernet in the First Mile (EFM)**: Extends Ethernet to wide-area networks (WANs).

## **Ethernet in the OSI Model**

- **Physical Layer (Layer 1)**: Defines the electrical, mechanical, and functional specifications for the physical medium.
- **Data Link Layer (Layer 2)**: Handles framing, MAC addressing, and error detection.

## **Ethernet Performance**

- **Latency**: Typically low, but depends on network congestion and switch performance.
- **Throughput**: Ranges from 10 Mbps to 400 Gbps (and beyond with emerging standards).
- **Reliability**: High, with error detection (FCS) and collision avoidance mechanisms.

## References

- https://en.wikipedia.org/wiki/Ethernet