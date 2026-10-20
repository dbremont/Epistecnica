# Kali Linux

# How to install Kali Linux with QEMU?

## QA

### How to install `Kali Linux` with `QEMU`?

```bash
## Let's assume that we have QEMU.

mkdir -p ~/vms/kali/{iso,vm}

## Download the current Kali Linux amd64 installer ISO
cd ~/vms/kali/iso

curl -LO https://cdimage.kali.org/current/kali-linux-2026.2-installer-amd64.iso

## Create the virtual disk
cd ~/vms/kali/vm

qemu-img create -f qcow2 kali.qcow2 30G

## Start the Kali Linux installer
cd ~/vms/kali/vm

qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=kali.qcow2,format=qcow2 \
    -cdrom ~/vms/kali/iso/kali-linux-2026.2-installer-amd64.iso \
    -nic user,model=e1000 \
    -boot d
```

## References

- https://www.kali.org/get-kali/#kali-platforms