# Continuous Delivery (CD)

- [Continuous Deployment (CD)](note.html?n=technica/computation/system/operation/operation-conceptual-model/continuous-deployment-cd.md)

> 

> **Continuous Deployment** being a more automated specialization of **Continuous Delivery**.
> 

- What is **Continuous Delivery (CD)?**
- How to deliver a set of **related applications  (in different dependency levels)**?
- How to think about **‘Continuous Delivery (CD)’**?
- What kind of Technical Element is  **‘Continuous Delivery (CD)’**?
- Which are the tchncal elmetns that made up - the ‘techncal practice’ of  contniosu felivery?
- **Continuous Delivery** answers: *How do I reliably deliver one application?*
- **Release Orchestration** answers: *How do I reliably deliver an ecosystem of interdependent applications in the correct order?*

```jsx
Technical Practice: Continuous Delivery
    ├── Activities
    │     ├── Build
    │     ├── Test
    │     ├── Package
    │     └── Deploy
    ├── Techniques
    │     ├── Blue-Green Deployment
    │     ├── Canary Release
    │     └── Automated Regression Testing
    ├── Principles
    │     ├── Automation
    │     ├── Fast Feedback
    │     └── Repeatability
    ├── Standards
    │     └── Release policies
    └── Tools
          ├── Jenkins
          ├── GitHub Actions
          └── Argo CD
```

