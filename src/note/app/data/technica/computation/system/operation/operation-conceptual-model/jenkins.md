---
tags: [tool]
---

# Jenkins


> A tools that when trigger (which are the triggering models??)  executed a workflow (which are the workflow models ??? which is the workflow space???)
> 

> Jenkins is a tool that automates the execution of workflows when triggered by various methods, including manual execution, webhooks, SCM polling, scheduled jobs, REST API calls, and external orchestrators. It supports multiple workflow types, such as Freestyle Jobs, Declarative Pipelines, Scripted Pipelines, Job DSL, and Shared Libraries, operating within a workflow space that encompasses build automation, testing, deployment, and infrastructure-as-code tasks across distributed nodes.
> 

> Jenkins is an event-driven, distributed automation server that orchestrates and executes CI/CD workflows, defined as jobs or pipelines, across a dynamically allocated set of compute nodes. It provides a plugin-extensible execution model, enabling integrations with SCMs, artifact repositories, cloud environments, and external services, while supporting declarative and imperative pipeline definitions for software delivery and infrastructure automation.
> 

> Jenkins is a popular open-source automation server that facilitates continuous integration and continuous delivery (**CI/CD**) by enabling developers to build, test, and deploy software efficiently.
> 

> Pipeline: A job type that defines the entire **build process** as code using a Jenkinsfile.
> 

> User Management: Role-Based Access Control  - Manages user permissions based on roles assigned to them.
> 

> Plugins: …
> 

> Integration Tools: …
> 

> Alert Mechanisms: …
> 

> Triggers:  - **Asynchronous Computation**.
> 

> Jenkins Syncrhonoyus Operation Model (Click) (Agent Driven) vs Aysncrhouc Operatio Model  (Trigger)
> 

> **Synchronous** execution waits for each job to finish before moving to the next.
> 

> **Asynchronous** execution runs jobs concurrently or in the background without blocking.
> 

> Automation First: **Core Idea**: Any repetitive manual task in software development should be automated.
> 

> Event-Driven Execution: **Core Idea**: Jenkins reacts to external events rather than requiring manual intervention.
> 

> Orchestration of Complex Pipelines: **Core Idea**: Jenkins provides a way to define, coordinate, and manage multi-stage workflows.
> 

> Extensibility via Plugins: **Core Idea**: Jenkins is designed to be modular and extendable through plugins.
> 

> Distributed and Parallel Execution: **Core Idea**: Build and test workloads should be distributed across multiple nodes for speed and efficiency.
> 

> Configuration as Code: **Core Idea**: The CI/CD pipeline should be defined declaratively in code.
> 

> Integration with DevOps Ecosystem: **Core Idea**: Jenkins acts as a central automation hub for DevOps workflows.
> 

> Security and Access Control: Core Idea: CI/CD pipelines must be secure, especially in enterprise environments.
> 

> Workflows: …
> 

> Agent: …
> 

QA:

- How Jenkins Execute SQL Queries?
- What the computational essence of Jenkins?
- What are the Jenkins implementation details?
- Which is the Jenkins Computational Space?
- What   is the Jenkins Architecture?
- Which is the user-lang abstractions  and  concept space?
- Which is the implementation concept space?
- Which is the relation between jobs vs jenkin files?
    - A **Jenkins Job** is a single-unit task that runs a predefined set of steps, typically configured via the Jenkins UI. It is often imperative, meaning the execution logic is defined step by step manually.
    - A **Pipeline** is a **scripted, version-controlled CI/CD workflow**, written in a **Jenkinsfile** (using Groovy). It provides a **declarative or scripted approach** for defining complex workflows, supporting parallel execution, error handling, and dynamic agent allocation.
- What  it a workflow in Jenkins?

## **Jenkins Model of Operation**

> The **Jenkins Model of Operation** outlines the various methods and processes through which Jenkins triggers and executes pipelines, focusing on the distinction between manual and non-manual operations.
> 

> This model provides a structured framework for understanding how Jenkins facilitates continuous integration and continuous deployment (CI/CD) workflows.
> 
- Manual
- Non-Manual
    - Webhook Trigger
    - Scheduled
    - Poll SCM
    - Jenkins REST API
    - GitHub Actions

## Jenkins Workflow Models

> Aka. Jenkins Tasks Models.
> 

> **Jenkins Workflow** is an automated process that orchestrates the execution of CI/CD tasks, defined through jobs or pipelines, enabling seamless software build, test, and deployment across distributed nodes.
> 

