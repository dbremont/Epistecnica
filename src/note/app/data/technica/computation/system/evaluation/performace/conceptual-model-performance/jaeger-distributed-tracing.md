---
tags: [tool]
---

# Jaeger Distributed Tracing


> Jaeger is an open-source distributed tracing system that helps developers monitor and troubleshoot the performance of microservices and distributed applications by providing insights into the flow of requests and dependencies between services.
> 

## Ports

In a Jaeger distributed tracing setup, various components communicate with each other and with the applications being traced using specific ports. Here are some of the common ports used in a Jaeger deployment and their meanings:

**Jaeger Agent Port (default: 6831/udp)**: - The Jaeger agent listens on this UDP port to receive trace data from instrumented applications. - It collects traces and forwards them to the Jaeger collector for further processing.

**Jaeger HTTP Collector Port (default: 14268)**: - The Jaeger collector listens on this HTTP port to accept incoming trace data from Jaeger agents and applications using HTTP/JSON format. - It performs validation, processing, and storage of trace data before forwarding it to the storage backend.

**Jaeger gRPC Collector Port (default: 14250)**: - The Jaeger collector listens on this gRPC port to accept incoming trace data from Jaeger agents and applications using the gRPC protocol. - It performs similar functions as the HTTP collector but uses the gRPC protocol for communication.

**Jaeger Query Port (default: 16686)**: - The Jaeger query service provides a web-based user interface for querying and visualizing trace data. - The Jaeger UI communicates with the query service on this port to display trace information.

**Jaeger Ingestion Port (default: 14267)**: - The Jaeger ingestion service is responsible for handling ingested traces and forwarding them to the collector. - This port is used internally within the Jaeger components for communication.

**Jaeger Agent Thrift Compact Port (default: 6832/udp)**: - In some Jaeger configurations, the Jaeger agent may use this UDP port to accept traces in the Thrift Compact format.

**Jaeger HTTP API Port (default: 16686)**: - The Jaeger query service also exposes an HTTP API on this port for programmatic access to trace data. - Applications or tools can make HTTP requests to retrieve trace information.

**Zipkin HTTP Collector Port (default: 9411)**: - Some Jaeger deployments include support for the Zipkin collector API on this port. - It allows Zipkin-compatible clients and applications to send trace data to Jaeger.

It’s important to note that the default port numbers can be customized in your Jaeger configuration if needed. The port numbers mentioned here are the defaults and are commonly used in Jaeger setups. When deploying Jaeger in a production environment, you may need to adjust firewall rules and network configurations to ensure that the necessary ports are accessible and properly secured.

## References

- [Jaeger: open source, end-to-end distributed tracing](https://www.jaegertracing.io/)