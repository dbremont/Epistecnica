---
tags: [note, production]
---

# Digital Production Sector

> In this note we will analyze several aspects of the software industry — as an overview — with links to Bremontix and to the entire production process, including market analysis and related topics.

> Digital Production Sector.

> Note: This note is highly unfinished, including its formulation. Open question: Does a newsfeed aggregator — a type of software — belong within the Digital Production Sector?

> Note: For organizational reasons, Machine Learning (ML) is considered part of the software industry.

Guiding Questions:

* What is the *product space* of the software industry? What is the structure of production inside a software firm?
* What is the *technical space* of the industry? How technical research works?
  - Are software techniques *operational*, or something else? For example, is a technique for implementing a hash table an operational technique? Or is it considered operational because it functions as part of the language’s building blocks?
* What are the *markets* of the industry?
* (Add more guiding questions as needed.)

## Product Space Taxonomy

> Guiding Question: What types of products does the Digital Sector produce?

> Note: To map the digital sector effectively, it is better to begin with the digital product space, since many industry classifications are arbitrary. For example, the gaming industry produces “games,” yet these are also part of the broader software publishing sector. Starting from products avoids artificial boundaries.

### Structure

> Goal: To provide a comprehensive and structured framework for tagging and classifying digital products across four orthogonal dimensions. Each dimension captures a different aspect of the product’s purpose, form, implementation, and market context.

> How to structure the space?

**Role Dimension**: The Role of a product exhibits a dual structure:

* **Primary** Intent—the immediate function the product performs; and
* **Secondary** Function—the broader capabilities, interactions, or system behaviors that the product facilitates.

| **Dimension**        | **Description**                                          | **Value**     | **Value Description**                                                              |
| -------------------- | -------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------- |
| **Role**             | The functional purpose or “why” the product exists.      | Information   | Provides, organizes, or structures information.                                    |
|                      |                                                          | Communication | Enables messaging, interaction, or signal exchange.                                |
|                      |                                                          | Coordination  | Aligns actions, workflows, schedules, or multi-actor processes.                    |
|                      |                                                          | Analysis      | Extracts insights, patterns, or meaning from data.                                 |
|                      |                                                          | Control       | Monitors, regulates, or stabilizes systems or processes.                           |
|                      |                                                          | Creation      | Produces, transforms, or synthesizes content or artifacts.                         |
|                      |                                                          | Storage       | Persists data, state, or digital content.                                          |
|                      |                                                          | Transaction   | Executes economic, operational, or procedural exchanges.                           |
|                      |                                                          | Automation    | Performs tasks or processes without human intervention.                            |
|                      |                                                          | Distribution  | Delivers or disseminates content, data, or services across channels.               |
| **Product Form**     | Ontological nature of the product (artifact vs service). | Good          | A discrete digital artifact that exists independently after delivery.              |
|                      |                                                          | Service       | A continuous, ongoing delivery requiring provider-side activity or compute.        |
| **Computationality** | Whether the value delivery depends on computation.       | Yes           | Requires active computation (APIs, cloud services, ML inference, pipelines, etc.). |
|                      |                                                          | No            | Delivers value without further computation (documents, media files, offline apps). |
| **Use Domain**       | The primary environment, sector, or audience of use.     | Consumer      | Used by individuals for personal activities or needs.                              |
|                      |                                                          | Enterprise    | Used by organizations for administrative or operational functions.                 |
|                      |                                                          | Industrial    | Used in manufacturing, energy, logistics, or other heavy-industry environments.    |
|                      |                                                          | Government    | Used by public institutions, agencies, or civic systems.                           |
|                      |                                                          | Scientific    | Used for research, modeling, simulation, or computation-heavy inquiry.             |
|                      |                                                          | Creative      | Used to produce artistic, media, or design-related content.                        |
|                      |                                                          | Education     | Used in teaching, learning, academic administration, or training.                  |
|                      |                                                          | Financial     | Used in banking, payments, trading, accounting, or investment.                     |

Others Tags:

