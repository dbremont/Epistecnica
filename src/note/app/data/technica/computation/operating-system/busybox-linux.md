# BusyBox Linux

> Note: This is not a Linux Distro.
> 

# How to install BusyBox Linux with QEMU?

## QA

### How to install `BusyBox Linux` with `QEMU`?

```bash
## Let's assume that we have QEMU and Buildroot.

mkdir -p ~/vms/busybox/{iso,vm}
cd ~/vms/busybox

## Download Buildroot
curl -LO https://buildroot.org/downloads/buildroot-2026.02.tar.xz

## Extract Buildroot
tar -xf buildroot-2026.02.tar.xz
cd buildroot-2026.02

## Build a minimal Linux system using BusyBox
make qemu_x86_64_defconfig
make

## Create the virtual disk
cd ~/vms/busybox/vm

qemu-img create -f qcow2 busybox.qcow2 2G

## Start the Linux system
qemu-system-x86_64 \
    -machine q35 \
    -m 512M \
    -smp 2 \
    -drive file=busybox.qcow2,format=qcow2 \
    -kernel ~/vms/busybox/buildroot-2026.02/output/images/bzImage \
    -append "root=/dev/vda console=ttyS0" \
    -nographic
```

> Unlike a conventional distribution installation, this example does not boot an installer ISO. Buildroot generates a minimal Linux system containing BusyBox, a Linux kernel, and the root filesystem.
> 

## References

- https://busybox.net/
- https://buildroot.org/