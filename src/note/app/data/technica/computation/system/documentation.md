# Documentation

> In this note we will reason about **Documentation (knowledge transfer without rediscovery).**
> 

> The main cache - system - of Humanity.
> 

> **Documentation** is the discipline of externalizing knowledge into persistent artifacts so that it can be transmitted across agents and generations, transforming individual discovery into cumulative knowledge. By doing so, it enables future agents to acquire mastery of a technical or epistemic domain without repeating the original experimentation, reasoning, observation, or practical learning that produced the knowledge.
> 

> **Note:** **Documentation** does not eliminate the cost of knowledge acquisition; it reduces it by eliminating the need to rediscover previously acquired knowledge.
> 

> Note: The organizing principle of this guide is the scaffolding of documentation, not the documentation process (lifecycle) itself.
> 

## Formulation

> **Documentation can be conceived as a technical activity** concerned with the systematic capture, organization, representation, and maintenance of knowledge.
> 

> The **activity of documentation** can be decomposed into several steps: knowledge acquisition, knowledge structuring, knowledge representation, knowledge validation, and knowledge preservation.
> 

> A **document** is a written, visual, or **digital representation** that contains information, content, or data, often organized in a structured or coherent manner, and intended to convey knowledge, ideas, instructions, or communication.
> 

### Technical Element Catalog

> Which are the set of **technical elements** that power the **documentation activity**?
> 

| Category | Description | Instance(s) |
| --- | --- | --- |
| **Documentation Technical Purpose** | The intended technical function of documentation: preserving, communicating, transferring, and operationalizing knowledge about Technical Objects, Processes, and Practices. | Enable system understanding; reduce maintenance cost; support operation; preserve design rationale; enable onboarding; support verification and compliance. |
| **Documentation Technical Problem** | The discrepancy between the knowledge required to operate, modify, verify, or reproduce a technical object and the knowledge currently available or accessible. | "Developers cannot safely modify a legacy system because architectural knowledge is lost"; "Operators cannot recover a failed production system because procedures are undocumented." |
| **Documentation Technical Requirement** | The explicit properties that documentation must satisfy. | Accuracy, completeness, consistency, accessibility, traceability, maintainability, version control, audience appropriateness. |
| **Documentation Technical Activity** | The organized sequence of technical acts through which technical knowledge is captured, structured, represented, validated, and maintained. | Documentation lifecycle: discovery → extraction → modeling → writing → review → publication → maintenance. |
| **Documentation Technical Agent** | The entity performing documentation activities. | Software engineer, technical writer, architect, domain expert, AI documentation assistant, automated documentation generator. |
| **Documentation Technical Object  (Deliverable)** | The produced artifact that carries documented knowledge. | API documentation, architecture document, user manual, runbook, ADR, source-code comments, design specification. |
| **Documentation Technique** | A repeatable method for transforming technical knowledge into documented representations. | Code annotation, diagramming, reverse engineering, interviewing, technical writing, modeling, API extraction, documentation generation. |
| **Documentation Mechanism** | The operational means through which documentation is produced, transformed, stored, or synchronized. | Static site generator, Markdown parser, UML generator, Javadoc, Sphinx, Git repository, documentation pipeline. |
| **Documentation Tool** | Concrete instruments used by Technical Agents during documentation activities. | Confluence, GitHub Wiki, Docusaurus, Javadoc, PlantUML, Draw.io, Swagger/OpenAPI tools. |
| **Documentation Infrastructure** | The technical environment that supports creation, storage, distribution, and evolution of documentation. | Documentation repository, version control system, CI/CD documentation pipeline, knowledge base, search engine. |
| **Documentation Practice** | A repeatable organizational pattern governing how documentation is created and maintained. | Docs-as-code, Architecture Decision Records, API-first documentation, Living Documentation, Knowledge Management. |
| **Documentation Representation** | The form used to encode technical knowledge. | Text, diagrams, tables, schemas, examples, code snippets, executable documentation. |
| **Documentation Feedback** | Signals used to evaluate documentation effectiveness and improve it. | User questions, documentation issues, outdated sections, failed procedures, support tickets. |
| **Documentation Verification** | The process of evaluating whether documentation correctly represents the Technical Object or Process. | Technical review, peer review, link validation, executable examples, synchronization checks. |
| **Documentation Maintenance** | The set of activities required to keep documentation aligned with evolving technical reality. | Updating architecture diagrams after redesign, updating API specifications after changes, removing obsolete instructions. |
| **Documentation Model** | The conceptual representation used to organize documented knowledge. | Information architecture, taxonomy, ontology, document hierarchy, system viewpoint model. |
| **Documentation Standard** | Normative rules governing documentation structure, notation, quality, or interoperability. | ISO/IEC/IEEE documentation standards, OpenAPI specification, UML notation, Markdown conventions. |
| **Documentation Blueprint** | The structural template or model that defines how documentation artifacts are produced. | Documentation templates, UML conventions, Markdown structure, OpenAPI specification, ADR format, IEEE documentation standards. |

### Documentation Lifecycle

> The Documentation Lifecycle describes the stages through which knowledge artifacts are created, structured, validated, maintained, and eventually retired to ensure that technical knowledge remains accessible, accurate, and useful over time.
> 

