---
tags: [container]
---

# Container Registry

- Related Virtualization: Conceptual Model: [Docker](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/docker.md)

> If you're looking for **open-source** **Docker registry hosts**, there are several options available that allow you to store and distribute Docker images. A Docker registry is essentially a repository for Docker images, providing an environment where you can push, pull, and manage your Docker images.
> 

Here are some popular open-source Docker registry solutions:

1. **Harbor**: Developed by VMware, Harbor is an open-source registry that secures artifacts with policies and role-based access control, ensures images are scanned and free from vulnerabilities, and signs images as trusted. Harbor also extends the open-source Docker Distribution by adding the functionalities usually required by an enterprise, such as security, identity, and management.
2. **Portus**: An authorization service and frontend for Docker registry (distribution), providing tools to administer the registry and control access to it.
3. **Docker Distribution (Registry)**: This is the open-source project that Docker Hub is built on. It can be deployed on your own infrastructure, and you can integrate it with your authentication providers. It is ideal for storing and managing your Docker images internally or in a private cloud environment.
4. [**Quay.io](http://quay.io/) by Red Hat (CoreOS Quay)**: Although there is a commercial version, [Quay.io](http://quay.io/) also offers an open-source version called Quay. It can be self-hosted, and it provides features like security scanning and automated builds.
5. **JFrog Artifactory**: Although not entirely open-source for all its features, JFrog Artifactory has an open-source version that supports Docker registry among other package formats. It is widely used in the industry for managing artifacts and provides robust features around access control, artifact handling, and integration with CI/CD pipelines.
6. **Kraken by Uber**: An open-source, peer-to-peer docker registry designed to handle thousands of concurrent users and millions of images without significant increases in latency or resource usage.