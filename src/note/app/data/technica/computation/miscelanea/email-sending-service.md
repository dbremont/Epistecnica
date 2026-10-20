# Email Sending Service


> An **Email Sending Service** is typically an external **Constitutive Technical Object (CTO)** that provides the infrastructure, protocols, and operational mechanisms necessary to send electronic mail reliably and at scale. It abstracts the underlying technical complexity—such as SMTP configuration, server management, queuing, deliverability monitoring, and authentication protocols (SPF, DKIM, DMARC)—allowing applications or users to dispatch emails without directly managing low-level network or mail server operations.
> 

QA:

- How to send emails on behalf of users?
- What is the Structure of an ‘**Email Service’?**
- How are email generated? How are email store?

## Formulation

**Which is  a email sending model?**

> An **Email Sending Model** is an **abstract operational pattern** that defines **how authority, identity, and delivery responsibility are structured** when sending email.
> 

> It is **conceptual and technology-agnostic**.
> 

It specifies:

- Who is authorized to send
- On whose behalf messages are sent
- How trust is established
- How messages are injected into the mail network

**Which is an email sending service?**

An **Email Sending Service** is a **concrete technical system**—typically an external **Constitutive Technical Object (CTO)**—that **implements one or more email sending models**.

It provides:

- Infrastructure (servers, queues, IPs)
- Operational techniques (retry, throttling, monitoring)
- APIs and administrative controls
- Deliverability and reputation management

## Terminology

| Term | Definition |
| --- | --- |
| **Email Service Provider** | The backend system that stores and routes emails. Includes SMTP servers for sending, and IMAP/POP3 servers for receiving and accessing messages. |
| **SMTP (Simple Mail Transfer Protocol)** | A protocol used for sending emails from a client or another server to a recipient mail server. |
| **IMAP (Internet Message Access Protocol)** | A protocol that allows clients to access and manage emails directly on the server, supporting multiple devices. |
| **POP3 (Post Office Protocol 3)** | A protocol that allows clients to download emails to a local device and optionally delete them from the server. |
| **Email Sending Service** | A cloud or external service (e.g., SendGrid, Mailgun, Amazon SES) that provides APIs or SMTP access to send emails on behalf of applications or users. |
| **Email Client** | The application used by end users to read, send, and organize emails (web, desktop, or mobile). |
| **Transactional Email** | Emails triggered by user actions or system events, such as password resets, order confirmations, or notifications. |
| **Promotional Email** | Marketing-focused emails intended to inform or persuade recipients, such as newsletters, discounts, or product announcements. |
| **System/Operational Email** | Administrative or infrastructure-related messages, including alerts, logs, and uptime notifications. |
| **Authentication & Trust** | Mechanisms that verify the sender’s identity and protect recipients from spoofing or phishing (e.g., SPF, DKIM, DMARC, TLS). |
| **SPF (Sender Policy Framework)** | DNS record specifying which servers are authorized to send email for a domain. |
| **DKIM (DomainKeys Identified Mail)** | A cryptographic method that signs outgoing emails to verify authenticity and integrity. |
| **DMARC (Domain-based Message Authentication, Reporting, and Conformance)** | A policy framework that instructs receiving servers on handling emails that fail SPF or DKIM checks. |
| **Bounce Handling / Return-Path** | Mechanisms to manage undelivered emails, often using a dedicated subdomain to track and process bounces. |
| **Email Template Engine** | Software for creating dynamic or personalized email content, often supporting HTML, CSS, and variable substitution. |
| **Deliverability Tools** | Systems and practices designed to ensure emails reach the inbox and avoid spam filters (e.g., IP warming, feedback loops, reputation monitoring). |
| **User Management** | The handling of subscriptions, preferences, opt-in/opt-out processes, and segmentation of recipients. |
| **Monitoring & Analytics** | Tracking metrics such as opens, clicks, bounce rates, and complaints to evaluate email performance. |
| **Compliance** | Legal frameworks governing email communications, such as GDPR, CAN-SPAM, CCPA, and CASL. |
| **Inbound Email Parsing** | Systems or services that process incoming emails for applications, such as ticketing, automated responses, or analytics. |
| **Rate Limiting & Throttling** | Controls to prevent excessive sending that could be interpreted as spam or overload mail servers. |
| **OAuth 2.0** | A secure authorization protocol that allows services to send email on behalf of a user without storing their password. |
| **IP Warm-Up** | Gradually increasing the volume of emails sent from a new IP address to build reputation and avoid spam filters. |
| **Branded Sending Domain** | A domain or subdomain used for sending emails that reflects the brand identity while ensuring deliverability and compliance. |
| **Mailhook** | Event-driven endpoints that allow applications to react to email events, such as delivery, bounces, or replies. |
| **Webhook** |  |

