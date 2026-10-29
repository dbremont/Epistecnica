---
tags: [java, ide, debugging, osgi, maven]
---

# Eclipse

> Eclipse is a versioned desktop IDE product instance — a Java-based, OSGi-composed workbench for editing, building, debugging, and extending software, above all Java.
>
> It is the complement of the command line and the bare build: the workspace returns fast, managed feedback (problems view, incremental build, debugger with source lookup) while the `Bundle` persists as the unit of functionality, claimed and wired by the Equinox runtime through the extension registry.
>
> This note characterizes Eclipse as a full ensemble — distribution, OSGi runtime, workbench, JDT, PDE, help, Maven bridge, configuration, practices, and evolution — following the schema in [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md).

## Formulation

### What technical element type does this technical instance belong to?

**Eclipse belongs to the `Production Technical System` technical element type, readable as a `Technical Element Set`.**

More specifically:

```text
Production Technical System
└── Eclipse (IDE distribution + OSGi runtime + workbench + JDT/PDE + RCP host)
    readable as Technical Element Set (distribution + bundles + workbench + tooling + practices)
```

Eclipse is a technical system because it is an organized composition of a provisioned distribution, an OSGi runtime with a bundle dependency graph and extension registry, a workbench of perspectives/views/editors, language tooling (JDT), plugin tooling (PDE), help and build bridges, configuration, management mechanisms, and update practices that collectively provide a development environment. A team *provisions* a distribution; the runtime *claims* and wires bundles; the workbench *realizes* perspectives. As a coherent body of objects + techniques + knowledge + institutions organized around one capability — develop, build, debug, and extend software from one workbench — it is also a `Technical Element Set`.

### What is this technical instance?

> Eclipse is a concrete, versioned desktop IDE technical system instance: a Java-VM-hosted, Equinox-OSGi-composed workbench of perspectives, views, and file-type-bound editors, with JDT (own compiler, incremental builder, refactoring, debugger), PDE (plugin develop/build/test tooling, PDE Build), Lucene-indexed help, and a Maven bridge — extensible through installable plugins and reusable as a Rich Client Platform for standalone applications.

