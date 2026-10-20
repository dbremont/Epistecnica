---
tags: [security]
---

# Linux Security Stack


> In this note, we will explore the **Linux Security Stack**.
> 

> Explore the security features of operating systems, including authentication, authorization, and access control. Study how the operating system manages user accounts, passwords, and file permissions, and how it defends against malware, viruses, and other security threats.
> 

## Formulation

> Security is the discipline that specifies how things *must* be (rules) and ensures that they *actually are* that way (enforcement).
> 

> **Policy Specification** The process of defining and formulating security policies to dictate how resources and information are protected.
> 

> **Auditing and Monitoring** Processes and tools that track and log security-related activities to ensure policy adherence and detect breaches.
> 

A **linux** **security triple** is a 4-tuple **(Layer, Security Object, Security Problem, Mechanism)** that expresses:

- **Layer** — the structural position within the system where protection is applied.
- **Security Object (Enforcement Points)** — the entity being protected (process, file, interface, credential, component, etc.).
- **Security Problem:  —** the threat, failure mode, or undesirable system state that must be prevented (e.g., privilege escalation, unauthorized access, code injection, tampering, data exfiltration).
- **Mechanism** — the concrete control, constraint, or enforcement technique that provides the protection.

| **Layer** | **Security Object** | **Security Problem** | **Description** | **Mechanism** |
| --- | --- | --- | --- | --- |
| **Hardware & Boot Integrity** | Firmware (UEFI/BIOS) | Firmware tampering | Attacker modifies firmware to gain persistent, pre-OS control | Secure Boot; firmware passwords |
|  |  | Unauthorized firmware rewrite | Malicious or unintended flashing of firmware components | UEFI write-protection; hardware jumpers |
| **Hardware & Boot Integrity** | Bootloader | Early-boot code injection | Attacker injects or replaces bootloader code | Signed bootloaders |
|  |  | Unverified boot chain | Boot process cannot confirm integrity of each stage | Measured Boot |
| **Hardware & Boot Integrity** | Hardware root-of-trust | Unverifiable state | Platform cannot attest to its boot integrity | TPM; PCR measurements |
| **Hardware & Boot Integrity** | Physical chassis | Direct physical intrusion | Attacker gains access to hardware for tampering or extraction | Chassis locks; tamper-evident seals |
| **Kernel Space Security** | Kernel syscall interface | Unauthorized privilege elevation | Abusing syscalls to escalate privileges | Seccomp; syscall filtering |
|  |  | Unsafe syscall exposure | Processes can access overly powerful syscalls | Seccomp profiles |
| **Kernel Space Security** | Kernel memory | Memory corruption | Bug or exploit modifies protected memory regions | KASLR; hardened memory |
|  |  | Arbitrary write | Attacker gains write access to kernel memory | Stack Canaries; SMAP/SMEP |
|  |  | ROP/JOP chains | Code-reuse attacks against kernel | Control-flow integrity protections |
| **Kernel Space Security** | Kernel modules | Unsigned module loading | Inserting untrusted kernel code | Signed modules |
|  |  | Module tampering | Modifying loaded modules or injecting malicious ones | Lockdown mode |
| **Kernel Space Security** | Kernel control logic | MAC bypass | Circumventing SELinux/AppArmor rules | SELinux; AppArmor |
| **Process Isolation** | Namespaces | Namespace breakout | Process escapes isolation boundary | PID/NET/IPC/USER/MNT namespaces |
|  |  | Unauthorized access to global resources | Process touches system-level objects | Namespace hardening |
|  | Process privileges | Excess capabilities | Process retains privileges it does not need | Linux capabilities |
|  |  | Privilege inheritance | Child processes inherit excessive privileges | NoNewPrivileges |
|  | Resource usage | Resource exhaustion | DoS via CPU/memory/file descriptor consumption | cgroups v2 |
|  | Syscall surface | Dangerous syscalls exposed | App can execute high-risk syscalls | seccomp-bpf |
| **Filesystem & Data Security** | Files & directories | Unauthorized read | Confidential data exposure | POSIX perms; ACLs |
|  |  | Unauthorized write | Integrity tampering of key files | ACLs; strict permissions |
|  | Sensitive data at rest | Offline data theft | Attacker steals disk or storage media | LUKS; fscrypt |
|  |  | Cleartext storage | Sensitive files unencrypted | fscrypt |
|  | System config files | Configuration tampering | Altering system behavior through config changes | chattr +i |
|  | Mounted untrusted FS | Malicious metadata | Exploits triggered via untrusted filesystem | noexec; nosuid; FUSE isolation |
| **Network & Boundary Protection** | Network interfaces | Unfiltered exposure | Service exposed unnecessarily to network | nftables; interface binding |
|  |  | Remote scanning | Attack surface visible externally | nftables |
|  | Packets & traffic flows | Malicious packets | Crafted packets exploit kernel or services | eBPF firewalls |
|  |  | Lateral movement | Attackers pivot internally | Firewall segmentation |
|  | Process network stacks | Unbounded connectivity | Processes connect freely to arbitrary hosts | Network namespaces |
|  | Inter-host links | MITM interception | Data stolen or altered in transit | WireGuard; IPsec |
|  |  | Cleartext transport | No encryption between nodes | IPsec |
| **Authentication & Authorization** | User identity | Weak authentication | Passwords easy to guess or phishable | PAM; MFA |
|  |  | Missing identity proof | No strong factor to tie user to identity | MFA (FIDO2/TOTP) |
|  | Remote access (SSH) | Password brute force | Repeated login attempts | SSH keys |
|  |  | Credential reuse | Using compromised credentials | Disable password login |
|  | Privilege escalation path | Misuse of sudo | Weak sudo policies allow privilege gain | Sudo least privilege |
|  | Central identity store | Policy drift | Different machines have inconsistent auth states | LDAP/Kerberos/SSSD |
|  |  | Unmanaged permissions | Stale accounts; incorrect privilege maps | Centralized directory |
| **Application-Level Security** | Application process | Overbroad system access | App touches more resources than needed | systemd sandboxing |
|  |  | Missing isolation | App affects host environment | chroot; sandboxing |
|  | Application code | Software vulnerabilities | Bugs lead to RCE or data loss | SAST; DAST; fuzzing |
|  |  | Injection surface | App accepts unsafe input | SAST; sanitization |
|  | Dependencies & libraries | Supply-chain injection | Malicious or compromised dependencies | Code signing |
|  |  | Unverified updates | Dependencies updated without integrity check | Package verification |
|  | App execution environment | Container breakout | Escape into host | Rootless containers |
| **Intrusion Detection** | Syscall activity | Hidden malicious behavior | Attacker actions not logged or monitored | Auditd; eBPF monitoring |
|  | Logs | Tampering | Attacker alters or deletes logs | Remote journald |
|  |  | Integrity loss | Logs lose trustworthiness | IMA/EVM |
|  | Critical system files | Silent modification | Attacker changes key files unnoticed | AIDE |
|  | Runtime events | Anomaly undetected | Unknown behavior escapes monitoring | Falco; SIEM |
| **Patch & Supply Chain** | Kernel | Unpatched vulnerabilities | Exploits due to old kernel | Livepatch |
|  |  | Upgrade downtime | Need to reboot causes lag in patching | Live kernel patching |
|  | Packages | Repository spoofing | Malicious packages impersonate real ones | GPG-verified repos |
|  |  | Dependency compromise | Attack via software supply chain | Package signing |
|  | System components | Open CVEs | Known issues left unresolved | CVE scanning |
|  | OS base image | Hidden modifications | Drift from golden image | Immutable OS |
| **Virtualization & Cloud** | Virtual machines | VM escape | Guest escapes into host | KVM protections |
|  |  | Hypervisor attack | Exploiting hypervisor bugs | Hardware virtualization |
|  | VM access labels | Cross-VM access bypass | Break MAC policy for VMs | sVirt + SELinux |
|  | MicroVM workloads | Excessive attack surface | Traditional VMs too large | Firecracker |
|  | Container network | Traffic leakage | Containers see traffic they should not | VRF; VLAN; VXLAN |
|  | Container privileges | Privilege breakout | Root container becomes host root | Rootless containers; user namespaces |

