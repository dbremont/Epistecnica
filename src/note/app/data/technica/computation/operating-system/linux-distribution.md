# Linux Distribution

> A **Linux distribution** is an integrated, versioned operating-system software stack that combines the **Linux kernel** with a user-space environment—such as a C library, system utilities, init/service manager, shells, package-management and repository infrastructure, security mechanisms, configuration defaults, and application software—under a defined **build, release, update, and governance model** to produce a deployable computing environment.
> 

## How to Characterize the Linux Distribution Space?

> Linux distributions are not a homogeneous set of operating systems. They differ along multiple, partially independent axes, including system architecture, package management, release model, configuration, security, target environment, and governance. Characterizing the Linux distribution space therefore requires identifying the major **parameter types** along which distributions vary, and the specific **parameters** that describe each type of variation.
> 

The methodology for characterizing the Linux distribution space is as follows:

- **Parameter Type** → a major dimension along which distributions vary.
- **Parameter** → a specific characteristic within that dimension.
- **Parameter Description** → an explanation of what the parameter represents.
- **Value Set** → the possible values that parameter can take.

### Parameter Space

| Parameter Type | Description | Parameter Set |
| --- | --- | --- |
| **Origin** | Historical and technical lineage of the distribution | Parent distribution, ancestry, derivation |
| **Architecture** | Hardware platforms supported by the distribution | ISA, CPU architecture, platform |
| **Kernel** | Kernel environment provided by the distribution | Kernel, variant, configuration |
| **Userspace** | Core user-space software environment | C library, shell, core utilities |
| **Interface** | Mechanisms through which users interact with the operating system | Interaction model, desktop environment, graphical stack |
| **Packaging** | Mechanisms for distributing and managing software | Package format, package manager, repository model |
| **Lifecycle** | Model governing releases, updates, and support | Release model, update model, support model |
| **Execution** | Mechanisms governing system initialization and service execution | Init system, service manager, supervision model |
| **Security** | Mechanisms governing protection and isolation | Access control, MAC, sandboxing, capabilities |
| **Target** | Intended environment and purpose of the distribution | Desktop, server, cloud, embedded, container |
| **Governance** | Organizational structure responsible for development and maintenance | Community, foundation, corporation, governance model |

### Distribution Space