| **Workflow Model** | **Description** | **Best For** | **Configuration Method** | **Complexity** | **Version Control?** |
| --- | --- | --- | --- | --- | --- |
| **Freestyle Jobs** | UI-based jobs configured with basic steps (build, test, deploy). | Simple, manual workflows. | Jenkins Web UI. | 🔹 Low | ❌ No |
| **Declarative Pipelines** | Structured, YAML-like pipeline defined in a `Jenkinsfile`. | CI/CD workflows with well-defined stages. | `Jenkinsfile` (Declarative syntax). | 🔸 Medium | ✅ Yes |
| **Scripted Pipelines** | Full Groovy scripting for dynamic pipeline execution. | Advanced, highly customized workflows. | `Jenkinsfile` (Scripted syntax). | 🔺 High | ✅ Yes |
| **Job DSL** | Groovy-based infrastructure-as-code for defining jobs. | Automating Freestyle Job creation. | Job DSL script stored in Git. | 🔸 Medium | ✅ Yes |
| **Shared Libraries** | Modular, reusable pipeline logic stored externally. | Large projects with repeated logic. | Groovy-based shared libraries. | 🔺 High | ✅ Yes |
| **REST API Triggered Workflows** | Jenkins jobs triggered externally via API. | Integrating Jenkins with external tools. | REST API (`curl` or scripts). | 🔹 Low | ❌ No |
| **SCM Polling/Webhooks** | Auto-trigger builds on SCM changes (GitHub, GitLab). | Continuous Integration workflows. | Webhook integration or SCM polling. | 🔸 Medium | ✅ Yes |
| **Scheduled Jobs (Cron)** | Runs jobs at predefined intervals. | Periodic maintenance or batch jobs. | UI-based or `triggers { cron('H */4 * * *') }` in pipeline. | 🔹 Low | ❌ No |
| **GitHub Actions / External Orchestration** | GitHub Actions triggering Jenkins workflows. | Hybrid CI/CD between Jenkins & GitHub. | GitHub Actions YAML + API calls. | 🔸 Medium | ✅ Yes |
| **Terraform + Jenkins (IaC)** | Automates Jenkins job creation with Terraform. | Infrastructure-as-Code workflows. | Terraform HCL + Jenkins Provider. | 🔺 High | ✅ Yes |

## Jenkins Abstractions

> Jenkins provides a **layered abstraction model** that allows users to interact with it at different levels of complexity. These **user-language abstractions** and their corresponding **concept spaces** define how users conceptualize and operate Jenkins at various stages of CI/CD automation.
> 

### User-Lang Abstractions

| **Abstraction** | **Conceptual Meaning** | **Examples** |
| --- | --- | --- |
| **Pipeline** | Automated sequence of tasks in CI/CD | "Build → Test → Deploy" |
| **Job** | A single executable unit in Jenkins | "Run Unit Tests" |
| **Build** | A specific execution instance of a job | "Build #42 failed" |
| **Stage** | A phase in a pipeline execution | "Compile → Test → Deploy" |
| **Artifact** | A generated output of a build process | ".jar, .war, Docker image" |
| **Node** | A machine that runs Jenkins jobs | "Agent on AWS EC2" |
| **Trigger** | An event that starts pipeline execution | "Git commit pushed" |
| **Notification** | A message sent about job status | "Slack alert on build failure" |

### Mid-Level User Abstractions (Pipeline & Job Execution)

| **Abstraction** | **Conceptual Meaning** | **Examples** |
| --- | --- | --- |
| **Jenkinsfile** | A script that defines a pipeline | "Declarative Groovy script" |
| **Declarative Pipeline** | A structured pipeline definition | `pipeline { agent any stages {...} }` |
| **Scripted Pipeline** | A Groovy-based dynamic pipeline | `node { stage('Build') {...} }` |
| **SCM (Source Control Management)** | Version control system integration | "Git, SVN, Mercurial" |
| **Webhook** | External trigger for Jenkins jobs | "GitHub Webhook for PR events" |
| **Environment Variable** | A runtime-configured variable for a job | `env.BUILD_NUMBER` |
| **Workspace** | Directory where Jenkins jobs execute | `/var/lib/jenkins/workspace/my-job` |

### Low-Level User Abstractions (System & Infrastructure Layer)

| **Abstraction** | **Conceptual Meaning** | **Examples** |
| --- | --- | --- |
| **Controller (Master)** | The core Jenkins instance | "Manages jobs and agents" |
| **Agent (Worker Node)** | A machine that executes builds | "Docker container with Jenkins agent" |
| **Label** | A tag used to assign jobs to agents | "linux-node, docker-builder" |
| **Queue** | The waiting list of pending jobs | "Build queued due to resource limits" |
| **Executor** | A process slot for running jobs | "2 executors per agent" |
| **Security Realm** | Authentication provider for Jenkins | "LDAP, Active Directory, OAuth" |
| **Authorization Strategy** | Defines user permissions | "Role-based access control (RBAC)" |
| **Remoting** | Jenkins agent communication layer | "JNLP, SSH, WebSockets" |