| **Stage** | **Purpose** | **Key Activities** | **Output** |
| --- | --- | --- | --- |
| **Discovery** | Identify the need for documentation and capture undocumented knowledge | Detect knowledge gaps, collect requirements, identify stakeholders, capture existing information | Documentation need, raw knowledge inputs |
| **Specification** | Define what the documentation should represent and how it should be structured | Define purpose, audience, scope, standards, information model, documentation blueprint | Documentation specification |
| **Creation** | Transform knowledge into a persistent artifact | Write, structure, illustrate, organize, and encode information according to standards | Draft documentation artifact |
| **Validation** | Ensure correctness, completeness, and alignment with reality | Technical review, peer review, verification, consistency checks, usability evaluation | Validated documentation |
| **Publication** | Make documentation accessible and discoverable | Publish, index, assign ownership, manage permissions, register metadata | Published documentation |
| **Consumption** | Enable knowledge acquisition and practical use | Read, reference, learn, execute procedures, support decisions and operations | Knowledge transfer and operational use |
| **Maintenance** | Keep documentation accurate over time | Update content, incorporate feedback, track changes, fix inconsistencies | Updated documentation version |
| **Evolution** | Improve documentation quality and capability | Refactor structure, improve standards, integrate new knowledge, optimize retrieval | Improved documentation system |
| **Retirement** | Manage obsolete knowledge artifacts | Archive, deprecate, preserve historical context, remove invalid references | Archived or retired documentation |

### **Documentation Technical Object  (Deliverable)**

> 

## **Documentation Technical Requirement**

> Documentation technical requirements define the structural, semantic, operational, and quality constraints that documentation artifacts must satisfy to ensure they are understandable, maintainable, discoverable, verifiable, and reusable by humans and technical systems.
> 

| **Category** | **Requirement** | **Description** |
| --- | --- | --- |
| **Structure** | Defined organization | Documentation must follow a consistent structure, hierarchy, and information architecture. |
| **Completeness** | Required information coverage | Documentation must contain all information necessary for its intended purpose and audience. |
| **Accuracy** | Alignment with reality | Documentation must accurately represent the system, process, behavior, or knowledge domain it describes. |
| **Consistency** | Internal coherence | Terminology, concepts, notation, and representations must remain consistent across artifacts. |
| **Traceability** | Linkage to sources and decisions | Documentation should preserve relationships between requirements, designs, implementations, changes, and evidence. |
| **Versioning** | Evolution management | Documentation changes must be tracked to maintain historical context and accountability. |
| **Discoverability** | Knowledge retrieval | Documentation must be indexed and organized so users can efficiently locate relevant information. |
| **Accessibility** | Availability to intended users | Documentation must be accessible through appropriate channels and formats. |
| **Maintainability** | Ease of update | Documentation should minimize the cost of correction, extension, and adaptation. |
| **Usability** | Effective knowledge transfer | Documentation must support understanding, learning, and execution of intended tasks. |
| **Validation** | Quality assurance | Documentation must undergo review and verification against defined standards. |
| **Interoperability** | Machine and human readability | Documentation should use formats and conventions that support integration with tools and systems. |

## Methodology

> How to ground the documentation?
> 
- Documentation Model
- Documentation Standard
- Documentation Blueprint

### Documentation Practice

> A repeatable organizational pattern governing how documentation is created and maintained.
> 

| **Methodology** | **Core Idea** | **Description** | **Typical Use Cases** |
| --- | --- | --- | --- |
| **Top-Down Documentation** | Start from the big picture | Begin with purpose, concepts, architecture, and high-level models before adding details. | System documentation, architecture guides, technical overviews |
| **Bottom-Up Documentation** | Build from existing knowledge | Capture detailed components first and progressively compose higher-level views. | Legacy systems, code documentation, reverse engineering |
| **Progressive Documentation** | Document continuously as knowledge evolves | Documentation grows incrementally alongside the system or process. | Agile development, evolving products |
| **Documentation-as-Code** | Treat documentation as an engineered artifact | Store, version, review, test, and deploy documentation using software engineering practices. | APIs, software projects, infrastructure documentation |
| **Single Source of Truth (SSOT)** | Maintain authoritative knowledge sources | Centralize critical information to avoid duplication and inconsistency. | Enterprise documentation, configuration management |
| **Model-Based Documentation** | Use models as primary representations | Represent systems through diagrams, schemas, formal models, and structured views. | Architecture, engineering systems, complex domains |
| **Audience-Centered Documentation** | Optimize for user needs | Design documentation around user goals, tasks, and knowledge levels. | User guides, developer documentation, training materials |
| **Task-Oriented Documentation** | Organize around actions | Structure documentation around what users need to accomplish. | Procedures, operational manuals, tutorials |
| **Concept-Oriented Documentation** | Organize around understanding | Explain concepts, principles, and relationships before tasks. | Reference documentation, technical knowledge bases |
| **Information Mapping** | Structure information into reusable units | Break content into standardized information blocks with clear relationships. | Large documentation systems, regulated environments |
| **Knowledge Graph Documentation** | Represent knowledge as connected entities | Capture relationships between concepts, components, decisions, and artifacts. | Complex systems, AI-assisted knowledge management |
| **Living Documentation** | Documentation evolves with the system | Keep documentation continuously synchronized with implementation and reality. | Software engineering, business processes |
| **Layered Documentation** | Provide multiple levels of abstraction | Organize documentation from overview to detailed implementation. | Enterprise architecture, technical platforms |
| **Template-Based Documentation** | Standardize document construction | Use predefined structures to ensure consistency and completeness. | Organizations, compliance documentation |
| **Documentation-Driven Development** | Documentation guides implementation | Define requirements and behavior through documentation before or alongside development. | APIs, specifications, regulated software |
| Architecture Decision Records (ADR) |  |  |  |
| API-First Documentation |  |  |  |
| Living Documentation |  |  |  |
| Documentation Review |  |  |  |
| Documentation Templates |  |  |  |
| Documentation Automation |  |  |  |

