---
tags: [container]
---

# Docker Network

- Related Virtualization: Conceptual Model: [Docker](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/docker.md)

Docker uses different networking models to facilitate communication between containers, including:

- **Bridge**: The default network driver for standalone containers. It creates an isolated network for containers to communicate with each other.
- **Host**: Removes network isolation between the container and the host, allowing containers to share the host's network stack.
- **Overlay**: Allows containers across multiple Docker hosts to communicate with each other as if they were on the same local network.