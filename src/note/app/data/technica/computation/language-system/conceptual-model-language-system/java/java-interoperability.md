# Java: 🔗Interoperability

> 

Guiding Question:

- Which type of **Interoperability  Mechanisms  does this Language Supports?**

## Mechanism

> 

| Category | Mechanism / Tool | Description | Typical Use Case | Package / Tool |
| --- | --- | --- | --- | --- |
| **Native Code (JNI)** | **JNI (Java Native Interface)** | Call C/C++ code from Java, or expose Java code to native libraries | Use native performance libraries, system APIs | `java.lang`, `jni.h` |
|  | **JNA (Java Native Access)** | Easier alternative to JNI for calling native shared libraries (no C glue) | Call OS-level APIs or native shared libraries | `com.sun.jna` |
| **Scripting Integration** | **Java Scripting API (JSR-223)** | Interact with scripting languages (JavaScript, Python via Jython, etc.) | Embed scripting inside Java apps | `javax.script` |
|  | **Nashorn (deprecated)** | JavaScript engine bundled with Java 8–14 | Lightweight scripting in Java | `jdk.nashorn.api.scripting` |
| **Web APIs** | **REST clients (e.g., WebClient, RestTemplate)** | Interact with REST APIs, web services | Call external services from Java | `org.springframework.web.client`, etc. |
|  | **SOAP (JAX-WS)** | Java API for XML Web Services (SOAP) | Enterprise web service integration | `javax.xml.ws` |
| **Database Access** | **JDBC (Java Database Connectivity)** | Connect and interact with relational databases | Query SQL databases like MySQL, PostgreSQL | `java.sql` |
|  | **JPA / Hibernate** | Object-relational mapping between Java and DB schemas | Use Java objects to represent database entities | `javax.persistence` |
| **Cross-language** | **GraalVM** | Run Java, JavaScript, Python, Ruby, and LLVM in one runtime | Polyglot applications with shared memory/runtime | `org.graalvm.*` |
|  | **Kotlin / Scala / Groovy** | Run on the JVM and interoperate with Java classes and libraries | Multi-paradigm JVM development | JVM languages |
| **Web Integration** | **Servlets / JSP** | Java to HTML/web interfaces | Web application development | `javax.servlet` |
|  | **Spring Boot** | REST APIs, JSON/XML parsing, WebSocket integration | Modern web services and microservices | `org.springframework.*` |
| **File / Data Formats** | **Jackson / Gson** | Convert Java objects to/from JSON | JSON interoperability | `com.fasterxml.jackson`, `com.google.gson` |
|  | **XML parsers (JAXB, DOM, SAX)** | Parse and bind XML to Java objects | XML data exchange | `javax.xml`, `javax.xml.bind` |
| **Message Queues** | **JMS (Java Message Service)** | Interact with message brokers (ActiveMQ, RabbitMQ, etc.) | Messaging between distributed systems | `javax.jms` |
|  | **Kafka clients** | Publish and consume from Apache Kafka | High-performance streaming data | `org.apache.kafka` |
| **Shell / System** | **ProcessBuilder / Runtime.exec()** | Run system commands or external programs | Run scripts, tools, other programs from Java | `java.lang` |
| **Browser / UI** | **JavaFX WebView** | Display and interact with HTML content in Java UI | Embed web content inside desktop apps | `javafx.scene.web.WebView` |

## Multi-Node System

- [‣](https://app.notion.com/p/6d62587cf82d476787d8faba8f292614?pvs=21)
- [‣](https://app.notion.com/p/161c0f5171ec80fbaedae02728d10c9a?pvs=21)

## **Java Native Interface (JNI)**

| **Component** | **Description** |
| --- | --- |
| **JNI** | A framework that allows Java code to interact with native applications and libraries written in other languages. |
| **Native Methods** | Methods declared in Java but implemented in native languages. |
| **JNI Functions** | Provides functions for managing and interacting with Java objects and methods from native code. |

## References

- [Interoperability](note.html?n=technica/computation/language-system/conceptual-model-language-system/interoperability.md)