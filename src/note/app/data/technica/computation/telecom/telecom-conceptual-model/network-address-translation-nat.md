---
tags: [internetworking]
---

# Network Address Translation (NAT)

- [Network Connectivity](note.html?n=technica/computation/telecom/telecom-conceptual-model/network-connectivity.md)

> **Network Address Translation (NAT)** is a packet translation mechanism in which a network device rewrites the IP addresses, and optionally the transport-layer port numbers, of packets as they traverse the device, enabling communication between different IP address domains.
> 

## `(Behavior)` What does NAT Do?

NAT performs the following operations:

1. **Intercepts packets passing through the NAT device:** Receives packets from an internal or external network.
2. **Rewrites packet addresses:** Changes the source or destination IP address; Optionally changes transport-layer ports (TCP/UDP ports).
3. **Maintains a translation state:** Stores a mapping between internal and external address/port pairs.
4. **Uses the mapping to translate return traffic:** Incoming packets matching an existing translation entry are rewritten and forwarded to the correct internal host.

## References

- https://en.wikipedia.org/wiki/Network_address_translation