Lineage: IBM VisualAge Micro Edition compiler contribution → Eclipse platform in Java, Eclipse Foundation stewardship → plugins described by `plugin.xml` become OSGi bundles with manifest metadata (Equinox) → 3.x stream → 4.x (e4) workbench.

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one Eclipse IDE installation instance (distribution, runtime structure, workbench, tooling, configuration surface, practices); deployment-specific values appear only in rows marked exemplar.
>
> Stopping rule: a row is terminal when it names a concrete file, directory, command, configuration attribute, measured value, URL, stack frame, or named actor; attribute slots (Profile, Version, Path) are terminal by rule.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a team *provisions* a distribution; the runtime *claims* and wires bundles; a plugin *extends* an extension point; the workbench *realizes* perspectives; JDT *embodies* the incremental-build technique.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → Eclipse | Running Eclipse IDE product instance: distribution plus OSGi runtime, workbench, JDT, PDE, and RCP hosting. |
| `Production Technical System` → Eclipse → `Technical Architecture` | Grouping: Technical Architecture elements. |
| `Production Technical System` → Eclipse → `Technical Architecture` → Coherence (everything is a plugin) | Organizing structure: platform, IDE tooling, and user-built apps are all plugins/bundles composed through the extension registry. |
| `Production Technical System` → Eclipse → `Technical Architecture` → Workbench | Familiar desktop UI shell organizing perspectives, views, and editors. |
| `Production Technical System` → Eclipse → `Technical Architecture` → Workbench → `Technical Interface` | Grouping: Technical Interface elements. |
| `Production Technical System` → Eclipse → `Technical Architecture` → Workbench → `Technical Interface` → Perspective | Organized arrangement of editors and views presenting tooling for a task. |
| `Production Technical System` → Eclipse → `Technical Architecture` → Workbench → `Technical Interface` → Editor | File-type-bound editing surface; the correct editor launches when a file opens. |
| `Production Technical System` → Eclipse → `Technical Architecture` → Workbench → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Production Technical System` → Eclipse → `Technical Architecture` → Workbench → `Constitutive Technical Object` → View | Auxiliary pane; exemplar: the Problems view listing errors and warnings in Java code. |
| `Production Technical System` → Eclipse → `Technical Architecture` → Workbench → `Technical Feedback` | Grouping: Technical Feedback elements. |
| `Production Technical System` → Eclipse → `Technical Architecture` → Workbench → `Technical Feedback` → Problems view | Feedback surface listing compilation errors and warnings. |
| `Production Technical System` → Eclipse → `Technical Capability` | Grouping: Technical Capability elements. |
| `Production Technical System` → Eclipse → `Technical Capability` → Realized capability | Capability realized: edit, build, debug, and extend Java (and other-language) software from one workbench; host standalone RCP applications. |
| `Production Technical System` → Eclipse → `Technical Institution` | Grouping: Technical Institution elements. |
| `Production Technical System` → Eclipse → `Technical Institution` → Governance (Eclipse Foundation) | Eclipse Foundation stewardship; Eclipse Public License; plugin contribution process. |
| `Production Technical System` → Eclipse → `Production Technical Object` | Grouping: Production Technical Object elements. |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution | Installed IDE distribution from which the runtime is provisioned (exemplar: a 4.x release stream). |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Technical Configuration` | Grouping: Technical Configuration elements. |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Technical Configuration` → eclipse.ini | JVM selection, heap, and system-property launch configuration (exemplar values per install). |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Constitutive Technical Object` → plugins/ | Installed bundle artifact pool. |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Constitutive Technical Object` → features/ | Grouped installable feature definitions (p2 provisioning). |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Constitutive Technical Object` → configuration/ | Install configuration state and profile data. |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Constitutive Technical Object` → Workspace | User working area holding projects, settings, and history (exemplar path per user). |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Constitutive Technical Object` → Workspace → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Constitutive Technical Object` → Workspace → `Constitutive Technical Object` → .metadata/ | Workbench state, preferences, and plugin runtime data. |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Technical Dependency` | Grouping: Technical Dependency elements. |
| `Production Technical System` → Eclipse → `Production Technical Object` → Distribution → `Technical Dependency` → JVM requirement | A Java VM is required to run the platform (exemplar: a Java 17/21 runtime). |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime | Executing Eclipse runtime: JVM process hosting the OSGi framework and the workbench. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Constitutive Technical Object` → JVM process | Operating-system process containing the runtime. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Constitutive Technical Object` → Bundle (plugin) | Modular unit of functionality: JAR plus manifest describing itself, its dependencies, and how it can be utilized or extended (manifest data formerly stored in `(root) > Technical Element Set > Production Technical System > Production Technical Object > Constitutive Technical Object` at the plugin root). |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Constitutive Technical Object` → Bundle |  |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Constitutive Technical Object` → Bundle → `Technical Specification` | Grouping: Technical Specification elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Constitutive Technical Object` → Bundle → `Technical Specification` → Manifest plus plugin.xml | Self-description: identity, `require`d dependencies, utilizable and extensible contributions. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Constitutive Technical Object` → Bundle → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Constitutive Technical Object` → Bundle → `Technical Mechanism` → Per-bundle classloader | Each plugin loads through its own classloader. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Constitutive Technical Object` → Extension | Contribution plugged into an extension point by some plugin. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Constitutive Technical Object` → JFace | UI layer above SWT: viewers, actions, and dialogs. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Mechanism` → Equinox OSGi | OSGi framework implementation hosting bundles and services. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Mechanism` → Extension registry | Runtime mechanism matching extensions to extension points. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Mechanism` → SWT | Standard Widget Toolkit: native-widget UI toolkit using operating-system calls for lists, buttons, and events. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Mechanism` → SWT → `Technical Dependency` | Grouping: Technical Dependency elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Mechanism` → SWT → `Technical Dependency` → Native binding (GTK and WebKit) | Operating-system widget calls underneath SWT; source of platform quirks (exemplar workaround: `(root) > Technical Element Set > Technical Dependency`, see SWT issue 1108). |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Dependency` | Grouping: Technical Dependency elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Dependency` → Bundle dependency | `(root) > Technical Element Set > Technical Dependency` statements expressing plugin-to-plugin dependencies. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Interface` | Grouping: Technical Interface elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Interface` → Extension point | Declared point at which a plugin can be extended (editors, views, builders). |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Specification` | Grouping: Technical Specification elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Runtime → `Technical Specification` → Non-code contributions | HTML help and documentation resources shipped inside plugins. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → JDT | Java Development Tools subsystem: editors, wizards, refactoring support, debugger, compiler, and incremental builder. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → JDT → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → JDT → `Technical Mechanism` → ECJ compiler | Own Java compiler from the VisualAge Micro Edition contribution, enabling tooling and compiler extension points a third-party command-line compiler could not offer. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → JDT → `Technical Mechanism` → Refactoring support | Automated code-restructuring tooling over the compiler model. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → JDT → `Constitutive Technique` | Grouping: Constitutive Technique elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → JDT → `Constitutive Technique` → Incremental builder | Rebuilds only changed code on save; separable as its own technique (take the Java Incremental Builder out of Eclipse). |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → JDT → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → JDT → `Constitutive Technical Object` → Java debugger | Debug engine plus source lookup for stepping through project and dependency code. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → PDE | Plug-in Development Environment: tooling to develop, build, deploy, and test plugins and other artifacts extending Eclipse. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → PDE → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → PDE → `Technical Mechanism` → PDE Build | Dependency-driven generation of Ant scripts constructing the build artifacts. |
| `Production Technical System` → Eclipse → `Constitutive Technical Object` → Help subsystem | Online help content, indexed and searched with Apache Lucene. |
| `Production Technical System` → Eclipse → `Technical Interaction` | Grouping: Technical Interaction elements. |
| `Production Technical System` → Eclipse → `Technical Interaction` → Maven integration (m2e) | Bridge resolving Maven dependencies into the workspace build path. |
| `Production Technical System` → Eclipse → `Production Technical System` | Grouping: Production Technical System elements. |
| `Production Technical System` → Eclipse → `Production Technical System` → Maven integration |  |
| `Production Technical System` → Eclipse → `Production Technical System` → Maven integration → `General Technique` | Grouping: General Technique elements. |
| `Production Technical System` → Eclipse → `Production Technical System` → Maven integration → `General Technique` → mvn eclipse:eclipse | Generates Eclipse project metadata from a Maven project (exemplar command; `mvn eclipse:clean` reverts it). |
| `Production Technical System` → Eclipse → `Production Technical System` → Maven integration → `General Technique` → mvn dependency:sources | Fetches dependency sources for debugger attachment (exemplar command). |
| `Production Technical System` → Eclipse → `Production Technical System` → Configuration |  |
| `Production Technical System` → Eclipse → `Production Technical System` → Configuration → `Technical Configuration` | Grouping: Technical Configuration elements. |
| `Production Technical System` → Eclipse → `Production Technical System` → Configuration → `Technical Configuration` → Runtime CLI options | Documented runtime command-line arguments (see Eclipse help runtime-options reference). |
| `Production Technical System` → Eclipse → `Production Technical System` → Configuration → `Technical Configuration` → Run and Debug configuration | Named launch definition: main type, classpath, arguments, JRE (exemplar per project). |
| `Production Technical System` → Eclipse → `Production Technical System` → Configuration → `Technical Configuration` → Source attachment | Project-source versus debugging-source settings; manual attachment when automatic resolution fails. |
| `Production Technical System` → Eclipse → `Production Technical System` → Configuration → `Technical Security` | Grouping: Technical Security elements. |
| `Production Technical System` → Eclipse → `Production Technical System` → Configuration → `Technical Security` → Certificates | JVM trust-store setup for Eclipse and Maven HTTPS access (exemplar per install). |
| `Production Technical System` → Eclipse → `Production Technical System` → Configuration → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Production Technical System` → Eclipse → `Production Technical System` → Configuration → `Technical Parameter` → Profile | Named list of UIs in an installation. |
| `Production Technical System` → Eclipse → `Production Technical System` → Failure |  |
| `Production Technical System` → Eclipse → `Production Technical System` → Failure → `Technical Failure` | Grouping: Technical Failure elements. |
| `Production Technical System` → Eclipse → `Production Technical System` → Failure → `Technical Failure` → Source-not-found | Debugger reaching bytecode without attached sources. |
| `Production Technical System` → Eclipse → `Technical Practice` | Grouping: Technical Practice elements. |
| `Production Technical System` → Eclipse → `Technical Practice` → Debug-source practice | Repeatable pattern: take the root Maven project, run `(root) > Technical Element Set > Technical Practice` plus `mvn dependency:sources`, else attach sources manually (exemplar frame: `AbstractSharedSessionContract.checkOpenOrWaitingForAutoClose`). |
| `Production Technical System` → Eclipse → `Technical Practice` → Plugin-install practice | Repeatable pattern: install plugins into the distribution through provisioning. |
| `Production Technical System` → Eclipse → `Technical Practice` → RCP practice | Repeatable pattern: build standalone applications on the Eclipse platform. |
| `Production Technical System` → Eclipse → `Technical Practice` → RCP practice → `Production Technical System` | Grouping: Production Technical System elements. |
| `Production Technical System` → Eclipse → `Technical Practice` → RCP practice → `Production Technical System` → Mars Rover monitoring (NASA and JPL) | Exemplar RCP application monitoring rover robots. |
| `Production Technical System` → Eclipse → `Technical Practice` → RCP practice → `Production Technical System` → Bioclipse | Exemplar RCP application for bioinformatics data visualization. |
| `Production Technical System` → Eclipse → `Technical Practice` → RCP practice → `Production Technical System` → Dutch Railway monitoring | Exemplar RCP application monitoring train performance. |
| `Production Technical System` → Eclipse → `Technical Evaluation` | Grouping: Technical Evaluation elements. |
| `Production Technical System` → Eclipse → `Technical Evaluation` → Evaluation | Grouping: evaluation surface of the installation. |
| `Production Technical System` → Eclipse → `Technical Evaluation` → Evaluation → `Verification` | Grouping: Verification elements. |
| `Production Technical System` → Eclipse → `Technical Evaluation` → Evaluation → `Verification` → Compiler verification | Compiler and problem markers verifying code against the language specification. |
| `Production Technical System` → Eclipse → `Technical Evaluation` → Evaluation → `Validation` | Grouping: Validation elements. |
| `Production Technical System` → Eclipse → `Technical Evaluation` → Evaluation → `Validation` → Launch validation | Running and debugging validating the artifact against its intended purpose. |
| `Production Technical System` → Eclipse → `Technical Evolution` | Grouping: Technical Evolution elements. |
| `Production Technical System` → Eclipse → `Technical Evolution` → Evolution plugins-to-bundles | Historical line: `(root) > Technical Element Set > Technical Evolution` plugins become OSGi bundles with manifest metadata under Equinox. |
| `Production Technical System` → Eclipse → `Technical Maintenance` | Grouping: Technical Maintenance elements. |
| `Production Technical System` → Eclipse → `Technical Maintenance` → Maintenance (p2 updates) | Patching and upgrading the installation while preserving workspace state. |

