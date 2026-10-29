# Java: 🛠️ Tooling & Ecosystem

> 

QA:

- …

## 🧰 Breviarium

| **Category** | **Type** | **Name** | **Description** |
| --- | --- | --- | --- |
| Core Development & Runtime | JDK | OpenJDK, Oracle JDK, GraalVM | Java Development Kits offering standard libraries and compiler tools; GraalVM adds polyglot and native compilation. |
|  | JVM | HotSpot, OpenJ9, GraalVM | Virtual Machines to execute bytecode efficiently; GraalVM supports AOT and multi-language execution. |
|  | Build Tools | Maven, Gradle, Ant | Build automation, dependency management, and lifecycle management. |
| Parallel & High-Performance Computing | Concurrency | Java Concurrency API | Native Java threads, executors, futures, and parallel streams. |
|  | Actor Model | Akka | Toolkit for building reactive, message-driven systems. |
|  | Reactive Frameworks | Quarkus (Reactive) | Lightweight, container-optimized framework for reactive programming. |
|  | GPU Offloading | Aparapi, TornadoVM, Rootbeer | Accelerate compute with OpenCL or GPU backends. |
|  | Distributed Data | Apache Spark, Flink, Hazelcast | Parallel stream and batch data processing and in-memory computation. |
| Numerical & Scientific Computing | Linear Algebra | ND4J, EJML, Colt | Fast matrix and vector operations. |
|  | Math & Units | Apache Commons Math, JScience | Statistics, numerical analysis, units of measurement. |
|  | Symbolic Math | Symja, JAS | Symbolic computation and algebra systems. |
| Data Structures & Algorithms | Collections | Guava, Apache Commons Collections | Enhanced collections, utilities, caching, and functional idioms. |
|  | Graph Algorithms | JGraphT | Rich graph theory library for modeling and computing. |
|  | Specialized Structures | Neo4j, Hipparchus, TarsosDSP | Graph DB (Neo4j), celestial mechanics (Hipparchus), audio analysis (TarsosDSP). |
| Machine Learning & AI | Deep Learning | DeepLearning4J (DL4J) | Scalable deep learning with GPU support. |
|  | Model Inference | ONNX Runtime | ONNX model deployment for inference. |
|  | Classical ML | Weka, Smile, Tribuo | Traditional ML algorithms, clustering, and decision trees. |
|  | NLP | Stanford NLP, OpenNLP | POS tagging, dependency parsing, named entity recognition. |
| Database & Data Management | ORM | Hibernate, JOOQ, MyBatis | Object-relational mapping, fluent SQL DSLs. |
|  | Drivers | JDBC, MongoDB Driver, Cassandra Driver | Standardized DB access for SQL and NoSQL. |
|  | In-Memory Data | Apache Ignite, Redisson | Distributed caching and memory grids. |
| Networking & Distributed Systems | Low-Level IO | Java NIO, Netty, Grizzly | Non-blocking network communication. |
|  | RPC Frameworks | gRPC, Apache Thrift | High-performance remote procedure call mechanisms. |
|  | Messaging | Kafka, RabbitMQ | Distributed messaging and pub/sub communication. |
|  |  | HttpClient | Feature-rich HTTP client supporting HTTP/1.1 and HTTP/2, cookies, connection pooling, proxies, etc. |
|  |  | 	MINA | Framework for building high-performance network applications with event-driven IO. |
| Logging & Monitoring | Logging APIs | Log4j, SLF4J, JUL | Structured logging libraries. |
|  | Metrics & Tracing | Micrometer, Prometheus Client, OpenTelemetry | Monitoring and instrumentation of Java apps. |
| Testing & Debugging | Unit Testing | JUnit, TestNG | Automated test frameworks. |
|  | Mocking | Mockito | Create mock objects for isolated tests. |
|  | Benchmarking | JMH | Benchmark harness for microperformance testing. |
|  | Profiling | Java Mission Control, VisualVM, YourKit | Performance profiling, memory analysis. |
| Web & API Development | Web Frameworks | Spring Boot, Jakarta EE, Micronaut, Quarkus | Full-featured web/microservice frameworks. |
|  | REST APIs | Jersey, Spring WebFlux, Retrofit | Declarative clients and reactive REST frameworks. |
|  | … | … | .. |
| Metacomputation & Bytecode Tools | AOP | AspectJ | Aspect-oriented programming with compile-time weaving. |
|  | Bytecode | ASM, Javassist, ByteBuddy | Bytecode generation and transformation. |
|  | Static Analysis | Soot, ProGuard | Code optimization, shrinkers, static analysis. |
| Deployment & DevOps | Containerization | Jib, Docker Java API | Build container images directly from Java projects. |
|  | CI/CD | Jenkins, GitHub Actions | Automate test, build, and deploy pipelines. |
|  | Config Management | Spring Cloud Config, Archaius | Externalized service configuration and dynamic refresh. |
| Security & Cryptography | Encryption | Bouncy Castle, JCA | Encryption, signatures, and certificate tools. |
|  | Auth & Identity | Keycloak, Spring Security | Authentication, OAuth2, role-based access. |
| Serialization & Data Formats | Serialization | Jackson, Gson, Avro, Protobuf | JSON, binary, and schema-based serializers. |
|  | Data Formats | Apache Parquet, ORC | Columnar file formats for large-scale data analytics. |
| Visualization & Reporting | Charting | JFreeChart, XChart, JavaFX Charts | Static and interactive data plotting libraries. |
|  | Reports | JasperReports, BIRT | Generate rich-text and tabular reports. |
| Interoperability & Polyglot | Scripting | JSR-223, GraalVM JS/Python, BeanShell | Embed interpreters for dynamic logic. |
| Interoperability & Polyglot | Native Interop | JNI, JNA, Project Panama | Bind to native C/C++ libraries or system APIs. |
| Scheduling & Orchestration | Job Scheduling | Quartz, Spring Batch | Cron-like scheduling and ETL pipelines. |
| Scheduling & Orchestration | Workflow Engines | Camunda, Temporal, Airflow (via REST) | Coordination of long-running distributed workflows. |
| Code Quality & Static Analysis | Linting | Checkstyle, Google Java Format | Code formatting and linting for consistency. |
|  | Bug Detection | SpotBugs, PMD | Static analyzers to find bugs and code smells. |
| Domain-Specific Toolkits | GIS | GeoTools | Geospatial data access and processing. |
|  | Bioinformatics | BioJava | Tools for sequence analysis, protein structures, and genomics. |
|  | Finance | Strata (OpenGamma), JQuantLib | Quantitative finance, analytics, risk models. |
|  | Audio | TarsosDSP | Audio analysis, pitch tracking, fingerprinting. |
|  | Robotics | LeJOS, Eclipse 4diac | Robotics control and IEC 61499 modeling in Java. |
|  | Simulation | MASON, Repast Simphony | Agent-based and multi-agent system simulation libraries. |
|  | Education/Visualization | Greenfoot, BlueJ | Educational Java IDEs with visual modeling. |
| Development Tools | Java Tools |  |  |
|  |  | **jinfo** | A JDK tool for displaying configuration information for a running Java process or a core file. |
|  |  | **jps** | A JDK tool to list the instrumented Java Virtual Machines (JVMs) on the target system. |
|  |  | **jar** | A Java Archive (JAR) tool for packaging compiled Java classes into a single file, typically used for distributing libraries and applications. |
|  |  | **jarsigner** | A tool for signing and verifying Java Archive (JAR) files, ensuring the authenticity and integrity of the code. |
|  |  | **javac** | The Java compiler, which translates Java source code into bytecode that can be executed by the JVM. |
|  |  | **javadoc** | A tool for generating API documentation in HTML format from Java source code, based on the comments and annotations in the code. |
|  |  | **javah** | A JDK tool used to generate C header and source files that are needed to implement native methods in Java code. |
|  |  | **javap** | A JDK tool that disassembles class files, showing the bytecode and details of the classes. |
|  |  | **jcmd** | A JDK tool for sending diagnostic command requests to a Java process, useful for monitoring and troubleshooting. |
|  |  | **jconsole** | A graphical monitoring tool to monitor and manage Java applications in real-time, allowing for tracking memory, threads, and CPU usage. |
|  |  | **jdb** | A command-line debugger for Java classes, allowing for step-by-step execution, breakpoint management, and variable inspection. |
|  |  | **jdeps** | A JDK tool to analyze the dependencies of Java class files, useful for identifying and managing modularity issues. |
|  |  | **jfr** | Java Flight Recorder, a profiling and event collection tool for Java applications, providing detailed diagnostics and performance data. |
|  |  | **jhat** | A JDK tool for analyzing heap dumps, allowing developers to explore object memory use and locate memory leaks. |
|  |  | **jstack** | A JDK tool that prints the Java stack traces of all threads in a Java process, useful for debugging deadlocks and performance issues. |
|  |  | **jstat** | A JDK tool for monitoring the performance and resource usage of a running Java process, providing real-time statistics on memory, GC, and more. |
|  |  | **keytool** | A key and certificate management utility used for managing keystores, private keys, and certificates in Java applications. |
|  |  | **ascii** | A JDK tool for generating ASCII representations of class files, useful for debugging class loading issues. |
|  |  | **wsgen** | A tool for generating web service artifacts, such as WSDL files, from Java classes annotated with JAX-WS annotations. |
|  |  | **wsimport** | A tool for generating Java code from WSDL files, creating client-side code for calling web services. |

