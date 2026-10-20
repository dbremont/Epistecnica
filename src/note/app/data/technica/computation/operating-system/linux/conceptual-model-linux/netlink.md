---
tags: [network]
---

# Netlink

- [Linux Network Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-network-stack.md)

> Netlink is a communication protocol in the Linux kernel that provides an interface between the kernel and user-space processes for managing networking-related tasks. It allows user-space applications to send and receive messages to and from the kernel, facilitating interactions with various networking subsystems such as routing, network configuration, and firewall management. Netlink supports different protocol families, each designed for specific purposes, such as `NETLINK_ROUTE` for routing and interface management, `NETLINK_INET_DIAG` for socket diagnostics, and more. This flexibility enables developers to create robust networking applications that can communicate directly with the kernel and handle various network events efficiently.
> 

> Netlink is often described as an ioctl() replacement. It aims to replace fixed-format C structures as supplied to ioctl() with a format which allows an easy way to add or extended the arguments.
> 

## References

- https://www.kernel.org/doc/html/v6.1/userspace-api/netlink/intro.html
- https://en.wikipedia.org/wiki/Netlink