## QA

### What is the difference between native and emulated widget toolkits, and why is SWT native?

> A native widget toolkit uses operating-system calls to build interface components such as lists and push buttons, leaving interaction handling to the operating system. Its widgets are "pixel perfect": they look and feel like their counterparts in other desktop applications, and OS vendors' look-and-feel updates arrive for free. The cost is portability — underlying OS widget implementations differ vastly, producing inconsistencies. An emulated toolkit implements components outside the OS (drawing, focus, mouse and keyboard itself): highly portable and flexible — modern native toolkits such as Windows Presentation Framework are equally flexible — but early emulated toolkits were slow and looked out of place; Smalltalk-80 programs were recognizable at a glance, which hurt acceptance. SWT is native: Eclipse defers to the OS, which is why platform quirks (such as the WebKit/GTK DMABUF renderer issue) surface in Eclipse directly.
>

### Why did the JDT team write its own compiler instead of using `javac`?

> The team started from a compiler code contribution from VisualAge Micro Edition and planned to build tooling on top of the compiler, so owning the compiler was the logical decision. It also let JDT committers provide extension points for extending the compiler — impossible if the compiler were a third-party command-line application.
>

### Is a plugin the same as a bundle?

> Yes. With the switch to OSGi, Eclipse plugins became known as bundles: a plugin and a bundle are the same thing — a modular subset of functionality describing itself with metadata in a manifest. A plugin is a JAR with a manifest stating its identity, its dependencies, and how it can be utilized or extended.
>