### Documentation Model

> How is knowledge organized?
> 

> The conceptual organization and knowledge representation strategy for documentation.
> 

> A Documentation **M** refers to a **structured framework** or approach used to create, organize, and present documentation for various types of projects, systems, or processes.
> 

> **Documentation models** provide guidelines and standards for how information should be captured, formatted, and communicated to users, developers, or other stakeholders.
> 

| **Documentation Model** | **Description** |
| --- | --- |
| **Diátaxis** | Organizes documentation into four distinct types—Tutorials, How-To Guides, Reference, and Explanations—based on user intent and learning needs. |
| **Topic-Based Authoring** | Structures documentation as independent, reusable topics that can be assembled into multiple publications. |
| **Information Mapping** | Organizes information into standardized, modular information blocks to improve readability, consistency, and reuse. |
| **Documentation-as-Code** | Treats documentation as source code by applying version control, code review, automated testing, and continuous publishing practices. |
| **Single Source of Truth (SSOT)** | Maintains one authoritative source for each piece of information, minimizing duplication and inconsistency. |
| **Living Documentation** | Keeps documentation continuously synchronized with the system, codebase, or operational reality as it evolves. |
| **Model-Based Documentation** | Uses formal models (e.g., UML, SysML, ER diagrams) as primary documentation artifacts, with textual descriptions derived from or linked to them. |
| **Knowledge Graph Documentation** | Represents documentation as an interconnected graph of concepts, entities, and relationships to enhance navigation and discovery. |
| **Layered Documentation** | Organizes documentation into multiple levels of abstraction, progressing from high-level concepts to detailed implementation. |
| **Audience-Centered Documentation** | Structures documentation according to the needs, expertise, and goals of different audiences (e.g., users, developers, operators, administrators). |
| **Task-Oriented Documentation** | Organizes content around the tasks users need to accomplish rather than around system components or features. |
| **Concept-Oriented Documentation** | Prioritizes explaining principles, models, and relationships to build understanding before introducing procedures or references. |
| **Reference-Centered Documentation** | Focuses on providing complete, structured, and authoritative factual information for lookup and precise retrieval. |
| **Process-Oriented Documentation** | Organizes documentation around workflows, procedures, and business or operational processes. |
| **Architecture-Centric Documentation** | Centers documentation on the structure, components, interfaces, and design decisions of a system or architecture. |
| **Linear Documentation** | Traditional sequential documentation that presents information in linear order is often used for tutorials or user guides. |
| **Hierarchical Documentation** | Organizes information in a hierarchical structure, such as chapters, sections, and subsections, allowing navigation through different levels of detail. |
| **Reference Documentation** | It focuses on providing detailed information about specific components, functions, or features, which developers often use as API references. |
| **Tutorial-based Documentation** | Walks users through step-by-step examples to help them understand and use a product or software. |
| **FAQ (Frequently Asked Questions)** | Presents a list of common questions and their corresponding answers to address user inquiries. |
| **Cookbook Documentation** | Provides a collection of solutions to common problems or tasks, often accompanied by code snippets. |
| **Interactive Documentation** | It offers an interactive experience where users can experiment with code examples, alter parameters, and observe results. |
| **Case Study Documentation** | Explores real-world scenarios or use cases to demonstrate how a product or technology can solve specific problems. |
| **Whitepapers** | In-depth documents that explore a specific topic, often presenting research findings, analysis, or technical details. |
| **Release Notes** | Summarizes changes, updates, and improvements in a new software or product version. |
| **Architecture Documentation** | Describes a system or software's overall structure, components, and interactions. |
| **Quick Start Guides** | Condensed guides that provide essential information to get users started with a product or technology quickly. |
| **Glossaries** | Lists and defines terms, acronyms, and jargon in a specific domain or industry. |
| **Troubleshooting and Debugging Documentation** | Helps users identify and resolve common issues they might encounter while using a product or software. |
| **Policy and Compliance Documentation** | Outlines rules, regulations, or policies that users must adhere to when using a service or product. |
| **Safety and Security Documentation** | Informs users about safety procedures, security practices, and potential risks associated with a product. |
| **Training Manuals** | Comprehensive resources are used for training, often in educational or corporate settings. |
| **Use Case Examples** | Documents that present real-world scenarios to demonstrate how a product or solution can be applied effectively. |
| **Knowledge Bases** | Online repositories of information that accumulate articles, how-tos, troubleshooting guides, and other resources to support users. |
| **Technical Specifications** | Detailed documents that outline the technical aspects of a system, software, or hardware. They cover architecture, design, requirements, and implementation details. |
| **Guides** | Comprehensive documents that offer in-depth information about a specific topic, technology, or process. These can cover concepts, best practices, and advanced usage scenarios. |