| Parameter Type | Parameter | Parameter Description | Value Set |
| --- | --- | --- | --- |
| **Origin** | Parent Distribution | Distribution from which it is derived | Debian, Arch, Fedora, independent, etc. |
| ↳ | Ancestry | Historical lineage of the distribution | Upstream → derivative → fork |
| ↳ | Derivation | Relationship to its upstream distribution | Derivative, fork, independent |
| **Architecture** | Instruction Set | CPU instruction sets supported | x86-64, ARM64, RISC-V, etc. |
| ↳ | Platform | Hardware platforms explicitly supported | PC, server, SBC, embedded, etc. |
| **Kernel** | Kernel | Kernel implementation | Linux |
| ↳ | Kernel Variant | Kernel variant or distribution-specific implementation | Mainline, LTS, hardened, real-time, etc. |
| ↳ | Kernel Configuration | Distribution's kernel configuration strategy | Generic, optimized, modular, minimal, etc. |
| **Userspace** | C Library | Primary system C library | glibc, musl, uClibc, etc. |
| ↳ | Shell | Default system shell | Bash, Dash, BusyBox ash, Zsh, etc. |
| ↳ | Core Utilities | Fundamental user-space utilities | GNU Coreutils, BusyBox, BSD utilities, etc. |
| **Interface** |  Desktop Environment          |  Default or principal integrated graphical desktop environment    |  GNOME, KDE Plasma, Xfce, LXQt, Cinnamon, MATE, none, etc.  |
|  ↳               |  Window Manager * Compositor  |  Component responsible for window management and/or compositing   |  Mutter, KWin, Xfwm, Openbox, Sway, Hyprland, etc.          |
|  ↳               |  Display Protocol             |  Protocol used by the graphical session                           |  Wayland, X11, both                                         |
|  ↳               |  Display Server               |  System component providing graphical display services            |  X.Org Server, Wayland compositor, etc.                     |
|  ↳               |  GUI Toolkit                  |  Primary toolkit used by graphical applications                   |  GTK, Qt, Tk, Electron, etc.                                |
|  ↳               |  Display Manager              |  Component responsible for graphical login and session selection  |  GDM, SDDM, LightDM, greetd, none                           |
|  ↳               |  Graphical Shell              |  User-facing graphical shell/interface layer                      |  GNOME Shell, KDE Plasma Shell, etc.                        |
|  ↳               |  Default Interface            |  Default interaction modality provided by the distribution        |  CLI, TUI, GUI, CLI + GUI                                   |
| **Security** | Access Control | Mechanisms governing access to system resources | DAC, MAC, RBAC, capabilities |
| ↳ | Mandatory Access Control | Mandatory security policy framework | SELinux, AppArmor, SMACK, none |
| ↳ | Isolation | Mechanisms for separating processes and workloads | Namespaces, containers, sandboxing |
| **Target** | Primary Environment | Environment for which the distribution is principally designed | Desktop, server, cloud, embedded |
| ↳ | Deployment Context | Typical deployment context | Bare metal, VM, container, appliance |
| ↳ | Use Case | Principal intended application | General purpose, security, networking, development, etc. |
| **Governance** | Organization | Organizational entity responsible for the distribution | Community, foundation, corporation, consortium |
| ↳ | Decision Model | How technical decisions are made | Benevolent dictator, committee, community, corporate |
| ↳ | Development Model | How development is organized | Community-driven, corporate-driven, hybrid |

### Value Description

