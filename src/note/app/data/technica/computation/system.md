# System

> A **Computational System** is a set of $n$ software interrelated  components that work together to provide computational functionalities.
> 

> Note: A **Computational System** is not a **Computational Process**, but a structured arrangement of components, representations, control mechanisms, and interaction relations capable of generating, executing, constraining, transforming, or coordinating computational processes. A computational process is an occurring execution or evolution of computation; a computational system is the organized substrate, architecture, or operational framework within which such processes are specified, instantiated, and managed. **This is key** their design - because a great system is much much than great **computation - is also great and useful interaction between the system and the user.**
> 

> **Note:** A **computational system** addresses a given problem not through a fixed solution, but via an **evolving process that adapts** to find the most **effective implementation** or keeps pace with the **changing nature of the problem**.
> 

> **Note**: Like many other areas of engineering that design and implement complex systems, this process is typically carried out through a set of layered specifications and refinements, generating multiple system models that evolve from less detailed to more detailed versions.
> 

> **Analyze system performance**, security, user interaction, and overall efficiency through observation and data-driven evaluation.
> 

> **Software Engineering** is the discipline of **constructing large computational systems** through the composition and organization of smaller computational descriptions, with complexity management as its central concern.
> 

> Case Studies: See (Miscellanea and https://github.com/dbremont/documentorum).
> 

Doing:

- How should we think about execution? What are its properties, and what is its nature?
- How to think about execution durability?   https://news.ycombinator.com/item?id=46245238
- How to Reason About **Code Quality: Software Functionality and Feature Scattering**? [‣](https://app.notion.com/p/178598edb79080668cf3d129fa8a0792?pvs=21)
    - **Technical Concept** — What does the software expose as a technical concept (e.g., interface, implementation, abstraction) that enables intelligibility? How can this technical concept affect interaction design? How can the software be evaluated from a conceptual perspective?

## Computation System

> How to make an abstract decomposition of any software system?
> 

> **Note:** This **decomposition** does not claim to be minimal or orthogonal. It is a conceptual tool for understanding software system production. Some parts are cross-cutting — for example, *diagnosis* can occur at multiple stages of the lifecycle, including construction and sustainment phases.
> 

> **Note:** Ideation and **Technical Specification** can also be decomposed into multiple levels of abstraction. **Technical specification** may range from high-level architecture all the way down to detailed component design, data schemas, and protocol definitions.
> 

> System Analysis is an abstract notion that entails many perspectives on understanding, measuring, and improving a software system, including performance evaluation, behavioral modeling, fault diagnosis, usage assessment, and feedback for system evolution and decision-making.
> 

| **Part** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Ideation (Specification)** | Clarifying intent, defining purpose, scope, high-level requirements, constraints, success criteria. | Problem statement, user stories, use cases, business rules. |
| **Technical Design (Specification)** | Transforming intent into architecture, models, flows, schemas, and component definitions. | UX Spec, UI Spec, System architecture, API contracts, data models, interaction diagrams, component specs, ai oriented specification. |
| **Implementation** | Constructing the system’s artifacts: code, configuration, assets. | Frontend/backend code, infrastructure code, configuration files, design tokens. |
| **— Validation** | Ensuring correctness, consistency, safety, performance before release. | Testing (unit, integration, e2e), verification, static analysis, QA reviews. |
| **— Core System** | Essential computational logic and capabilities. | Algorithms, domain logic, state management, services. |
| **— Documentation** | Capturing knowledge about system design, usage, and operation. | User manuals, API documentation, design docs, architecture diagrams, onboarding guides. |
| **— Interaction Systems(s)** | Interfaces and behaviors between entities. | **System–System:** APIs, protocols, integrations.  
**System–User:** UI, interactions, accessibility, workflows. |
| Analysis |  |  |
| **Operation** | Running the system in real-world conditions; ensuring reliability and availability. | Deployment, runtime environment, networking, scheduling, resource management. |
| **Monitoring** | Observing system behavior, performance, failures, and signals. | Logs, metrics, tracing, dashboards, alerting systems. |
| **Diagnosis** | Identifying causes of failures, degradations, or incorrect behavior. | Incident analysis, debugging, root-cause analysis, audit tools. |
| **Sustainment (Evolution & Improvement)** | Extending, optimizing, refactoring, maintaining the system over time. | Feature updates, refactors, performance improvements, architecture migrations. |
| **Security** | Protecting the system and its data against threats, vulnerabilities, misuse, and unauthorized access throughout its lifecycle. | Threat modeling, authentication & authorization, encryption, secure coding practices, vulnerability scanning, penetration testing, incident response. |
| **Governance** | Ensuring compliance with organizational policies, legal regulations, standards, and ethical guidelines. | Compliance audits, policy enforcement, risk management, documentation, reporting, review boards. |

### **Validation**

> See for Functional Validation ([Verification](note.html?n=technica/computation/dependability/verification.md))
> 

| **Dimension** | **Description** |
| --- | --- |
| **Functional Validation** | Ensuring the system behaves as expected according to specifications and business rules. |
| **Performance Validation** | Verifying efficiency, scalability, and responsiveness under expected workloads. |
| **Security Validation** | Testing for vulnerabilities, misconfigurations, and potential threats. |
| **Usability & Interaction Validation** | Confirming the system is user-friendly, accessible, and intuitive. |
| **Compliance & Governance Validation** | Ensuring adherence to legal, regulatory, and organizational standards. |

## Production Phase(s)

> This checklist provides a comprehensive overview of essential aspects to consider when designing, evaluating, or maintaining a robust and efficient computational software system.
> 

> **Note:** Different subsystems may require adaptation. For example, the **user interface (UI)** demands a deep understanding of user behavior and needs.
> 

> **Software Analysis:** The systematic examination of a software system to understand its structure, behavior, performance, and correctness.
> 

![image.png](data/technica/computation/assets/system/image.png)

| **Part** | **Task** | **Description** |
| --- | --- | --- |
| **💡 Ideation (Specification)** | 🔍 Market Research | Collecting information about users, competitors, trends, and business opportunities to define product vision. |
|  | 📝 Problem Definition | Identifying the problem to solve, its scope, constraints, and expected outcomes. |
|  | 📋 Requirements Gathering | Capturing functional, non-functional, and domain-specific requirements from stakeholders. |
|  | 🧪 Concept Validation | Testing assumptions via prototypes, mockups, or surveys to reduce risk before design. |
| **🛠 Technical Specification  & Design** | 🎨 Product Design | High-level structuring of product functionality and interactions |
|  | ✅ Technical Feasibility Analysis | Assessing whether proposed designs can meet performance, security, and operational requirements. |
|  | 🏗 System Architecture | Defining high-level system components, their responsibilities, and interactions. |
|  | 🖌 UX/UI Design | Visual and experiential design for usability and user satisfaction |
|  |  |  |
|  | 🔗 API & Interface Design | Designing endpoints, data contracts, protocols, and integration specifications. |
|  | 💾 Data Modeling | Structuring data entities, relationships, and persistence mechanisms. |
|  | 🎯 Interaction Design | Designs flow, animations, and interface behavior |
|  | 🧩 Design Systems | Maintains reusable components and design standards |
| 🛠 Prototyping |  | Builds mockups or MVPs to test ideas before full development. |
| **💻 Implementation** | 👨‍💻 Coding | Writing application code for frontend, backend, services, and supporting libraries. |
|  | ⚙️ Configuration | Setting up environment variables, infrastructure definitions, deployment scripts, and CI/CD pipelines. |
|  | 🎨 Asset Creation | Producing design assets, media, templates, and other resources needed for the system. |
| **— 🔍 Validation** | 🧩 Unit & Integration Testing | Ensuring individual modules and their interactions function correctly. |
|  | 🌐 End-to-End Testing | Verifying the system as a whole meets requirements and user expectations. |
|  | 🛠 Static & Dynamic Analysis | Detecting bugs, security issues, and code quality problems using tools. |
| **— 🧠 Core System** | ⚡ Algorithm Implementation | Building domain-specific algorithms, business logic, and processing pipelines. |
|  | 🗄 State & Data Management | Implementing services, caches, databases, and state synchronization mechanisms. |
| **— 🔗 Interaction System** | 🔌 System-System Integration | Connecting components, APIs, and services for seamless communication. |
|  | 🖥 System-User Interaction | Designing UI/UX workflows, accessibility features, and interaction patterns. |
| **— 📚 Documentation** | 📖 Developer Guides | Writing code comments, architecture overviews, and usage instructions. |
|  | 📘 User Manuals | Providing end-user guides, tutorials, and FAQs. |
|  |  |  |
| **🚀 Operation** | 🚢 Deployment & Release | Installing, configuring, and launching the system in target environments. |
|  | 🕹 Runtime Management | Managing processes, resource allocation, job scheduling, and service orchestration. |
|  | 🎛 Feature Flagging & A/B Testing | Allows controlled experiments and staged releases |
|  | 📊 Analytics & Instrumentation | Tracks usage, performance, and engagement metrics |
| **📊 Monitoring** | 📈 Metrics Collection | Tracking system performance, usage, and operational KPIs. |
|  | 📝 Logging & Tracing | Capturing system events, errors, and execution traces for analysis. |
|  | 🚨 Alerts & Dashboards | Creating visualizations and notifications to detect abnormal conditions quickly. |
| **🔧 Diagnosis** | 🕵️ Incident Analysis | Investigating failures, errors, and anomalies in the system. |
|  | 🔎 Root-Cause Analysis | Identifying underlying causes of recurring issues or degradations. |
|  | 🛠 Debugging & Auditing | Examining code, configuration, or logs to pinpoint problems. |
| **♻️ Sustainment (Evolution & Improvement)** | ✨ Feature Updates | Adding new capabilities based on evolving requirements or market feedback. |
|  | 🔄 Refactoring | Improving internal structure, readability, and maintainability without changing behavior. |
|  | ⚡ Performance Optimization | Tuning system performance, scalability, and efficiency. |
|  | 🧹 Technical Debt Management | Reducing accumulated suboptimal designs, outdated libraries, or workarounds. |
| **📈 Post-Launch & Growth** | 📣 Product Marketing | Crafts positioning, messaging, and go-to-market strategy. |
|  | 🚀 Product-Led Growth (PLG) | Uses the product itself to drive acquisition and upselling. |
|  | 🤝 Customer Success & Support | Enhances retention, onboarding, and problem resolution. |
|  | 🔄 Lifecycle Management | Manages product updates, sunsetting, and long-term evolution. |
|  | 🗣 Feedback Loops | Integrates user insights and complaints back into development. |
| **🛡 Security** | 🛡 Threat Modeling & Risk Assessment | Identifying potential attack vectors and mitigating risks in design and operation. |
|  | 🔑 Access Control & Encryption | Implementing authentication, authorization, and secure data handling. |
|  | 🐞 Vulnerability Scanning & Penetration Testing | Detecting and fixing security gaps proactively. |
| **📜 Governance** | ⚖️ Compliance & Policy Enforcement | Ensuring legal, regulatory, and organizational requirements are met. |
|  | 🧾 Audit & Reporting | Documenting activities, incidents, and compliance evidence. |
|  | 👀 Review & Oversight | Periodically assessing systems, processes, and practices for improvements. |

## Implementation Work Process Model(s)

| **Workflow Name** | **Type** | **Typical Phases** | **Best For** |
| --- | --- | --- | --- |
| **Waterfall** | Linear | Requirements → Design → Implementation → Verification → Maintenance | Highly regulated industries, hardware, documentation-heavy environments |
| **V-Model (Verification & Validation)** | Linear with Testing Focus | Requirements → Design → Implementation → Unit Testing → Integration Testing → System Testing | Safety-critical systems (e.g. aerospace, medical) |
| **Agile (Scrum)** | Iterative/Incremental | Product Backlog → Sprint Planning → Sprint → Review → Retrospective | Software teams needing flexibility and fast iteration |
| **Agile (Kanban)** | Continuous Flow | To-Do → In Progress → Done | Teams needing visual work tracking and WIP limits |
| **Lean Product Workflow** | Iterative/Lean | Understand → Define → Sketch → Decide → Prototype → Validate | Fast MVPs, reducing waste in startups and small teams |
| **Design Thinking Workflow** | Empathic/Iterative | Empathize → Define → Ideate → Prototype → Test → Iterate | User-centered products, innovation-focused teams |
| **Double Diamond** | Divergent/Convergent | Discover → Define → Develop → Deliver | Creative and design-driven organizations |
| **Lean Startup Cycle** | Build-Measure-Learn | Idea → Build MVP → Measure Feedback → Learn → Iterate or Pivot | Startups validating business models and products |
| **Dual-Track Agile** | Parallel Discovery & Delivery | Continuous Discovery → Continuous Delivery | Mature teams balancing ongoing research with delivery |
| **Stage-Gate Workflow** | Phased with Gates | Discovery → Scope → Business Case → Development → Testing → Launch | Large orgs, hardware/complex products, budget control |
| **Jobs To Be Done (JTBD)** | Needs-Focused | Identify Jobs → Map Job Steps → Uncover Pains/Gains → Align Solutions | Products solving deep user problems |
| **SAFe Workflow** | Scaled Agile | Portfolio → Value Stream → Program (ART) → Team Iterations | Enterprises scaling Agile with governance |
| **Integrated Product Development (IPD)** | Concurrent Engineering | Cross-functional concept → Parallel design/dev → Validation | Engineering/manufacturing co-design |
| **Disciplined Agile Delivery (DAD)** | Hybrid Agile | Inception → Construction → Transition → Ongoing | Organizations requiring governance and flexibility |

## The Division of Labor

| Category | Subcategory | Role | Description |
| --- | --- | --- | --- |
| **Strategy** | Market Analysis | Market Research Analyst | Conducts competitive analysis and identifies market trends |
|  |  | Opportunity Scout | Discovers unmet needs and innovation whitespace |
|  | User Insights | UX Researcher | Studies user behaviors through interviews/surveys |
|  | Product Vision | Product Strategist | Defines long-term roadmap and business alignment |
|  |  | Chief Product Officer (CPO) | Sets company-wide product vision and P&L strategy |
| **Design** | Interaction Design | Interaction Designer (IxD) | Designs user flows and micro-interactions |
|  | Visual Design | UI Designer | Creates visual interfaces and design systems |
|  |  | Visual Designer | Focuses on branding and aesthetic consistency |
|  | Prototyping | Prototyping Specialist | Builds clickable prototypes (Figma/Framer) |
|  | Design Systems | Design Systems Engineer | Maintains component libraries and design tokens |
| **Engineering** | Frontend Development | Frontend Developer | Implements responsive UIs |
|  |  | UX Engineer | Bridges design-dev with coded prototypes |
|  | DevOps | DevOps Engineer | Manages CI/CD pipelines and cloud infrastructure |
|  | Testing | QA Engineer | Executes test cases and usability audits |
| **Operations** | Product Management | Product Manager | Prioritizes features and manages cross-functional teams |
|  | Agile Practices | Agile Coach | Facilitates Scrum/Kanban workflows |
|  | Releases | Release Manager | Coordinates version rollouts and hotfixes |
| **Growth** | Marketing | Product Marketer | Develops GTM strategies and positioning |
|  | Customer Experience | Customer Success Manager | Improves onboarding and retention |
|  | Data | Data Analyst | Tracks engagement metrics and A/B tests |
| **Governance** | Compliance | Ethical Design Advocate | Ensures ADA/WCAG compliance and ethical AI practices |
|  | Technical Excellence | Technical Product Manager | Manages technical debt and architecture decisions |
| **Leadership** | Product Leadership | Head of Product | Oversees product portfolio strategy |
|  | Design Leadership | UX Director | Leads design team and establishes UX standards |
|  |  | DesignOps Manager | Optimizes design workflows and tooling |
| **Specialized** | Emerging Tech | AR/VR Designer | Designs immersive 3D/spatial interfaces |
|  |  | Conversational UX Designer | Creates voice/chatbot interaction patterns |
|  | Safety-Critical Design | Human Factors Engineer | Optimizes UX for medical/aviation systems |

## Component

> A **component** is a modular, deployable unit of software that provides specific functionality and can interact with other components through well-defined interfaces. Components may be standalone or part of a larger system and can serve various roles depending on their purpose.
> 

### Dimension

| **Dimension** | **Value** | **Description** |
| --- | --- | --- |
| **Form** | Standalone Computational Service | A self-contained service performing a specific computation or function, deployable independently. |
|  | Computational Library | A collection of reusable functions, classes, or APIs that can be integrated into other components or systems. |
|  | Framework | Offers a reusable structure or scaffolding for building other components or applications. |
| Function | Integration | Connects, adapts, or orchestrates interactions between multiple components or external systems. |
|  |  |  |

### Component Space

> A **Component Space** represents the universe of software components in a system, categorized by their purpose, form, and function. It helps in understanding how components contribute to system construction, integration, and operation.
> 

> See more in  https://www.bremontix.xyz/lab/pro/Production/Industry/Software/Production/Component/
> 

## Software Analysis

### **Why?**

> **Why?**
> 

| **Goal** | **Description** |
| --- | --- |
| **Performance Optimization** | Identifies areas for improvement to ensure the system runs more efficiently, leading to faster execution and lower resource consumption. |
| **Issue Detection** | Helps to identify and diagnose performance bottlenecks, bugs, and inefficiencies within the system that affect its stability and functionality. |
| **Resource Allocation** | Provides insights into resource usage (CPU, memory, disk, etc.), enabling better distribution of resources for optimal performance. |
| **Capacity Planning** | Assists in understanding system load and performance trends to forecast future resource needs and plan for growth. |
| **Security** | Detects performance issues that may indicate security vulnerabilities, such as abnormal resource consumption due to attacks or breaches. |
| **User Experience** | Ensures that the system provides fast, responsive interactions for users, optimizing performance for improved satisfaction. |
| **Data-Driven Decisions** | Collects actionable data that informs decision-making, helping teams prioritize performance improvements based on real insights. |
| **Cost Control** | Identifies inefficient areas where system resources are being overused, helping to reduce operational costs by optimizing performance. |
| **Business Continuity** | Ensures that the system performs consistently and reliably, reducing the risk of downtime or failures that could disrupt business operations. |
| **System Optimization** | Focuses on maximizing overall system efficiency through continuous monitoring, improvements, and fine-tuning of components. |
| **Performance Tuning** | Involves adjusting system parameters and configurations to improve performance, such as tuning database queries or optimizing algorithms. |
| **Predictive Analysis** | Uses historical data to predict future performance trends, helping to anticipate problems before they occur and ensure continued system stability. |
| **Meet’s SLA’s** | Ensures that the system meets the defined Service Level Agreements (SLA) by adhering to specified performance metrics, such as uptime and response time. |

### Space

> Which type of **analysis exists**?
> 

> **HCI Analytics** applies computational, statistical, and machine learning techniques to model, measure, and optimize human-computer interactions by analyzing user behavior, cognitive load, interaction patterns, and system responsiveness through multimodal data sources such as eye tracking, keystroke dynamics, and physiological signals.
> 

| **Category** | **Subcategory** | **Purpose** | **Methods** | **Use Case(s)** |
| --- | --- | --- | --- | --- |
| **Static Analysis** | Code Quality | Detect style violations, maintainability issues | ESLint, SonarQube, Pylint | Enforcing coding standards |
|  | Security Vulnerabilities | Identify flaws (e.g., SQLi, XSS) before runtime | Snyk, Fortify, Checkmarx | Auditing open-source dependencies |
|  | Type Checking | Verify type safety at compile time | TypeScript, MyPy (Python), Flow (JS) | Preventing runtime type errors |
| **Dynamic Analysis** | Runtime Profiling | Measure CPU, memory, I/O usage | XHProf (PHP), VisualVM (Java), perf (Linux) | Optimizing bottlenecked algorithms |
|  | Fuzz Testing | Discover crashes via random inputs | AFL, libFuzzer, OSS-Fuzz | Testing parsers/network protocols |
|  | Taint Analysis | Track untrusted data flow | PHPStan (taint mode), CodeQL | Preventing injection attacks |
| **Formal Verification** | Model Checking | Prove system correctness against formal specs | TLA+, Spin, UPPAAL | Verifying distributed algorithms |
|  | Theorem Proving | Mathematically verify code logic | Coq, Isabelle, Lean | Blockchain smart contracts |
| **Performance Analysis** | Benchmarking | Compare speed/resource usage under load | JMeter, k6, Apache Benchmark | Evaluating database queries |
|  | Tracing | Track request flow across microservices | OpenTelemetry, Jaeger, Zipkin | Diagnosing latency in distributed systems |
| **Behavioral Analysis** | Model-Based Testing | Validate against expected state machines | SpecExplorer, GraphWalker | Testing IoT device workflows |
|  | Concurrency Analysis | Detect race conditions/deadlocks | ThreadSanitizer (TSan), Go’s race detector | Debugging multi-threaded apps |
| **Dependency Analysis** | License Compliance | Audit third-party licenses (e.g., GPL, MIT) | FOSSA, Black Duck, SPDX | Legal risk mitigation |
|  | Impact Analysis | Assess changes’ effects on dependent modules | Dependency-cruiser, CodeScene | Planning refactoring |
| **AI/ML-Assisted** | Anomaly Detection | Identify unusual patterns (e.g., memory leaks) | Prometheus + ML4logs, Amazon DevOps Guru | Monitoring cloud infrastructure |
|  | Code Generation | Auto-generate/test code via LLMs | GitHub Copilot, Codex, ChatGPT | Boilerplate reduction |
| **HCI Analytics** | … | … | … | … |

[Design](note.html?n=technica/computation/system/design.md)

[Interface](note.html?n=technica/computation/system/interface.md)

[**Evaluation**](note.html?n=technica/computation/system/evaluation.md)

[Operation](note.html?n=technica/computation/system/operation.md)

Miscellanea

[Programming](note.html?n=technica/computation/system/programming.md)

[Documentation](note.html?n=technica/computation/system/documentation.md)

## References

- https://github.com/dbremont/documentorum/tree/main/op
- https://www.bremontix.xyz/lab/pro/Production/Industry/Software/
- https://www.bremontix.xyz/lab/pro/Catalog/Good/Software/
- [ ]  [A Guide to a Production Observability System](https://app.notion.com/p/A-Guide-to-a-Production-Observability-System-1bdc0f5171ec80c8866bd644daed19ce?pvs=21)
- [ ]  [A General Guide to System Performance Analysis](https://app.notion.com/p/A-General-Guide-to-System-Performance-Analysis-1c2c0f5171ec80238202dd58928585b4?pvs=21)
- [ ]  [**A Guide to Improving Computational Systems in a Principled Way**](https://app.notion.com/p/A-Guide-to-Improving-Computational-Systems-in-a-Principled-Way-1bec0f5171ec808fb56ffd094de27a12?pvs=21)
- [ ]  [A Guide to Standards Computational System Performace Analysis Benchmarks](https://app.notion.com/p/A-Guide-to-Standards-Computational-System-Performace-Analysis-Benchmarks-1bec0f5171ec800ebe36f51d0bdae9fb?pvs=21)
- [Measuring an Engineering Organization](https://lethain.com/measuring-engineering-organizations/)
- [3 Pillars of Observability](https://medium.com/hepsiburadatech/3-pillars-of-observability-d458c765dd26)
- [The Modern Observability Problem](https://failingfast.io/opentelemetry-observability/)
- [haskell-code-s](https://github.com/grin-compiler/haskell-code-spot)**Domain Profiled Data**:
 Profiling tools collect information about the execution of software 
programs, including function execution times, memory usage, and call 
stacks.[pot](https://github.com/grin-compiler/haskell-code-spot)
- [Monitoring is a Pain](https://matduggan.com/were-all-doing-metrics-wrong/)
- [Latency Numbers Every Programmer Should Know](https://colin-scott.github.io/personal_website/research/interactive_latency.html)
- [Metrology](https://www.wikiwand.com/en/Metrology)
- Leiserson, C., Shun, J. (n.d.). [Performance Engineering of Software Systems](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/).
- Gregg, B. (2013). Systems performance. Prentice Hall.
- Jain, R. (1991). The art of computer systems performance analysis. John Wiley Sons.
- **Papers**:
    - Pourmajidi, W., Zhang, L., Steinbacher, J., Erwin, T., & Miranskyy, A. (2023). A Reference Architecture for Observability and Compliance of Cloud Native Applications.
    - Li, B., Peng, X., Xiang, Q., Wang, H., Xie, T., Sun, J., & Liu, X. (2022). Enjoy your observability: an industrial survey of microservice tracing and analysis. 27, 1–28.
    - Scrocca, M., Tommasini, R., Margara, A., Valle, E. della, & Sakr, S. (2020). The Kaiju project: enabling event-driven observability. 85–96.
    - Liu, Y. Y., Slotine, J. J., & Barab́asi, A. L. (2013). Observability of complex systems. 110(7), 2460–2465.
    - Burgess, M. (2019). From Observability to Significance in Distributed Information Systems.
    - Hollingsworth, J. K., Miller, B. P., & Cargille, J. (1994). Dynamic program instrumentation for scalable performance tools. 841–850.
    - Bruegge, B., Gottschalk, T., & Luo, B. (1993). A framework for dynamic program analyzers. 65–82.
- Practice
    - https://github.com/csiglab/performace-labs
    - https://github.com/csiglab/networking-labs
    - https://github.com/dbremont/linux-api-labs
    - https://github.com/csiglab/cs-analyst-labs
- [Principled Performance Analytics](https://www.usenix.org/conference/srecon22americas/presentation/desai)
- [A Guide to Monitor Linux Server using Prometheus and Grafana](https://geekflare.com/prometheus-grafana-setup-for-linux/)
- [Observability](https://en.wikipedia.org/wiki/Observability_(software))
- [Monitoring with Telegraf, InfluxDB and Grafana](https://stanislas.blog/2018/04/monitoring-telegraf-influxdb-grafana/)
- [Don’t Blindly Trust Your Java Profiler! · Stefan-Marr.de](https://stefan-marr.de/2023/09/dont-blindly-trust-your-profiler/)
- Andriesse, D. (2018). Practical Binary Analysis.
- Niedermaier, S., Koetter, F., Freymann, A., & Wagner, S. (2019). On Observability and Monitoring of Distributed Systems: An Industry Interview Study.
- Ding, B., Kulkarni, J., & Yekhanin, S. (2017). Collecting telemetry data privately. 30.
- [Governor](https://en.wikipedia.org/wiki/Governor_(device))
- [All my favorite tracing tools: eBPF, QEMU, Perfetto, new ones I built and more](https://app.notion.com/p/d5ae68609e634ebda0df4c3007e7b272?pvs=21)
- [How a Single Line of Code Made a 24-core Server Slower Than a Laptop](https://pkolaczk.github.io/server-slower-than-a-laptop/)
- [CPU Utilization is Wrong](https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html)
- [What scientists must know about Hardware to write fast code (2020) (viralinstruction.com)](https://news.ycombinator.com/item?id=37747822)
- Performance-Aware Programming Series
[https://www.computerenhance.com/p/table-of-contents](https://www.computerenhance.com/p/table-of-contents)
- Visualization of Programming Language Efficiency
[https://www.reddit.com/r/ProgrammingLanguages/comments/1e16s99/visualization_of_programming_language_efficiency/](https://www.reddit.com/r/ProgrammingLanguages/comments/1e16s99/visualization_of_programming_language_efficiency/)
- Dumais, Susan, et al. “Understanding user behavior through log data and analysis.” Ways of Knowing in HCI (2014): 349-372.
- [Fast and flexible observability with canonical log lines](https://stripe.com/blog/canonical-log-lines)
- [Message Templates](https://messagetemplates.org/)
- [Schema evolution in Avro, Protocol Buffers and Thrift](https://martin.kleppmann.com/2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html)
- [Production Twitter on One Machine? 100Gbps NICs and NVMe are fast - Tristan Hume](https://thume.ca/2023/01/02/one-machine-twitter/)
- Hardware Benchmarks
[https://versus.com/en/nvidia-geforce-rtx-3090-vs-nvidia-geforce-rtx-4070-ti](https://versus.com/en/nvidia-geforce-rtx-3090-vs-nvidia-geforce-rtx-4070-ti)
- [Compute Cost Calculator](https://compute-cost.com/)
- [s-tui](https://github.com/amanusk/s-tui)
- [btop](https://github.com/aristocratos/btop)
- [stacer](https://oguzhaninan.github.io/Stacer-Web/)
- https://linux.die.net/man/8/blktrace [blktrace - generate traces of the i/o traffic on block devices]
- https://linux.die.net/man/1/iotop
- https://github.com/retis-org/retis [Tracing packets in the Linux networking stack & friends]
- [*Linux Performance](https://news.ycombinator.com/item?id=13498485)[(http://www.brendangregg.com/linuxperf.html)](http://www.brendangregg.com/linuxperf.html)*
- [*Linux Performance Analysis](https://news.ycombinator.com/item?id=10654681)[(http://techblog.netflix.com/2015/11/linux-performance-analysis-in-60s.html)](http://techblog.netflix.com/2015/11/linux-performance-analysis-in-60s.html)*
- [How newlines affect *Linux* kernel *performance*](https://news.ycombinator.com/item?id=18169584)[(https://nadav.amit.zone/blog/*linux*-inline)](https://nadav.amit.zone/blog/linux-inline)
- [BPF *Performance* Tools: *Linux* System and Application Observability](https://news.ycombinator.com/item?id=20442200)[(http://www.brendangregg.com/blog/2019-07-15/bpf-*performance*-tools-book.html)](http://www.brendangregg.com/blog/2019-07-15/bpf-performance-tools-book.html)
- [*Linux* kernel *performance*: Flame Graphs](https://news.ycombinator.com/item?id=3717606)[(http://dtrace.org/blogs/brendan/2012/03/17/*linux*-kernel-*performance*-flame-graphs/)](http://dtrace.org/blogs/brendan/2012/03/17/linux-kernel-performance-flame-graphs/)
- [What *Linux* can learn from Solaris *performance* and vice-versa](https://news.ycombinator.com/item?id=7291877)[(http://www.slideshare.net/brendangregg/what-*linux*-can-learn-from-solaris-*performance*-and-viceversa)](http://www.slideshare.net/brendangregg/what-linux-can-learn-from-solaris-performance-and-viceversa)
- [Netdata – *Linux* *performance* monitoring, done right](https://news.ycombinator.com/item?id=11388196)[(https://github.com/firehol/netdata)](https://github.com/firehol/netdata)
- [Bypassing the *Linux* kernel for high-*performance* packet filtering](https://news.ycombinator.com/item?id=10181042)[(https://blog.cloudflare.com/kernel-bypass/)](https://blog.cloudflare.com/kernel-bypass/)
- [*Linux* network *performance* parameters](https://news.ycombinator.com/item?id=37403799)[(https://github.com/leandromoreira/*linux*-network-*performance*-parameters)](https://github.com/leandromoreira/linux-network-performance-parameters)
    - [ASP.NET Core metrics](https://learn.microsoft.com/en-us/aspnet/core/log-mon/metrics/metrics?view=aspnetcore-8.0)
- [.NET Performance Profiler](https://www.jetbrains.com/profiler)
- [Status Page](https://www.atlassian.com/software/statuspage?r=prd-sds)
- [15 awesome Grafana dashboards and examples](https://www.airplane.dev/blog/grafana-dashboards-and-examples)
- [Top 10 DevOps Dashboard Templates with Samples and Examples](https://www.slideteam.net/blog/top-10-devops-dashboard-templates-with-samples-and-examples)
- [Top 10 Monitoring Dashboard Templates with Samples and Examples](https://www.slideteam.net/blog/top-10-monitoring-dashboard-templates-with-samples-and-examples)
- https://raymii.org/s/software/Logging_all_Cpp_destructors_poor_mans_run-time_tracing.html
- https://github.com/wolfpld/tracy
- https://news.ycombinator.com/item?id=41650905
- https://en.wikipedia.org/wiki/Software_performance_testing
- https://en.wikipedia.org/wiki/Benchmark_(computing)
- https://en.wikipedia.org/wiki/Web_server_benchmarking
- https://en.wikipedia.org/wiki/Metrology
- [https://tu-dresden.de/zih/ressourcen/dateien/lehre/ws0910/lars/vorlesung_02_requirements-metrics-techniques.pdf?lang=en](https://tu-dresden.de/zih/ressourcen/dateien/lehre/ws0910/lars/vorlesung_02_requirements-metrics-techniques.pdf?lang=en)
- [ ]  [‣](https://app.notion.com/p/1be598edb79080a48d24f6af0b839018?pvs=21)
- [ ]  [‣](https://app.notion.com/p/1be598edb790802687b9d1c4b8bff0a1?pvs=21)
- [ ]  Mytkowicz, Todd, et al. "Evaluating the accuracy of Java profilers." ACM Sigplan Notices 45.6 (2010): 187-197.
- [ ]  Burchell, Humphrey, et al. "Don’t Trust Your Profiler: An Empirical Study on the Precision and Accuracy of Java Profilers." Proceedings of the 20th ACM SIGPLAN International Conference on Managed Programming Languages and Runtimes. 2023.
- [Time](note.html?n=technica/computation/miscelanea/time.md)
- https://www.youtube.com/watch?v=sX2nF1fW7kI
- https://www.youtube.com/watch?v=kPh8pod0-gk
- https://benchmark.clickhouse.com/
- https://skills.sh/
- https://www.seangoedecke.com/how-i-estimate-work/
- https://uphack.io/blog/post/the-illusion-of-building/
- https://github.com/rrweb-io/rrweb