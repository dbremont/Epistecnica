---
tags: [note, production]
---

# Constitutive Technical Object

> A Software Component (Supply) represents any computational building block that can be produced, deployed, and integrated within a software system. Components are categorized by their Type/Domain, Form, Function, and Computational Role, providing a clear abstraction for system construction and analysis.

## Dimension

| **Dimension**          | **Value**                        | **Description**                                                                                               |
| ---------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Form**               | Standalone Computational Service | A self-contained service performing a specific computation or function, deployable independently.             |
|                        | Computational Library            | A collection of reusable functions, classes, or APIs that can be integrated into other components or systems. |
|                        | Framework                        | Offers a reusable structure or scaffolding for building other components or applications.                     |
|                        | Application                      | A complete executable program providing end-user functionality.                                               |
|                        | Component                        | A modular element within a system that encapsulates specific functionality.                                   |
| **Function**           | Integration                      | Connects, adapts, or orchestrates interactions between multiple components or external systems.               |
|                        | Computation                      | Performs data processing, calculations, simulations, or transformations.                                      |
|                        | Storage / Retrieval              | Manages persistent or transient data for use by other components.                                             |
|                        | Communication                    | Enables messaging, event handling, or remote procedure calls between components.                              |
|                        | Security / Authentication        | Ensures confidentiality, integrity, access control, or user verification.                                     |
|                        | Monitoring / Observability       | Tracks performance, logs events, collects metrics, and provides insights.                                     |
|                        | Automation / Orchestration       | Executes tasks, schedules jobs, or coordinates workflows automatically.                                       |
| **Computational Role** | Data Provider                    | Supplies data to other components or systems.                                                                 |
|                        | Processor                        | Performs computation or transformation of data.                                                               |
|                        | Coordinator                      | Manages control flow or orchestrates multiple components.                                                     |
|                        | Consumer                         | Receives and uses data or services from other components.                                                     |
|                        | Gateway / Adapter                | Bridges different interfaces, protocols, or systems.                                                          |
|                        | Observer / Monitor               | Collects metrics, logs, or observes system behavior without altering it.                                      |

## Component Space

> A **Component Space** represents the universe of software components in a system, categorized by their purpose, form, and function. It helps in understanding how components contribute to system construction, integration, and operation.

