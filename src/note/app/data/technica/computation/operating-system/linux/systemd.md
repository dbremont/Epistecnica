---
tags: [initialization]
---

# Systemd


> A **system** and **service manager** that handles the boot process, system services, and management of daemons.
> 

> In systemd, the grand unifying abstraction is the concept of a **"unit,"** which represents a resource or service, such as a system service, a mount point, a device, or a socket, and is managed consistently through systemd's control interfaces, enabling unified and flexible management of various system components.
> 

Guiding Questions:

- Which are the usual units  - services that comones by default with ubuntu?

![](https://upload.wikimedia.org/wikipedia/commons/3/35/Systemd_components.svg)

## Taxonomy of Units

Here is a table of different types of systemd units, which are the fundamental building blocks used to manage various aspects of a Linux system:

| **Unit Type** | **File Extension** | **Description** | **Key Functions** |
| --- | --- | --- | --- |
| **Service Unit** | `.service` | Manages services (daemons) that run continuously or on-demand. | - Start, stop, and manage background services <br> - Handles long-running processes (e.g., web servers, databases) |
| **Socket Unit** | `.socket` | Manages inter-process communication sockets, usually used to start services on-demand. | - Defines network or IPC sockets <br> - Automatically starts associated services when a socket is accessed |
| **Target Unit** | `.target` | Represents a group of units to be started or stopped together, similar to runlevels in SysVinit. | - Group units for a particular system state (e.g., `multi-user.target`, `graphical.target`) |
| **Device Unit** | `.device` | Manages kernel devices recognized by `udev`. | - Tracks and manages hardware devices <br> - Used for handling device availability and dependencies |
| **Mount Unit** | `.mount` | Controls mount points for filesystems. | - Automates mounting of filesystems <br> - Manages mount points defined in `/etc/fstab` |
| **Automount Unit** | `.automount` | Manages mount points that are automatically mounted on access. | - Triggers the mounting of a filesystem when it is accessed |
| **Swap Unit** | `.swap` | Manages swap space on the system. | - Handles enabling and disabling swap partitions or swap files |
| **Path Unit** | `.path` | Monitors file or directory changes and triggers actions. | - Watches paths and starts associated services when changes are detected |
| **Timer Unit** | `.timer` | Schedules and runs services based on time or intervals, similar to cron jobs. | - Schedules tasks to run at specific times or intervals <br> - Replaces traditional cron jobs |
| **Slice Unit** | `.slice` | Organizes and manages groups of system processes (cgroups). | - Defines resource boundaries for processes <br> - Helps in resource allocation and limitation |
| **Scope Unit** | `.scope` | Manages externally created processes. | - Groups processes started outside of systemd, allowing for resource management |
| **Snapshot Unit** | n/a | Represents a saved state of running services and units. | - Captures and restores the state of units <br> - Used for system recovery and debugging |

## List of Components

> Ubuntu, like most Linux distributions, runs various daemons (background services) to perform essential system tasks and provide various functionalities.
> 

 Some of the main daemons that you may find running on an Ubuntu system include:

1. **systemd:** The system and service manager that initializes the system during boot, manages services, and handles process management.
2. **NetworkManager:** Manages network connections, including wired, wireless, and VPN configurations.
3. **sshd:** The OpenSSH server daemon responsible for enabling remote secure shell (SSH) access to the system.
4. **cron:** The cron daemon that runs scheduled tasks and commands at specified intervals.
5. **rsyslogd:** The system logging daemon responsible for collecting, processing, and forwarding log messages.
6. **avahi-daemon:** Implements Zeroconf networking, allowing automatic service discovery on local networks.
7. **cupsd:** The Common Unix Printing System daemon for managing print jobs and printer configurations.
8. **apport:** The daemon that intercepts application crashes and generates crash reports.
9. **snapd:** The daemon responsible for managing Snap packages, a form of application packaging on Ubuntu.
10. **polkitd:** The PolicyKit daemon that handles authentication and authorization for privileged tasks.
11. **ModemManager:** Manages mobile broadband (cellular) connections and modems.
12. **upowerd:** Monitors power-related events and provides power management functionality.
13. **bluetoothd:** The Bluetooth daemon responsible for managing Bluetooth devices and connections.
14. **avahi-daemon:** Implements Zeroconf networking, allowing automatic service discovery on local networks.
15. **thermald:** Monitors thermal sensors and manages thermal policies to prevent overheating.

## Clients

- https://askubuntu.com/questions/1030850/is-there-a-gui-tool-for-managing-systemd-on-ubuntu-18-04-bionic-beaver
- systemctl
- https://github.com/KDE/systemdgenie
- …

## References

- https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html - .Service File Spec
- https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files
- https://systemd.io/
- https://serverfault.com/questions/867322/what-is-the-difference-between-service-and-systemctl
- https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units
- https://wiki.archlinux.org/title/Systemd
- https://github.com/systemd/systemd
- https://xeiaso.net/talks/systemd-the-good-parts-2021-05-16/
- https://github.com/systemd/systemd/blob/main/docs/HACKING.md
- https://wiki.archlinux.org/title/Mkosi
- https://skarnet.com/projects/service-manager.html
- https://systemd-by-example.com/
- https://blog.darknedgy.net/technology/2020/05/02/0/