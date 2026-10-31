---
tags: [stream-processing-system]
---

# Data Streaming


> 

QA:

- How are files downloaded from the server to the browser? For example, videos.

## Protocols

> 

| **Technology** | **Description** | **Primary Use Case** | **Features** | **Limitations** |
| --- | --- | --- | --- | --- |
| **HLS (HTTP Live Streaming)** | Adaptive bitrate streaming protocol developed by Apple. | Live and on-demand video streaming. | - Works with standard HTTP servers.  - Supports adaptive bitrate streaming.  - Widely supported on Apple devices. | - High latency in live streaming.  - Requires segmenting video into small chunks. |
| **DASH (Dynamic Adaptive Streaming over HTTP)** | Open standard for adaptive bitrate streaming, often used in OTT platforms. | Video-on-demand and live streaming. | - Codec-agnostic.  - Wide range of client and CDN support.  - Supports adaptive streaming. | - More complex to implement compared to HLS. |
| **CMAF (Common Media Application Format)** | A standard for packaging content for adaptive streaming, compatible with HLS and DASH. | Unified streaming workflows. | - Enables low-latency streaming.  - Simplifies multi-format workflows.  - Reduces CDN costs. | - Relatively new, requiring updated tools and players. |
| **RTMP (Real-Time Messaging Protocol)** | Protocol initially designed for live video delivery, commonly used for ingest to CDNs. | Video ingest for streaming platforms. | - Low latency.  - Easy to implement with tools like OBS. | - Deprecated for direct playback in browsers.  - Replaced by HLS/DASH for distribution. |
| **WebRTC (Web Real-Time Communication)** | Real-time communication protocol supporting peer-to-peer streaming over HTTP/UDP. | Real-time video chats, live-streaming events. | - Ultra-low latency.  - Supports bidirectional communication. | - Complex setup.  - Not suitable for large-scale, multi-user live broadcasting. |
| **SSE (Server-Sent Events)** | HTTP-based protocol for unidirectional, server-to-client updates. | Real-time notifications, event streaming. | - Lightweight and simple.  - Works over HTTP/1.1. | - Unidirectional (server-to-client only).  - Not ideal for high-frequency updates. |
| **LL-HLS (Low-Latency HLS)** | Extension of HLS designed for low-latency live video streaming. | Real-time sports and live events. | - Low latency (<2s).  - Backward compatible with traditional HLS. | - Requires CDN and player support for LL-HLS. |
| **WebSockets** | Full-duplex, low-latency communication protocol over TCP. | Real-time chat, notifications, and gaming. | - Bidirectional communication.  - Native support in browsers.  - Low overhead compared to HTTP polling. | - Not suitable for large-scale media streaming.  - Requires a persistent connection for operation. |
| **Comet (HTTP Long Polling)** | Simulates real-time communication by keeping HTTP connections open for extended periods. | Real-time notifications in legacy systems. | - Works in environments without WebSocket or SSE support. | - Inefficient due to repeated HTTP connections.  - Higher latency compared to WebSockets. |
| **CMAF-LL** | Low-latency streaming using CMAF packaging. | Ultra-low latency live streaming. | - Compatible with DASH and HLS.  - Supports latency as low as 1-2 seconds. | - Requires specialized setup and tools. |
| **MPEG-TS over HTTP** | Traditional MPEG transport stream delivery via HTTP. | IPTV and legacy live streaming systems. | - Compatible with older streaming setups. | - High latency and inefficient for modern adaptive streaming. |
| **Progressive HTTP** | Non-adaptive HTTP-based delivery where files are downloaded sequentially. | Small-scale video streaming. | - Simple to implement.  - Works with standard HTTP servers. | - No support for adaptive bitrate.  - High bandwidth usage. |
| **QUIC Streaming** | HTTP/3-based protocol for low-latency streaming over QUIC (UDP). | Modern low-latency video streaming. | - Built-in multiplexing.  - Resilient to packet loss. | - Requires updated infrastructure and client support. |
| **SRT (Secure Reliable Transport)** | Open-source protocol designed for secure, low-latency video streaming. | Live broadcasting and contribution. | - Highly reliable for low-latency connections.  - Resilient to network jitter and packet loss. | - Limited direct playback support; primarily used for ingest and transport. |
| **RTP over HTTP** | Real-time Transport Protocol adapted for HTTP delivery. | Real-time media transport. | - Low-latency and suitable for live events. | - Less commonly supported compared to HLS and DASH. |
| **FMP4 Streaming** | Fragmented MP4 (fMP4) files streamed over HTTP. | Adaptive streaming workflows. | - Compatible with HLS and DASH. | - Requires packaging tools to create fMP4 segments. |
| **Long Polling** | Client sends a request to the server and waits for a response before closing the connection, simulating real-time updates. | Real-time chat, event notifications, legacy systems. | - Works with any HTTP server.  - Simple to implement in legacy systems. | - Requires re-connection for each new update, leading to higher server load.  - Higher latency than WebSockets. |
| **Push Notifications** | Mechanism for sending real-time notifications from a server to a client, even when the client is not actively interacting. | Mobile apps, web apps, and notifications. | - Supports background updates and notifications.  - Works even when client is not active. | - Requires support for push service (e.g., Firebase Cloud Messaging for mobile).  - Latency and reliability depend on network conditions. |
| **HTTP/2 Server Push** | Extension of HTTP/2 allowing the server to send resources to the client without explicit requests. | Reducing latency by preemptively pushing resources. | - Built into HTTP/2.  - Reduces the need for multiple requests to fetch resources. | - Does not support true real-time streaming.  - Limited to resource delivery, not for full-duplex communication. |

