---
tags: [container]
---

# Docker

- Related Virtualization: Conceptual Model: [Docker Compose](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/docker-compose.md), [Docker Image](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/docker-image.md), [Docker Network](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/docker-network.md), [Container Registry](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/container-registry.md), [Container Orchestration](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/container-orchestration.md), [Container](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/container.md)

> TODO:  NOW THAT THE NOTE IS SORT OF ORGANIZE - LET’S CONTINUE WORKING ON IT.
> 

> Docker is a platform that enables developers to package and distribute applications and their dependencies in lightweight, isolated containers for efficient and consistent deployment across different environments.
> 

> Docker relies on several key components in a typical Linux-based tech stack, including the Docker Engine (which includes the Docker daemon and client), container runtimes (such as containerd or runc), a container image registry (like Docker Hub or a private registry), and the host operating system’s kernel features (such as cgroups and namespaces) to provide containerization and orchestration capabilities.
> 

> Containers: Docker containers are instances of Docker images. Containers are lightweight, runnable environments that encapsulate the application, its dependencies, and a writable layer known as the container layer. Containers are ephemeral and can be started, stopped, and removed without affecting the underlying image.
> 

> Bind Mounts: Bind mounts allow you to map a directory or file on the host system into a container. They provide a direct, real-time connection between the container’s file system and the host’s file system. Data stored in bind mounts is accessible from both the host and the container.
> 

> Registry: Docker images can be stored and shared in remote repositories called Docker registries. Docker Hub is a popular public registry, and organizations often use private registries to manage their images. You can push and pull images to and from registries to share them with others.
> 

## Formulation

- What is its technical purpose?
- Within which technical domain does it operate?
- Which are the **technical problem** set that this **production technical object** helps to solve?

## Interface

- (Interface) What interaction interface does the tool offer to enable users to achieve their technical goals?
- What operations does the interface guarantee?
- How is the interface contract realized?
- Which are the `technical artifacts` that form part of the interface?

### Docker Files

> Docker primarily uses Dockerfiles and various configuration files to define and customize containerized environments.
> 

> Dockerfile: A Dockerfile is a text file that contains instructions for building a Docker image. It specifies the base image, adds files and directories to the image, sets environment variables, and defines the image’s entry point. Dockerfiles are used to create customized images that can be used to run containers.
> 

Here’s a list of some critical Docker files and configuration files:

| **File Name** | **Description** |
| --- | --- |
| **Dockerfile** | A text file containing instructions to build a Docker image, defining the base image and settings. |
| **.dockerignore** | Specifies patterns for files and directories to exclude when building the Docker image, reducing size. |
| **docker-compose.yml** | A YAML file used with Docker Compose to define multi-container applications and their configurations. |
| **Docker Compose Override Files** | Files (e.g., `docker-compose.override.yml`) that override or extend configurations for different environments. |
| **.env** | An environment file for storing environment variables that can be referenced in `docker-compose.yml`. |
| **Dockerfile.template** | A template from which Dockerfiles may be generated, allowing for dynamic content creation. |
| **Dockerignore Templates** | Templates or scripts used to dynamically generate `.dockerignore` files based on project needs. |
| **Docker Build Context** | The directory where the Dockerfile resides, including all files and subdirectories used for the build. |
| **Docker Image Manifest (manifest.json)** | Internally managed file containing information about the image’s layers, inspectable via commands. |
| **Docker Configuration Files** | Configuration files like `daemon.json` and `config.json` that customize Docker’s behavior. |
| **Docker Swarm Configuration Files** | Configuration files (e.g., `docker-swarm-init`, `docker-swarm-join`) for initializing and joining Swarm nodes. |
| **Docker Network Configuration Files** | Files (e.g., `docker-compose-network.yml`) that define custom network configurations for Docker Compose. |

## Implementation

- How is the tool implemented? How does it virtualized underlying resources?
- Which are the components of technical system?
- Which elements does the operating system provide to support the interface contract?
- Which techniques are embedded in the technical product?
- Can a container emulates an operating system?
- Which constituent technical objects are embedded within the technical product?
- Which constituent technical objects are embedded within it?
- Which technical principles guide its design?
- Which external infrastructure elements does it depend on, and how does it interact with them?

### Virtualization Model

> Note: Docker Virtualization Model For Linux.
> 

