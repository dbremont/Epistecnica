---
tags: [note]
---

# A Guide to Build & Debug the Linux Kernel


> Goals: Build and Debug the Linux Kernel + OS/Distro.
> 

> Task: `3c6e68a1-262f-4038-9aa1-04a100680718`.
> 

> Path:  `19018e8f-5c5d-44ad-ba02-7965e082bd29`.
> 

> Note: So Many Failed Paths; Look in https://github.com/csiglab/append-only-incomming-work/tree/main/details for more.
> 

Reflection:

> Reflection:  I have tried math paths; with each path I have learned more stuff;  I have improved and reflect on my workflow (modifying the logging system) to account for a better task model (the tree and sequence based tasks); and log more detail have them. It’s hard; but the only way to become stronger is with tackling problems of increasing difficulty that expand and improve your circle of competence.
> 

> "The configuration is highly complex. Try using a minimal config file instead. My initial attempt at a `<<tabula rasa>>` approach didn't succeed.”
> 

QA:

- How to know my current kernel  version?  `uname -r.`
- Which tools I have tried?`virt-make-fs`, …
- Where are the kernel requirements? `cat Documentation/process/changes.rst`
- Where is my kernel configuration (Ubuntu)? `/boot/config-xxxxx...`

## Index

## Configuration

> …
> 

| **Category** | **Command** | **Description** |
| --- | --- | --- |
| **Configuration** | `make menuconfig` | Open a terminal-based menu for configuring the kernel. |
|  | `make xconfig` | Open a graphical menu (requires Qt libraries). |
|  | `make nconfig` | Improved `menuconfig` with better UI. |
|  | `make oldconfig` | Update `.config` while keeping old choices. |
|  | `make olddefconfig` | Like `oldconfig`, but auto-selects defaults. |
|  | `make defconfig` | Use the default configuration for the target architecture. |
|  | `make allmodconfig` | Enable all possible modules (`m`). |
|  | `make allyesconfig` | Enable everything (`y`) that can be built-in. |
|  | `make allnoconfig` | Disable all features. |
|  | `make randconfig` | Generate a random kernel configuration. |
|  | `make localmodconfig` | Enable only the modules currently loaded. |
|  | `make savedefconfig` | Save current config as ./defconfig (minimal config) |
| **Building** | `make` | Compile the kernel using `.config`. |
|  | `make -j$(nproc)` | Build using all CPU cores (faster compilation). |
|  | `make bzImage` | Build the compressed kernel image (`arch/x86/boot/bzImage`). |
|  | `make modules` | Compile only kernel modules. |
|  | `make modules_install` | Install compiled modules to `/lib/modules/$(uname -r)`. |
|  | `make install` | Install the kernel (may overwrite the existing one). |
| **Cleaning** | `make clean` | Remove compiled objects but keep configuration. |
|  | `make mrproper` | Remove all build files **including** `.config`. |
|  | `make distclean` | Like `mrproper`, but also removes backup files. |
| **Debugging** | `make help` | Show all available `make` targets. |
|  | `make V=1` | Show full compiler commands for debugging. |
|  | `make W=1` | Show extra warnings. |
|  | `make -k` | Keep compiling even if errors occur. |

## Building

> …
> 

```bash
## Dependencies
sudo apt update
sudo apt install qemu-system-x86 qemu-utils gdb build-essential libncurses-dev bison flex libssl-dev libelf-dev git debootstrap

## Use The Build Configurationof my Distro's Kernel
uname -a

## Download Kernel
wget https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.11.10.tar.gz
tar -xvzf linux-6.11.10.tar.gz

## Config
cp /boot/... .config
make nconfig

## 
scripts/config --disable CONFIG_SYSTEM_TRUSTED_KEYS
scripts/config --disable CONFIG_SYSTEM_REVOCATION_KEYS

make nconfig

## Build
make -j$(nproc --ignore 2)
```

## Running

> I Failed / Need to Change Strategy
> 

> The `CONFIG_SQUASHFS=m` setting in the Linux kernel configuration means that **SquashFS support is compiled as a module** (`m`) rather than being built directly into the kernel (`y`).
 This can cause issues when trying to mount a root filesystem from an 
initramfs that uses SquashFS, because the kernel cannot load the module 
at boot time without access to the root filesystem.
> 

> `CONFIG_SQUASHFS=y`
> 

