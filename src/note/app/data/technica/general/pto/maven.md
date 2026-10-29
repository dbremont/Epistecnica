---
tags: [build-system, package-manager]
---

# Apache Maven

- [Build System](note.html?n=technica/computation/system/operation/operation-conceptual-model/build-system.md)

> In this note, we will explore **Apache Maven**, a technical system that allows developers to **specify build execution plans**—descriptions of the computations that a build engine must carry out to transform project sources and resources into build artifacts.
> 

> We will examine how Maven represents these plans, how they are declared in the **POM (Project Object Model)**, how Maven constructs an execution plan from that declaration, and how the Maven engine subsequently executes that plan.
> 

> **Note:** Maven is not a generic build system; it is specifically designed for Java and JVM-based projects. Consequently, Java- and JVM-specific artifacts, abstractions, and conventions are embedded in its model, including packaging types (`jar`, `war`, `ear`, etc.), the standard project directory structure, and the organization of source, test, resource, and build-output artifacts.
> 

> **Note:** The computation—or **build graph**—that can be specified in Maven is constrained by a predefined computational blueprint imposed by **Maven Core**, including its project model, lifecycle model, and execution engine. In other words, a Maven POM does not define an arbitrary computation graph; it declares a project within the computational model that Maven Core provides.
> 

## Formulation

### What is Maven?

### What type of technical element is ‘Maven’?

### What technical problems does maven solves?

### What are the technical roles of maven?

### Which are the technical capabilities of maven?

### How to  configure `Maven` ?

- What is the role of the **`settings.xml`** file in Maven?
- What is the grammar of **`settings.xml`** ?

## Interface

> How to interact with Maven?
> 

### Command Language

- What is the grammar (syntax) of the `mvn` command-line tool?
    - Which concepts help make that grammar intelligible?
    - What it’s the semantics?
- `mvn [options] [<goal(s)>] [<phase(s)>]`  →  `[<goal(s)>] [<phase(s)>]`  `->` `[target]`
    - **Target** → a lifecycle phase, a plugin goal, or a plugin:goal invocation

#### Which is the target space in `mvn <target>`?

> **Note:** The term **target** is introduced in this note as a generic term for the argument supplied to Maven after `mvn`, usually expressed using a mnemonic name. A target may designate a **lifecycle phase** (e.g., `compile`, `test`, `package`, `install`), a **plugin goal** (e.g., `compiler:compile`, `install:install`), or, more generally, a **concrete plugin goal** identified by its fully qualified plugin coordinates  (e.g., `org.apache.maven.plugins:maven-resources-plugin:resources`). Thus, **target** is used here as an umbrella term for the executable specification supplied in a Maven invocation.
> 

| Target | Type | Description | Concrete Plugin Goal Execution Sequence |
| --- | --- | --- | --- |
| `validate` | Lifecycle phase | Validate the project | — **(no default plugin goal; may be bound in the POM)** |
| `initialize` | Lifecycle phase | Initialize build state | — **(no default plugin goal; may be bound in the POM)** |
| `generate-sources` | Lifecycle phase | Generate source code | — **(no default plugin goal; may be bound in the POM)** |
| `process-sources` | Lifecycle phase | Process source code | — **(no default plugin goal; may be bound in the POM)** |
| `generate-resources` | Lifecycle phase | Generate resources | — **(no default plugin goal; may be bound in the POM)** |
| `process-resources` | Lifecycle phase | Process main resources | `org.apache.maven.plugins:maven-resources-plugin:resources` (`resources:resources`) |
| `compile` | Lifecycle phase | Compile main source code | `org.apache.maven.plugins:maven-resources-plugin:resources` (`resources:resources`) → `org.apache.maven.plugins:maven-compiler-plugin:compile` (`compiler:compile`) |
| `process-classes` | Lifecycle phase | Process compiled classes | `org.apache.maven.plugins:maven-resources-plugin:resources` (`resources:resources`) → `org.apache.maven.plugins:maven-compiler-plugin:compile` (`compiler:compile`) |
| `generate-test-sources` | Lifecycle phase | Generate test sources | `org.apache.maven.plugins:maven-resources-plugin:resources` (`resources:resources`) → `org.apache.maven.plugins:maven-compiler-plugin:compile` (`compiler:compile`) |
| `process-test-sources` | Lifecycle phase | Process test sources | `org.apache.maven.plugins:maven-resources-plugin:resources` (`resources:resources`) → `org.apache.maven.plugins:maven-compiler-plugin:compile` (`compiler:compile`) |
| `generate-test-resources` | Lifecycle phase | Generate test resources | `org.apache.maven.plugins:maven-resources-plugin:resources` (`resources:resources`) → `org.apache.maven.plugins:maven-compiler-plugin:compile` (`compiler:compile`) |
| `process-test-resources` | Lifecycle phase | Process test resources | `org.apache.maven.plugins:maven-resources-plugin:resources` (`resources:resources`) → `org.apache.maven.plugins:maven-compiler-plugin:compile` (`compiler:compile`) → `org.apache.maven.plugins:maven-resources-plugin:testResources` (`resources:testResources`) |
| remote-resources:process |  |  |  |
| assembly:single |  |  |  |

### Which are the default lifecycles, and what goal-execution sequence does each define?