> The **Docker virtualization model on Linux** employs a containerization architecture that utilizes **kernel features** such as **cgroups** (control groups) and **namespaces to provide lightweight process isolation**, allowing the **Docker daemon** to manage and orchestrate multiple containers as isolated user space instances, each with its own **file system** (constructed from layered images using the **Union File System**), **networking stack** (configured via bridge, overlay, or host networking modes), and **resource limits**, while leveraging the host Linux kernel to achieve high-density application deployment without the overhead of traditional virtual machines, enabling rapid scaling and efficient utilization of system resources.
> 

| **Resource (X)** | **Virtualized Component (Y)** |
| --- | --- |
| **Operating System** | Docker Daemon |
| **Applications** | Containers |
| **Application Environment** | Images |
| **Configuration** | Dockerfile |
| **Data Storage** | Volumes |
| **Networking** | Bridge Network, Host Network, Overlay Network |
| **Clustering Resources** | Docker Swarm |
| **Service Management** | Services (in Docker Swarm) |
| **User Commands** | Docker CLI |
| **Image Repository** | Docker Hub |

### **Docker Engine**

> **Docker Engine**: The core component of Docker, responsible for creating, running, and managing containers.
> 

It consists of:

- **Server (Docker Daemon)**: A background service that manages Docker containers, images, networks, and volumes.
- **REST API**: An API that allows clients to communicate with the Docker daemon, enabling the management of Docker resources.
- **CLI (Command-Line Interface)**: The `docker` command used by users to interact with the Docker daemon through the command line.

### Docker Image

> A Docker image is a lightweight, standalone, and executable package containing all the necessary components and dependencies to run a specific application or service. It is a fundamental building block in Docker containerization technology, which allows you to create, deploy, and manage applications consistently and isolatedly across different environments.
> 

> Images: Docker images are read-only templates that contain an application or service and all of its dependencies. Images are stored in a layered format, consisting of a base image and a series of read-only layers that represent changes made to the base image. Images are immutable, meaning they cannot be modified once created.
> 

### Docker Container

> Containers are lightweight, isolated environments that provide a consistent and reproducible way to run applications. You can perform various operations within containers to manage and interact with them. Here’s a list of common operations you can perform in containers:
> 
1. **Create a Container**: You can create a new container based on an existing image using the `docker run` command.
2. **Start a Container**: You can start a previously created container using the `docker start` command.
3. **Stop a Container**: You can stop a running container using the `docker stop` command.
4. **Restart a Container**: You can restart a container using the `docker restart` command.
5. **Pause a Container**: You can pause a running container using the `docker pause` command.
6. **Unpause a Container**: You can unpause a paused container using the `docker unpause` command.
7. **Attach to a Container**: You can attach to a running container’s console or standard input/output using the `docker attach` command.
8. **Inspect a Container**: You can view detailed information about a container using the `docker inspect` command.
9. **List Containers**: You can list all running and stopped containers using the `docker ps` or `docker container ls` command.
10. **Remove a Container**: You can remove a stopped container using the `docker rm` command.
11. **Execute a Command in a Container**: You can run a one-time command within a running container using the `docker exec` command.
12. **Copy Files to/from a Container**: You can copy files to/from a container using the `docker cp` command.
13. **Rename a Container**: You can rename a container using the `docker rename` command.
14. **View Container Logs**: You can view the logs generated by a container using the `docker logs` command.
15. **Set Environment Variables**: You can set environment variables for a container using the `e` or `-env` flag when creating a container.
16. **Mount Volumes**: You can mount volumes from the host machine into a container to share data between them.
17. **Modify Container Configuration**: You can modify certain container configurations, such as the container’s hostname, by using flags when creating or running a container.
18. **Limit Container Resources**: You can limit the CPU and memory resources a container can use using resource constraints.
19. **Commit Changes**: You can commit changes made in a container to create a new image using the `docker commit` command.
20. **Export and Import Containers**: You can export a container’s filesystem as an archive using the `docker export` command and then import it to create a new image using the `docker import` command.
21. **Network Operations**: You can configure network settings for containers, including exposing ports, connecting containers to specific networks, and creating custom networks.
22. **Execute Commands in the Shell**: You can run interactive shell sessions within a container by using the `docker exec -it` command.
23. **View Container Statistics**: You can view real-time resource usage statistics for a container using the `docker stats` command.

### Docker Volume

> Persistent storage for Docker containers. Volumes are used to store data generated by and used by Docker containers, allowing data to persist even when containers are stopped or removed.
> 

> Volumes: Volumes are a way to persist data in Docker. They provide a mechanism for containers to store and share data between themselves and the host system or other containers. Volumes are typically used for data that needs to survive container restarts, updates, or removals.
> 

