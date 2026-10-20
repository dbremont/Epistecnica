# Fedora

> 

## QA

### How to install Fedora with QEMU?

```bash
## Let's assume that we have QEMU.

mkdir -p ~/vms/fedora/{iso,vm}
cd ~/vms/fedora/iso
curl -LO https://download.fedoraproject.org/pub/fedora/linux/releases/44/Workstation/x86_64/iso/Fedora-Workstation-Live-44-1.7.x86_64.iso

## Create the virtual disk
cd ~/vms/fedora/vm

qemu-img create -f qcow2 fedora.qcow2 30G

## Start the Fedora installer
cd ~/vms/fedora/vm

qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=fedora.qcow2,format=qcow2 \
    -cdrom ~/vms/fedora/iso/Fedora-Workstation-Live-44-1.7.x86_64.iso \
    -nic user,model=e1000 \
    -boot d
```

## References

- https://fedoraproject.org/