- **Stub Documentation Pattern** – A minimal placeholder document that exists for **cognitive ease**, maintaining the structure while directing users to the actual content elsewhere.
- FAQ Pattern: **Purpose:** Collects commonly asked questions and answers in a structured format.
- Change Log Pattern: Tracks modifications over time with timestamps and descriptions.
- Decision Log (ADR - Architecture Decision Record) Pattern: Documents **why** a decision was made, including alternatives considered.
- Incident Report Pattern: Captures details of an issue, including **root cause, impact, and resolution.**
- Code Annotation Pattern: Uses inline comments and structured annotations to explain code.
- Tutorial/Walkthrough Pattern: Guides users through a process with **step-by-step** instructions.
- Cookbook/Recipe Pattern: Provides small, **reusable code snippets** for common use cases.
- Knowledge Base (KB) Pattern: collection of articles for self-service troubleshooting and learning.
- Glossary Pattern: Defines terms and concepts in a structured way.

### Documentation Standard

> What rules must documentation follow?
> 

| **Framework** | **Purpose** | **Usage** |
| --- | --- | --- |
| **ISO/IEC/IEEE 26514** | Defines requirements and recommendations for designing and developing user documentation | Software user documentation |
| **ISO/IEC/IEEE 26511** | Defines requirements for managing documentation development processes | Software documentation management |
| **ISO/IEC/IEEE 12207 Documentation Processes** | Defines documentation activities within software lifecycle processes | Software engineering lifecycle |
| **ISO/IEC/IEEE 15288** | Defines system lifecycle processes, including information management | Systems engineering |
| **ISO 9001 Documented Information Requirements** | Defines control, management, and retention of documented information | Quality management systems |
| **DITA (Darwin Information Typing Architecture)** | XML-based standard for modular, topic-based documentation | Technical documentation, product manuals |
| **DocBook** | Structured XML vocabulary for technical documentation | Books, manuals, software documentation |
| **Markdown Specification (CommonMark)** | Defines a standardized lightweight markup format | Developer documentation, repositories |
| **OpenAPI Specification (OAS)** | Defines machine-readable API documentation contracts | REST API documentation |
| **AsyncAPI Specification** | Defines documentation standards for event-driven APIs | Messaging systems, event architectures |
| **RFC Documentation Style (RFC 2119 / RFC 8174)** | Defines terminology for requirements and normative language | Internet standards, technical specifications |
| **C4 Model** | Defines a standardized approach for software architecture documentation | Software architecture |
| **Arc42** | Defines a template and structure for architecture documentation | Software architecture documentation |
| **ADRs (Architecture Decision Records)** | Defines a lightweight format for documenting architectural decisions | Software architecture governance |
| **Diátaxis Framework** | Defines a documentation organization model based on user needs | Developer documentation |
| **Docs-as-Code Practices** | Applies software engineering workflows to documentation | Engineering organizations |
| **MADR (Markdown Architectural Decision Records)** | Defines a structured ADR format using Markdown | Software projects |
| **BPMN Documentation Standards** | Defines notation for documenting business processes | Business process modeling |
| **UML Documentation Standards** | Defines standardized visual modeling notation | Software and system design |
| **SysML Documentation Standards** | Defines modeling notation for systems engineering | Complex engineered systems |

### Document Format

> How is the document encoded or represented?
> 

> The physical or logical representation of the document.
> 

> Markdown, HTML, PDF, DOCX, XML, DITA XML, AsciiDoc, reStructuredText
> 

### Software API Specification Format

| **Format** | **Description** |
| --- | --- |
| **OpenAPI Specification (OAS) / Swagger** | Machine-readable description of REST APIs, including endpoints, operations, parameters, schemas, authentication, and responses. |
| **RAML (RESTful API Modeling Language)** | YAML-based API modeling language used to define REST APIs, resources, methods, and data structures. |
| **WSDL (Web Services Description Language)** | XML-based formal description of SOAP web services, including operations, messages, bindings, and service endpoints. |
| **GraphQL SDL (Schema Definition Language)** | Schema language used to define GraphQL APIs, including types, queries, mutations, subscriptions, and relationships. |
| **AsyncAPI** | Specification format for documenting event-driven and asynchronous APIs, including messages, channels, and communication protocols. |
| **MSON (Markdown Syntax for Object Notation)** | Markdown-based format for describing data structures and API objects, commonly used in API Blueprint ecosystems. |
| **WADL (Web Application Description Language)** | XML-based format for describing REST web services, including resources, methods, and representations. |
| **ReDoc** | API documentation rendering framework that generates interactive documentation interfaces from OpenAPI specifications. |

### Documentation Type

> The structural representation and presentation style used to organize information within a documentation artifact.
> 

