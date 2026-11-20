---
tags: [note, social, catalog]
---

# Computational System Product Space

> Overview of Software System Taxonomy & Profiles.

> Software Supply Chain: …

## Documentation

> …
> 

## File Browsing

> …
>

### Retrieval System

> Product Space

| **Type of System** | **Type** | **Description** | **Instance(s)** |
| --- | --- | --- | --- |
| **Web Search Engines** | General-purpose retrieval | Systems designed to index and retrieve web content using crawling, indexing, and ranking algorithms. Optimized for scalability, freshness, and relevance across heterogeneous data. | Google Search, Bing, DuckDuckGo |
| **Enterprise Search** | Organizational / Intranet retrieval | Retrieves documents, emails, reports, and databases within an organization. Often includes access control, domain-specific ranking, and metadata handling. | Elastic Enterprise Search, SharePoint Search |
| **Digital Library / Scholarly IR** | Domain-specific / Academic | Focused on curated collections of scholarly or structured content. Supports Boolean, faceted, and semantic queries. | PubMed / Entrez, ACM Digital Library |
| **Multimedia Retrieval** | Content-based retrieval | Indexes and retrieves non-textual data (images, audio, video) using content descriptors like color histograms, SIFT features, or embeddings. | Google Images, YouTube Search, Shazam |
| **Question-Answering Systems** | Semantic / QA retrieval | Maps natural language queries to concise answers rather than document lists. Integrates NLP, knowledge graphs, and deep learning models. | IBM Watson, OpenAI Chat-based QA, WolframAlpha |
| **Recommender Systems** | Personalized retrieval | Suggests items based on user preferences, behavior, or collaborative filtering. Focused on ranking rather than explicit search. | Netflix Recommendations, Amazon Product Suggestions |
| **Federated / Distributed IR** | Multi-source retrieval | Aggregates results from multiple independent repositories or databases, sometimes in real-time. Supports heterogeneous query translation and merging. | PubMed Central + Institutional Repositories, Meta-search engines |
| **Vertical / Domain-specific Engines** | Specialized retrieval | Optimized for specific domains like legal, medical, or e-commerce data. Often uses domain-specific ontologies or taxonomies. | LexisNexis (Legal), WebMD (Medical), Zillow (Real Estate) |
| **Real-time / Streaming Retrieval** | Dynamic content retrieval | Focused on time-sensitive or continuously updating data streams. Supports low-latency indexing and retrieval. | Twitter Search, Google News, Stock Data Retrieval |


## Information System

> ERP.
> 

| **Level** | **Category** | **Subcategory** | **Description / Examples** |
| --- | --- | --- | --- |
| **Purpose & Scope** | **Operational Systems** | Transaction Processing Systems (TPS) | Handles routine transactions (e.g., POS, ATM systems). |
|  |  | Enterprise Resource Planning (ERP) | Manages core business functions (e.g., SAP, NetSuite). |
|  |  | Supply Chain Management (SCM) | Optimizes logistics & inventory (e.g., Oracle SCM). |
|  | **Decision Support Systems** | Management Information Systems (MIS) | Provides reports for business insights (e.g., Power BI). |
|  |  | Decision Support Systems (DSS) | Analyzes data for decision-making (e.g., IBM Cognos). |
|  | **Strategic & Knowledge Systems** | Executive Information Systems (EIS) | High-level business insights for executives. |
|  |  | Business Intelligence (BI) | Data analytics & visualization (e.g., Tableau, Qlik). |
|  |  | Knowledge Management Systems (KMS) | Stores and shares knowledge (e.g., Confluence, SharePoint). |
| **Data & Technology Layers** | **Data Management & Integration** | Data Warehousing & ETL | Aggregates & transforms data (e.g., Snowflake, Redshift). |
|  |  | Big Data Analytics | Large-scale data analysis (e.g., Hadoop, Spark). |
|  |  | Master Data Management (MDM) | Ensures consistent data across systems (e.g., Informatica MDM). |
|  | **System Integration** | API-Based Integration | Connects apps via RESTful/SOAP APIs (e.g., Apigee, MuleSoft). |
|  |  | Middleware & ESB | Connects enterprise applications (e.g., WSO2, MuleSoft). |
|  |  | Cloud Integration (iPaaS) | Connects SaaS applications (e.g., Boomi, Zapier). |
| **Industry-Specific Systems** | **Healthcare Information Systems** | Electronic Health Records (EHR) | Manages patient data (e.g., Epic, Cerner). |
|  | **Financial Information Systems** | Banking & Financial Services | Supports transactions & compliance (e.g., SAP Financials). |
|  | **Government & Public Sector** | Government ERP | Manages public services (e.g., Tyler Technologies). |
|  | **Manufacturing & Logistics** | Manufacturing Execution Systems (MES) | Tracks production processes (e.g., Siemens Opcenter). |
| **Emerging Technologies** | **AI-Driven Information Systems** | AI in BI & Analytics | AI-powered insights (e.g., IBM Watson). |
|  | **Blockchain-Based Systems** | Distributed Ledgers | Secure transactions (e.g., Hyperledger). |
|  | **IoT & Edge Computing** | Real-Time Monitoring | Connects smart devices (e.g., AWS IoT). |
|  | **Cybersecurity & Risk Management** | Security Information & Event Management (SIEM) | Protects enterprise data (e.g., Splunk, ArcSight). |

