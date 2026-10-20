---
tags: [tool]
---

# CoreDNS

- [Domain Name Service (DNS)](note.html?n=technica/computation/telecom/telecom-conceptual-model/domain-name-service-dns.md)

> **CoreDNS** is a fast, flexible, and extensible **DNS server** written in Go, designed as both a **general-purpose authoritative and recursive DNS server** and a **DNS-based service discovery tool**, particularly in **cloud-native environments** like **Kubernetes**.
> 

## 🧠 **Technical Definition of CoreDNS**

**CoreDNS** is a **modular DNS server framework** that:

- Implements the **DNS protocol (RFC 1035, 2181, etc.)**
- Operates as a **chain of plugins**, each of which handles DNS queries at specific stages of processing
- Uses a **declarative configuration file** (`Corefile`) to define server behavior
- Can act as:
    - A **recursive resolver**
    - An **authoritative nameserver**
    - A **DNS proxy**
    - A **service discovery backend**
    - Or a **custom DNS function processor**

## 🔧 **CoreDNS Architecture (Plugin-Based)**

- **Pipeline execution model**: Incoming queries are processed through a **chain of plugins**.
- Each plugin conforms to a standard **interface**:
    
    ```go
    ServeDNS(ctx context.Context, w dns.ResponseWriter, r *dns.Msg) (int, error)
    
    ```
    
- Plugins may **handle, modify, forward, or block** queries.

## 🧱 **CoreDNS Plugins (Examples)**

| Plugin | Function |
| --- | --- |
| `forward` | Forwards DNS queries to upstream resolvers |
| `cache` | Caches DNS responses |
| `kubernetes` | Integrates with the Kubernetes API for service discovery |
| `file` | Serves zones from a static zone file |
| `hosts` | Reads `/etc/hosts`-like files |
| `template` | Generates synthetic DNS responses based on rules |
| `rewrite` | Rewrites query names, types, or classes |

## 📦 **Deployment Contexts**

- **Default DNS service in Kubernetes** (as a replacement for `kube-dns`)
- **Containerized and cloud-native** applications
- DNS-based **microservice discovery**
- Embedded **DNS service in edge appliances or IoT** systems

## ⚙️ **Key Technical Features**

- Written in **Go** (Golang)
- Uses **Caddy’s plugin model**
- Supports **DNS over TCP and UDP**
- Supports **DNSSEC**
- High-performance due to **concurrent, non-blocking architecture**
- **Hot-reloadable configuration** via Corefile
- Extensible with **custom plugins**

## 🧪 Minimal Corefile for Forwarding

```
. {
  forward . 1.1.1.1 8.8.8.8
  log
  cache
}

```

This makes CoreDNS:

- Listen on port 53
- Forward all queries to Cloudflare and Google
- Log queries
- Cache results

## References

- https://coredns.io/
- [**Kubernetes**](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/kubernetes.md)