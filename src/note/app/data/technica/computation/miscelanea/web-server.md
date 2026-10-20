# Web Server

- [Web Framework](note.html?n=technica/computation/miscelanea/web-framework.md)

> A **web server** is a **stateful, network-facing software system that implements HTTP(S) semantics over TCP/QUIC transport, orchestrates concurrency, and maps requests to resources or applications**, serving as the foundational **application-layer endpoint** of the web.
> 

## Server Space

| Server | Concurrency Model | Key Features | Typical Use Cases | Performance Notes |
| --- | --- | --- | --- | --- |
| **Apache HTTP Server** | Process-per-connection (Prefork), Thread-per-connection (Worker), Event-driven (Event MPM) | Rich module ecosystem, `.htaccess`, dynamic configuration, CGI/FastCGI support | Shared hosting, legacy PHP apps, environments needing per-directory overrides | Higher memory footprint under high concurrency; flexible but less efficient for static content |
| **Nginx** | Event-driven, async non-blocking I/O (single-threaded workers, each with event loop) | Reverse proxy, load balancing, caching, TLS termination, efficient static file serving | High-concurrency environments, microservices reverse proxy, CDN edges | Very low memory usage per connection; excels at handling 10k–1M concurrent clients |
| **Lighttpd** | Event-driven async (like Nginx) | Lightweight, optimized for low memory, FastCGI support | Embedded systems, low-resource servers | Faster than Apache for static content, but less feature-rich than Nginx |
| **Caddy** | Event-driven, Go-based concurrency | Automatic HTTPS (Let’s Encrypt), modern config, built-in reverse proxy | Developer-friendly setups, quick TLS deployment | Lower raw throughput than Nginx, but easier TLS automation |
| **Microsoft IIS** | Thread pool + I/O Completion Ports (IOCP) | Deep Windows integration, ASP.NET/ISAPI support, GUI management | Enterprise Windows environments | Good performance on Windows, but tied to Windows ecosystem |
| **Tomcat** (Servlet Container) | Thread-per-request model (Java threads) | Java EE servlet/JSP engine, integration with Spring/Java apps | Java enterprise applications | Not optimized for static files; often run behind Nginx/Apache |
| **Node.js (as web server)** | Event loop with async I/O (libuv) | JavaScript runtime, full app server, not just static serving | Real-time apps (chat, APIs, microservices) | Excellent concurrency, but single-threaded bottlenecks possible |
| **Cherokee** | Event-driven async | Web-based admin UI, reverse proxy features | Experimental/educational, ease of admin | Never gained mass adoption; lower ecosystem support |
| **LiteSpeed** | vent-driven, async non-blocking I/O (proprietary implementation) | Drop-in Apache replacement, HTTP/3/QUIC support, LSAPI (optimized PHP handler), caching, built-in security features | High-performance hosting (esp. WordPress/PHP), commercial hosting providers | Very high throughput and efficient PHP handling; proprietary (open-source fork exists: OpenLiteSpeed) |

## References

- https://en.wikipedia.org/wiki/Web_server
- https://en.wikipedia.org/wiki/Client%E2%80%93server_model
- https://github.com/dbremont/documentorum/blob/main/component/multinode/NGINX.md
- https://github.com/dbremont/documentorum/blob/main/component/multinode/Apache%20HTTP%20Server.md