| **Product Notion**        | **Description**                                            | **Role**                                | **Product Form** | **Comp.** | **Use Domain**          |
| ------------------------- | ---------------------------------------------------------- | --------------------------------------- | ---------------- | --------- | ----------------------- |
| Mobile App                | A packaged software artifact installed locally on devices. | Information / Communication / Creation  | Good             | No        | Consumer / Enterprise   |
| SaaS Application          | A remotely delivered application accessed via the cloud.   | Coordination / Transaction / Automation | Service          | Yes       | Enterprise              |
| API Endpoint              | Programmatic interface exposed over a network.             | Coordination / Distribution             | Service          | Yes       | Enterprise / Industrial |
| ML Model (Static)         | A trained model distributed as an artifact.                | Analysis                                | Good             | No        | Scientific / Enterprise |
| ML Inference Service      | Model served via compute infrastructure.                   | Analysis / Automation                   | Service          | Yes       | Enterprise / Industrial |
| Database System           | Software designed to store and retrieve structured data.   | Storage / Coordination                  | Good             | No        | Enterprise              |
| Cloud Storage             | Provider-managed storage accessible over the network.      | Storage                                 | Service          | Yes       | Enterprise / Consumer   |
| Digital Media File        | Standalone audio, video, or image asset.                   | Distribution / Information              | Good             | No        | Consumer                |
| Industrial Control System | Software controlling machines or industrial processes.     | Control / Automation                    | Service          | Yes       | Industrial              |
| E-commerce Platform       | System enabling the execution of commercial transactions.  | Transaction / Coordination              | Service          | Yes       | Consumer / Enterprise   |
Dataset

### Type Space

> Which are the products types - from the used domain?

> These are concrete, usable product types (not abstract meta-categories).

> Note: “Mobile App” is an abstract container category. In this section we list actual product types such as Streaming Service, CRM System, Trading Engine, etc., each representing a functionally coherent class of digital products.

| **Product Type**                     | **Description**                                                | **Role**                     | **Product Form** | **Computationality** | **Use Domain**          |
| ------------------------------------ | -------------------------------------------------------------- | ---------------------------- | ---------------- | -------------------- | ----------------------- |
| **Social Media Service**             | Network platform enabling communication and sharing.           | Communication / Distribution | Service          | Yes                  | Consumer                |
| **Streaming Service**                | On-demand delivery of digital media.                           | Distribution                 | Service          | Yes                  | Consumer                |
| **Digital Media File**               | Audio, video, or image artifact.                               | Information / Distribution   | Good             | No                   | Consumer                |
| **Operating System**                 | System software managing hardware and applications.            | Control / Coordination       | Good             | Yes                  | General-purpose         |
| **Development Tool**                 | Tools to create, debug, and deploy software.                   | Creation / Transformation    | Good             | Yes                  | Technical               |
| **Data System (DBMS, Cache, etc.)**  | Systems for storing, indexing, and retrieving structured data. | Information / Coordination   | Service          | Yes                  | Technical / Enterprise  |
| **SaaS Productivity Suite**          | Cloud-based office and collaboration tools.                    | Coordination                 | Service          | Yes                  | Enterprise              |
| **CRM System**                       | Customer relationship and sales management.                    | Coordination / Analysis      | Service          | Yes                  | Enterprise              |
| **ERP System**                       | Integrated enterprise operations management.                   | Coordination / Transaction   | Service          | Yes                  | Enterprise              |
| **Business Intelligence Dashboard**  | Visual analytics and reporting environment.                    | Analysis                     | Service          | Yes                  | Enterprise              |
| **SCADA System**                     | Supervisory control of industrial processes.                   | Control / Monitoring         | Service          | Yes                  | Industrial              |
| **Industrial IoT Platform**          | Sensor integration and industrial data orchestration.          | Coordination / Control       | Service          | Yes                  | Industrial              |
| **PLC Configuration Software**       | Programming tool for industrial controllers.                   | Creation / Control           | Good             | No                   | Industrial              |
| **Digital Twin Model**               | Virtual replica of physical systems.                           | Analysis / Simulation        | Good             | No                   | Industrial              |
| **e-Government Portal**              | Web interface for accessing public services.                   | Transaction / Coordination   | Service          | Yes                  | Government              |
| **Census Data Platform**             | Access and analysis of population data.                        | Information / Analysis       | Service          | Yes                  | Government              |
| **Identity Management System**       | Digital identity authentication and control.                   | Control / Transaction        | Service          | Yes                  | Government              |
| **Simulation Software**              | Tools for modeling physical or computational systems.          | Analysis / Simulation        | Good             | No                   | Scientific              |
| **HPC Compute Service**              | High-performance computational resources on demand.            | Transformation / Analysis    | Service          | Yes                  | Scientific              |
| **Research Dataset**                 | Curated scientific or technical dataset.                       | Information                  | Good             | No                   | Scientific              |
| **ML Model**                         | Trained machine learning artifact for inference.               | Analysis / Automation        | Good             | No                   | Scientific / Enterprise |
| **Design Tool**                      | Tools for graphic, industrial, or UX design.                   | Creation                     | Good             | No                   | Creative                |
| **DAW (Digital Audio Workstation)**  | Audio composition and editing environment.                     | Creation                     | Good             | No                   | Creative                |
| **Asset Marketplace**                | Platform to buy and sell digital creative assets.              | Distribution / Transaction   | Service          | Yes                  | Creative                |
| **LMS (Learning Management System)** | Platform for course management and delivery.                   | Coordination / Distribution  | Service          | Yes                  | Education               |
| **Digital Textbook**                 | Digital instructional content.                                 | Information                  | Good             | No                   | Education               |
| **Online Banking Platform**          | Interface for managing digital financial operations.           | Transaction / Information    | Service          | Yes                  | Financial               |
| **Trading Engine**                   | Automated execution of market trades.                          | Transaction / Control        | Service          | Yes                  | Financial               |
| **Accounting Software**              | Tool for financial record management.                          | Information / Coordination   | Good             | No                   | Financial               |

