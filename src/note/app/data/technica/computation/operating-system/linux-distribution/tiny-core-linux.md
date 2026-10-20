# Tiny Core Linux

# How to install Tiny Core Linux with QEMU?

## QA

### How to install `Tiny Core Linux` with `QEMU`?

```bash
## Let's assume that we have QEMU.

mkdir -p ~/vms/tinycore/{iso,vm}

## Download the Tiny Core Linux x86_64 ISO
cd ~/vms/tinycore/iso

curl -LO http://tinycorelinux.net/16.x/x86_64/release/CorePure64-current.iso

## Create the virtual disk
cd ~/vms/tinycore/vm

qemu-img create -f qcow2 tinycore.qcow2 10G

## Start the Tiny Core Linux installer
cd ~/vms/tinycore/vm

qemu-system-x86_64 \
    -machine q35 \
    -m 1G \
    -smp 2 \
    -drive file=tinycore.qcow2,format=qcow2 \
    -cdrom ~/vms/tinycore/iso/CorePure64-current.iso \
    -nic user,model=e1000 \
    -boot d
```

## References

- [Tiny Core Linux](http://www.tinycorelinux.net/)
- [Tiny Core Linux Downloads](http://www.tinycorelinux.net/downloads.html)
- [QEMU documentation](https://www.qemu.org/docs/)

## References

- https://en.wikipedia.org/wiki/Tiny_Core_Linux