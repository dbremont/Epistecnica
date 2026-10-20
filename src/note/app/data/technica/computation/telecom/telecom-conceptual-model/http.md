---
tags: [computer-network, protocol]
---

# HTTP

- [Transmission Control Protocol (TCP)](note.html?n=technica/computation/telecom/telecom-conceptual-model/transmission-control-protocol-tcp.md), [QUIC](note.html?n=technica/computation/telecom/telecom-conceptual-model/quic.md)

> **HTTP (Hypertext Transfer Protocol)** is an application-layer protocol in the OSI model that facilitates stateless, text-based communication between networked clients and servers by defining a structured format for request and response messages, typically over TCP (HTTP/1.x, HTTP/2) or QUIC (HTTP/3), supporting extensible semantics, header-based metadata, and methods for content negotiation, caching, and resource manipulation via standardized verbs and status codes.
> 

> HTTP defines several methods (verbs) that indicate the desired action to be performed on the server. Common methods include GET (retrieve data), POST (submit data), PUT (update data), and DELETE (remove data).
> 

> Uniform Resource Locators (URLs) or Uniform Resource Identifiers (URIs) are used to identify resources on the web. They specify the address of the resource and the protocol to be used (usually HTTP or HTTPS).
> 

> HTTP headers provide additional information about the request or response. Headers can convey details like content type, caching preferences, authentication information, and more.
> 

> HTTP responses include status codes that indicate the outcome of the request. Status codes range from informational (1xx) to successful (2xx), redirection (3xx), client error (4xx), and server error (5xx).
> 

> HTTP has evolved over time with different versions. The most common versions are HTTP/1.0 and HTTP/1.1. HTTP/2 introduced improvements like multiplexing and compression.
> 

> The principles of HTTP have influenced the design of RESTful APIs (Representational State Transfer), which use HTTP methods and status codes to create, read, update, and delete resources.
> 

> URL: (Uniform Resource Locator) is a web address that specifies the location of a resource on the internet, such as a webpage, image, or file.
> 

> URI: (Uniform Resource Identifier) is a string of characters used to uniquely identify a resource, either by its location, name, or both, on the internet.
> 

> Slug: In web development, a “slug” refers to a human-readable, URL-friendly text string used to uniquely identify a resource, often in the context of URLs for articles, posts, or pages.
> 

![image.png](data/technica/computation/telecom/telecom-conceptual-model/assets/http/image.png)

Request:

```
GET / HTTP/1.1
Host: www.example-host.com
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0
Accept: */*
Accept-Language: en-US
Accept-Encoding: gzip
Connection: closed
```

Response:

```
HTTP/1.1 200 OK
Server: nginx/1.0.15
date: Thu, 23 Oct 2014 00:25:37 GMT
content-Type: text/html; charset=iso-8859-1
transfer-encoding: chunked
Connection: close
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Content-Encoding: gzip
```

## Request

```bnf
Request = Request-Line
           *(( general-header
            | request-header
            | entity-header ) CRLF)
           CRLF
           [ message-body ]

Request-Line = Method SP Request-URI SP HTTP-Version CRLF

Method = "OPTIONS" | "GET" | "HEAD" | "POST" | "PUT" | "DELETE" | "TRACE" | "CONNECT"

Request-URI = "*" | absoluteURI | abs_path | authority

HTTP-Version = "HTTP" "/" 1*DIGIT "." 1*DIGIT

general-header = Cache-Control
               | Connection
               | Date
               | Pragma
               | Trailer
               | Transfer-Encoding
               | Upgrade
               | Via
               | Warning

request-header = Accept
               | Accept-Charset
               | Accept-Encoding
               | Accept-Language
               | Authorization
               | Accept-Ranges
               | If-Range
               | Range
               | Expect
               | From
               | Host
               | If-Match
               | If-Modified-Since
               | If-None-Match
               | If-Unmodified-Since
               | Max-Forwards
               | Proxy-Authorization
               | Referer
               | TE
               | User-Agent

entity-header = Allow
              | Content-Encoding
              | Content-Language
              | Content-Length
              | Content-Location
              | Content-MD5
              | Content-Range
              | Content-Type
              | Expires
              | Last-Modified
              | extension-header

CRLF = CR LF
SP = <US-ASCII SP, space (32)>
```