## Software Industry Structure

> ...

## Technology

| **Technique Dimension**                 | **Description**                                                                                                                                          | **Instance(s)**                                                                                              |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Technical Research Technique**        | Methods for generating new technical knowledge; concerned with discovery, invention, modeling, and theoretical–experimental exploration.                 | Scientific experimentation, algorithm research, materials R&D, ML model training, simulation-based inquiry   |
| **Operational Technique**               | Methods for operating, maintaining, executing, and supervising technological systems in real environments; grounded in procedure and routine.            | DevOps, IT operations, manufacturing operations, NOC processes, industrial control routines                  |
| **Constitutive Technique**              | Techniques for creating technological systems: designing, assembling, composing, implementing, and architecting components into functioning wholes.      | Software architecture, system design patterns, PCB design, CAD/CAM methods, compiler construction            |
| **Representational Technique**          | Techniques for encoding, modeling, abstracting, and representing phenomena, structures, or processes so they can be understood or processed technically. | Data modeling, ontology design, UML diagrams, mathematical modeling, visualization methods                   |
| **Diagnostic Technique**                | Techniques for identifying, analyzing, and explaining faults, inefficiencies, or anomalies in systems.                                                   | Debugging, profiling, root cause analysis, system health monitoring, failure analysis                        |
| **Measurement Technique**               | Techniques for quantifying properties, states, or performance of systems or phenomena.                                                                   | Telemetry, instrumentation, benchmarking, metrology, sensor calibration                                      |
| **Optimization Technique**              | Techniques for improving systems—reducing cost, increasing performance, improving efficiency, tuning parameters, or optimizing processes.                | Performance tuning, algorithmic optimization, control optimization, A/B testing                              |
| **Integration Technique**               | Techniques for connecting heterogeneous components, systems, or subsystems into cohesive, interoperable architectures.                                   | API integration, data pipeline assembly, enterprise system integration, robotics system integration          |
| **Validation & Verification Technique** | Techniques used to ensure correctness, reliability, and adherence to requirements or constraints.                                                        | Testing, formal verification, compliance checks, QA pipelines                                                |
| **Protection & Safety Technique**       | Techniques ensuring security, safety, integrity, or resilience of systems.                                                                               | Cryptographic methods, access control schemes, safety engineering, hazard analysis, cybersecurity monitoring |
| **Execution Technique**                 | Techniques related to runtime execution, deployment, and distribution of technological artifacts.                                                        | Build systems, container orchestration, distributed execution frameworks, CI/CD pipelines                    |
| **Materialization Technique**           | Techniques for transforming designs into physical artifacts (in cyber-physical or hardware systems).                                                     | Fabrication processes, additive manufacturing, machining techniques, semiconductor processes                 |

## References

* [Bremontix Ars](https://righteous-guardian-68f.notion.site/In-136c0f5171ec80f9a969eb374ac750c6?source=copy_link)
* Software Technology
* Technology
* [A Guide to Profile an Industry](/view.html?p=notes/technica/breviarium/a-guide-to-profile-an-industry.md)
* [Taxonomy of Software Products](https://righteous-guardian-68f.notion.site/Computational-System-Space-195c0f5171ec80dc9d11e8dc52cbad9c?source=copy_link)
* [Software Market Size](https://www.grandviewresearch.com/industry-analysis/software-market-report)
* [The Software Complexity of Nations](https://arxiv.org/abs/2407.13880)
* [A Guide Computational System Implementation Toolkit](https://righteous-guardian-68f.notion.site/A-Guide-Computational-System-Implementation-Toolkit-1b5c0f5171ec8038909ef15467f06fb2?source=copy_link)
* [Software Product Space](/view.html?p=notes/social/good/software/readme.md)