| **Category**                    | **Component / Element**               | **Description**                                            | **Form** (Implementation/Physical Form)                                 | **Function** (Primary Purpose/Role)                                          |
| ------------------------------- | ------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Data Management / Storage**   | Database                              | Structured storage and retrieval of data                   | Standalone Service / Library                                            | Stores, queries, and manages persistent data                                 |
|                                 | Data Lake / Warehouse                 | Large-scale structured/unstructured storage                | Standalone Service                                                      | Centralizes, processes, and analyzes big data                                |
|                                 | Cache                                 | Temporary high-speed data storage                          | Library / Service / In-memory store                                     | Speeds up data access and reduces load on primary storage                    |
|                                 | File System / File Manager            | Organizes and manages files                                | OS-level Service / Library / Cloud client                               | Provides hierarchical storage, access, upload, and retrieval mechanisms      |
|                                 | Object Storage                        | Stores unstructured data                                   | Standalone Service                                                      | Provides scalable and durable storage                                        |
|                                 | Repository                            | Abstraction over data storage                              | Interface/class, DAO, ORM wrapper                                       | Provides CRUD operations, abstracts data source                              |
|                                 | Database Connector                    | Handles communication with databases                       | Driver, connection pool, client library                                 | Establishes connections, executes queries                                    |
|                                 | Message Queue                         | Middleware for asynchronous communication/data exchange    | Standalone Service / Broker (RabbitMQ, Kafka), queue, topic             | Decouples producers/consumers, ensures reliable message delivery             |
| **Computation / AI**            | Algorithm Library                     | Collection of reusable computational routines              | Library                                                                 | Implements algorithms for numerical, symbolic, or logical computation        |
|                                 | Math / Statistical Engine             | Advanced mathematical operations                           | Library / Service                                                       | Supports analytics, simulation, and optimization                             |
|                                 | GPU / Accelerator Interface           | High-performance computation interface                     | Driver / Library                                                        | Enables parallel computation on specialized hardware                         |
|                                 | Machine Learning Library              | Algorithms for learning from data                          | Library                                                                 | Implements supervised, unsupervised, and reinforcement learning              |
|                                 | Model Serving Platform                | Deploys AI models                                          | Service / Framework                                                     | Provides inference endpoints for AI models                                   |
|                                 | Data Pipeline                         | Prepares and transforms data                               | Library / Service                                                       | Extracts, transforms, and loads data for computation or AI                   |
|                                 | Simulation Engine                     | Models real-world phenomena                                | Library / Service                                                       | Performs predictive or analytical simulations                                |
|                                 | Calculator                            | Performs specific computations                             | Module, pure function, stateless bean                                   | Executes formulas, conversions, aggregations                                 |
| **Integration & Communication** | API Gateway                           | Manages external and internal service communication        | Standalone Service / Reverse proxy / Routing layer                      | Routes, authenticates, aggregates service requests                           |
|                                 | Service Client / RPC Interface        | Consumes external APIs or performs remote procedure calls  | SDK, REST client, gRPC stub / Library / Protocol                        | Invokes remote services, manages connections                                 |
|                                 | Event Bus                             | Event-driven communication backbone                        | Service / Library / Pub-Sub system                                      | Broadcasts events to multiple subscribers asynchronously                     |
|                                 | Webhook Handler / Adapter             | Listens for external notifications / translates interfaces | HTTP endpoint, listener, wrapper class                                  | Receives and processes updates, ensures interoperability                     |
|                                 | Messaging Queue                       | Asynchronous communication                                 | Broker, queue, topic                                                    | Enables decoupled, reliable message passing                                  |
| **User Interface (UI)**         | Button                                | Interactive element for triggering actions                 | Graphical element, HTML `<button>`, framework component                 | Triggers events, submits forms, navigates                                    |
|                                 | Form Field                            | Input area for user data                                   | Text box, dropdown, checkbox, date picker                               | Captures and validates user input                                            |
|                                 | Data Grid                             | Displays tabular data with controls                        | Table with sorting/filtering/pagination                                 | Presents datasets, enables data manipulation                                 |
|                                 | Modal                                 | Overlay dialog for focused tasks                           | Pop-up window, lightbox, dialog                                         | Displays additional info without page navigation                             |
|                                 | Navigation Bar                        | Guides users through application                           | Menu bar, sidebar, tabs, breadcrumbs                                    | Provides routing and context switching                                       |
|                                 | UI Component                          | Generic visual or interactive element                      | Component / Library                                                     | Handles user interaction and presentation                                    |
|                                 | CLI Tool                              | Command-line interface                                     | Application                                                             | Provides text-based access to system functionality                           |
|                                 | API Interface                         | Programmatic interface                                     | Library / Service                                                       | Exposes functionality to other systems or applications                       |
| **Business Logic**              | Service                               | Stateless unit of business logic                           | Class, module, microservice, serverless function                        | Implements use cases, orchestrates operations                                |
|                                 | Workflow Engine                       | Manages complex/multi-step business processes              | Library / Service / Rule engine / State machine / BPMN interpreter      | Coordinates steps, handles transitions                                       |
|                                 | Validator                             | Ensures data meets business rules                          | Rule set, schema validator, custom logic class                          | Validates input, enforces constraints                                        |
|                                 | Scheduler / Task Scheduler            | Executes time-based or recurring jobs                      | Cron job, service, queue listener                                       | Automates tasks, triggers periodic actions                                   |
|                                 | Calculator                            | Performs specific computations                             | Module, pure function, stateless bean                                   | Executes formulas, conversions, aggregations                                 |
| **Security**                    | Authentication Module / Middleware    | Verifies identity                                          | Library / Service / Filter / Interceptor                                | Authenticates users, enforces access control                                 |
|                                 | Authorization Module                  | Manages permissions                                        | Library / Service                                                       | Controls access rights and privileges                                        |
|                                 | Encryption / Crypto Library / Utility | Secures data                                               | Library / Module / Cryptographic Service                                | Provides cryptographic operations for confidentiality, integrity, signatures |
|                                 | Security Audit / Monitoring           | Tracks security events                                     | Service / Tool                                                          | Detects anomalies and logs security-relevant activity                        |
| **Monitoring & Observability**  | Logging Framework / Logger            | Captures application events                                | Library / Service / Centralized logging                                 | Records runtime events for analysis and debugging                            |
|                                 | Metrics Collector / Monitor           | Measures performance                                       | Library / Service / Agent / Dashboard                                   | Tracks system and application metrics, alerts                                |
|                                 | Profiler                              | Analyzes runtime performance                               | Tool / Library                                                          | Identifies bottlenecks and inefficiencies                                    |
|                                 | Tracing System                        | Tracks request flow                                        | Service / Library                                                       | Provides end-to-end observability of distributed systems                     |
| **Automation & Orchestration**  | Workflow Engine                       | Manages multi-step processes                               | Library / Service                                                       | Coordinates multi-step processes and dependencies                            |
|                                 | CI/CD Pipeline                        | Automates build & deployment                               | Tool / Service                                                          | Streamlines software integration, testing, and delivery                      |
|                                 | Container Orchestrator                | Manages containers                                         | Service / Framework                                                     | Deploys, scales, and monitors containerized applications                     |
| **Configuration & Management**  | Configuration Manager                 | Centralizes system/application settings                    | Library / Service / Config file / Environment variables / Config server | Provides consistent configuration access across components                   |
|                                 | Feature Flag System                   | Manages conditional functionality                          | Library / Service                                                       | Allows dynamic enabling/disabling of system features                         |
|                                 | Secrets Manager                       | Stores sensitive data                                      | Standalone Service                                                      | Safely manages credentials, API keys, and certificates                       |
| **Testing & Verification**      | Unit Test Framework                   | Tests individual code units                                | Library / Tool                                                          | Validates functionality of specific components                               |
|                                 | Integration Test Framework            | Tests combined components                                  | Library / Tool                                                          | Ensures components interact correctly                                        |
|                                 | Formal Verification Tool              | Mathematically verifies correctness                        | Tool / Framework                                                        | Proves correctness of algorithms or critical systems                         |
| **Performance & Optimization**  | Profiler                              | Measures resource usage                                    | Tool / Library                                                          | Identifies bottlenecks and inefficiencies                                    |
|                                 | Load Tester                           | Simulates high usage                                       | Tool                                                                    | Evaluates system scalability and performance                                 |
|                                 | Optimizer                             | Improves algorithms / code                                 | Library / Tool                                                          | Enhances speed, memory usage, or efficiency                                  |
| **Cross-Cutting & Utility**     | Error Handler                         | Centralizes error management                               | Global exception handler, error boundary, middleware                    | Catches, logs, and transforms errors                                         |
|                                 | Serializer                            | Converts objects to/from wire format                       | JSON/XML serializer, protocol buffer                                    | Encodes/decodes data for storage/transmission                                |
|                                 | Localization Manager                  | Supports multiple languages                                | Resource bundle, i18n library, locale resolver                          | Provides translations, formats locale-specific content                       |
|                                 | ID Generator                          | Creates unique identifiers                                 | UUID generator, sequence generator, snowflake algorithm                 | Produces unique keys, prevents collisions                                    |




