# qemu-system-x86_64


> 

QA:

- How to debug the Linux Kernel using Alpine Linux?

## List of Flags

> `qemu-system-x86_64  --help`
> 

| **Flag** | **Purpose** | **Example** |
| --- | --- | --- |
| **`-hda <file>`** | Specify the first hard disk image (IDE). | `-hda disk.img` |
| **`-hdb <file>`** | Specify the second hard disk image (IDE). | `-hdb disk2.img` |
| **`-kernel <file>`** | Specify a kernel image to boot. | `-kernel vmlinuz` |
| **`-drive <options>`** | Define a drive with specific options (e.g., `file`, `format`, `if`). | `-drive file=disk.img,format=qcow2,if=virtio` |
| **`-boot <order>`** | Set the boot order (e.g., `c` for hard disk, `d` for CD-ROM). | `-boot order=d` |
| **`-m <size>`** | Set the amount of RAM for the guest. | `-m 2048` (2 GB of RAM) |
| **`-cdrom <file>`** | Specify a CD-ROM image (IDE). | `-cdrom ubuntu.iso` |
| **`-smp <n>`** | Set the number of CPU cores. | `-smp 4` (4 CPU cores) |
| **`-initrd <file>`** | Specify an initial RAM disk (initrd) for the kernel. | `-initrd initrd.img` |
| **`-append <cmdline>`** | Pass kernel command-line arguments. | `-append "root=/dev/sda1 console=ttyS0"` |
| **`-netdev <type>,id=<name>,...`** | Configure a network backend. | `-netdev user,id=net0` |
| **`-device <driver>,...`** | Add a device to the guest (e.g., network card, USB device). | `-device e1000,netdev=net0` |
| **`-nographic`** | Disable graphical output and use the terminal for input/output. | `-nographic` |
| **`-curses`** | Use a text-based interface for the display. | `-curses` |
| **`-vga <type>`** | Specify the type of VGA card to emulate. | `-vga std` (standard VGA) |
| **`-display <type>`** | Specify the display backend (e.g., `sdl`, `gtk`, `none`). | `-display sdl` |
| **`-monitor <type>`** | Specify the monitor interface (e.g., `stdio`, `telnet`). | `-monitor stdio` |
| **`-serial <device>`** | Redirect the serial port to a device (e.g., `stdio`, `telnet`). | `-serial stdio` |
| **`-parallel <device>`** | Redirect the parallel port to a device. | `-parallel /dev/parport0` |
| **`-usb`** | Enable USB support. | `-usb` |
| **`-usbdevice <device>`** | Add a USB device (e.g., `mouse`, `tablet`). | `-usbdevice tablet` |
| **`-soundhw <model>`** | Enable sound hardware (e.g., `hda`, `ac97`). | `-soundhw hda` |
| **`-enable-kvm`** | Enable KVM (Kernel-based Virtual Machine) for hardware acceleration. | `-enable-kvm` |
| **`-cpu <model>`** | Specify the CPU model to emulate. | `-cpu host` (use the host CPU model) |
| **`-accel <type>`** | Enable an acceleration method (e.g., `kvm`, `tcg`). | `-accel kvm` |
| **`-s`** | Start a GDB server on port 1234. | `-s` |
| **`-gdb <device>`** | Start a GDB server on a specific device (e.g., `tcp::1234`). | `-gdb tcp::26000` |
| **`-S`** | Pause the CPU at startup (useful for debugging). | `-S` |
| **`-d <options>`** | Enable debug output (e.g., `cpu`, `int`, `mmu`). | `-d cpu,int` |
| **`-snapshot`** | Run in snapshot mode (changes to disk images are not saved). | `-snapshot` |
| **`-loadvm <snapshot>`** | Load a VM snapshot at startup. | `-loadvm snapshot1` |
| **`-net <type>,...`** | Configure a network interface (legacy option, prefer `-netdev`). | `-net user,hostfwd=tcp::2222-:22` |
| **`-fsdev <type>,...`** | Configure a file system device (e.g., `local`, `proxy`). | `-fsdev local,id=fs1,path=/shared,security_model=none` |
| **`-virtfs <options>`** | Configure a virtual file system (e.g., `local`, `proxy`). | `-virtfs local,path=/shared,mount_tag=host0,security_model=none` |
| **`-bios <file>`** | Specify a custom BIOS file. | `-bios bios.bin` |
| **`-pflash <file>`** | Specify a parallel flash image (e.g., for UEFI). | `-pflash uefi.img` |
| **`-L <path>`** | Specify the directory for BIOS, VGA BIOS, and keymaps. | `-L /usr/share/qemu` |
| **`-vnc <display>`** | Start a VNC server for remote display. | `-vnc :1` |
| **`-spice <options>`** | Enable SPICE remote desktop protocol. | `-spice port=5900,addr=127.0.0.1` |
| **`-rtc <options>`** | Configure the real-time clock (e.g., `base=utc`). | `-rtc base=utc` |
| **`-clock <options>`** | Configure the clock source (e.g., `rt`, `vm`). | `-clock rt` |
| **`-name <name>`** | Set the name of the guest (displayed in the window title). | `-name "My VM"` |
| **`-uuid <uuid>`** | Set the UUID of the guest. | `-uuid 550e8400-e29b-41d4-a716-446655440000` |

## References

- [Alpine Linux](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/alpine-linux.md)
- [Tiny Core Linux](note.html?n=technica/computation/operating-system/linux-distribution/tiny-core-linux.md)
- [A Guide to Build & Debug the Linux Kernel](https://app.notion.com/p/A-Guide-to-Build-Debug-the-Linux-Kernel-1a8c0f5171ec80d19474e2d019cd11db?pvs=21)