| Technical Element | Description | Category |
| --- | --- | --- |
| Continuous Delivery | … | **Technical Element Set Modulo /** Technical Acivity |
| Continuous Delivery Domain | Engineering discipline concerned with automated software delivery and deployment. | Technical Domain |
| Software Delivery Environment | Production, staging, testing, and infrastructure where software executes. | Reality |
| CI/CD Pipeline | Automated workflow that builds, tests, packages, and deploys software. | Technical Activity |
| Build Stage | Compiles source code into executable artifacts. | Technical Activity |
| Test Stage | Executes automated quality validation. | Technical Activity |
| Package Stage | Produces deployable artifacts. | Technical Activity |
| Deployment Stage | Releases artifacts into an execution environment. | Technical Activity |
| Source Code Repository | Stores version-controlled source code. | Technical Infrastructure |
| Build Server | Executes automated builds and pipeline jobs. | Technical Infrastructure |
| Artifact Repository | Stores versioned deployable artifacts. | Technical Infrastructure |
| Container Registry | Stores container images. | Technical Infrastructure |
| Deployment Platform | Executes deployments (Kubernetes, VM, serverless, etc.). | Technical Infrastructure |
| Version Control System | Manages software revisions and history. | Technical Infrastructure |
| Developer | Creates and maintains application code. | Technical Agent |
| Build System | Compiles and packages software automatically. | Technical Agent |
| Deployment Engine | Executes deployment workflows. | Technical Agent |
| Test Runner | Executes automated tests. | Technical Agent |
| Release Manager | Authorizes production releases. | Technical Agent |
| Source Code | Human-readable software implementation. | Technical Blueprint |
| Build Script | Describes build procedure. | Technical Blueprint |
| Deployment Manifest | Describes deployment configuration. | Technical Blueprint |
| Infrastructure as Code | Declarative infrastructure specification. | Technical Blueprint |
| Container Image | Immutable deployable software package. | Production Technical Object |
| Deployable Package | Versioned application artifact (WAR, JAR, ZIP, etc.). | Production Technical Object |
| Running Application | Operational deployed software instance. | Production Technical Object |
| Library | Reusable software component. | Constitutive Technical Object |
| Microservice | Deployable subsystem within a larger application. | Constitutive Technical Object |
| Configuration File | Component defining runtime behavior. | Constitutive Technical Object |
| Continuous Integration | Technique for integrating code frequently with automated validation. | Technique |
| Continuous Deployment | Technique for automatically deploying validated software. | Technique |
| Blue-Green Deployment | Deployment technique minimizing downtime. | Operative Technique |
| Canary Deployment | Incremental deployment strategy. | Operative Technique |
| Rolling Deployment | Progressive replacement deployment technique. | Operative Technique |
| Feature Flags | Technique for runtime feature activation. | Operative Technique |
| Unit Testing | Component verification technique. | Constitutive Technique |
| Integration Testing | Component interaction verification technique. | Constitutive Technique |
| Static Analysis | Code quality verification technique. | Constitutive Technique |
| Packaging | Technique for creating deployable artifacts. | Constitutive Technique |
| Deliver software rapidly and safely | Desired operational objective. | Technical Purpose |
| Pipeline Architecture | Organization of stages, jobs, dependencies, and environments. | Technical Architecture |
| Deployment Specification | Defines deployment parameters and environment configuration. | Technical Specification |
| Build Specification | Defines compilation and packaging parameters. | Technical Specification |
| Software Release Requirement | Software must be deployable at any time. | Technical Requirement |
| Pipeline Failure | Build, test, packaging, or deployment failure. | Technical Failure |
| Deployment Rollback | Restores previous stable release after failure. | Maintenance |
| Pipeline Logs | Execution output generated during pipeline execution. | Technical Feedback |
| Test Report | Results produced by automated testing. | Technical Feedback |
| Monitoring Metrics | Runtime operational telemetry. | Technical Feedback |
| Build | Atomic action compiling source code. | Technical Act |
| Execute Tests | Atomic validation action. | Technical Act |
| Publish Artifact | Atomic artifact publication action. | Technical Act |
| Deploy Application | Atomic deployment action. | Technical Act |
| Rollback Deployment | Atomic recovery action. | Technical Act |
| Build Reproducibility | Principle ensuring identical builds from identical inputs. | Technical Principle |
| Immutable Artifacts | Principle prohibiting post-build modification. | Technical Principle |
| Idempotent Deployment | Principle allowing repeated deployment without side effects. | Technical Principle |
| Automation First | Principle minimizing manual intervention. | Technical Principle |
| Trunk-Based Development | Development planning strategy. | Technical Strategy |
| GitFlow | Branch management strategy. | Technical Strategy |
| Release Train | Scheduled release strategy. | Technical Strategy |
| DevOps | Organizational and operational framework for continuous delivery. | Technical Framework |
| Build Automation | Mechanism transforming source into binaries. | Technical Mechanism |
| Dependency Resolution | Mechanism retrieving required libraries. | Technical Mechanism |
| Containerization | Mechanism packaging software into containers. | Technical Mechanism |
| Orchestration | Mechanism coordinating deployments across infrastructure. | Technical Mechanism |
| Pipeline Execution Time | Performance limitation on delivery speed. | Technical Constraint |
| Production Approval Policy | Organizational deployment constraint. | Technical Constraint |
| Infrastructure Capacity | Resource limitation affecting deployment. | Technical Constraint |
| Security Policy | Compliance constraint governing releases. | Technical Constraint |
| Compute Resources | CPU, memory, storage, and network consumed by pipelines. | Resource |
| Build Time | Time resource required for pipeline execution. | Resource |
| Engineering Effort | Human labor required for development and maintenance. | Technical Labor |
| DevOps Competence | Capability to operate delivery pipelines effectively. | Technical Competence |
| Continuous Delivery Maturity | Historical progression toward higher automation and reliability. | Technical Evolution |
| DevOps Research | Investigation into improved delivery practices. | Technical Research |
| ISO/IEC 12207 | Software lifecycle engineering standard. | Technical Standard |
| Secure SDLC | Security engineering standard or organizational policy. | Technical Standard |
| CI/CD Governance Team | Organization defining delivery policies. | Technical Institution |
| Pipeline Validation | Verification that pipeline outputs satisfy specifications. | Verification |
| Secure Delivery | Protection of software artifacts, credentials, and deployment infrastructure. | Security |
| Legacy Deployment Process | Manual deployment process superseded by automated delivery. | Technical Obsolescence |