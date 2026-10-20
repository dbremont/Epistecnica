# Arch Linux

> **Arch Linux** is an independently developed, x86-64–oriented Linux distribution based on a **minimal, rolling-release architecture** that provides a lightweight userspace and a comparatively unopinionated system base, with software distributed primarily through **`pacman`** and the **Arch User Repository (AUR)**; its design emphasizes **simplicity, modularity, transparency, user-controlled system composition, upstream-aligned packaging, and continuous package evolution**, leaving the selection and configuration of the kernel, init system, desktop environment, services, filesystem, networking stack, and other system components largely to the administrator.
> 

Actual questions:

- What is the meaning of installing a OS?

## Characterization

| Parameter Type | Parameter | Arch Linux |
| --- | --- | --- |
| **Origin** | Parent Distribution | **Independent** |
| ↳ | Ancestry | **Independent** |
| ↳ | Derivation | **Independent** |
| **Architecture** | Instruction Set | **x86-64** |
| ↳ | Platform | **PC** |
| **Kernel** | Kernel | **Linux** |
| ↳ | Kernel Variant | **Mainline** |
| ↳ | Kernel Configuration | **Generic** |
| **Userspace** | C Library | **glibc** |
| ↳ | Shell | **Bash** |
| ↳ | Core Utilities | **GNU Coreutils** |
| **Interface** | Desktop Environment | **None** |
| ↳ | Window Manager / Compositor | **None** |
| ↳ | Display Protocol | **None by default** |
| ↳ | Display Server | **None by default** |
| ↳ | GUI Toolkit | **None by default** |
| ↳ | Display Manager | **None by default** |
| ↳ | Graphical Shell | **None by default** |
| ↳ | Default Interface | **CLI** |
| **Packaging** | Package Format | **`.pkg.tar` / `.pkg.tar.zst`** |
| ↳ | Package Manager | **Pacman** |
| ↳ | Repository Model | **Binary / centralized** |
| **Lifecycle** | Release Model | **Rolling** |
| ↳ | Update Model | **Continuous** |
| **Execution** | Init System | **systemd** |
| ↳ | Service Manager | **systemd** |
| **Security** | Access Control | **DAC** |
| ↳ | Mandatory Access Control | **None by default** |
| ↳ | Isolation | **Namespaces / sandboxing available** |
| **Target** | Primary Environment | **General purpose / Desktop / Server** |
| ↳ | Deployment Context | **Bare metal / VM / Container** |
| ↳ | Use Case | **General purpose / Development** |
| **Governance** | Organization | **Community** |
| ↳ | Decision Model | **Community** |
| ↳ | Development Model | **Community-driven** |

## Installation & Configuration

> After doing [How to installed `Arch Linux` with `QEMU`?](note.html?n=technica/computation/operating-system/linux-distribution/arch-linux.md).
> 

Two paths:

- https://wiki.archlinux.org/title/Archinstall
- https://wiki.archlinux.org/title/Installation_guide

System conditions:

- **Boot Firmware:** **BIOS (SeaBIOS)** — QEMU's default firmware for this configuration. — [How to installed `Arch Linux` with `QEMU`?](note.html?n=technica/computation/operating-system/linux-distribution/arch-linux.md).
- **Bootloader (Booting Software):** **GRUB** — a BIOS-compatible bootloader used to load the Arch Linux kernel.
- **Partition Table:** **MBR (DOS)** — the partitioning scheme used for the BIOS-based installation.
- **Root Filesystem:** **ext4** — mounted as `/`.
- **Kernel:** **Linux** — installed by `pacstrap`.
- **Distribution:** **Arch Linux**.
- **Virtualization:** **QEMU**, using the `q35` machine type.

Manual Process:

- `localectl list-keymaps` → list available console keyboard layouts
    - `localectl status` → show the current locale and keyboard configuration
    - `loadkeys us` → load the `us` keyboard layout
