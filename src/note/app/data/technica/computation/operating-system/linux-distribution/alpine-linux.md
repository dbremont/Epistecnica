# Alpine Linux

# How to install Alpine Linux with QEMU?

## QA

### How to install `Alpine Linux` with `QEMU`?

```bash
## Let's assume that we have QEMU.

mkdir -p ~/vms/alpine/{iso,vm}

## Download the Alpine Linux x86_64 standard ISO
cd ~/vms/alpine/iso

curl -LO https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/alpine-standard-3.23.3-x86_64.iso

## Create the virtual disk
cd ~/vms/alpine/vm

qemu-img create -f qcow2 alpine.qcow2 10G

## Start the Alpine Linux installer
cd ~/vms/alpine/vm

qemu-system-x86_64 \
    -machine q35 \
    -m 1G \
    -smp 2 \
    -drive file=alpine.qcow2,format=qcow2 \
    -cdrom ~/vms/alpine/iso/alpine-standard-3.24.1-x86_64.iso \
    -nic user,model=e1000 \
    -boot d
```

## References

- https://www.alpinelinux.org/