| Documentation Type | **Description** |
| --- | --- |
| **Reference Documentation** | Structured information designed for lookup and precise retrieval of facts, specifications, parameters, or definitions. |
| **Tutorial** | Step-by-step instructional material that teaches users a concept, technology, or workflow through guided examples. |
| **How-To Guide** | Task-oriented documentation focused on accomplishing a specific goal or solving a particular problem. |
| **Conceptual Documentation** | Explains concepts, principles, architecture, and relationships to build understanding. |
| **User Guide / User Manual** | Provides instructions and explanations for end users on installing, configuring, and using a system or product. |
| **Developer Documentation** | Technical information required by developers to build, integrate, extend, maintain, or contribute to a system. |
| **Technical Specification** | Formal description of requirements, interfaces, behaviors, constraints, and system properties. |
| **Architecture Document** | Describes system structure, components, interactions, architecture, and major design decisions. |
| **Design Document** | Describes proposed solutions, design rationale, implementation approaches, and trade-offs. |
| **API Documentation** | Defines API interfaces, endpoints, contracts, parameters, responses, examples, and usage patterns. |
| **API Reference** | Detailed reference for API operations, functions, classes, methods, parameters, return values, and examples. |
| **Code Documentation** | Source code comments and generated documentation explaining implementation details and intended behavior. |
| **Data Model & Schema Documentation** | Documents data models, schemas, entities, relationships, and database structures. |
| **Configuration Guide** | Explains how to configure software settings, options, parameters, and environments. |
| **Deployment Guide** | Documents procedures for deploying software across environments, infrastructure, containers, or cloud platforms. |
| **Migration Guide** | Guides users through upgrading or migrating between versions, platforms, or systems. |
| **Operational Runbook** | Procedures for operating, monitoring, troubleshooting, recovering, and maintaining production systems. |
| **Workflow & Process Documentation** | Documents operational workflows, development processes, review procedures, and organizational practices. |
| **Performance Optimization Guide** | Best practices for tuning, scaling, and improving system performance. |
| **Security Guide** | Documents security architecture, best practices, vulnerabilities, hardening, and operational security procedures. |
| **Decision Record (ADR)** | Captures architectural or technical decisions, context, alternatives considered, and consequences. |
| **Knowledge Base Article** | Reusable, searchable information for support, operations, or organizational knowledge sharing. |
| **FAQ (Frequently Asked Questions)** | Collection of common questions and concise answers for users or developers. |
| **Glossary** | Defines domain-specific terminology, abbreviations, and vocabulary. |
| **Checklist** | Structured list of verification steps, validation criteria, or required actions. |
| **Template** | Reusable document structure that standardizes documentation creation. |
| **Report** | Presents analyzed information, findings, metrics, observations, and conclusions. |
| **Whitepaper** | In-depth explanation of a technology, methodology, research topic, or proposed solution. |
| **Release Notes / Changelog** | Records changes, bug fixes, improvements, breaking changes, and new capabilities across releases. |
| **Contributor Guide** | Explains contribution processes, coding standards, submission workflows, and collaboration practices. |
| **User Stories & Use Cases** | Describes real-world scenarios, user goals, and interactions with the system. |
| **Accessibility Documentation** | Describes accessibility features, compliance considerations, and inclusive design guidance. |
| **License Documentation** | Explains licensing terms, usage rights, and legal obligations. |
| **Feedback & Support Guide** | Explains how users can report issues, request features, or obtain support. |
| **Incident Report** | Documents an operational incident or software defect, including symptoms, reproduction steps, impact, and evidence. |
| **Incident Analysis (Postmortem)** | Analyzes the causes, impact, resolution, lessons learned, and preventive actions following an incident. |

## Documentation Tool & Mechanism

> Static site generators (SSGs) generate static HTML, CSS, and JavaScript files from templates and content, often in Markdown or similar formats.
> 

| **Static Site Generator** | **Description** |
| --- | --- |
| **Jekyll** | A widely used SSG that’s easy to set up and is the default choice for GitHub Pages. |
| **Hugo** | Known for its speed, Hugo is written in Go and supports many themes and templates. |
| **Gatsby** | Built on React, Gatsby is highly customizable and suitable for building modern, data-driven websites. |
| **Next.js** | Commonly used for server-rendered React applications, Next.js can also generate static sites using the `getStaticProps` function. |
| **VuePress** | Designed for documentation, VuePress uses Vue.js and Markdown to create static sites with Vue components. |
| **Nuxt.js** | Similar to Next.js, but for Vue.js, Nuxt.js can be configured to generate static sites. |
| **Gridsome** | A Vue.js-based SSG optimized for creating fast and responsive websites. |
| **11ty (Eleventy)** | A flexible SSG that supports multiple template engines and data sources. |
| **Pelican** | A Python-based SSG is often used for blogs, supporting content written in reStructuredText or Markdown. |
| **Hexo** | A fast and simple SSG for blogs powered by Node.js and Markdown. |
| **Middleman** | A Ruby-based SSG that’s known for its extensibility and ease of use. |
| **Sphinx** | Designed for documentation, Sphinx is a Python-based SSG that can generate HTML, PDFs, and more. |
| **Metalsmith** | A pluggable JavaScript-based SSG is suitable for creating custom-built pipelines. |
| **Nanoc** | A Ruby-based SSG with a focus on flexibility and performance. |
| **Docusaurus** | Created by Facebook, Docusaurus is designed for documentation and provides out-of-the-box features for building technical documentation sites. |
| **MkDocs** | A Python-based SSG for creating documentation using Markdown. |
| **Zola** | A fast Rust-based SSG with theming and shortcode support. |
| **Wintersmith** | A flexible Node.js-based SSG with support for plugins and content sources. |
| **Sculpin** | A PHP-based SSG that converts Markdown and Twig templates into static HTML files. |
| **Bridgetown** | A Ruby-based SSG designed for building modern, performant websites with support for Ruby, JavaScript, and other languages. |
| **Mintlify** |  |

