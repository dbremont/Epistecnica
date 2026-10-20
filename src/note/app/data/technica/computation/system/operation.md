# Operation

What is the hierhcy of deplymetn and operation element?

Sinse the **operation itself is a system**?  Where to build and store the description of such a system?

Controller System → Operational System

https://chatgpt.com/share/6a89ffec-a01c-83ea-80a4-4b71003f6c7d  (Operation Unit - Production Technical  Objects - That Operationzliaed This Cocnepts)

- https://github.com/dbremont/Operation/blob/main/README.md

Provision → Instantiate → Start → Stop → Restart → Scale → Upgrade

Name for the technical field:

- Production Operation
- Deployment Operation
- Deployable  Computation Process Artifact Operation

Computation Process Artifact  Operation Production Technical Object Type of Systems:

- How does they model  Computation Process Artifact  Operation?

What is the **fundamental unit of deployment**?

- Deployable  Computation Process Artifact (Container, Executable)
- Computanabile Platform → Physicla hardware, etc

```bash
Composition Unit
        │
        ├── Environment
        │
        ├── System Landscape
        │       │
        │       └── System
        │               │
        │               └── Deployment Group
        │                       │
        │                       └── Deployment Instance
        │                               │
        │                               └── Container
        │                                       │
        │                                       └── Process
```

→ THIS IS PART OF SOFTWARE PRODUCTION

→ THE OPERAION PART

