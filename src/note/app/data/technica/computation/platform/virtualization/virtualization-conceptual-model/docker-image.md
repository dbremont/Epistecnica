---
tags: [container]
---

# Docker Image

- Related Virtualization: Conceptual Model: [Docker](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/docker.md)

> A Docker image is a lightweight, standalone, and executable package containing all the necessary components and dependencies to run a specific application or service. It is a fundamental building block in Docker containerization technology, which allows you to create, deploy, and manage applications consistently and isolatedly across different environments.
> 

> Docker uses a union filesystem, which allows multiple filesystems to be stacked on top of each other.
> 

> A Layer represents a set of file system changes. Each layer in a Docker image represents a filesystem snapshot.
> 

> Layers in a Docker image are read-only and cannot be modified after they are created.
> 

> Each instruction in a Dockerfile generates a new layer in the image. - For example, instructions like RUN, COPY, ADD, and ENV create new layers. - The result of these instructions is a filesystem change or configuration addition.
> 

Here are some key characteristics and components of a Docker image:

1. **Filesystem Snapshot**: A Docker image is essentially a snapshot of a filesystem that includes the application’s code, libraries, and other necessary files. It can also contain configuration settings, environment variables, and other runtime parameters.
2. **Layered Structure**: Docker images are composed of multiple layers. Each layer represents a set of changes or instructions applied to the base image. This layered structure enables efficient image sharing and versioning.
3. **Immutable**: Docker images are immutable, meaning they cannot be modified once created. If you need to change an idea, you typically create a new image with the desired changes, which may be based on an existing image.
4. **Reproducibility**: Docker images are designed to be highly reproducible. By defining the image’s construction process in a Dockerfile, you can ensure that the same idea can be recreated on different systems, guaranteeing consistency across environments.
5. **Portability**: Docker images are highly portable because they encapsulate everything needed to run an application, including its dependencies. You can run the same Docker image on different platforms, such as development laptops, testing servers, and production clusters.
6. **Registry**: Docker images are often stored in remote repositories called Docker registries (e.g., Docker Hub, Azure Container Registry, or private registries). These registries allow for easy sharing and distribution of images among team members and across organizations.
7. **Base Images**: Docker images are typically based on a parent or base image. Base images provide a minimal and optimized environment for specific types of applications (e.g., a Python base image for Python applications). You can build custom images on top of these base images.
8. **Versioning**: Docker images can be versioned using tags. Tags provide a way to label different versions of the same image. For example, you might have an idea tagged as “v1.0” and another as “v2.0” to represent different releases of an application.

## References

- https://docs.docker.com/reference/cli/docker/image/