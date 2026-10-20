---
tags: [cluster-management, container, iaas]
---

# Kubernetes

- Related Virtualization: Conceptual Model: k3s: [Lightweight Kubernetes](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/k3s-lightweight-kubernetes.md)

> **Kubernetes**:  { Management of Nodes + Resources, Pods (Containerized Workloads) }
> 

> A **container orchestration platform** that manages automated deployment, scaling, and operation of application **containers across clusters of hosts**. It is highly effective in abstracting the underlying infrastructure for container deployments.
> 

> **Kubernetes** is an **open-source container orchestration platform** designed to automate the deployment, scaling, and management of containerized applications across a cluster of machines. It provides a framework to run distributed systems resiliently, with **high availability**, **scalability**, and **self-healing** capabilities, abstracting the underlying infrastructure from the application.
> 

> **Pods**: The smallest deployable units in Kubernetes, typically representing a single container (or multiple containers with shared storage and network) that are scheduled together on the same node. **Pods** are ephemeral and can be recreated automatically by the system if they fail.
> 

> **Nodes**: Physical or virtual machines that run Kubernetes workloads. Nodes contain the necessary components to run pods, such as the **kubelet** (which communicates with the Kubernetes master), **kube-proxy** (for networking), and container runtime (e.g., Docker, containerd).
> 

> **Kubernetes Master (Control Plane)**: The set of components responsible for controlling the cluster, including the **API server**, **controller manager**, **scheduler**, and **etcd** (a distributed key-value store for cluster state).
> 

> **Deployments**: **Deployments** provide declarative updates for Pods and ReplicaSets, allowing you to describe the desired state for your application (e.g., which container image to use, how many replicas, etc.). Kubernetes ensures that the actual state matches the desired state, handling the deployment, scaling, and rolling updates automatically.
> 

> **ReplicaSets**: A ReplicaSet ensures that a specified number of **identical Pods** are running at any given time. It is used by Deployments to maintain the required number of replicas.
> 

> **Services**: **Services** provide a stable, virtual IP address for accessing Pods and allow for load balancing and service discovery. They can expose applications internally within the cluster or externally to the outside world (e.g., LoadBalancer, NodePort).
> 

> **Namespaces**: Namespaces provide **virtual clusters** within a Kubernetes cluster, enabling resource isolation, organization, and multi-tenancy. Resources such as Pods, Services, and Deployments can be scoped to a specific namespace.
> 

> **StatefulSets**: StatefulSets manage the deployment of stateful applications that require stable, unique network identities, persistent storage, and ordered deployment or scaling. They are commonly used for applications like databases or services with persistent state.
> 

> **Persistent Volumes (PV) and Persistent Volume Claims (PVC)**: **Persistent Volumes** provide abstraction for storage resources. **Persistent Volume Claims** are requests for storage that are fulfilled by PVs. They are used to manage **stateful workloads** that require persistent data.
> 

> **Ingress**: **Ingress** manages external access to services, typically HTTP and HTTPS, and provides routing based on the URL path or host. It can also provide SSL termination, load balancing, and name-based virtual hosting.
> 

> **Horizontal Pod Autoscaling (HPA)**: The **HPA** automatically adjusts the number of Pods in a Deployment or ReplicaSet based on observed CPU utilization (or other metrics like memory or custom metrics), enabling dynamic scaling of applications to match demand.
> 

> **ConfigMaps and Secrets**: **ConfigMaps** allow you to store non-sensitive configuration data that can be accessed by Pods. **Secrets** are used for storing sensitive data such as passwords, API tokens, or SSH keys, which can be securely injected into containers at runtime.
> 

> **Controller Manager**: The **controller manager** runs controllers that monitor the state of the cluster and ensure the desired state matches the actual state. These controllers handle tasks like managing ReplicaSets, Deployments, and stateful applications.
> 

> **Kubernetes API**: Kubernetes exposes a REST API that allows users and external systems to interact with the cluster programmatically. The API server is the entry point for all REST requests, ensuring security and communication between various Kubernetes components.
> 

### Key Features

- **Declarative Configuration**: Kubernetes allows users to declare the desired state of the system (e.g., how many replicas of an app should be running), and it will automatically ensure that the system matches that state.
- **Self-Healing**: Automatically reschedules failed or evicted Pods, replaces unhealthy containers, and rolls back deployments when necessary.
- **Service Discovery & Load Balancing**: Kubernetes provides internal DNS and load balancing for accessing services within the cluster.
- **Rolling Updates & Rollbacks**: Kubernetes supports zero-downtime rolling updates for deploying new versions of applications, with the ability to rollback in case of failure.
- **High Availability & Fault Tolerance**: Kubernetes can run across multiple nodes in a cluster, ensuring that workloads are distributed and remain highly available even in the event of node failures.
- **Multi-cloud and Hybrid Deployments**: Kubernetes supports running on **on-premises data centers**, **public clouds**, or a **hybrid environment**, allowing for flexible infrastructure management.

### Underlying Architecture

- **Master/Control Plane**: The control plane contains the components responsible for overall management of the cluster (e.g., scheduling, state management, etc.).
    - **API Server**: Exposes the Kubernetes API, which clients (e.g., `kubectl`) use to interact with the cluster.
    - **Scheduler**: Determines on which node a pod should run based on resource availability and constraints.
    - **Controller Manager**: Ensures that the system stays in the desired state by running controllers (e.g., Replication Controller, Deployment Controller).
    - **etcd**: The consistent, distributed key-value store that holds the configuration data and state of the cluster.
- **Worker Nodes**: These nodes run the workloads (containers), and each node contains:
    - **Kubelet**: An agent that runs on each node and ensures the containers are running as expected.
    - **Kube-Proxy**: Manages network rules and facilitates communication between services in the cluster.
    - **Container Runtime**: The software responsible for running containers (e.g., Docker, containerd).

## What is the relation of Kubernetes with Hardware Abstraction Layers?

> Kubernetes abstracts containerized applications from the underlying hardware and infrastructure, but it doesn’t directly manage physical resources (like CPU, memory, or storage).
> 

Instead, it interacts with **infrastructure abstraction systems** such as:

- **Cloud Platforms (e.g., AWS, Azure, GCP)**: These cloud platforms abstract compute, storage, and networking resources, and Kubernetes interfaces with them via cloud provider APIs. Kubernetes can dynamically provision and manage virtual machines, storage, and networking resources, abstracting the specifics of underlying hardware while providing elastic scalability.
- **Virtualization Platforms (e.g., VMware, OpenStack)**: These platforms abstract physical compute resources into virtual machines (VMs), and Kubernetes can manage containerized applications running within VMs. Kubernetes interfaces with the virtualization layer to schedule containers and manage resources.

## References

- https://kubernetes.io/
- …