## Hardware

> …

## OS System

> …

## Language System

> …

## Frameworks

> …

### CLI Framework

- [Textual](https://www.notion.so/Textual-161c0f5171ec801081c3fcb36033bdd7?pvs=21)
- …

### Web Frameworks

> …

### Microservices Framework

> …

## Libraries

### Request Router

### **Core Computation**

### Parallel & Distributed

### Data Processing

### Computational Learning

- [ ]  https://mc-stan.org/

### Optimization

### Simulation

### **Templating**

### **Scraping**

### Parsing

### Code Generation

### URL Parsing

### HTTP Parsing

### DI (Dependency Injection)

### Image Processing

### Video Processing

### Signal Processing

### Language Parsing

> ….

### Data Integration Format

### UI

| **Category** | **Library/API** | **Description** | **Language Bindings** |
| --- | --- | --- | --- |
| **Low-Level APIs** | **OpenGL** | Cross-platform, industry-standard API for rendering 2D and 3D vector graphics. Used in games, simulations, and CAD software. | C, C++, Python (PyOpenGL), Java (JOGL) |
|  | **Vulkan** | Low-overhead, high-performance API for 3D graphics and computing. A modern alternative to OpenGL. | C, C++, Python (Vulkan bindings) |
|  | **DirectFB** | Lightweight graphics library for Linux, designed for full-screen applications without the need for a windowing system. | C |
|  | **Mesa 3D** | Open-source implementation of OpenGL and Vulkan. Provides hardware-accelerated 3D rendering for multiple drivers. | C |
| **2D Graphics** | **Cairo** | Vector-based 2D graphics library, supporting drawing to multiple outputs (e.g., PDFs, PNGs, X11 surfaces). | C, C++, Python, Perl, Lua |
|  | **SDL (Simple DirectMedia Layer)** | Cross-platform library for low-level access to audio, keyboard, mouse, and 2D graphics. Primarily used for game development. | C, C++, Python (Pygame), Lua |
|  | **Xlib/XCB** | Low-level libraries for interfacing directly with the X Window System. Provides control over windows and graphics on X11 servers. | C, C++ |
|  | **Qt (QPainter)** | Framework for building GUIs and applications, featuring a powerful 2D drawing API (QPainter). | C++, Python (PyQt, PySide) |
| **3D Graphics** | **OpenSceneGraph** | High-performance 3D graphics toolkit for visual simulation, games, and scientific applications. Built on top of OpenGL. | C++, Python |
|  | **OGRE (Object-Oriented Graphics Rendering Engine)** | Scene-oriented, flexible 3D engine for applications requiring real-time rendering, such as games and simulations. | C++, Python |
|  | **Panda3D** | Open-source 3D engine that simplifies real-time 3D rendering for games, simulations, and virtual reality applications. | C++, Python |
|  | **Irrlicht** | Lightweight 3D engine designed for real-time applications. Supports both OpenGL and Vulkan rendering backends. | C++, Python |
| **GUI Toolkits** | **GTK** | Cross-platform GUI toolkit for creating graphical applications, primarily on Linux. Provides basic drawing and windowing capabilities. | C, Python (PyGTK), ValaOpenGL |
|  | **Qt (QtGui/QML)** | Provides extensive support for 2D and 3D graphics in GUI applications, with both procedural (C++) and declarative (QML) approaches. | C++, Python (PyQt, PySide) |
| **Windowing and Display APIs** | **X11** | Core protocol of the X Window System, providing the foundation for graphical user interfaces in Linux. | C, C++ |
|  | **Wayland** | Modern display server protocol, designed to be simpler and more efficient than X11. Provides better support for modern GPUs. | C |
|  | **EGL** | Interface between Khronos rendering APIs (like OpenGL) and native window systems (like X11 or Wayland). Manages contexts and surfaces. | C |
| **High-Level Visualization** | **Matplotlib** | Python 2D plotting library, designed for producing publication-quality graphs and figures. | Python |
|  | **Plotly** | High-level graphing library for interactive plots. Generates D3.js-based visualizations in web browsers. | Python, JavaScript, R |
|  | **VMD (Visual Molecular Dynamics)** | Molecular visualization program used for displaying, animating, and analyzing large biomolecular systems using 3D graphics. | C, Python |
|  | **ParaView** | Open-source application for large-scale 3D data visualization. | C++, Python |
| **Image Processing** | **OpenCV** | Library for computer vision and image processing, offering fast access to algorithms for image recognition, object tracking, and more. | C++, Python |
|  | **ImageMagick** | Command-line tool and API for converting, editing, and composing bitmap images. Supports a wide variety of formats. | C, Python |

### Visualization

### Verification

> [Verification](https://www.notion.so/Verification-1c1c0f5171ec8010ae66c140e13114c9?pvs=21).

## Data System

> …

### Storage

> ..

### Streaming System

> …

### In-Memory Storage

> …

### Data Grid

> …

### Migration

> …

### Data Migration

> ….

### ORM

> DAL: Database Abstraction Layer.

### Replication

## Cache System

| **Category** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **In-Process (Local Memory)** | Cache lives inside the application process; very low latency, limited to process memory. | Ehcache (in-memory mode), Caffeine, Guava Cache |
| **Distributed In-Memory Key-Value** | Cache shared across multiple nodes; RAM-based, partitioned or replicated; low-latency network access. | Redis Cluster, Memcached, Hazelcast, Apache Ignite (in-memory mode) |
| **Hybrid (Persistent Cache)** | Cache keeps hot data in memory and persists to disk for durability or large datasets. | Apache Ignite (persistent mode), Hazelcast with persistence, Ehcache with disk store |
| **Disk-Based (Out-of-Memory)** | Primary storage on disk; memory used for caching indices or hot data; slower but durable. | RocksDB, LevelDB, LMDB, BerkeleyDB |
| **Managed Cloud Cache Services** | Cloud-managed caching services; may offer distributed in-memory or hybrid options. | Amazon ElastiCache (Redis/Memcached), Azure Cache for Redis, Google Cloud Memorystore |
| **Streaming / Event-Driven Cache** | Supports caching for real-time streaming or event processing; often integrates with messaging systems. | Apache Kafka Streams (state stores), Hazelcast Jet, Redis Streams |

## Status Page

> …

## **Internationalisation and Localisation**

> …

## Locks

> …

## Rate Limiting

> …

## Search System

> …

## **Scheduler**

> …

## **Load Balancer**

> …

## Server Node

> …

## Microservices Framework

> …

## Event-Driven Architecture (EDA)

> …

## **Communication Protocols**

> API’s …

### Web Socket

### TCP

### HTTP

### Message Queue

## Failure Recovery

> …

## Security

> ….

### Public Key Cryptography

> …

### …

## API Tester

> See more in [HTTP](https://www.notion.so/HTTP-02db6de08e44446fb37b31659c61555f?pvs=21).
> 
- VS Code Rest Client https://marketplace.visualstudio.com/items?itemName=humao.rest-client
- API Tester  https://chromewebstore.google.com/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm?hl=en
- RESTer https://chromewebstore.google.com/detail/rester/eejfoncpjfgmeleakejdcanedmefagga?hl=en
- Curl

## Analysis & Monitoring

> Performace, Security, Domain Related Analysis: HCI Analytics & Debugging.

### **Code Quality**

### **Code Analysis**

### Instrumentation

### Profiling

## Virtualization

> …

## **Computing Platform**

> …

- IaaS
- PaaS
- SaaS

### Formal Methods

### Static Analysis

### Unit Testing

## Configuration Management

> …

## Package Manager

> …

## Build Tools

> …

## Low Latency Processing

> or Real - Near Real Time Processing

## Job Processing

> …

## Workflow Processing

> ..

## Version Control

> …

## **Deployment**

> …

## CI/CD

> …

| **Category** | **Subcategory** | **Tools** | **Examples** |
| --- | --- | --- | --- |
| **Software Engineering Tools** | Development Tools | Tools for writing and managing code | IDEs (Visual Studio, IntelliJ), Text Editors (VS Code, Sublime), Version Control (Git, SVN), Build Systems (Maven, Gradle) |
|  | Language System |  | GCC, JDK, … |
|  | Testing Tools | Tools for automating and managing tests | Unit Testing (JUnit, Pytest), Integration Testing (Selenium), Test Automation (Jenkins) |
|  | Debugging Tools | Tools for identifying and resolving issues | Debuggers (GDB, LLDB), Profilers (Valgrind, JProfiler) |
|  | Collaboration Tools | Tools for team collaboration | Project Management (Jira, Trello), Communication (Slack, Microsoft Teams) |
| **Software System Components** | Databases | Tools for storing and managing data | SQL (PostgreSQL, MySQL), NoSQL (MongoDB, Cassandra) |
|  | Queue Systems | Tools for managing communication between services | Message Brokers (RabbitMQ, Kafka) |
|  | Caching Systems | Tools for improving system performance | Caching (Redis, Memcached) |
|  | Data Lakes | Tools for storing large, unstructured or semi-structured data | Hadoop, Amazon S3, Azure Data Lake |
|  | Data Warehouses | Tools for storing structured data for analytical purposes | Google BigQuery, Amazon Redshift, Snowflake |
|  | Networking Tools | Tools for managing communication between systems | Load Balancers (Nginx, HAProxy), API Gateways (Kong, Apigee) |
|  | Authentication & Authorization | Tools for user identity and access control | OAuth, OpenID Connect, SSO systems |
|  | Storage & File Systems | Tools for managing file storage | Cloud Storage (Amazon S3, Google Cloud Storage), Distributed File Systems (HDFS, Ceph) |
| **Operational & Maintenance Tools** | Deployment Tools | Tools for automating deployment processes | CI/CD (Jenkins, GitHub Actions, CircleCI) |
|  | Monitoring & Logging Tools | Tools for tracking system performance and logs | Monitoring (Prometheus, Grafana), Logging (ELK Stack, Splunk) |
|  | Configuration Management | Tools for automating software system configuration | Ansible, Puppet, Chef |
|  | Containerization & Orchestration | Tools for managing containers and distributed systems | Docker, Kubernetes |
| **Machine Learning Tools** | Machine Learning Engineering | Tools for processing data, training models, and deploying them | Apache Spark, Dask, TensorFlow, PyTorch, Keras, MLflow |
|  | Model Deployment & Scaling | Tools for deploying and scaling machine learning models | TensorFlow Serving, MLflow, Kubernetes, AWS SageMaker |
|  | Model Monitoring Tools | Tools for monitoring model performance and drift | MLflow, Seldon, Prometheus |
| **Machine Learning Libraries** | ML Algorithms | Pre-built libraries for machine learning algorithms and models | Scikit-learn, XGBoost, LightGBM, CatBoost |
|  | Deep Learning Libraries | Libraries specifically for deep learning applications | TensorFlow, PyTorch, Keras, Caffe |
| **Software System Library Tools** | Data Processing Libraries | Libraries for processing, transforming, and analyzing data | NumPy, Pandas, Dask, Apache Spark, Vaex |
|  | Web Frameworks | Libraries for developing web applications | Django, Flask, Express.js, Spring Boot |
|  | UI/Frontend Libraries | Libraries for building user interfaces | React, Vue.js, Angular, Svelte |
|  | Networking Libraries | Libraries for managing network requests and APIs | Axios, Requests (Python), Retrofit (Java), Fetch API (JavaScript) |
|  | Cryptography Libraries | Libraries for implementing encryption, decryption, and security | OpenSSL, PyCryptodome, Bouncy Castle |
|  | Testing Libraries | Libraries specifically for testing frameworks and utilities | Mocha, Chai (JavaScript), JUnit, Pytest |
|  | Data Visualization Libraries | Libraries for visualizing data and analysis results | Matplotlib, Seaborn, Plotly, D3.js |

## Documentation

> ….

> Observatory of Skills: Praxis log and potential improvements to increase productivity.
> 

> Observatorio de Habilidades: Bitácora de praxis y posibles mejoras para incrementar la productividad.
> 

> See more in Bremontix Ars and https://github.com/dbremont/.
> 

> https://www.joinenginuity.com/;
> 

TODO:

- Query Execution Engine
- Execution Plan
- The Concept of Cardinality
- Be able to trace network calls.
- We have a stream of problems—bugs—coming from a given software system. Can we really improve the software by looking at the bugs in isolation? For example, if we assign them to different programmers, will that approach lead to meaningful system improvements?
    - Key concepts to elaborate and answer - synergies between bugs - solutions. Connection Between Bugs. Deep underlying patters.

## Index

## Breviarium

- [ ]  Security → Pass Keys.
- [ ]  Make a C program that downloads a file from a site with/without SSL OR TSL Verification.
- [ ]  Create a Distributed System Lab To Study Scalability.
- [ ]  Think Deeply about Serializing Intelligence and Organization a Platform for It & Communication.
    - [ ]  Lab Transmission de Archivo, HTTP.
    - [ ]  La Test Transactions Hibernate y Postgres SQL.
    

## Practice

- [ ]  Estudiar - Lexical Analysis
- [Scanning](https://www.notion.so/Scanning-220c0f5171ec80258726df5c4be7cbd1?pvs=21)
- https://en.wikipedia.org/wiki/Deterministic_finite_automaton
- http://github.com/dbremont/language-system-labs/

## 🔧 **Core Utility Tool**

- [ ]  Random Number Generator (RNG)

### PDF

- https://pdfe.com/app/my-documents
- …

## GIT

- [ ]  Improve my understanding of `git merge.`
- [ ]  …

## Diction

> [A Guide to Improve Spanish Diction](https://www.notion.so/A-Guide-to-Improve-Spanish-Diction-203c0f5171ec80108681f48aeeaa54b3?pvs=21)
> 

## Design

- [ ]  https://github.com/excalidraw/excalidrawhttps://github.com/excalidraw/excalidraw

## System Integration

> Note:  Gateway is a very similar idea.
> 
- https://api200.co/
- https://github.com/API-200/api200
- https://apisix.apache.org/ → Gateway.
- https://zapier.com/
- https://airbyte.com/
- https://www.nango.dev/
- WhatsApp Business.
- https://github.com/pathwaycom/pathway
- https://github.com/huginn/huginn

## Billing System

- [ ]  https://docs.craterapp.com/
- [ ]  https://invoiceninja.com/

## CLI

- [ ]  https://typer.tiangolo.com/

## GUI

- [ ]  https://news.ycombinator.com/item?id=44872313
- [ ]  https://github.com/derekeder/csv-to-html-table

## Report Generation

- [ ]  https://carbone.io/
- [ ]  JasperReports
- [ ]  https://weasyprint.org/
- [ ]  General Templates Engines → Handlebar.

## Documentation

- [ ]  https://vrite.io/

## **Automated Data Extraction System**

- [ ]  https://github.com/scrapy/scrapy
- [ ]  …

## Data System

- [ ]  Base Migration
- [ ]  https://github.com/ClickHouse/ClickHouse
- [ ]  https://www.graphile.org/postgraphile/
- [ ]  https://news.ycombinator.com/item?id=44955459

## Data Format & Serialization

- [ ]  https://github.com/apache/fory
- [ ]  …

## Storage System

- [ ]  https://github.com/seaweedfs/seaweedfs

## Distributed System

- [ ]  Distributed Counter.
- [ ]  CRDTs (Conflict-Free Replicated Data Types).
- [ ]  Distributed Lock
- [ ]  …

## Geographic Information Systems (GIS)

- [ ]  Map Visualization

## Video System Integration

> …
> 

## Static Site Generator

- [ ]  https://www.mkdocs.org/

## Backend-as-a-Service (BaaS)

- [ ]  [TrailBase](https://github.com/trailbaseio/trailbase) — an open, single-executable Firebase alternative: SQLite + type-safe APIs + realtime subscriptions + auth, with a built-in WebAssembly runtime for the custom logic. The self-hosted row of the BaaS space, and the one that keeps the database in the deployable.
- [ ]  https://formspree.io/ - **Formspree is a serverless form handling and submission API service**, used to process form submissions without needing to build your own backend.
- [ ]  https://formcarry.com/
- [ ]  https://getform.io/
- [ ]  https://docs.docker.com/engine/containers/runmetrics/

## Security

- [ ]  https://news.ycombinator.com/item?id=43971068
- [ ]  Supabase Auth
- [ ]  Clerk.dev
- [ ]  https://next-auth.js.org/
- [ ]  https://authjs.dev/
- [ ]  Keycloak
- [ ]  https://hub.docker.com/r/steveltn/https-portal/
- [ ]  https://github.com/FiloSottile/mkcert
- [ ]  https://github.com/pocket-id/pocket-id
- [ ]  https://www.keycloak.org/
- [ ]  https://fidoalliance.org/passkeys/
- [ ]  https://github.com/S3N4T0R-0X0/APT-Attack-Simulation
- [ ]  https://github.com/NextronSystems/APTSimulator



## Workflow Orchestration

- [ ]  https://github.com/cadence-workflow/cadence
- [ ]  https://temporal.io/
- [ ]  Apache Airflow
- [ ]  Task Queue
    - [ ]  Celery
    - [ ]  RQ (Redis Queue)
- [ ]  Business Process Management Suites
    - [ ]  Zeebe
    - [ ]  Camunda
- [ ]  https://github.com/Netflix/conductor
- [ ]  https://n8n.io/
- [ ]  https://github.com/shopify/roast

## Development Workflow

- [ ]  https://www.focalboard.com/
- [ ]  https://www.librechat.ai/
- [ ]  https://cursor.com/
- [ ]  https://github.com/sst/opencode

## Enterprise Information System

- [ ]  https://strapi.io/

## No-Code

- [ ]  https://github.com/appsmithorg/appsmith
- [ ]  …

## Internationalization and Localization

> …
> 
- [ ]  https://en.wikipedia.org/wiki/Internationalization_and_localization

## Language System

- Look Parsing in One of My Failures Points - Please Learn How to Parse Things.
- https://writewithharper.com/ - Grammar Checker - With Language Server.

## AI Assistant

- https://github.com/menloresearch/jan
- …

## Multimedia Systems

> See more in https://github.com/dbremont/visiotecnica-labs and https://github.com/dbremont/language-system-labs/tree/main/tools/multimedia
> 
- [ ]  Create a Simple Video player with SDL  - Linux  - X11.

## Intelligent Systems

- [ ]  https://github.com/rasbt/LLMs-from-scratch/tree/main
- [ ]  https://biomni.stanford.edu/
- [ ]  https://github.com/open-webui/open-webui
- [ ]  https://lmstudio.ai/docs/app
- [ ]  https://github.com/Canner/WrenAI
- [ ]  https://github.com/emcie-co/parlant

### RLVR/RLHF Libraries

- verl - ByteDance
- TRL - HuggingFace
- slime - Zhipu AI
- prime-rl - Prime Intellect
- ROLL - Alibaba
- Nemo-RL - NVIDIA
- AReaL - Ant Research
- SkyRL - UC Berkeley
- open-instruct - Allen AI
- torchtune - PyTorch
- https://github.com/OpenPipe/ART

## Status Page

- [ ]  https://github.com/TwiN/gatus
- [ ]  …

## Computational Software System Analysis

- [ ]  https://github.com/sharkdp/hyperfine
- [ ]  https://github.com/hengyoush/kyanos
- [ ]  Log the stack trace when a thread is created in Java.
- [ ]  https://www.slf4j.org/api/org/slf4j/Logger.html
- [ ]  https://github.com/jedisct1/yes-rs Why is this fast?

## **Paste Service**

- [ ]  https://pastebin.com/
- [ ]  https://rentry.co/

## QR Code Generator

- [ ]  https://justaqrcode.com/

## Text Autosuggestion

> Powering Corrections, etc.

> Text Autosuggestion is a real-time linguistic inference mechanism that predicts and proposes candidate tokens (words, phrases, or character sequences) during user text input, based on partial input and contextual signals.

Constitutive Techniques:

- Probabilistic Language Modeling
- Sequence Modeling (Autoregression)
- Context Encoding
- Candidate Generation
- Ranking & Scoring
- Spell Correction Integration
- Personalization & Online Adaptation
- Latency Optimization Techniques
- UI Mediation Strategy

Constitutive Technical Objects: (Can these techniques be embedded into a technical object that can be integrated **(Embeddable)** to build larger end products?)

- ...

Evaluation Metrics -> (Solutions -> Trade offs):

- ...

Cases:

- Apple Inc. Method, System, and Graphical User Interface for Providing Word Recommendations. U.S. Patent 8,074,172 B2, issued December 6, 2011.
- Gboard — Gboard
- SwiftKey — Microsoft SwiftKey
- Gmail Smart Compose

## References

- [ ]  [A Guide to Quick Prototype Software Systems](https://www.notion.so/A-Guide-to-Quick-Prototype-Software-Systems-20cc0f5171ec8089bc0ed2c37beb3833?pvs=21)
- [ ]  https://gist.github.com/dbremont/10ef404e1feaf6cee3cf15ab14282f43
- [ ]  https://deepwiki.org/
- [ ]  https://www.admonymous.co/
- [ ]  https://github.com/OpenSignLabs/OpenSign
- [ ]  https://github.com/lechmazur/elimination_game
- [ ]  Terminal Recording - https://github.com/faressoft/terminalizer
- [ ]  https://github.com/codecrafters-io/build-your-own-x
- [ ]  ‣
- [ ]  [A Guide to Quick Prototype Software Systems](https://www.notion.so/A-Guide-to-Quick-Prototype-Software-Systems-20cc0f5171ec8089bc0ed2c37beb3833?pvs=21)
- [ ]  ‣
- [ ]  https://github.com/thedevdojo/wave?tab=readme-ov-file
- [ ]  https://github.com/borglab/gtsam
- [ ]  https://github.com/halide/Halide

https://github.com/evershopcommerce/evershop

https://github.com/strapi/strapi

- https://lmstudio.ai/

https://github.com/niespodd/browser-fingerprinting

https://strudel.cc/workshop/getting-started/

https://perma.cc/

- [ ]  https://github.com/datalab-to/marker
- [ ]  https://github.com/datalab-to/surya
- [ ]  https://github.com/ast-grep/ast-grep

https://www.paradedb.com/

https://github.com/fullcalendar/fullcalendar

https://github.com/unfoldadmin/django-unfold?tab=readme-ov-file

https://github.com/lucasdillmann/nginx-ignition/tree/main

https://karpathy.bearblog.dev/digital-hygiene/

https://www.swyx.io/virtual-mailbox

https://github.com/cointop-sh/cointop/

UI Design

- https://dribbble.com/tags/complex-ui
- https://www.reddit.com/r/UXDesign/comments/1f2fxpt/what_is_the_most_complicated_user_interface_you/
- https://www.nngroup.com/articles/wizards/

https://stately.ai/docs

https://en.wikipedia.org/wiki/Finite-state_machine

https://github.com/YaoApp/yao

https://www.8090.ai/

https://www.metamap.com/

https://www.cvedetails.com/cve/CVE-2025-56383/

https://github.com/hluk/CopyQ 

https://github.com/QwenLM/Qwen3-VL/tree/main/cookbooks

https://think-async.com/Asio/

Universal Search Function - One Search - All types of Entities - Documents

Data Replication:

- Kafka
- Kafka
- https://debezium.io/
- Change Data Capture (CDC)
- https://en.wikipedia.org/wiki/Oracle_Streams

https://github.com/wizenheimer/blaze

I trully have a weak concept of structured concurrency

Fixed mkdocs  search system displaying  tables

Think Deeply about Design

- https://chatgpt.com/share/68efacc6-6988-8001-8d45-df53146d9f68

https://github.com/PaddlePaddle/PaddleOCR

https://www.fast.ai/posts/2025-10-16-karpathy-tokenizers.html

Nginix:

- Under which user does the process runs?
- What does sites-enabled and sites aviable means?
- Does Nginix serves symlinks?
- How to connect NOTIFY GIBHUB REPO events to my some server - to build and deploy my app?
    - Github Webhooks
    - GitHub Actions
    - GitHub does **not** allow `post-receive` hooks directly.
    - **Third-party CI/CD tools:** GitLab CI, Jenkins, CircleCI, etc., can listen to GitHub via webhooks or API and update your server automatically.
    - Jenkins
    - gocd
- What CI means?
- …

https://github.com/microsoft/data-formulator/?tab=readme-ov-file - The Modern Problem It’s With Analytical Tool - Is With the Praxis Necesasary to Make Them Useful

Thread Local Cache in C++ - https://github.com/lemire/Code-used-on-Daniel-Lemire-s-blog/tree/master/2025/10/19/

https://github.com/bruin-data/ingestr/

https://www.reddit.com/r/Python/comments/1o04g6v/i_benchmarked_5_different_fastapi_file_upload/

https://stackoverflow.com/questions/59393486/what-exactly-is-pythons-spooledtemporaryfile

https://github.com/Infisical/infisical/

https://github.com/openreplay/openreplay/

https://github.com/rrweb-io/rrweb

https://status.io/

https://github.com/sinaptik-ai/pandas-ai

https://github.com/TarekRaafat/autoComplete.js/

Programming Tips:

- Satinize File Path for Storage? What security problems can this entail if not done?

Monitoring:

- HA Proxy

Fast App Prototyping:

- Authentication Provider
- State Model Storage  Mechanism → Relational DB,  Documents DB, … Postgrest Rest
- **PostgREST** → instant REST API for your tables, views, and RPCs
- **Realtime engine** → websocket-based subscription to database changes
- **Auth** → user management, JWTs, Row Level Security integration
- **Storage** → file/object storage with access control
- **Edge Functions** → serverless functions for custom logic
- **Dashboard** → visual SQL editor, table view, API explorer
- https://github.com/open-webui/open-webui/tree/main

https://garagehq.deuxfleurs.fr/

- https://en.wikipedia.org/wiki/Coefficient_of_determination

https://docs.asciinema.org/

https://affine.pro/pricing

https://hub.docker.com/

https://www.arxiv.org/abs/2510.15511

- https://news.ycombinator.com/item?id=45751400
- https://news.ycombinator.com/item?id=45747018

https://github.com/MiniMax-AI/MiniMax-M2

https://github.com/bkhtmltopdf/bkhtmltopdf

Monitoring:

- logrotate
- sudo journalctl --rotate
- sudo journalctl --vacuum-time=1s
- du -h --max-depth=4 / 2>/dev/null | sort -hr | head -20

https://github.com/jherkenhoff/STM

UI Automation [Do we Have Another Name For This] - User Automation - HCI Automation:

- https://droidrun.ai/
- https://github.com/droidrun/droidrun?tab=readme-ov-file
- 
- **Sobre los Contratos**: …
    - https://www.docuseal.com/
    - https://www.signserver.org/
    - https://documenso.com/
- https://www.opensignlabs.com/
- https://github.com/normal-computing/fuji-web/
- https://www.solidjs.com/
- https://github.com/Bash-it/bash-it/
- https://github.com/idkhub-com/reactive-agents
- https://immich.app/ (Image Server)
- https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B

- https://github.com/OvidijusParsiunas/deep-chat?fbclid=IwAR0uSvTiVXL5rICg3YfKqV2er0E355LGrg5ha6JVkUEaem8PKU98sU6ysbE



## References

- [Software Value Chain](https://ideas.repec.org/p/dar/wpaper/52732.html)
- [Tool](https://en.wikipedia.org/wiki/Tool)
- [miscellanea-labs](https://github.com/dbremont/miscellanea-labs)
- [Profiler](https://www.notion.so/Profiler-1c1c0f5171ec80f0ae85c627e8971d92?pvs=21)
- [documentorum](https://github.com/dbremont/documentorum)