→ [https://spinnaker.io/](https://spinnaker.io/) Interal Model for Continous Develivery

https://docs.github.com/en/actions/reference/workflows-and-actions

- How to build a docker image as an artifact in GHCR?
- What type of elements should a deployment artifcat contains? Should a docker image -  contint the source code? or It should be a wrapper for the executable?

> **DevOps** is a set of practices, tools, and a cultural mindset that integrates software development (Dev) and IT operations (Ops) to improve collaboration, automate workflows, and accelerate software delivery with high reliability.
> 

| **Category** | **Subcategory** | **Description** | **Tools** |
| --- | --- | --- | --- |
| **Data Collection & Ingestion** | Log Collection | Tools for collecting logs, metrics, and telemetry data from various systems. | **Fluentd**, **Logstash**, **Filebeat**, **Telegraf** |
|  | Data Ingestion | Tools for ingesting data from various sources into pipelines. | **Apache Kafka**, **Apache NiFi**, **Kinesis**, **Azure Event Hubs** |
| **Data Storage & Management** | Data Lakes | Tools to store large volumes of raw and structured data for ML processing. | **Hadoop HDFS**, **Amazon S3**, **Google Cloud Storage**, **MinIO** |
|  | Databases | Systems for storing structured and unstructured data. | **PostgreSQL**, **MongoDB**, **Elasticsearch**, **Google BigQuery** |
| **Model Training & Development** | Model Development | Frameworks for building machine learning models. | **TensorFlow**, **PyTorch**, **Scikit-learn**, **Keras**, **XGBoost** |
|  | Model Training & Tuning | Tools for optimizing and tuning models. | **Optuna**, **Hyperopt**, **Keras Tuner**, **Ray Tune** |
| **Model Deployment & Serving** | Model Serving | Systems that serve trained models for inference in production. | **TensorFlow Serving**, **TorchServe**, **FastAPI**, **Flask** |
|  | Model Deployment | Tools for automating model deployment pipelines. | **Kubeflow**, **MLflow**, **Seldon Core**, **TFX** |
| **Continuous Integration/Continuous Deployment (CI/CD)** | CI/CD Pipelines | Tools for automating the building, testing, and deployment of ML models. | **Jenkins**, **GitLab CI/CD**, **CircleCI**, **Azure DevOps** |
|  | Version Control | Tools for versioning models, data, and code. | **Git**, **DVC (Data Version Control)**, **MLflow** |
| **Monitoring & Observability** | Model Monitoring | Tools to monitor the performance of ML models in production. | **Prometheus**, **Grafana**, **Datadog**, **Kibana** |
|  | Log Monitoring | Systems to track, analyze, and visualize logs from applications and services. | **ELK Stack (Elasticsearch, Logstash, Kibana)**, **Graylog**, **Splunk** |
| **Automated ML (AutoML)** | Automated Model Selection | Tools to automate the selection and training of ML models. | **H2O.ai**, **Auto-Sklearn**, **TPOT**, **Google Cloud AutoML** |
|  | Hyperparameter Optimization | Tools for automating the hyperparameter tuning process. | **Optuna**, **Hyperopt**, **Ray Tune**, **Keras Tuner** |
| **Collaboration & Documentation** | Experiment Tracking | Tools for logging experiments, model parameters, and metrics. | **MLflow**, **Comet ML**, **Weights & Biases**, **Neptune.ai** |
|  | Model Registry | Systems for storing and tracking models throughout their lifecycle. | **MLflow**, **DVC**, **TensorFlow Model Garden** |

## Continuous Integration  (CI)

> **Continuous Integration (CI)** is a development practice where code changes are automatically built, tested, and merged into a shared repository multiple times a day to detect and fix issues early.
> 

## Continuous Delivery (CD)

> **Continuous Delivery (CD)** is a software development practice where code changes are automatically tested and prepared for deployment to production, ensuring that software can be released at any time with minimal effort.
> 

## Continuous Deployment (CD)

> A deployment model refers to a specific approach or strategy for deploying and delivering software applications or systems. It outlines how an application or system is made available to end-users, whether they are internal employees, external customers, or other systems. Deployment models encompass various aspects, including the infrastructure, architecture, distribution, scalability, and management of the application. They play a crucial role in determining how an application is hosted, maintained, and accessed.
> 

**Deployment models** can vary significantly based on factors such as the application’s requirements, the organization’s goals, and the target environment.

Here are some common deployment models:

1. **On-Premises Deployment**: In this model, the application is deployed within an organization’s own physical data center or infrastructure. The organization is responsible for provisioning, managing, and maintaining the hardware and software.
2. **Cloud Deployment**: Applications are hosted on cloud infrastructure provided by cloud service providers like AWS, Azure, or Google Cloud. Organizations rent resources from the cloud provider, reducing the need for on-premises hardware management.
3. **Hybrid Cloud Deployment**: A combination of on-premises and cloud resources is used. Some components or workloads are deployed in the cloud, while others remain on-premises. This model offers flexibility and scalability.
4. **Edge Computing Deployment**: Applications are deployed on edge devices or servers located close to the data source or end-users. This is suitable for scenarios requiring low latency and real-time processing.
5. **Serverless Deployment**: Applications are broken down into small, event-driven functions. Cloud providers manage the underlying infrastructure, and users are billed based on the actual compute usage.
6. **Containerized Deployment**: Applications and their dependencies are packaged into containers, ensuring consistency across different environments. Containers can be deployed on any platform supporting containerization technology.
7. **Microservices Deployment**: Applications are decomposed into small, independent microservices. Each microservice can be developed, deployed, and scaled independently, promoting flexibility and scalability.
8. **Web Deployment**: Web applications are deployed on web servers and made accessible over the internet. Common web servers include Apache, Nginx, and Microsoft IIS.
9. **Mobile Deployment**: Mobile applications are distributed through app stores (e.g., Apple App Store, Google Play Store) and installed on smartphones and tablets.
10. **Desktop Deployment**: Desktop applications are packaged as installable executables for Windows, macOS, or Linux. Users download and install the software locally.
11. **IoT (Internet of Things) Deployment**: Software is deployed on embedded systems or IoT devices, often with resource constraints. Deployment methods may involve OTA (Over-The-Air) updates.
12. **Virtual Appliance Deployment**: Applications are packaged as virtual appliances, including the operating system and dependencies. These appliances can be run in virtualized environments.
13. **Bare Metal Deployment**: Applications are deployed directly on physical hardware without virtualization or containerization. This is common in scenarios requiring maximum performance.
14. **Continuous Deployment (CD)**: Applications are continuously deployed and updated based on code changes. CD pipelines automate the build, test, and deployment processes.
15. **Rolling Deployment**: Updates are deployed gradually to subsets of servers or instances at a time, ensuring the application remains available during the update process.
16. **Blue-Green Deployment**: Simultaneous deployment of a new version alongside the existing version, with a switch-over when the new version is ready.
17. **Canary Deployment**: Gradual release of a new version to a subset of users for testing before a full rollout.

## Dimensions

> When discussing deployment models for software applications, it’s important to consider various dimensions that describe the characteristics and attributes of the deployment.
> 

These dimensions help define how the application is deployed, hosted, and managed. Here is a list of common dimensions of a **deployment model**:

**Location**: 

- **On-Premises**: The application is deployed in an organization’s own physical data centers or infrastructure.
- **Cloud**: The application is hosted and run on cloud infrastructure provided by a cloud service provider.

**Deployment Type**: 

- **Single-Tenant**: The application is dedicated to a single organization or user.
- **Multi-Tenant**: The application is shared among multiple organizations or users.

**Scalability**: 

- **Vertical Scaling**: Resources (e.g., CPU, memory) are added to a single instance of the application to handle increased load.
- **Horizontal Scaling**: Multiple instances of the application are deployed to distribute load and improve scalability.

**Isolation**:

- **Isolated Deployment**: Each instance of the application runs in its own isolated environment.
- **Shared Deployment**: Multiple instances of the application share resources and infrastructure.

**Resource Management**:

- **Self-Managed**: The organization is responsible for managing and maintaining the underlying infrastructure.
- **Managed Service**: The cloud provider or a third-party service manages infrastructure, scaling, and maintenance.

**Data Storage**: 

- **Local Storage**: Data is stored on the same server or instance as the application.
- **Distributed Storage**: Data is stored in distributed databases or storage systems for scalability and fault tolerance.

**Deployment Method**: 

- **Manual Deployment**: The application is deployed and updated manually.
- **Automated Deployment**: Deployment and updates are automated using CI/CD pipelines or deployment tools.

**Rollback Strategy**: 

- **Rollback to Previous Version**: The ability to revert to the previous version of the application in case of issues during deployment.
- **Rolling Back in Stages**: Gradual rollback by rolling back a subset of instances or users at a time.

**Testing Environment**: 

- **Staging Environment**: A separate environment for testing new releases and updates before deploying them to the production environment.
- **Production Environment**: The live environment where the application serves end-users.

**Traffic Routing**: 

- **Load Balancing**: Distributing incoming traffic across multiple instances of the application to improve availability and performance.
- **Traffic Shifting**: Gradual routing of traffic to new versions of the application during updates.

**High Availability**: 

- **Failover Clustering**: Redundant systems and automatic failover to ensure application availability.
- **Load Balancing**: Distributing traffic to multiple instances for load distribution and failover.

**Data Backup and Recovery**:

- **Regular Backups**: Scheduled backups of data and configurations to prevent data loss.
- **Disaster Recovery**: Plans and procedures for recovering the application and data in the event of a disaster.

**Deployment Rollout Strategy**: 

- **Blue-Green Deployment**: Simultaneous deployment of a new version alongside the existing version, with a switch-over.
- **Canary Deployment**: Gradual release of a new version to a subset of users for testing before a full rollout.

**Geo-Redundancy**:

- **Multi-Region Deployment**: Deploying instances of the application in multiple geographic regions for redundancy and global reach.
- **Disaster Recovery Sites**: Establishing secondary sites for failover in the event of regional outages.

## Software Packing Models

> Software packaging models refer to the methods and formats used to package and distribute software applications and libraries. These packaging models help streamline the distribution, installation, and management of software across various platforms and environments.
> 

| **Packaging Model** | **Description** | **Examples** |
| --- | --- | --- |
| **Installer Executables** | Installers that include scripts and dependencies for software installation. | MSI (Windows), EXE Installers |
| **Package Managers** | Systems for managing software installation, updates, and dependencies via repositories. | APT (Debian/Ubuntu), YUM (RHEL/CentOS), Homebrew (macOS), Chocolatey (Windows) |
| **App Stores** | Centralized platforms for distributing and installing applications. | Apple App Store (iOS/macOS), Google Play Store (Android), Microsoft Store (Windows) |
| **Containerization** | Packages applications with dependencies in portable containers for consistent deployment. | Docker Containers, Kubernetes Helm Charts |
| **Package Files and Archives** | Compressed or bundled files containing software and related resources. | ZIP, Tarballs, JAR (Java Archive) |
| **Installer Scripts** | Custom scripts for automating software installation and configuration. | Shell Scripts (Bash), Python Scripts |
| **Package Repositories** | Centralized repositories for distributing software libraries and dependencies. | PyPI (Python), NPM (Node.js), RubyGems (Ruby) |
| **Virtual Appliances** | Pre-configured virtual machine images for easy deployment. | VMDK, OVF, Vagrant Boxes |
| **Application Marketplaces** | Platforms for purchasing and downloading software and extensions. | Steam (Games), Salesforce AppExchange |
| **Cloud Deployment Packages** | Infrastructure-as-Code (IaC) templates for deploying cloud applications. | AWS CloudFormation Templates, Azure ARM Templates |
| **Plugin & Extension Stores** | Repositories for software plugins and extensions. | WordPress Plugin Repository, Visual Studio Code Marketplace |
| **CI/CD Artifact Repositories** | Storage for build artifacts and software packages in DevOps pipelines. | JFrog Artifactory, Sonatype Nexus |

## QA

### **Should each application be deployed in its own Docker container, or should all applications run in a single container?**

> 

## References

Operation: Conceptual Model

- [What is CI/CD?](https://about.gitlab.com/topics/ci-cd/)
- [Log Processing](note.html?n=technica/computation/system/evaluation/monitoring/monitoring-conceptual-model/log-processing.md)
- https://www.reddit.com/r/devops/
- https://en.wikipedia.org/wiki/DevOps
- [A Guide to Akamai-Linode](https://app.notion.com/p/A-Guide-to-Akamai-Linode-155c0f5171ec805d8d20e63d32f68077?pvs=21)
- https://www.usebraintrust.com/hire/interview-questions/devops-engineers
- https://news.ycombinator.com/item?id=36354049
- https://news.ycombinator.com/item?id=14652993
- https://arxiv.org/abs/1909.05409
- https://news.ycombinator.com/item?id=32639970
- https://dev.to/prodevopsguytech/100-aws-devops-interview-questions-and-answers-3g1i
- https://roadmap.sh/questions/devops
- [Service Discovery](note.html?n=technica/computation/miscelanea/service-discovery.md)
- (Web Administration Window -  Computer Web Server) http://cockpit-project.org/
- https://ml-ops.org/
- https://ollama.com/
- https://en.wikipedia.org/wiki/MLOps
- https://openrouter.ai/
- https://lmstudio.ai/
- [MLOps](https://madewithml.com/courses/mlops/)
- [MLOps-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp)
- https://huyenchip.com/mlops/
- https://github.com/visenger/awesome-mlops
- https://blog.vllm.ai/2025/12/17/large-scale-serving.html