### **Manufacturing & Logistics**

### PLM (Product Lifecycle Management)

> Manages product data and lifecycle from design to disposal.
> 

### Computer-Aided Engineering (CAE)

> Simulation and analysis of design performance
> 

### Computer-Aided Manufacturing (CAM)

> Converts designs into machine instructions
> 

### CAD (Computer-Aided Design)

> Computer-Aided Design.
> 

### Supervisory Control and Data Acquisition (SCADA)

> Monitors and controls industrial processes
> 

### Industrial Internet of Things (IIoT)

> Connects devices and sensors for real-time monitoring and analytics
> 

### Quality Management Systems (QMS)

> Ensures compliance with quality standards (ISO, Six Sigma, etc.)
> 

### Supply Chain Management (SCM)

> Manages logistics, procurement, and supplier coordination
> 

### Scheduling and Planning Software

> Optimizes job scheduling and production planning
> 

### Additive Manufacturing Software

> Supports 3D printing and digital fabrication
> 

### Warehouse Management System (WMS)

> Controls movement and storage of goods in warehouses
> 

### Inventory Management

> Tracks inventory levels, movement, and storage
> 

### Enterprise Asset Management (EAM)

> Manages maintenance and lifecycle of physical assets
> 

### Manufacturing Execution Systems (MES)

> Tracks and controls production on the factory floor
> 

## Non Local Computation

| **Type** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Distributed Systems** | Multiple nodes coordinate to appear as a single system; focus on consensus, synchronization, and fault tolerance. | Google Spanner, Apache Zookeeper |
| **Dataflow / Batch Processing** | Computation expressed as transformations on distributed datasets; emphasizes moving computation to the data. | MapReduce, Apache Spark, Flink (batch) |
| **Streaming / Online Computation** | Operates on data distributed *in time*, handling continuous event streams with low latency. | Apache Flink (streaming), Kafka Streams, Apache Storm |
| **In-Memory Data Grids** | Distributed, in-memory key–value data stores enabling computation close to the data. | Apache Ignite, Hazelcast, Oracle Coherence |
| **Federated / Privacy-Preserving Systems** | Computation performed across distributed nodes while keeping data local, often for privacy or bandwidth reasons. | TensorFlow Federated, FATE, PySyft |
| **Peer-to-Peer / Gossip Systems** | Fully decentralized systems where computation emerges from peer interactions without central coordination. | BitTorrent, Kademlia DHT, Gnutella |
| **Edge / Fog Computing** | Moves computation closer to data sources (IoT devices, sensors) to reduce latency and bandwidth use. | AWS Greengrass, Azure IoT Edge |
| **Grid / Cloud Supercomputing** | Aggregates geographically distributed or heterogeneous resources for large-scale computation. | BOINC, Globus, HPC clusters |
| **Quantum Non-Local Computation** | Exploits quantum entanglement to perform computations where information is distributed but correlated non-locally. | Quantum teleportation protocols, non-local games |
| **Communication Complexity Models** | Frameworks quantifying the minimum communication required to compute a function across distributed nodes. | Two-party protocols, multiparty communication models |