## Design

### Structure

> What is the structure of a **Email Sending Service**?
> 

| Part | Description | Role |
| --- | --- | --- |
| **SMTP (Transmission Engine)** | Core component responsible for sending emails using SMTP (Simple Mail Transfer Protocol) or other transport protocols. | Ensures emails are dispatched from the service to recipient mail servers reliably. |
| **API Layer** | Exposes RESTful or SDK-based interfaces for external applications to submit email requests. | Decouples the service logic from clients, enabling programmatic email sending. |
| **Queue (Buffer System)** | Temporary storage for outgoing messages before transmission. | Manages traffic bursts, retries, and rate limits to optimize deliverability. |
| **Authentication & Security Module** | Implements SPF, DKIM, DMARC, TLS, and other security standards. | Ensures emails are trusted, verifiable, and protected in transit. |
| **Monitoring & Logging** | Tracks delivery status, bounces, complaints, and errors. | Provides observability, diagnostics, and compliance reporting. |
| **Analytics & Reporting** | Collects data on delivery rates, open rates, clicks, and engagement. | Supports performance evaluation, optimization, and user insights. |
| **Reputation & Deliverability Manager** | Maintains IP/domain reputation, throttling, and blacklisting handling. | Ensures maximum inbox placement and minimizes spam labeling. |
| **Administration & Configuration Interface** | Dashboard or management console for configuration, templates, and credentials. | Provides user control, system configuration, and operational oversight. |

### Technique Space Taxonomy

> What are the techniques used to design and operate an **Email Sending Service**?
> 

| Type | Description | Instance(s) |
| --- | --- | --- |
| **Queueing & Delivery Management** | Methods to handle outgoing emails, ensure retries, and manage traffic spikes. | Outgoing Email Queueing, Retry Strategies, Throttling / Rate Limiting |
| **Security & Authentication** | Techniques to ensure message authenticity, integrity, and confidentiality. | SPF/DKIM/DMARC enforcement, TLS transport, API authentication (OAuth2, API keys) |
| **Reputation & Deliverability** | Methods to maintain sender IP/domain trust and ensure inbox placement. | IP Reputation Management, Feedback Loop Processing, IP Warm-up, Blacklist Monitoring |
| **High Availability & Scalability** | Techniques to ensure consistent performance under high load. | Load Balancing, Horizontal Scaling, Failover Mechanisms, Distributed SMTP Clusters |
| **Content & Template Management** | Methods for dynamic and reusable email content generation. | Template Engines, Variable Substitution, Localization, HTML Rendering |
| **Observability & Monitoring** | Techniques for tracking system and delivery performance. | Logging, Metrics Collection, Dashboards, Alerting |
| **Analytics & Engagement Tracking** | Methods for measuring recipient engagement and optimizing campaigns. | Open/Click Tracking, Bounce Analysis, A/B Testing, Campaign Reporting |
| **API & Integration** | Techniques to expose service functionality to external applications. | REST/GraphQL APIs, SDKs (Python, Java, Node.js), Webhooks |
| **Compliance & Regulatory Techniques** | Methods to enforce legal and organizational email policies. | Opt-in/Opt-out Management, GDPR/CAN-SPAM Compliance, Audit Logging |
| **Operations & Administration** | Techniques for service configuration, management, and operational oversight. | Dashboard Management, Template Management, Credential/Access Control, System Configuration |

### Technique Space

> What are the constitutive techniques used in the design, implementation, and operation of an **Email Sending Service**?
> 

| Technique | Type | Description |
| --- | --- | --- |
| Outgoing Email Queueing | Queueing & Delivery Management | Manages outgoing emails in a buffer to handle high volume and retry failed deliveries. |
| Retry Strategies | Queueing & Delivery Management | Implements mechanisms like exponential backoff, priority scheduling, or delayed retries for failed sends. |
| IP Reputation Management | Reputation & Deliverability | Techniques to monitor and improve sending IP/domain reputation, including warm-up strategies. |
| Throttling / Rate Limiting | Queueing & Delivery Management | Controls sending rate to prevent overload and minimize spam flagging. |
| Authentication Enforcement | Security & Compliance | Applying SPF, DKIM, DMARC, and TLS to ensure messages are trusted and verifiable. |
| Template Management | Content Management | Techniques for creating dynamic, reusable email templates with variable substitution and localization. |
| Analytics & Engagement Tracking | Performance & Monitoring | Collects and processes metrics such as opens, clicks, bounces, and unsubscribes to optimize campaigns. |
| Logging & Monitoring | Observability & Operations | Centralized tracking of system events, delivery status, errors, and operational metrics. |
| API Abstraction | Integration & Automation | Exposes email functionality through REST/GraphQL interfaces or SDKs, decoupling service from clients. |
| High-Availability Architecture | Scalability & Reliability | Techniques for load balancing, clustering, and failover to ensure continuous operation. |
| Compliance Automation | Regulatory & Legal | Enforces opt-in/out policies, GDPR/CAN-SPAM rules, and automated reporting. |
| Feedback Loop Processing | Reputation & Deliverability | Techniques for processing ISP feedback (spam complaints, bounces) to adjust sending practices. |
| Encryption & Secure Transport | Security & Authentication | Ensures message confidentiality and integrity using TLS and secure API authentication. |