## Documentation Infrastructure

> 

## Documentation Technique

> Documentation techniques are systematic methods used to record, organize, and communicate information across various fields. Below is a structured overview of common documentation techniques categorized by type.
> 

### Type

| **Technique Type** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Manual Authoring** | Documentation written directly by humans using text editors or documentation tools. | Technical writing, Markdown authoring, Word documents |
| **Structured Authoring** | Documentation created from predefined content structures, schemas, or reusable components. | DITA, DocBook, XML-based authoring |
| **Template-Based Authoring** | Documentation produced from standardized templates to ensure consistency. | RFC template, ADR template, Design document template |
| **Docs-as-Code** | Documentation managed as source code using version control and software engineering workflows. | Markdown + Git, MkDocs, Sphinx, Hugo, Mintlify |
| **API-Driven Documentation** | Documentation generated from machine-readable API specifications. | OpenAPI/Swagger, AsyncAPI, GraphQL Schema documentation |
| **Code Annotation** | Documentation embedded directly within source code. | Javadoc, JavaDoc comments, Doxygen, XML Documentation, Rustdoc |
| **Automatic Generation** | Documentation generated directly from software artifacts or metadata. | Javadoc generation, UML generation, database schema documentation |
| **Reverse Documentation** | Documentation reconstructed from existing systems rather than written during development. | Reverse-engineered architecture diagrams, legacy system documentation |
| **Literate Programming** | Documentation and source code are written together as a single narrative artifact. | Knuth Web, Jupyter Notebook, Quarto |
| **Knowledge Capture** | Documentation created by extracting knowledge from experts or operational experience. | SME interviews, workshops, design reviews, postmortems |
| **Observation-Based Documentation** | Documentation produced by observing users, systems, or operational processes. | Process mapping, workflow observation, shadowing |
| **Collaborative Documentation** | Documentation authored and maintained collectively by multiple contributors. | Wiki editing, collaborative Markdown, Confluence |
| **AI-Assisted Authoring** | Documentation drafted, expanded, summarized, or translated using AI systems. | LLM-generated documentation, AI-assisted API descriptions |
| **Executable Documentation** | Documentation containing executable examples that are continuously validated. | Doctest, executable notebooks, tested code examples |
| **Living Documentation** | Documentation continuously synchronized with the evolving system through automation or CI/CD. | Architecture-as-Code, Living Documentation, Continuous Documentation |
| **Visual Documentation** | Documentation conveyed primarily through diagrams or graphical representations. | UML, BPMN, C4 Model, ER diagrams, flowcharts |
| **Decision Documentation** | Documentation focused on capturing engineering and architectural decisions. | ADRs (Architecture Decision Records), Decision Logs |
| **Traceability Documentation** | Documentation created by explicitly linking related engineering artifacts. | Requirements traceability matrices, requirement-to-test mappings |
| **Information Architecture** | Is the art and science of organizing and structuring information to facilitate effective navigation, understanding, and retrieval within a system or environment. |  |
|  |  |  |

### Space

> Which are the concrete techniques?
> 

| **Technique** | **Description** | **Usage** | **Tags** |
| --- | --- | --- | --- |
| Interview | Gather knowledge through structured or semi-structured conversations with subject matter experts. | Knowledge elicitation, requirements, procedures. | Elicitation, SME |
| Observation | Learn by directly watching people, systems, or processes. | Process documentation, workflow capture. | Field Study |
| Shadowing | Follow an expert while they perform work to document tacit knowledge. | SOPs, operational documentation. | Knowledge Capture |
| Think-Aloud Protocol | Ask users to verbalize their reasoning while performing tasks. | UX documentation, process discovery. | User Research |
| Workshop | Facilitate collaborative sessions to create or refine documentation. | Architecture, requirements, process mapping. | Collaboration |
| Brainstorming | Generate and organize documentation content collaboratively. | Early design, planning. | Ideation |
| Card Sorting | Organize information into logical groups. | Documentation information architecture. | IA, UX |
| Affinity Mapping | Cluster related ideas or notes into themes. | Knowledge organization. | Synthesis |
| Process Mapping | Create a visual representation of a workflow or business process. | SOPs, operations. | BPM, Workflow |
| Storyboarding | Describe a process or interaction as a sequence of events. | Tutorials, UX flows. | Narrative |
| Use Case Analysis | Document system behavior through actor interactions. | Functional specifications. | UML |
| User Story Mapping | Organize features around user journeys. | Agile documentation. | Agile |
| Task Analysis | Break a task into detailed steps and decisions. | Procedures, work instructions. | Workflow |
| Knowledge Distillation | Condense complex information into concise explanations. | Guides, onboarding. | Summarization |
| Example-Driven Explanation | Explain concepts primarily through worked examples. | API docs, tutorials. | Examples |
| Diagramming | Represent concepts visually using formal or informal diagrams. | Architecture, design. | UML, C4, BPMN |
| Screenshot Annotation | Explain software using annotated screenshots. | User manuals, training. | UI Documentation |
| Screen Recording | Capture workflows as video demonstrations. | Training, onboarding. | Multimedia |
| Code Commenting | Embed explanatory information directly in source code. | Developer documentation. | Source Code |
| API Introspection | Generate documentation from code or interface metadata. | API references. | OpenAPI |
| Reverse Engineering | Infer documentation from an existing implementation. | Legacy systems. | Recovery |
| Template Application | Produce documentation using standardized templates. | ADRs, RFCs, reports. | Standardization |
| Peer Review | Improve docu |  |  |