| Parameter Type | Parameter | Value | Value Description |
| --- | --- | --- | --- |
| **Origin** | **Parent Distribution** | Debian | Distribution serving as the direct upstream foundation. |
| ↳ | ↳ | Arch | Arch Linux serves as the direct upstream foundation. |
| ↳ | ↳ | Fedora | Fedora serves as the direct upstream foundation. |
| ↳ | ↳ | Independent | No other Linux distribution serves as the direct upstream foundation. |
| **Origin** | **Ancestry** | Upstream → derivative | Historical lineage in which the distribution inherits substantial technical components from an upstream distribution. |
| ↳ | ↳ | Upstream → fork | Historical lineage in which the project diverged from an upstream project and developed independently. |
| ↳ | ↳ | Independent | No direct upstream Linux-distribution ancestor. |
| **Origin** | **Derivation** | Derivative | Distribution substantially based on an existing upstream distribution. |
| ↳ | ↳ | Fork | Distribution that diverged from an upstream project and subsequently developed under independent control. |
| ↳ | ↳ | Independent | Distribution developed independently rather than as a derivative of another Linux distribution. |
| **Architecture** | **Instruction Set** | x86-64 | 64-bit x86 instruction-set architecture. |
| ↳ | ↳ | ARM64 | 64-bit ARM/AArch64 instruction-set architecture. |
| ↳ | ↳ | RISC-V | RISC-V instruction-set architecture. |
| ↳ | ↳ | Multi-architecture | Distribution supporting multiple instruction-set architectures as first-class targets. |
| **Architecture** | **Platform** | PC | General-purpose personal-computer hardware platform. |
| ↳ | ↳ | Server | General-purpose server hardware platform. |
| ↳ | ↳ | SBC | Single-board computer and similar compact computing platform. |
| ↳ | ↳ | Embedded | Specialized or resource-constrained hardware platform. |
| **Kernel** | **Kernel** | Linux | Linux is used as the operating-system kernel. |
| **Kernel** | **Kernel Variant** | Mainline | Kernel closely tracking the upstream Linux kernel. |
| ↳ | ↳ | LTS | Kernel based on a Linux long-term-support branch. |
| ↳ | ↳ | Hardened | Kernel modified or configured to strengthen security properties. |
| ↳ | ↳ | Real-time | Kernel configured or patched to provide stronger deterministic scheduling and latency characteristics. |
| **Kernel** | **Kernel Configuration** | Generic | General-purpose configuration intended to provide broad hardware and workload compatibility. |
| ↳ | ↳ | Optimized | Configuration tuned for a particular workload, platform, or hardware class. |
| ↳ | ↳ | Minimal | Configuration containing only functionality considered necessary for the target system. |
| ↳ | ↳ | Modular | Configuration in which significant functionality is provided through loadable kernel modules. |
| **Userspace** | **C Library** | glibc | GNU C Library used as the primary system C library. |
| ↳ | ↳ | musl | Lightweight C library emphasizing simplicity, standards orientation, and static linking. |
| ↳ | ↳ | uClibc | Lightweight C library designed primarily for resource-constrained systems. |
| **Userspace** | **Shell** | Bash | GNU Bourne Again Shell used as the system's principal shell. |
| ↳ | ↳ | Dash | Lightweight POSIX-compatible shell derived from the Almquist shell family. |
| ↳ | ↳ | BusyBox ash | Lightweight shell implementation provided by BusyBox. |
| ↳ | ↳ | Zsh | Feature-rich interactive shell providing extended scripting and completion facilities. |
| **Userspace** | **Core Utilities** | GNU Coreutils | GNU implementations of fundamental Unix command-line utilities. |
| ↳ | ↳ | BusyBox | Compact multi-call binary providing many standard Unix utilities. |
| ↳ | ↳ | BSD utilities | Core utilities originating from the BSD operating-system tradition. |
| **Interface** | **Desktop Environment** | GNOME | Integrated graphical desktop environment providing the principal desktop experience and associated components. |
| ↳ | ↳ | KDE Plasma | Integrated graphical desktop environment providing the Plasma desktop experience and associated components. |
| ↳ | ↳ | Xfce | Lightweight integrated graphical desktop environment emphasizing low resource consumption. |
| ↳ | ↳ | LXQt | Lightweight Qt-based graphical desktop environment. |
| ↳ | ↳ | Cinnamon | Graphical desktop environment providing a conventional desktop interaction model. |
| ↳ | ↳ | MATE | Graphical desktop environment providing a traditional desktop interaction model. |
| ↳ | ↳ | None | No integrated desktop environment is provided as the principal graphical environment. |
| **Interface** | **Window Manager / Compositor** | Mutter | Window manager and compositor used by GNOME to manage application windows and graphical composition. |
| ↳ | ↳ | KWin | Window manager and compositor used by KDE Plasma to manage windows and graphical composition. |
| ↳ | ↳ | Xfwm | Window manager used by Xfce for X11 window management and composition. |
| ↳ | ↳ | Openbox | Lightweight X11 window manager providing window management without requiring a full desktop environment. |
| ↳ | ↳ | Sway | Wayland compositor implementing a tiling window-management model. |
| ↳ | ↳ | Hyprland | Wayland compositor providing dynamic tiling and graphical composition. |
| **Interface** | **Display Protocol** | Wayland | Display protocol through which graphical clients communicate with a Wayland compositor. |
| ↳ | ↳ | X11 | Display protocol used by graphical applications to communicate with an X server. |
| ↳ | ↳ | Both | Supports both Wayland and X11 graphical sessions. |
| **Interface** | **Display Server** | X.Org Server | X11 display server providing graphical display services to X11 clients. |
| ↳ | ↳ | Wayland compositor | Compositor providing the display functionality for a Wayland graphical session. |
| **Interface** | **GUI Toolkit** | GTK | Graphical user-interface toolkit used to construct graphical applications and interface components. |
| ↳ | ↳ | Qt | Cross-platform graphical application framework and toolkit. |
| ↳ | ↳ | Tk | Lightweight graphical user-interface toolkit. |
| ↳ | ↳ | Electron | Desktop application framework based on Chromium and web technologies. |
| **Interface** | **Display Manager** | GDM | Graphical display manager providing graphical login and session management. |
| ↳ | ↳ | SDDM | Graphical display manager providing login and graphical session selection. |
| ↳ | ↳ | LightDM | Lightweight display manager providing graphical login and session management. |
| ↳ | ↳ | greetd | Minimal login and session-management daemon. |
| ↳ | ↳ | None | No graphical display manager is provided or enabled by default. |
| **Interface** | **Graphical Shell** | GNOME Shell | User-facing graphical shell providing the primary GNOME interaction layer. |
| ↳ | ↳ | KDE Plasma Shell | User-facing graphical shell providing the primary KDE Plasma interaction layer. |
| **Interface** | **Default Interface** | CLI | Command-line interface is the principal default interaction modality. |
| ↳ | ↳ | TUI | Terminal-based text interface is the principal default interaction modality. |
| ↳ | ↳ | GUI | Graphical user interface is the principal default interaction modality. |
| ↳ | ↳ | CLI + GUI | Both command-line and graphical interfaces are provided as principal interaction modalities. |
| **Packaging** | **Package Format** | `.deb` | Debian binary package format used to distribute prebuilt software packages. |
| ↳ | ↳ | `.rpm` | RPM binary package format used to distribute prebuilt software packages. |
| ↳ | ↳ | `.pkg.tar` | Arch Linux package archive format. |
| ↳ | ↳ | `.apk` | Alpine Linux package archive format. |
| ↳ | ↳ | Source | Software is distributed primarily as source code for local or distribution-controlled construction. |
| **Packaging** | **Package Manager** | APT | Package-management system used to resolve, install, upgrade, and remove Debian packages. |
| ↳ | ↳ | DNF | Package-management system used to manage RPM packages and resolve dependencies. |
| ↳ | ↳ | Pacman | Package-management system used to manage Arch package archives and repositories. |
| ↳ | ↳ | Portage | Package-management system used by Gentoo to manage software builds, dependencies, and installations. |
| ↳ | ↳ | Zypper | Package-management system used to manage RPM packages and repositories in the SUSE ecosystem. |
| ↳ | ↳ | tce | Tiny Core package-management mechanism for installing and managing Tiny Core extensions. |
| **Packaging** | **Repository Model** | Binary / centralized | Software is primarily distributed as prebuilt binaries through centrally maintained repositories. |
| ↳ | ↳ | Source-based | Software is primarily obtained as source and built according to distribution or local configuration. |
| ↳ | ↳ | Binary | Software is distributed primarily as prebuilt binary packages. |
| **Lifecycle** | **Release Model** | Fixed | Produces discrete releases with defined versions and release boundaries. |
| ↳ | ↳ | Rolling | Continuously updates the installed system without requiring periodic major-version replacement. |
| ↳ | ↳ | Point-release | Produces discrete releases within a broader release series or major version. |
| **Lifecycle** | **Update Model** | Periodic | Software updates are delivered according to defined release or update cycles. |
| ↳ | ↳ | Continuous | Software updates are continuously integrated into the active distribution. |
| **Execution** | **Init System** | systemd | Uses systemd as the primary system initialization and service-management framework. |
| ↳ | ↳ | OpenRC | Uses OpenRC as the primary system initialization and service-management framework. |
| ↳ | ↳ | BusyBox init | Uses the BusyBox `init` implementation as the primary initialization mechanism. |
| **Execution** | **Service Manager** | systemd | Uses systemd to manage system services, dependencies, startup, and service lifecycle. |
| ↳ | ↳ | OpenRC | Uses OpenRC to manage service startup, shutdown, and service state. |
| ↳ | ↳ | BusyBox | Uses BusyBox-provided mechanisms for basic system and process initialization. |
| **Security** | **Access Control** | DAC | Access to resources is primarily controlled through discretionary permissions associated with resource ownership. |
| ↳ | ↳ | MAC | Access is constrained by centrally defined mandatory security policies. |
| ↳ | ↳ | RBAC | Permissions are organized around roles assigned to users or processes. |
| ↳ | ↳ | Capabilities | Traditional superuser privileges are divided into fine-grained process capabilities. |
| **Security** | **Mandatory Access Control** | SELinux | Mandatory access control is enforced through SELinux security policies. |
| ↳ | ↳ | AppArmor | Mandatory access control is enforced through AppArmor application profiles. |
| ↳ | ↳ | SMACK | Mandatory access control is implemented through SMACK security labels and policies. |
| ↳ | ↳ | None | No dedicated mandatory access-control framework is provided by default. |
| **Security** | **Isolation** | Namespaces | Kernel namespaces isolate process views of system resources. |
| ↳ | ↳ | Containers | Operating-system-level isolation mechanisms are used to separate workloads. |
| ↳ | ↳ | Sandboxing | Explicit restrictions are used to limit application access to system resources or capabilities. |
| **Target** | **Primary Environment** | Desktop | Distribution is principally designed for interactive personal-computing workloads. |
| ↳ | ↳ | Server | Distribution is principally designed for persistent network services and server workloads. |
| ↳ | ↳ | Cloud | Distribution is principally designed for cloud infrastructure and dynamically provisioned workloads. |
| ↳ | ↳ | Embedded | Distribution is principally designed for dedicated or resource-constrained devices. |
| **Target** | **Deployment Context** | Bare metal | Intended to run directly on physical hardware. |
| ↳ | ↳ | VM | Intended to run as a guest operating system within a virtual machine. |
| ↳ | ↳ | Container | Intended to provide a userspace environment for containerized workloads. |
| ↳ | ↳ | Appliance | Intended to provide a specialized, purpose-built computing environment. |
| **Target** | **Use Case** | General purpose | Designed to support a broad range of computing workloads. |
| ↳ | ↳ | Security | Specialized for security assessment, penetration testing, digital forensics, or related security operations. |
| ↳ | ↳ | Networking | Specialized for network infrastructure and network-service workloads. |
| ↳ | ↳ | Development | Optimized for software development and engineering workflows. |
| **Governance** | **Organization** | Community | Development and maintenance are primarily organized by a community of contributors. |
| ↳ | ↳ | Foundation | Development and governance are organized under a formal foundation structure. |
| ↳ | ↳ | Corporation | A commercial organization has primary organizational responsibility for the distribution. |
| ↳ | ↳ | Consortium | Multiple organizations jointly participate in development or governance. |
| **Governance** | **Decision Model** | Benevolent dictator | Major technical decisions are ultimately controlled by a principal project maintainer or leader. |
| ↳ | ↳ | Committee | Major decisions are made through a designated committee or governing group. |
| ↳ | ↳ | Community | Technical decisions are primarily made through community processes and contributor consensus. |
| ↳ | ↳ | Corporate | Major technical and strategic decisions are primarily controlled by a corporation. |
| **Governance** | **Development Model** | Community-driven | Development is primarily organized and performed by community contributors. |
| ↳ | ↳ | Corporate-driven | Development is primarily directed and resourced by a commercial organization. |
| ↳ | ↳ | Hybrid | Development combines substantial community participation with organizational or corporate direction. |

