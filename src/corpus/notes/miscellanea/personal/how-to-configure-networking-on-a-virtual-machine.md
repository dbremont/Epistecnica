---
tags: [note, como]
---

# How to configure networking on a virtual machine?


> To give a **virtual machine (VM)** access to the network, you can use different networking modes depending on your virtualization platform.
> 

## Index

## **Bridged Networking (Direct Access to LAN)**

- The VM acts like a physical machine on the network.
- It gets an IP from the same network as the host (via DHCP or static assignment).
- Best for scenarios where the VM needs full network access, including being discoverable by other machines.

**How to Set Up**:

- **VirtualBox**:
    1. Go to **Settings** → **Network**.
    2. Change **"Attached to"** to **"Bridged Adapter"**.
    3. Select the correct physical network interface.
- **KVM/QEMU (Linux)**:
    
    ```bash
    sudo ip link add br0 type bridge
    sudo ip link set eth0 master br0
    sudo ip link set br0 up
    
    ```
    
- **VMware**:
    1. Go to **Virtual Machine Settings** → **Network Adapter**.
    2. Select **"Bridged"**.

## **NAT (Network Address Translation)**

- The VM shares the host’s IP and connects via NAT.
- The VM can access external networks, but external systems **cannot** reach the VM.
- Best for internet access without exposing the VM to the network.

**How to Set Up**:

- **VirtualBox**:
    - Default setting for new VMs.
    - Go to **Settings** → **Network** → Select **"NAT"**.
- **KVM/QEMU** (via `libvirt`):
    
    ```bash
    virsh net-start default
    virsh net-autostart default
    
    ```
    
- **VMware**:
    - Select **"NAT"** in network settings.

## **Host-Only Network**

- The VM can communicate only with the host and other VMs on the same host.
- No internet access unless configured with routing.

**How to Set Up**:

- **VirtualBox**:
    - Go to **Settings** → **Network** → Choose **"Host-Only Adapter"**.
- **KVM/QEMU**:
    
    ```bash
    sudo ip link add vnet0 type bridge
    
    ```
    

## **Internal Network**

- The VM can only talk to other VMs on the same host.
- No access to the external network or the host unless additional routing is set.