### **Meta-Level Abstractions (Extensibility & Customization)**

> For **plugin developers, infrastructure architects, and cloud engineers**, Jenkins is an **extensible automation platform** with a flexible plugin system and cloud-native integrations.
> 

| **Abstraction** | **Conceptual Meaning** | **Examples** |
| --- | --- | --- |
| **Plugin API** | Framework for extending Jenkins | "Jenkins Java Plugin Development" |
| **Event Hooks** | Custom triggers for Jenkins actions | "On job success, trigger another job" |
| **REST API** | Programmatic interface to Jenkins | "Trigger jobs via HTTP calls" |
| **Infrastructure as Code (IaC)** | Configuring Jenkins using code | "JCasC (Jenkins Configuration as Code)" |
| **Kubernetes Integration** | Dynamic agent provisioning | "Jenkins X, Helm, Kubernetes plugin" |

## Pipeline Models

- Jenkinsfile: A configuration file that defines the entire build process using a structured format.
- Scripted Pipeline: A more flexible pipeline model written in Groovy, allowing for complex logic and control flow.

## Job Models

- Freestyle Job: 	A simple job type that allows users to configure various build steps without code.
- …

## Build Environments

- Build Agents: Machines (nodes) where Jenkins executes build jobs, which can be configured for specific tasks.

## Artifact Management

- Artifact Repository: Managing build artifacts produced during the CI/CD process, allowing for versioning and retrieval.

## Testing

- Automated Testing: Configuring automated tests to run during the build process, ensuring code quality.
- Code Quality Tools: Integrating tools that analyze code for quality, style, and security issues during builds.

## Jenkins Architecture

> Jenkins follows a **distributed, event-driven, modular architecture**, enabling **scalable, automated, and extensible CI/CD workflows**. The architecture is designed to accommodate a wide range of **build, test, deployment, and monitoring operations**, while integrating seamlessly with **version control systems, artifact repositories, cloud platforms, and infrastructure automation tools**. Below is a holistic and in-depth technical characterization of Jenkins' architecture.
> 

### Architectural Model: Distributed and Modular

> Jenkins adheres to a **distributed client-server model**, where a **central controller (formerly master) orchestrates jobs** and **multiple agents (workers) execute workloads**. The modularity is enhanced through a **plugin-based extension system**, allowing seamless integration with DevOps toolchains.
> 

**Controller (Master) Node**

- **Core Responsibilities:**
    - Orchestrates pipeline execution and schedules jobs.
    - Manages communication with agent nodes.
    - Handles build definitions, credentials, logs, and artifact storage.
    - Exposes **REST API, CLI, and Web UI** for external control and automation.
- **Technical Aspects:**
    - Runs as a **Java Servlet** inside a web container (e.g., **Jetty, Tomcat**).
    - Uses a **message queue-based scheduler** for agent job dispatching.
    - Implements a **directed acyclic graph (DAG)-based execution model** for pipelines.
    - Uses **JNLP, SSH, WebSockets, or Kubernetes API** to connect to agents.
    - Stores job configurations and metadata in **XML-based flat files** or an **external database**.

**Agent (Worker) Nodes**

- **Core Responsibilities:**
    - Execute build and test jobs delegated by the controller.
    - Provide **compute isolation per job**, allowing parallel execution.
    - Support both **static (persistent) and dynamic (ephemeral) provisioning**.
- **Technical Aspects:**
    - Run Jenkins **agent.jar** (Java-based remoting service).
    - Can be deployed on **bare-metal, VMs, Docker containers, or Kubernetes pods**.
    - Uses **distributed workspace mechanisms** to manage build directories.
    - Communicates securely with the controller via **TLS-encrypted channels**.
    - Uses **process-level isolation (Linux namespaces, cgroups, or containers)** to prevent conflicts.

### Execution Model: Pipeline Processing & Task Scheduling

> Jenkins implements a **multi-threaded execution model** with **job queue prioritization** and **distributed execution**.
> 

**Pipeline Execution Model**

Jenkins executes **pipelines** using a **Directed Acyclic Graph (DAG)** structure, allowing optimized parallelization and dependency resolution. Pipelines are expressed using **Jenkinsfiles** in a **domain-specific language (DSL) based on Groovy**.

- **Pipeline Types:**
    - **Declarative Pipelines** (structured, recommended for CI/CD automation).
    - **Scripted Pipelines** (Groovy-based, more flexible for complex workflows).