## Collaboration & Communication

> …
> 

| **Category** | **Subcategory** | **Example Tools** | **Focus/Description** |
| --- | --- | --- | --- |
| **Messaging & Real-Time Communication** | Instant Messaging | Rocket.Chat, Mattermost, Matrix | Real-time, direct communication between users (text, media, file sharing). |
|  | Chat Rooms & Group Messaging | Zulip, Slack (Open-source alternatives) | Group-based discussions organized into topics or channels. |
|  | Voice/Video Calls & Conferencing | Jitsi Meet, BigBlueButton, Nextcloud Talk | Real-time voice and video communication for meetings and group calls. |
| **Project Management & Issue Tracking** | Task Management | Taiga, OpenProject, Redmine | Organizing tasks, to-dos, deadlines, and project milestones for collaborative work. |
|  | Issue Tracking & Bug Tracking | GitLab, MantisBT, Phabricator | Managing issues, bugs, and feature requests in team or development projects. |
|  | Kanban and Scrum Boards | Wekan, Trello (Open-source alternatives) | Visual project management using boards and cards for task tracking. |
| **Document Collaboration & Sharing** | Document Editing & Collaboration | Etherpad, OnlyOffice, CryptPad | Real-time document creation, editing, and collaboration for teams. |
|  | File Sharing and Synchronization | Nextcloud, Seafile, Syncthing | File storage, synchronization, and sharing across multiple devices or team members. |
|  | Wikis & Knowledge Management | MediaWiki, DokuWiki, TikiWiki | Collaborative knowledge creation, editing, and organization in a wiki format. |
| **Version Control & Code Collaboration** | Version Control Systems | Git, Mercurial, Subversion | Tracking changes in source code and managing different project versions collaboratively. |
|  | Code Review & Collaboration | GitHub (Open-source alternatives like GitLab), Phabricator, Gerrit | Code sharing, review, and collaboration among developers with integrated version control. |
| **Team Collaboration Platforms** | Integrated Communication & Collaboration Suites | Mattermost, Rocket.Chat, Jitsi Meet | Combining messaging, file sharing, project management, and task tracking in one platform. |
|  | Enterprise Collaboration Platforms | Nextcloud Hub, Zimbra | Comprehensive solutions for businesses with integrated file management, communication, and collaboration tools. |
| **Asynchronous Communication & Discussions** | Discussion Forums | Discourse, Flarum, phpBB | Facilitating threaded discussions, support forums, and community engagement. |
|  | Mailing Lists & Newsletters | Mailman, Sympa | Asynchronous communication through email for groups, announcements, and discussions. |
| **Social Collaboration & Networking** | Social Networking Platforms | Mastodon, Friendica | Social interactions and community building with a focus on privacy and open-source ethics. |
|  | Microblogging & Messaging | GNU social, Pleroma | Short-form, real-time content creation and interaction (similar to Twitter but open-source). |
| **Collaborative Scheduling & Event Management** | Calendar and Scheduling Tools | Radicale, Nextcloud Calendar | Managing group calendars, event scheduling, and appointments within a collaborative environment. |
|  | Event Management Systems | OpenConferenceWare, Attendize | Organizing and managing events, conferences, and meetups collaboratively. |
| **Communication Infrastructure** | Real-Time Communication Protocols | Matrix, XMPP, WebRTC | Protocols enabling real-time messaging, voice, and video communications. |
|  | Push Notifications & Messaging Queues | RabbitMQ, Kafka, Apache Pulsar | Distributing real-time alerts and notifications across multiple systems or users. |
| **Automation and Workflow Collaboration** | Collaboration Automation Tools | Node-RED, n8n | Automating workflows, communication processes, and team collaboration using triggers and actions. |
|  | CI/CD for Collaborative Development | Jenkins, GitLab CI, Travis CI | Automating testing, deployment, and integration workflows for collaborative software development. |

## Organizational Cognitive Tools

- [ ]  https://docs.paperless-ngx.com/

## **Programming Software**

> Tools and environments that developers use to create, test, and debug software. Examples include text editors, compilers, debuggers, and Integrated Development Environments (IDEs) like Visual Studio and Eclipse.
> 