### Documentation Pattern

| **Pattern** | **Description** |
| --- | --- |
| Problem → Solution | Introduces a problem, then presents its solution and rationale. |
| Goal → Steps → Result | Organizes content around accomplishing a specific objective through sequential actions. |
| Overview → Details | Begins with a high-level summary before progressively exposing detail. |
| General → Specific | Explains broad concepts before discussing concrete instances or exceptions. |
| Concept → Example | Introduces an idea followed by one or more illustrative examples. |
| Example → Concept | Derives the general principle from concrete examples. |
| Question → Answer (FAQ) | Structures information as a collection of common questions and answers. |
| Step-by-Step Procedure | Presents an ordered sequence of actions to accomplish a task. |
| Decision Tree | Guides the reader through branching choices based on conditions. |
| Checklist | Organizes information as a list of items to verify or complete. |
| Recipe | Defines required inputs, ordered steps, and expected outputs. |
| Before → After | Demonstrates change by contrasting initial and final states. |
| Comparison Matrix | Compares multiple alternatives across common criteria. |
| Hierarchical Decomposition | Breaks a complex subject into progressively smaller components. |
| Layered Explanation | Presents information across increasing levels of abstraction or expertise. |
| Chronological Narrative | Organizes information according to temporal sequence. |
| Lifecycle | Structures content around the stages of an object's or process's lifecycle. |
| Cause → Effect | Explains relationships between causes and resulting outcomes. |
| Symptom → Diagnosis → Resolution | Documents troubleshooting and problem resolution workflows. |
| Input → Process → Output | Describes a system in terms of its inputs, transformations, and outputs. |
| State → Transition | Organizes information around states and the events that change them. |
| Context → Problem → Solution | Introduces context before describing the problem and proposed solution. |
| Rationale → Decision → Consequences | Captures the reasoning behind decisions and their implications (e.g., ADRs). |
| Reference Catalog | Presents information as a structured lookup organized by entries or topics. |
| Progressive Disclosure | Reveals complexity incrementally to avoid overwhelming the reader. |
| Hub-and-Spoke | Uses a central overview page linking to specialized documents. |
| Modular Composition | Builds documents from reusable, self-contained sections. |
| Tabular Reference | Organizes information into structured tables for rapid lookup. |
| Cross-Referenced Network | Connects related documents through hyperlinks and explicit references rather than a strict hierarchy. |
| Stub Documentation Pattern | A minimal placeholder document that exists for **cognitive ease**, maintaining the structure while directing users to the actual content elsewhere. |

### Tips

| **Tip** | **Description** |
| --- | --- |
| Know your audience | Write for the knowledge level, goals, and context of the intended readers. |
| Start with the purpose | Clearly state what the document is about and what the reader will achieve. |
| Be concise | Use the fewest words necessary without sacrificing clarity. |
| Prefer clarity over cleverness | Use simple, direct language and avoid ambiguity. |
| Organize logically | Structure information so readers can easily navigate and locate content. |
| Use consistent terminology | Use the same term for the same concept throughout the documentation. |
| Show examples | Reinforce concepts with practical examples, code snippets, or scenarios. |
| Use visuals when appropriate | Diagrams, tables, and screenshots often communicate more effectively than text alone. |
| Keep documentation current | Update documentation whenever the underlying system or process changes. |
| Make content discoverable | Use descriptive headings, navigation, indexing, and cross-references. |
| Write for scanning | Use headings, lists, tables, and short paragraphs to improve readability. |
| Validate instructions | Verify that procedures, commands, and examples work as written. |
| Record assumptions | Explicitly state prerequisites, constraints, and dependencies. |
| Review regularly | Periodically assess documentation for accuracy, relevance, and completeness. |

### Don’ts

| **Don't** | **Reason** |
| --- | --- |
| Don't duplicate information unnecessarily | Duplication creates inconsistent and difficult-to-maintain documentation. |
| Don't assume prior knowledge | Readers may lack the context that seems obvious to the author. |
| Don't let documentation become stale | Outdated documentation is often worse than having no documentation. |
| Don't mix unrelated topics | Keep each document focused on a single purpose or subject. |
| Don't use inconsistent terminology | Multiple names for the same concept confuse readers. |
| Don't write long, unstructured paragraphs | Dense text is difficult to scan and understand. |
| Don't omit prerequisites | Users need to know required conditions before following instructions. |
| Don't include unverified examples | Incorrect commands or code quickly erode trust. |
| Don't bury critical information | Place warnings, requirements, and important decisions where they are easily noticed. |
| Don't overload diagrams | Excessively detailed visuals become difficult to interpret. |
| Don't document implementation trivia | Focus on information that helps readers understand, use, or maintain the system. |
| Don't rely solely on screenshots | Screenshots become outdated quickly and are difficult to search. |
| Don't leave broken links or references | Invalid references reduce confidence and usability. |
| Don't use unexplained acronyms or jargon | Define specialized terminology before using it. |
| Don't treat documentation as an afterthought | Documentation should evolve alongside the product, process, or system. |