## Linux Security Stack Structure

> The Linux Security Stack encompasses a range of security modules and tools designed to safeguard the Linux operating system by managing access controls, enforcing policies, and monitoring security-related events.
> 

| **Component** | **Description** | **Tag(s)** |
| --- | --- | --- |
| **SELinux (Security-Enhanced Linux)** | A kernel-level Mandatory Access Control (MAC) system that enforces strict, label-based security policies to control how processes and objects interact. Provides fine-grained isolation beyond traditional UNIX permissions. | MAC; Policy Enforcement; Kernel Security |
| **AppArmor** | A profile-based MAC system that restricts program behavior using per-application rules. Simpler than SELinux, focused on confining applications rather than full system labeling. | MAC; Application Confinement |
| **Seccomp (Secure Computing Mode)** | Restricts the set of Linux system calls a process can invoke, minimizing its attack surface. Often used in sandboxed environments and containers. | Syscall Filtering; Sandboxing |
| **Linux Capabilities** | Splits traditional root privileges into discrete units (capabilities) that can be individually granted or removed from processes, reducing the risk of privilege escalation. | Least Privilege; Privilege Model |
| **Auditd** | Kernel-aided auditing daemon for logging and tracking security-significant events (syscalls, file changes, authentication, policy violations). Critical for forensics and compliance. | Auditing; Logging; Forensics |
| **Firewall (iptables/nftables)** | Packet filtering and network control frameworks for implementing firewalls, routing rules, NAT, and traffic shaping. nftables is the modern replacement. | Network Filtering; Boundary Protection |
| **PAM (Pluggable Authentication Modules)** | A unified authentication framework that allows flexible integration of authentication mechanisms (passwords, keys, MFA, biometrics). | Authentication; Identity |
| **Cgroups (Control Groups)** | Kernel feature for limiting, accounting, and isolating CPU, memory, I/O, and other resources per process or container. First line of defense against resource exhaustion. | Resource Control; Isolation |
| **eBPF (Extended Berkeley Packet Filter)** | Safe, JIT-compiled kernel execution sandbox for dynamic tracing, monitoring, filtering, and security enforcement. Used by Falco, Cilium, Tracee. | Observability; Kernel Extension; Security Monitoring |
| **Filesystem Permissions (POSIX ACLs, ownership model)** | Enforces read/write/execute permissions on files and directories. Performed by the kernel on every access via system calls like `open()`, `read()`, `write()`, and `exec()`. | Access Control; Filesystem Security |
| **AIDE (Advanced Intrusion Detection Environment)** | A file-integrity monitoring system that detects unexpected modifications to critical files by comparing against a cryptographic baseline. | Integrity Monitoring; FIM |
| **Polkit (PolicyKit)** | A system service for controlling system-level privilege elevation requests outside the traditional UNIX user model. Used heavily by desktop and system services. | Authorization; Privilege Escalation Control |
| **IMA/EVM (Integrity Measurement Architecture)** | Kernel integrity-checking frameworks that verify file content and metadata using cryptographic signatures to prevent tampering. | Integrity; Secure Boot Chain |
| **App Sandbox Tools (systemd sandboxing)** | systemd options (`PrivateTmp`, `ProtectSystem`, `NoNewPrivileges`, etc.) used to restrict application filesystem, namespace, and privilege access without containers. | Application Isolation; Hardening |
| **LUKS/dm-crypt** | Kernel-backed encryption for block devices, protecting data at rest through full-disk or partition encryption. | Encryption; Data-at-Rest Security |
| **Containers (rootless, user namespaces)** | Lightweight isolation using cgroups, namespaces, seccomp, and capabilities, providing strong app confinement with no privileged access. | Isolation; Sandboxing; Multi-tenancy |
| **Audit Rules + Syscall Hooks** | Kernel filtering rules attached to auditd for fine-grained syscall monitoring, violation detection, and compliance enforcement. | Monitoring; Enforcement |
| **Kernel Lockdown Mode** | Prevents userspace from modifying the kernel, disabling certain debug interfaces and enforcing stricter code-loading rules. | Kernel Hardening; Attack Surface Reduction |

## File Permisions(s)

![image.png](data/technica/computation/operating-system/linux/conceptual-model-linux/assets/linux-security-stack/image.png)

## Linux Security Tool(s)

> 
- SSH
- GnuPG
- OpenSSL
- **XCA (X Certificate and Key Management)**
- [KeyStore Explorer](https://keystore-explorer.org/): Tool to manage PKI in Java.

## References

- [CPU Modes](https://en.wikipedia.org/wiki/CPU_modes)
- [Protection Ring](https://en.wikipedia.org/wiki/Protection_ring)
- https://wiki.archlinux.org/title/Polkit
- https://wiki.archlinux.org/title/Security
- [Public Key Infrastructure (PKI)](https://app.notion.com/p/Public-Key-Infrastructure-PKI-231c0f5171ec804dab54dc561a00b492?pvs=21)
- https://en.wikipedia.org/wiki/System_Security_Services_Daemon
- https://en.wikipedia.org/wiki/Address_space_layout_randomization