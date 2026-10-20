# Virtualization

> Virtualization is a technology that allows multiple simulated environments or dedicated resources to be created from a single physical hardware system, enabling efficient resource utilization and isolation. It abstracts hardware and software resources, allowing users to run multiple operating systems and applications on the same physical machine by using hypervisors or containerization technologies, thereby enhancing scalability, flexibility, and management of IT infrastructure.
> 

> **Infrastructure Abstraction System (IaaS)**:  A cloud computing model that provides virtualized computing resources over the internet, abstracting hardware (e.g., compute, storage, networking) into virtual machines and services, managed via APIs, allowing users to provision and scale infrastructure dynamically.
> 

> **Infrastructure as Code (**IaC**)**: The practice of managing and provisioning infrastructure through machine-readable configuration files or scripts, enabling automated, version-controlled, and reproducible infrastructure deployment, often using tools like Terraform, Ansible, or CloudFormation.
> 

> **Cluster Management**: The process of overseeing and maintaining a distributed system of interconnected machines (nodes) in a cluster, managing the allocation of resources, failure recovery, scaling, and configuration of workloads to ensure efficient, reliable operation.
> 

> **Container Cluster Management**: The orchestration and management of a cluster of nodes running containerized applications, where tools like Kubernetes, Docker Swarm, or Apache Mesos handle container scheduling, resource allocation, scaling, and networking across the cluster.
> 

QA:

- How to virtualize and automate all my development experiments?
- How does IaaS and IaC related?
    - **IaC** is a **methodology** or **approach** for defining and provisioning infrastructure, typically on an IaaS platform, using code. It enables automation and management of infrastructure with configuration files.
    - **IaaS** is a **service model** that provides the underlying virtualized infrastructure (compute, storage, networking) abstracted from the hardware layer, typically offering resources that IaC can provision, configure, and manage.
- …

## Resources

| **Resource (X)** | **Virtualized Abstraction (Y)** |
| --- | --- |
| **CPU** | Virtual CPUs (vCPUs) |
| **Memory** | Virtual Memory (vRAM) |
| **Disk Storage** | Virtual Disk Images (VDI, Docker Volumes) |
| **Network Interface** | Virtual Network Interface Cards (vNICs) |
| **File System** | Overlay File Systems (UnionFS, aufs) |
| **Process Management** | Containers (LXC, Docker) |
| **Device Access** | Virtual Devices (virtio devices) |
| **User Accounts** | User Namespaces |
| **Network Stack** | Network Namespaces |
| **Resource Limits** | Control Groups (cgroups) |
| **Cluster Resources** | Virtualized Clusters (Kubernetes Pods, Docker Swarm Services) |

## **Virtualization Method**

| **Virtualization Method** | **Description** | **Use Case** |
| --- | --- | --- |
| **Full Virtualization** | Simulates complete hardware, allowing multiple operating systems to run on a single physical machine. | Running different OS types or versions simultaneously (e.g., KVM, VMware Workstation). |
| **Paravirtualization** | The guest OS is aware of the virtualization and communicates with the hypervisor for efficient resource management. | Performance-sensitive workloads, such as server applications (e.g., Xen). |
| **Hardware-assisted Virtualization** | Uses CPU extensions (like Intel VT-x or AMD-V) to improve performance and enable full virtualization. | Running virtual machines on compatible hardware for better performance. |
| **Operating System -level Virtualization (Aka Containers)** | **Containers** share the host OS kernel while providing isolated environments for applications. | Lightweight applications, microservices, and DevOps (e.g., Docker, LXC). |
| **Network Virtualization** | Abstracts network resources, creating virtual networks that can be independently managed and configured. | Multi-tenant cloud environments and software-defined networking (SDN). |
| **Storage Virtualization** | Pools physical storage resources to create a unified storage system that can be easily managed. | Simplifying storage management in data centers and enhancing storage performance. |
| **Desktop Virtualization** | Runs desktop environments on virtual machines, allowing users to access their desktops from any device. | Remote work scenarios and centralized desktop management (e.g., VDI). |
| **Application Virtualization** | Runs applications in isolated environments without needing a full OS instance, often using streaming technology. | Deploying applications without modifying the host OS (e.g., Microsoft App-V, Citrix). |
| **Cloud Virtualization** | Provides virtual resources over the internet, allowing on-demand access to compute, storage, and networking. | Scalable infrastructure in public and private clouds (e.g., AWS, Azure). |
| **Server Virtualization** | Consolidates multiple server instances on a single physical server, optimizing resource usage. | Reducing hardware costs and improving resource efficiency in data centers (e.g., VMware ESXi). |

## Conceptual Model

Virtualization: Conceptual Model

## References

- [Linux Virtualization Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-virtualization-stack.md)
- https://en.wikipedia.org/wiki/OS-level_virtualization
- Bellard, F. (n.d.). QEMU, a Fast and Portable Dynamic Translator.
- Craig, I. D. (2011). Virtual Machines (2006th ed.). Springer.
- 
- Runtimes Environments Containers are chroot https://earthly.dev/blog/chroot/
- Build your own Docker with Linux namespaces, cgroups, and chroot (akashrajpurohit.com) https://news.ycombinator.com/item?id=36488356
- https://blog.lizzie.io/linux-containers-in-500-loc.html
- [How to configure networking on a virtual machine?](https://app.notion.com/p/How-to-configure-networking-on-a-virtual-machine-1a1c0f5171ec80a6877dd4c084cac4f9?pvs=21)
- https://news.ycombinator.com/item?id=32764501