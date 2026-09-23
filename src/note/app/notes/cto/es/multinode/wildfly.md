# Wildfly

## Formulation

### What technical element type does this technical instance belong to?

**WildFly belongs to the `Production Technical System` technical element type.**

More specifically:

```text
Production Technical System
└── WildFly
```

WildFly is a technical system because it is an organized composition of software runtime components, services, subsystems, interfaces, configuration, dependencies, and management mechanisms that collectively provide an application-server runtime.

### What is this technical instance?

> WildFly is a concrete modular application-server technical system instance providing a managed runtime for deploying, executing, integrating, securing, and managing enterprise applications and supporting technical services.

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one WildFly server distribution instance (artefacts, configuration surface, runtime structure, practices); deployment-specific values appear only in rows marked exemplar.
>
> Stopping rule: a row is terminal when it names a concrete file, process, configuration attribute, measured value, or named actor; attribute slots (Port, Version, Name) are terminal by rule.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.

| Instance Tree Path | Description | Technical Category | Technical Element Type Tree Path |
|---|---|---|---|
| **WildFly** | Running WildFly application-server platform instance. | System Structure | `(root) > Production Technical System` |
| WildFly > Instance Boundary | Scope of this decomposition: distribution artefacts, configuration surface, runtime structure, and operating practices; deployment-specific values appear only in exemplar rows. | System Structure | `Set Boundary` |
| WildFly > Distribution | Installed WildFly server distribution from which the runtime is provisioned. | System Structure | `(root) > Production Technical Object` |
| WildFly > Distribution > WildFly Home | Root filesystem location containing the server installation. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `bin/` | Executable scripts and command-line entry points. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `bin/standalone.sh` | Launch mechanism for a standalone server process. | Technical Operation | `Technical Operation > Technical Technique > Operative Technique` |
| WildFly > Distribution > `bin/standalone.bat` | Windows launch script for a standalone server process. | Technical Operation | `Technical Operation > Technical Technique > Operative Technique` |
| WildFly > Distribution > `bin/domain.sh` | Launch mechanism for managed-domain processes. | Technical Operation | `Technical Operation > Technical Technique > Operative Technique` |
| WildFly > Distribution > `bin/domain.bat` | Windows launch script for managed-domain processes. | Technical Operation | `Technical Operation > Technical Technique > Operative Technique` |
| WildFly > Distribution > `bin/jboss-cli.sh` | Command-line management client launcher. | Technical Operation | `Technical Operation > Technical Technique > Operative Technique` |
| WildFly > Distribution > `bin/jboss-cli.bat` | Windows command-line management client launcher. | Technical Operation | `Technical Operation > Technical Technique > Operative Technique` |
| WildFly > Distribution > `bin/add-user.sh` | User/identity configuration utility. | Technical Operation | `Technical Operation > Technical Technique` |
| WildFly > Distribution > `bin/add-user.bat` | Windows user and identity configuration utility. | Technical Operation | `Technical Operation > Technical Technique` |
| WildFly > Distribution > `bin/elytron-tool.sh` | Elytron security utility launcher. | Technical Operation | `Technical Operation > Technical Technique` |
| WildFly > Distribution > `bin/elytron-tool.bat` | Windows Elytron security utility launcher. | Technical Operation | `Technical Operation > Technical Technique` |
| WildFly > Distribution > `bin/client/` | Client library directory for remote access. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `bin/client/jboss-cli-client.jar` | Client library for remote management access. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `bin/init.d/` | Unix service initialization scripts. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `bin/service/` | Service wrapper definitions. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `bin/jboss-cli.xml` | CLI configuration file. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `bin/standalone.conf` | Standalone JVM launch configuration (heap, system properties). | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `bin/standalone.conf.bat` | Windows standalone JVM launch configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `bin/domain.conf` | Domain-mode JVM launch configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `bin/domain.conf.bat` | Windows domain-mode JVM launch configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `modules` | JBoss Modules repository containing server modules. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `modules > Module` | Isolated module containing classes/resources and dependency metadata. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `modules > Module > module.xml` | Module dependency and resource declaration. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Distribution > `modules/system/layers/base/` | Base layer containing core WildFly modules. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/` | Standalone-server runtime state and configuration tree. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/configuration/` | Standalone server configuration repository. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/configuration/standalone.xml` | Main standalone server configuration (default profile). | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone-full.xml` | Full standalone configuration profile including additional services such as messaging. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone-ha.xml` | Standalone high-availability configuration profile. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone-full-ha.xml` | Full high-availability standalone configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone-microprofile.xml` | MicroProfile standalone configuration profile. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone-microprofile-ha.xml` | MicroProfile high-availability configuration profile. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone-load-balancer.xml` | Load-balancer configuration profile. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/mgmt-users.properties` | Management user credentials store. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/mgmt-groups.properties` | Management group-to-role mapping. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/application-users.properties` | Application user credentials store. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/application-roles.properties` | Application user-to-role mapping. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/logging.properties` | Logging configuration properties. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone_xml_history/` | Configuration change history. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/deployments/` | Deployment content and deployment markers. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/data/` | Runtime-generated persistent server data. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/data/content/` | Content repository for deployed artifacts. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/data/timer-service-data/` | EJB timer persistence data. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/data/tx-object-store/` | Transaction object store. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/log/` | Runtime log storage. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/log/server.log` | Main server log file. | Technical Control | `Technical Control > Technical Feedback` |
| WildFly > Distribution > `standalone/log/audit.log` | Management audit log. | Technical Control | `Technical Control > Technical Feedback` |
| WildFly > Distribution > `standalone/tmp/` | Runtime temporary data. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `standalone/tmp/vfs/` | Virtual file system cache for deployments. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Distribution > `docs/` | Documentation and schema files. | Knowledge & Methodology | `Knowledge & Methodology > Technical Knowledge` |
| WildFly > Distribution > `docs/schema/` | XML schema definitions for configuration files. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Domain Distribution | Domain-mode configuration and process-management structure. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Domain Distribution > `domain/configuration/domain.xml` | Domain-wide profiles, server groups and subsystem configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/host.xml` | Host Controller configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/host-master.xml` | Master Host Controller configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/host-slave.xml` | Slave Host Controller configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > Host Controller | Process responsible for managing server processes on a host. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Domain Distribution > Configuration Propagation Flow | Host controller propagating configuration to managed servers. | System Relations | `Technical Interaction` |
| WildFly > Domain Distribution > Domain Controller | Process responsible for managing the domain-wide configuration. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Domain Distribution > Deployment Distribution Flow | Domain controller distributing deployments to server groups. | System Relations | `Technical Interaction` |
| WildFly > Domain Distribution > Server Group | Named collection of server instances sharing a profile and socket binding group. | System Structure | `Technical Element Set` |
| WildFly > Domain Distribution > Profile | Named configuration profile containing subsystem configurations. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/servers/` | Runtime state of managed servers. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Domain Distribution > `domain/data/` | Domain persistent runtime data. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Domain Distribution > `domain/log/` | Domain log storage. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Domain Distribution > `domain/tmp/` | Domain temporary data. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Domain Distribution > `domain/deployments/` | Domain deployment content. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Domain Distribution > `domain/configuration/domain_xml_history/` | Domain configuration change history. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Domain Distribution > `domain/configuration/host_xml_history/` | Host configuration change history. | System Structure | `Production Technical Object > Constitutive Technical Object` |
| WildFly > Domain Distribution > `domain/configuration/application-users.properties` | Application user credentials store. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/application-roles.properties` | Application user-to-role mapping. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/mgmt-users.properties` | Management user credentials store. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/mgmt-groups.properties` | Management group-to-role mapping. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Runtime | Executing WildFly server runtime. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > JVM | Java Virtual Machine executing WildFly. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > Java Process | Operating-system process containing the WildFly runtime. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > Standalone Server | Independently operated server runtime. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > Managed Server | Domain-managed server runtime. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > Process Controller | Process spawning and supervising server processes. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > Server Controller | Controller of an individual server runtime. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > JBoss Modules | Modular class-loading infrastructure. | Mechanism & Capability | `Mechanism & Capability > Technical Mechanism` |
| WildFly > Runtime > JBoss Modules > Module Loader | Loads modules and resolves module dependencies. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JBoss Modules > Module Dependency Graph | Graph of module visibility/dependency relations. | System Relations | `System Relations > Technical Dependency` |
| WildFly > Runtime > JBoss Modules > Module Class Loader | Class-loading mechanism associated with a module. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JBoss Modules > Automatic Dependencies | Dependencies automatically added to deployments (Jakarta EE APIs, Weld for CDI, etc.). | System Relations | `System Relations > Technical Dependency` |
| WildFly > Runtime > JBoss Modules > Class Loading Precedence | System Dependencies > User Dependencies > Local Resource > Inter-deployment Dependencies. | Mechanism & Capability | `Mechanism & Capability > Technical Mechanism` |
| WildFly > Runtime > Service Container | WildFly's modular service-management infrastructure (MSC). | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > Service Container > Service | Runtime service registered in the service container. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > Service Container > Service Dependency | Dependency between runtime services. | System Relations | `System Relations > Technical Dependency` |
| WildFly > Runtime > Service Container > Service Lifecycle | Installation, start, stop and removal of runtime services. | Lifecycle & Continuity | `Lifecycle & Continuity > Technical Lifecycle` |
| WildFly > Runtime > Service Container > Service Builder | Fluent API for building service definitions. | Mechanism & Capability | `Mechanism & Capability > Technical Mechanism` |
| WildFly > Runtime > Service Container > Service Controller | Manages service state transitions. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > Service Container > Service Registry | Registry of available services. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > Request Controller | Runtime mechanism for controlling request processing and concurrency. | Mechanism & Capability | `Mechanism & Capability > Technical Mechanism` |
| WildFly > Runtime > Request Flow | Listener to container to application request propagation. | System Relations | `Technical Interaction` |
| WildFly > Runtime > IO / Worker Infrastructure | Runtime I/O and worker-thread infrastructure. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Runtime > XNIO | Low-level non-blocking I/O and worker infrastructure used by WildFly components. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > XNIO > Worker | Thread worker for I/O processing. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime > XNIO > Channel | I/O channel abstraction. | System Structure | `Technical Interface` |
| WildFly > Runtime > Deployment Runtime | Runtime responsible for processing application deployments. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Management | Administrative control plane of WildFly. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Management > Management Model | Structured model representing configurable and runtime resources. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Management > Management Model > Root Resource | Root of the management-resource tree. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Management > Management Model > Resource | Addressable management resource. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Management > Management Model > Attribute | Named property of a management resource. | Requirements & Definition | `Requirements & Definition > Technical Parameter` |
| WildFly > Management > Management Model > Operation | Management operation executable against a resource. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > Management Model > Operation Catalog | Catalog of management operation definitions. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Management > Management Model > Capability | Named capability exposed or required by a management resource. | Mechanism & Capability | `Mechanism & Capability > Technical Capability` |
| WildFly > Management > Management Model > Capability Reference | Relationship connecting resources through capabilities. | System Relations | `System Relations > Technical Dependency` |
| WildFly > Management > Management Model > Capability Registry | Registry of exposed and required capabilities. | System Structure | `Constitutive Technical Object` |
| WildFly > Management > Management Model > Address | Ordered list of key/value pairs identifying a resource. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Management > Management Model > DMR | Detyped Model Representation — the wire format for management operations. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Management > Management Controller | Component interpreting and executing management operations. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Management > Operation Dispatch | Controller dispatching operations to runtime services. | System Relations | `Technical Interaction` |
| WildFly > Management > Management Controller > Operation Handler | Mechanism processing a management operation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Management > Management Controller > Configuration Persister | Mechanism persisting management-model changes into configuration. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Management > Management Controller > Model Controller | Controller implementing the management model. | System Structure | `Constitutive Technical Object` |
| WildFly > Management > Management Controller > Audit Logging | Recording of management operations for security and compliance. | Technical Control | `Technical Control > Technical Feedback` |
| WildFly > Management > Management Controller > Access Control | Role-based access control for management operations. | Technical Control | `Technical Control > Technical Security` |
| WildFly > Management > Management Interface | Network interface exposing management operations. | System Structure | `Production Technical System > Technical Interface` |
| WildFly > Management > HTTP Management Interface | HTTP-based management interface (port 9990). | System Structure | `Technical Interface` |
| WildFly > Management > Native Management Interface | Native management protocol interface (port 9999). | System Structure | `Technical Interface` |
| WildFly > Management > CLI | Command-line client for management operations. | Technical Operation | `Technical Operation > Technical Technique` |
| WildFly > Management > CLI > Command | Management command issued by an operator or automation. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > CLI > DMR Request | Detyped Model Representation request sent to the management controller. | System Relations | `System Relations > Technical Interaction` |
| WildFly > Management > CLI Actuation | Command line encoding operator intent into management operations on the controller. | Technical Operation | `Technical Interface & Actuation` |
| WildFly > Management > Console Actuation | Browser console encoding operator intent into management operations. | Technical Operation | `Technical Interface & Actuation` |
| WildFly > Management > Web Management Interface | Browser-based management interface (HAL). | System Structure | `Technical Interface` |
| WildFly > Management > JMX Management | JMX-based management integration. | System Structure | `Technical Interface` |
| WildFly > Management > JMX Management > MBean Server | Runtime registry and access point for MBeans. | System Structure | `Constitutive Technical Object` |
| WildFly > Management > Model Browser | Tool for exploring the management model tree. | Knowledge & Methodology | `Knowledge & Methodology > Technical Framework` |
| WildFly > Configuration | Runtime configuration structure. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Configuration > Extension | Configuration declaration loading a server extension module. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Configuration > Subsystem | Configurable server subsystem. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Configuration > Interface | Named network binding interface. | System Structure | `Technical Interface` |
| WildFly > Configuration > Socket Binding Group | Named collection of socket bindings. | System Structure | `Technical Element Set` |
| WildFly > Configuration > Socket Binding | Named network endpoint binding. | System Structure | `Technical Interface` |
| WildFly > Configuration > Outbound Socket Binding | Configuration for outbound network connectivity. | System Structure | `Technical Interface` |
| WildFly > Configuration > System Property | Runtime configuration parameter exposed as a system property. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Environment Variable | External runtime configuration parameter. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Path | Named filesystem path. | System Structure | `Constitutive Technical Object` |
| WildFly > Provisioning | Mechanism for constructing a WildFly installation from feature/layer definitions. | Technical Operation | `Technical Operation > Technical Practice` |
| WildFly > Provisioning > Galleon | Provisioning technology used to compose WildFly installations. | Knowledge & Methodology | `Knowledge & Methodology > Technical Framework` |
| WildFly > Provisioning > WildFly Galleon Feature Pack | Feature-pack definition supplying WildFly features. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > Feature | Provisionable unit in the feature-pack model. | System Structure | `Constitutive Technical Object` |
| WildFly > Provisioning > Layer | Named compositional server layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > Layer Dependency | Dependency between provisioning layers. | System Relations | `Technical Dependency` |
| WildFly > Provisioning > `core-server` layer | Base server layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `core-tools` layer | CLI/add-user/Elytron-tool support layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `web-server` layer | Web-server capability layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `datasources` layer | Datasource capability layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `jpa` layer | JPA capability layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `ejb` layer | Enterprise Beans capability layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `messaging-activemq` layer | Jakarta Messaging/ActiveMQ Artemis integration layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `jaxrs-server` layer | Jakarta REST, CDI/JPA and web-server composition layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `ee-core-profile-server` layer | Jakarta EE Core Profile server composition. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `cloud-server` layer | Cloud-oriented server composition layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `health` layer | Runtime health capability layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > `jdr` layer | Diagnostic-reporting capability layer. | System Structure | `Technical Element Set` |
| WildFly > Provisioning > WildFly Glow | Tooling to identify required Galleon Feature-packs and Layers from application binaries. | Knowledge & Methodology | `Knowledge & Methodology > Technical Framework` |
| WildFly > Provisioning > Prospero | Tool for installing and managing updates of WildFly servers. | Technical Operation | `Technical Operation > Technical Practice` |
| WildFly > Extensions | Extension modules that introduce management resources and runtime services. | System Structure | `Technical Element Set` |
| WildFly > Extensions > `org.wildfly.extension.undertow` | Extension implementing Undertow integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.messaging-activemq` | Extension implementing ActiveMQ Artemis integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.core-management` | Core-management extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.health` | Health subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.metrics` | Metrics subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.microprofile.config-smallrye` | MicroProfile Config extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.microprofile.health-smallrye` | MicroProfile Health extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.microprofile.metrics-smallrye` | MicroProfile Metrics extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.microprofile.fault-tolerance-smallrye` | MicroProfile Fault Tolerance extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.microprofile.reactive-messaging-smallrye` | MicroProfile Reactive Messaging extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.microprofile.openapi-smallrye` | MicroProfile OpenAPI extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.clustering.server` | Server-clustering integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.elytron` | Elytron security extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.elytron-oidc-client` | Elytron OIDC client extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.io` | I/O subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.remoting` | Remoting subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.transactions` | Transactions subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.batch.jberet` | Batch JBeret extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.bean-validation` | Bean Validation extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.datasources-agroal` | Agroal datasources extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.discovery` | Discovery subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.ee` | EE subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.weld` | CDI/Weld integration extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.ejb3` | EJB3 subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.jaxrs` | JAX-RS subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.jmx` | JMX subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.jpa` | JPA subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.logging` | Logging subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.mail` | Mail subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.naming` | Naming subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.pojo` | POJO subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.security.manager` | Security Manager extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.singleton` | Singleton subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.webservices` | Web Services subsystem extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.mod_cluster` | mod_cluster extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.opentelemetry` | OpenTelemetry extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.micrometer` | Micrometer extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.clustering.ejb` | Distributable EJB clustering extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.clustering.web` | Distributable Web clustering extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.clustering.singleton` | Singleton clustering extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.iiop-openjdk` | IIOP/OpenJDK ORB extension. | System Structure | `Constitutive Technical Object` |
| WildFly > Extensions > `org.wildfly.extension.jsf` | JSF extension (Mojarra). | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems | Collection of server subsystems. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > EE | Jakarta EE integration subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > EE > Default Bindings | Default Jakarta EE resource bindings. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > EE > Global Modules | Modules made available globally to deployments. | System Structure | `Technical Dependency` |
| WildFly > Subsystems > EE > Concurrency | Jakarta Concurrency integration. | Mechanism & Capability | `Technical Capability` |
| WildFly > Subsystems > EE > Managed Executor Service | Managed thread pool executor. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > EE > Managed Scheduled Executor Service | Managed scheduled executor. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > EE > Context Service | Managed context propagation service. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld | Contexts and Dependency Injection runtime integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > CDI / Weld > Bean Discovery | Mechanism for discovering CDI beans. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Dependency Injection | Mechanism for resolving and injecting dependencies. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Bean Archive | Archive containing CDI beans. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > CDI / Weld > `beans.xml` | CDI activation and configuration descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > CDI / Weld > Producer Method | Method producing CDI-injectable instances. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Interceptor | CDI interceptor binding and implementation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Decorator | CDI decorator for interface-based enhancement. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 | Jakarta Enterprise Beans runtime. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > EJB3 > Stateless Session Bean | Runtime representation of a stateless EJB. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > EJB3 > Stateful Session Bean | Runtime representation of a stateful EJB. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > EJB3 > Singleton Session Bean | Runtime representation of a singleton EJB. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > EJB3 > Message-Driven Bean | EJB receiving asynchronous messages. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > EJB3 > EJB Container | Runtime container for Enterprise Beans. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > EJB3 > EJB Pool | Pool of EJB instances. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > EJB3 > Remote Invocation | Remote EJB invocation mechanism. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > Timer Service | EJB timer runtime. | Mechanism & Capability | `Technical Capability` |
| WildFly > Subsystems > EJB3 > `ejb-jar.xml` | EJB deployment descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > EJB3 > `jboss-ejb3.xml` | WildFly-specific EJB deployment descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Naming | JNDI/naming infrastructure. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Naming > JNDI Namespace | Namespace containing bound application/server resources. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Naming > JNDI Binding | Individual name-to-resource binding. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Naming > Remote Naming | Remote naming access mechanism. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow | Web-server subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Server | Undertow server resource. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Server > Default Server | Default Undertow server instance. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Host | Virtual host resource. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Host > Default Host | Default virtual host. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > HTTP Listener | HTTP endpoint listener. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > HTTPS Listener | HTTPS/TLS endpoint listener. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > AJP Listener | AJP endpoint listener. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > Servlet Container | Servlet runtime container. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Servlet | Servlet runtime component. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Filter | Servlet filter component. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Listener | Servlet context listener. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > WebSocket | WebSocket protocol support. | Mechanism & Capability | `Technical Capability` |
| WildFly > Subsystems > Undertow > HTTP Invoker | HTTP-based invocation endpoint. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > Handler | Undertow request handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Buffer Pool | Managed buffer pool for I/O. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > RESTEasy | Jakarta REST implementation. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > RESTEasy > REST Endpoint | Application REST endpoint. | System Structure | `Technical Interface` |
| WildFly > Subsystems > RESTEasy > Message Body Reader | HTTP request-body deserialization component. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Message Body Writer | HTTP response-body serialization component. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Provider | REST content-processing provider. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > RESTEasy > Jackson Provider | Jackson JSON REST provider. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > RESTEasy > JSON-B Provider | JSON-B REST provider. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > RESTEasy > JSON-P Provider | JSON-P REST provider. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > RESTEasy > JAXB Provider | JAXB REST provider. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > RESTEasy > Exception Mapper | REST exception-to-response mapper. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Client | REST client runtime. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > RESTEasy > WebTarget | REST client invocation target. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > RESTEasy > Subresource | Sub-resource of a REST endpoint. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > RESTEasy > Request Filter | Client-side REST filter and interceptor. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Client Builder | Builder of REST client instances. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources | JDBC datasource subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Datasources > Datasource | Managed JDBC datasource. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Datasources > XA Datasource | XA-capable datasource. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Datasources > Connection Pool | Pool of database connections. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Datasources > JDBC Driver | JDBC driver module/resource. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Datasources > JNDI Binding | Datasource's JNDI resource binding. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Datasources > XA Recovery | XA transaction recovery configuration. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > Security Domain | Datasource security domain reference. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Datasources > Validation | Connection validation configuration. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > Pool Capacity | Configured connection pool size bounds. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Prefill | Connection pool prefill configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Subsystems > JPA | Jakarta Persistence integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > Persistence Unit | Deployment-defined persistence configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > JPA > Hibernate ORM | JPA persistence implementation. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > Entity Manager | Persistence runtime interface. | System Structure | `Technical Interface` |
| WildFly > Subsystems > JPA > Hibernate Cache | Persistence caching infrastructure. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > `persistence.xml` | JPA persistence-unit specification. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > JPA > Second-Level Cache | Shared persistence cache. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan | Distributed/local caching subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Infinispan > Cache Container | Logical collection of caches. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Infinispan > Local Cache | Single-node cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Infinispan > Distributed Cache | Distributed cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Infinispan > Replicated Cache | Replicated cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Infinispan > Invalidation Cache | Cache with invalidation semantics. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Infinispan > Persistent Cache | Cache with persistence store. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Infinispan > Cache Store | Persistence mechanism for cache entries. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Eviction | Cache entry eviction policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Expiration | Cache entry expiration policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Partition Handling | Partition handling configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Subsystems > Infinispan > Memory Store | Memory and off-heap store configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Subsystems > Infinispan > Indexing | Cache indexing configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Subsystems > JGroups | Cluster communication subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JGroups > Channel | Logical group-communication channel. | System Structure | `Technical Interface` |
| WildFly > Subsystems > JGroups > Protocol Stack | Ordered communication protocol stack. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > JGroups > Transport | Network transport used by a JGroups channel. | System Structure | `Technical Interface` |
| WildFly > Subsystems > JGroups > Protocol Properties | Communication protocol properties. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > Channel State | Group-communication channel state. | Technical Control | `Technical Feedback` |
| WildFly > Subsystems > JGroups > Receiver | Message receiver of a channel. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JGroups > Discovery Protocol | Node discovery protocol. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Failure Detection | Node failure detection mechanism. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > MERGE3 | Cluster merge protocol. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > FD_SOCK | Socket-based failure detection. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Clustering | Collection of clustering integrations. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Clustering > Cluster Node | WildFly server participating in a cluster. | System Structure | `Production Technical System` |
| WildFly > Subsystems > Clustering > Cluster Membership | Relation among participating server nodes. | System Relations | `Technical Interaction` |
| WildFly > Subsystems > Clustering > Distributed Session Management | Mechanism distributing web-session state. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Clustering > Session Replication Flow | Replication of session state across cluster nodes. | System Relations | `Technical Interaction` |
| WildFly > Subsystems > Distributable Web | Distributed web application/session infrastructure. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Distributable Web > Session Management | Management of distributable HTTP sessions. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Distributable Web > Session Affinity | Mechanism controlling session-node affinity. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Distributable Web > Session Replication | Mechanism replicating session state. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Distributable EJB | Distributed EJB state/management infrastructure. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Singleton | Cluster singleton service infrastructure. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Singleton > Singleton Service | Service active on one cluster member at a time. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Singleton > Singleton Policy | Policy for singleton election and failover. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions | Transaction-management subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > Transaction Manager | Coordinates transactions. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > Commit Coordination | Coordinator driving participants toward commit. | System Relations | `Technical Interaction` |
| WildFly > Subsystems > Transactions > Transaction | Unit of coordinated resource work. | Technical Operation | `Technical Activity` |
| WildFly > Subsystems > Transactions > XA Coordination | Two-phase transaction coordination mechanism. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Recovery | Transaction recovery mechanism. | Technical Control | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Object Store | Persistent transaction log storage. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > Timeout | Transaction timeout configuration. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Transactions > JTS | Java Transaction Service integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ | Jakarta Messaging / ActiveMQ Artemis integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server | Embedded Artemis messaging server. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address | Artemis message address. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Queue | JMS/Artemis queue. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Topic | JMS/Artemis topic. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connection Factory | JMS connection factory. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connector | Messaging network connector. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Remote Connector | Connector to external broker. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Acceptor | Messaging network acceptor. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Pooled Connection Factory | Managed pooled JMS connection factory. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > JMS Bridge | Bridge between JMS destinations. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Messaging-ActiveMQ > Security Setting | Messaging security configuration. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting | Per-address configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Messaging-ActiveMQ > Redelivery | Message redelivery configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Subsystems > Messaging-ActiveMQ > Security Roles | Messaging security roles. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Messaging-ActiveMQ > Divert | Message diversion rule. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Resource Adapters | Jakarta Connectors resource-adapter integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Resource Adapters > Resource Adapter | Deployable integration component. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Resource Adapters > Connection Definition | Resource-adapter connection definition. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Resource Adapters > `ra.xml` | Resource-adapter deployment descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Resource Adapters > `ironjacamar.xml` | IronJacamar-specific descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Resource Adapters > Admin Object | Resource-adapter administrative object. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Resource Adapters > Activation | Message-driven activation configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Security | Legacy security subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Security > Legacy Security Domain | Legacy authentication/authorization domain. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron | Unified WildFly security subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Security Domain | Elytron security-domain configuration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Security Realm | Source of identities/security attributes. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Identity Realm | Realm containing predefined identities. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Filesystem Realm | Realm backed by filesystem data. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > JDBC Realm | Realm backed by database queries. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > LDAP Realm | Realm backed by LDAP. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > JAAS Realm | Realm using JAAS login context. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Aggregate Realm | Composition of multiple realms. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Elytron > Caching Realm | Realm with identity caching. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Key Store | Cryptographic key-store definition. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Trust Store | Trusted-certificate store. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Credential Store | Secure credential-storage mechanism. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Authentication Factory | Mechanism assembling HTTP/SASL authentication. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > HTTP Authentication Factory | HTTP authentication mechanism factory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > SASL Authentication Factory | SASL authentication mechanism factory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Permission Mapper | Maps identities/roles to permissions. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Role Mapper | Maps roles between security contexts. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Principal Transformer | Transforms security principals. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Evidence Decoder | Decodes authentication evidence. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Realm Mapper | Maps realms across security domains. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > TLS Configuration | Centralized SSL/TLS configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Elytron > Cipher Suite | Configured TLS cipher suite. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Protocol | Configured TLS protocol version. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > OIDC Client | OpenID Connect client integration. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Web Services | Jakarta XML Web Services integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Web Services > JAX-WS Endpoint | SOAP web-service endpoint. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Web Services > WSDL | Service interface description. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > `jboss-webservices.xml` | JBossWS-specific deployment descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > Handler Chain | SOAP handler chain. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Batch JBeret | Jakarta Batch implementation. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Batch JBeret > Job | Batch job definition. | Technical Operation | `Technical Activity` |
| WildFly > Subsystems > Batch JBeret > Step | Batch processing step. | Technical Operation | `Technical Task` |
| WildFly > Subsystems > Batch JBeret > Job Repository | Persistent batch job state. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Mail | Jakarta Mail integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Mail > Mail Session | Configured mail-session resource. | System Structure | `Technical Interface` |
| WildFly > Subsystems > JMX | Java Management Extensions integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JMX > MBean | Managed Java object. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JMX > MBean Server | Runtime registry and access point for MBeans. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JMX > JMX Connector | Remote JMX access connector. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Logging | Server logging infrastructure. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Logging > Log Category | Named logging category. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Logging > Handler | Log output handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Logging > File Handler | File-based logging handler. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Logging > Console Handler | Console logging handler. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Logging > Periodic Rotating File Handler | Time-based rotating file handler. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Logging > Size Rotating File Handler | Size-based rotating file handler. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Logging > Async Handler | Asynchronous logging handler. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Logging > Formatter | Log-message formatting mechanism. | Mechanism & Capability | `Technical Technique` |
| WildFly > Subsystems > Logging > Log Level | Severity filtering threshold. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > IO | I/O subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > IO > Worker | Thread worker resource. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > IO > Buffer Pool | Managed buffer resource. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Remoting | Remote communication infrastructure. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Remoting > Connector | Remote communication connector. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Remoting > Endpoint | Remoting endpoint. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Remoting > HTTP Upgrade | HTTP-upgrade-based remoting. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Remoting > SASL Policy | SASL authentication policy for remoting. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Discovery | Service discovery infrastructure. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Discovery > Discovery Provider | Provider used to locate remote services. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Discovery > Static Discovery | Static list-based discovery. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Discovery > Aggregate Discovery | Composite discovery provider. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Mod_Cluster | Dynamic load-balancing integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Mod_Cluster > Proxy | Front-end load-balancing proxy. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Mod_Cluster > Advertise | Cluster advertisement mechanism. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Mod_Cluster > Balancer | Load-balancing policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Mod_Cluster > Node | Cluster node registration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Health | Runtime health-check subsystem. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Health Check | Runtime health evaluation. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Readiness Check | Kubernetes readiness probe. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Liveness Check | Kubernetes liveness probe. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Metrics | Runtime metrics infrastructure. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Metrics > Metric | Measured runtime property. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Gauge | Point-in-time metric. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Counter | Monotonically increasing metric. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Histogram | Distribution metric. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > MicroProfile | MicroProfile capability collection. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > MicroProfile > Config | Externalized configuration capability. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > MicroProfile > Health | Application health capability. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance | Fault-tolerance mechanisms. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > MicroProfile > Reactive Messaging | Reactive messaging capability. | Mechanism & Capability | `Technical Capability` |
| WildFly > Subsystems > MicroProfile > Metrics | Application/runtime metrics capability. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > MicroProfile > OpenAPI | API documentation generation. | Knowledge & Methodology | `Knowledge & Methodology > Technical Knowledge` |
| WildFly > Subsystems > MicroProfile > JWT | JWT authentication capability. | Technical Control | `Technical Security` |
| WildFly > Subsystems > SAR | Service Archive deployment subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > SAR > SAR Deployment | Service Archive deployment. | Technical Operation | `Technical Activity` |
| WildFly > Subsystems > SAR > MBean | MBean supplied by SAR deployment. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JSF | Jakarta Server Faces integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JSF > Mojarra | JSF implementation. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JSF > `faces-config.xml` | JSF configuration descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > POJO | Plain Old Java Object subsystem. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > POJO > POJO Deployment | POJO deployment unit. | Technical Operation | `Technical Activity` |
| WildFly > Subsystems > Bean Validation | Jakarta Bean Validation integration. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Bean Validation > Validator | Bean validation runtime. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Bean Validation > Constraint | Validation constraint definition. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Deployment Scanner | Filesystem-based deployment detection. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Deployment Scanner > Scan Interval | Deployment directory polling interval. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Deployment Scanner > Auto-deploy | Automatic deployment configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Deployment Scanner > Deployment Marker | Marker controlling scanner deployment state. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment | Application deployment system. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Deployment Unit | Unit submitted to WildFly for deployment. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Subdeployment | Nested deployment within an enterprise archive. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Resource Root | Resource root of a deployment unit. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Deployment Overlay | Overlay altering deployment content without repackaging. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Deployment Structure | Structural organization of deployment content. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Deployment > WAR | Web application deployment archive. | System Structure | `Production Technical Object` |
| WildFly > Deployment > JAR | Java/application module deployment archive. | System Structure | `Production Technical Object` |
| WildFly > Deployment > EAR | Enterprise application archive. | System Structure | `Production Technical Object` |
| WildFly > Deployment > RAR | Resource-adapter archive. | System Structure | `Production Technical Object` |
| WildFly > Deployment > SAR | Service Archive deployment. | System Structure | `Production Technical Object` |
| WildFly > Deployment > Deployment Descriptor | Declarative deployment configuration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` | Servlet deployment descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-web.xml` | WildFly web-deployment descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ejb-jar.xml` | EJB deployment descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-ejb3.xml` | WildFly EJB deployment descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `persistence.xml` | JPA persistence-unit specification. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `beans.xml` | CDI activation descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `application.xml` | Java EE application descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-app.xml` | JBoss application descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ra.xml` | Resource adapter descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ironjacamar.xml` | IronJacamar descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `application-client.xml` | Application client descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-client.xml` | JBoss application client descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-deployment-structure.xml` | Class-loading control descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Annotation | Annotation contributing deployment metadata. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Processor | Component processing deployment metadata/content. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Phase | Ordered stage of deployment processing. | Technical Operation | `Technical Activity` |
| WildFly > Deployment > Deployment Unit Processor | Processor transforming deployment state during deployment. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Service | Runtime service representing deployed application state. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Deployment Lifecycle | Deploy, undeploy, redeploy, replace and related transitions. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Scanner | Filesystem-based deployment detection mechanism. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Scanner > Deployment Marker | Marker controlling scanner deployment state. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker | Marker controlling scanner deployment state. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Application | Application deployed into WildFly. | System Structure | `Production Technical System` |
| WildFly > Deployment > Application > Module | Application module within an application deployment. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Component | Deployable application component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Servlet | Deployed servlet component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > CDI Bean | Deployed CDI component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > EJB | Deployed Enterprise Bean. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > REST Resource | Deployed REST resource. | System Structure | `Technical Interface` |
| WildFly > Deployment > Application > Persistence Unit | Deployed persistence unit. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > JNDI Resource | Application-visible resource binding. | System Structure | `Technical Interface` |
| WildFly > Deployment > Application > Security Domain Association | Application-to-security-domain relation. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Datasource Dependency | Application-to-datasource relation. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Messaging Dependency | Application-to-messaging resource relation. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Module Dependency | Application module dependency on WildFly module. | System Relations | `Technical Dependency` |
| WildFly > Network | Network-facing technical structure. | System Structure | `Constitutive Technical Object` |
| WildFly > Network > Public Interface | Interface exposed for application traffic. | System Structure | `Technical Interface` |
| WildFly > Network > Management Interface | Interface exposed for administration. | System Structure | `Technical Interface` |
| WildFly > Network > Unsecure Interface | Interface for unsecured traffic. | System Structure | `Technical Interface` |
| WildFly > Network > HTTP Endpoint | HTTP application endpoint. | System Structure | `Technical Interface` |
| WildFly > Network > HTTPS Endpoint | HTTPS/TLS application endpoint. | System Structure | `Technical Interface` |
| WildFly > Network > AJP Endpoint | AJP application endpoint. | System Structure | `Technical Interface` |
| WildFly > Network > Remoting Endpoint | Remote invocation endpoint. | System Structure | `Technical Interface` |
| WildFly > Network > Messaging Endpoint | Messaging endpoint. | System Structure | `Technical Interface` |
| WildFly > Network > JGroups Endpoint | Cluster communication endpoint. | System Structure | `Technical Interface` |
| WildFly > Network > TXN Recovery Endpoint | Transaction recovery endpoint. | System Structure | `Technical Interface` |
| WildFly > Network > TXN Status Manager Endpoint | Transaction status manager endpoint. | System Structure | `Technical Interface` |
| WildFly > Network > Management HTTP Endpoint | Management HTTP endpoint (9990). | System Structure | `Technical Interface` |
| WildFly > Network > Management Native Endpoint | Management native endpoint (9999). | System Structure | `Technical Interface` |
| WildFly > Network > Socket Binding | Named socket binding with port and interface. | Requirements & Definition | `Technical Configuration` |
| WildFly > Network > Socket Binding Group | Named collection of socket bindings. | System Structure | `Technical Element Set` |
| WildFly > Network > Port Offset | Offset applied to all socket bindings. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Outbound Socket Binding | Configuration for outbound connectivity. | Requirements & Definition | `Technical Configuration` |
| WildFly > Network > Client Mapping | Client-side address mapping for a socket binding. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Network > Interface Criteria | Address selection rules for a network interface. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Runtime Security | Runtime security structure. | System Structure | `Technical Element Set` |
| WildFly > Runtime Security > Authentication | Identity verification capability. | Mechanism & Capability | `Technical Capability` |
| WildFly > Runtime Security > Authorization | Permission-decision capability. | Mechanism & Capability | `Technical Capability` |
| WildFly > Runtime Security > TLS | Transport-security mechanism. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime Security > Credential Store | Secure credential storage. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Identity | Security identity representation. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Principal | Security principal representation. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Role | Authorization-role representation. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Permission | Authorization permission representation. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Security Event | Security-related runtime event. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Security > Audit Event | Auditable security event. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Security > Security Domain | Runtime security domain. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Realm | Runtime security realm. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > SSL Context | Runtime SSL/TLS context. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Control | Runtime control and observability structure. | Technical Control | `Technical Element Set` |
| WildFly > Runtime Control > Configuration State | Current server configuration state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime State | Current runtime state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime Metric | Quantitative runtime observation. | Technical Control | `Technical Performance` |
| WildFly > Runtime Control > Log Event | Recorded runtime event. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Health Result | Result of a health evaluation. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Diagnostic Report | Consolidated diagnostic information. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > JDR | JBoss Diagnostic Reporting mechanism. | Technical Control | `Technical Technique` |
| WildFly > Runtime Control > Audit Log | Management audit trail. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Server Log | Server runtime log. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > GC Log | Garbage collection log. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Thread Dump | Thread state snapshot. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Heap Dump | Memory state snapshot. | Technical Control | `Technical Feedback` |
| WildFly > Lifecycle | WildFly technical lifecycle. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Lifecycle > Provision | Construction of a WildFly installation. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Install | Installation of WildFly distribution. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure | Establishment of server configuration. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Start | Creation and activation of runtime services. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Boot | Initialization of server runtime. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Deploy | Introduction of application deployment into runtime. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Redeploy | Replacement/reprocessing of deployment. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Reload | Reinitialization of server configuration/runtime. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Shutdown | Controlled termination of server runtime. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Undeploy | Removal of application deployment. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Maintain | Continued corrective/preventive technical work. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Patch | Application of a server update/patch. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Upgrade | Transition to a newer WildFly version. | Lifecycle & Continuity | `Technical Evolution` |
| WildFly > Lifecycle > Migrate | Transition from an older technical configuration/version. | Lifecycle & Continuity | `Technical Evolution` |
| WildFly > Lifecycle > Retire | Removal of WildFly from technical service. | Lifecycle & Continuity | `Technical Obsolescence` |
| WildFly > Lifecycle > Rollback | Reversion to a previous configuration/version. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Backup | Preservation of configuration and data state. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Restore | Recovery from a preserved state. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > External Resources | External resources on which WildFly depends. | Technical Context | `Technical Resource` |
| WildFly > External Resources > CPU | Processing resource. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Memory | Runtime memory resource. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Filesystem | Persistent storage resource. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Network | Network resource. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Database | External persistence resource. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Message Broker | External messaging resource where remote messaging is configured. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Identity Provider | External identity source (e.g., Keycloak, LDAP). | Technical Context | `Technical Resource` |
| WildFly > External Resources > Certificate Authority | External trust infrastructure. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Load Balancer | External traffic-routing infrastructure (e.g., mod_cluster, HAProxy). | Technical Context | `Technical Resource` |
| WildFly > External Resources > JDK | External Java runtime. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Operating System | External OS facilities. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Container Runtime | Docker/Podman runtime where containerized. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes | Kubernetes orchestration environment. | Technical Context | `Technical Resource` |
| WildFly > External Resources > DNS | External name-resolution resource. | Technical Context | `Technical Resource` |
| WildFly > External Resources > NTP | External time-synchronization resource. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Storage Devices | External block and file storage devices. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Network Devices | External network devices. | Technical Context | `Technical Resource` |
| WildFly > Technical Standards | Standards implemented or integrated by WildFly. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta EE | Enterprise Java platform specification family implemented by WildFly. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Servlet | Web application programming model. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta REST | RESTful web-service specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Enterprise Beans | Enterprise component specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Persistence | Persistence specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Messaging | Messaging specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta CDI | Dependency-injection/context specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Transactions | Transaction specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Bean Validation | Bean validation specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Batch | Batch processing specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Concurrency | Concurrency utilities specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Connectors | Resource adapter specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Mail | Mail specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta WebSocket | WebSocket specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta JSON Binding | JSON-B specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta JSON Processing | JSON-P specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta XML Binding | JAXB specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta XML Web Services | JAX-WS specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JDBC | Java database-connectivity standard/API. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JNDI | Naming API/model. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JMX | Java management standard/API. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > HTTP | Application/network protocol. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > HTTPS | Secure HTTP protocol. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > TLS | Transport-security protocol. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > AJP | Apache JServ Protocol. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > WebSocket | WebSocket protocol. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OIDC | OpenID Connect. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OAuth 2.0 | Authorization framework. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > SAML | Security Assertion Markup Language. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JWT | JSON Web Token. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > MicroProfile | MicroProfile specification family. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OpenAPI | API description standard. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OpenTelemetry | Observability standard. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Security | Jakarta Security specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Authentication | Jakarta Authentication specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Authorization | Jakarta Authorization specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Faces | Jakarta Faces specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Server Pages | Jakarta Server Pages specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Expression Language | Jakarta Expression Language specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Interceptors | Jakarta Interceptors specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Dependency Injection | Jakarta Dependency Injection specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Activation | Jakarta Activation specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Management | Jakarta Management specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Deployment | Jakarta Deployment specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Annotations | Jakarta Annotations specification. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > SOAP | SOAP messaging protocol. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > XML-RPC | XML-RPC protocol. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Practices | Repeatable practices used to operate and maintain WildFly. | Knowledge & Methodology | `Technical Practice` |
| WildFly > Technical Practices > Provisioning | Reproducible server construction. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Configuration Management | Controlled management of server configuration. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Application Deployment | Controlled introduction of applications. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Monitoring | Observation of runtime state and performance. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Health Checking | Periodic/evaluative checking of runtime health. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Log Analysis | Analysis of generated runtime records. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Backup / Recovery | Preservation and restoration of required technical state. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Patching | Application of maintenance updates. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Capacity Management | Management of resource capacity and limits. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Security Hardening | Reduction of unnecessary exposure and configuration risk. | Technical Control | `Technical Security` |
| WildFly > Technical Practices > Performance Tuning | Optimization of runtime performance characteristics. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Thread Management | Configuration and tuning of thread pools. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Connection Pool Tuning | Optimization of datasource connection pools. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > JVM Tuning | Optimization of JVM heap, GC, and system properties. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Incident Management | Handling of runtime incidents. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Problem Management | Analysis of recurring technical problems. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Change Management | Controlled introduction of configuration changes. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Release Management | Planning and control of server releases. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Compliance Management | Assurance of regulatory and policy compliance. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Disaster Recovery | Restoration of service after catastrophic failure. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Cost Management | Management of operational resource costs. | Technical Control | `Technical Practice` |
| WildFly > Technical Dependencies | External and internal dependencies of WildFly. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > JVM | WildFly requires a compatible Java runtime. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Operating System | Runtime depends on OS facilities. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Filesystem | Runtime depends on filesystem access. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Network Stack | Runtime communication depends on network facilities. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Database | Datasource/JPA applications may depend on databases. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > External Services | Applications/server features may depend on external services. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Message Broker | Remote messaging depends on external broker. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Identity Provider | Security depends on external identity source. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Certificate Authority | TLS depends on external trust infrastructure. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Load Balancer | Cluster traffic routing depends on external LB. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Container Runtime | Containerized deployment depends on Docker/Podman. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Kubernetes API | Kubernetes deployment depends on API server. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > OS Packages | Runtime depends on operating-system packages. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > DNS | Name resolution depends on external DNS. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > NTP | Time synchronization depends on external NTP. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > External Monitoring | Observability depends on external monitoring and logging systems. | System Relations | `Technical Dependency` |
| WildFly > Technical Control | Control and observability structure of this WildFly instance. | Technical Control | `Technical Element Set` |
| WildFly > Technical Control > Verification Suite | Determination that configuration/deployment satisfies specified conditions. | Technical Control | `Verification` |
| WildFly > Technical Control > Validation Suite | Determination that the deployed system fulfills its intended technical purpose. | Technical Control | `Validation` |
| WildFly > Technical Control > Feedback | Logs, metrics, health and management state returned from runtime. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Failure | Runtime failure of a component/service/deployment. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Hazard | Condition capable of causing undesirable technical consequences. | Technical Control | `Technical Hazard` |
| WildFly > Technical Control > Risk | Possibility and consequence of an undesirable technical event. | Technical Control | `Technical Risk` |
| WildFly > Technical Control > Trade-off | Configuration/design compromise among competing technical properties. | Technical Control | `Technical Trade-off` |
| WildFly > Technical Control > Performance | Runtime response, throughput, resource consumption and related measurements. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Availability | Runtime uptime and accessibility. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Throughput | Requests processed per unit time. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Latency | Response time distribution. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Resource Utilization | CPU, memory, disk, network consumption. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Error Rate | Frequency of failed requests/operations. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Saturation | Degree of resource saturation. | Technical Control | `Technical Performance` |
| WildFly > Distribution > `bin/standalone.sh` > JVM Launch | Invocation of the Java runtime with standalone parameters. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/standalone.sh` > Classpath Setup | Construction of the runtime classpath from modules and boot libraries. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/standalone.sh` > Module Path Configuration | Configuration of the JBoss Modules path for the runtime. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/standalone.sh` > Main Class Invocation | Invocation of the WildFly bootstrap main class. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/domain.sh` > Host Controller Launch | Invocation of the Host Controller process. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/domain.sh` > Domain Controller Connection | Establishment of connection to the Domain Controller. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/jboss-cli.sh` > CLI Bootstrap | Initialization of the management CLI client. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/jboss-cli.sh` > Connection Establishment | Connection of the CLI to a management endpoint. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/add-user.sh` > User Creation | Interactive or batch creation of a management/application user. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/add-user.sh` > Credential Hashing | Hashing of the user password for storage. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/add-user.sh` > Property File Update | Update of the users/groups properties files. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/elytron-tool.sh` > Keystore Generation | Generation of a cryptographic keystore. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `bin/elytron-tool.sh` > Credential Store Generation | Generation of a credential store. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Distribution > `modules > Module > module.xml` > Dependencies Declaration | Declaration of module dependencies. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Distribution > `modules > Module > module.xml` > Resources Declaration | Declaration of module resources and exports. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Distribution > `modules > Module > module.xml` > Main Class Declaration | Declaration of the module main class. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Distribution > `modules > Module > module.xml` > Properties Declaration | Declaration of module properties and aliases. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Distribution > `standalone/configuration/standalone.xml` > Extensions Section | Declarations of loaded server extensions. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone.xml` > Management Section | Management interface and security-realm configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone.xml` > Profile Section | Subsystem configuration for the active profile. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone.xml` > Interfaces Section | Named interface declarations. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone.xml` > Socket Binding Groups Section | Named socket-binding groups. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone.xml` > Deployment Scanner Section | Deployment-scanner configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone.xml` > System Properties Section | System-property declarations. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone.xml` > Paths Section | Named filesystem path declarations. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Distribution > `standalone/configuration/standalone.xml` > Management Users | Management user/group references. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/domain.xml` > Profiles Section | Domain-wide subsystem profiles. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/domain.xml` > Server Groups Section | Named server groups. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/domain.xml` > Socket Binding Groups Section | Domain-wide socket-binding groups. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/domain.xml` > Hosts Section | Declared host controllers. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/domain.xml` > Server Configurations Section | Per-server configuration entries. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/host.xml` > Host Identity | Host controller identity. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/host.xml` > Domain Controller Reference | Reference to the domain controller. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/host.xml` > Local Server Configuration | Locally managed server configuration. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/host.xml` > JVM Configuration | JVM launch options per server. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/host.xml` > Interface Configuration | Host-level interface declarations. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > `domain/configuration/host.xml` > Socket Binding Group | Host-level socket-binding group. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > Host Controller > Registration | Registration of the host with the Domain Controller. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Domain Distribution > Host Controller > Process Supervision | Supervision of the managed server processes. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Domain Distribution > Host Controller > Configuration Propagation | Propagation of domain configuration to servers. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Domain Distribution > Domain Controller > Central Configuration | Central management of domain configuration. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Domain Distribution > Domain Controller > Server Group Management | Management of server groups across hosts. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Domain Distribution > Domain Controller > Deployment Distribution | Distribution of deployments to server groups. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Domain Distribution > Server Group > Profile Assignment | Association of a profile with a server group. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > Server Group > Socket Binding Group Assignment | Association of a socket-binding group with a server group. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Domain Distribution > Server Group > JVM Assignment | Association of JVM settings with a server group. | Requirements & Definition | `Requirements & Definition > Technical Configuration` |
| WildFly > Runtime > JVM > Heap | JVM heap memory regions. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime > JVM > Metaspace | JVM metaspace region. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime > JVM > Thread Stacks | Per-thread JVM stacks. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime > JVM > GC | Garbage collector subsystem. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JVM > Class Loader Subsystem | JVM class-loading subsystem. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JVM > JIT Compiler | Just-in-time compiler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JVM > JNI | Java Native Interface. | System Structure | `Technical Interface` |
| WildFly > Runtime > Java Process > Process Descriptor | OS process descriptor. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime > Java Process > Thread Pools | OS-level threads backing the runtime. | System Structure | `Technical Element Set` |
| WildFly > Runtime > Java Process > File Descriptors | Open file descriptors. | System Structure | `Technical Resource` |
| WildFly > Runtime > Java Process > Signal Handlers | Handlers for OS signals. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JBoss Modules > Module Repository | Repository of installed modules. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime > JBoss Modules > Module Index | Index of modules by name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime > JBoss Modules > Local Loader | Loader for local module resources. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JBoss Modules > Resource Loader | Loader for module resources. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JBoss Modules > Module Loader > Dependency Resolution | Algorithm resolving module dependencies. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JBoss Modules > Module Loader > Module Linking | Linking of modules into the runtime graph. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JBoss Modules > Module Class Loader > Parent Delegation | Delegation policy to parent class loader. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > JBoss Modules > Module Class Loader > Resource Visibility | Visibility rules for module resources. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > Service Container > Service Installation | Installation of services into the container. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Runtime > Service Container > Service Start | Start of installed services. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Runtime > Service Container > Service Stop | Stop of running services. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Runtime > Service Container > Service Removal | Removal of services from the container. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Runtime > Service Container > Dependency Resolution | Resolution of inter-service dependencies. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > Service Container > State Transition | Controlled service state transition. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > Service Container > Service Registry > Lookup | Lookup of services by name. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > Request Controller > Request Queue | Queue of pending requests. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime > Request Controller > Concurrency Control | Control of request concurrency. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > Request Controller > Backpressure | Backpressure handling. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > XNIO > Selector | I/O selector for readiness events. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > XNIO > Channel Listener | Listener for I/O channel events. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > XNIO > Worker Task Queue | Queue of tasks for worker threads. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime > XNIO > Worker Thread Pool | Pool of I/O worker threads. | System Structure | `Technical Element Set` |
| WildFly > Runtime > Deployment Runtime > Deployment Processor Chain | Chain of processors applied to deployments. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime > Deployment Runtime > Deployment Repository | Repository of deployed content realized through computation. | System Structure | `Production Virtual Technical Object` |
| WildFly > Runtime > Deployment Runtime > VFS | Virtual file system for deployment content realized through computation. | System Structure | `Production Virtual Technical Object` |
| WildFly > Runtime > Deployment Runtime > Runtime Stage | Runtime-stage deployment processing. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Management > Management Model > Root Resource > Host | Host-level management resource. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Management > Management Model > Root Resource > Server | Server-level management resource. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Management > Management Model > Root Resource > Deployment | Deployment management resource. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Management > Management Model > Resource > Address | Address identifying the resource. | Requirements & Definition | `Requirements & Definition > Technical Specification` |
| WildFly > Management > Management Model > Resource > Attributes | Attributes of the resource. | Requirements & Definition | `Requirements & Definition > Technical Parameter` |
| WildFly > Management > Management Model > Resource > Operations | Operations on the resource. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > Management Model > Resource > Children | Child resources. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Management > Management Model > Attribute > Value Type | Type of the attribute value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Management > Management Model > Attribute > Access Type | Read/write/read-only access. | Requirements & Definition | `Technical Parameter` |
| WildFly > Management > Management Model > Attribute > Default Value | Default attribute value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Management > Management Model > Operation > Operation Signature | Signature of the operation. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > Management Model > Operation > Operation Handler | Handler executing the operation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Management > Management Model > Operation > Result | Result returned by the operation. | Technical Control | `Technical Feedback` |
| WildFly > Management > Management Controller > Model Controller > Model Registration | Registration of resources in the model. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > Management Controller > Model Controller > Model Traversal | Traversal of the model tree. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > Management Controller > Model Controller > Model Validation | Validation of model changes. | Technical Control | `Verification` |
| WildFly > Management > Management Controller > Configuration Persister > XML Serialization | Serialization of model to XML. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Management > Management Controller > Configuration Persister > XML Deserialization | Deserialization of model from XML. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Management > Management Controller > Configuration Persister > Backup | Backup of persisted configuration. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Management > Management Controller > Audit Logging > Event Record | Recording of management events. | Technical Control | `Technical Feedback` |
| WildFly > Management > Management Controller > Audit Logging > Log Rotation | Rotation of audit logs. | Technical Control | `Technical Feedback` |
| WildFly > Management > Management Controller > Access Control > Role Assignment | Assignment of roles to identities. | Technical Control | `Technical Security` |
| WildFly > Management > Management Controller > Access Control > Permission Check | Check of operation permissions. | Technical Control | `Technical Security` |
| WildFly > Management > HTTP Management Interface > HTTP Endpoint | HTTP listener for management. | System Structure | `Technical Interface` |
| WildFly > Management > HTTP Management Interface > JSON Encoding | JSON encoding of DMR. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Management > HTTP Management Interface > Authentication | HTTP authentication for management. | Technical Control | `Technical Security` |
| WildFly > Management > HTTP Management Interface > Console | HAL management console. | System Structure | `Technical Interface` |
| WildFly > Management > Native Management Interface > Native Protocol | Native management protocol. | System Structure | `Technical Interface` |
| WildFly > Management > Native Management Interface > SASL Authentication | SASL-based authentication for native management. | Technical Control | `Technical Security` |
| WildFly > Management > CLI > Command > Connect Command | CLI connect command. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > CLI > Command > Read Command | CLI read-attribute/read-resource command. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > CLI > Command > Write Command | CLI write-attribute command. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > CLI > Command > Operation Command | CLI :operation command. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > CLI > Command > Deploy Command | CLI deploy/undeploy command. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > CLI > Command > Batch Command | CLI batch command. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > CLI > DMR Request > Request Encoding | Encoding of DMR request. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Management > CLI > DMR Request > Response Handling | Handling of DMR response. | Technical Control | `Technical Feedback` |
| WildFly > Management > Web Management Interface > HAL Console | HAL web console. | System Structure | `Technical Interface` |
| WildFly > Management > Web Management Interface > REST Endpoint | REST endpoint for management. | System Structure | `Technical Interface` |
| WildFly > Management > JMX Management > MBean Server > Registration | Registration of MBeans. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > JMX Management > MBean Server > Query | JMX query processing. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > JMX Management > MBean Server > Notification | JMX notification delivery. | Technical Control | `Technical Feedback` |
| WildFly > Management > Model Browser > Tree Navigation | Navigation of the management model tree. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Management > Model Browser > Attribute Inspection | Inspection of resource attributes. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Configuration > Extension > Module Reference | Reference to the extension module. | System Structure | `Production Technical System > Constitutive Technical Object` |
| WildFly > Configuration > Extension > Subsystem Registration | Registration of extension subsystems. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Configuration > Subsystem > Resource Definition | Definition of subsystem resources. | Requirements & Definition | `Technical Specification` |
| WildFly > Configuration > Subsystem > Operation Definition | Definition of subsystem operations. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Configuration > Subsystem > Capability Declaration | Declaration of subsystem capabilities. | Mechanism & Capability | `Technical Capability` |
| WildFly > Configuration > Interface > Inet Address | Inet address of the interface. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Socket Binding Group > Port Offset | Port offset applied to bindings. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Socket Binding > Port | Port number. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Socket Binding > Interface Reference | Interface associated with the binding. | System Structure | `Technical Interface` |
| WildFly > Configuration > Socket Binding > Fixed Port | Fixed-port flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Outbound Socket Binding > Remote Host | Remote host. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Outbound Socket Binding > Remote Port | Remote port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Outbound Socket Binding > Local Address | Local address used for outbound connections. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > System Property > Name | Property name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > System Property > Value | Property value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > System Property > Boot Time | Boot-time property flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Environment Variable > Name | Environment variable name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Environment Variable > Value | Environment variable value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Path > Name | Path name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Configuration > Path > Path Value | Absolute or relative path value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Server Architecture | Modular service-container architecture organizing subsystems, services, and deployments. | System Structure | `Technical Architecture` |
| WildFly > Server Architecture > Service Container Architecture | MSC-based runtime organizing services through dependencies and lifecycles. | System Structure | `Technical Architecture` |
| WildFly > Server Blueprints | Generative descriptions prescribing server construction, assembly, and deployment. | System Structure | `Technical Blueprint` |
| WildFly > Server Blueprints > Source Tree | Versioned source prescribing server construction. | System Structure | `Technical Blueprint` |
| WildFly > Server Blueprints > Feature-Pack Definitions | Galleon definitions prescribing installation composition. | System Structure | `Technical Blueprint` |
| WildFly > Modularity | Decomposability into independently provisionable modules and layers. | Mechanism & Capability | `Technical Property` |
| WildFly > Portability | Operability across operating systems and container runtimes. | Mechanism & Capability | `Technical Property` |
| WildFly > Reliability | Degree of sustained correct service under expected conditions. | Mechanism & Capability | `Technical Quality` |
| WildFly > Maintainability | Degree to which the server can be patched, upgraded, and reconfigured. | Mechanism & Capability | `Technical Quality` |
| WildFly > Provisioning > Galleon > Feature Pack Repository | Repository of feature packs. | System Structure | `Constitutive Technical Object` |
| WildFly > Provisioning > Galleon > Provisioning Plan | Plan describing features/layers to install. | Requirements & Definition | `Technical Specification` |
| WildFly > Provisioning > Galleon > Provisioning Execution | Execution of the provisioning plan. | Technical Operation | `Technical Activity` |
| WildFly > Provisioning > Feature > Feature Dependency | Dependency between features. | System Relations | `Technical Dependency` |
| WildFly > Provisioning > Feature > Feature Package | Package produced by a feature. | System Structure | `Constitutive Technical Object` |
| WildFly > Provisioning > Layer > Layer Dependency | Dependency between layers. | System Relations | `Technical Dependency` |
| WildFly > Provisioning > Layer > Layer Feature | Feature contained in a layer. | System Structure | `Constitutive Technical Object` |
| WildFly > Provisioning > Layer > Layer Package | Package contained in a layer. | System Structure | `Constitutive Technical Object` |
| WildFly > Provisioning > WildFly Glow > Binary Scan | Scan of an application binary. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Provisioning > WildFly Glow > Feature Pack Discovery | Discovery of required feature packs. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Provisioning > WildFly Glow > Layer Discovery | Discovery of required layers. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Provisioning > Prospero > Install | Installation of a WildFly server. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Provisioning > Prospero > Update | Update of an installed WildFly server. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Provisioning > Prospero > Rollback | Rollback of an update. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Provisioning > Feature-Pack Assembly | Technique for composing server installations from feature packs and layers. | Technical Operation | `Constitutive Technique` |
| WildFly > Provisioning > Layer Boundary | Criterion distinguishing provisioned layers from non-members. | System Structure | `Set Boundary` |
| WildFly > Provisioning > Layer Coherence | Shared Galleon feature-pack model integrating layers into one server. | System Structure | `Set Coherence` |
| WildFly > Provisioning > Layer Governance | Galleon provisioning rules governing layer composition. | System Structure | `Set Governance` |
| WildFly > Provisioning > Layer Realization | Jakarta EE runtime capability the layer composition collectively realizes. | System Structure | `Set Realization` |
| WildFly > Extensions > `org.wildfly.extension.undertow` > Subsystem Registration | Registration of the Undertow subsystem. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Extensions > `org.wildfly.extension.messaging-activemq` > Subsystem Registration | Registration of the ActiveMQ Artemis subsystem. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Extensions > `org.wildfly.extension.elytron` > Subsystem Registration | Registration of the Elytron subsystem. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Extensions > `org.wildfly.extension.io` > Subsystem Registration | Registration of the I/O subsystem. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Extensions > `org.wildfly.extension.transactions` > Subsystem Registration | Registration of the transactions subsystem. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Extensions > `org.wildfly.extension.batch.jberet` > Subsystem Registration | Registration of the Batch JBeret subsystem. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Extensions > `org.wildfly.extension.health` > Subsystem Registration | Registration of the health subsystem. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Extensions > `org.wildfly.extension.metrics` > Subsystem Registration | Registration of the metrics subsystem. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > EE > Default Bindings > Default Datasource Binding | Default datasource JNDI binding. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > EE > Default Bindings > Default JMS Binding | Default JMS connection factory binding. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > EE > Default Bindings > Default Concurrency Binding | Default concurrency utility binding. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > EE > Global Modules > Module Reference | Reference to a globally visible module. | System Structure | `Technical Dependency` |
| WildFly > Subsystems > EE > Concurrency > Managed Executor | Managed executor service. | Mechanism & Capability | `Technical Capability` |
| WildFly > Subsystems > EE > Concurrency > Managed Scheduled Executor | Managed scheduled executor service. | Mechanism & Capability | `Technical Capability` |
| WildFly > Subsystems > EE > Concurrency > Managed Thread Factory | Managed thread factory. | Mechanism & Capability | `Technical Capability` |
| WildFly > Subsystems > EE > Concurrency > Context Service | Managed context propagation service. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Bean Discovery > Archive Scanning | Scanning of deployment archives. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Bean Discovery > Bean Registration | Registration of discovered beans. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Dependency Injection > Injection Point Resolution | Resolution of injection points. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Dependency Injection > Instance Creation | Creation of injectable instances. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Interceptor > Binding | Interceptor binding. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Interceptor > Invocation | Interceptor invocation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > CDI / Weld > Decorator > Delegation | Decorator delegation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > Stateless Session Bean > Pooling | Pooling of stateless EJB instances. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > Stateless Session Bean > Invocation | Invocation of stateless EJB methods. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > EJB3 > Stateful Session Bean > Passivation | Passivation of stateful EJB state. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > Stateful Session Bean > Activation | Activation of stateful EJB state. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > Singleton Session Bean > Locking | Locking of singleton EJB. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > Singleton Session Bean > Startup | Startup of singleton EJB. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > EJB3 > Message-Driven Bean > Message Consumption | Consumption of messages by MDB. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > Message-Driven Bean > Pooling | Pooling of MDB instances. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > EJB Container > Lifecycle Callbacks | Lifecycle callback invocations. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > EJB3 > EJB Container > Security Interceptors | Security interceptors. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > EJB Container > Transaction Interceptors | Transaction interceptors. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > EJB Pool > Pool Sizing | Pool size configuration. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > EJB3 > EJB Pool > Instance Creation | Creation of pooled EJB instances. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > EJB3 > Remote Invocation > Serialization | Serialization of remote invocations. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > Remote Invocation > Transport | Transport of remote invocations. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > EJB3 > Timer Service > Timer Creation | Creation of EJB timers. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > EJB3 > Timer Service > Timer Expiry | Expiry of EJB timers. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > EJB3 > Timer Service > Timer Persistence | Persistence of EJB timers. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Naming > JNDI Namespace > Root Context | Root JNDI context. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Naming > JNDI Namespace > java: Context | java: namespace. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Naming > JNDI Namespace > java:comp Context | java:comp namespace. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Naming > JNDI Namespace > java:module Context | java:module namespace. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Naming > JNDI Namespace > java:app Context | java:app namespace. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Naming > JNDI Namespace > java:global Context | java:global namespace. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Naming > JNDI Binding > Lookup | Lookup of bound resources. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Naming > JNDI Binding > Bind | Binding of resources. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Naming > JNDI Binding > Unbind | Unbinding of resources. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Naming > Remote Naming > Remote Lookup | Remote JNDI lookup. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Server > Default Server > HTTP Listener | Default HTTP listener. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > Server > Default Server > AJP Listener | Default AJP listener. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > Server > Default Server > HTTPS Listener | Default HTTPS listener. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > Host > Default Host > Virtual Host | Default virtual host. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Host > Default Host > Access Log | Access log for the virtual host. | Technical Control | `Technical Feedback` |
| WildFly > Subsystems > Undertow > Servlet Container > Servlet Lifecycle | Servlet lifecycle management. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > Undertow > Servlet Container > Session Management | HTTP session management. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Servlet Container > Filter Chain | Servlet filter chain. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Servlet > Init | Servlet initialization. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Undertow > Servlet > Service | Servlet request servicing. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Undertow > Servlet > Destroy | Servlet destruction. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Undertow > Filter > Init | Filter initialization. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Undertow > Filter > DoFilter | Filter chain execution. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Undertow > Listener > Context Initialized | Context initialization callback. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Undertow > Listener > Context Destroyed | Context destruction callback. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Undertow > WebSocket > Handshake | WebSocket handshake. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > WebSocket > Frame Handling | WebSocket frame handling. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > HTTP Invoker > EJB Invocation | HTTP-based EJB invocation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Request Handling | Request handling by the handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Buffer Pool > Buffer Allocation | Allocation of buffers. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Buffer Pool > Buffer Release | Release of buffers. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > REST Endpoint > Request Handling | Handling of REST requests. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > RESTEasy > REST Endpoint > Response Generation | Generation of REST responses. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > RESTEasy > Message Body Reader > Deserialization | Deserialization of request bodies. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Message Body Writer > Serialization | Serialization of response bodies. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Provider > Registration | Registration of providers. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > RESTEasy > Provider > Selection | Selection of providers for a request. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Jackson Provider > JSON Serialization | Jackson JSON serialization. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Jackson Provider > JSON Deserialization | Jackson JSON deserialization. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > JSON-B Provider > JSON-B Serialization | JSON-B serialization. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > JSON-P Provider > JSON-P Serialization | JSON-P serialization. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > JAXB Provider > XML Serialization | JAXB XML serialization. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Exception Mapper > Exception Mapping | Mapping of exceptions to responses. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Client > Request Build | Building of client requests. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > RESTEasy > Client > Response Handling | Handling of client responses. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Datasources > Datasource > Connection Acquisition | Acquisition of a database connection. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > Datasource > Connection Release | Release of a database connection. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > XA Datasource > XA Start | XA transaction start. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > XA Datasource > XA End | XA transaction end. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > XA Datasource > XA Prepare | XA prepare phase. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > XA Datasource > XA Commit | XA commit phase. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > XA Datasource > XA Rollback | XA rollback phase. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > Connection Pool > Pool Sizing | Connection pool sizing. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Connection Pool > Validation | Connection validation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > Connection Pool > Eviction | Connection eviction. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > JDBC Driver > Driver Loading | Loading of the JDBC driver. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > JNDI Binding > Datasource Lookup | Lookup of the datasource via JNDI. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > XA Recovery > Recovery Scan | Scan of in-doubt XA transactions. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > XA Recovery > Recovery Commit | Recovery commit of XA transactions. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > Security Domain > Credential Retrieval | Retrieval of datasource credentials. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > Validation > Validation Query | Execution of the validation query. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Persistence Unit > Entity Manager Factory | Creation of the entity manager factory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Persistence Unit > Entity Manager | Creation of entity managers. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate ORM > Session Factory | Hibernate session factory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate ORM > Dialect Resolution | Resolution of the SQL dialect. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Entity Manager > Persistence Context | Persistence context management. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Entity Manager > Flush | Flush of persistence context. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate Cache > First-Level Cache | First-level (session) cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > Hibernate Cache > Second-Level Cache | Second-level (shared) cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > Hibernate Cache > Query Cache | Query result cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > Second-Level Cache > Cache Region | Cache region. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > Second-Level Cache > Cache Concurrency Strategy | Concurrency strategy for the cache. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Cache Container > Default Cache | Default cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Infinispan > Cache Container > Named Cache | Named cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Infinispan > Local Cache > Storage | Local cache storage. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Infinispan > Distributed Cache > Ownership | Ownership of cache entries. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Distributed Cache > Rebalancing | Rebalancing of cache entries. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Replicated Cache > Replication | Replication of cache entries. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Invalidation Cache > Invalidation | Invalidation of cache entries. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Persistent Cache > Cache Store | Persistent cache store. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Infinispan > Cache Store > Write | Write to the cache store. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Cache Store > Read | Read from the cache store. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Eviction > Eviction Policy | Cache eviction policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Expiration > Lifespan | Cache entry lifespan. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Infinispan > Expiration > Max Idle | Cache entry max idle time. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > Channel > Send | Send on a JGroups channel. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Channel > Receive | Receive on a JGroups channel. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Protocol Stack > Transport Protocol | Transport protocol in the stack. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Protocol Stack > Discovery Protocol | Discovery protocol in the stack. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Protocol Stack > Failure Detection Protocol | Failure detection protocol in the stack. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Protocol Stack > Ordering Protocol | Message ordering protocol. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Protocol Stack > Fragmentation Protocol | Message fragmentation protocol. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Protocol Stack > Flow Control Protocol | Flow control protocol. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Transport > TCP | TCP transport. | System Structure | `Technical Interface` |
| WildFly > Subsystems > JGroups > Transport > UDP | UDP transport. | System Structure | `Technical Interface` |
| WildFly > Subsystems > JGroups > Discovery Protocol > Multicast Discovery | Multicast-based discovery. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Failure Detection > Heartbeat | Heartbeat-based failure detection. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > MERGE3 > Merge Coordination | Coordination of cluster merges. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > FD_SOCK > Socket Monitoring | Socket-based monitoring for failures. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Clustering > Cluster Node > Node Identity | Identity of the cluster node. | System Structure | `Production Technical System` |
| WildFly > Subsystems > Clustering > Cluster Node > Node State | State of the cluster node. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Clustering > Cluster Membership > Join | Join of a node to the cluster. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Clustering > Cluster Membership > Leave | Leave of a node from the cluster. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Clustering > Cluster Membership > View Change | Cluster view change. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Clustering > Distributed Session Management > Session Replication | Replication of sessions. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Clustering > Distributed Session Management > Session Failover | Failover of sessions. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Distributable Web > Session Management > Session Creation | Creation of HTTP sessions. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Distributable Web > Session Management > Session Invalidation | Invalidation of HTTP sessions. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Distributable Web > Session Affinity > Node Affinity | Node affinity for sessions. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Distributable Web > Session Replication > Replication Trigger | Trigger for session replication. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Distributable Web > Session Replication > Replication Transport | Transport for session replication. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Singleton > Singleton Service > Election | Election of the singleton provider. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Singleton > Singleton Service > Failover | Failover of the singleton service. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Singleton > Singleton Policy > Simple Policy | Simple singleton policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Singleton > Singleton Policy > Random Policy | Random singleton policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Transaction Manager > Begin | Begin of a transaction. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Transactions > Transaction Manager > Commit | Commit of a transaction. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Transactions > Transaction Manager > Rollback | Rollback of a transaction. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Transactions > Transaction Manager > Suspend | Suspension of a transaction. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Transactions > Transaction Manager > Resume | Resumption of a transaction. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Transactions > Transaction > Enlist Resource | Enlistment of a resource. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Transactions > Transaction > Delist Resource | Delisting of a resource. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Transactions > XA Coordination > Prepare | Prepare phase of two-phase commit. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > XA Coordination > Commit | Commit phase of two-phase commit. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > XA Coordination > Rollback | Rollback phase of two-phase commit. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Recovery > Recovery Manager | Transaction recovery manager. | Technical Control | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Recovery > Recovery Scan | Periodic recovery scan. | Technical Control | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Object Store > Transaction Log | Persistent transaction log. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > Object Store > Log Write | Write to the transaction log. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Object Store > Log Read | Read from the transaction log. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Timeout > Transaction Timeout | Transaction timeout value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Transactions > Timeout > Reaper | Transaction reaper. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > JTS > ORB Integration | ORB integration for JTS. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Acceptors | Broker acceptors. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Connectors | Broker connectors. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Security Settings | Broker security settings. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Persistence | Message persistence. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Journal | Message journal. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address > Address Settings | Settings for the address. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address > Bindings | Bindings of the address. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Queue > Consumers | Queue consumers. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Queue > Messages | Queued messages. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Topic > Subscriptions | Topic subscriptions. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Topic > Messages | Topic messages. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connection Factory > Connection Creation | Creation of JMS connections. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connection Factory > Session Creation | Creation of JMS sessions. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connector > Transport | Transport of the connector. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Messaging-ActiveMQ > Remote Connector > Remote Transport | Transport to the remote broker. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Messaging-ActiveMQ > Acceptor > Transport | Transport of the acceptor. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Messaging-ActiveMQ > Pooled Connection Factory > Pooling | Pooling of JMS connections. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Messaging-ActiveMQ > JMS Bridge > Source | Bridge source. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > JMS Bridge > Target | Bridge target. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > JMS Bridge > Quality of Service | QoS of the bridge. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Security Setting > Authentication | Messaging authentication. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Messaging-ActiveMQ > Security Setting > Authorization | Messaging authorization. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting > Dead Letter Address | Dead-letter address. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting > Expiry Address | Expiry address. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting > Max Size Bytes | Maximum address size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Divert > Routing | Routing of diverted messages. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Resource Adapters > Resource Adapter > Deployment | Deployment of the resource adapter. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Resource Adapters > Resource Adapter > Connection Factory | Connection factory provided by the adapter. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Resource Adapters > Resource Adapter > Admin Object | Admin object provided by the adapter. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Resource Adapters > Connection Definition > Managed Connection Factory | Managed connection factory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Resource Adapters > Connection Definition > Connection Factory Interface | Connection factory interface. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Resource Adapters > Connection Definition > Connection Interface | Connection interface. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Resource Adapters > Admin Object > Admin Object Interface | Admin object interface. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Resource Adapters > Admin Object > Admin Object Properties | Admin object properties. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Resource Adapters > Activation > Activation Spec | Activation specification. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Resource Adapters > Activation > Message Listener | Message listener. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Security > Legacy Security Domain > Authentication | Legacy authentication. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Security > Legacy Security Domain > Authorization | Legacy authorization. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Security > Legacy Security Domain > Mapping | Legacy role mapping. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Elytron > Security Domain > Default Realm | Default realm of the domain. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Security Domain > Role Decoder | Role decoder. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Security Domain > Permission Mapper | Permission mapper. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Security Realm > Identity Acquisition | Acquisition of identities. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Security Realm > Credential Acquisition | Acquisition of credentials. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Identity Realm > Identity Store | Identity store. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Filesystem Realm > Filesystem Store | Filesystem-backed identity store. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > JDBC Realm > SQL Query | SQL query for identity retrieval. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Elytron > LDAP Realm > LDAP Search | LDAP search for identities. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > JAAS Realm > Login Context | JAAS login context. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Aggregate Realm > Realm Composition | Composition of multiple realms. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Caching Realm > Cache | Identity cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Key Store > Key Entry | Key entry. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Key Store > Certificate Entry | Certificate entry. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Trust Store > Trusted Certificate | Trusted certificate. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Credential Store > Credential Entry | Credential entry. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Authentication Factory > Mechanism Selection | Selection of authentication mechanism. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > HTTP Authentication Factory > HTTP Mechanism | HTTP authentication mechanism. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > SASL Authentication Factory > SASL Mechanism | SASL authentication mechanism. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Permission Mapper > Permission Assignment | Assignment of permissions. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Role Mapper > Role Transformation | Transformation of roles. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Principal Transformer > Principal Transformation | Transformation of principals. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Evidence Decoder > Evidence Decoding | Decoding of evidence. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Realm Mapper > Realm Mapping | Mapping across realms. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > TLS Configuration > Protocol Selection | Selection of TLS protocol. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > TLS Configuration > Cipher Suite Selection | Selection of cipher suites. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > TLS Configuration > Certificate Revocation | Certificate revocation checking. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Cipher Suite > Cipher Name | Cipher suite name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Protocol > Protocol Name | TLS protocol name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > OIDC Client > Token Validation | Validation of OIDC tokens. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > OIDC Client > Token Refresh | Refresh of OIDC tokens. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Web Services > JAX-WS Endpoint > Request Handling | Handling of SOAP requests. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Web Services > JAX-WS Endpoint > Response Generation | Generation of SOAP responses. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Web Services > WSDL > Service Definition | Service definition in WSDL. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > WSDL > Binding Definition | Binding definition in WSDL. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > WSDL > Port Type Definition | Port-type definition in WSDL. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > WSDL > Message Definition | Message definition in WSDL. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > Handler Chain > Handler Invocation | Invocation of SOAP handlers. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Batch JBeret > Job > Job Instance | Batch job instance. | Technical Operation | `Technical Activity` |
| WildFly > Subsystems > Batch JBeret > Job > Job Execution | Batch job execution. | Technical Operation | `Technical Activity` |
| WildFly > Subsystems > Batch JBeret > Step > Step Execution | Batch step execution. | Technical Operation | `Technical Task` |
| WildFly > Subsystems > Batch JBeret > Step > Chunk Processing | Chunk processing. | Technical Operation | `Technical Task` |
| WildFly > Subsystems > Batch JBeret > Step > Batchlet Processing | Batchlet processing. | Technical Operation | `Technical Task` |
| WildFly > Subsystems > Batch JBeret > Job Repository > Job State | Persistent job state. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Batch JBeret > Job Repository > Step State | Persistent step state. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Mail > Mail Session > Session Properties | Mail session properties. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mail > Mail Session > Credentials | Mail session credentials. | Technical Control | `Technical Security` |
| WildFly > Subsystems > JMX > MBean > Attribute | MBean attribute. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JMX > MBean > Operation | MBean operation. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JMX > MBean > Notification | MBean notification. | Technical Control | `Technical Feedback` |
| WildFly > Subsystems > JMX > MBean Server > Registration | MBean registration. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JMX > MBean Server > Query | MBean query. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JMX > JMX Connector > Remote Access | Remote JMX access. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Logging > Log Category > Level | Log level of the category. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Log Category > Handlers | Handlers attached to the category. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Logging > Log Category > Use Parent Handlers | Use-parent-handlers flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Handler > Level | Handler level. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Handler > Formatter | Handler formatter. | Mechanism & Capability | `Technical Technique` |
| WildFly > Subsystems > Logging > Handler > Filter | Handler filter. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Logging > File Handler > File Path | File path of the handler. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > File Handler > Append | Append flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Console Handler > Target | Console target (stdout/stderr). | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Periodic Rotating File Handler > Suffix | Rotation suffix pattern. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Size Rotating File Handler > Max File Size | Maximum file size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Size Rotating File Handler > Max Backup Index | Maximum backup index. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Async Handler > Queue Length | Async queue length. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Async Handler > Overflow Action | Overflow action. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Formatter > Pattern | Format pattern. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Log Level > Severity | Severity threshold. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > IO > Worker > Task Queue | Worker task queue. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > IO > Worker > Thread Pool | Worker thread pool. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > IO > Buffer Pool > Buffer Size | Buffer size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > IO > Buffer Pool > Buffer Count | Buffer count. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Remoting > Connector > Transport | Transport of the connector. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Remoting > Connector > Security | Security of the connector. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Remoting > Endpoint > Listener | Listener of the endpoint. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Remoting > HTTP Upgrade > Upgrade Handshake | HTTP upgrade handshake. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Remoting > SASL Policy > Mechanism Selection | Selection of SASL mechanisms. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Discovery > Discovery Provider > Static Provider | Static discovery provider. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Discovery > Discovery Provider > Aggregate Provider | Aggregate discovery provider. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Discovery > Static Discovery > Address List | Static address list. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Discovery > Aggregate Discovery > Provider Composition | Composition of providers. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Mod_Cluster > Proxy > Balancer | Balancer of the proxy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Mod_Cluster > Proxy > Node Registration | Node registration with the proxy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Mod_Cluster > Advertise > Multicast | Multicast advertisement. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Mod_Cluster > Advertise > Socket Advertisement | Socket advertisement. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Mod_Cluster > Balancer > Load Factor | Load factor. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mod_Cluster > Balancer > Sticky Session | Sticky-session configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Mod_Cluster > Node > Node Registration | Registration of the node. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Health > Health Check > UP | UP health result. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Health Check > DOWN | DOWN health result. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Readiness Check > READY | READY readiness result. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Readiness Check > NOT_READY | NOT_READY readiness result. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Liveness Check > ALIVE | ALIVE liveness result. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Liveness Check > DEAD | DEAD liveness result. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Metrics > Metric > Value | Metric value. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Metric > Unit | Metric unit. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Gauge > Reading | Gauge reading. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Counter > Increment | Counter increment. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Counter > Decrement | Counter decrement. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Histogram > Buckets | Histogram buckets. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > MicroProfile > Config > Property Source | Source of configuration properties. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > MicroProfile > Config > Property Value | Value of a configuration property. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Health > Health Check | Application health check. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Retry | Retry policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Timeout | Timeout policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Circuit Breaker | Circuit-breaker policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Bulkhead | Bulkhead policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Fallback | Fallback policy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > MicroProfile > Reactive Messaging > Channel | Reactive messaging channel. | System Structure | `Technical Interface` |
| WildFly > Subsystems > MicroProfile > Reactive Messaging > Connector | Reactive messaging connector. | System Structure | `Technical Interface` |
| WildFly > Subsystems > MicroProfile > Metrics > Metric | Application metric. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > MicroProfile > OpenAPI > Document | OpenAPI document. | Knowledge & Methodology | `Knowledge & Methodology > Technical Knowledge` |
| WildFly > Subsystems > MicroProfile > OpenAPI > Operation | OpenAPI operation. | Knowledge & Methodology | `Knowledge & Methodology > Technical Knowledge` |
| WildFly > Subsystems > MicroProfile > JWT > Token | JWT token. | Technical Control | `Technical Security` |
| WildFly > Subsystems > MicroProfile > JWT > Claim | JWT claim. | Technical Control | `Technical Security` |
| WildFly > Subsystems > SAR > SAR Deployment > Deployment | Deployment of a service archive. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > SAR > SAR Deployment > Undeployment | Undeployment of a service archive. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > SAR > MBean > Registration | Registration of the SAR MBean. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JSF > Mojarra > Lifecycle | JSF lifecycle. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > JSF > Mojarra > Component Tree | JSF component tree. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JSF > Mojarra > Renderer | JSF renderer. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JSF > `faces-config.xml` > Navigation Rules | JSF navigation rules. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > JSF > `faces-config.xml` > Managed Beans | JSF managed beans. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > POJO > POJO Deployment > Deployment | POJO deployment. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > POJO > POJO Deployment > Undeployment | POJO undeployment. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > Bean Validation > Validator > Validation | Bean validation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Bean Validation > Constraint > Definition | Constraint definition. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Bean Validation > Constraint > Violation | Constraint violation. | Technical Control | `Technical Feedback` |
| WildFly > Subsystems > Deployment Scanner > Scan | Scan of the deployment directory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Deployment Scanner > Deploy | Deployment of detected content. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Deployment Scanner > Undeploy | Undeployment of removed content. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Deployment Scanner > Scan Interval > Interval Value | Scan interval value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Deployment Scanner > Auto-deploy > Enabled | Auto-deploy enabled flag. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Deployment Scanner > Deployment Marker > Marker Type | Type of deployment marker. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Unit > Archive | Archive submitted for deployment. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Deployment Unit > Descriptor | Descriptor of the deployment unit. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Unit > Structure | Structure of the deployment unit. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > WEB-INF | WEB-INF directory. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > META-INF | META-INF directory. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > Static Content | Static web content. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > Classes | Compiled classes. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > Libraries | Bundled libraries. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > JAR > META-INF | META-INF directory. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > JAR > Classes | Compiled classes. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > JAR > Resources | Packaged resources. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > EAR > Modules | Application modules. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > EAR > Libraries | Bundled libraries. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > EAR > META-INF | META-INF directory. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > RAR > META-INF | META-INF directory. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > RAR > Native Libraries | Native libraries. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > SAR > META-INF | META-INF directory. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > SAR > Service Classes | Service classes. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Deployment Descriptor > Element | Declarative element in the descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Descriptor > Schema Reference | Schema reference for the descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Servlet Declaration | Servlet declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Filter Declaration | Filter declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Listener Declaration | Listener declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Welcome File | Welcome file declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Security Constraint | Security constraint. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-web.xml` > Context Root | Context root. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-web.xml` > Virtual Host | Virtual host. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ejb-jar.xml` > Session Bean | Session bean declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ejb-jar.xml` > Message-Driven Bean | Message-driven bean declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ejb-jar.xml` > Assembly Descriptor | Assembly descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `persistence.xml` > Persistence Unit | Persistence unit declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `persistence.xml` > Class List | List of persistence classes. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `persistence.xml` > Properties | Persistence properties. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `beans.xml` > Discovery Mode | Bean discovery mode. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `beans.xml` > Interceptors | Interceptor declarations. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `beans.xml` > Decorators | Decorator declarations. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `application.xml` > Module | Application module declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `application.xml` > Security Role | Security role declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-app.xml` > Class Loading | Class-loading configuration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ra.xml` > Resource Adapter | Resource-adapter declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ra.xml` > Connection Definition | Connection-definition declaration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ironjacamar.xml` > Connection Pool | Connection-pool configuration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `application-client.xml` > Client Descriptor | Client descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-client.xml` > Client Descriptor | JBoss client descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-deployment-structure.xml` > Dependencies | Deployment dependencies. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-deployment-structure.xml` > Exclusions | Deployment exclusions. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-deployment-structure.xml` > Local Resources | Local resource declarations. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Annotation > Class Annotation | Class-level annotation. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Annotation > Method Annotation | Method-level annotation. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Annotation > Field Annotation | Field-level annotation. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Processor > Parse | Parse phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Processor > Register | Register phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Processor > Deploy | Deploy phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > STRUCTURE | STRUCTURE phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > PARSE | PARSE phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > REGISTER | REGISTER phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > DEPENDENCIES | DEPENDENCIES phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > CONFIGURE_MODULE | CONFIGURE_MODULE phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > POST_MODULE | POST_MODULE phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > INSTALL | INSTALL phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > CLEANUP | CLEANUP phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Unit Processor > Transform | Transformation of deployment state. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Service > Registration | Registration of the deployment service. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Deployment Service > Start | Start of the deployment service. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Deployment Service > Stop | Stop of the deployment service. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Deployment Lifecycle > Deploy | Deploy transition. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Lifecycle > Undeploy | Undeploy transition. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Lifecycle > Redeploy | Redeploy transition. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Lifecycle > Replace | Replace transition. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Lifecycle > Explode | Explode transition. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Scanner > Scan | Scan of the deployment directory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Scanner > Deploy | Deployment of detected content. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Scanner > Undeploy | Undeployment of removed content. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Marker > `.dodeploy` | Marker for deployment. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker > `.undeploy` | Marker for undeployment. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker > `.deployed` | Marker for successful deployment. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker > `.failed` | Marker for failed deployment. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker > `.isdeploying` | Marker for in-progress deployment. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker > `.skipdeploy` | Marker for skipped deployment. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Application > Module > Classes | Application module classes. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Module > Resources | Application module resources. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Module > Libraries | Application module libraries. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Module > Class Loader | Application module class loader. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Application > Component > Servlet Component | Servlet component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Component > EJB Component | EJB component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Component > CDI Component | CDI component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Component > REST Component | REST component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Component > WebSocket Component | WebSocket component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Servlet > Lifecycle | Servlet lifecycle. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > Servlet > Request Handling | Servlet request handling. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Application > Servlet > Session Handling | Servlet session handling. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Application > CDI Bean > Scope | CDI bean scope. | Requirements & Definition | `Technical Parameter` |
| WildFly > Deployment > Application > CDI Bean > Lifecycle | CDI bean lifecycle. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > CDI Bean > Injection | CDI bean injection. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Application > EJB > Lifecycle | EJB lifecycle. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > EJB > Business Interface | EJB business interface. | System Structure | `Technical Interface` |
| WildFly > Deployment > Application > EJB > Transaction Attribute | EJB transaction attribute. | Requirements & Definition | `Technical Parameter` |
| WildFly > Deployment > Application > EJB > Security Role | EJB security role. | Technical Control | `Technical Security` |
| WildFly > Deployment > Application > REST Resource > Resource Method | REST resource method. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Application > REST Resource > Path | REST resource path. | Requirements & Definition | `Technical Parameter` |
| WildFly > Deployment > Application > REST Resource > Media Type | REST media type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Deployment > Application > Persistence Unit > Entity | JPA entity. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Persistence Unit > Entity Manager Factory | Entity manager factory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Application > Persistence Unit > Data Source | Data source reference. | System Structure | `Technical Interface` |
| WildFly > Deployment > Application > JNDI Resource > Resource Reference | Resource reference. | System Structure | `Technical Interface` |
| WildFly > Deployment > Application > JNDI Resource > Environment Entry | Environment entry. | System Structure | `Technical Interface` |
| WildFly > Deployment > Application > Security Domain Association > Domain Reference | Reference to the security domain. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Datasource Dependency > Datasource Reference | Reference to the datasource. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Messaging Dependency > Connection Factory Reference | Reference to the connection factory. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Messaging Dependency > Destination Reference | Reference to the destination. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Module Dependency > Module Reference | Reference to a WildFly module. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Module Dependency > Export | Export of module packages. | System Relations | `Technical Dependency` |
| WildFly > Network > Public Interface > Inet Address | Public interface inet address. | System Structure | `Technical Interface` |
| WildFly > Network > Management Interface > Inet Address | Management interface inet address. | System Structure | `Technical Interface` |
| WildFly > Network > Unsecure Interface > Inet Address | Unsecure interface inet address. | System Structure | `Technical Interface` |
| WildFly > Network > HTTP Endpoint > Port | HTTP port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > HTTPS Endpoint > Port | HTTPS port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > HTTPS Endpoint > Certificate | TLS certificate. | System Structure | `Constitutive Technical Object` |
| WildFly > Network > AJP Endpoint > Port | AJP port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Remoting Endpoint > Port | Remoting port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Messaging Endpoint > Port | Messaging port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > JGroups Endpoint > Port | JGroups port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > TXN Recovery Endpoint > Port | TXN recovery port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > TXN Status Manager Endpoint > Port | TXN status manager port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Management HTTP Endpoint > Port | Management HTTP port (9990). | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Management Native Endpoint > Port | Management native port (9999). | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Socket Binding > Name | Socket binding name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Socket Binding > Port | Socket binding port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Socket Binding > Interface | Socket binding interface. | System Structure | `Technical Interface` |
| WildFly > Network > Socket Binding Group > Default Interface | Default interface of the group. | System Structure | `Technical Interface` |
| WildFly > Network > Socket Binding Group > Port Offset | Port offset of the group. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Port Offset > Offset Value | Port offset value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Outbound Socket Binding > Remote Host | Remote host. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Outbound Socket Binding > Remote Port | Remote port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Runtime Security > Authentication > Mechanism | Authentication mechanism. | Mechanism & Capability | `Technical Capability` |
| WildFly > Runtime Security > Authentication > Credential | Credential used for authentication. | Technical Control | `Technical Security` |
| WildFly > Runtime Security > Authorization > Policy | Authorization policy. | Mechanism & Capability | `Technical Capability` |
| WildFly > Runtime Security > Authorization > Decision | Authorization decision. | Technical Control | `Technical Security` |
| WildFly > Runtime Security > TLS > Handshake | TLS handshake. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime Security > TLS > Cipher Negotiation | Cipher negotiation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime Security > TLS > Certificate Validation | Certificate validation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime Security > Credential Store > Entry | Credential entry. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Credential Store > Alias | Credential alias. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Identity > Name | Identity name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Identity > Attributes | Identity attributes. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Principal > Name | Principal name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Role > Name | Role name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Permission > Name | Permission name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Permission > Actions | Permission actions. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Security Event > Type | Type of security event. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Security > Security Event > Timestamp | Timestamp of the event. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Security > Audit Event > Category | Category of audit event. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Security > Audit Event > Outcome | Outcome of the audited event. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Security > Security Domain > Name | Security domain name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Security Domain > Realm | Realm of the security domain. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Realm > Name | Realm name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Realm > Identity Store | Identity store of the realm. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > SSL Context > Protocol | TLS protocol of the context. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > SSL Context > Cipher Suites | Cipher suites of the context. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Control > Configuration State > Active Profile | Active configuration profile. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Configuration State > Running Mode | Running mode (standalone/domain). | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Configuration State > Server State | Server state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime State > Started | Started state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime State > Stopped | Stopped state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime State > Reload Required | Reload-required state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime State > Restart Required | Restart-required state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime Metric > Name | Metric name. | Technical Control | `Technical Performance` |
| WildFly > Runtime Control > Runtime Metric > Value | Metric value. | Technical Control | `Technical Performance` |
| WildFly > Runtime Control > Runtime Metric > Unit | Metric unit. | Technical Control | `Technical Performance` |
| WildFly > Runtime Control > Log Event > Level | Log event level. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Log Event > Message | Log event message. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Log Event > Timestamp | Log event timestamp. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Health Result > Status | Health status. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Health Result > Check | Health check name. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Diagnostic Report > Section | Diagnostic report section. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > JDR > Collection | Diagnostic data collection. | Technical Control | `Technical Technique` |
| WildFly > Runtime Control > JDR > Report | Diagnostic report generation. | Technical Control | `Technical Technique` |
| WildFly > Runtime Control > Audit Log > Entry | Audit log entry. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Server Log > Entry | Server log entry. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > GC Log > Entry | GC log entry. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Thread Dump > Thread | Thread in the dump. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Heap Dump > Heap Region | Heap region in the dump. | Technical Control | `Technical Feedback` |
| WildFly > Lifecycle > Provision > Provisioning Plan | Plan for provisioning. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Provision > Provisioning Execution | Execution of provisioning. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Install > Distribution Extraction | Extraction of the distribution. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Install > File Placement | Placement of installation files. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure > Profile Selection | Selection of the configuration profile. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure > Subsystem Configuration | Configuration of subsystems. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure > Interface Configuration | Configuration of network interfaces. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure > Socket Binding Configuration | Configuration of socket bindings. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure > Security Configuration | Configuration of security domains. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Start > Service Container Start | Start of the service container. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Start > Subsystem Start | Start of subsystems. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Start > Deployment Start | Start of deployments. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Boot > Bootstrap | Bootstrap phase. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Boot > Configuration Load | Loading of configuration. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Boot > Service Installation | Installation of services. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Deploy > Deployment Processing | Processing of the deployment. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Deploy > Deployment Start | Start of the deployed application. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Redeploy > Undeploy | Undeploy phase of redeploy. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Redeploy > Deploy | Deploy phase of redeploy. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Reload > Stop | Stop phase of reload. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Reload > Start | Start phase of reload. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Shutdown > Graceful Shutdown | Graceful shutdown. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Shutdown > Forced Shutdown | Forced shutdown. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Undeploy > Deployment Stop | Stop of the deployed application. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Undeploy > Content Removal | Removal of deployment content. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Maintain > Corrective Maintenance | Corrective maintenance. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Maintain > Preventive Maintenance | Preventive maintenance. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Patch > Patch Application | Application of the patch. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Patch > Patch Verification | Verification of the patch. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Upgrade > Version Change | Change to a new version. | Lifecycle & Continuity | `Technical Evolution` |
| WildFly > Lifecycle > Upgrade > Configuration Migration | Migration of configuration. | Lifecycle & Continuity | `Technical Evolution` |
| WildFly > Lifecycle > Migrate > Configuration Transformation | Transformation of configuration. | Lifecycle & Continuity | `Technical Evolution` |
| WildFly > Lifecycle > Migrate > Application Migration | Migration of applications. | Lifecycle & Continuity | `Technical Evolution` |
| WildFly > Lifecycle > Retire > Decommissioning | Decommissioning of the server. | Lifecycle & Continuity | `Technical Obsolescence` |
| WildFly > Lifecycle > Retire > Data Archival | Archival of data. | Lifecycle & Continuity | `Technical Obsolescence` |
| WildFly > Lifecycle > Rollback > Version Reversion | Reversion to a previous version. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Rollback > Configuration Reversion | Reversion of configuration. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Backup > Configuration Backup | Backup of configuration. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Backup > Data Backup | Backup of data. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Backup > Deployment Backup | Backup of deployments. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Restore > Configuration Restore | Restore of configuration. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Restore > Data Restore | Restore of data. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Restore > Deployment Restore | Restore of deployments. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > External Resources > CPU > Core | CPU core. | Technical Context | `Technical Resource` |
| WildFly > External Resources > CPU > Frequency | CPU frequency. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Memory > Heap | Runtime heap. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Memory > Off-Heap | Off-heap memory. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Filesystem > Disk | Disk storage. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Filesystem > Files | Files accessed by the runtime. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Network > Bandwidth | Network bandwidth. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Network > Latency | Network latency. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Database > Connection | Database connection. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Database > Storage | Database storage. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Message Broker > Queue | Broker queue. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Message Broker > Topic | Broker topic. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Identity Provider > Realm | Identity provider realm. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Identity Provider > Endpoint | Identity provider endpoint. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Certificate Authority > Root Certificate | Root certificate. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Certificate Authority > CRL | Certificate revocation list. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Load Balancer > Virtual IP | Virtual IP of the load balancer. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Load Balancer > Pool | Backend pool. | Technical Context | `Technical Resource` |
| WildFly > External Resources > JDK > JRE | Java runtime. | Technical Context | `Technical Resource` |
| WildFly > External Resources > JDK > JDK Tools | JDK tools. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Operating System > Kernel | OS kernel. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Operating System > Libraries | OS libraries. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Container Runtime > Image | Container image. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Container Runtime > Volume | Container volume. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes > Namespace | Kubernetes namespace. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes > Service | Kubernetes service. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes > ConfigMap | Kubernetes ConfigMap. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes > Secret | Kubernetes Secret. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes > Ingress | Kubernetes Ingress. | Technical Context | `Technical Resource` |
| WildFly > Technical Standards > Jakarta EE > Profile | Jakarta EE profile. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Servlet > Version | Jakarta Servlet version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta REST > Version | Jakarta REST version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Enterprise Beans > Version | Jakarta EJB version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Persistence > Version | Jakarta Persistence version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Messaging > Version | Jakarta Messaging version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta CDI > Version | Jakarta CDI version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Transactions > Version | Jakarta Transactions version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Bean Validation > Version | Jakarta Bean Validation version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Batch > Version | Jakarta Batch version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Concurrency > Version | Jakarta Concurrency version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Connectors > Version | Jakarta Connectors version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Mail > Version | Jakarta Mail version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta WebSocket > Version | Jakarta WebSocket version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta JSON Binding > Version | Jakarta JSON-B version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta JSON Processing > Version | Jakarta JSON-P version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta XML Binding > Version | Jakarta XML Binding version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta XML Web Services > Version | Jakarta XML WS version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JDBC > Version | JDBC version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JNDI > Version | JNDI version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JMX > Version | JMX version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > HTTP > Version | HTTP version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > HTTPS > Version | HTTPS version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > TLS > Version | TLS version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > AJP > Version | AJP version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > WebSocket > Version | WebSocket version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OIDC > Version | OIDC version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OAuth 2.0 > Version | OAuth 2.0 version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > SAML > Version | SAML version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JWT > Version | JWT version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > MicroProfile > Version | MicroProfile version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OpenAPI > Version | OpenAPI version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OpenTelemetry > Version | OpenTelemetry version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Practices > Provisioning > Plan Definition | Definition of the provisioning plan. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Provisioning > Execution | Execution of provisioning. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Configuration Management > Change Control | Control of configuration changes. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Configuration Management > Version Control | Versioning of configuration. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Application Deployment > Release Process | Process of releasing applications. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Application Deployment > Rollback Process | Process of rolling back applications. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Monitoring > Metric Collection | Collection of runtime metrics. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Monitoring > Alerting | Alerting on monitored conditions. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Health Checking > Probe Scheduling | Scheduling of health probes. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Health Checking > Result Handling | Handling of health-check results. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Log Analysis > Collection | Collection of log events. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Log Analysis > Interpretation | Interpretation of log events. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Backup / Recovery > Backup Scheduling | Scheduling of backups. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Backup / Recovery > Restore Procedure | Procedure for restore. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Patching > Patch Planning | Planning of patches. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Patching > Patch Application | Application of patches. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Capacity Management > Sizing | Capacity sizing. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Capacity Management > Scaling | Capacity scaling. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Security Hardening > Exposure Reduction | Reduction of exposure. | Technical Control | `Technical Security` |
| WildFly > Technical Practices > Security Hardening > Configuration Hardening | Hardening of configuration. | Technical Control | `Technical Security` |
| WildFly > Technical Practices > Performance Tuning > JVM Tuning | Tuning of the JVM. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Performance Tuning > Subsystem Tuning | Tuning of subsystems. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Thread Management > Pool Sizing | Sizing of thread pools. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Thread Management > Queue Sizing | Sizing of thread queues. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Connection Pool Tuning > Pool Sizing | Sizing of connection pools. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Connection Pool Tuning > Timeout Tuning | Tuning of connection timeouts. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > JVM Tuning > Heap Sizing | Sizing of the JVM heap. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > JVM Tuning > GC Selection | Selection of the garbage collector. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > JVM Tuning > System Property Tuning | Tuning of system properties. | Technical Control | `Technical Practice` |
| WildFly > Technical Dependencies > JVM > Java Version | Required Java version. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > JVM > JVM Options | Required JVM options. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Operating System > OS Family | Required OS family. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Operating System > OS Libraries | Required OS libraries. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Filesystem > Paths | Required filesystem paths. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Filesystem > Permissions | Required filesystem permissions. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Network Stack > Protocols | Required network protocols. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Network Stack > Ports | Required network ports. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Database > JDBC Driver | Required JDBC driver. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Database > Schema | Required database schema. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > External Services > Endpoint | Required external endpoint. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > External Services > Credentials | Required external credentials. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Message Broker > Broker Endpoint | Required broker endpoint. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Message Broker > Destinations | Required destinations. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Identity Provider > IdP Endpoint | Required IdP endpoint. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Identity Provider > Client Credentials | Required client credentials. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Certificate Authority > Root Certificate | Required root certificate. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Certificate Authority > Trust Chain | Required trust chain. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Load Balancer > Frontend Address | Required frontend address. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Load Balancer > Backend Pool | Required backend pool. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Container Runtime > Image | Required container image. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Container Runtime > Volume | Required container volume. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Kubernetes API > API Server | Required API server. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Kubernetes API > Service Account | Required service account. | System Relations | `Technical Dependency` |
| WildFly > Technical Control > Verification Suite > Unit Test | Unit test execution. | Technical Control | `Verification` |
| WildFly > Technical Control > Verification Suite > Integration Test | Integration test execution. | Technical Control | `Verification` |
| WildFly > Technical Control > Verification Suite > Static Analysis | Static analysis. | Technical Control | `Verification` |
| WildFly > Technical Control > Verification Suite > Inspection | Dimensional inspection. | Technical Control | `Verification` |
| WildFly > Technical Control > Validation Suite > User Validation | User validation. | Technical Control | `Validation` |
| WildFly > Technical Control > Validation Suite > Operational Trial | Operational trial. | Technical Control | `Validation` |
| WildFly > Technical Control > Validation Suite > Acceptance Test | Acceptance test. | Technical Control | `Validation` |
| WildFly > Technical Control > Feedback > Log Feedback | Log-based feedback. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Feedback > Metric Feedback | Metric-based feedback. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Feedback > Health Feedback | Health-based feedback. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Feedback > Management State Feedback | Management-state feedback. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Failure > Crash | Crash failure. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Failure > Hang | Hang failure. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Failure > Deadlock | Deadlock failure. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Failure > Memory Leak | Memory-leak failure. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Failure > Thread Leak | Thread-leak failure. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Hazard > Exposed Voltage | Exposed-voltage hazard. | Technical Control | `Technical Hazard` |
| WildFly > Technical Control > Hazard > Thermal Runaway | Thermal-runaway hazard. | Technical Control | `Technical Hazard` |
| WildFly > Technical Control > Hazard > Race Condition | Race-condition hazard. | Technical Control | `Technical Hazard` |
| WildFly > Technical Control > Hazard > Resource Exhaustion | Resource-exhaustion hazard. | Technical Control | `Technical Hazard` |
| WildFly > Technical Control > Risk > Availability Risk | Availability risk. | Technical Control | `Technical Risk` |
| WildFly > Technical Control > Risk > Integrity Risk | Integrity risk. | Technical Control | `Technical Risk` |
| WildFly > Technical Control > Risk > Confidentiality Risk | Confidentiality risk. | Technical Control | `Technical Risk` |
| WildFly > Technical Control > Risk > Compliance Risk | Compliance risk. | Technical Control | `Technical Risk` |
| WildFly > Technical Control > Trade-off > Performance vs Energy | Performance-vs-energy trade-off. | Technical Control | `Technical Trade-off` |
| WildFly > Technical Control > Trade-off > Flexibility vs Complexity | Flexibility-vs-complexity trade-off. | Technical Control | `Technical Trade-off` |
| WildFly > Technical Control > Trade-off > Availability vs Consistency | Availability-vs-consistency trade-off. | Technical Control | `Technical Trade-off` |
| WildFly > Technical Control > Trade-off > Security vs Usability | Security-vs-usability trade-off. | Technical Control | `Technical Trade-off` |
| WildFly > Technical Control > Performance > Response Time | Response-time measurement. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Performance > Throughput | Throughput measurement. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Performance > Resource Consumption | Resource-consumption measurement. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Availability > Uptime | Uptime measurement. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Availability > Downtime | Downtime measurement. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Throughput > Requests per Second | Requests-per-second metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Throughput > Bytes per Second | Bytes-per-second metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Latency > p50 | Median latency. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Latency > p95 | 95th-percentile latency. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Latency > p99 | 99th-percentile latency. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Resource Utilization > CPU Utilization | CPU-utilization metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Resource Utilization > Memory Utilization | Memory-utilization metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Resource Utilization > Disk Utilization | Disk-utilization metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Resource Utilization > Network Utilization | Network-utilization metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Error Rate > HTTP 5xx Rate | HTTP 5xx error rate. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Error Rate > Exception Rate | Exception rate. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Error Rate > Timeout Rate | Timeout rate. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Saturation > Thread Pool Saturation | Thread-pool saturation. | Technical Control | `Technical Performance` |
| WildFly > Technical Control > Saturation > Connection Pool Saturation | Connection-pool saturation. | Technical Control | `Technical Performance` |
| WildFly > Technical Control > Saturation > Heap Saturation | Heap saturation. | Technical Control | `Technical Performance` |
| WildFly > Technical Control > Saturation > Queue Saturation | Queue saturation. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Undertow > Server > Default Server > Listener | Endpoint listeners of the default server. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Undertow > Server > Default Server > Listener > HTTP Listener | HTTP listener of the default server. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > Server > Default Server > Listener > HTTPS Listener | HTTPS listener of the default server. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > Server > Default Server > Listener > AJP Listener | AJP listener of the default server. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > Server > Default Server > Host | Virtual-host resources of the default server. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Server > Default Server > Host > Default Host | Default host of the default server. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Server > Default Server > Host > Default Host > Location | Filesystem location served by the host. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Server > Default Server > Host > Default Host > Access Log | Access log of the default host. | Technical Control | `Technical Feedback` |
| WildFly > Subsystems > Undertow > Server > Default Server > Host > Default Host > Filter | HTTP filter of the default host. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Server > Default Server > Host > Default Host > Handler | Request handler of the default host. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Servlet Container > Deployment | Deployment of a web application. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > Undertow > Servlet Container > Servlet Context | Servlet context. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > Servlet Container > Session Manager | HTTP session manager. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Servlet Container > Session Cookie | Session cookie configuration. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Undertow > Servlet Container > Session Timeout | Session timeout. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Undertow > Servlet Container > Welcome File | Welcome file handling. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Undertow > Servlet Container > MIME Mapping | MIME-type mapping. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Undertow > Servlet Container > Error Page | Error-page mapping. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Undertow > Servlet Container > Security Constraint | Security constraint enforcement. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Undertow > Servlet Container > Servlet Mapping | Servlet URL mapping. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Undertow > Servlet Container > Filter Mapping | Filter URL mapping. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Undertow > Servlet Container > Listener Registration | Listener registration. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Undertow > WebSocket > Endpoint | WebSocket endpoint. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Undertow > WebSocket > Session | WebSocket session. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Undertow > WebSocket > Message Encoder | WebSocket message encoder. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > WebSocket > Message Decoder | WebSocket message decoder. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > File Handler | Static file handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Directory Handler | Directory listing handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Resource Handler | Classpath resource handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Redirect Handler | Redirect handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Proxy Handler | Reverse proxy handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Access Log Handler | Access log handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Graceful Shutdown Handler | Graceful shutdown handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Request Limiting Handler | Request limiting handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Blocking Handler | Blocking handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Compression Handler | Compression handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Byte-range Handler | Byte-range handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Undertow > Handler > Path Template Handler | Path-template handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > REST Endpoint > Path Template | REST path template. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > RESTEasy > REST Endpoint > HTTP Method | HTTP method binding. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > RESTEasy > REST Endpoint > Consumes | Consumed media types. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > RESTEasy > REST Endpoint > Produces | Produced media types. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > RESTEasy > REST Endpoint > Parameter Binding | REST parameter binding. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > RESTEasy > REST Endpoint > Request Context | REST request context. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > RESTEasy > REST Endpoint > Response Builder | REST response builder. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > REST Endpoint > Exception Mapping | REST exception mapping. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Provider > Filter | REST filter provider. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Provider > Interceptor | REST interceptor provider. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Provider > Context Resolver | REST context resolver. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Provider > Param Converter | REST parameter converter. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Provider > Feature | REST feature provider. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > RESTEasy > Provider > Dynamic Feature | REST dynamic feature provider. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > Datasource > Connection URL | JDBC connection URL. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Datasource > User Name | Datasource user name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Datasource > Password | Datasource password. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Datasources > Datasource > Driver Class | JDBC driver class. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Datasource > Transaction Isolation | Transaction isolation level. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Datasource > Pool Configuration | Connection-pool configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Datasources > Datasource > Validation Configuration | Connection-validation configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Datasources > Datasource > Timeout Configuration | Connection-timeout configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Datasources > Datasource > Statement Cache | Statement cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Datasources > XA Datasource > XA Properties | XA properties. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Datasources > XA Datasource > Recovery Credentials | XA recovery credentials. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Datasources > XA Datasource > Recovery Username | XA recovery username. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Datasources > XA Datasource > Recovery Password | XA recovery password. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Datasources > Connection Pool > Initial Size | Initial pool size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Connection Pool > Minimum Size | Minimum pool size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Connection Pool > Maximum Size | Maximum pool size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Connection Pool > Idle Timeout | Idle timeout. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Connection Pool > Leak Detection | Leak detection. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > Connection Pool > Flush Strategy | Pool flush strategy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > JDBC Driver > Module Name | JDBC driver module name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > JDBC Driver > Class Name | JDBC driver class name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > JDBC Driver > XA Datasource Class | XA datasource class. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > JNDI Binding > Binding Name | JNDI binding name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > XA Recovery > Recovery Module | XA recovery module. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Datasources > Security Domain > Domain Name | Security domain name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Validation > Check Valid Connection SQL | Validation SQL. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Validation > Validate on Match | Validate-on-match flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Validation > Background Validation | Background-validation flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Datasources > Validation > Background Validation Millis | Background-validation interval. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JPA > Persistence Unit > Name | Persistence unit name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JPA > Persistence Unit > Transaction Type | Persistence-unit transaction type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JPA > Persistence Unit > Provider | Persistence provider. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JPA > Persistence Unit > Data Source | Persistence-unit datasource. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JPA > Persistence Unit > Managed Classes | Managed persistence classes. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > JPA > Persistence Unit > Mapping File | ORM mapping file. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > JPA > Persistence Unit > Properties | Persistence-unit properties. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JPA > Hibernate ORM > Dialect | Hibernate SQL dialect. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JPA > Hibernate ORM > JDBC Bind | JDBC parameter binding. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate ORM > Statement Preparation | SQL statement preparation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate ORM > Result Set Handling | Result-set handling. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate ORM > Entity Persister | Entity persister. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate ORM > Collection Persister | Collection persister. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate ORM > Identifier Generator | Identifier generator. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate ORM > Dirty Checking | Dirty checking. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate ORM > Flush Mode | Flush mode. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JPA > Entity Manager > Persist | Entity persist operation. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JPA > Entity Manager > Merge | Entity merge operation. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JPA > Entity Manager > Remove | Entity remove operation. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JPA > Entity Manager > Find | Entity find operation. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JPA > Entity Manager > Query | Query execution. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JPA > Entity Manager > Lock | Entity lock operation. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JPA > Entity Manager > Refresh | Entity refresh operation. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > JPA > Hibernate Cache > Cache Region Factory | Cache region factory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate Cache > Cache Provider | Cache provider. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Hibernate Cache > Cache Concurrency Strategy | Cache concurrency strategy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JPA > Second-Level Cache > Entity Cache | Entity-level cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > Second-Level Cache > Collection Cache | Collection-level cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > Second-Level Cache > Natural Id Cache | Natural-id cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > Second-Level Cache > Query Cache | Query-level cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JPA > Second-Level Cache > Cache Eviction | Cache eviction. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Cache Container > Transport | Cache-container transport. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Cache Container > Global Configuration | Global cache configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Infinispan > Local Cache > Mode | Local cache mode. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Infinispan > Distributed Cache > Owners | Number of owners. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Infinispan > Distributed Cache > Segments | Number of segments. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Infinispan > Distributed Cache > L1 Lifespan | L1 cache lifespan. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Infinispan > Replicated Cache > Sync Replication | Synchronous replication. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Replicated Cache > Async Replication | Asynchronous replication. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Invalidation Cache > Invalidation Threshold | Invalidation threshold. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Infinispan > Persistent Cache > Store Type | Cache-store type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Infinispan > Cache Store > Write Behind | Write-behind store. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Cache Store > Write Through | Write-through store. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Cache Store > Read Through | Read-through store. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Eviction > Eviction Strategy | Eviction strategy. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Infinispan > Eviction > Eviction Max Entries | Maximum entries before eviction. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Infinispan > Expiration > Interval | Expiration interval. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Infinispan > Expiration > Reaper | Expiration reaper. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Channel > Cluster Name | Channel cluster name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > Channel > Address | Channel address. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > Channel > State Transfer | State transfer on the channel. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Channel > Message Dispatcher | Message dispatcher. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JGroups > Protocol Stack > Protocol Order | Order of protocols in the stack. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > Protocol Stack > Protocol Configuration | Per-protocol configuration. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > JGroups > Transport > Port | Transport port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > Transport > Bind Address | Transport bind address. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > Transport > Buffer Size | Transport buffer size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > Discovery Protocol > Initial Hosts | Initial hosts for discovery. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > Failure Detection > Timeout | Failure-detection timeout. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > Failure Detection > Max Attempts | Maximum failure-detection attempts. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > MERGE3 > Merge Interval | Merge interval. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JGroups > FD_SOCK > Client Bind Address | FD_SOCK client bind address. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Clustering > Cluster Node > Name | Cluster node name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Clustering > Cluster Node > Address | Cluster node address. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Clustering > Cluster Membership > Coordinator | Cluster coordinator. | System Structure | `Production Technical System` |
| WildFly > Subsystems > Clustering > Cluster Membership > View | Cluster view. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Clustering > Cluster Membership > Node List | List of cluster members. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Clustering > Distributed Session Management > Session Cache | Distributed session cache. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Clustering > Distributed Session Management > Session Ownership | Session ownership. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Distributable Web > Session Management > Session Access | Session access. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Distributable Web > Session Affinity > Node Selection | Node-selection algorithm. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Distributable Web > Session Replication > Replication Mode | Replication mode. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Distributable Web > Session Replication > Replication Granularity | Replication granularity. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Distributable EJB > State Replication | EJB state replication. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Distributable EJB > Failover | EJB failover. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Distributable EJB > Load Balancing | EJB load balancing. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Singleton > Singleton Service > Service Name | Singleton service name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Singleton > Singleton Service > Provider | Singleton provider. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Singleton > Singleton Policy > Policy Name | Singleton policy name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Transactions > Transaction Manager > Transaction ID | Transaction identifier. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Transactions > Transaction Manager > Transaction Status | Transaction status. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Transactions > Transaction Manager > Transaction Timeout | Transaction timeout. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Transactions > Transaction > Resource Enlistment | Resource enlistment. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Transactions > Transaction > Synchronization | Transaction synchronization. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Transactions > Transaction > Branch | Transaction branch. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > XA Coordination > XA Resource | XA resource. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > XA Coordination > XA Branch | XA branch. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > XA Coordination > XID | XA transaction identifier. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Transactions > Recovery > Recovery Manager > Scan Interval | Recovery scan interval. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Transactions > Recovery > Recovery Manager > Recovery Module | Recovery module. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Recovery > Recovery Scan > In-Doubt Transaction | In-doubt transaction. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > Recovery > Recovery Scan > Heuristic Outcome | Heuristic outcome. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Transactions > Object Store > Transaction Log > Log File | Transaction log file. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > Object Store > Transaction Log > Log Entry | Transaction log entry. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > Object Store > Log Write > Append | Append to log. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Object Store > Log Write > Sync | Sync log write. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Object Store > Log Read > Scan | Scan log file. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Object Store > Log Read > Replay | Replay log entry. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Transactions > Timeout > Transaction Timeout > Timeout Value | Timeout value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Transactions > Timeout > Reaper > Reaper Thread | Reaper thread. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > Timeout > Reaper > Reaper Interval | Reaper interval. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Transactions > JTS > ORB Integration > ORB | ORB instance. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > JTS > ORB Integration > POA | Portable Object Adapter. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Transactions > JTS > ORB Integration > IOR | Interoperable Object Reference. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Acceptors > In-VM Acceptor | In-VM acceptor. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Acceptors > Netty Acceptor | Netty acceptor. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Acceptors > HTTP Acceptor | HTTP acceptor. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Connectors > In-VM Connector | In-VM connector. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Connectors > Netty Connector | Netty connector. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Security Settings > Security Domain | Broker security domain. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Security Settings > Permission | Broker permission. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Persistence > Journal Type | Journal type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Persistence > Journal Directory | Journal directory. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Journal > Journal File | Journal file. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Journal > Journal Record | Journal record. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Broker Server > Journal > Journal Compaction | Journal compaction. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address > Address Name | Address name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address > Routing Type | Address routing type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address > Bindings > Queue Binding | Queue binding. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address > Bindings > Topic Binding | Topic binding. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Queue > Queue Name | Queue name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Queue > Durable | Durable flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Queue > Max Consumers | Maximum consumers. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Queue > Consumers > Consumer | Queue consumer. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Queue > Messages > Message | Queued message. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Topic > Topic Name | Topic name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Topic > Durable Subscription | Durable subscription. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Topic > Non-Durable Subscription | Non-durable subscription. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Topic > Messages > Message | Topic message. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connection Factory > Factory Name | Connection-factory name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connection Factory > Connectors | Connectors used by the factory. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connection Factory > Discovery Group | Discovery group. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connection Factory > HA | High-availability flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connection Factory > Client ID | Client ID. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connection Factory > Reconnect Attempts | Reconnect attempts. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connector > Socket Binding | Connector socket binding. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Connector > Protocol | Connector protocol. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Remote Connector > Remote Socket Binding | Remote-connector socket binding. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Remote Connector > Remote Protocol | Remote-connector protocol. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Acceptor > Acceptor Name | Acceptor name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Acceptor > Socket Binding | Acceptor socket binding. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Acceptor > Protocol | Acceptor protocol. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Pooled Connection Factory > Pool Name | Pool name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Pooled Connection Factory > Max Pool Size | Maximum pool size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Pooled Connection Factory > Min Pool Size | Minimum pool size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Pooled Connection Factory > Idle Timeout | Pool idle timeout. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > JMS Bridge > Source > Source Connection Factory | Source connection factory. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > JMS Bridge > Source > Source Destination | Source destination. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > JMS Bridge > Target > Target Connection Factory | Target connection factory. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > JMS Bridge > Target > Target Destination | Target destination. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Messaging-ActiveMQ > JMS Bridge > Quality of Service > QoS Mode | QoS mode. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > JMS Bridge > Quality of Service > Failure Retry Interval | Failure-retry interval. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Security Setting > Authentication > User | Messaging user. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Messaging-ActiveMQ > Security Setting > Authentication > Role | Messaging role. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Messaging-ActiveMQ > Security Setting > Authorization > Permission | Messaging permission. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting > Address Match | Address match pattern. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting > Dead Letter Address > DLQ | Dead-letter queue. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting > Expiry Address > Expiry Queue | Expiry queue. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting > Max Size Bytes > Bytes | Maximum size in bytes. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting > Page Size Bytes | Page size in bytes. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting > Page Cache Max Size | Page-cache max size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Address Setting > Message Counter History | Message-counter history. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Divert > Divert Name | Divert name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Divert > Routing Type | Divert routing type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Divert > Forwarding Address | Forwarding address. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Divert > Filter | Divert filter. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Messaging-ActiveMQ > Divert > Transformer | Divert transformer. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Resource Adapters > Resource Adapter > Archive | Resource-adapter archive. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Resource Adapters > Resource Adapter > Deployment Descriptor | Resource-adapter deployment descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Resource Adapters > Resource Adapter > Connection Factory > Managed Connection Factory | Managed connection factory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Resource Adapters > Resource Adapter > Connection Factory > Connection Factory Interface | Connection factory interface. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Resource Adapters > Resource Adapter > Admin Object > Admin Object Interface | Admin-object interface. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Resource Adapters > Resource Adapter > Admin Object > Admin Object Properties | Admin-object properties. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Resource Adapters > Connection Definition > Managed Connection Factory > Connection Factory Impl | Connection-factory implementation. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Resource Adapters > Connection Definition > Managed Connection Factory > Connection Impl | Connection implementation. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Resource Adapters > Connection Definition > Connection Factory Interface > Interface Class | Interface class. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Resource Adapters > Connection Definition > Connection Interface > Interface Class | Connection interface class. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Resource Adapters > Admin Object > Admin Object Interface > Interface Class | Admin-object interface class. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Resource Adapters > Admin Object > Admin Object Properties > Property | Admin-object property. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Resource Adapters > Activation > Activation Spec > Message Listener Type | Message-listener type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Resource Adapters > Activation > Message Listener > onMessage | Message-listener callback. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Security > Legacy Security Domain > Authentication > Login Module | Legacy login module. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Security > Legacy Security Domain > Authentication > JAAS Configuration | JAAS configuration. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Security > Legacy Security Domain > Authorization > Role Mapping | Role mapping. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Security > Legacy Security Domain > Mapping > Principal Mapping | Principal mapping. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Elytron > Security Domain > Default Realm > Realm Name | Default realm name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Security Domain > Role Decoder > Decoder Name | Role-decoder name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Security Domain > Permission Mapper > Mapper Name | Permission-mapper name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Security Realm > Name | Realm name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Security Realm > Identity Acquisition > Identity | Identity acquisition. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Security Realm > Credential Acquisition > Credential | Credential acquisition. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Identity Realm > Identity Store > Identity Entry | Identity entry. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Identity Realm > Identity Store > Attribute | Identity attribute. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Filesystem Realm > Filesystem Store > File | Identity file. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Filesystem Realm > Filesystem Store > Directory | Identity directory. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Filesystem Realm > Filesystem Store > Level | Filesystem level. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > JDBC Realm > SQL Query > Principal Query | Principal query. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Elytron > JDBC Realm > SQL Query > Role Query | Role query. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Elytron > JDBC Realm > SQL Query > Attribute Query | Attribute query. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Elytron > LDAP Realm > LDAP Search > Search Base | LDAP search base. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > LDAP Realm > LDAP Search > Filter | LDAP search filter. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > JAAS Realm > Login Context > Login Module | JAAS login module. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Aggregate Realm > Realm Composition > Realm Order | Realm order. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Caching Realm > Cache > Cache Size | Cache size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Caching Realm > Cache > Cache Timeout | Cache timeout. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Key Store > Key Entry > Alias | Key alias. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Key Store > Key Entry > Key Algorithm | Key algorithm. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Key Store > Key Entry > Key Size | Key size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Key Store > Certificate Entry > Alias | Certificate alias. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Key Store > Certificate Entry > Certificate | Certificate. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Trust Store > Trusted Certificate > Alias | Trusted-certificate alias. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Trust Store > Trusted Certificate > Certificate | Trusted certificate. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Elytron > Credential Store > Credential Entry > Alias | Credential alias. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Credential Store > Credential Entry > Secret | Credential secret. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Elytron > Authentication Factory > Mechanism Selection > Mechanism Name | Authentication-mechanism name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > HTTP Authentication Factory > HTTP Mechanism > Mechanism Name | HTTP authentication-mechanism name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > SASL Authentication Factory > SASL Mechanism > Mechanism Name | SASL mechanism name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Permission Mapper > Permission Assignment > Permission | Assigned permission. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Elytron > Role Mapper > Role Transformation > Role | Transformed role. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Elytron > Principal Transformer > Principal Transformation > Principal | Transformed principal. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Elytron > Evidence Decoder > Evidence Decoding > Evidence Type | Evidence type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Realm Mapper > Realm Mapping > Realm Name | Realm name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > TLS Configuration > Protocol Selection > Protocol | TLS protocol. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > TLS Configuration > Cipher Suite Selection > Cipher Suite | Cipher suite. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > TLS Configuration > Certificate Revocation > Revocation Check | Revocation check. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Elytron > Cipher Suite > Cipher Name > Name | Cipher-suite name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > Protocol > Protocol Name > Name | Protocol name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Elytron > OIDC Client > Token Validation > Signature | Token signature. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Elytron > OIDC Client > Token Validation > Expiry | Token expiry. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Elytron > OIDC Client > Token Validation > Issuer | Token issuer. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Elytron > OIDC Client > Token Refresh > Refresh Token | Refresh token. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Web Services > JAX-WS Endpoint > Service Endpoint Interface | Service endpoint interface. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Web Services > JAX-WS Endpoint > Implementation Class | Endpoint implementation class. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Web Services > JAX-WS Endpoint > Binding | SOAP binding. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > JAX-WS Endpoint > Handler Chain | SOAP handler chain of the endpoint. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Web Services > JAX-WS Endpoint > Handler Chain > Handler | SOAP handler. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Web Services > WSDL > Service Definition > Port | WSDL port. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > WSDL > Binding Definition > Operation | WSDL binding operation. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > WSDL > Port Type Definition > Operation | WSDL port-type operation. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > WSDL > Message Definition > Part | WSDL message part. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Web Services > Handler Chain > Handler Invocation > Inbound | Inbound handler invocation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Web Services > Handler Chain > Handler Invocation > Outbound | Outbound handler invocation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Batch JBeret > Job > Job Instance > Instance ID | Job-instance ID. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Batch JBeret > Job > Job Execution > Execution ID | Job-execution ID. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Batch JBeret > Job > Job Execution > Batch Status | Batch status. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Batch JBeret > Job > Job Execution > Exit Status | Exit status. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Batch JBeret > Step > Step Execution > Step Name | Step name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Batch JBeret > Step > Chunk Processing > Reader | Chunk reader. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Batch JBeret > Step > Chunk Processing > Processor | Chunk processor. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Batch JBeret > Step > Chunk Processing > Writer | Chunk writer. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Batch JBeret > Step > Chunk Processing > Checkpoint | Chunk checkpoint. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Batch JBeret > Step > Batchlet Processing > Batchlet | Batchlet. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Batch JBeret > Job Repository > Job State > Job Instance | Job instance. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Batch JBeret > Job Repository > Step State > Step Execution | Step execution. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Mail > Mail Session > Session Properties > Host | Mail host. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mail > Mail Session > Session Properties > Port | Mail port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mail > Mail Session > Session Properties > Protocol | Mail protocol. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mail > Mail Session > Session Properties > Debug | Debug flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mail > Mail Session > Credentials > User | Mail user. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Mail > Mail Session > Credentials > Password | Mail password. | Technical Control | `Technical Security` |
| WildFly > Subsystems > JMX > MBean > Attribute > Name | MBean attribute name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JMX > MBean > Attribute > Type | MBean attribute type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JMX > MBean > Operation > Name | MBean operation name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JMX > MBean > Operation > Signature | MBean operation signature. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JMX > MBean > Notification > Type | Notification type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JMX > MBean Server > Registration > Object Name | MBean object name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JMX > MBean Server > Query > Query Expression | JMX query expression. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JMX > JMX Connector > Remote Access > RMI | RMI-based JMX access. | System Structure | `Technical Interface` |
| WildFly > Subsystems > Logging > Log Category > Level > Level Value | Log-level value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Log Category > Handlers > Handler Reference | Handler reference. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Logging > Log Category > Use Parent Handlers > Flag | Use-parent-handlers flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Handler > Level > Level Value | Handler-level value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Handler > Formatter > Pattern | Formatter pattern. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Handler > Filter > Expression | Filter expression. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > File Handler > File Path > Path | Log-file path. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > File Handler > Append > Flag | Append flag. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Console Handler > Target > Target | Console target. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Periodic Rotating File Handler > Suffix > Suffix Pattern | Rotation suffix. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Size Rotating File Handler > Max File Size > Size | Max file size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Size Rotating File Handler > Max Backup Index > Index | Max backup index. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Async Handler > Queue Length > Length | Async queue length. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Async Handler > Overflow Action > Action | Overflow action. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Formatter > Pattern > Format | Format pattern. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Logging > Log Level > Severity > Severity | Severity threshold. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > IO > Worker > Task Queue > Queue | Worker task queue. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > IO > Worker > Thread Pool > Threads | Worker threads. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > IO > Buffer Pool > Buffer Size > Size | Buffer size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > IO > Buffer Pool > Buffer Count > Count | Buffer count. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Remoting > Connector > Transport > Transport Type | Transport type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Remoting > Connector > Security > SASL Policy | Connector SASL policy. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Remoting > Endpoint > Listener > Listener Type | Listener type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Remoting > HTTP Upgrade > Upgrade Handshake > Upgrade Header | HTTP upgrade header. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Remoting > SASL Policy > Mechanism Selection > Mechanism | SASL mechanism. | Technical Control | `Technical Security` |
| WildFly > Subsystems > Discovery > Discovery Provider > Static Provider > Address List | Static address list. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Discovery > Discovery Provider > Aggregate Provider > Providers | Aggregated providers. | System Structure | `Technical Element Set` |
| WildFly > Subsystems > Discovery > Static Discovery > Address List > Address | Static address. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Discovery > Aggregate Discovery > Provider Composition > Provider | Aggregated provider. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Mod_Cluster > Proxy > Balancer > Balancer Type | Balancer type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mod_Cluster > Proxy > Node Registration > Node | Registered node. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > Mod_Cluster > Advertise > Multicast > Multicast Address | Multicast address. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mod_Cluster > Advertise > Multicast > Multicast Port | Multicast port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mod_Cluster > Advertise > Socket Advertisement > Socket Binding | Advertisement socket binding. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mod_Cluster > Balancer > Load Factor > Factor | Load factor. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Mod_Cluster > Balancer > Sticky Session > Sticky | Sticky-session flag. | Requirements & Definition | `Technical Configuration` |
| WildFly > Subsystems > Mod_Cluster > Node > Node Registration > Node | Registered node. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Health > Health Check > UP > Status | UP status. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Health Check > DOWN > Status | DOWN status. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Readiness Check > READY > Status | READY status. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Readiness Check > NOT_READY > Status | NOT_READY status. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Liveness Check > ALIVE > Status | ALIVE status. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Health > Liveness Check > DEAD > Status | DEAD status. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > Metrics > Metric > Value > Value | Metric value. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Metric > Unit > Unit | Metric unit. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Gauge > Reading > Reading | Gauge reading. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Counter > Increment > Delta | Counter increment. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Counter > Decrement > Delta | Counter decrement. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > Metrics > Histogram > Buckets > Bucket | Histogram bucket. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > MicroProfile > Config > Property Source > Source Name | Property-source name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Config > Property Value > Value | Property value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Health > Health Check > Check Name | Health-check name. | Technical Control | `Technical Evaluation` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Retry > Max Retries | Maximum retries. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Retry > Delay | Retry delay. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Timeout > Timeout Value | Timeout value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Circuit Breaker > Failure Threshold | Failure threshold. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Circuit Breaker > Delay | Circuit-breaker delay. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Bulkhead > Max Concurrent | Maximum concurrent calls. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Bulkhead > Queue Size | Bulkhead queue size. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Fault Tolerance > Fallback > Fallback Method | Fallback method. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > MicroProfile > Reactive Messaging > Channel > Channel Name | Channel name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Reactive Messaging > Connector > Connector Name | Connector name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > MicroProfile > Metrics > Metric > Metric Name | Metric name. | Technical Control | `Technical Performance` |
| WildFly > Subsystems > MicroProfile > OpenAPI > Document > Info | OpenAPI info section. | Knowledge & Methodology | `Knowledge & Methodology > Technical Knowledge` |
| WildFly > Subsystems > MicroProfile > OpenAPI > Document > Paths | OpenAPI paths section. | Knowledge & Methodology | `Knowledge & Methodology > Technical Knowledge` |
| WildFly > Subsystems > MicroProfile > OpenAPI > Operation > Operation ID | OpenAPI operation ID. | Knowledge & Methodology | `Knowledge & Methodology > Technical Knowledge` |
| WildFly > Subsystems > MicroProfile > JWT > Token > Header | JWT header. | Technical Control | `Technical Security` |
| WildFly > Subsystems > MicroProfile > JWT > Token > Payload | JWT payload. | Technical Control | `Technical Security` |
| WildFly > Subsystems > MicroProfile > JWT > Claim > Claim Name | JWT claim name. | Technical Control | `Technical Security` |
| WildFly > Subsystems > MicroProfile > JWT > Claim > Claim Value | JWT claim value. | Technical Control | `Technical Security` |
| WildFly > Subsystems > SAR > SAR Deployment > Deployment > Archive | SAR archive. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > SAR > SAR Deployment > Undeployment > Archive | SAR archive. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > SAR > MBean > Registration > Object Name | SAR MBean object name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > JSF > Mojarra > Lifecycle > Restore View | JSF restore-view phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > JSF > Mojarra > Lifecycle > Apply Request Values | JSF apply-request-values phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > JSF > Mojarra > Lifecycle > Process Validations | JSF process-validations phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > JSF > Mojarra > Lifecycle > Update Model Values | JSF update-model-values phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > JSF > Mojarra > Lifecycle > Invoke Application | JSF invoke-application phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > JSF > Mojarra > Lifecycle > Render Response | JSF render-response phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > JSF > Mojarra > Component Tree > UIViewRoot | JSF UIViewRoot. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JSF > Mojarra > Component Tree > UIComponent | JSF UIComponent. | System Structure | `Constitutive Technical Object` |
| WildFly > Subsystems > JSF > Mojarra > Renderer > RenderKit | JSF RenderKit. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > JSF > `faces-config.xml` > Navigation Rules > Rule | JSF navigation rule. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > JSF > `faces-config.xml` > Managed Beans > Bean | JSF managed bean. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > POJO > POJO Deployment > Deployment > Archive | POJO archive. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > POJO > POJO Deployment > Undeployment > Archive | POJO archive. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Subsystems > Bean Validation > Validator > Validation > Constraint Validation | Constraint validation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Bean Validation > Constraint > Definition > Annotation | Constraint annotation. | Requirements & Definition | `Technical Specification` |
| WildFly > Subsystems > Bean Validation > Constraint > Violation > Message | Violation message. | Technical Control | `Technical Feedback` |
| WildFly > Subsystems > Deployment Scanner > Scan > Directory Scan | Directory scan. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Subsystems > Deployment Scanner > Deploy > Marker Handling | Marker handling. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Deployment Scanner > Undeploy > Marker Handling | Marker handling. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Subsystems > Deployment Scanner > Scan Interval > Interval | Scan interval. | Requirements & Definition | `Technical Parameter` |
| WildFly > Subsystems > Deployment Scanner > Deployment Marker > Type | Marker type. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Unit > Archive > File | Deployment archive file. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Deployment Unit > Descriptor > File | Deployment descriptor file. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Unit > Structure > Directory | Deployment directory. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > WEB-INF > `web.xml` | Servlet deployment descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > WAR > WEB-INF > `jboss-web.xml` | WildFly web descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > WAR > WEB-INF > `beans.xml` | CDI descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > WAR > WEB-INF > Classes | Compiled classes. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > WEB-INF > Libraries | Bundled libraries. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > META-INF > `MANIFEST.MF` | Manifest file. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > WAR > META-INF > Services | Service loader files. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > WAR > Static Content > HTML | Static HTML content. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > Static Content > CSS | Static CSS content. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > Static Content > JavaScript | Static JavaScript content. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > WAR > Static Content > Images | Static images. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > JAR > META-INF > `MANIFEST.MF` | Manifest file. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > JAR > META-INF > `persistence.xml` | Persistence descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > JAR > META-INF > `beans.xml` | CDI descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > JAR > Classes > Package | Java package. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > JAR > Classes > Class | Java class. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > JAR > Resources > Properties File | Properties file. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > JAR > Resources > XML File | XML resource. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > EAR > Modules > EJB Module | EJB module. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > EAR > Modules > Web Module | Web module. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > EAR > Modules > Connector Module | Connector module. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > EAR > Modules > Client Module | Client module. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > EAR > Libraries > Library JAR | Library JAR. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > EAR > META-INF > `application.xml` | Application descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > EAR > META-INF > `jboss-app.xml` | JBoss application descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > RAR > META-INF > `ra.xml` | Resource-adapter descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > RAR > META-INF > `ironjacamar.xml` | IronJacamar descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > RAR > Native Libraries > Library | Native library. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > SAR > META-INF > `jboss-service.xml` | Service descriptor. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > SAR > Service Classes > Service | Service class. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Deployment Descriptor > Element > Element Name | Descriptor element name. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Descriptor > Schema Reference > Namespace | Descriptor namespace. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Servlet Declaration > Servlet Name | Servlet name. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Servlet Declaration > Servlet Class | Servlet class. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Servlet Declaration > Init Parameter | Servlet init parameter. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Servlet Declaration > Load On Startup | Load-on-startup. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Filter Declaration > Filter Name | Filter name. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Filter Declaration > Filter Class | Filter class. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Listener Declaration > Listener Class | Listener class. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Welcome File > File | Welcome file. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Security Constraint > Role | Security role. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `web.xml` > Security Constraint > URL Pattern | Security URL pattern. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-web.xml` > Context Root > Root | Context root. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-web.xml` > Virtual Host > Host | Virtual host. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ejb-jar.xml` > Session Bean > Bean Name | Session-bean name. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ejb-jar.xml` > Session Bean > Bean Class | Session-bean class. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ejb-jar.xml` > Session Bean > Session Type | Session-bean type. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ejb-jar.xml` > Message-Driven Bean > Bean Name | MDB name. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ejb-jar.xml` > Message-Driven Bean > Destination | MDB destination. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ejb-jar.xml` > Assembly Descriptor > Security Role | EJB security role. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `persistence.xml` > Persistence Unit > Unit Name | Persistence-unit name. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `persistence.xml` > Persistence Unit > Transaction Type | Persistence transaction type. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `persistence.xml` > Class List > Class | Persistence class. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `persistence.xml` > Properties > Property | Persistence property. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `beans.xml` > Discovery Mode > Mode | Bean-discovery mode. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `beans.xml` > Interceptors > Interceptor | Interceptor class. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `beans.xml` > Decorators > Decorator | Decorator class. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `application.xml` > Module > Module URI | Module URI. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `application.xml` > Security Role > Role | Application security role. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-app.xml` > Class Loading > Policy | Class-loading policy. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ra.xml` > Resource Adapter > Adapter Class | Resource-adapter class. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ra.xml` > Connection Definition > Managed Connection Factory | Managed connection factory. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `ironjacamar.xml` > Connection Pool > Pool Configuration | Connection-pool configuration. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `application-client.xml` > Client Descriptor > Client Name | Client name. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-client.xml` > Client Descriptor > Client Name | JBoss client name. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-deployment-structure.xml` > Dependencies > Module | Deployment module dependency. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-deployment-structure.xml` > Exclusions > Exclusion | Deployment exclusion. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > `jboss-deployment-structure.xml` > Local Resources > Resource | Local resource. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Annotation > Class Annotation > Annotation | Class-level annotation. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Annotation > Method Annotation > Annotation | Method-level annotation. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Annotation > Field Annotation > Annotation | Field-level annotation. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Processor > Parse > Descriptor Parser | Descriptor parser. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Processor > Parse > Annotation Scanner | Annotation scanner. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Processor > Register > Component Registry | Component registry. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Processor > Deploy > Service Installation | Service installation. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > STRUCTURE > Structure Build | Structure build. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > PARSE > Parse | Parse phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > REGISTER > Register | Register phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > DEPENDENCIES > Dependency Resolution | Dependency resolution. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > CONFIGURE_MODULE > Module Configuration | Module configuration. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > POST_MODULE > Post-Module Processing | Post-module processing. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > INSTALL > Install | Install phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Phase > CLEANUP > Cleanup | Cleanup phase. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Deployment Unit Processor > Transform > Transform Step | Transform step. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Service > Registration > Service Name | Deployment-service name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Deployment > Deployment Service > Start > Service Start | Service start. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Deployment Service > Stop > Service Stop | Service stop. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Deployment Lifecycle > Deploy > Transition | Deploy transition. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Lifecycle > Undeploy > Transition | Undeploy transition. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Lifecycle > Redeploy > Transition | Redeploy transition. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Lifecycle > Replace > Transition | Replace transition. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Lifecycle > Explode > Transition | Explode transition. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Deployment > Deployment Scanner > Scan > Directory Scan | Directory scan. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Scanner > Deploy > Marker Handling | Marker handling. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Scanner > Undeploy > Marker Handling | Marker handling. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Deployment Marker > `.dodeploy` > Marker | `.dodeploy` marker. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker > `.undeploy` > Marker | `.undeploy` marker. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker > `.deployed` > Marker | `.deployed` marker. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker > `.failed` > Marker | `.failed` marker. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker > `.isdeploying` > Marker | `.isdeploying` marker. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Deployment Marker > `.skipdeploy` > Marker | `.skipdeploy` marker. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Application > Module > Classes > Class | Application class. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Module > Resources > Resource | Application resource. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Module > Libraries > Library | Application library. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Module > Class Loader > Loader | Application module class loader. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Application > Component > Servlet Component > Servlet | Servlet component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Component > EJB Component > EJB | EJB component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Component > CDI Component > Bean | CDI bean component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Component > REST Component > Resource | REST resource component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Component > WebSocket Component > Endpoint | WebSocket endpoint component. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Servlet > Lifecycle > Init | Servlet init. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > Servlet > Lifecycle > Service | Servlet service. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > Servlet > Lifecycle > Destroy | Servlet destroy. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > Servlet > Request Handling > Request Dispatch | Servlet request dispatch. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Application > Servlet > Session Handling > Session Access | Servlet session access. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Application > CDI Bean > Scope > Scope Annotation | CDI scope annotation. | Requirements & Definition | `Technical Parameter` |
| WildFly > Deployment > Application > CDI Bean > Lifecycle > Creation | CDI bean creation. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > CDI Bean > Lifecycle > Destruction | CDI bean destruction. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > CDI Bean > Injection > Injection Point | CDI injection point. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Application > EJB > Lifecycle > Creation | EJB creation. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > EJB > Lifecycle > Invocation | EJB invocation. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > EJB > Lifecycle > Passivation | EJB passivation. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > EJB > Lifecycle > Activation | EJB activation. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > EJB > Lifecycle > Removal | EJB removal. | Technical Operation | `Technical Operation > Technical Activity` |
| WildFly > Deployment > Application > EJB > Business Interface > Interface | EJB business interface. | System Structure | `Technical Interface` |
| WildFly > Deployment > Application > EJB > Transaction Attribute > Attribute | EJB transaction attribute. | Requirements & Definition | `Technical Parameter` |
| WildFly > Deployment > Application > EJB > Security Role > Role | EJB security role. | Technical Control | `Technical Security` |
| WildFly > Deployment > Application > REST Resource > Resource Method > Method | REST resource method. | Technical Operation | `Technical Operation > Technical Act` |
| WildFly > Deployment > Application > REST Resource > Path > Path | REST resource path. | Requirements & Definition | `Technical Parameter` |
| WildFly > Deployment > Application > REST Resource > Media Type > Media Type | REST media type. | Requirements & Definition | `Technical Parameter` |
| WildFly > Deployment > Application > Persistence Unit > Entity > Entity Class | JPA entity class. | System Structure | `Constitutive Technical Object` |
| WildFly > Deployment > Application > Persistence Unit > Entity > Entity Mapping | JPA entity mapping. | Requirements & Definition | `Technical Specification` |
| WildFly > Deployment > Application > Persistence Unit > Entity Manager Factory > Factory | Entity manager factory. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Deployment > Application > Persistence Unit > Data Source > DataSource | Data source. | System Structure | `Technical Interface` |
| WildFly > Deployment > Application > JNDI Resource > Resource Reference > Reference Name | JNDI reference name. | System Structure | `Technical Interface` |
| WildFly > Deployment > Application > JNDI Resource > Environment Entry > Entry Name | JNDI environment entry name. | System Structure | `Technical Interface` |
| WildFly > Deployment > Application > Security Domain Association > Domain Reference > Domain | Security domain. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Datasource Dependency > Datasource Reference > Datasource | Datasource. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Messaging Dependency > Connection Factory Reference > Connection Factory | Connection factory. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Messaging Dependency > Destination Reference > Destination | Messaging destination. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Module Dependency > Module Reference > Module | WildFly module. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Application > Module Dependency > Export > Package | Exported package. | System Relations | `Technical Dependency` |
| WildFly > Deployment > Archive Assembly | Technique for assembling deployment archives for WildFly deployment. | Technical Operation | `Constitutive Technique` |
| WildFly > Services | Technical services delivered to deployed applications. | Lifecycle & Continuity | `Technical Element Set` |
| WildFly > Services > Deployment Service | Controlled introduction and lifecycle of application deployments. | Lifecycle & Continuity | `Technical Service` |
| WildFly > Services > Deployment Service > Deployment Capability | Possibility of deploying and running enterprise applications. | Mechanism & Capability | `Technical Capability` |
| WildFly > Services > Deployment Service > Deployment Interface | Boundary through which deployments are submitted: scanner, CLI, console. | System Structure | `Technical Interface` |
| WildFly > Services > Deployment Service > Deployment Mechanism | Processor chain transforming deployment content into runtime services. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Services > Deployment Service > Deployment Activity | Sequence of submit, verify, and activate acts. | Technical Operation | `Technical Activity` |
| WildFly > Services > Deployment Service > Deployment Task | Single deploy or undeploy unit of work. | Technical Operation | `Technical Task` |
| WildFly > Services > Deployment Service > Deployment Requirement | Deployments must reach active state within operational bounds. | Requirements & Definition | `Technical Requirement` |
| WildFly > Services > Deployment Service > Deployment Feedback | Deployment state, markers, and scanner notifications. | Technical Control | `Technical Feedback` |
| WildFly > Services > Deployment Service > Deployment Evaluation | Determination of deployment success and health. | Technical Control | `Technical Evaluation` |
| WildFly > Services > Deployment Service > Deployment Maintenance | Redeploy, rollback, and content-repository upkeep. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Services > Deployment Service > Deployment Lifecycle | Deploy, operate, undeploy trajectory of a deployment. | Lifecycle & Continuity | `Technical Lifecycle` |
| WildFly > Network > Public Interface > Inet Address > Address | Public inet address. | System Structure | `Technical Interface` |
| WildFly > Network > Management Interface > Inet Address > Address | Management inet address. | System Structure | `Technical Interface` |
| WildFly > Network > Unsecure Interface > Inet Address > Address | Unsecure inet address. | System Structure | `Technical Interface` |
| WildFly > Network > HTTP Endpoint > Port > Port | HTTP port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > HTTPS Endpoint > Port > Port | HTTPS port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > HTTPS Endpoint > Certificate > Certificate | TLS certificate. | System Structure | `Constitutive Technical Object` |
| WildFly > Network > AJP Endpoint > Port > Port | AJP port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Remoting Endpoint > Port > Port | Remoting port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Messaging Endpoint > Port > Port | Messaging port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > JGroups Endpoint > Port > Port | JGroups port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > TXN Recovery Endpoint > Port > Port | TXN recovery port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > TXN Status Manager Endpoint > Port > Port | TXN status manager port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Management HTTP Endpoint > Port > Port | Management HTTP port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Management Native Endpoint > Port > Port | Management native port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Socket Binding > Name > Name | Socket-binding name. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Socket Binding > Port > Port | Socket-binding port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Socket Binding > Interface > Interface | Socket-binding interface. | System Structure | `Technical Interface` |
| WildFly > Network > Socket Binding Group > Default Interface > Interface | Default interface. | System Structure | `Technical Interface` |
| WildFly > Network > Socket Binding Group > Port Offset > Offset | Port offset. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Port Offset > Offset Value > Offset | Port offset value. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Outbound Socket Binding > Remote Host > Host | Remote host. | Requirements & Definition | `Technical Parameter` |
| WildFly > Network > Outbound Socket Binding > Remote Port > Port | Remote port. | Requirements & Definition | `Technical Parameter` |
| WildFly > Runtime Security > Authentication > Mechanism > Mechanism | Authentication mechanism. | Mechanism & Capability | `Technical Capability` |
| WildFly > Runtime Security > Authentication > Credential > Credential | Authentication credential. | Technical Control | `Technical Security` |
| WildFly > Runtime Security > Authorization > Policy > Policy | Authorization policy. | Mechanism & Capability | `Technical Capability` |
| WildFly > Runtime Security > Authorization > Decision > Decision | Authorization decision. | Technical Control | `Technical Security` |
| WildFly > Runtime Security > TLS > Handshake > Handshake | TLS handshake. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime Security > TLS > Cipher Negotiation > Cipher | Negotiated cipher. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime Security > TLS > Certificate Validation > Validation | Certificate validation. | Mechanism & Capability | `Technical Mechanism` |
| WildFly > Runtime Security > Credential Store > Entry > Entry | Credential entry. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Credential Store > Alias > Alias | Credential alias. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Identity > Name > Name | Identity name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Identity > Attributes > Attribute | Identity attribute. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Principal > Name > Name | Principal name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Role > Name > Name | Role name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Permission > Name > Name | Permission name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Permission > Actions > Actions | Permission actions. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Security Event > Type > Type | Security-event type. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Security > Security Event > Timestamp > Timestamp | Security-event timestamp. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Security > Audit Event > Category > Category | Audit-event category. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Security > Audit Event > Outcome > Outcome | Audit-event outcome. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Security > Security Domain > Name > Name | Security-domain name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Security Domain > Realm > Realm | Security-domain realm. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Realm > Name > Name | Realm name. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > Realm > Identity Store > Store | Realm identity store. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > SSL Context > Protocol > Protocol | SSL context protocol. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Security > SSL Context > Cipher Suites > Cipher Suite | SSL context cipher suite. | System Structure | `Constitutive Technical Object` |
| WildFly > Runtime Control > Configuration State > Active Profile > Profile | Active profile. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Configuration State > Running Mode > Mode | Running mode. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Configuration State > Server State > State | Server state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime State > Started > State | Started state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime State > Stopped > State | Stopped state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime State > Reload Required > State | Reload-required state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime State > Restart Required > State | Restart-required state. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Runtime Metric > Name > Name | Runtime-metric name. | Technical Control | `Technical Performance` |
| WildFly > Runtime Control > Runtime Metric > Value > Value | Runtime-metric value. | Technical Control | `Technical Performance` |
| WildFly > Runtime Control > Runtime Metric > Unit > Unit | Runtime-metric unit. | Technical Control | `Technical Performance` |
| WildFly > Runtime Control > Log Event > Level > Level | Log-event level. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Log Event > Message > Message | Log-event message. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Log Event > Timestamp > Timestamp | Log-event timestamp. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Health Result > Status > Status | Health-result status. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Health Result > Check > Check | Health-check name. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > Diagnostic Report > Section > Section | Diagnostic-report section. | Technical Control | `Technical Evaluation` |
| WildFly > Runtime Control > JDR > Collection > Collection | JDR collection. | Technical Control | `Technical Technique` |
| WildFly > Runtime Control > JDR > Report > Report | JDR report. | Technical Control | `Technical Technique` |
| WildFly > Runtime Control > Audit Log > Entry > Entry | Audit-log entry. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Server Log > Entry > Entry | Server-log entry. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > GC Log > Entry > Entry | GC-log entry. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Thread Dump > Thread > Thread | Dumped thread. | Technical Control | `Technical Feedback` |
| WildFly > Runtime Control > Heap Dump > Heap Region > Region | Heap-dump region. | Technical Control | `Technical Feedback` |
| WildFly > Lifecycle > Provision > Provisioning Plan > Plan | Provisioning plan. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Provision > Provisioning Execution > Execution | Provisioning execution. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Install > Distribution Extraction > Extraction | Distribution extraction. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Install > File Placement > Placement | File placement. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure > Profile Selection > Selection | Profile selection. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure > Subsystem Configuration > Configuration | Subsystem configuration. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure > Interface Configuration > Configuration | Interface configuration. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure > Socket Binding Configuration > Configuration | Socket-binding configuration. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Configure > Security Configuration > Configuration | Security configuration. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Start > Service Container Start > Start | Service-container start. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Start > Subsystem Start > Start | Subsystem start. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Start > Deployment Start > Start | Deployment start. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Boot > Bootstrap > Bootstrap | Bootstrap. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Boot > Configuration Load > Load | Configuration load. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Boot > Service Installation > Installation | Service installation. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Deploy > Deployment Processing > Processing | Deployment processing. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Deploy > Deployment Start > Start | Deployment start. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Redeploy > Undeploy > Undeploy | Undeploy phase. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Redeploy > Deploy > Deploy | Deploy phase. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Reload > Stop > Stop | Reload stop. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Reload > Start > Start | Reload start. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Shutdown > Graceful Shutdown > Shutdown | Graceful shutdown. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Shutdown > Forced Shutdown > Shutdown | Forced shutdown. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Undeploy > Deployment Stop > Stop | Deployment stop. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Undeploy > Content Removal > Removal | Content removal. | Technical Operation | `Technical Activity` |
| WildFly > Lifecycle > Maintain > Corrective Maintenance > Maintenance | Corrective maintenance. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Maintain > Preventive Maintenance > Maintenance | Preventive maintenance. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Patch > Patch Application > Application | Patch application. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Patch > Patch Verification > Verification | Patch verification. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Upgrade > Version Change > Change | Version change. | Lifecycle & Continuity | `Technical Evolution` |
| WildFly > Lifecycle > Upgrade > Configuration Migration > Migration | Configuration migration. | Lifecycle & Continuity | `Technical Evolution` |
| WildFly > Lifecycle > Migrate > Configuration Transformation > Transformation | Configuration transformation. | Lifecycle & Continuity | `Technical Evolution` |
| WildFly > Lifecycle > Migrate > Application Migration > Migration | Application migration. | Lifecycle & Continuity | `Technical Evolution` |
| WildFly > Lifecycle > Retire > Decommissioning > Decommissioning | Decommissioning. | Lifecycle & Continuity | `Technical Obsolescence` |
| WildFly > Lifecycle > Retire > Data Archival > Archival | Data archival. | Lifecycle & Continuity | `Technical Obsolescence` |
| WildFly > Lifecycle > Rollback > Version Reversion > Reversion | Version reversion. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Rollback > Configuration Reversion > Reversion | Configuration reversion. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Backup > Configuration Backup > Backup | Configuration backup. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Backup > Data Backup > Backup | Data backup. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Backup > Deployment Backup > Backup | Deployment backup. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Restore > Configuration Restore > Restore | Configuration restore. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Restore > Data Restore > Restore | Data restore. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Lifecycle > Restore > Deployment Restore > Restore | Deployment restore. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > External Resources > CPU > Core > Core | CPU core. | Technical Context | `Technical Resource` |
| WildFly > External Resources > CPU > Frequency > Frequency | CPU frequency. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Memory > Heap > Heap | Runtime heap. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Memory > Off-Heap > Off-Heap | Off-heap memory. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Filesystem > Disk > Disk | Disk storage. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Filesystem > Files > File | Accessed file. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Network > Bandwidth > Bandwidth | Network bandwidth. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Network > Latency > Latency | Network latency. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Database > Connection > Connection | Database connection. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Database > Storage > Storage | Database storage. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Message Broker > Queue > Queue | Broker queue. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Message Broker > Topic > Topic | Broker topic. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Identity Provider > Realm > Realm | IdP realm. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Identity Provider > Endpoint > Endpoint | IdP endpoint. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Certificate Authority > Root Certificate > Root Certificate | Root certificate. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Certificate Authority > CRL > CRL | Certificate revocation list. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Load Balancer > Virtual IP > Virtual IP | Load-balancer virtual IP. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Load Balancer > Pool > Pool | Backend pool. | Technical Context | `Technical Resource` |
| WildFly > External Resources > JDK > JRE > JRE | Java runtime environment. | Technical Context | `Technical Resource` |
| WildFly > External Resources > JDK > JDK Tools > Tool | JDK tool. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Operating System > Kernel > Kernel | OS kernel. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Operating System > Libraries > Library | OS library. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Container Runtime > Image > Image | Container image. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Container Runtime > Volume > Volume | Container volume. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes > Namespace > Namespace | Kubernetes namespace. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes > Service > Service | Kubernetes service. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes > ConfigMap > ConfigMap | Kubernetes ConfigMap. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes > Secret > Secret | Kubernetes Secret. | Technical Context | `Technical Resource` |
| WildFly > External Resources > Kubernetes > Ingress > Ingress | Kubernetes Ingress. | Technical Context | `Technical Resource` |
| WildFly > Application Runtime Domain | Enterprise Java application-server runtime domain. | Technical Context | `Technical Domain` |
| WildFly > Application Runtime Domain > Undeployed Artifact Problem | Undeployed application artifacts require a managed, secure runtime to execute and integrate. | Technical Context | `Technical Problem` |
| WildFly > Application Runtime Domain > Managed Runtime Purpose | Provide a managed runtime for deploying, executing, integrating, securing, and managing enterprise applications. | Technical Context | `Technical Purpose` |
| WildFly > Application Runtime Domain > JVM Compatibility | WildFly requires a compatible Java runtime version. | Technical Context | `Technical Constraint` |
| WildFly > Application Runtime Domain > Resource Bounds | Execution is bounded by available CPU, memory, filesystem, and network capacity. | Technical Context | `Technical Constraint` |
| WildFly > Application Runtime Domain > Specification Compliance | Subsystems must conform to Jakarta EE and related specifications. | Technical Context | `Technical Constraint` |
| WildFly > Application Runtime Domain > Availability Objective | Sustained availability of deployed applications under expected load. | Requirements & Definition | `Technical Requirement` |
| WildFly > Application Runtime Domain > Deployment Responsiveness | Deployments must reach running state within operational time bounds. | Requirements & Definition | `Technical Requirement` |
| WildFly > Operators | Operators sustaining the WildFly instance. | Agents & Competence | `Technical Agent` |
| WildFly > Operators > Administrator | Human agent administering server configuration and lifecycle. | Agents & Competence | `Technical Agent` |
| WildFly > Operators > Application Deployer | Agent introducing application deployments into the runtime. | Agents & Competence | `Technical Agent` |
| WildFly > Operators > Provisioning Pipeline | Automated pipeline constructing and patching server installations. | Agents & Competence | `Technical Agent` |
| WildFly > Operators > Administration Effort | Purposive configuration, deployment, and maintenance effort. | Agents & Competence | `Technical Labor` |
| WildFly > Operators > Administration Expertise | Acquired capacity to reliably administer WildFly systems. | Agents & Competence | `Technical Competence` |
| WildFly > Technical Standards > Jakarta EE > Profile > Profile | Jakarta EE profile. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Servlet > Version > Version | Jakarta Servlet version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta REST > Version > Version | Jakarta REST version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Enterprise Beans > Version > Version | Jakarta EJB version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Persistence > Version > Version | Jakarta Persistence version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Messaging > Version > Version | Jakarta Messaging version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta CDI > Version > Version | Jakarta CDI version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Transactions > Version > Version | Jakarta Transactions version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Bean Validation > Version > Version | Jakarta Bean Validation version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Batch > Version > Version | Jakarta Batch version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Concurrency > Version > Version | Jakarta Concurrency version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Connectors > Version > Version | Jakarta Connectors version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta Mail > Version > Version | Jakarta Mail version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta WebSocket > Version > Version | Jakarta WebSocket version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta JSON Binding > Version > Version | Jakarta JSON-B version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta JSON Processing > Version > Version | Jakarta JSON-P version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta XML Binding > Version > Version | Jakarta XML Binding version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > Jakarta XML Web Services > Version > Version | Jakarta XML WS version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JDBC > Version > Version | JDBC version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JNDI > Version > Version | JNDI version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JMX > Version > Version | JMX version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > HTTP > Version > Version | HTTP version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > HTTPS > Version > Version | HTTPS version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > TLS > Version > Version | TLS version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > AJP > Version > Version | AJP version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > WebSocket > Version > Version | WebSocket version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OIDC > Version > Version | OIDC version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OAuth 2.0 > Version > Version | OAuth 2.0 version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > SAML > Version > Version | SAML version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > JWT > Version > Version | JWT version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > MicroProfile > Version > Version | MicroProfile version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OpenAPI > Version > Version | OpenAPI version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Standards > OpenTelemetry > Version > Version | OpenTelemetry version. | Requirements & Definition | `Technical Standard` |
| WildFly > Technical Practices > Provisioning > Plan Definition > Definition | Plan definition. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Provisioning > Execution > Execution | Provisioning execution. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Configuration Management > Change Control > Control | Change control. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Configuration Management > Version Control > Control | Version control. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Application Deployment > Release Process > Process | Release process. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Application Deployment > Rollback Process > Process | Rollback process. | Technical Operation | `Technical Practice` |
| WildFly > Technical Practices > Monitoring > Metric Collection > Collection | Metric collection. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Monitoring > Alerting > Alerting | Alerting. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Health Checking > Probe Scheduling > Scheduling | Probe scheduling. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Health Checking > Result Handling > Handling | Result handling. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Log Analysis > Collection > Collection | Log collection. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Log Analysis > Interpretation > Interpretation | Log interpretation. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Backup / Recovery > Backup Scheduling > Scheduling | Backup scheduling. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Backup / Recovery > Restore Procedure > Procedure | Restore procedure. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Patching > Patch Planning > Planning | Patch planning. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Patching > Patch Application > Application | Patch application. | Lifecycle & Continuity | `Technical Maintenance` |
| WildFly > Technical Practices > Capacity Management > Sizing > Sizing | Capacity sizing. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Capacity Management > Scaling > Scaling | Capacity scaling. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Security Hardening > Exposure Reduction > Reduction | Exposure reduction. | Technical Control | `Technical Security` |
| WildFly > Technical Practices > Security Hardening > Configuration Hardening > Hardening | Configuration hardening. | Technical Control | `Technical Security` |
| WildFly > Technical Practices > Performance Tuning > JVM Tuning > Tuning | JVM tuning. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Performance Tuning > Subsystem Tuning > Tuning | Subsystem tuning. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Thread Management > Pool Sizing > Sizing | Thread-pool sizing. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Thread Management > Queue Sizing > Sizing | Thread-queue sizing. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Connection Pool Tuning > Pool Sizing > Sizing | Connection-pool sizing. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > Connection Pool Tuning > Timeout Tuning > Tuning | Timeout tuning. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > JVM Tuning > Heap Sizing > Sizing | Heap sizing. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > JVM Tuning > GC Selection > Selection | GC selection. | Technical Control | `Technical Practice` |
| WildFly > Technical Practices > JVM Tuning > System Property Tuning > Tuning | System-property tuning. | Technical Control | `Technical Practice` |
| WildFly > Design Rules | General rules governing construction and operation of this WildFly instance. | Knowledge & Methodology | `Technical Principle` |
| WildFly > Design Rules > Least Privilege | Management and application access granted only as required. | Knowledge & Methodology | `Technical Principle` |
| WildFly > Design Rules > Separation of Concerns | Subsystems isolate distinct technical responsibilities. | Knowledge & Methodology | `Technical Principle` |
| WildFly > Operating Strategies | Regimes for planning and allocating work on this WildFly instance. | Knowledge & Methodology | `Technical Strategy` |
| WildFly > Operating Strategies > Rolling Upgrade | Sequenced update of clustered servers preserving service availability. | Knowledge & Methodology | `Technical Strategy` |
| WildFly > Governing Bodies | Institutions governing this WildFly instance. | Knowledge & Methodology | `Technical Institution` |
| WildFly > Governing Bodies > Jakarta EE Working Group | Body stewarding the enterprise specifications WildFly implements. | Knowledge & Methodology | `Technical Institution` |
| WildFly > Governing Bodies > JBoss Community | Community sustaining WildFly knowledge, practice, and evolution. | Knowledge & Methodology | `Technical Institution` |
| WildFly > Technical Dependencies > JVM > Java Version > Version | Required Java version. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > JVM > JVM Options > Option | Required JVM option. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Operating System > OS Family > Family | Required OS family. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Operating System > OS Libraries > Library | Required OS library. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Filesystem > Paths > Path | Required filesystem path. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Filesystem > Permissions > Permission | Required filesystem permission. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Network Stack > Protocols > Protocol | Required network protocol. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Network Stack > Ports > Port | Required network port. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Database > JDBC Driver > Driver | Required JDBC driver. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Database > Schema > Schema | Required database schema. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > External Services > Endpoint > Endpoint | Required external endpoint. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > External Services > Credentials > Credential | Required external credential. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Message Broker > Broker Endpoint > Endpoint | Required broker endpoint. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Message Broker > Destinations > Destination | Required destination. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Identity Provider > IdP Endpoint > Endpoint | Required IdP endpoint. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Identity Provider > Client Credentials > Credential | Required client credential. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Certificate Authority > Root Certificate > Root Certificate | Required root certificate. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Certificate Authority > Trust Chain > Chain | Required trust chain. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Load Balancer > Frontend Address > Address | Required frontend address. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Load Balancer > Backend Pool > Pool | Required backend pool. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Container Runtime > Image > Image | Required container image. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Container Runtime > Volume > Volume | Required container volume. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Kubernetes API > API Server > Server | Required API server. | System Relations | `Technical Dependency` |
| WildFly > Technical Dependencies > Kubernetes API > Service Account > Account | Required service account. | System Relations | `Technical Dependency` |
| WildFly > Technical Control > Verification Suite > Unit Test > Test Case | Unit test. | Technical Control | `Verification` |
| WildFly > Technical Control > Verification Suite > Integration Test > Test Case | Integration test. | Technical Control | `Verification` |
| WildFly > Technical Control > Verification Suite > Static Analysis > Analysis Report | Static analysis. | Technical Control | `Verification` |
| WildFly > Technical Control > Verification Suite > Inspection > Inspection Record | Inspection. | Technical Control | `Verification` |
| WildFly > Technical Control > Validation Suite > User Validation > Validation Outcome | User validation. | Technical Control | `Validation` |
| WildFly > Technical Control > Validation Suite > Operational Trial > Trial Run | Operational trial. | Technical Control | `Validation` |
| WildFly > Technical Control > Validation Suite > Acceptance Test > Test Case | Acceptance test. | Technical Control | `Validation` |
| WildFly > Technical Control > Feedback > Log Feedback > Log Record | Log feedback. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Feedback > Metric Feedback > Metric Reading | Metric feedback. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Feedback > Health Feedback > Health Report | Health feedback. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Feedback > Management State Feedback > State Snapshot | Management-state feedback. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Failure > Crash > Failure | Crash failure. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Failure > Hang > Failure | Hang failure. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Failure > Deadlock > Failure | Deadlock failure. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Failure > Memory Leak > Failure | Memory-leak failure. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Failure > Thread Leak > Failure | Thread-leak failure. | Technical Control | `Technical Failure` |
| WildFly > Technical Control > Hazard > Exposed Voltage > Hazard | Exposed-voltage hazard. | Technical Control | `Technical Hazard` |
| WildFly > Technical Control > Hazard > Thermal Runaway > Hazard | Thermal-runaway hazard. | Technical Control | `Technical Hazard` |
| WildFly > Technical Control > Hazard > Race Condition > Hazard | Race-condition hazard. | Technical Control | `Technical Hazard` |
| WildFly > Technical Control > Hazard > Resource Exhaustion > Hazard | Resource-exhaustion hazard. | Technical Control | `Technical Hazard` |
| WildFly > Technical Control > Risk > Availability Risk > Risk | Availability risk. | Technical Control | `Technical Risk` |
| WildFly > Technical Control > Risk > Integrity Risk > Risk | Integrity risk. | Technical Control | `Technical Risk` |
| WildFly > Technical Control > Risk > Confidentiality Risk > Risk | Confidentiality risk. | Technical Control | `Technical Risk` |
| WildFly > Technical Control > Risk > Compliance Risk > Risk | Compliance risk. | Technical Control | `Technical Risk` |
| WildFly > Technical Control > Trade-off > Performance vs Energy > Trade-off | Performance-vs-energy trade-off. | Technical Control | `Technical Trade-off` |
| WildFly > Technical Control > Trade-off > Flexibility vs Complexity > Trade-off | Flexibility-vs-complexity trade-off. | Technical Control | `Technical Trade-off` |
| WildFly > Technical Control > Trade-off > Availability vs Consistency > Trade-off | Availability-vs-consistency trade-off. | Technical Control | `Technical Trade-off` |
| WildFly > Technical Control > Trade-off > Security vs Usability > Trade-off | Security-vs-usability trade-off. | Technical Control | `Technical Trade-off` |
| WildFly > Technical Control > Performance > Response Time > Measurement | Response-time measurement. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Performance > Throughput > Measurement | Throughput measurement. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Performance > Resource Consumption > Measurement | Resource-consumption measurement. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Availability > Uptime > Measurement | Uptime measurement. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Availability > Downtime > Measurement | Downtime measurement. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Throughput > Requests per Second > Metric | Requests-per-second metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Throughput > Bytes per Second > Metric | Bytes-per-second metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Latency > p50 > Metric | Median latency. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Latency > p95 > Metric | 95th-percentile latency. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Latency > p99 > Metric | 99th-percentile latency. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Resource Utilization > CPU Utilization > Metric | CPU-utilization metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Resource Utilization > Memory Utilization > Metric | Memory-utilization metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Resource Utilization > Disk Utilization > Metric | Disk-utilization metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Resource Utilization > Network Utilization > Metric | Network-utilization metric. | Mechanism & Capability | `Technical Performance` |
| WildFly > Technical Control > Error Rate > HTTP 5xx Rate > Rate | HTTP 5xx error rate. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Error Rate > Exception Rate > Rate | Exception rate. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Error Rate > Timeout Rate > Rate | Timeout rate. | Technical Control | `Technical Feedback` |
| WildFly > Technical Control > Saturation > Thread Pool Saturation > Saturation | Thread-pool saturation. | Technical Control | `Technical Performance` |
| WildFly > Technical Control > Saturation > Connection Pool Saturation > Saturation | Connection-pool saturation. | Technical Control | `Technical Performance` |
| WildFly > Technical Control > Saturation > Heap Saturation > Saturation | Heap saturation. | Technical Control | `Technical Performance` |
| WildFly > Technical Control > Saturation > Queue Saturation > Saturation | Queue saturation. | Technical Control | `Technical Performance` |
| WildFly > WildFly Ecosystem | Coherent body of server, tooling, configurations, and practices realizing managed Jakarta EE runtime capability. | System Structure | `Production Technical Element Set` |

## How are the Java EE / Jakarta EE specifications implemented?

| Specification | Description | Implementation Detail |
| --- | --- | --- |
| Jakarta Servlet | Server-side web components: servlets, filters, listeners. | Undertow Servlet Container, Servlet, Filter (`org.wildfly.extension.undertow`) |
| Jakarta REST | REST endpoints with content negotiation. | RESTEasy, REST Endpoint, Jackson / JSON-B / JSON-P Providers (`org.wildfly.extension.jaxrs`) |
| Jakarta Enterprise Beans | Managed components with pooling, timers, remoting. | EJB3 Container, EJB Pool, Timer Service (`org.wildfly.extension.ejb3`) |
| Jakarta Persistence | Object-relational persistence units and entity management. | JPA, Hibernate ORM, Entity Manager, Second-Level Cache (`org.wildfly.extension.jpa`) |
| Jakarta Messaging | Queues, topics, pooled connection factories. | Messaging-ActiveMQ Broker Server, Queue, Topic, Pooled Connection Factory (`org.wildfly.extension.messaging-activemq`) |
| Jakarta CDI | Bean discovery, injection, interceptors, decorators. | CDI / Weld Bean Discovery, Dependency Injection, Interceptor, Decorator (`org.wildfly.extension.weld`) |
| Jakarta Dependency Injection | Injectable types and qualifiers. | CDI / Weld Dependency Injection, Producer Method |
| Jakarta Interceptors | Interception around business methods and lifecycle events. | CDI / Weld Interceptor; EJB3 interceptors |
| Jakarta Transactions | Distributed transaction coordination and recovery. | Transaction Manager, XA Coordination, Recovery (`org.wildfly.extension.transactions`) |
| Jakarta Bean Validation | Constraint declarations and validation runtime. | Validator, Constraint (`org.wildfly.extension.bean-validation`) |
| Jakarta Batch | Chunked batch jobs with steps and repositories. | Batch JBeret Job, Step, Job Repository (`org.wildfly.extension.batch.jberet`) |
| Jakarta Concurrency | Managed executors and context propagation. | Managed Executor Service, Context Service (EE subsystem) |
| Jakarta Connectors | Resource adapters with activation and connection definitions. | Resource Adapters, Activation, `ra.xml`, `ironjacamar.xml` |
| Jakarta Mail | Mail sessions for message dispatch. | Mail Session (`org.wildfly.extension.mail`) |
| Jakarta WebSocket | Full-duplex socket endpoints. | Undertow WebSocket, HTTP/HTTPS Listeners |
| Jakarta JSON Binding | JSON serialization binding. | RESTEasy JSON-B Provider |
| Jakarta JSON Processing | Streaming and object JSON processing. | RESTEasy JSON-P Provider |
| Jakarta XML Binding | XML binding for payloads. | RESTEasy JAXB Provider |
| Jakarta XML Web Services | SOAP endpoints with WSDL and handler chains. | JAX-WS Endpoint, WSDL, Handler Chain (`org.wildfly.extension.webservices`) |
| Jakarta Faces | Component-based server-side UI. | JSF, Mojarra, `faces-config.xml` (`org.wildfly.extension.jsf`) |
| Jakarta Server Pages | JSP page execution in the web container. | Undertow Servlet Container JSP support (no dedicated Jasper rows in this table yet) |
| Jakarta Expression Language | Unified expression evaluation in pages and CDI. | Provided via Faces/CDI integration (no dedicated rows) |
| Jakarta Security | Application security constraints and identity stores. | Elytron Security Domain, Security Realm (`org.wildfly.extension.elytron`) |
| Jakarta Authentication | HTTP/SASL authentication mechanisms. | Elytron HTTP/SASL Authentication Factory, OIDC Client |
| Jakarta Authorization | Role and permission decisions. | Elytron Role Mapper, Permission Mapper |
| Jakarta Annotations | Metadata-driven configuration. | Deployment Annotation processing (Class/Method/Field Annotation) |
| Jakarta Activation | Activation framework for data content. | No dedicated subsystem (provided transitively via Mail) |
| Jakarta Management | Standardized management model. | Not implemented as such (management via DMR model, HTTP/Native interfaces, JMX) |
| Jakarta Deployment | Standard deployment tooling API. | Not implemented as such (deployment via Deployment Scanner, CLI, console) |
| JDBC | Relational access through managed pools. | Datasource, XA Datasource, Connection Pool, JDBC Driver (`org.wildfly.extension.datasources-agroal`) |
| JNDI | Naming and directory lookup. | Naming, JNDI Namespace, JNDI Binding (`org.wildfly.extension.naming`) |
| JMX | Managed beans and remote management. | MBean, MBean Server (`org.wildfly.extension.jmx`) |
| HTTP/HTTPS | Web transport listeners. | Undertow HTTP/HTTPS Listeners, Socket Binding |
| TLS | Transport security for endpoints and remoting. | Elytron TLS Configuration, Cipher Suite; Runtime Security TLS |
| MicroProfile Config/Health/Metrics | Externalized config, probes, telemetry. | MicroProfile Config/Health/Metrics (`org.wildfly.extension.microprofile.*-smallrye`, `…metrics`) |
| MicroProfile Fault Tolerance | Retries, bulkheads, circuit breaking. | Fault Tolerance mechanisms (`org.wildfly.extension.microprofile.fault-tolerance-smallrye`) |
| MicroProfile JWT | Token-based authentication. | JWT authentication capability (MicroProfile) |
| MicroProfile OpenAPI | API description generation. | OpenAPI generation (`org.wildfly.extension.microprofile.openapi-smallrye`) |
| MicroProfile Reactive Messaging | Reactive message channels. | Reactive Messaging capability (`org.wildfly.extension.microprofile.reactive-messaging-smallrye`) |
| OpenTelemetry | Distributed tracing and metrics export. | OpenTelemetry/Micrometer extensions, Metrics subsystem |

## Configuration File(s)

```csharp
- ls bin/standalone.sh
- ls bin/standalone.conf
- ls standalone/configuration/standalone.xml
```

## Admin User

```bash
./bin/add-user.sh
./bin/add-user.sh -u admin -p NEW_PASSWORD
```

## QA

### How does WildFly handle the situation when the user provides WildFly module libraries?

### What is the structure (Architecture) of Wildfly?

### What is a provider `org.jboss.resteasy.plugins.providers.jackson.ResteasyJackson2Provider`?

### What is the role of the web.xml, jboss-deployment-structure.xml and jboss-web.xml?

### What is JSON-B?

### How can we detect library drift between the development libraries (usually not the API) and the libraries provided by the application container?

### How to create the pom - dependency tree of a Maven Project?

### What is an application container? What characteristics must it have in order to be considered one?

## References

- [WildFly](https://www.wildfly.org/)