## Uses

| **Type** | **System** | **Description** | **Primary Use Case** | **Protocol/Transport** |
| --- | --- | --- | --- | --- |
| **Video Streaming** | **HLS (HTTP Live Streaming)** | Adaptive bitrate streaming protocol for delivering media over HTTP. | Live video streaming, on-demand video | HTTP, HLS |
|  | **DASH (Dynamic Adaptive Streaming over HTTP)** | Similar to HLS, used for adaptive streaming via HTTP. | Streaming video and multimedia content | HTTP, MPEG-DASH |
|  | **RTMP (Real-Time Messaging Protocol)** | Protocol for delivering audio, video, and data over the internet. | Live streaming platforms, media streaming | TCP/IP, RTMP |
|  | **WebRTC (Web Real-Time Communication)** | Peer-to-peer communication protocol for live video and audio streaming. | Video conferencing, live interaction | WebSockets, UDP |
|  | **Apple AirPlay** | Wireless streaming protocol for media content. | Video and audio streaming between Apple devices | Wi-Fi, AirPlay |
| **Event Streaming** | **Apache Kafka** | A distributed streaming platform for building real-time data pipelines. | Event streaming, log aggregation, real-time analytics | TCP/IP |
|  | **Apache Pulsar** | A distributed messaging and event streaming platform. | Messaging, real-time event processing | TCP/IP, HTTP |
|  | **Amazon Kinesis** | A fully managed platform for real-time streaming data. | Real-time analytics, video streaming, IoT telemetry | TCP/IP |
|  | **Google Cloud Pub/Sub** | A messaging service for event-driven architectures. | Event-driven processing, log aggregation | HTTP/HTTPS, WebSockets |
| **Real-Time Analytics** | **Apache Flink** | A stream processing framework for real-time data analytics and processing. | Real-time data processing, event-driven applications | TCP/IP |
|  | **Streamsets** | A data integration platform for building streaming data pipelines. | Data pipeline building, real-time data processing | HTTP, Kafka, various APIs |
|  | **Apache Samza** | A distributed stream processing framework designed for large-scale data. | Real-time analytics, data pipeline processing | TCP/IP |
|  | **Confluent (Kafka)** | An enterprise platform built around Apache Kafka. | Data integration, stream processing, real-time apps | TCP/IP |
| **Messaging Systems** | **RabbitMQ** | A general-purpose messaging broker that supports stream processing. | Queue-based message processing, real-time alerts | AMQP, MQTT, HTTP |
|  | **NATS** | A lightweight, high-performance messaging system. | IoT, microservices, edge applications | TCP/IP, WebSockets |
|  | **Redis Streams** | An extension of Redis to support stream data processing. | Real-time data storage, event-driven systems | TCP/IP |
| **IoT Streaming** | **Azure IoT Hub** | A cloud platform for IoT device management and data streaming. | Real-time IoT data ingestion, telemetry | MQTT, HTTPS |
|  | **AWS IoT Core** | Managed cloud service for connecting IoT devices and handling streaming data. | IoT data processing, telemetry, real-time analytics | MQTT, HTTPS |
| **Cloud Data Streaming** | **Azure Event Hubs** | A highly scalable cloud event streaming service for large-scale data ingestion. | IoT telemetry, real-time analytics | AMQP, HTTPS |
|  | **Google Cloud Dataflow** | Managed service for stream and batch data processing. | Stream processing, ETL jobs | HTTP, Beam SDK |

## References

- https://en.wikipedia.org/wiki/Streaming_media
- https://en.wikipedia.org/wiki/Comet_(programming)
- https://news.ycombinator.com/item?id=35937554
- …