## Response

```bnf
<HTTP-Response> ::= <Response-Line> <Headers> <CRLF> <Message-Body>
<Response-Line> ::= <HTTP-Version> SP <Status-Code> SP <Reason-Phrase>
<HTTP-Version> ::= "HTTP/" <Digit> "." <Digit>
<Status-Code> ::= <Digit> <Digit> <Digit>
<Reason-Phrase> ::= *TEXT
<Headers> ::= <Header-Field> <CRLF>
<Message-Body> ::= *OCTET
<Header-Field> ::= <Field-Name> ":" SP <Field-Value>
<Field-Name> ::= *TOKEN
<Field-Value> ::= *TEXT
<SP> ::= " "
<CRLF> ::= "\r\n"
<Digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<TOKEN> ::= <Any valid token character>
<TEXT> ::= <Any valid text character>
<OCTET> ::= <Any valid octet value>
```

## **Uniform Resource Identifier (URI)**

> A **Uniform Resource Identifier (URI)** is a standardized string of characters used to identify a resource — either by its **location**, its **name**, or both — on the Internet or another network.
> 

> It serves as a **general syntax** for defining all forms of resource identifiers, including **URLs** and **URNs**.
> 

Resource Identifiers:

- **URL (Uniform Resource Locator)** — identifies a resource by *its location* (e.g., `https://example.com/page`).
- **URN (Uniform Resource Name)** — identifies a resource by *a persistent name* (e.g., `urn:isbn:9780131103627`).

### **Structure**

A URI consists of several components, not all of which are required:

```
scheme:[//authority]path[?query][#fragment]
scheme://[user:password@]host[:port]/path[?query][#fragment]

Case:
https://user:pass@www.example.com:443/docs/index.html?search=test#intro

```

| **Component** | **Description** | **Example** |
| --- | --- | --- |
| **Scheme** | Specifies the protocol or mechanism used to access the resource. | `https`, `ftp`, `mailto`, `file` |
| **Authority** | Defines who controls the namespace or how to reach the host; may include user info, host, and port. | `user:pass@example.com:8080` |
| **Path** | Identifies the specific resource within the scope of the scheme and authority. | `/docs/resource.txt` |
| **Query** | Provides additional parameters for the request; often used in web URLs. | `?key=value&lang=en` |
| **Fragment** | Identifies a secondary resource or position within the primary resource. | `#section2` |

### Standard URI’s

> See https://en.wikipedia.org/wiki/Well-known_URI
> 

> https://datatracker.ietf.org/doc/html/rfc8615#section-3.1
> 

| URI Path | Defined In | Functional Domain | Purpose | Deployment Level |
| --- | --- | --- | --- | --- |
| `/robots.txt` | RFC 9309 | Crawling | Controls search engine indexing | Very High |
| `/.well-known/acme-challenge/` | RFC 8555 | PKI / TLS | Domain validation for ACME CAs | Very High |
| `/.well-known/security.txt` | RFC 9116 | Security | Security contact disclosure | High |
| `/.well-known/mta-sts.txt` | RFC 8461 | Email Security | SMTP TLS enforcement policy | High |
| `/.well-known/openid-configuration` | OpenID Foundation | Identity | OpenID Connect discovery | Very High |
| `/.well-known/oauth-authorization-server` | RFC 8414 | Identity | OAuth 2.0 metadata discovery | High |
| `/.well-known/webfinger` | RFC 7033 | Identity / Federation | Resource identity discovery | High |
| `/.well-known/change-password` | WHATWG / Browser convention | Browser UX | Standard password change location | High |
| `/.well-known/apple-app-site-association` | Apple | Mobile Linking | iOS Universal Links | Very High |
| `/.well-known/assetlinks.json` | Google | Mobile Linking | Android app-site association | Very High |
| `/.well-known/matrix/server` | Matrix.org | Federation | Matrix server routing | Medium |
| `/.well-known/matrix/client` | Matrix.org | Federation | Matrix client config | Medium |
| `/.well-known/nodeinfo` | Fediverse convention | Federation | Instance metadata | Medium |
| `/.well-known/host-meta` | RFC 6415 | Discovery | Host-level metadata | Medium |