## Distribution Space

| Distribution | Description | Technical Characterization (Parameter Type -  Parameter) |
| --- | --- | --- |
| **Debian** | Community-developed, general-purpose Linux distribution emphasizing stability, broad architecture support, and a large software repository. | **Parent Distribution:** Independent
**Derivation:** Independent
**Instruction Set:** x86-64, ARM64, RISC-V, etc.
**Kernel:** Linux
**Kernel Variant:** Mainline / LTSC**C 
Library:** glibc
**Shell:** Bash
**Core Utilities:** GNU Coreutils
**Package Format:** `.deb`
**Package Manager:** APT
**Repository Model:** Binary / centralized
**Release Model:** Fixed
**Update Model:** Periodic
**Init System:** systemd
**Access Control:** DAC
**Mandatory Access Control:** AppArmor / SELinux
**Primary Environment:** General purpose
**Deployment Context:** Bare metal / VM / container
**Organization:** Community
**Decision Model:** Community
**Development Model:** Community-driven |
| **Fedora** | Community-driven Linux distribution sponsored by Red Hat, serving as an upstream platform for technologies later incorporated into the Red Hat ecosystem. | Parent Distribution: Independent
Derivation: Independent
Instruction Set: x86-64, ARM64, etc.
Kernel: Linux
Kernel Variant: Mainline
C Library: glibc
Shell: Bash
Core Utilities: GNU Coreutils
Package Format: .rpm
Package Manager: DNF
Repository Model: Binary / centralized
Release Model: Fixed
Update Model: Periodic
Init System: systemd
Access Control: DAC
Mandatory Access Control: SELinux
Primary Environment: Desktop / server / cloud
Deployment Context: Bare metal / VM / cloud
Organization: Community / corporation
Decision Model: Community / corporate
Development Model: Community-driven / corporate-driven |
| **Ubuntu** | Debian-derived distribution developed by Canonical and oriented toward accessible desktop, server, cloud, and general-purpose computing. | Parent Distribution: Debian
Derivation: Derivative
Instruction Set: x86-64, ARM64, etc.
Kernel: Linux
Kernel Variant: Mainline / LTSC
C Library: glibc
Shell: Bash
Core Utilities: GNU Coreutils
Package Format: .deb
Package Manager: APT
Repository Model: Binary / centralized
Release Model: Fixed / point-release
Update Model: Periodic
Init System: systemd
Access Control: DAC
Mandatory Access Control: AppArmor
Primary Environment: Desktop / server / cloud
Deployment Context: Bare metal / VM / cloud / container
Organization: Corporation / community
Decision Model: Corporate
Development Model: Hybrid |
| **Gentoo** | Independently developed distribution emphasizing configurability, source-based software construction, and fine-grained control over the installed system. | Parent Distribution: Independent
Derivation: Independent
Instruction Set: x86-64, ARM64, etc.
Kernel: Linux
Kernel Variant: Configurable
C Library: glibc / musl
Shell: Bash
Core Utilities: GNU Coreutils
Package Format: Source
Package Manager: Portage
Repository Model: Source-based
Release Model: Rolling
Update Model: Continuous
Init System: OpenRC / systemd
Access Control: DAC
Primary Environment: General purpose / development
Deployment Context: Bare metal / VM / container
Organization: Community
Decision Model: Community
Development Model: Community-driven |
| Kali Linux | Debian-derived distribution specialized for penetration testing, digital forensics, security assessment, and related security operations. | Parent Distribution: Debian
Derivation: Derivative
Instruction Set: x86-64, ARM64, etc.
Kernel: Linux
Kernel Variant: Mainline / LTSC
C Library: glibc
Shell: Bash
Core Utilities: GNU Coreutils
Package Format: .deb
Package Manager: APT
Repository Model: Binary / centralized
Release Model: Rolling
Update Model: Continuous
Init System: systemd
Access Control: DAC
Mandatory Access Control: AppArmor
Primary Environment: Security
Deployment Context: Bare metal / VM / container
Organization: Community / corporation
Development Model: Corporate-driven / community |
| openSUSE | Linux distribution associated with the SUSE ecosystem, providing both a stable release model and a rolling-release variant for desktop, server, and development workloads. | Parent Distribution: SUSE lineage
Derivation: Derivative / independent lineage
Instruction Set: x86-64, ARM64, etc.
Kernel: Linux
Kernel Variant: Mainline / LTSC
C Library: glibc
Shell: Bash
Core Utilities: GNU Coreutils
Package Format: .rpm
Package Manager: Zypper
Repository Model: Binary / centralized
Release Model: Fixed / rolling
Update Model: Periodic / continuous
Init System: systemd
Access Control: DAC
Mandatory Access Control: AppArmor
Primary Environment: Desktop / server
Deployment Context: Bare metal / VM / cloud
Organization: Community / corporation
Decision Model: Community / corporate
Development Model: Hybrid |
| Arch Linux | Independently developed, minimalist Linux distribution emphasizing simplicity, user control, current software, and a rolling-release model. | Parent Distribution: Independent
Derivation: Independent
Instruction Set: x86-64
Kernel: Linux
Kernel Variant: Mainline
C Library: glibc
Shell: Bash
Core Utilities: GNU Coreutils
Package Format: .pkg.tar
Package Manager: Pacman
Repository Model: Binary / centralized
Release Model: Rolling
Update Model: Continuous
Init System: systemd
Access Control: DAC
Primary Environment: General purpose
Deployment Context: Bare metal / VM / container
Organization: Community
Decision Model: Community
Development Model: Community-driven |
| Rocky Linux | Community-maintained enterprise Linux distribution designed to provide binary compatibility with Red Hat Enterprise Linux and target production server workloads. | Parent Distribution: RHEL
Derivation: Derivative
Instruction Set: x86-64, ARM64, etc.
Kernel: Linux
Kernel Variant: LTSC
C Library: glibc
Shell: Bash
Core Utilities: GNU Coreutils
Package Format: .rpm
Package Manager: DNF
Repository Model: Binary / centralized
Release Model: Fixed
Update Model: Periodic
Init System: systemd
Access Control: DAC
Mandatory Access Control: SELinux
Primary Environment: Server / cloud
Deployment Context: Bare metal / VM / cloud
Organization: Community
Decision Model: Community
Development Model: Community-driven |
| Tiny Core Linux | Extremely small Linux distribution designed to provide a minimal operating environment with a modular userspace and very low resource requirements. | Parent Distribution: Independent
Derivation: Independent
Instruction Set: x86 / ARM
Kernel: Linux
Kernel Variant: Minimal
C Library: musl / glibc, depending on edition
Shell: BusyBox ash
Core Utilities: BusyBox
Package Format: Tiny Core packages
Package Manager: tce
Repository Model: Binary
Release Model: Rolling
Update Model: Continuous
Init System: BusyBox init
Access Control: DAC
Primary Environment: Minimal / embedded / desktop
Deployment Context: Bare metal / VM
Organization: Community
Decision Model: Community
Development Model: Community-driven |