> Named Volumes: Named volumes are a type of volume that Docker manages and names automatically. They provide a more abstract and flexible way to manage data persistence. Named volumes can be shared among multiple containers and are decoupled from container lifecycles.
> 

> Anonymous Volumes: Anonymous volumes are automatically created by Docker and are linked to a specific container. They are typically used when you don’t need to access the volume from outside the container. Anonymous volumes are useful for temporary or transient data storage.
> 

### Container Persistence

> Here's a table outlining the various methods for achieving data persistence in Docker containers:
> 

| **Persistence Method** | **Description** | **Use Case** |
| --- | --- | --- |
| **Volumes** | Managed by Docker, volumes provide a way to store data outside of the container's filesystem. | Ideal for databases and applications requiring persistent data. |
| **Bind Mounts** | Link a directory from the host filesystem to a container, allowing the container to read/write directly to the host. | Useful for development environments or when sharing data between the host and containers. |
| **Anonymous Volumes** | Volumes created without a specific name, often used for temporary data storage during container runs. | Suitable for temporary data that doesn't need to persist after container removal. |
| **Docker Compose with Volumes** | Use Docker Compose to define and manage volumes, allowing for easier orchestration of multi-container applications. | Best for complex applications that require multiple containers with shared data. |
| **Database Containers** | Run databases in separate containers with volumes to ensure data persistence and backup capabilities. | Commonly used for applications that rely on databases for stateful data. |
| **Object Storage** | Use external object storage services (e.g., Amazon S3, Google Cloud Storage) for storing data generated by containers. | Ideal for applications that generate large amounts of unstructured data, like media files. |
| **Snapshotting** | Create snapshots of container volumes at specific points in time, enabling backup and restore capabilities. | Useful for backup strategies and data recovery processes. |
| **Docker Swarm Persistent Storage** | Use Docker Swarm's volume drivers to manage persistent storage across a cluster of Docker hosts. | Best for distributed applications that require high availability and data consistency. |

### Container Orchestration

> Container orchestration tools help manage and automate the deployment, scaling, and management of containerized applications.
> 

## Evaluation

> (Evaluation) Which technical requirements does it satisfy?
> 

## Evolution

> How has it evolved?
> 

## Maintenance

> How is it maintained?
> 

## Failure Mode

> (Failure Mode Set) How can it fail?
> 

## Limitation

> Which is the limit of the `production technical object`?
> 

## QA

### How to x?

```bash
## Stop Containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

## List Network Interface
docker network ls

## Remove User Defined Networks
docker network prune -f

## Docker Communicaton Socket (IPC)
/var/run/docker.sock

```

### Can a Docker container execute binaries in a format that is incompatible with the host kernel?

> Fundamentally, **no**. A Docker container cannot natively execute binaries whose executable format, instruction set architecture, or operating system interface is incompatible with the host kernel, because a container does not include its own kernel—it relies entirely on the host's kernel to create and manage its processes. When a process inside a container invokes `execve()`, the request is handled directly by the host kernel, which examines the binary format (such as the ELF format used by Linux executables), verifies that it recognizes the executable type, loads the program into memory, and begins execution. If the binary is built for a different operating system (for example, a Windows PE executable) or a different processor architecture (for example, an ARM binary on an x86-64 machine), the host kernel cannot interpret or execute it natively. Likewise, if the application depends on kernel features or system calls that are unavailable in the host kernel, execution may fail even though the binary itself is a valid Linux executable. The container's filesystem, libraries, and user-space tools do not influence this compatibility because they operate above the kernel interface. The only exception is when an additional compatibility layer or emulator—such as QEMU for cross-architecture emulation or Wine for certain Windows applications—is explicitly introduced. In these cases, the incompatible binary is not executed directly by the kernel; instead, it is interpreted or translated by another user-space program that itself runs as a normal Linux process. Therefore, compatibility is ultimately determined by the capabilities of the **host kernel**, not by the container image.
> 

### Can a container be considered an operating system?

> **TL;DR:** In the context of containers, an "operating system" informally refers to the **user-space environment**—the collection of executables (binaries), shared libraries, configuration files, package manager, and filesystem hierarchy—rather than the kernel. A Docker image such as Alpine or Ubuntu packages this user-space, while all containers running on the host share the host's Linux kernel.
> 

