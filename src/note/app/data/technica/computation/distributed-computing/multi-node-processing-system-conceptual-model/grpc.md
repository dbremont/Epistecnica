---
tags: [computer-network, protocol, web-framework, web-server]
---

# gRPC


> gRPC is a high-performance, open-source remote procedure call (RPC) framework that enables efficient communication and data exchange between distributed applications.
> 

**It’s particularly well-suited for building microservices due to its features:**

1. **Efficiency**: gRPC uses HTTP/2 as its transport protocol, enabling multiplexing of requests and responses over a single connection. This minimizes latency and reduces overhead, making it efficient for communication between microservices.
2. **Strongly Typed Contracts**: gRPC relies on Protocol Buffers (Protobufs) for service contract definition. This ensures a clear and well-defined interface between microservices, making it easier to maintain and update services without breaking compatibility.
3. **Streaming**: gRPC supports both unary (single request, single response) and streaming interactions. This is beneficial for scenarios like real-time data updates, where microservices need to push data to each other.
4. **Code Generation**: gRPC generates client and server code from your service definition, providing a consistent and type-safe way to communicate between microservices. This reduces the likelihood of errors and inconsistencies.
5. **Language Agnostic**: gRPC supports multiple programming languages, making it easy to build microservices using different technologies while still enabling them to communicate seamlessly.
6. **Load Balancing**: gRPC offers built-in support for client-side load balancing, allowing requests to be distributed across multiple instances of a microservice for improved performance and fault tolerance.
7. **Security**: gRPC provides strong authentication and encryption options, ensuring that communication between microservices remains secure.
8. **Bi-directional Communication**: gRPC supports bidirectional streaming, which can be useful for scenarios where microservices need to have ongoing conversations or exchange data in real-time.

In summary, **gRPC** is a powerful tool for modeling microservices due to its performance, contract definition capabilities, and support for various communication patterns. It simplifies the process of building and maintaining microservices by providing a robust and efficient communication framework.

## References

[gRPC](https://grpc.io/)

Ismael Gonzalez. 2020. Building Microservice APIs Using GRPC. Ph.D. Dissertation. California State University, Long Beach, CA.

Ruwan Fernando. 2019. Evaluating Performance of REST vs. gRPC. https://medium.com/@EmperorRXF/evaluating-performance-of-rest-vs-grpc-1b8bdf0b22da

Google. 2021. Generate gRPC Code. https://www.grpc.io/docs/languages/python/quickstart/Google Scholar

Google. 2021. Introduction to gRPC. https://grpc.io/docs/what-is-grpc/introduction/

Bershad, B. N., Anderson, T. E., Lazowska, E. D., & Levy, H. M. (n.d.). Lightweight Remote Procedure Call.

Birrell, A. D., & Nelson, B. J. (1983). Implementing remote procedure calls. Proceedings of the 9th ACM Symposium on Operating Systems Principles, SOSP 1983, 3. https://doi.org/10.1145/800217.806609

McEniry, Chris Mac. “Using gRPC with Go.” login Usenix Mag. 43 (2018): n. pag.

[GRPC: A high performance, open source, general RPC framework](https://news.ycombinator.com/item?id=9114748)

[gRPC benchmark results (github.com/lesnyrumcajs)](https://news.ycombinator.com/item?id=27085265)

[gRPC in Production (sourcegraph.com)](https://news.ycombinator.com/item?id=14822294)

[A detailed comparison of REST and gRPC (kreya.app)](https://news.ycombinator.com/item?id=35711196)

[Open-RPC](https://open-rpc.org/)

[gRPC: Up and Running](https://www.oreilly.com/library/view/grpc-up-and/9781492058328/)

[gRPC-Gateway](https://grpc-ecosystem.github.io/grpc-gateway/)

[grpcurl](https://github.com/fullstorydev/grpcurl)