## Evaluation

> How to evaluate a **Email Sending Service?**
> 

| Category | Criteria | Description |
| --- | --- | --- |
| **Deliverability** | Inbox Placement Rate | Measures the percentage of sent emails that reach recipients’ inboxes rather than spam/junk folders. |
|  | Bounce Handling | Ability to manage hard and soft bounces efficiently and provide actionable reporting. |
| **Scalability & Performance** | Throughput | Maximum number of emails the service can send per second/minute/hour. |
|  | Queue Management | Effectiveness in handling high-volume bursts without delays or failures. |
| **Reliability** | Uptime & SLA | Service availability and guarantees for uninterrupted operation. |
|  | Retry Mechanisms | Automatic handling of transient delivery failures to ensure reliable message delivery. |
| **Security & Compliance** | Authentication & Protocols | Support for SPF, DKIM, DMARC, TLS, and secure API connections. |
|  | Regulatory Compliance | Adherence to GDPR, CAN-SPAM, or other relevant data protection regulations. |
| **Usability & Integration** | API & SDK Quality | Ease of integration, documentation quality, and language support for clients. |
|  | Dashboard & Management | Intuitive interfaces for monitoring, configuration, and reporting. |
| **Analytics & Insights** | Tracking & Reporting | Ability to monitor opens, clicks, engagement metrics, and generate actionable insights. |
|  | Reputation Management | Tools to monitor IP/domain reputation, blacklist status, and deliverability trends. |
| **Cost Efficiency** | Pricing Model | Alignment of service cost with usage, volume, and value provided. |
|  | Resource Optimization | Ability to achieve maximum deliverability and throughput without unnecessary expense. |

## Case Study

| **Email Sending Service** | **Description** |
| --- | --- |
| **SendGrid** | Cloud-based service providing high-volume email delivery, transactional and marketing emails, APIs, analytics, and deliverability tools. Widely used for SaaS applications and enterprise communications. |
| **Amazon SES (Simple Email Service)** | Scalable, cost-effective email sending service integrated with AWS. Supports bulk sending, transactional messages, and detailed monitoring, with strong emphasis on security and reputation management. |
| **Mailgun** | Developer-focused email platform with powerful APIs, email validation, and analytics. Suitable for transactional emails, automated workflows, and high-volume campaigns. |
| **Postmark** | Focused on transactional email delivery with fast inbox placement, reliability, and detailed logging. Optimized for critical emails like password resets and notifications. |

## QA

### How a Email Sending Server send mails on Behalf of Users? Does it needs the user credentials?

| **Sending Model** | **Authentication Mechanism** | **Typical Use Case** |
| --- | --- | --- |
| **Domain-authorized sending** | Domain-level authentication via DNS records (SPF authorization, DKIM signing, DMARC policy enforcement). No per-user credentials involved. | SaaS applications, transactional email, system notifications |
| **API-based sending** | Application authentication using API keys or OAuth tokens issued to the application or service, not the end user. | Cloud email services, backend systems, microservices |
| **OAuth delegated sending** | User-granted OAuth authorization with scoped access tokens (no password sharing). | Personal email integration (e.g., Gmail API, Outlook API) |
| **SMTP AUTH as user** | SMTP authentication using the user’s mailbox credentials (username/password or app password). | Legacy systems, direct mailbox relay |

## References

- https://github.com/AnswerDotAI/markdown_merge
- https://aws.amazon.com/ses/
- [A Guide To eMails](https://app.notion.com/p/A-Guide-To-eMails-2834cbf8494e4cbeaab329451472d7cc?pvs=21)
- https://rspamd.com/
- https://github.com/postalserver/postal
- https://github.com/Mailtrain-org/mailtrain
- https://github.com/mautic/mautic
- https://github.com/postalsys/emailengine
- https://github.com/haraka/Haraka
- https://github.com/mailhog/MailHog
- https://books.dwf.dev/docs/system-design/c24