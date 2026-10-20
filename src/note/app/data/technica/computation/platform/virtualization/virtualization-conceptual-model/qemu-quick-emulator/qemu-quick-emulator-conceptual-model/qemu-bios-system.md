# QEMU: BIOS System


### **QEMU BIOS System Overview**

QEMU provides BIOS and firmware support for different architectures to initialize the system before the operating system takes over. The BIOS or firmware is responsible for hardware initialization, bootstrapping the OS, and providing legacy services if required.

---

## **1. x86 BIOS Support (Legacy BIOS & UEFI)**

For **x86 (i386 & x86_64)** emulation, QEMU supports multiple BIOS/firmware options:

### **A. SeaBIOS (Default Legacy BIOS)**

- SeaBIOS is a lightweight, open-source BIOS used in QEMU for **legacy BIOS booting**.
- It supports **16-bit real mode**, legacy bootloaders (e.g., GRUB, LILO, SYSLINUX), and traditional BIOS interrupts.
- Used when running QEMU with a standard PC machine type (`pc`, `q35`).
- **Location:** `/usr/share/qemu/bios.bin` (on some systems) or embedded in QEMU.

### **Example: Boot with SeaBIOS**

```bash
qemu-system-i386 -bios /usr/share/qemu/bios.bin -hda disk.img

```

---

### **B. OVMF (UEFI Firmware)**

- **OVMF** (Open Virtual Machine Firmware) provides **UEFI** support for QEMU.
- Uses **EDK II**, a modern UEFI implementation.
- Required for booting modern OSes in **UEFI mode**.

### **Example: Boot with UEFI (OVMF)**

```bash
qemu-system-x86_64 -bios /usr/share/OVMF/OVMF_CODE.fd -drive file=disk.img,format=raw

```

---

## **2. ARM, RISC-V, and Other Architectures**

Other architectures use different firmware instead of a traditional PC BIOS:

### **A. ARM (U-Boot, UEFI)**

- ARM does **not** use a BIOS like x86; instead, it relies on **bootloaders** such as:
    - **U-Boot** (for embedded and Linux systems).
    - **EDK II/OVMF for ARM** (for UEFI boot).
- QEMU provides `pflash` support to load UEFI firmware.

### **Example: Boot ARM with UEFI**

```bash
qemu-system-aarch64 -M virt -cpu cortex-a72 -bios QEMU_EFI.fd -hda disk.img

```

---

### **B. RISC-V (OpenSBI + U-Boot)**

- RISC-V systems use:
    - **OpenSBI** (Supervisor Binary Interface) for low-level initialization.
    - **U-Boot** for boot management.

### **Example: Boot RISC-V with OpenSBI & U-Boot**

```bash
qemu-system-riscv64 -M virt -bios opensbi-riscv64-generic-fw_dynamic.bin -kernel uboot.bin

```

---

## **3. Custom BIOS in QEMU**

- You can load **custom BIOS ROMs** using the `bios` option.
- Useful for running modified firmware, custom embedded systems, or debugging firmware.

### **Example: Boot with a Custom BIOS**

```bash
qemu-system-i386 -bios mycustombios.bin -hda disk.img

```

---

## **4. Debugging and Development**

- QEMU allows **BIOS debugging** with **GDB**:

Then, attach **GDB**:
    
    ```bash
    qemu-system-i386 -S -s -bios bios.bin
    
    ```
    
    ```bash
    gdb -ex "target remote localhost:1234"
    
    ```
    

---

## **Conclusion**

- **SeaBIOS** = Default **legacy BIOS** for x86.
- **OVMF** = UEFI firmware for x86 and ARM.
- **U-Boot/OpenSBI** = Used for ARM & RISC-V platforms.
- **Custom BIOS support** via `bios` option.

Would you like help with a specific firmware setup in QEMU? 🚀