### What are extensions and extension points?

> They are the other element of the Eclipse component model besides plugins. An extension point is a declared point at which a plugin can be extended (editors, views, builders); an extension is a contribution plugged into such a point by some plugin. The extension registry matches the two at runtime.
>

### How does Eclipse resolve Maven dependencies?

> Through the Maven bridge (m2e): `mvn eclipse:eclipse` generates Eclipse project metadata from a Maven project (`mvn eclipse:clean` reverts it), and `mvn dependency:sources` fetches dependency sources for debugger attachment. Dependency lookup therefore starts from the root Maven project and follows its declared dependencies.
>

### Why does adding `~/.m2/repository` as a source folder fail?

> Eclipse Debug Source Lookup does not recursively scan `~/.m2/repository` for matching `*-sources.jar` files. Source resolution follows the launch's source lookup path — project sources, classpath entries, and explicitly attached external archives — so adding the whole repository as a source folder changes nothing at suspend time: the debugger still reports "source not found". `mvn dependency:sources` only fetches the `*-sources.jar` files into the repository; they take effect when attached per artifact — through the Maven Dependencies container (m2e source attachment) or manual attachment of the specific sources jar — not through the repository directory itself. That is also why project sources and debugging sources are treated differently: the former feed the incremental builder, the latter feed the lookup path at the suspended frame.
>