```bash
 qemu-system-x86_64 \
  -kernel arch/x86/boot/bzImage \
  -append "console=ttyS0 root=/dev/sda nokaslr"\
  -drive file=image/bullseye.img,format=raw\
  -net user,hostfwd=tcp::10021-:22 -net nic \
  -nographic \
  -m 2G \
  -s \
  -S
```

## Debug

```bash
gdb vmlinux
target remote localhost:1234
b start_kernel
```

## Build Artifacts

> Here’s a table of common **Linux build artifacts** produced during the kernel or user-space software build process. These artifacts are generated as part of compiling and linking programs, libraries, and kernel modules, and they can serve different purposes depending on the build configuration.
> 

| **Artifact** | **Description** | **Common Location** |
| --- | --- | --- |
| **`vmlinuz`** | The Linux kernel image (compressed). This is the final bootable kernel file used by the bootloader (e.g., GRUB). | Typically in `arch/x86/boot/` |
| **`vmlinux`** | Uncompressed Linux kernel image, contains debugging symbols (larger than `vmlinuz`). Useful for debugging with GDB or other tools. | Typically in the root build directory |
| **`bzImage`** | Compressed Linux kernel image, optimized for booting. This is usually the image used by bootloaders (e.g., GRUB) for systems. | Typically in `arch/x86/boot/` |
| **`System.map`** | A symbol map of the kernel, listing the addresses of kernel functions and variables. Useful for kernel debugging. | Typically in the root build directory |
| **`config`** | Kernel configuration file used to define which features and modules are included in the build (e.g., `make menuconfig` generates this file). | Typically in the root build directory |
| **`.config`** | A file that stores the kernel configuration settings, which define what modules and features are enabled or disabled in the kernel. | Root directory (in case of `make` or `make menuconfig`) |
| **`modules`** | Kernel modules or object files (`*.ko`), which are loadable extensions to the kernel, typically used for hardware drivers and other kernel features. | `lib/modules/<version>/` |
| **`modules.dep`** | A dependency file for kernel modules, listing the dependencies between kernel modules for correct loading order. | `lib/modules/<version>/` |
| **`initrd.img`** | Initial RAM disk image used for booting the system before the root filesystem is available. Typically created by `mkinitrd` or `dracut`. | `/boot/` |
| **`dts` / `dtb`** | Device tree source (`dts`) and device tree blob (`dtb`) files, describing hardware in a device-independent manner for ARM-based or other non-x86 systems. | `arch/arm/boot/dts/` |
| **`ld` (Linker Output)** | Object files (`*.o`) produced by the compiler during the build process. These are later linked to form executables or kernel modules. | Typically in the `obj/` directory in the build tree |
| **`Makefile`** | The file containing instructions for the build process. It defines build targets, dependencies, and commands for compiling and linking. | Root directory |
| **`build`** | Intermediate build directory where various build artifacts like object files and temporary output files are stored during the kernel compilation process. | Inside the root build directory |
| **`core`** | Core dumps, produced when a program crashes, containing the program's memory image. Useful for post-mortem debugging. | Typically in the current working directory |
| **`tarball`** | A compressed archive of the source code and build artifacts (e.g., `.tar.gz`). Often created for distribution or packaging. | Typically the root or source directory |
| **`pkg-config`** | Configuration data for external libraries that provide information about installed libraries (such as flags for linking). | Typically in `/usr/lib/pkgconfig/` or similar |
| **`.debug`** | Directory containing debug symbols for programs, usually generated by the build system to facilitate debugging. | `/usr/lib/debug/` |
| **`elf` files** | Executable and Linkable Format files, typically produced for user-space applications. These are the actual compiled binaries. | Typically in `/bin/`, `/sbin/`, `/usr/bin/` |
| **`depmod`** | The `depmod` command generates dependency files for kernel modules. These describe the dependencies between modules so that the correct modules are loaded in order. | `lib/modules/<version>/` |
| **`module.symvers`** | This file contains the symbols exported by the kernel modules and is used for ensuring compatibility between modules and the kernel. | `lib/modules/<version>/` |
| **`squashfs`** | A compressed read-only file system typically used in embedded or live systems. It is often the root file system for these environments. | `/boot/` or custom locations like `/mnt` |
| **`build-id`** | A unique identifier embedded in the ELF binary during the build, useful for distinguishing between different versions of a binary. | Part of the executable file or `/usr/lib/debug/` |
| **`log`** | Build logs or system logs produced during the build or runtime process. Useful for tracking errors or status during compilation. | Typically in `build.log` or `/var/log/` |
| **`obj`** | Intermediate object files created during the build process that are later linked to form the final kernel or application. | Typically in the `obj/` directory in the build tree |
|  |  |  |

