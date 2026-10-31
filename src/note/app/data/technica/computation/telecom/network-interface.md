# Network Interface


> A **network interface** is a **system-level endpoint** that implements the data-plane and control-plane machinery required to send and receive packets over a specific link, exposing this capability to the OS networking stack.
> 

> It is a **software abstraction backed by (optional) hardware**, representing a **packet I/O endpoint**.
> 

Guiding questions:

- What is the role of a network interface?
- What happens if we don’t have network interfaces?
- Does each network interface represented and endpoint? Does they have **IP** assign? How the **OS** - route correctly the packages?
- What are the types of physical interfaces?  How does the physical interface - becomes a software one In Linux?
- Which others deep questions should I be asking?
- How to detect the performance limits of my NIC?
- How does the **socket abstraction** is connected - related to the NIC **physical technical object**?

## Type Space

> List network interfaces with `ipconfig`.
> 

| **Type of Network Interface** | **Description** | **Medium** | **Examples** |
| --- | --- | --- | --- |
| **Ethernet Interface** | A wired network interface using Ethernet cables for high-speed data transfer. | Wired | Ethernet NIC, RJ45 ports |
| **Wi-Fi Interface** | A wireless network interface that uses radio waves for data transmission. | Wireless | Built-in Wi-Fi adapter, USB Wi-Fi dongle |
| **Bluetooth Interface** | A short-range wireless interface for connecting peripheral devices. | Wireless | Bluetooth adapter, integrated Bluetooth in laptops and phones |
| **Cellular Interface** | A mobile network interface for connecting to cellular networks (e.g., 4G, 5G). | Wireless | SIM card slot, built-in cellular modem |
| **Virtual Network Interface** | A software-based interface used in virtualized environments for network connections. | Virtual | vNIC in virtual machines, virtual adapters |
| **Loopback Interface** | A special software-based interface used for testing and inter-process communication within the same device. | Virtual | `lo` interface, 127.0.0.1 IP address |
| **Fiber Optic Interface** | A high-speed wired interface using fiber optic cables for data transmission. | Wired | Fiber NIC, SFP ports |
| **Satellite Interface** | A wireless interface for communication via satellite links. | Wireless | Satellite modem, VSAT terminals |
| **Powerline Interface** | A wired interface using electrical wiring for network data transmission. | Wired | Powerline adapters, HomePlug |
| **Thunderbolt Interface** | A high-speed wired interface used primarily for connecting peripherals and displays, but can also support networking. | Wired | Thunderbolt ports and adapters |

## References

- https://en.wikipedia.org/wiki/Network_interface_controller
- https://jvns.ca/blog/2017/09/03/network-interfaces/
- https://news.ycombinator.com/item?id=14017683
- https://news.ycombinator.com/item?id=11995866
- https://loomcom.com/blog/understanding-the-network-interface-card/