- `ip link` → list network interfaces
- `iwctl` → configure Wi-Fi
- `ping archlinux.org` → verify network connectivity
- `timedatectl set-ntp true` → enable network time synchronization
- `lsblk` → list storage devices and partitions
- `cfdisk /dev/sda` → partition the disk using an MBR/DOS partition table
- `mkfs.ext4 /dev/sda1` → create the root filesystem
- `mount /dev/sda1 /mnt` → mount the root filesystem
- `pacstrap -K /mnt base linux linux-firmware` → install the base Arch system
- `genfstab -U /mnt >> /mnt/etc/fstab` → generate the filesystem mount configuration
- `arch-chroot /mnt` → enter the installed system
- `ln -sf /usr/share/zoneinfo/America/Santo_Domingo /etc/localtime` → configure the time zone
- `hwclock --systohc` → synchronize the hardware clock
- `vim /etc/locale.gen` → select locales to generate
- `locale-gen` → generate the selected locales
- `echo "LANG=en_US.UTF-8" > /etc/locale.conf` → configure the system locale
- `echo "KEYMAP=us" > /etc/vconsole.conf` → configure the persistent console keyboard layout
- `echo "archlinux" > /etc/hostname` → configure the hostname
- `passwd` → set the root password
- `useradd -m -G wheel -s /bin/bash <username>` → create a user
- `passwd <username>` → set the user's password
- `visudo` → configure `sudo`
- `systemctl enable NetworkManager` → enable NetworkManager at boot
- `pacman -S amd-ucode` → install AMD CPU microcode
- `pacman -S grub` → install GRUB
- `grub-install --target=i386-pc /dev/sda` → install GRUB for BIOS
- `grub-mkconfig -o /boot/grub/grub.cfg` → generate the GRUB configuration
- `exit` → leave the chroot
- `umount -R /mnt` → unmount the installed system
- `reboot` → reboot into Arch Linux

### Graphical Stack Installation & Configuration

- How to tell the user land (process manager - systemd, or whaterver) - to bypass - the display manager - and call the window manager?
- Does systemd start the display manager? What happens if systemd starts multiple display managers? How can we move from one session to the other?
- How a terminal works? How pty works? How vt (virtual terminal) works?
- How to switch from vts? How to list them? `Ctrl+Alt+F1`.
- What is a logging session?
- What is the difference between VTY and PTY?
- Where can I see the kernel's `init` parameter, and how does it determine which program becomes PID 1?
- How does a process respond to a keyboard command? When we press a key sequence, how are the processes that will receive the input selected?

```bash
I Kind of like this flow - its the most principle one.

systemd
   │
   ▼
TTY/login
   │
   ▼
Hyprland
```

## QA

### How to installed `Arch Linux` with `QEMU`?

```bash
## Let's assuem that we have QEMU.

mkdir -p ~/vms/arch/{iso,vm}
cd ~/vms/arch/iso

curl -LO https://geo.mirror.pkgbuild.com/iso/latest/archlinux-x86_64.iso

## In vm
cd ~/vms/arch/vm
qemu-img create -f qcow2 arch.qcow2 30G

## Start the Arch Linux installer
cd ~/vms/arch/vm
qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=arch.qcow2,format=qcow2 \
    -cdrom  ~/vms/arch/iso/archlinux-x86_64.iso \
    -nic user,model=e1000 \
    -boot order=d
```

### **Which tools are used to configure Wi-Fi, WLAN, and Ethernet controllers in Linux?**

| **Task** | **Description** | **Tool** |
| --- | --- | --- |
| **Discover PCI/PCIe controller** | Enumerate and inspect PCI/PCIe devices and their drivers | `lspci` |
| **Load controller driver** | Load or unload the kernel module associated with a controller | `modprobe` |
| **Configure network interface** | Configure link state, IP addresses, and routing | `ip` |
| **Configure Wi-Fi** | Configure and inspect 802.11 wireless parameters | `iw` |
| **Manage Wi-Fi connections** | Manage Wi-Fi networks, authentication, association, and connection profiles through the `iwd` subsystem | iwctl |
| **Configure Wi-Fi authentication** | Authenticate and associate with wireless networks | `wpa_supplicant` |
| **Configure Ethernet controller** | Inspect and configure Ethernet link parameters, offloads, and statistics | `ethtool` |
| **Manage network connections** | High-level configuration and management of Wi-Fi and Ethernet connections | `nmcli` |