## Apache Commons

> https://commons.apache.org/[.apache.org/](https://commons.apache.org/).
> 

| **Category** | **Library** | **Description** |
| --- | --- | --- |
| **Core Utilities** | **Commons Lang** | Enhances standard Java with utilities for `String`, `Object`, `Number`, `Date`, reflection, and more. |
|  | **Commons IO** | Streamlines file and I/O operations such as copying, filtering, and file monitoring. |
|  | **Commons Collections** | Extends the Java Collections Framework with additional data structures and algorithms. |
|  | **Commons Compress** | Supports compression formats like ZIP, GZIP, TAR, BZIP2, 7z, and more. |
|  | **Commons Exec** | Launches and controls external processes. |
| **Configuration & Serialization** | **Commons Configuration** | Provides a unified API for accessing configuration data from various sources (XML, properties, INI, etc). |
|  | **Commons Digester** | Parses XML into Java objects using pattern-based rules. |
|  | **Commons BeanUtils** | Facilitates reflection-based property access and copying between JavaBeans. |
| **Mathematics & Statistics** | **Commons Math** | A library of lightweight, self-contained mathematics and statistics components. Includes linear algebra, complex numbers, ODE solvers, optimization, and more. |
| **Database Utilities** | **Commons DbUtils** | Simplifies JDBC operations and resource handling. |
| **Networking & Communication** | **Commons Net** | Implements network protocols such as FTP, SMTP, POP3, IMAP, Telnet, NNTP, and others. |
|  | **Commons Email** | Builds on JavaMail for simplified email sending, including attachments and HTML support. |
| **Code Utilities** | **Commons Codec** | Encodes and decodes in Base64, Hex, Phonetic, URL, Soundex, BZip2, etc. |
|  | **Commons CLI** | Parses command-line arguments (e.g., `--help`, `-f filename.txt`). |
|  | **Commons Logging** | A lightweight wrapper for different logging frameworks (often replaced by SLF4J today). |
|  | **Commons Text** | Utilities for string substitution, templating, and text similarity (e.g., Levenshtein). |
|  | **Commons VFS** | Abstracts different file systems (FTP, SFTP, HTTP, ZIP, local file systems) into a virtual file system API. |
| **Object Pools & Resource Management** | **Commons Pool** | Implements object pooling (e.g., database connections, thread pools). |
|  | **Commons DBCP** | Provides database connection pooling using `Commons Pool`. |
| **Testing & Functors** | **Commons Functor** | Defines functional programming types (functions, predicates, procedures) — now mostly superseded by Java 8 lambdas. |
| **Others** | **Commons JCI** | Java Compiler Interface for abstracting Java compilation at runtime. |
|  | **Commons RNG** | Random number generators with known statistical properties (e.g., Mersenne Twister). |
|  | **Commons Numbers** | Precision-focused numerical computations (complex numbers, floating-point arithmetic). |