## QA

### How to see the display manager of my Distro?

> The display manger - will depen don
> 

```bash
cat /etc/X11/default-display-manager
```

### How the security works in Linux Distro?

> 

## References

[Debian](note.html?n=technica/computation/operating-system/linux-distribution/debian.md)

[Fedora](note.html?n=technica/computation/operating-system/linux-distribution/fedora.md)

[Ubuntu](note.html?n=technica/computation/operating-system/linux-distribution/ubuntu.md)

[Gentoo](note.html?n=technica/computation/operating-system/linux-distribution/gentoo.md)

[Kali Linux](note.html?n=technica/computation/operating-system/linux-distribution/kali-linux.md)

[openSUSE](note.html?n=technica/computation/operating-system/linux-distribution/opensuse.md)

[Arch Linux](note.html?n=technica/computation/operating-system/linux-distribution/arch-linux.md)

[Rocky Linux](note.html?n=technica/computation/operating-system/linux-distribution/rocky-linux.md)

[Alpine Linux](note.html?n=technica/computation/operating-system/linux-distribution/alpine-linux.md)

[Tiny Core Linux](note.html?n=technica/computation/operating-system/linux-distribution/tiny-core-linux.md)

- [Linux](note.html?n=technica/computation/operating-system/linux.md)
- https://www.kernel.org/
- [Hyprland](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/hyprland.md)
- [Linux Security Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-security-stack.md)