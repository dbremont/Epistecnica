---
tags: [computer-network, protocol]
---

# Domain Name Service (DNS)

- [CoreDNS](note.html?n=technica/computation/telecom/telecom-conceptual-model/coredns.md)

> System that translates human-readable domain names, such as www.example.com, into IP addresses, which are used by computers to identify each other on the internet.
> 

> The **Domain Name System (DNS)** is a distributed, hierarchical naming architecture that resolves human-readable domain names into IP addresses and other resource records by recursively querying authoritative name servers via UDP/TCP over port 53, enabling scalable, fault-tolerant hostname-to-resource mapping across the internet.
> 

[https://pbs.twimg.com/media/GLswl51WAAA7gB-?format=jpg&name=large](https://pbs.twimg.com/media/GLswl51WAAA7gB-?format=jpg&name=large)

## Name System

### Structure of the Namespace

- **Syntax of names**: Defines how names are written and parsed. This includes supported characters, delimiters (e.g., dots in DNS), and extensibility mechanisms.
- **Types of records**: Specifies what kinds of data are associated with names (e.g., A, MX, TXT in DNS).
- **Possible structures**:
    - Flat: All names exist at the same level (e.g., early host files).
    - Hierarchical: Names are organized in a tree structure (e.g., DNS).
    - Other: Hybrid or distributed structures.

### Administrative Structure

- **Record storage**: Determines which servers are responsible for storing name records.
- **Lookup mechanism**: Describes how queries are routed to the appropriate servers.
- **Structure possibilities**:
    - Flat: Centralized or replicated database.
    - Hierarchical: Delegation of authority across levels (e.g., root → TLD → domain).

### Authoritative Structure

- **Authority and binding**: Who is allowed to assign names and update bindings.
- **Delegation**: How authority is passed down or distributed (e.g., parent domain delegates to child).
- **Design principle**: Ideally, the authoritative structure should mirror the administrative structure for clarity and coherence.

---

## DNS Structure

The **Domain Name System (DNS)** is organized hierarchically. Each level represents a component of the domain name:

1. **Root Level (`.`)**:
    - The top of the hierarchy.
    - Maintained by root name servers.
    - Knows the authoritative servers for each Top-Level Domain (TLD).
2. **Top-Level Domain (TLD)**:
    - Examples: `.com`, `.org`, `.net`.
    - Each TLD has authoritative servers for domains within it.
3. **Second-Level Domain**:
    - Registered by organizations or individuals.
    - Example: `example.com`.
4. **Subdomain**:
    - Created by adding prefixes.
    - Example: `www.example.com` or `mail.example.com`.
5. **Hostname**:
    - The specific endpoint (e.g., device or service).
    - Often the leftmost label: e.g., `mail` in `mail.example.com`.

DNS resolution starts at the root and proceeds down through the hierarchy until the final IP address is resolved.

---

## Implementation Details

### Recursive vs. Iterative Lookup

- **Recursive**:
    - Client sends a request to a resolver.
    - Resolver returns the final answer after contacting other servers as needed.
    - 
        - Simpler client
    - – Resolver vulnerable to DNS laundering attacks
- **Iterative**:
    - Resolver returns the address of the next server closer to the answer.
    - 
        - Simpler servers
    - 
        - Clients have more control and visibility (can cache more)
    - – Clients must handle timeouts/retries

### UDP Considerations

- DNS typically uses UDP (not TCP):
    - Avoids connection setup; reduces latency.
    - Reliable delivery managed via retransmissions.
    - TCP congestion control irrelevant for small queries.

### Security

- DNS was originally designed with minimal security.
- Focus is on **authenticity and integrity**, not confidentiality.
- **DNSSEC** adds digital signatures but is not widely adopted.
- Addresses:
    - **Spoofed responses**
    - **Cache poisoning attacks**

### Scalability

Key scalability goals: none of the following should grow linearly with system size:

- **Database state** per server
- **Routing metadata**
- **Load** on any individual server (especially root)
- **Name resolution path length**
- **Consistency traffic**, even with widespread caching

### Caching

Caching is critical for performance and scalability. It can occur at several levels:

- **Application-level**:
    - E.g., browsers cache DNS results to reduce lookup time.
- **Stub resolver** (e.g., BIND library):
    - Usually stateless; minimal caching.
- **Local resolver** (e.g., ISP's DNS):
    - Performs aggressive caching.

Caching benefits:

- **Temporal locality**: Same names requested frequently.
- **Spatial locality**: Requests for related names (e.g., assets on same domain).
- Zipf-like access patterns: small number of names dominate.
- Cooperative caching usually unnecessary – benefits saturate after ~10–20 clients.

**Negative caching** is also supported – failures (e.g., NXDOMAIN) are cached to reduce unnecessary queries.

## DNS Performace

> "**DNS Performance**" refers to how quickly and reliably the **Domain Name System (DNS)** resolves domain names (e.g., `example.com`) into IP addresses that computers use to communicate. DNS performance is crucial because it's one of the first steps in loading any website or service on the internet.
> 

### 🧩 **Key Factors Affecting DNS Performance**

1. **DNS Resolver Latency**
    - Time taken by your DNS resolver (e.g., Google DNS `8.8.8.8`, Cloudflare `1.1.1.1`) to respond to queries.
    - Geographical proximity and server load affect latency.
2. **Caching Efficiency**
    - Frequently requested domains are cached to reduce lookup time.
    - Poor caching can lead to repeated queries to authoritative servers, increasing load times.
3. **Propagation Time:** Time it takes for updated DNS records (like A, CNAME, MX) to propagate across DNS servers globally.
4. **Authoritative Server Performance**
    - How fast the server that owns the domain's zone file responds.
    - Often handled by registrars, CDNs, or custom infrastructure.
5. **Anycast Routing:** Modern DNS providers use anycast to route requests to the nearest data center, minimizing latency.
6. **TCP vs UDP**
    - Most DNS queries use UDP, which is faster but less reliable.
    - DNS over HTTPS (DoH) and DNS over TLS (DoT) use TCP, with added encryption but slightly higher latency.
7. **Timeouts and Retries:**  Failures or slow responses can trigger retries, increasing resolution time.

### 📈 **Common DNS Performance Metrics**

| Metric | Description |
| --- | --- |
| **Query Time (ms)** | Time taken for a DNS query to resolve. |
| **Cache Hit Ratio** | % of queries resolved via cache vs external fetch. |
| **Uptime (%)** | Availability of the DNS service. |
| **Throughput (QPS)** | Queries per second the system can handle. |
| **Error Rate** | % of failed or misrouted queries. |

### 🧪 **Tools to Measure DNS Performance**

- [**dnsperf.com**](https://www.dnsperf.com/) – Compare public DNS resolvers.
- [**Namebench**](https://github.com/google/namebench) – Benchmark DNS servers from your location.
- **`dig`, `nslookup`** – CLI tools to measure individual DNS query times.
- **Pingdom / WebPageTest** – Analyze overall site performance, including DNS lookup time.

### 🚀 **Ways to Improve DNS Performance**

- Use **fast public DNS resolvers** (Cloudflare `1.1.1.1`, Google `8.8.8.8`, Quad9 `9.9.9.9`).
- Enable **DNS caching** on local networks or servers.
- Reduce **TTL** for agility (increase TTL for fewer external lookups).
- Choose **authoritative DNS providers** with global PoPs and Anycast.
- Use **DNS prefetching** and **preconnect** hints in web pages.
- Consider **Private DNS**, **DoH**, or **DoT** for added security with reasonable performance trade-offs.

## DNS Record

> A **DNS (Domain Name System) record** is an entry in a DNS database that maps domain names to various types of data, most commonly IP addresses. DNS records are essential for translating human-readable domain names (like `example.com`) into machine-readable information (like `93.184.216.34`).
> 

[https://pbs.twimg.com/media/Ge7wR4LbUAA39RA?format=png&name=4096x4096](https://pbs.twimg.com/media/Ge7wR4LbUAA39RA?format=png&name=4096x4096)

### 🔧 Common Types of DNS Records

| Type | Name | Purpose |
| --- | --- | --- |
| `A` | Address Record | Maps a domain to an IPv4 address |
| `AAAA` | IPv6 Address Record | Maps a domain to an IPv6 address |
| `CNAME` | Canonical Name Record | Alias for another domain name |
| `MX` | Mail Exchange | Specifies mail servers for email delivery |
| `NS` | Name Server | Indicates authoritative name servers for a domain |
| `TXT` | Text Record | Carries arbitrary text; often used for verification (e.g. SPF, DKIM) |
| `SOA` | Start of Authority | Contains administrative info about the domain |
| `PTR` | Pointer Record | Maps an IP address to a domain name (reverse DNS) |
| `SRV` | Service Locator | Specifies services available in the domain (e.g. for VoIP) |

### Host

> In a **DNS record**, the **Host** field specifies the **subdomain** (or root domain) that the record applies to.
> 

| Host | Meaning |
| --- | --- |
| `@` | The root domain (e.g., `example.com`) |
| `www` | The subdomain `www.example.com` |
| `mail` | The subdomain `mail.example.com` |
| `*` | A wildcard for **any subdomain** (e.g., `anything.example.com`) |
| `blog` | The subdomain `blog.example.com` |

### 📌 Case Study

```
example.com.   3600 IN A     93.184.216.34
example.com.   3600 IN MX    10 mail.example.com.
www            3600 IN CNAME example.com.

```

### 🛠 Tools to Query DNS Records

- `dig example.com ANY`
- `nslookup example.com`
- `host example.com`

## Name Server Service

> Here are examples of both **private DNS server software** (you run them yourself) and **privacy-focused public DNS services** (you use their servers):
> 

### 🖥️ **Private DNS Server Software (Self-Hosted)**

> These let you **run your own DNS server** at home, in a company, or on a VPS.
> 

| Software | Description |
| --- | --- |
| **Pi-hole** | Blocks ads and trackers network-wide; often used on Raspberry Pi. |
| **Unbound** | Lightweight validating, recursive, caching DNS resolver with DNSSEC support. |
| **Bind9** | Full-featured DNS server used by ISPs and enterprises; highly configurable. |
| **dnsmasq** | Small and fast DNS/DHCP server, ideal for embedded devices or local networks. |
| **CoreDNS** | Modern DNS server used in Kubernetes clusters. Highly modular and programmable. |
| **Knot Resolver** | High-performance resolver with DNSSEC and modular plugin support. |
| **PowerDNS (Recursor)** | DNS server with a focus on performance and flexibility; often used by ISPs. |

### 🌐 **Privacy-Focused Public DNS Services**

> You don’t run these yourself, but they offer **enhanced privacy, speed, and filtering**.
> 

| Provider | IP Address | Features |
| --- | --- | --- |
| **Cloudflare (1.1.1.1)** | `1.1.1.1` / `2606:4700:4700::1111` | Fast, no logging, DNS over HTTPS (DoH) & TLS (DoT). |
| **Google Public DNS** | `8.8.8.8` / `2001:4860:4860::8888` | Reliable, fast, but logs anonymized data. |
| **Quad9** | `9.9.9.9` | Blocks malicious domains, DNSSEC, privacy-focused. |
| **AdGuard DNS** | `94.140.14.14` | Blocks ads, trackers, phishing; customizable. |
| **NextDNS** | (Custom IPs) | Fully configurable filter lists, logs, analytics. |
| **OpenDNS** | `208.67.222.222` | Parental controls, content filtering. |
| **CleanBrowsing** | `185.228.168.9` | Family-safe filtering (Adult/Malware/DNS-only options). |

## Secure DNS

- DNS over HTTP.
- …

## References

- [DNS](https://courses.cs.washington.edu/courses/csep552/13sp/lectures/1/dns.txt)
- [Time to live (TTL)](https://en.wikipedia.org/wiki/Time_to_live)
- [Negative Cache](https://en.wikipedia.org/wiki/Negative_cache)
- Jung, J., Sit, E., Balakrishnan, H., & Morris, R. (2001). DNS Performance and the Effectiveness of Caching. 153–167.
- Son, S., & Shmatikov, V. (2010). The Hitchhiker’s Guide to DNS Cache Poisoning. 466–483.
- Jung, J., Sit, E., Balakrishnan, H., & Morris, R. (2001). DNS Performance and the Effectiveness of Caching. 153–167. https://doi.org/10.1145/505202.505223
- Son, S., & Shmatikov, V. (2010). The Hitchhiker’s Guide to DNS Cache Poisoning. 466–483.
- Mockapetris, P. (1983). [RFC 883] Domain Names: Implementation specification.
- Mockapetris, P. (1987). [RFC 882] Domain Names-Concepts and Facilities.
- Mockapetris, P., & Dunlap, K. J. (1988). Development of the Domain Name System. 123–133.
- [The 6 Best Free Dynamic DNS Providers](https://www.makeuseof.com/tag/5-best-dynamic-dns-providers-can-lookup-free-today/)
- [Naming](note.html?n=technica/computation/system/programming/conceptual-model-programming/naming.md)
- https://dnschecker.org/
- https://www.dnsperf.com/
- https://www.nic.do/
- https://en.wikipedia.org/wiki/DNS_over_HTTPS