| Lifecycle | Description | Goal (Phase) Sequence |
| --- | --- | --- |
| **`default`** | The primary lifecycle for building and packaging a project. | `validate → initialize → generate-sources → process-sources → generate-resources → process-resources → compile → process-classes → generate-test-sources → process-test-sources → generate-test-resources → process-test-resources → test-compile → process-test-classes → test → prepare-package → package → pre-integration-test → integration-test → post-integration-test → verify → install → deploy` |
| **`clean`** | Removes artifacts generated by previous builds. | `pre-clean → clean → post-clean` |
| **`site`** | Generates project documentation and the Maven project site. | `pre-site → site → post-site → site-deploy` |

### Project Language

> See [Project Object Model](#sec-project-object-model).
> 

### Practice

> How to used maven?
> 
1. **What are some best practices for managing dependencies in Maven?**
    - How do you avoid dependency hell?
2. **How do you ensure reproducible builds in Maven?**
    - What is the role of the `maven-enforcer-plugin` and the `dependency-lock` feature?
3. **What is the purpose of the `maven-release-plugin`?**
    - How do you automate the release process using this plugin?

## Project Object Model

### What is `pom.xml`?

> `pom.xml` is the XML serialization of a Maven **Project Object Model (POM)**.
> 

### What kinds of **computations** are expressed by **`pom.xml`**?

> A `pom.xml` is a computational-description artifact that describes a specialized type of computation graph: a software-project build graph.
> 

> What **computational model** is imposed by the **`pom.xml`** mechanism? `pom.xml` imposes a declarative descriptive model for software-project computations: a Maven project/build model.
> 

### How flexible is an execution plan by `pom.xml`? Does Maven impose certain bounds or constraints on the plans that can be specified (e.g., through a schema, template, or blueprint), or can one specify an arbitrary build plan?

> **Maven does not allow an arbitrary execution plan to be specified directly in the `pom.xml`, as a general-purpose workflow or DAG engine would.** Instead, Maven's execution model is highly extensible but remains constrained by its **lifecycle model, plugin architecture, and lifecycle bindings**. The `pom.xml` configures and extends these mechanisms rather than defining an unconstrained execution graph.
> 

> **Conceptually:**  Project Description + Lifecycle Model + Lifecycle Bindings + Plugin Configuration → Execution Plan.
> 

### What is the grammar of `pom.xml` in `ISO-14977 EBNF`?

> In order to visualized used - [https://matthijsgroen.github.io/ebnf2railroad/try-yourself.html#Execution](https://matthijsgroen.github.io/ebnf2railroad/try-yourself.html#Execution) or [https://www.bottlecaps.de/rr/ui](https://www.bottlecaps.de/rr/ui).
> 

```bash
POM
    ::= XMLDeclaration? Project

Project
    ::= "<project" ProjectAttributes ">"
            ModelVersion
            Parent?
            Coordinates
            ProjectMetadata?
            Organization?
            Licenses?
            Developers?
            Contributors?
            MailingLists?
            Prerequisites?
            Modules?
            SCM?
            IssueManagement?
            CIManagement?
            DistributionManagement?
            Properties?
            DependencyManagement?
            Dependencies?
            Repositories?
            PluginRepositories?
            Build?
            Reporting?
            Profiles?
        "</project>"

ProjectAttributes
    ::= Namespace
        XsiNamespace?
        SchemaLocation?

ModelVersion
    ::= "<modelVersion>" "4.0.0" "</modelVersion>"

Parent
    ::= "<parent>"
            GroupId
            ArtifactId
            Version
            RelativePath?
        "</parent>"

Coordinates
    ::= GroupId?
        ArtifactId
        Version?
        Packaging?

GroupId
    ::= "<groupId>" CoordinateValue "</groupId>"

ArtifactId
    ::= "<artifactId>" CoordinateValue "</artifactId>"

Version
    ::= "<version>" VersionValue "</version>"

Packaging
    ::= "<packaging>" PackagingValue "</packaging>"

RelativePath
    ::= "<relativePath>" Path "</relativePath>"

ProjectMetadata
    ::= Name?
        Description?
        URL?
        InceptionYear?

Name
    ::= "<name>" Text "</name>"

Description
    ::= "<description>" Text "</description>"

URL
    ::= "<url>" URI "</url>"

InceptionYear
    ::= "<inceptionYear>" Text "</inceptionYear>"

Organization
    ::= "<organization>"
            OrganizationName?
            OrganizationURL?
        "</organization>"

OrganizationName
    ::= "<name>" Text "</name>"

OrganizationURL
    ::= "<url>" URI "</url>"

Licenses
    ::= "<licenses>"
            License*
        "</licenses>"

License
    ::= "<license>"
            LicenseName
            LicenseURL?
            LicenseDistribution?
            LicenseComments?
        "</license>"

LicenseName
    ::= "<name>" Text "</name>"

LicenseURL
    ::= "<url>" URI "</url>"

LicenseDistribution
    ::= "<distribution>" Text "</distribution>"

LicenseComments
    ::= "<comments>" Text "</comments>"

Developers
    ::= "<developers>"
            Developer*
        "</developers>"

Developer
    ::= "<developer>"
            DeveloperID?
            DeveloperName?
            DeveloperEmail?
            DeveloperURL?
            DeveloperOrganization?
            DeveloperOrganizationURL?
            DeveloperRoles?
            DeveloperTimezone?
            DeveloperProperties?
        "</developer>"

DeveloperID
    ::= "<id>" Text "</id>"

DeveloperName
    ::= "<name>" Text "</name>"

DeveloperEmail
    ::= "<email>" Text "</email>"

DeveloperURL
    ::= "<url>" URI "</url>"

DeveloperOrganization
    ::= "<organization>" Text "</organization>"

DeveloperOrganizationURL
    ::= "<organizationUrl>" URI "</organizationUrl>"

DeveloperRoles
    ::= "<roles>"
            Role*
        "</roles>"

Role
    ::= "<role>" Text "</role>"

DeveloperTimezone
    ::= "<timezone>" Text "</timezone>"

DeveloperProperties
    ::= "<properties>"
            Property*
        "</properties>"

Contributors
    ::= "<contributors>"
            Contributor*
        "</contributors>"

Contributor
    ::= "<contributor>"
            ContributorName?
            ContributorEmail?
            ContributorURL?
            ContributorOrganization?
            ContributorOrganizationURL?
            ContributorRoles?
            ContributorTimezone?
            ContributorProperties?
        "</contributor>"

MailingLists
    ::= "<mailingLists>"
            MailingList*
        "</mailingLists>"

MailingList
    ::= "<mailingList>"
            MailingListName
            MailingListSubscribe?
            MailingListUnsubscribe?
            MailingListPost?
            MailingListArchive?
        "</mailingList>"

Prerequisites
    ::= "<prerequisites>"
            MavenVersion?
        "</prerequisites>"

MavenVersion
    ::= "<maven>" VersionValue "</maven>"

Modules
    ::= "<modules>"
            Module*
        "</modules>"

Module
    ::= "<module>" Path "</module>"

SCM
    ::= "<scm>"
            Connection?
            DeveloperConnection?
            Tag?
            URL?
            Revision?
        "</scm>"

Connection
    ::= "<connection>" Text "</connection>"

DeveloperConnection
    ::= "<developerConnection>" Text "</developerConnection>"

Tag
    ::= "<tag>" Text "</tag>"

Revision
    ::= "<revision>" Text "</revision>"

IssueManagement
    ::= "<issueManagement>"
            IssueSystem?
            IssueURL?
        "</issueManagement>"

IssueSystem
    ::= "<system>" Text "</system>"

IssueURL
    ::= "<url>" URI "</url>"

CIManagement
    ::= "<ciManagement>"
            CISystem?
            CIURL?
            CINotifiers?
        "</ciManagement>"

CISystem
    ::= "<system>" Text "</system>"

CIURL
    ::= "<url>" URI "</url>"

CINotifiers
    ::= "<notifiers>"
            Notifier*
        "</notifiers>"

Notifier
    ::= "<notifier>"
            NotifierType?
            NotifierSendOnError?
            NotifierSendOnFailure?
            NotifierSendOnSuccess?
            NotifierSendOnWarning?
            NotifierConfiguration?
        "</notifier>"

NotifierType
    ::= "<type>" Text "</type>"

NotifierSendOnError
    ::= "<sendOnError>" Boolean "</sendOnError>"

NotifierSendOnFailure
    ::= "<sendOnFailure>" Boolean "</sendOnFailure>"

NotifierSendOnSuccess
    ::= "<sendOnSuccess>" Boolean "</sendOnSuccess>"

NotifierSendOnWarning
    ::= "<sendOnWarning>" Boolean "</sendOnWarning>"

NotifierConfiguration
    ::= Configuration

DistributionManagement
    ::= "<distributionManagement>"
            Repository?
            SnapshotRepository?
            Site?
            Relocation?
            DownloadURL?
            Status?
        "</distributionManagement>"

Repository
    ::= "<repository>"
            RepositoryID?
            RepositoryName?
            RepositoryURL
            RepositoryLayout?
            RepositoryReleases?
            RepositorySnapshots?
        "</repository>"

SnapshotRepository
    ::= "<snapshotRepository>"
            RepositoryID?
            RepositoryName?
            RepositoryURL
            RepositoryLayout?
            RepositoryReleases?
            RepositorySnapshots?
        "</snapshotRepository>"

RepositoryID
    ::= "<id>" Text "</id>"

RepositoryName
    ::= "<name>" Text "</name>"

RepositoryURL
    ::= "<url>" URI "</url>"

RepositoryLayout
    ::= "<layout>" LayoutValue "</layout>"

RepositoryReleases
    ::= "<releases>"
            Enabled?
            UpdatePolicy?
            ChecksumPolicy?
        "</releases>"

RepositorySnapshots
    ::= "<snapshots>"
            Enabled?
            UpdatePolicy?
            ChecksumPolicy?
        "</snapshots>"

Enabled
    ::= "<enabled>" Boolean "</enabled>"

UpdatePolicy
    ::= "<updatePolicy>" Text "</updatePolicy>"

ChecksumPolicy
    ::= "<checksumPolicy>" Text "</checksumPolicy>"

Site
    ::= "<site>"
            SiteID?
            SiteName?
            SiteURL
        "</site>"

SiteID
    ::= "<id>" Text "</id>"

SiteName
    ::= "<name>" Text "</name>"

SiteURL
    ::= "<url>" URI "</url>"

Relocation
    ::= "<relocation>"
            RelocationGroupId?
            RelocationArtifactId?
            RelocationVersion?
            RelocationMessage?
        "</relocation>"

RelocationGroupId
    ::= "<groupId>" CoordinateValue "</groupId>"

RelocationArtifactId
    ::= "<artifactId>" CoordinateValue "</artifactId>"

RelocationVersion
    ::= "<version>" VersionValue "</version>"

RelocationMessage
    ::= "<message>" Text "</message>"

DownloadURL
    ::= "<downloadUrl>" URI "</downloadUrl>"

Status
    ::= "<status>" Text "</status>"

Properties
    ::= "<properties>"
            Property*
        "</properties>"

Property
    ::= "<" PropertyName ">"
            PropertyValue
        "</" PropertyName ">"

PropertyName
    ::= XMLName

PropertyValue
    ::= Text

DependencyManagement
    ::= "<dependencyManagement>"
            Dependencies
        "</dependencyManagement>"

Dependencies
    ::= "<dependencies>"
            Dependency*
        "</dependencies>"

Dependency
    ::= "<dependency>"
            DependencyGroupId?
            DependencyArtifactId
            DependencyVersion?
            DependencyType?
            DependencyClassifier?
            DependencyScope?
            Optional?
            Exclusions?
        "</dependency>"

DependencyGroupId
    ::= "<groupId>" CoordinateValue "</groupId>"

DependencyArtifactId
    ::= "<artifactId>" CoordinateValue "</artifactId>"

DependencyVersion
    ::= "<version>" VersionValue "</version>"

DependencyType
    ::= "<type>" Text "</type>"

DependencyClassifier
    ::= "<classifier>" Text "</classifier>"

DependencyScope
    ::= "<scope>" ScopeValue "</scope>"

Optional
    ::= "<optional>" Boolean "</optional>"

Exclusions
    ::= "<exclusions>"
            Exclusion*
        "</exclusions>"

Exclusion
    ::= "<exclusion>"
            ExclusionGroupId?
            ExclusionArtifactId?
        "</exclusion>"

ExclusionGroupId
    ::= "<groupId>" CoordinateValue "</groupId>"

ExclusionArtifactId
    ::= "<artifactId>" CoordinateValue "</artifactId>"

Repositories
    ::= "<repositories>"
            Repository*
        "</repositories>"

PluginRepositories
    ::= "<pluginRepositories>"
            PluginRepository*
        "</pluginRepositories>"

PluginRepository
    ::= "<pluginRepository>"
            RepositoryID?
            RepositoryName?
            RepositoryURL
            RepositoryLayout?
            RepositoryReleases?
            RepositorySnapshots?
        "</pluginRepository>"

Build
    ::= "<build>"
            BuildExtensions?
            BuildDefaultGoal?
            BuildDirectory?
            BuildFinalName?
            BuildResources?
            BuildTestResources?
            BuildSourceDirectory?
            BuildTestSourceDirectory?
            BuildScriptSourceDirectory?
            BuildOutputDirectory?
            BuildTestOutputDirectory?
            BuildFilters?
            BuildPluginManagement?
            BuildPlugins?
        "</build>"

BuildExtensions
    ::= "<extensions>"
            Extension*
        "</extensions>"

Extension
    ::= "<extension>"
            ExtensionGroupId
            ExtensionArtifactId
            ExtensionVersion
        "</extension>"

BuildDefaultGoal
    ::= "<defaultGoal>" Text "</defaultGoal>"

BuildDirectory
    ::= "<directory>" Path "</directory>"

BuildFinalName
    ::= "<finalName>" Text "</finalName>"

BuildResources
    ::= "<resources>"
            Resource*
        "</resources>"

BuildTestResources
    ::= "<testResources>"
            Resource*
        "</testResources>"

Resource
    ::= "<resource>"
            ResourceTargetPath?
            ResourceFiltering?
            ResourceDirectory?
            ResourceIncludes?
            ResourceExcludes?
        "</resource>"

ResourceTargetPath
    ::= "<targetPath>" Path "</targetPath>"

ResourceFiltering
    ::= "<filtering>" Boolean "</filtering>"

ResourceDirectory
    ::= "<directory>" Path "</directory>"

ResourceIncludes
    ::= "<includes>"
            Include*
        "</includes>"

ResourceExcludes
    ::= "<excludes>"
            Exclude*
        "</excludes>"

Include
    ::= "<include>" PathPattern "</include>"

Exclude
    ::= "<exclude>" PathPattern "</exclude>"

BuildFilters
    ::= "<filters>"
            Filter*
        "</filters>"

Filter
    ::= "<filter>" Path "</filter>"

BuildPluginManagement
    ::= "<pluginManagement>"
            Plugins
        "</pluginManagement>"

BuildPlugins
    ::= "<plugins>"
            Plugin*
        "</plugins>"

Plugins
    ::= "<plugins>"
            Plugin*
        "</plugins>"

Plugin
    ::= "<plugin>"
            PluginGroupId?
            PluginArtifactId
            PluginVersion?
            PluginExtensions?
            PluginExecutions?
            PluginDependencies?
            PluginGoals?
            PluginConfiguration?
        "</plugin>"

PluginGroupId
    ::= "<groupId>" CoordinateValue "</groupId>"

PluginArtifactId
    ::= "<artifactId>" CoordinateValue "</artifactId>"

PluginVersion
    ::= "<version>" VersionValue "</version>"

PluginExtensions
    ::= "<extensions>" Boolean "</extensions>"

PluginExecutions
    ::= "<executions>"
            Execution*
        "</executions>"

Execution
    ::= "<execution>"
            ExecutionID?
            ExecutionPhase?
            ExecutionGoals?
            ExecutionConfiguration?
        "</execution>"

ExecutionID
    ::= "<id>" Text "</id>"

ExecutionPhase
    ::= "<phase>" Text "</phase>"

ExecutionGoals
    ::= "<goals>"
            Goal*
        "</goals>"

Goal
    ::= "<goal>" Text "</goal>"

PluginDependencies
    ::= "<dependencies>"
            Dependency*
        "</dependencies>"

PluginGoals
    ::= "<goals>"
            Goal*
        "</goals>"

PluginConfiguration
    ::= "<configuration>"
            ConfigurationElement*
        "</configuration>"

ExecutionConfiguration
    ::= Configuration

Configuration
    ::= "<configuration>"
            ConfigurationElement*
        "</configuration>"

ConfigurationElement
    ::= XMLConfigurationElement

XMLConfigurationElement
    ::= "<" XMLName ConfigurationAttributes? ">"
            ConfigurationContent*
        "</" XMLName ">"
      | "<" XMLName ConfigurationAttributes? "/>"

ConfigurationContent
    ::= Text
      | XMLConfigurationElement

Reporting
    ::= "<reporting>"
            ReportingExcludeDefaults?
            ReportingOutputDirectory?
            ReportingPlugins?
        "</reporting>"

ReportingExcludeDefaults
    ::= "<excludeDefaults>" Boolean "</excludeDefaults>"

ReportingOutputDirectory
    ::= "<outputDirectory>" Path "</outputDirectory>"

ReportingPlugins
    ::= "<plugins>"
            ReportPlugin*
        "</plugins>"

ReportPlugin
    ::= "<plugin>"
            ReportPluginGroupId?
            ReportPluginArtifactId
            ReportPluginVersion?
            ReportPluginReportSets?
            ReportPluginConfiguration?
        "</plugin>"

ReportPluginGroupId
    ::= "<groupId>" CoordinateValue "</groupId>"

ReportPluginArtifactId
    ::= "<artifactId>" CoordinateValue "</artifactId>"

ReportPluginVersion
    ::= "<version>" VersionValue "</version>"

ReportPluginReportSets
    ::= "<reportSets>"
            ReportSet*
        "</reportSets>"

ReportSet
    ::= "<reportSet>"
            ReportSetID?
            ReportSetInherited?
            ReportSetReports?
            ReportSetConfiguration?
        "</reportSet>"

ReportSetID
    ::= "<id>" Text "</id>"

ReportSetInherited
    ::= "<inherited>" Boolean "</inherited>"

ReportSetReports
    ::= "<reports>"
            Report*
        "</reports>"

Report
    ::= "<report>" Text "</report>"

ReportSetConfiguration
    ::= Configuration

ReportPluginConfiguration
    ::= Configuration

Profiles
    ::= "<profiles>"
            Profile*
        "</profiles>"

Profile
    ::= "<profile>"
            ProfileID?
            Activation?
            ProfileBuild?
            ProfileModules?
            ProfileDistributionManagement?
            ProfileProperties?
            ProfileDependencyManagement?
            ProfileDependencies?
            ProfileRepositories?
            ProfilePluginRepositories?
            ProfileReporting?
        "</profile>"

ProfileID
    ::= "<id>" Text "</id>"

Activation
    ::= "<activation>"
            ActiveByDefault?
            JDK?
            OS?
            PropertyActivation?
            FileActivation?
        "</activation>"

ActiveByDefault
    ::= "<activeByDefault>" Boolean "</activeByDefault>"

JDK
    ::= "<jdk>" Text "</jdk>"

OS
    ::= "<os>"
            OSName?
            OSFamily?
            OSArch?
            OSVersion?
        "</os>"

OSName
    ::= "<name>" Text "</name>"

OSFamily
    ::= "<family>" Text "</family>"

OSArch
    ::= "<arch>" Text "</arch>"

OSVersion
    ::= "<version>" Text "</version>"

PropertyActivation
    ::= "<property>"
            ActivationName?
            ActivationValue?
        "</property>"

ActivationName
    ::= "<name>" Text "</name>"

ActivationValue
    ::= "<value>" Text "</value>"

FileActivation
    ::= "<file>"
            FileExists?
            FileMissing?
        "</file>"

FileExists
    ::= "<exists>" Path "</exists>"

FileMissing
    ::= "<missing>" Path "</missing>"

ProfileBuild
    ::= Build

ProfileModules
    ::= Modules

ProfileDistributionManagement
    ::= DistributionManagement

ProfileProperties
    ::= Properties

ProfileDependencyManagement
    ::= DependencyManagement

ProfileDependencies
    ::= Dependencies

ProfileRepositories
    ::= Repositories

ProfilePluginRepositories
    ::= PluginRepositories

ProfileReporting
    ::= Reporting

Boolean
    ::= "true"
      | "false"

PackagingValue
    ::= "pom"
      | "jar"
      | "war"
      | "ear"
      | "ejb"
      | "rar"
      | "par"
      | Text

ScopeValue
    ::= "compile"
      | "provided"
      | "runtime"
      | "test"
      | "system"
      | "import"

LayoutValue
    ::= "default"
      | "legacy"
      | Text

CoordinateValue
    ::= Text

VersionValue
    ::= Text

Path
    ::= Text

PathPattern
    ::= Text

URI
    ::= Text

Text
    ::= XMLText

XMLName
    ::= XMLNameStart XMLNameChar*

XMLNameStart
    ::= Letter
      | "_"
      | ":"

XMLNameChar
    ::= Letter
      | Digit
      | "."
      | "-"
      | "_"
      | ":"
```

### How are the dependencies specified?

### **What is the difference between a dependency and a dependencyManagement section in the `pom.xml`?**

### **What is dependency scope in Maven?** Can you explain the differences between `compile`, `provided`, `runtime`, `test`, and `system` scopes?

> 

### **How does Maven resolve dependency conflicts?**

> 

### What  is a maven profile?

> 

## Repository System

1. **What is the difference between a local repository and a remote repository?**
2. Where is the local repository located, and how does Maven use it?
3. **How do you configure a custom remote repository in Maven?**
4. What is the difference between a `repository` and a `pluginRepository`?
5. **What is a Maven mirror?**
6. How do you configure a mirror in the `settings.xml` file?

> A repository is a directory where all the project jars, library jar, plugins or any other project specific artifacts are stored and can be used by Maven easily.
> 

**Types**:

- **local** (Maven local repository is a folder location on your machine.)
- **central** (Maven central repository is repository provided by Maven community. It contains a large number of commonly used libraries.)
- **remote** (Maven provides concept of Remote Repository, which is developer’s own custom repository containing required libraries or other project jars.)

## Execution

- How to inspect and debug the execution?
- What is the map - between the target (goal, phase) → `pluging:goal set`?
- Should I use the concept of a **mnemonic target** for something like `clean`, and **explicit target** for `maven-clean-plugin:clean`?
- How can I determine which Maven plugins and goals are available to a project? Are plugins and goals project-specific, or are they provided by the Maven installation and the machine environment?

## Implementation

- How is maven implemented?
- How are lifecycle implemented?
- What is the architecture of maven?

## Extensibility

> How can maven be extended?
> 

### Plugin System

#### What is a Maven plugin?

> A Maven plugin is a component that provides **goals**—executable units of build functionality that Maven can invoke.
> 

#### How do you create a Maven plugin?

> A Maven plugin is created as a Maven project whose packaging is `maven-plugin`. Its implementation consists of one or more **Mojo** classes, with each Mojo implementing a particular goal.
> 

#### Which interface(s) does a Maven plugin implement?

The fundamental executable unit is the **Mojo** (`org.apache.maven.plugin.Mojo`). A concrete Mojo normally extends Maven's `AbstractMojo`, which provides a convenient base implementation.

So, more precisely:

- **Plugin** → contains one or more goals.
- **Goal implementation** → a Mojo.
- **Mojo** → implements `org.apache.maven.plugin.Mojo`

#### How does a Maven plugin integrate with the Maven technical system?

Integration occurs through several mechanisms:

- The plugin is packaged as a Maven artifact, normally with `maven-plugin` packaging.
- Maven discovers/resolves the plugin from its coordinates (`groupId`, `artifactId`, `version`).
- The plugin descriptor (`META-INF/maven/plugin.xml`) describes its goals and configuration.
- Maven loads the plugin and its dependencies using its classloader infrastructure.
- Each goal is represented by a Mojo implementation.
- Maven invokes the Mojo when the corresponding goal is explicitly requested or when that goal is **bound to a lifecycle phase**.

### **Which are the Plugin Space?**

> Which are the most commonly used Maven plugins?
> 

| Plugin | Description | Goals (set) |
| --- | --- | --- |
| `maven-clean-plugin` | Cleans build artifacts | `{ clean }` |
| `maven-resources-plugin` | Copies project resources | `{ resources, testResources, copy-resources }` |
| `maven-remote-resources-plugin` | Processes resources obtained from remote resource bundles | `{ process }` |
| `maven-compiler-plugin` | Compiles Java source | `{ compile, testCompile }` |
| `maven-surefire-plugin` | Runs unit tests | `{ test }` |
| `maven-failsafe-plugin` | Runs integration tests | `{ integration-test, verify }` |
| `maven-jar-plugin` | Creates JAR artifacts | `{ jar, test-jar }` |
| `maven-war-plugin` | Creates WAR artifacts | `{ war, exploded, inplace }` |
| `maven-install-plugin` | Installs artifacts in local repository | `{ install, install-file }` |
| `maven-deploy-plugin` | Deploys artifacts to remote repository | `{ deploy, deploy-file }` |
| `maven-dependency-plugin` | Manages/analyzes dependencies | `{ tree, copy, unpack, analyze, ... }` |
| `maven-enforcer-plugin` | Enforces project/build rules | `{ enforce, display-info }` |
| `maven-assembly-plugin` | Builds distributable assemblies | `{ single, assembly }` |
| `maven-shade-plugin` | Creates shaded/uber JARs | `{ shade }` |
| `maven-javadoc-plugin` | Generates JavaDoc | `{ javadoc, jar, test-javadoc, ... }` |
| `maven-site-plugin` | Generates project sites | `{ site, deploy }` |
| `maven-ear-plugin` | Packages enterprise applications as EAR files | `{ ear, generate-application-xml, ... }` |
| `maven-release-plugin` | Manages project releases and versioning | `{ prepare, perform, rollback, ... }` |
| `maven-checkstyle-plugin` | Checks Java source code against Checkstyle rules | `{ check, checkstyle, ... }` |
| `maven-pmd-plugin` | Performs static analysis using PMD | `{ check, pmd, cpd, ... }` |
| `jacoco-maven-plugin` | Generates and reports code coverage | `{ prepare-agent, report, check, ... }` |
| `maven-archetype-plugin` | Generates projects from Maven archetypes | `{ generate, create-from-project, ... }` |
| `maven-source-plugin` |  |  |

## Performance

> **How can Maven builds be made faster?**
> 
1. **How does Maven resolve dependencies during the build process?**
    - What is the role of the `~/.m2/repository` directory?
2. **What is the Maven build lifecycle in terms of its internal implementation?**
    - How does Maven execute phases and goals internally?
3. **How can you improve Maven build performance?**
    - What are some best practices for reducing build time (e.g., parallel builds, offline mode)?

## QA

- How does Java resolve class and type references? How does it locate classes and JARs during compilation and runtime?
- How does Maven manage a multi-module project?
- How do Maven plugins register their mnemonic names?
- How do you handle multi-environment builds (e.g., dev, test, prod) in Maven?
- How do you integrate Maven with CI/CD tools like Jenkins, GitLab CI, or GitHub Actions?
- How do you handle environment-specific configurations in a CI/CD pipeline?
- How does Maven compare to Gradle in terms of flexibility and performance?
- How can I identify the set of plugin goals bound to a given lifecycle phase?

### Which are the most useful small snippets or one-liners for Maven?

- -   `mvn remote-resources:process assembly:single -Prapido` .
- `mvn help:effective-pom`
- Hello World App:  `mvn archetype:generate -DgroupId=com.sample.app -DartifactId=sample -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.5 -DinteractiveMode=false`
- How to get the help for a specific plugin? `mvn help:describe -Dplugin=org.apache.maven.plugins:maven-compiler-plugin`
- See the maven profiles:  `mvn help:active-profiles`

### Can we consider Maven's terminology of “lifecycle” and “phase” to be conceptually problematic?

> Maven defines a lifecycle as an ordered sequence of phases. However, in the command-line interface, specifying a lifecycle phase as a target triggers the execution of that phase and all preceding phases, resulting in the execution of a cumulative sequence of plugin goals.
> 

> `mvn compile` triggers the execution of the `compile` lifecycle phase and all preceding phases in the lifecycle, namely `validate`, `initialize`, `generate-sources`, `process-sources`, `generate-resources`, and `process-resources`.
> 

### Can a plugin create its own target mnemonics?

> A plugin can introduce new target mnemonics through its plugin-goal names and plugin prefix, but it cannot introduce new lifecycle-phase mnemonics.
> 

> This are ban - Lifecycle phases (`validate`, `compile`, `test`, `package`, etc.) belong to Maven's lifecycle model.
> 

### How to see the concrete plugin of a target (argument)?

> There is no simple, direct command; several options are available:
> 

Several Options:

- `mvn help:effective-pom`
- `mvn package -X`   - Execute and see.

### How to see the goals of a Plugin?

> `mvn <plugin-prefix>:help -Ddetail`
> 

### How to see all of the plugins used by a specific `pom.xml`?

> **Note:** `xmllint` is provided by the `libxml2-utils` package on Debian/Ubuntu.
> 

```bash
mvn help:effective-pom -Doutput=/tmp/effective-pom.xml
xmllint --xpath \                                                                                                                         [12:48:30]
  '//*[local-name()="plugin"]/*[local-name()="artifactId"]/text()' \
  /tmp/effective-pom.xml | sort | uniq  
```

### Does every lifecycle phase have to be explicitly mapped to a `plugin:goal` in the `pom.xml`?

> **No. Not every lifecycle-phase-to-goal mapping has to be explicitly declared in the `pom.xml`.** Maven provides **default lifecycle bindings** based on the project's **packaging type**. For example, for `jar` packaging, Maven's default lifecycle bindings associate phases such as `compile`, `test`, and `package` with specific plugin goals.
> 

> You only need to declare a phase-to-goal mapping explicitly in the `pom.xml` when you want to **override, extend, or customize** Maven's default bindings.
> 

### How can I list the lifecycle phase → plugin goal mappings for a Maven project?

```bash
EFFECTIVE_POM="${1:-/tmp/effective-pom.xml}"

if [[ -f "$EFFECTIVE_POM" ]]; then
    echo "Using existing effective POM: $EFFECTIVE_POM"
else
    echo "Generating effective POM..."
    mvn help:effective-pom -Doutput="$EFFECTIVE_POM" -q
fi

echo
echo "Lifecycle phase -> plugin:goal"
echo "---------------------------------------------"

count=$(xmllint --xpath \
    'count(//*[local-name()="plugin"]/*[local-name()="executions"]/*[local-name()="execution"])' \
    "$EFFECTIVE_POM")

for ((i=1; i<=count; i++)); do

    phase=$(xmllint --xpath \
        "string((//*[local-name()='plugin']/*[local-name()='executions']/*[local-name()='execution'])[$i]/*[local-name()='phase'])" \
        "$EFFECTIVE_POM")

    plugin=$(xmllint --xpath \
        "string((//*[local-name()='plugin']/*[local-name()='executions']/*[local-name()='execution'])[$i]/ancestor::*[local-name()='plugin'][1]/*[local-name()='artifactId'])" \
        "$EFFECTIVE_POM")

    goals=$(xmllint --xpath \
        "((//*[local-name()='plugin']/*[local-name()='executions']/*[local-name()='execution'])[$i]/*[local-name()='goals']/*[local-name()='goal']/text())" \
        "$EFFECTIVE_POM" 2>/dev/null || true)

    if [[ -n "$phase" && -n "$plugin" && -n "$goals" ]]; then
        while IFS= read -r goal; do
            [[ -n "$goal" ]] &&
                printf '%-20s -> %s:%s\n' "$phase" "$plugin" "$goal"
        done <<< "$goals"
    fi
done
```

### What does the term MOJO stand for?

> **MOJO** is Maven terminology for **“Maven plain Old Java Object.”**
> 

> **Mojo** is the Java object that implements a **Maven goal**.
> 

```bash
Maven Plugin
    │
    ├── Goal: compile
    │      └── Mojo implementation
    │
    ├── Goal: test
    │      └── Mojo implementation
    │
    └── Goal: package
           └── Mojo implementation
```

> Plugin → provides goals → each goal is implemented by a Mojo.
> 

### **What directory structure does Maven expect?**

> Note:  This can be change - but this is the default.
> 

```bash
project/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/          # Application source code
│   │   └── resources/     # Application resources
│   │
│   └── test/
│       ├── java/          # Test source code
│       └── resources/     # Test resources
│
└── target/                # Generated build output
```

### Which tools to used to visualize a grammar?

| Tool | Description | Capability Set |
| --- | --- | --- |
| **DrawGrammar** | Converts grammar productions into **railroad diagrams**. Designed specifically for visual grammar representation. | **EBNF visualization** · Railroad diagrams · Quick grammar exploration |
| **Mermaid Railroad Diagrams** | Provides a railroad-diagram syntax for representing EBNF-style constructs such as optionality, repetition, alternatives, and grouping. | **Documentation** · Markdown · Diagrams-as-code · EBNF-style syntax |
| **EBNF 2 Railroad** | Online EBNF editor that generates a documentation page containing railroad diagrams and navigation between grammar rules. | **Interactive editing** · EBNF visualization · Documentation generation · Rule navigation |
| **GrammKit** | Generates railroad diagrams while also exposing **references and dependencies between grammar rules**. | **Grammar visualization** · Railroad diagrams · Rule dependency/reference graph · Large-grammar analysis |

### How are the properties used by the plugins?

> 

## References

- [maven - What is the difference between artifactId and groupId in pom.xml? - Stack Overflow](https://stackoverflow.com/questions/39185798/what-is-the-difference-between-artifactid-and-groupid-in-pom-xml)
- [Maven – Glossary](https://maven.apache.org/glossary.html)
- [Maven – Guide to Working with Multiple Modules](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
- Maven – Maven Getting Started Guide
- [Maven – POM Reference](https://maven.apache.org/pom.html)
- [Maven pom.xml - javatpoint](https://www.javatpoint.com/maven-pom-xml)
- [Maven Tutorial](http://tutorials.jenkov.com/maven/maven-tutorial.html)
- [Maven Tutorial - Tutorialspoint](https://www.tutorialspoint.com/maven/index.htm)
- [Setting the Java Version in Maven | Baeldung](https://www.baeldung.com/maven-java-version)
- [Maven is broken by design](http://blog.ltgt.net/maven-is-broken-by-design/)
- - [Maven: [great idea, poor implementation (Part 1) - kief.com]](http://kief.com/maven-great-idea-poor-implementation-part-1.html)
- - [Maven: [great idea, poor implementation (Part 2) - kief.com]](http://kief.com/maven-great-idea-poor-implementation-part-2.html)
- - [Maven: [great idea, poor implementation (Part 3) - kief.com]](http://kief.com/maven-great-idea-poor-implementation-part-3.html)
- [We Switched from Maven to Bazel and Builds Got 10x Faster | by Jason Lunz | Code Red](https://redfin.engineering/we-switched-from-maven-to-bazel-and-builds-got-10x-faster-b265a7845854)
- [How to get started with Maven | Aditya’s Blog](https://adityasridhar.com/posts/how-to-get-started-with-maven)
- [Bazel - a fast, scalable, multi-language and extensible build system" - Bazel](https://bazel.build/)
- [java - Maven dependency graph](https://stackoverflow.com/questions/17413089/maven-dependency-graph/34066648)
- [Maven is broken by design](http://blog.ltgt.net/maven-is-broken-by-design/)
- [What is “pom” packaging in maven?](https://stackoverflow.com/questions/7692161/what-is-pom-packaging-in-maven)
- [Why Graddle is Better than Maven](https://assets.thoughtworks.com/assets/technology-radar-may-2013.pdf)
- [Maven: Non-resolvable parnter POM](https://stackoverflow.com/questions/7612309/maven-non-resolvable-parent-pom)
- [mvnd: Maven’s Speed Daemon, a Conversation with Peter Palaga and Guillaume Nodet](https://www.infoq.com/news/2020/12/mvnd-mavens-speed-daemon/)
- [POM Reference](https://maven.apache.org/pom.html)
- [Maven Tutorial](https://www.tutorialspoint.com/maven/index.htm)
- [Maven Tutorial](http://tutorials.jenkov.com/maven/maven-tutorial.html)
- [Why Everyone (Eventually) Hates (or Leaves) Maven](http://nealford.com/memeagora/2013/01/22/why_everyone_eventually_hates_maven.html)
- [InternalReprogrammability](https://martinfowler.com/bliki/InternalReprogrammability.html)
- [Workflow](note.html?n=technica/computation/language-system/conceptual-model-language-system/workflow.md)
- [Computation Description Artifact](note.html?n=technica/computation/language-system/conceptual-model-language-system/computation-description-artifact.md)
- [Java](note.html?n=technica/computation/language-system/conceptual-model-language-system/java.md)
- https://maven.apache.org/pom.html
- [Java](note.html?n=technica/computation/language-system/conceptual-model-language-system/java.md)
- [Jenkins](note.html?n=technica/computation/system/operation/operation-conceptual-model/jenkins.md)
- [Apache Maven](https://www.notion.so/Apache-Maven-d84ccddd5a5840a98866c124ef937703?source=copy_link)
