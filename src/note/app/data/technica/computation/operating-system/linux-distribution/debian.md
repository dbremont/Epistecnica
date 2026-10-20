# Debian

> 

## Interface Stack

| Layer | Debian |
| --- | --- |
| **Desktop Environment** | **GNOME** (default) |
| **Display Server** | **Wayland** (default GNOME session) |
| **Legacy Display Server** | X.Org Server / X11 |
| **Display Manager** | **GDM** (GNOME Display Manager) |
| **Window Manager / Compositor** | **Mutter** |
| **Graphics API** | OpenGL, Vulkan |
| **3D Graphics** | Mesa |
| **Kernel Graphics** | Linux DRM/KMS |
| **User-space Graphics Interface** | libdrm, Mesa, DRI |
| **Input** | libinput |
| **Desktop Toolkit** | GTK |
| **Audio** | PipeWire + WirePlumber |
| **Session / Service Management** | systemd + systemd-logind |
| **Desktop Services** | D-Bus |
| **Accessibility** | AT-SPI |
| **Remote Desktop** | GNOME Remote Desktop / related RHEL components |

## QA

### How to install Debian with QEMU?

```bash
## Let's assume that we have QEMU.

mkdir -p ~/vms/debian/{iso,vm}
cd ~/vms/debian/iso

curl -LO https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-13.6.0-amd64-netinst.iso

## Create the virtual disk
cd ~/vms/debian/vm
qemu-img create -f qcow2 debian.qcow2 30G

## Start the Debian installer
cd ~/vms/debian/vm
qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=debian.qcow2,format=qcow2 \
    -cdrom ~/vms/debian/iso/debian-13.0.0-amd64-netinst.iso \
    -nic user,model=e1000 \
    -boot d
```

## References

- https://www.debian.org/