## **3D Modeling (Design & Drafting)**

*(Precision modeling for floor plans, sections, and construction details)*

- **AutoCAD** – Industry-standard 2D drafting & 3D modeling.
- **Revit (Autodesk)** – BIM (Building Information Modeling) for parametric design, documentation, and collaboration.
- **Archicad (Graphisoft)** – BIM-focused alternative to Revit, popular in Europe.
- **Rhino3D + Grasshopper** – Freeform NURBS modeling + algorithmic design (for complex geometries).
- **SketchUp (Pro)** – Quick 3D massing studies, conceptual design (with extensions like **V-Ray** or **Enscape**).

- **Mesh-Based Modeling**
    - **Blender** (sculpting, retopology).
    - **ZBrush** (digital sculpting, high-poly meshes).
    - **MeshLab** (3D mesh cleaning/processing).

## **GIS & Spatial Analysis**

*(Geometric tools for maps, terrains, and geospatial data)*

- **QGIS**, **ArcGIS** (polygon/terrain processing).
- **Google Earth Engine** (large-scale geospatial computation).

\

## **Visualization & Rendering**

*(Turning geometric data into images/video)*

- **Photorealistic Rendering**: **KeyShot**, **Lumion**, **V-Ray** (for Blender/Maya).
- **Scientific/Data Viz**: **ParaView**, **Tableau** (3D data plotting).
- **Real-Time Rendering**: **Unreal Engine**, **Twinmotion** (archviz/games).

## Digital Representation

> …
> 

### **BIM (Building Information Modeling)**

> **BIM (Building Information Modeling)** is a **process-driven digital representation** of a building's physical and functional characteristics, supported by specialized **software tools** that enable **3D modeling, data integration, collaboration, and lifecycle management** of construction projects.
> 

## Simulation Software

> Software that mimics real-world activities, processes, or systems for analysis, training, or experimentation. Examples include MATLAB, Simulink, and AutoCAD.
> 

## Network Software

> Software that facilitates the connection, management, and communication of computers and devices in a network. Examples include network drivers, protocols (e.g., TCP/IP), and network management software.
> 

### Communication Software

- https://tox.chat/
- https://jitsi.org/
- https://delta.chat/en/
- https://signal.org/

## **Middleware**

> Software that acts as an intermediary between different software applications or between applications and the operating system, enabling communication and data management. Examples include message brokers, API management tools, and application servers.
> 

## **Operating System (OS)**

> Software that manages hardware resources and provides services for application software. Examples include Windows, macOS, Linux, and Android.
> 

### **Virtualization Software**

> Software that allows multiple operating systems to run on a single physical machine by abstracting hardware resources. Examples include VMware, VirtualBox, and Hyper-V.
> 

### **Embedded Software**

> Specialized software designed to operate hardware with limited resources, often in real-time environments. Examples include software in embedded systems like smart TVs, medical devices, or automotive systems.
> 

### **Security Software**

> Software designed to protect computers and networks from threats such as viruses, malware, and unauthorized access. Examples include firewalls, antivirus programs, and encryption tools.
> 

## **Firmware**

> Low-level software programmed directly into a hardware device, controlling its basic functions. Examples include BIOS in computers, firmware in routers, and microcontrollers in electronic devices.
> 

### **Utility Software**

> System management tools that help analyze, configure, optimize, or maintain a computer. Examples include antivirus programs, disk cleanup tools, and file management utilities.
> 

## Text Editor

> …
> 

## Note-taking

> …
> 

## eMail Service

> …
> 
- https://github.com/stalwartlabs/mail-server

## Multimedia

> …
> 

## Computational Photography

> …
> 

## Computer Graphics

> …
> 

## Image Processing

> …
> 

## Video Processing

> …
> 

## Audio Processing

> …
> 

## Signal Processing

> …
> 

## References

- https://selfh.st/
- https://www.reddit.com/r/selfhosted/
- https://awesome-selfhosted.net/
- Create a My Digital Toolbox → https://karpathy.bearblog.dev/digital-hygiene/
- [A Guide Computational System Implementation Toolkit](https://www.notion.so/A-Guide-Computational-System-Implementation-Toolkit-1b5c0f5171ec8038909ef15467f06fb2?pvs=21)