## CONFIG_SYSTEM_TRUSTED_KEYS

> `CONFIG_SYSTEM_TRUSTED_KEYS` is a Linux kernel configuration option related to cryptographic key management, specifically for verifying signed kernel modules, firmware, and other security-sensitive components.
> 

Uses:

- **Secure Boot & Module Signing**: Ensures that only signed kernel modules can be loaded, preventing unauthorized code execution.
- **Firmware Validation**: Verifies signed firmware before allowing it to run in the system.
- **UEFI Secure Boot Integration**: Can include keys from the UEFI firmware's database of trusted keys.

Meaning:

- This option specifies a file containing a list of **public keys** that the kernel will consider **trusted** at boot time.
- These keys are used primarily for verifying **signed kernel modules** and other cryptographic validations.
- If set to an empty string (`""`), no additional trusted keys are added, and only built-in keys (like those from UEFI Secure Boot or compiled into the kernel) are used.

Typical Values:

- A path to a key file (e.g., `"certs/signing_key.pem"`).
- An empty string (`""`), meaning no additional keys beyond the default built-in keys.
- `builtin_trusted_keys`, meaning only the keys compiled into the kernel will be used.

## CONFIG_SYSTEM_REVOCATION_KEYS

> `CONFIG_SYSTEM_REVOCATION_KEYS` is a Linux kernel configuration option that defines a list of **revoked cryptographic keys**. These are public keys that the kernel should no longer trust for verifying signed modules, firmware, or other security-sensitive operations.
> 

Meaning:

- This option points to a file containing a list of **revoked keys**.
- The revoked keys are added to the **kernel’s revocation keyring** (`.system_revoked_keys`).
- Any certificates signed by these keys will be **rejected** by the kernel.

Practical Use Cases:

1. **Revoking Compromised Keys**: If a private key used for signing modules gets leaked, you can revoke the corresponding public key.
2. **UEFI Secure Boot Integration**: If a key previously trusted by the system is later deemed untrustworthy, it can be added to the revocation list.
3. **Enforcing Security Policies**: Organizations can use this to prevent outdated or unauthorized module signatures.

Typical Values:

- A path to a file containing revoked certificates (e.g., `"certs/revocation.pem"`).
- An empty string (`""`), meaning no additional revocations beyond those built into the kernel.

## References

- [qemu-system-x86_64 ](https://app.notion.com/p/qemu-system-x86_64-1a8c0f5171ec80acaf30e1f5cc9ddd04?pvs=21)
- [GDB (GNU Project Debugger)](https://app.notion.com/p/GDB-GNU-Project-Debugger-3599c5c295d0469eaf23ed27d2e79a47?pvs=21)
- [Debug](https://app.notion.com/p/Debug-8fa8c6ebb4974f91b6b9e6a683610b58?pvs=21)
- https://www.linuxfromscratch.org/blfs/view/svn/postlfs/initramfs.html
- https://www.youtube.com/watch?v=asnXWOUKhTA
- [initrd](https://app.notion.com/p/initrd-1a8c0f5171ec80708cb0ecddd27cb41c?pvs=21)
- [**initramfs**](https://app.notion.com/p/initramfs-1aac0f5171ec80c3b1bdc7c5a10d525d?pvs=21)
- [ELF (Executable and Linkable Format)](https://app.notion.com/p/ELF-Executable-and-Linkable-Format-4c1f82af902b453395724ee43854d2bd?pvs=21)
- [GCC : GNU Compiler Collection](https://app.notion.com/p/GCC-GNU-Compiler-Collection-81de263588f8499c8479ddd729a4c045?pvs=21)
- [C Language](https://app.notion.com/p/C-Language-8655c4697ccf46dab526d2c63f25652c?pvs=21)
- https://linuxconfig.org/in-depth-howto-on-linux-kernel-configuration
- https://wiki.gentoo.org/wiki/Kernel/Gentoo_Kernel_Configuration_Guide
- https://www.youtube.com/watch?v=T5SZERvLriA
- [http://blog.k3170makan.com/2020/11/linux-kernel-exploitation-0x0-debugging.html](http://blog.k3170makan.com/2020/11/linux-kernel-exploitation-0x0-debugging.html)
    - [https://raw.githubusercontent.com/google/syzkaller/refs/heads/master/tools/create-image.sh](https://raw.githubusercontent.com/google/syzkaller/refs/heads/master/tools/create-image.sh)
