---
tags: [container]
---

# Container

- Related Virtualization: Conceptual Model: [Docker](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/docker.md)

> A **container** is an isolated execution environment that encapsulates an application and its dependencies, enabling it to run consistently across different computing environments. Technically, it is a user-space process that leverages kernel-level features to provide isolation, resource control, and process management, all while sharing the host system’s kernel. Containers are constructed from **container images**, which are layered filesystems designed to provide lightweight and portable application execution.
> 

QA:

- …

## Virtualization Model

> The container virtualization model leverages kernel-level isolation mechanisms, such as namespaces and cgroups, to create lightweight, portable, and resource-controlled user-space processes that share the host OS kernel, enabling multi-tenancy and efficient application execution without the overhead of full hardware virtualization.
> 
1. **Namespace Isolation**: Containers use Linux kernel namespaces to isolate various system resources:
    - **PID Namespace**: Isolates process IDs, ensuring that a container only sees its own processes.
    - **Network Namespace**: Provides network isolation, giving each container its own network stack (e.g., IP addresses, ports).
    - **Mount Namespace**: Ensures the container has its own file system, often created via union filesystems like OverlayFS or AUFS.
    - **UTS Namespace**: Allows each container to have its own hostname.
    - **IPC Namespace**: Isolates Inter-Process Communication (IPC) resources like message queues, semaphores, and shared memory.
    - **User Namespace**: Maps container user IDs to host user IDs, isolating user access within the container.
2. **Control Groups (cgroups)**: Containers use cgroups to manage and limit the allocation of system resources such as CPU, memory, and I/O bandwidth, ensuring resource isolation and preventing resource contention between containers on the same host.
3. **Union Filesystem**: A container’s filesystem is typically built using union filesystems (e.g., **OverlayFS**, **AUFS**, or **Btrfs**), which allow multiple layers of filesystems to be stacked on top of each other. The base image is immutable, while any changes made by the container are stored in a writable layer above it.
4. **Container Image**: A **container image** is a snapshot of the filesystem and application dependencies. It is composed of multiple layers, with each layer representing a set of changes (e.g., adding files, installing software). This image is read-only, and containers are instantiated as runtime processes from these images. Images can be versioned and stored in container registries (e.g., Docker Hub).
5. **Runtime Environment**: A container typically runs in user space on top of the host system's kernel. It communicates directly with the host's kernel via system calls but is isolated from other processes via namespaces and controlled by cgroups. The container runtime (e.g., **containerd**, **CRI-O**) is responsible for managing the container’s lifecycle, including pulling images, creating containers, and launching the processes inside.
6. **Process Model**: A container is typically composed of one or more processes running in a single isolated environment. The container runtime ensures that these processes execute with the privileges and resource limits defined by the container configuration, preventing them from interacting with the host system or other containers outside of the defined isolation.
7. **Network Virtualization**: Containers often utilize network virtualization technologies such as **virtual Ethernet bridges (veth)**, **Network Namespaces**, and **macvlan networks** to create a network stack that can be completely isolated from the host or other containers.
8. **Security Features**: Containers utilize a combination of security mechanisms to ensure isolation and prevent malicious activity:
    - **SELinux/AppArmor**: Mandatory access control (MAC) systems to enforce security policies on containers.
    - **Seccomp**: A Linux kernel feature that filters the system calls a container is allowed to make, limiting the attack surface.
    - **Linux Capabilities**: Containers are often run with a reduced set of capabilities, limiting their ability to perform certain privileged operations.

## Technologies

| **Container Technology** | **Description** | **Use Case** |
| --- | --- | --- |
| **Docker** | A platform for developing, shipping, and running applications in containers, using a layered filesystem. | Application packaging, microservices, and CI/CD workflows. |
| **Kubernetes** | An open-source container orchestration platform for automating the deployment, scaling, and management of containerized applications. | Managing large-scale container deployments in production. |
| **OpenShift** | A Kubernetes-based container platform that provides developer and operational tools for managing containers. | Enterprise-level application development and deployment. |
| **LXC (Linux Containers)** | An operating-system-level virtualization method for running multiple isolated Linux systems on a single host. | Lightweight system virtualization and testing environments. |
| **rkt (pronounced "rocket")** | A container engine designed for simplicity and security, developed by CoreOS. | Running applications in a secure environment. |
| **Containerd** | An industry-standard core container runtime that manages the complete container lifecycle, from image transfer to container execution. | Foundation for higher-level container orchestration tools. |
| **CRI-O** | A lightweight container runtime specifically for Kubernetes, allowing Kubernetes to manage container images and run containers. | Integrating with Kubernetes to run OCI-compliant containers. |
| **Podman** | A daemonless container engine that allows users to create, manage, and run containers and pods without requiring a background service. | Simplified container management without a central daemon. |
| **Docker Swarm** | Docker's native clustering and orchestration tool, enabling the management of a cluster of Docker engines. | Simplified orchestration for smaller deployments. |
| **AWS Fargate** | A serverless compute engine for containers that works with Amazon ECS, allowing users to run containers without managing servers. | Running containerized applications in the cloud without infrastructure management. |
| **Azure Container Instances (ACI)** | A service that allows users to run containers on Azure without managing the underlying infrastructure. | Quickly deploying single containers in the cloud. |
| **Google Kubernetes Engine (GKE)** | A managed Kubernetes service by Google Cloud for deploying, managing, and scaling containerized applications. | Simplified Kubernetes management in the Google Cloud. |

## References

- https://github.com/opencontainers/runc
- https://kubernetes.io/docs/concepts/architecture/cri/
- https://en.wikipedia.org/wiki/Open_Container_Initiative
- https://github.com/opencontainers/runtime-spec
- https://en.wikipedia.org/wiki/Containerization_(computing)