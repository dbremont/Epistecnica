# Rocky Linux

# How to install Rocky Linux with QEMU?

## QA

### How to install `Rocky Linux` with `QEMU`?

```bash
## Let's assume that we have QEMU.

mkdir -p ~/vms/rocky/{iso,vm}

## Download the Rocky Linux 10.2 x86_64 installer ISO
cd ~/vms/rocky/iso

curl -LO https://dl.rockylinux.org/pub/rocky/10/isos/x86_64/Rocky-10.2-x86_64-dvd1.iso

## Create the virtual disk
cd ~/vms/rocky/vm

qemu-img create -f qcow2 rocky.qcow2 30G

## Start the Rocky Linux installer
cd ~/vms/rocky/vm

# If this does not work - used the second.
qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=rocky.qcow2,format=qcow2 \
    -cdrom ~/vms/rocky/iso/Rocky-10.2-x86_64-dvd1.iso \
    -nic user,model=e1000 \
    -boot order=d
    
    
  qemu-system-x86_64 \
  -machine q35 \
  -enable-kvm \
  -cpu host \
  -m 4G \
  -smp 4 \
  -drive file=rocky.qcow2,format=qcow2 \
  -cdrom ~/vms/rocky/iso/Rocky-10.2-x86_64-dvd1.iso \
  -nic user,model=e1000 \
  -boot order=d
  \
  
## Use the installed version

qemu-system-x86_64 \
  -machine q35 \
  -enable-kvm \
  -cpu host \
  -m 4G \
  -smp 4 \
  -drive file=rocky.qcow2,format=qcow2 \
  -nic user,model=e1000
```

#### Why does `ps -aux` need permission to show the full path of the executing process?

> 

## References

- https://dl.rockylinux.org/pub/rocky/10/isos/x86_64/