- **Execution Flow:**
    1. **Code changes trigger pipeline execution** (event-driven).
    2. **Pipeline script is parsed and converted into a DAG**.
    3. **DAG scheduler optimizes parallel and sequential steps**.
    4. **Jobs are dispatched to agents** for execution.
    5. **Results, logs, and artifacts are collected and stored**.

**Task Scheduling & Load Balancing**

Jenkins provides **intelligent job scheduling** based on resource availability and agent capabilities.

- **Scheduling Mechanisms:**
    - **FIFO (First In, First Out)** queue for job execution.
    - **Priority-based scheduling** for high-importance jobs.
    - **Node affinity and label-based constraints** to distribute workloads optimally.
- **Concurrency Handling:**
    - **Parallel execution support** using multi-threading.
    - **Distributed locking** to prevent resource conflicts.
    - **Build queue monitoring** for performance optimization.

### **Communication & Remoting Layer**

> Jenkins implements a **secure, event-driven communication model** for agent interactions and external integrations.
> 

**Agent Communication Protocols**

Agents communicate with the controller using multiple secure channels:

- **JNLP (Java Network Launch Protocol):** Legacy TCP-based communication for self-registering agents.
- **SSH:** Secure remote execution for Unix-based worker nodes.
- **WebSockets:** Lightweight, bidirectional communication (useful in cloud environments).
- **Kubernetes API:** Used for dynamic agent provisioning in containerized workloads.

### Data Persistence & Storage Architecture

> Jenkins persists pipeline configurations, logs, and artifacts in structured storage systems.
> 

**Metadata & Build Storage**

- Job definitions and pipeline states are stored as **XML files** within the Jenkins home directory.
- Build logs, artifacts, and workspace data are stored in **local or remote storage backends**.
- Supports **external databases** (e.g., PostgreSQL, MySQL) via plugins for scalable storage.

**Credentials & Secrets Management**

- Uses **AES encryption** for stored credentials.
- Supports **HashiCorp Vault, Kubernetes Secrets, AWS Secrets Manager** for secure credential storage.

### Extensibility & Plugin System

> Jenkins has a **plugin-driven architecture**, making it highly extensible.
> 

**Plugin System Architecture**

- **Uses Java-based Plugin API** for extending Jenkins' capabilities.
- **Over 1,500+ plugins** available for SCMs, cloud platforms, build tools, etc.
- Plugins interact via **Jenkins Plugin Extension Points**.

**Key Plugin Categories**

- **Source Control Management (SCM):** Git, SVN, Bitbucket, GitHub.
- **Build Tools:** Maven, Gradle, Ant, Bazel.
- **Artifact Repositories:** Nexus, Artifactory.
- **Cloud Integrations:** AWS, GCP, Azure.

### Security & Access Control

> Jenkins implements **multi-layered security controls** to prevent unauthorized access and pipeline tampering.
> 

**Authentication & Authorization**

- Supports **LDAP, Active Directory, OAuth, and SAML-based authentication**.
- Role-based access control (RBAC) via **Matrix-based security models**.
- Enforces **principle of least privilege (PoLP)** for user roles.

**Secure Build Execution**

- Uses **sandboxed Groovy execution** to prevent malicious script execution.
- Implements **trusted artifact signing** for secure deployment pipelines.

### Cloud-Native & Containerization Support

> Jenkins is optimized for cloud-based CI/CD with **containerized and serverless execution models**.
> 

**Kubernetes-Native Jenkins**

- **Jenkins X**: Cloud-native Jenkins variant with GitOps support.
- **Dynamic agent provisioning** using Kubernetes pods.
- Supports **Docker-based ephemeral build environments**.

**Infrastructure as Code (IaC)**

- Pipelines as code with **Jenkinsfile**.
- Integrates with Terraform, Helm, Ansible for infra automation.

### **API & External Interfaces**

> Jenkins provides **multiple automation interfaces** for external toolchain integration.
> 

**REST API**

- Supports **JSON, XML-based queries** for build management.
- Provides endpoints for **job triggers, build results, and logs**.

**CLI (Command-Line Interface)**

- Enables **scriptable job execution and configuration**.
- Supports **batch automation via shell scripts**.

## Jenkins Files

> Which is the Jenkins Jobs Space?
> 

## Controller Node

> 

## Agent Node

> ….
> 

## Jenkins Plugins

> 

https://plugins.jenkins.io/ui/search/?query=

## References

- [Jenkins](https://www.jenkins.io/)
- https://www.jenkins.io/doc/book/
- https://plugins.jenkins.io/
- https://www.jenkins.io/doc/developer/
- https://github.com/csiglab/devops-labs
- https://github.com/jenkinsci/jenkins
- [http://localhost:8080/computer/(built-in)/](http://localhost:8080/computer/(built-in)/)