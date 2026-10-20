# Gentoo

# How to install Gentoo with QEMU?

## QA

### How to install `Gentoo` with `QEMU`?

```bash
## Let's assume that we have QEMU.

mkdir -p ~/vms/gentoo/{iso,vm}

## Download the Gentoo amd64 minimal installation ISO
cd ~/vms/gentoo/iso

curl -LO https://distfiles.gentoo.org/releases/amd64/autobuilds/20260811T083102Z/livegui-amd64-20260811T083102Z.iso

## Create the virtual disk
cd ~/vms/gentoo/vm

qemu-img create -f qcow2 gentoo.qcow2 30G

## Start the Gentoo installation environment
cd ~/vms/gentoo/vm

qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=gentoo.qcow2,format=qcow2 \
    -cdrom ~/vms/gentoo/iso/install-amd64-minimal-20260712T170110Z.iso \
    -nic user,model=e1000 \
    -boot d
```

## References

- https://www.gentoo.org/
- [https://wiki.gentoo.org/wiki/Handbook:AMD64](https://wiki.gentoo.org/wiki/Handbook:AMD64)
- [https://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/](https://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/)
- [https://www.qemu.org/docs/](https://www.qemu.org/docs/)