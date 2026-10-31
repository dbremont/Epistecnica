# Data Plane


> The data plane, also known as the forwarding plane, is responsible for the actual transmission of data between network devices. It is responsible for processing and forwarding data packets, and is typically implemented in hardware.
> 

![](https://techterms.com/img/xl/multicast_946.png)

**Casting**

> Determines the number of destinations for a message sent by a source.
> 

> The `cast` references to refer to how the packet is addressed, not the medium on which the packet travels. A unicast is addressed to a single recipient, while a broadcast is addressed to every recipient. A multicast is addressed to every recipient which has subscribed to the multicast group (the destination address of the packet).
> 

There are three types of network communication protocols based on the number of recipients:

- **Unicast**: Unicast is a one-to-one communication protocol. In this type of communication, a sender transmits data to a single recipient. Examples of unicast protocols include TCP and HTTP.
- **Multicast**: Multicast is a one-to-many communication protocol. In this type of communication, a sender transmits data to a group of recipients. Multicast communication is efficient as data is sent only once and then replicated by the network to reach all group members. Examples of multicast protocols include IGMP (Internet Group Management Protocol) and PIM (Protocol Independent Multicast).
- **Broadcast**: Broadcast is a one-to-all communication protocol. In this type of communication, a sender transmits data to all devices on the network. Broadcast communication can be used for network discovery or sending urgent messages to all devices on the network. Examples of broadcast protocols include ARP (Address Resolution Protocol) and DHCP (Dynamic Host Configuration Protocol).

## References

- https://en.wikipedia.org/wiki/Data_plane