## Status Codes

[](https://pbs.twimg.com/media/F6xOA5SbQAATmjP?format=jpg&name=large)

> HTTP (Hypertext Transfer Protocol) uses a set of standardized status codes to indicate the outcome of a client’s request to the server. These status codes are three-digit numbers that provide information about the request’s success, failure, or other conditions.
> 

| **Category** | **Code** | **Description** |
| --- | --- | --- |
| Informational | 100 | Continue - The server has received the request headers; the client should proceed with the body. |
|  | 101 | Switching Protocols - The server is switching protocols as requested by the client. |
|  | 102 | Processing - The server is processing the request but no response is available yet. |
|  | 103 | Early Hints - Used to return some response headers before the final HTTP message. |
| Success | 200 | OK - The request has succeeded. |
|  | 201 | Created - The request has been fulfilled, resulting in the creation of a new resource. |
|  | 202 | Accepted - The request has been accepted for processing, but processing is not yet complete. |
|  | 203 | Non-Authoritative Information - The server is a transforming proxy and modified the response. |
|  | 204 | No Content - The server successfully processed the request but returns no content. |
|  | 205 | Reset Content - The server processed the request and asks the client to reset the document view. |
|  | 206 | Partial Content - The server is delivering only part of the resource due to a range header. |
| Redirection | 300 | Multiple Choices - The request has multiple possible responses; the client should choose one. |
|  | 301 | Moved Permanently - The requested resource has been permanently moved to a new URL. |
|  | 302 | Found (Temporary Redirect) - The requested resource temporarily resides under a different URL. |
|  | 303 | See Other - The response to the request can be found under a different URL (used for POST redirects). |
|  | 304 | Not Modified - Indicates that the resource has not been modified since the last request. |
|  | 305 | Use Proxy (Deprecated) - The requested resource must be accessed through a proxy. (No longer used.) |
|  | 307 | Temporary Redirect - The request should be repeated with another URI, but future requests should use the original. |
|  | 308 | Permanent Redirect - The request and all future requests should be repeated using another URI. |
| Client Error | 400 | Bad Request - The server cannot process the request due to malformed syntax. |
|  | 401 | Unauthorized - Authentication is required and has failed or not been provided. |
|  | 402 | Payment Required - Reserved for future use (originally intended for digital payment systems). |
|  | 403 | Forbidden - The server understood the request but refuses to authorize it. |
|  | 404 | Not Found - The requested resource could not be found on the server. |
|  | 405 | Method Not Allowed - The request method is not supported for the requested resource. |
|  | 406 | Not Acceptable - The server cannot produce a response matching the client's acceptable content types. |
|  | 407 | Proxy Authentication Required - The client must first authenticate with the proxy. |
|  | 408 | Request Timeout - The server timed out waiting for the request from the client. |
|  | 409 | Conflict - The request conflicts with the current state of the server. |
|  | 410 | Gone - The requested resource is no longer available and will not be available again. |
|  | 411 | Length Required - The request did not specify the length of its content, which is required. |
|  | 412 | Precondition Failed - A request header condition evaluated to false on the server. |
|  | 413 | Payload Too Large - The request is larger than the server is willing or able to process. |
|  | 414 | URI Too Long - The request URI is longer than the server is willing to interpret. |
|  | 415 | Unsupported Media Type - The request entity has a media type the server does not support. |
|  | 416 | Range Not Satisfiable - The client asked for a portion of the file, but the server cannot supply it. |
|  | 417 | Expectation Failed - The server cannot meet the requirements of the Expect request-header field. |
|  | 418 | I’m a Teapot (April Fools' joke) - A humorous response indicating the server refuses to brew coffee. |
|  | 421 | Misdirected Request - The request was sent to a server unable to respond. |
|  | 422 | Unprocessable Entity - The request was well-formed but contains semantic errors. |
|  | 423 | Locked - The requested resource is locked and cannot be modified. |
|  | 424 | Failed Dependency - The request failed because it depended on another request that failed. |
|  | 426 | Upgrade Required - The client should switch to a different protocol. |
|  | 428 | Precondition Required - The server requires the request to be conditional. |
|  | 429 | Too Many Requests - The user has sent too many requests in a given time ("rate limiting"). |
|  | 431 | Request Header Fields Too Large - The server refuses the request due to excessively large headers. |
|  | 451 | Unavailable For Legal Reasons - The resource is inaccessible due to legal reasons. |
| Server Error | 500 | Internal Server Error - A generic error message when the server encounters an unexpected condition. |
|  | 501 | Not Implemented - The server does not support the functionality required to fulfill the request. |
|  | 502 | Bad Gateway - The server, while acting as a gateway, received an invalid response from an upstream server. |
|  | 503 | Service Unavailable - The server is not ready to handle the request (e.g., overloaded or down for maintenance). |
|  | 504 | Gateway Timeout - The server, while acting as a gateway, did not receive a timely response from an upstream server. |
|  | 505 | HTTP Version Not Supported - The server does not support the HTTP protocol version used in the request. |
|  | 506 | Variant Also Negotiates - The server has an internal configuration error. |
|  | 507 | Insufficient Storage - The server cannot store the representation needed to complete the request. |
|  | 508 | Loop Detected - The server detected an infinite loop while processing the request. |
|  | 510 | Not Extended - Further extensions to the request are required. |
|  | 511 | Network Authentication Required - The client needs to authenticate to gain network access. |

## Header

> 

| **Header Name** | **Purpose** | **Example** |
| --- | --- | --- |
| `Host` | Specifies the domain name of the server | `example.com` |
| `User-Agent` | Describes the client software | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` |
| `Accept` | Tells the server which content types the client accepts | `text/html,application/xhtml+xml,application/xml` |
| `Accept-Encoding` | Specifies accepted compression methods | `gzip, deflate, br` |
| `Accept-Language` | Specifies preferred languages | `en-US,en;q=0.9` |
| `Content-Type` | Indicates the MIME type of the request body | `application/json` |
| `Content-Length` | Length of the request body in bytes | `348` |
| `Authorization` | Authentication credentials | `Bearer abc123xyz` |
| `Cache-Control` | Controls caching behavior | `no-cache`, `max-age=3600` |
| `Cookie` | Sends cookies from client to server | `sessionId=abc123; theme=dark` |
| `Set-Cookie` | Server sets cookies on the client | `sessionId=abc123; Path=/; HttpOnly` |
| `Referer` (sic) | Indicates the URL of the referring page | `https://example.com/page1` |
| `Location` | Redirect location (used in responses) | `https://example.com/login` |
| `ETag` | Resource identifier for cache validation | `"abc123etag"` |
| `If-None-Match` | Used with ETag for conditional requests | `"abc123etag"` |
| `Connection` | Controls connection behavior | `keep-alive`, `close` |
| `X-Requested-With` | Indicates AJAX requests | `XMLHttpRequest` |
| `Origin` | Specifies the origin of the request | `https://example.com` |
| `Access-Control-Allow-Origin` | CORS header, defines allowed origins | `*` or `https://example.com` |
| `X-Forwarded-For` | Identifies originating IP address of a client | `203.0.113.42` |
| `Server` | Indicates server software | `nginx/1.21.6` |
| `Date` | Timestamp of the HTTP response | `Tue, 11 Jun 2025 12:34:56 GMT` |

## MIME (Multipurpose Internet Mail Extensions) Types

> Also known as media type or Content Type.
> 

> Media types are used to specify the format and structure of data transmitted over a network, enabling proper interpretation and rendering by different software applications.
> 

Here is a list of common media types, also known as MIME types (Multipurpose Internet Mail Extensions):

- **text/plain** - **.txt**: Plain text content without any formatting.
- **text/html** - **.html**, .htm: Hypertext Markup Language for web pages.
- **application/json** - **.json**: JavaScript Object Notation for data interchange.
- **application/xml** - **.xml**: Extensible Markup Language for structured data.
- **application/pdf** - **.pdf**: Portable Document Format for documents.
- **image/jpeg** - **.jpg**, .jpeg: JPEG image format.
- **image/png** - **.png**: Portable Network Graphics image format.
- **image/gif** - **.gif**: Graphics Interchange Format for simple animations.
- **audio/mpeg** - **.mp3**: MPEG Audio Layer III format for audio files.
- **audio/wav** - **.wav**: Waveform Audio File Format for uncompressed audio.
- **video/mp4** - **.mp4**: MPEG-4 video format for multimedia content.
- **video/quicktime** - **.mov**: QuickTime video format developed by Apple.
- **application/octet-stream** - **(various**): Binary data that doesn’t fit other categories.
- **application/x-www-form-urlencoded**: Form data submitted via URLs.
- **multipart/form-data** : Form data submitted as part of a multipart message.
- **application/javascript** - **.js**: JavaScript code.
- **application/rss+xml** - **.rss**: RSS (Rich Site Summary) feed format.
- **application/zip** - **.zip**: Compressed archive format.
- **application/vnd.ms-excel** - **.xls**: Microsoft Excel spreadsheet format.
- **application/vnd.openxmlformats-officedocument.wordprocessingml.document** - **.docx**: Microsoft Word document format.
- `**/**`

## **HTTP Basic Authentication**

> 
- [ ]  https://en.wikipedia.org/wiki/Basic_access_authentication
- [ ]  https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/WWW-Authenticate

## 🔢 **HTTP Versions**

| **Version** | **Year** | **Transport** | **Key Features** | **Limitations / Notes** |
| --- | --- | --- | --- | --- |
| **HTTP/0.9** | 1991 | TCP | - Only `GET` request supported- No headers- Simple HTML only | No status codes, headers, or extensibility |
| **HTTP/1.0** | 1996 | TCP | - Status codes- Headers- MIME types | New TCP connection per request (no keep-alive by default) |
| **HTTP/1.1** | 1997 | TCP | - Persistent connections- Chunked transfer- Pipelining | Head-of-line blocking, limited parallelism |
| **HTTP/2** | 2015 | TCP (TLS/SSL usually) | - Binary protocol- Multiplexing- Header compression- Server push | More efficient than 1.1, but still affected by TCP limits |
| **HTTP/3** | 2022 | QUIC (UDP-based) | - Uses QUIC instead of TCP- Faster handshakes- True multiplexing | Requires browser and server support |

## HTTP Performance

> 

## References

- [Cool URIs can be ugly](https://news.ycombinator.com/item?id=39345439)
- [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)
- [How Do Websockets Work?](https://sookocheff.com/post/networking/how-do-websockets-work/)
- [WebSockets - A Conceptual Deep Dive](https://ably.com/topic/websockets)
- [List of HTTP status codes](https://www.wikiwand.com/en/List_of_HTTP_status_codes)
- [The HTTP crash course nobody asked for](https://fasterthanli.me/articles/the-http-crash-course-nobody-asked-for)
- [The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455)
- [Uniform Resource Identifier](https://www.wikiwand.com/en/Uniform_Resource_Identifier)
- [MIME](https://en.wikipedia.org/wiki/MIME)
- [Media Type](https://en.wikipedia.org/wiki/Media_type)
- [Scalable WebSocket Architecture](https://blog.hathora.dev/scalable-websocket-architecture/)
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers
- [HTTP/2 and HTTP/3 explained](https://news.ycombinator.com/item?id=39700443) ([alexandrehtrb.github.io](http://alexandrehtrb.github.io/))
- Padmanabhan, V. N., & Mogul, J. C. (1995). Improving HTTP Latency. 28(1–2), 25–35.
- [Improving Performance with HTTP Streaming (medium.com/airbnb-engineering)](https://news.ycombinator.com/item?id=35982732)
- [Does Websocket use the same TCP connection that was used by the initial HTTP for the handshake?](https://stackoverflow.com/questions/53383042/does-websocket-use-the-same-tcp-connection-that-was-used-by-the-initial-http-for)
- Popa, L., Ghodsi, A., & Stoica, I. (2010). HTTP as the Narrow Waist of the Future Internet. 1–6.
- [Berkeley Socket](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/berkeley-socket.md)
- [Linux Network Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-network-stack.md)
- https://datatracker.ietf.org/doc/html/rfc3986