### Why does the debugger show "source not found", and how is it fixed?

> The debugger suspends on bytecode with no attached source. Fix order: work from the root Maven project, regenerate metadata with `mvn clean eclipse:eclipse`, fetch sources with `mvn dependency:sources`, and if resolution still fails, attach the sources manually.
>

### How does debug source resolution work?

> Debugging needs a bytecode-to-source mapping per launch. Resolution order: project sources first — the root Maven project and its modules, since sources and dependencies follow the project and its dependencies — then dependency sources fetched via `mvn dependency:sources`, else manually attached sources. Project sources and debugging sources are treated differently in Eclipse: the former drive the incremental build and problem markers, the latter drive the debugger's source lookup at a suspended frame (exemplar: `AbstractSharedSessionContract.checkOpenOrWaitingForAutoClose()`). When lookup fails, the debugger reports "source not found".
>

### Why do attached sources sometimes fail to link in the Debug view?

> Because Eclipse links debug classes to sources by the **exact runtime class container and class identity**, not merely by Maven `groupId:artifactId:version`. Attaching the `*-sources.jar` of the Maven artifact is not enough when the class at the suspended frame came from somewhere else: with WildFly/JBoss Modules, the class may be loaded from a different JAR or module classloader — or a different build — than the Maven artifact whose sources you attached, so the lookup finds no match and the Debug view still shows no source. The fix is to attach the sources to the container that actually provided the runtime class (the module or JAR on the server's classpath), not just to the Maven-coordinate artifact.
>

### How do Run/Debug configurations work?

> A Run/Debug configuration is a named launch definition holding the main type, classpath, arguments, and JRE for one launchable unit; the debugger then steps through project and dependency code using the source resolution above.
>

### What are perspectives, views, editors, workspaces, and profiles?

> The workbench is the familiar UI shell organizing how Eclipse appears on the desktop. Editors are associated with file types, so the correct editor launches when a file opens; a view (such as the Problems view) shows errors or warnings; editors and views together form a perspective presenting tooling in an organized fashion. The workspace is the user's working area of projects and settings; a profile is the list of UIs in an installation.
>

### What is `WEBKIT_DISABLE_DMABUF_RENDERER=1` and when is it needed?

> A workaround for a WebKit/GTK renderer fault under SWT's native bindings: setting the variable disables the DMABUF renderer path that breaks Eclipse rendering on affected Linux desktops. Upstream tracker: eclipse.platform.swt issue 1108.
>

## References

- [The Architecture of Open Source Applications: Eclipse](https://www.aosabook.org/en/eclipse.html)
- [Eclipse Platform Technical Overview](https://www.eclipse.org/articles/Whitepaper-Platform-3.1/eclipse-platform-whitepaper.html)
- [Eclipse: A platform for integrating development tools](https://www.ics.uci.edu/~andre/ics228s2006/desriviereswiegand.pdf)
- [Eclipse runtime command-line arguments](https://help.eclipse.org/latest/index.jsp?topic=/org.eclipse.platform.doc.isv/reference/misc/runtime-options.html)
- [Eclipse SWT issue 1108 (DMABUF renderer)](https://github.com/eclipse-platform/eclipse.platform.swt/issues/1108)
- [Eclipse (software)](https://en.wikipedia.org/wiki/Eclipse_(software))
- [List of Eclipse-based software](https://en.wikipedia.org/wiki/List_of_Eclipse-based_software)
- [Standard Widget Toolkit](https://en.wikipedia.org/wiki/Standard_Widget_Toolkit)
- [JFace](https://en.wikipedia.org/wiki/JFace)
- [Eclipse Equinox](https://en.wikipedia.org/wiki/Equinox_(OSGi))
- [Open Services Gateway initiative (OSGi)](https://www.osgi.org/)
- [Introduction to OSGi](https://www.baeldung.com/osgi)
- [Using the Eclipse IDE for Java programming - Tutorial](https://www.vogella.com/tutorials/Eclipse/article.html)
- [Eclipse java debugging: source not found - Stack Overflow](https://stackoverflow.com/questions/6174550/eclipse-java-debugging-source-not-found)
- [Maven](note.html?n=technica/general/pto/maven.md)
- [VS Code](note.html?n=technica/pto/vscode.md)
- [Java EE / Jakarta EE](note.html?n=technica/cto/es/multinode/java-ee-jakarta-ee.md)
- [WildFly](note.html?n=technica/cto/es/multinode/wildfly.md)
- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md)
