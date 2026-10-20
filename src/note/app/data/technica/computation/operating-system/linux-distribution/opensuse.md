# openSUSE

# How to install openSUSE with QEMU?

## QA

### How to install `openSUSE` with `QEMU`?

```bash
## Let's assume that we have QEMU.

mkdir -p ~/vms/opensuse/{iso,vm}

## Download the openSUSE Leap 16.0 x86_64 installer ISO
cd ~/vms/opensuse/iso

curl -LO https://download.opensuse.org/download/distribution/openSUSE-current/offline/Leap-16.0-offline-installer-x86_64.install.iso

## Create the virtual disk
cd ~/vms/opensuse/vm

qemu-img create -f qcow2 opensuse.qcow2 30G

## Start the openSUSE installer
cd ~/vms/opensuse/vm

qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=opensuse.qcow2,format=qcow2 \
    -cdrom ~/vms/opensuse/iso/openSUSE-Leap-16.0-DVD-x86_64-Media.iso \
    -nic user,model=e1000 \
    -boot d
```

## References

- https://www.opensuse.org/