---
tags: [initialization]
---

# Init System

- [initrd](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/initrd.md)

> 

Here is a table of various init systems, which are responsible for booting the system and managing services:

| **Init System** | **Description** | **Key Features** | **Default in** |
| --- | --- | --- | --- |
| **SysVinit** | One of the earliest init systems used in UNIX and Linux, based on scripts executed at different runlevels. | - Simple and traditional <br> - Script-based <br> - Sequential startup | Older Linux distributions (e.g., Debian, CentOS) |
| **systemd** | A modern init system and service manager for Linux, designed to replace SysVinit with a dependency-based model. | - Parallel startup <br> - Unified system management <br> - Socket-based activation <br> - Extensive logging | Most modern Linux distributions (e.g., Ubuntu, Fedora, Arch) |
| **Upstart** | An event-based replacement for SysVinit, developed by Canonical for Ubuntu. | - Event-driven <br> - Parallel startup <br> - Dynamic management of services | Ubuntu (before 15.04) |
| **OpenRC** | A dependency-based init system that works with existing init scripts from other systems like SysVinit. | - Compatible with SysVinit scripts <br> - Dependency-based <br> - Parallel service startup | Gentoo, Alpine Linux |
| **runit** | A minimal and fast init system, providing service supervision and reliable service management. | - Fast startup <br> - Process supervision <br> - Simple configuration | Void Linux, Artix Linux |
| **s6** | A small and secure init system focused on simplicity and service supervision. | - Process supervision <br> - Modular design <br> - Fast and lightweight | [Skarnet.org](http://skarnet.org/), Alpine Linux (optional) |
| **BSD init** | The traditional init system used in BSD operating systems. | - Simple and traditional <br> - Script-based | FreeBSD, OpenBSD |
| **launchd** | A unified service management framework for macOS and iOS, combining features of init, cron, and inetd. | - Service management <br> - On-demand service startup <br> - Process monitoring | macOS, iOS |

## References

- https://en.wikipedia.org/wiki/Init
- https://en.wikipedia.org/wiki/Daemon_(computing)