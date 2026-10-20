---
tags: [data-collection]
---

# Tracing


> Practice of capturing and visualizing the flow of requests and activities within a distributed application to understand its performance and troubleshoot issues.
> 

> Distributed Tracing: A technique for tracing and visualizing requests and transactions as they move across distributed systems to understand performance bottlenecks and dependencies.
> 

## Tracing

> Time Passing Tree Model: Model the trace of functions.
> 

> This can be model using a “Phylogenetic Trees“.
> 

![image.png](data/technica/computation/system/evaluation/performace/conceptual-model-performance/assets/tracing/image.png)

## Tracing Model

A tracing model, in the context of distributed systems and observability, refers to a framework or approach for capturing and representing information about the flow of requests and activities within a complex, distributed application or system. The primary goal of a tracing model is to provide insights into how requests traverse various components, services, and interactions, helping developers and operators understand and analyze the system’s behavior and performance.

Key components and concepts typically associated with a tracing model include:

**Trace**: A trace represents the end-to-end journey of a request as it moves through the system. It encompasses all the individual activities and operations related to a particular request.

**Span**: A span represents a single unit of work or activity within a trace. Spans are used to record the start and end times of specific operations or events, such as function calls, database queries, or network requests.

**Trace ID**: A trace ID is a unique identifier assigned to each trace. It links all related spans together, allowing them to be associated with the same trace.

**Parent-Child Relationships**: Spans are organized in a hierarchical or parent-child relationship. Child spans represent sub-activities or operations that are part of a larger activity or transaction.

**Context and Metadata**: Each span can include additional context and metadata, such as service and operation names, tags, attributes, and error information. This data provides context and insights into the behavior of the system.

**Context Propagation**: The practice of passing contextual information, such as request IDs or correlation IDs, across distributed services and components to link related telemetry data.

**Timestamps and Durations**: Spans record timestamps for their start and end times, as well as the duration of the activity. This information is crucial for performance analysis and troubleshooting.

**Sampling**: To reduce the overhead of tracing, not all requests are traced. Sampling allows you to control which requests are captured as traces. Sampling strategies can include probabilistic sampling and adaptive sampling.

**Export and Storage**: Traces and spans are typically collected by tracing agents or instrumentation libraries within applications. They are then exported to a centralized tracing system or storage backend for analysis and long-term storage.

**Interoperability**: Tracing models often adhere to open standards and protocols to facilitate interoperability between different tracing systems and libraries. This allows organizations to choose the tracing tools that best suit their needs.

**Visualization and Analysis**: Traces and spans can be visualized and analyzed using tracing UIs and dashboards. These tools help in identifying bottlenecks, performance issues, and dependencies within the system.

Tracing models are essential for gaining observability into distributed systems, especially in microservices architectures, where requests can traverse multiple services and components. They enable developers and operators to troubleshoot issues, optimize performance, and gain insights into the end-to-end behavior of their applications. Popular tracing models and standards include OpenTracing, OpenTelemetry, and the W3C Trace Context specification.

## Universal Tracing Model

A universal tracing model, often referred to as a distributed tracing model, is a standardized approach for capturing and representing information about the flow of requests and activities within a distributed system. This model aims to provide a unified way to trace the execution path of a request as it moves through different components and services in a complex application or microservices architecture. Here are the key components and characteristics of a universal tracing model:

**Trace**: A trace represents the end-to-end journey of a request or transaction as it traverses various services and components. It provides a high-level view of how a request is processed.

**Span**: A span represents a single unit of work or activity within the trace. Spans are used to record the start and end times of specific operations, such as database queries, HTTP requests, or method invocations.

**Trace ID**: A trace ID is a unique identifier assigned to each trace. It links all related spans together, allowing them to be associated with the same trace.

**Parent-Child Relationships**: Spans are organized in a hierarchical or parent-child relationship, where a span can have one or more child spans. This structure reflects the flow of activities within the system.

**Context and Metadata**: Each span can include additional context and metadata, such as service and operation names, tags, attributes, and error information. This data provides valuable insights into the behavior of the system.