## Multi-Node System

- [‣](https://app.notion.com/p/6d62587cf82d476787d8faba8f292614?pvs=21)
- [‣](https://app.notion.com/p/161c0f5171ec80fbaedae02728d10c9a?pvs=21)

## Language Systems Tools

> Code Representation Manipulation,  Code Generation, Source Code Analysis, …
> 
- [**ASM**](note.html?n=technica/computation/language-system/conceptual-model-language-system/asm.md)
- [**Byte Buddy**](note.html?n=technica/computation/language-system/conceptual-model-language-system/byte-buddy.md)
- [Java Bytecode](note.html?n=technica/computation/language-system/conceptual-model-language-system/java-bytecode.md)

## References

- [Java](note.html?n=technica/computation/language-system/conceptual-model-language-system/java.md)
- [**AspectJ**](note.html?n=technica/computation/language-system/conceptual-model-language-system/aspectj.md)
- [Apache Maven](note.html?n=technica/general/pto/maven.md)
- https://github.com/akullpp/awesome-java
- https://docs.oracle.com/javase/8/docs/technotes/guides/jar/index.html
- https://en.wikipedia.org/wiki/JAR_(file_format)
- [**CSBB:** Java Language System](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/csbb-java-language-system.md)
- [Java HotSpot Virtual Machine](note.html?n=technica/computation/language-system/conceptual-model-language-system/java-hotspot-virtual-machine.md)
- https://docs.oracle.com/en/java/javase/17/docs/specs/jar/jar.html
- https://stackoverflow.com/questions/11333208/where-are-java-archive-file-structure-specifications
- https://github.com/dbremont/language-system-labs/tree/main/java
- https://en.wikipedia.org/wiki/Java_Virtual_Machine_Tools_Interface