### Which networking control subsystems exist in Linux, and how are they divided between the kernel and user space?

| **Layer** | **Networking control subsystem** | **Primary Role** | **Interaction Interface** |
| --- | --- | --- | --- |
| **Kernel** | **Net core** | Fundamental networking stack: sockets, packets, namespaces, routing, protocol dispatch | `socket()`, `netlink`, `/proc`, `/sys` |
| **Kernel** | **Protocol stacks** | Implement networking protocols | TCP/IP, UDP, IPv4/IPv6, ARP, ICMP, etc. |
| **Kernel** | **Network device subsystem** | Represents and controls network interfaces | `net_device`, rtnetlink |
| **Kernel** | **Network drivers** | Control Ethernet/Wi-Fi hardware | NIC drivers, `cfg80211`, driver-specific APIs |
| **Kernel** | **Wireless subsystem** | Common kernel framework for WLAN devices | `cfg80211`, `mac80211` |
| **Kernel** | **Traffic control (TC)** | Queuing, shaping, scheduling, filtering, packet classification | `tc`, netlink |
| **Kernel** | **Netfilter** | Packet filtering, NAT, connection tracking | nftables/iptables interfaces |
| **Kernel** | **XDP/eBPF** | Programmable packet processing and observability | eBPF/XDP |
| **Kernel** | **Network namespaces** | Isolate network stacks/interfaces/routing tables | `ip netns` |
| **User space** | **iproute2** | General Linux networking configuration | `ip`, `tc`, `ss`, `bridge` |
| **User space** | **Wireless management** | Configure WLAN devices, associations, regulatory settings, etc. | `iw`, `wpa_supplicant` |
| **User space** | **Network management** | Manage interfaces, addresses, routes, DNS, connections | NetworkManager, `systemd-networkd` |
| **User space** | **Firewall management** | Configure kernel packet-filtering rules | `nft`, `iptables` |
| **User space** | **DHCP / IP configuration** | Acquire/configure network parameters | `dhclient`, `dhcpcd`, NetworkManager |
| **User space** | **DNS management** | Resolver configuration and DNS services | `systemd-resolved`, `resolvectl` |

### What is the difference between a locale and a keymap?

> 

### **What is the relationship between disk partitioning, firmware, and the bootloader?**

> The **disk partitioning defines the storage structure that the firmware and bootloader use during the boot process**. The firmware determines how the system starts and, depending on the boot mode, locates the bootloader differently. With **UEFI**, the firmware looks for a bootloader executable in the **EFI System Partition (ESP)**, which must be a FAT-formatted partition. With **BIOS**, the firmware loads bootloader code from the disk's boot sector, and the bootloader then locates the operating-system files.
> 

### What is an storage device? What does lsblk does?

> 

### What does it mean to mount a filesystem? What exactly is being attached to what—the filesystem, the block device containing it, or the filesystem namespace?

> 

### What is the used of the term session?

- ps → kernel process sessions (SID)
- loginctl → systemd/logind user sessions

### What is the used of the term user?

> 

### How to parse ‘ /etc/passwd ‘?

> 

## References

- https://archlinux.org/
- https://wiki.archlinux.org/title/Installation_guide
- https://wiki.archlinux.org/title/List_of_applications
- https://wiki.archlinux.org/title/General_recommendations
- https://gist.github.com/mjkstra/96ce7a5689d753e7a6bdd92cdc169bae
- [QEMU (Quick Emulator)](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/qemu-quick-emulator.md)
- [**Interconnect**](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/interconnect.md)
- https://wiki.archlinux.org/title/Iwd
- https://wiki.archlinux.org/title/Installation_guide
- https://wiki.osdev.org/OVMF
- [File System](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/file-system.md)
- [Booting (Initialization)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/booting-initialization.md)
- [**Boot Firmware Subsystem**](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/boot-firmware-subsystem.md)
- [Linux Graphics Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-graphics-stack.md)
- [**TTY Subsystem**](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/tty-subsystem.md)