**Timestamps and Durations**: Spans record timestamps for their start and end times, as well as the duration of the activity. This information helps in performance analysis and debugging.

**Sampling**: To reduce overhead, not all requests are traced. Sampling allows you to control which requests are captured as traces. Common sampling strategies include probabilistic sampling and adaptive sampling.

**Export and Storage**: Traces and spans are typically collected by tracing agents or instrumentation libraries within applications. They are then exported to a centralized tracing system or storage backend for analysis.

**Interoperability**: A universal tracing model often adheres to open standards and protocols to facilitate interoperability between different tracing systems and libraries. This allows organizations to choose the tracing tools that best suit their needs.

**Visualization and Analysis**: Traces and spans can be visualized and analyzed using tracing UIs and dashboards. These tools help developers and operators gain insights into the performance, latency, and dependencies of their systems.

**Root Span**: Every trace starts with a root span, representing the beginning of a request. Child spans are created for subsequent activities and operations.

A universal tracing model is crucial for understanding the behavior and performance of complex, distributed systems, especially in microservices architectures. It provides observability into how requests are processed, where bottlenecks occur, and how services interact with each other, aiding in troubleshooting and optimizing application performance. Commonly used tracing standards, such as OpenTelemetry and W3C Trace Context, aim to promote consistency and interoperability in tracing across different platforms and ecosystems.

## Models

There are several trace data models and formats used in the field of distributed tracing, each with its own representation and semantics. Here’s a list of common trace data models:

**Zipkin Trace Data Model**: Zipkin uses a trace data model based on spans and trace IDs. Spans represent individual units of work, and trace IDs link spans together to form a trace. Each span has attributes, such as start and end times, duration, and service and operation names.

**Jaeger Trace Data Model**: Jaeger’s trace data model is similar to Zipkin and follows the OpenTelemetry format. It consists of spans, trace IDs, and attributes. Spans represent work within a distributed system, and trace IDs link them into a trace. Attributes include context information and metadata.

**OpenTelemetry Trace Data Model**: OpenTelemetry defines a trace data model that includes spans, trace IDs, and attributes. Spans represent individual operations, and trace IDs link them together to form a trace. Attributes provide context and additional information.

**OTLP (OpenTelemetry Protocol) Trace Data Model**: OTLP is a protocol used for transmitting trace data in a structured format. It defines a trace data model compatible with OpenTelemetry, including spans, trace IDs, attributes, and other trace-related metadata.

**Google Cloud Trace Data Model**: Google Cloud Trace uses a trace data model that includes spans and trace context. Spans represent units of work, and trace context is used to link spans into a trace. Additional metadata and annotations are included.

**AWS X-Ray Trace Data Model**: AWS X-Ray uses segments and subsegments as its trace data model. Segments represent the top-level operations, while subsegments represent subparts of those operations. They are organized into a hierarchy to form a trace.

**Datadog Trace Data Model**: Datadog’s trace data model includes traces, spans, and metrics. Traces consist of spans representing distributed work, and metrics capture performance and error information. Tags and attributes provide context.

**New Relic Trace Data Model**: New Relic APM uses a trace data model based on transactions, segments, and transaction events. Transactions represent top-level operations, segments represent subparts of transactions, and events capture details.

**Instana Trace Data Model**: Instana’s trace data model includes spans, traces, and snapshots. Spans represent units of work, traces link spans together, and snapshots capture performance and error information.

**LightStep Trace Data Model**: *: LightStep uses a trace data model based on spans, traces, and span references. Spans represent work, traces link spans into a trace, and span references define dependencies between spans.

**Dynatrace Trace Data Model**: *: Dynatrace uses a trace data model consisting of traces, spans, and services. Traces capture the journey of a request, spans represent individual work units, and services represent components.

These trace data models are used by various distributed tracing systems and observability platforms to capture, represent, and analyze the behavior and performance of applications and microservices in complex, distributed environments. The choice of trace data model may depend on the specific tracing solution you use or the interoperability requirements of your observability ecosystem.

## Refeernces

- [Tracing: Structured logging, but better (andydote.co.uk)](https://news.ycombinator.com/item?id=37562593)