## Evaluation

> What make a document **`A`** better than **`B`**?
> 

| **Evaluation Method** | **Description** |
| --- | --- |
| **Documentation Verification** | Determines whether the documentation is technically correct, internally consistent, complete, current, and conforms to defined standards. |
| **Documentation Validation** | Determines whether the documentation enables its intended audience to successfully accomplish its intended purpose. |
| **Documentation Review** | Evaluates documentation through peer, expert, or stakeholder review to identify defects and opportunities for improvement. |
| **Usability Evaluation** | Assesses how easily users can find, understand, and apply the documented information. |
| **Readability Assessment** | Measures clarity, comprehensibility, and suitability for the target audience. |
| **Quality Assessment** | Evaluates documentation against predefined quality criteria such as accuracy, completeness, consistency, maintainability, and usability. |
| **Coverage Analysis** | Determines whether all required topics, features, processes, or requirements are documented. |
| **Consistency Checking** | Verifies consistent terminology, structure, formatting, and cross-references throughout the documentation. |
| **Link and Reference Validation** | Confirms that hyperlinks, references, citations, and external resources remain valid and accurate. |
| **Executable Verification** | Verifies that documented commands, code examples, and procedures execute successfully as documented. |
| **Compliance Assessment** | Evaluates whether documentation satisfies organizational, contractual, regulatory, or industry standards. |
| **Maintenance Assessment** | Evaluates whether documentation remains synchronized with the current system or process. |

## Documentation Feedback

> The systematic collection, analysis, and incorporation of input from documentation users and stakeholders to improve the accuracy, clarity, completeness, usability, and relevance of documentation over time.
> 

| **Feedback Mechanism** | **Description** |
| --- | --- |
| User Feedback | Collect comments, suggestions, and issues from documentation users. |
| Peer Review | Gather feedback from colleagues or fellow authors. |
| Subject Matter Expert (SME) Review | Validate technical accuracy with domain experts. |
| Editorial Review | Improve grammar, style, consistency, and readability. |
| Usability Testing | Observe users performing tasks to identify documentation deficiencies. |
| Analytics | Analyze search queries, page views, navigation paths, and abandonment to identify improvement opportunities. |
| Surveys | Collect structured user satisfaction and usefulness ratings. |
| Issue Tracking | Record documentation defects, enhancement requests, and missing content. |
| Community Contributions | Accept corrections and improvements from external contributors. |
| Continuous Feedback Loop | Regularly incorporate feedback into documentation revisions. |

## Documentation Maintenance

> The ongoing process of keeping documentation accurate, complete, consistent, relevant, and synchronized with the system, process, or knowledge it describes throughout its lifecycle.
> 

| **Maintenance Activity** | **Description** |
| --- | --- |
| Content Updates | Revise documentation to reflect changes in the documented subject. |
| Accuracy Verification | Periodically confirm that content remains technically correct. |
| Version Synchronization | Keep documentation aligned with software, products, or processes across releases. |
| Link Maintenance | Repair or remove broken hyperlinks and references. |
| Example Maintenance | Update code samples, screenshots, diagrams, and command examples. |
| Terminology Management | Maintain consistent vocabulary and definitions across documents. |
| Cross-Reference Maintenance | Update internal references after restructuring or renaming content. |
| Refactoring | Reorganize or simplify documentation without changing its meaning. |
| Archiving | Preserve obsolete documentation for historical or compliance purposes. |
| Deprecation | Clearly mark content that is outdated or scheduled for removal. |
| Content Consolidation | Merge duplicate or overlapping documentation to reduce redundancy. |
| Content Pruning | Remove obsolete, inaccurate, or low-value information. |
| Scheduled Review | Periodically review documentation according to a defined maintenance cadence. |
| Automation | Use tools to detect stale content, broken links, outdated examples, or documentation drift. |
| Change Tracking | Record revisions, authorship, and the rationale for documentation changes. |

Documentation: Conceptual Model

## QA

### How to think about documentation in the **`agents era`**?

> 

### **How can I generate an OpenAPI Specification (OAS) file at compile time for a Jakarta EE application, without enabling OpenAPI in production?**

> 

## References

- [jina.ai](https://docs.jina.ai/)
- [Twilio Docs](https://www.twilio.com/docs)
- [Skype Help](https://support.skype.com/en/skype/all/)
- [Docker Docs](https://docs.docker.com/)
- [Heroku Docs](https://devcenter.heroku.com/start)
- [Dropbox Docs](https://help.dropbox.com/)
- [Campaign Monitor](https://help.campaignmonitor.com/)
- https://diataxis.fr/
- https://github.com/scalar/scalar
- [Docusaurus](https://docusaurus.io/)
- https://docs.stripe.com/api
- [Literatura](https://app.notion.com/p/Literatura-258d610507c742ceaf2b544b2e99b4c1?pvs=21)
- [Philosophia Artium Technicarum et Operis](https://app.notion.com/p/Philosophia-Artium-Technicarum-et-Operis-355c0f5171ec808b82f8d7a85e8134cd?pvs=21)
- [12 Best Documentation Examples (Expert Picks)](https://herothemes.com/blog/best-documentation-examples/)
- https://www.youtube.com/watch?v=TmyWfATmRq0&list=WL&index=9&t=800s