> Strictly speaking, **a container is not an operating system**, although it is often mistaken for one because it contains many of the same user-space components found in a Linux distribution. An operating system consists of both **kernel-space** and **user-space** components. The kernel provides the fundamental mechanisms that manage hardware resources, schedule processes, allocate memory, implement filesystems, handle networking, enforce security, and expose the system call interface through which applications interact with the machine. User-space, in contrast, contains programs such as shells, libraries, package managers, compilers, utilities, and applications. A Docker container packages only a selected portion of this user-space environment together with an application and its dependencies. The kernel remains external and is shared with every other container running on the host. Consequently, a container cannot boot independently, manage hardware, schedule processes, or provide operating system services without the host kernel. From a systems perspective, a container is more accurately described as **an isolated execution environment** or **an isolated user-space instance** rather than an operating system. Linux namespaces provide each container with its own view of processes, filesystems, networking, users, and other resources, while control groups (cgroups) regulate resource consumption. This isolation can make a container appear to behave like a separate operating system, but the isolation is an abstraction implemented by a single shared kernel rather than the existence of an independent operating system.
> 

### What is the meaning of the Alpine container?

> An Alpine container is **a container image whose user-space environment is derived from Alpine Linux**, a lightweight Linux distribution specifically designed to minimize size, complexity, and resource consumption. The term "Alpine container" does not refer to a special kind of container or a different virtualization technology; rather, it identifies the contents of the container's root filesystem. An Alpine container typically includes the Alpine directory hierarchy, the BusyBox implementation of standard Unix utilities, the musl C standard library, the `apk` package manager, configuration files, and whatever applications have been installed into the image. It deliberately excludes the Linux kernel because the kernel is supplied by the host operating system at runtime. As a result, an Alpine container behaves like a minimal Alpine Linux installation while actually executing all of its processes through the host's kernel. The principal motivation for using Alpine is its extremely small footprint, often resulting in base images of only a few megabytes, which reduces download times, storage requirements, attack surface, and deployment latency. However, this minimalism also introduces trade-offs: the use of musl instead of glibc can lead to compatibility issues with software expecting the GNU C Library, and the BusyBox implementations of common utilities may not support every feature available in their GNU counterparts. Thus, an Alpine container should be understood not as an operating system in itself, but as **a portable, self-contained Alpine Linux user-space environment that executes on top of a shared Linux kernel**, providing a compact and efficient foundation for containerized applications.
> 

## References

- [Overview of Docker Build](https://docs.docker.com/build/)
- [How to configure different dockerfile for development and production](https://stackoverflow.com/questions/46440909/how-to-configure-different-dockerfile-for-development-and-production)
- [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [How Container Networking Works: Practical Explanation Container Networking Is Simple!](https://iximiuz.com/en/posts/container-networking-is-simple/)
- [Linux post-installation steps for Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/)
- [Ask HN: “Build your own Docker” tutorial – what to include?](https://news.ycombinator.com/item?id=21762951)
- [Docker Compose Overview](https://docs.docker.com/compose/)
- [How to Fix and Debug Docker Containers Like a Superhero](https://www.docker.com/blog/how-to-fix-and-debug-docker-containers-like-a-superhero/)
- [A Beginner’s Guide to Debugging Docker Containers](https://earthly.dev/blog/debugging-docker-containers/)
- [It’s Time to Forget About Docker](https://martinheinz.dev/blog/35)
- https://dozzle.dev/ - Real-time logging and monitoring for Docker in the browser
- https://dockge.kuma.pet/
- Internals:
    - [Bocker](https://gitlab.com/dbtudes/bocker)
    - [Docker Internals A Deep Dive Into Docker For Engineers Interested In The Gritty Details](http://docker-saigon.github.io/post/Docker-Internals/)
    - [Deep Dive into Docker Internals - Union Filesystem](https://martinheinz.dev/blog/44)
    - [Measuring Docker Performance: What a mess!!!](https://www.diva-portal.org/smash/get/diva2:1107544/FULLTEXT01.pdf)
    - [moby](https://github.com/moby/moby/tree/master)
    - [contained](https://github.com/containerd/containerd)
    - [How to work with container images using ctr](https://labs.iximiuz.com/courses/containerd-cli/ctr/image-management)
    - [The tool that really runs your containers: deep dive into runc and OCI specifications](https://mkdev.me/posts/the-tool-that-really-runs-your-containers-deep-dive-into-runc-and-oci-specifications)
    - [runc](https://github.com/opencontainers/runc)
- [Virtualization](note.html?n=technica/computation/platform/virtualization.md)
- [Linux Virtualization Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-virtualization-stack.md)
- [Philosophia Artium Technicarum et Operis](https://app.notion.com/p/Philosophia-Artium-Technicarum-et-Operis-355c0f5171ec808b82f8d7a85e8134cd?pvs=21)