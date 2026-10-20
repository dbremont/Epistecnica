# Video Streaming


> **Video streaming** is the process of delivering video content over the internet in real-time, allowing users to watch the video without having to download the entire file beforehand.
> 

QA:

- What is a video?
- How videos are display?
- What is **video streaming**?
- How videos are represented?

## Protocols

> 

| **Criteria** | **HLS (HTTP Live Streaming)** | **DASH (Dynamic Adaptive Streaming over HTTP)** | **RTSP (Real-Time Streaming Protocol)** | **RTMP (Real-Time Messaging Protocol)** | **WebRTC (Web Real-Time Communication)** |
| --- | --- | --- | --- | --- | --- |
| **Protocol Type** | HTTP-based | HTTP-based | TCP-based (client-server) | TCP-based (client-server) | Peer-to-peer (also client-server) |
| **Adaptive Bitrate** | Yes | Yes | No | No | Yes |
| **Latency** | High (usually 10-30 seconds) | Medium (depends on buffer size) | Low (real-time) | Low (real-time) | Very low (real-time) |
| **Supported Media Formats** | MP4, TS | MP4, WebM | RTSP streams | FLV (Flash Video) | VP8/VP9, H.264, Opus (WebRTC supported formats) |
| **Content Delivery** | Server to client via HTTP | Server to client via HTTP | Client requests server for video stream | Server to client (usually via Flash player) | Peer-to-peer or server for relay |
| **Scalability** | Very scalable | Very scalable | Less scalable (requires special servers) | Scalable, but less than HTTP-based | Highly scalable for direct connections, less for relayed |
| **Streaming Types** | Live, On-demand | Live, On-demand | Live | Live | Live (real-time video/audio) |
| **Error Recovery** | Excellent (due to HTTP and chunking) | Good (via HTTP, but requires extra buffering) | Limited error handling | Limited error handling | Strong error correction (due to WebRTC) |
| **Compatibility** | Broad browser support | Broad browser support | Limited browser support | Limited browser support | Supported in modern browsers (Chrome, Firefox, etc.) |
| **Encryption/DRM** | Yes (via AES encryption) | Yes (via encryption and DRM solutions) | Yes (via RTSP security mechanisms) | Yes (via RTMP encryption) | Yes (via SRTP and encryption) |
| **Popular Use Cases** | Live streaming, large-scale broadcasts, adaptive streaming | Video on demand, live streaming, adaptive streaming | Security camera feeds, surveillance, IP cams | Flash-based video players, streaming platforms | Video conferencing, real-time communication, gaming |
| **Latency Handling** | Higher latency, good for non-interactive content | Medium latency, suitable for adaptive delivery | Real-time (low latency) | Real-time (low latency) | Ultra-low latency, suitable for interactive applications |

## Servers

> 

| **Video Server** | **Supported Protocols** | **Use Case** | **Key Features** | **Scalability** | **Licensing** | **Popular Platforms** |
| --- | --- | --- | --- | --- | --- | --- |
| **Nginx with RTMP module** | RTMP, HLS, HDS, RTSP | Live streaming, On-demand | Low-latency live streaming, adaptive bitrate support, HTTP streaming | Highly scalable | Open source (MIT license) | YouTube, Twitch (for RTMP) |
| **Wowza Streaming Engine** | RTMP, HLS, DASH, HDS, RTSP, MPEG-DASH | Live and on-demand streaming | Adaptive bitrate, live transcoding, DRM support | Very scalable | Commercial (paid) | Media companies, broadcasters |
| **Red5** | RTMP, WebRTC, HLS, RTSP, MPEG-DASH | Live and interactive video streaming | WebRTC support, real-time communication, low-latency | Scalable with clusters | Open source (Apache License 2.0) | Educational platforms, real-time apps |
| **VLC Media Server** | RTSP, HLS, HTTP | Video streaming, On-demand | Stream live video, media server for media files, supports various formats | Medium scalability | Open source (GPL) | Home servers, personal use |
| **Kurento Media Server** | WebRTC, RTSP, RTMP, HLS, SIP | Interactive video, WebRTC applications | Real-time communication, live video call support | Scalable (clustered) | Open source (Apache License 2.0) | WebRTC applications, video conferencing |
| **Flussonic Media Server** | HLS, MPEG-DASH, RTSP, RTMP | Live streaming, DVR, on-demand video | Time-shifted TV, transcoding, stream recording | Highly scalable | Commercial (paid) | IPTV, Broadcast TV, OTT services |
| **Streamroot** | HLS, DASH, RTMP, WebRTC | Peer-to-peer video streaming, adaptive bitrate | Peer-to-peer support, advanced CDN, live streaming | Highly scalable (peer-to-peer) | Commercial (paid) | OTT providers, large-scale video platforms |
| **Plex Media Server** | HTTP, HLS, RTSP | Home media server, On-demand streaming | Easy setup, media library management, transcoding | Medium scalability | Free, Premium version available | Home servers, personal use |
| **MistServer** | RTMP, HLS, DASH, RTSP, WebRTC, Icecast | Live streaming, on-demand video, interactive video | Low-latency, HTML5 streaming, adaptive bitrate | Scalable (via cloud) | Commercial (paid) | IPTV, OTT, broadcast solutions |
| **Airflow Media Server** | HLS, RTMP, HDS, RTSP | Live and on-demand streaming | Customizable CDN, HLS transcoding, adaptive streaming | Scalable via clusters | Commercial (paid) | Live video streaming services |
| **JWPlayer** | HLS, DASH, RTMP | On-demand video, Live streaming | Video player integration, cloud streaming, DRM | Very scalable | Commercial (paid) | Online media platforms, corporate video |

## References

- [Firefox](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/firefox.md)
- [‣](https://app.notion.com/p/65b8a74e2a474ef2b72983934b205626?pvs=21)
- [Data Streaming](note.html?n=technica/computation/telecom/telecom-conceptual-model/data-streaming.md)
- [Video Processing](note.html?n=technica/computation/graphical-heterogeneous-high-performance-computing-system/graphical-computing-system/video-processing.md)
- https://bytebytego.com/courses/system-design-interview/design-youtube
- https://news.ycombinator.com/item?id=22748247
- https://news.ycombinator.com/item?id=29793526
- https://news.ycombinator.com/item?id=37823160
- https://news.ycombinator.com/item?id=5651008
- https://news.ycombinator.com/item?id=31642292
- https://news.ycombinator.com/item?id=11815417
- https://news.ycombinator.com/item?id=6367018
- https://news.ycombinator.com/item?id=19069560
- https://news.ycombinator.com/item?id=27952725
- https://news.ycombinator.com/item?id=16930229
- https://news.ycombinator.com/item?id=10404974
- https://news.ycombinator.com/item?id=1052106
- https://news.ycombinator.com/item?id=9038310
- https://news.ycombinator.com/item?id=11815417
- https://news.ycombinator.com/item?id=6367018
- https://news.ycombinator.com/item?id=19069560
- https://news.ycombinator.com/item?id=27952725
- https://news.ycombinator.com/item?id=29793526
- https://news.ycombinator.com/item?id=37823160
- https://github.com/videojs/video.js
- https://github.com/video-dev/hls.js
- https://github.com/sampotts/plyr
- https://github.com/phoboslab/jsmpeg
- 
- https://github.com/dbremont/video-stream-lab
- https://github.com/jinyucn/Video-Streaming-Research-Papers/blob/main/Repository%20of%20papers.md
- - [Representation Problem: Video (Data)]
- [Linux Multimedia Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-multimedia-stack.md)