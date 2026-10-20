# Java: 🧩 Modularization

> This note explores modularization strategies, linking models, and the resulting artifacts, detailing how functions, modules, and concurrency mechanisms contribute to structured and efficient code organization.
> 

Guiding Questions:

- What fundamental principles of modularization (e.g., encapsulation, separation of concerns) does the language emphasize?
- How does the language define and structure modules at the syntactic and semantic levels?
- How does the language’s modularization compare to classical module systems like those in ML, Lisp, or Java?
- How does the language handle **module-wide type aliasing** and **type exports**?
- Scope, Name Resolution, and Visibility
    - How does the language handle name resolution within and across modules? (Lexical scoping, dynamic scoping, hierarchical resolution?)
    - How does the module system prevent or resolve naming conflicts? (Shadowing, aliasing, namespace imports?)
    - What mechanisms does the language provide for **controlling visibility** (public/private/protected/internal keywords, package-private scope, sealed modules)?
    - How does the module system handle **qualified imports** and **re-exporting** of module contents?
- Encapsulation and Dependency Management
    - How does the module system enforce **information hiding** and **encapsulation**?
    - What dependency resolution strategies does the language use? (Explicit dependency declarations, implicit resolution, package managers?)
    - How does the module system interact with **versioning and backward compatibility**?
    - How does it handle **cyclic dependencies** and **mutual recursion** across modules?
- Linking, Loading, and Compilation
    - How are modules compiled, linked, and loaded? (Static linking, dynamic linking, Just-in-Time (JIT) compilation?)
    - How does the module system influence **incremental compilation** and **build performance**?
    - How does the module system interact with **ahead-of-time (AOT) compilation** vs. **runtime loading**?
    - Does the language support **hot-reloading** or **dynamic module replacement**?
    - What mechanisms exist for **cross-module inlining and optimization** at compile time?

## Mechanisms

> &  Artifacts.
> 

| **Level** | **Mechanism** | **Introduced In** | **Description** |
| --- | --- | --- | --- |
| **Language** | **Package** | Java 1 | Groups related classes and interfaces; provides namespace management and access control (`public`, package-private). |
| **Language** | **Class** | Java 1 | Fundamental unit of code encapsulation; supports visibility modifiers and object-oriented design. |
| **Language** | **Interface** | Java 1 | Abstract contract; promotes decoupling and supports polymorphism and multiple inheritance (interface-only). |
| **Language** | **Inner/Nested Classes** | Java 1 | Supports encapsulation within a class; can access enclosing class members. Includes static and non-static nested types. |
| **Language** | **Enum** | Java 5 | Type-safe representation of fixed constants with behavior. Often used to encapsulate strategies or states. |
| **Language** | **Record** | Java 14 | Concise immutable data carriers with automatically generated boilerplate code. Promotes modular and declarative modeling. |
| **Language** | **Annotations** | Java 5 | Metadata mechanism used for modular design, dependency injection, and aspect-oriented features. |
| **Language** | **Generic Types** | Java 5 | Enable type-safe, reusable components (e.g., `List<T>`). Increase modularity through parameterized behavior. |
| **Compiler/Runtime** | **Jar (Java Archive)** | Java 1 | A bundling format for compiled `.class` files, resources, and metadata into a distributable unit. |
| **Platform** | **ServiceLoader (SPI)** | Java 6 | Supports decoupled modular design by enabling runtime discovery of service implementations. |
| **Platform** | **Java Module System (JPMS)** | Java 9 | Defines explicit module boundaries with `module-info.java`; enforces strong encapsulation and reliable configuration. |
| **Build Tool** | **Maven Modules** | External | Structure for multi-project builds; promotes code reuse, versioning, and separation of concerns. |
| **Build Tool** | **Gradle Modules (Projects/Subprojects)** | External | Supports modular builds, dependency isolation, and task orchestration. More flexible than Maven. |
| **Framework** | **OSGi Modules (Bundles)** | External | Dynamic module system for Java; supports runtime component loading/unloading and fine-grained lifecycle control. |
| **Framework** | **Spring Modules (Contexts/Beans)** | External | Logical and DI-based modularization; enables configuration and lifecycle management at a granular level. |

## Linking

> Linking + Loading.
> 

## Java  Package System

In Java, packages are a fundamental feature for organizing classes and interfaces into namespaces. They help manage and group related code, enhance modularity, and control access levels. Here’s a detailed overview:

### **Java Packages Overview**

| **Aspect** | **Description** | **Examples** |
| --- | --- | --- |
| **Definition** | A package is a namespace that organizes classes and interfaces into a hierarchical structure. Packages help avoid naming conflicts and manage access control. | `package com.example.myapp;` |
| **Declaration** | Packages are declared at the top of a Java source file using the `package` keyword. This must be the first statement in the file (excluding comments). | `package com.example.myapp;` |
| **Access Control** | Packages provide access control by defining access levels (public, protected, default, private) for classes, methods, and fields. Classes within the same package have package-private access to each other. | `public class MyClass { ... }` |
| **Importing Packages** | To use classes or interfaces from another package, you need to import them using the `import` statement. You can import single classes or entire packages. | `import java.util.ArrayList;`<br>`import java.util.*;` |
| **Package Hierarchy** | Packages can be organized hierarchically using dot notation. For example, `com.example.myapp` can contain sub-packages like `com.example.myapp.utils`. | `package com.example.myapp.utils;` |
| **Default Package** | If no package is specified, classes belong to the default (unnamed) package. This is not recommended for larger applications. | `// No package declaration` |
| **Package Naming Conventions** | Package names are typically written in all lowercase letters and follow a reverse domain name convention to ensure uniqueness. | `package com.example.myapp;` |
| **Access Modifiers** | Access to package members can be controlled using `public`, `protected`, and package-private (default) access modifiers. Package-private members are accessible only within the same package. | `protected void method();` |
| **Java Standard Packages** | Java provides a set of built-in packages that offer a wide range of functionality, including utilities, I/O operations, and networking. Examples include `java.lang`, `java.util`, `java.io`. | `import java.util.List;` |
| **Creating and Using Packages** | To create a package, declare it at the top of your Java source file. To use it, compile the source files and place them in the appropriate directory structure that matches the package name. | `javac -d bin src/com/example/myapp/MyClass.java` |
| **Package Documentation** | The `javadoc` tool can generate documentation for packages, classes, and methods, including descriptions, usage examples, and access levels. | `/** * Description of the package */` |

## Class Loader

> A **class loader** is a mechanism in the JVM that dynamically loads classes into memory at runtime, ensuring that classes are accessed and instantiated in the correct order and context, adhering to the JVM's structural principles (**techne**) and the expectations of application logic and security (**ethos**), while enabling flexibility in how and where classes are sourced from (**telos**).
> 

| **ClassLoader Type** | **Description** | **Classes Loaded** | **Parent ClassLoader** |
| --- | --- | --- | --- |
| **Bootstrap ClassLoader** | Loads core Java classes from the JDK (e.g., `java.lang.*`, `java.util.*`). This is part of the JVM. | Core Java classes, like `java.lang.Object` | None (it's the root ClassLoader) |
| **Extension ClassLoader** | Loads classes from the `jre/lib/ext` directory or any additional extensions. | Classes in the `jre/lib/ext` directory | Bootstrap ClassLoader |
| **System/Application ClassLoader** | Loads classes from the classpath (`-cp` or `CLASSPATH` environment variable). | User-defined application classes | Extension ClassLoader |
| **Custom ClassLoader** | User-defined class loader. Used to load classes from custom locations (e.g., file system, network). | Any class defined by the user | System/Application ClassLoader |

## **Class Loading Phases (JVM-Level)**

### **Loading**

- **Definition**: Locates the binary representation (`.class` file, network, generated bytecode) of a class/interface.
- **Mechanism**:
    - Triggered by `new`, `Class.forName()`, or JVM resolution.
    - Delegates to a **`ClassLoader`** (parent-first by default).
    - Output: A **`Class<?>`** object in the JVM’s method area.

### **Linking**

**Verification (JVM Security Gate)**

- Ensures bytecode adheres to **JVM spec** (e.g., no stack overflows, valid opcodes).
- Uses **`Xverify:none`** (HotSpot) to disable (risky).

**Preparation (Memory Allocation)**

- Allocates static memory for **class variables** (zeroed values).
- Sets **class metadata** (method tables, field offsets).

**Resolution (Symbolic → Direct References)**

- Resolves **symbolic references** (strings in constant pool) to **actual JVM structures**.
    - E.g., `java/lang/Object` → Direct pointer to `Object`’s method table.
- **Lazy resolution** (may defer until first use).

**Initialization (`<clinit>` Execution)**

- Runs **static initializers** (`static {}` blocks) in **thread-safe** manner.
- JVM ensures **sequential initialization** (per-class lock).

## **ClassLoader Hierarchy (Delegation Model)**

> The JVM uses a **parent-delegation** mechanism to avoid **duplicate loading and enforce security**:
> 

### **Bootstrap ClassLoader (Native, JVM Core)**

- Written in **C++**, loads `java.*`, `javax.*`, etc. (from `rt.jar`, `modules`).
- **No parent**, highest privilege.

### **Platform ClassLoader (Java 9+, replaces `ExtClassLoader`)**

- Loads **JDK extensions** (`jdk.*`, `sun.*`).
- Parent: **Bootstrap**.

### **Application (System) ClassLoader**

- Loads user classes (`classpath`).
- Parent: **Platform**.

### **Custom ClassLoaders**

- User-defined (e.g., OSGi, Tomcat’s `WebappClassLoader`).
- **Override `findClass()`** (not `loadClass()` to preserve delegation).

## **Visibility Rules**

> ..
> 
- A class loaded by **Child CL** can see classes from **Parent CL**, but not vice versa.
- Prevents **namespace clashes** (e.g., two versions of `org.example.Foo`).

## **Uniqueness Guarantee**

- A class is uniquely identified by:
    - **Fully Qualified Name (FQN)** + **Defining ClassLoader**.
- Prevents **type confusion attacks**.

## **Dynamic Class Loading**

- **`Class.forName()`**: Uses caller’s `ClassLoader`.
- **`Thread.contextClassLoader`**: Bypasses delegation (used in SPI, e.g., JDBC).

## **Memory & Leaks**

- **PermGen/Metaspace**: Loaded classes reside here (leak if `ClassLoader` isn’t GC’d).

## **Bytecode Manipulation & Agents**

- **`java.lang.instrument`**: Injects `ClassFileTransformer` into classloading pipeline.
- **Retransformation**: HotSwap classes at runtime (limited by JVM constraints).

## **Java Modules (JPMS, Java 9+)**

- **Replaces `rt.jar`** with **jimage** (module graph).
- **`ClassLoader` changes**:
    - **Bootstrap** → Loads **java.base**.
    - **Platform/App** → Map to **module layers**.
- **Stronger encapsulation**: Explicit `opens`/`exports` required.

## How to break Java Class Loading Visibility Rules?

> Violating Java’s class loading visibility rules requires bypassing the **parent-delegation model** or manipulating **protection domains**, which can break type safety and security. Here are **technical methods** to achieve this (with caveats):
> 

### **Directly Inject Classes into Bootstrap Loader**

> Use Unsafe API or JNI to manually define a class in the bootstrap classloader’s namespace.
> 

Implications:

- ✖ **SecurityException** (unless JVM flags like `--add-opens` are used).
- ✖ Breaks JVM assumptions (e.g., `java.*` classes must be loaded by bootstrap loader).

Example:

```java
sun.misc.Unsafe unsafe = sun.misc.Unsafe.getUnsafe();
Class<?> hackedClass = unsafe.defineClass(
    "com.example.Hack", 
    bytecode, 0, bytecode.length, 
    null,  // Use bootstrap loader
    null   // No ProtectionDomain
);
```

### **Custom ClassLoader with Reverse Delegation**

> Override **loadClass()** to skip parent delegation and load classes locally first.
> 

Implications:

- ✖ Risk of **LinkageError** (e.g., duplicate class definitions).
- ✖ May expose **confidential classes** (e.g., child loader sees parent’s restricted classes).

Example:

```java
class HijackingLoader extends ClassLoader {
    @Override
    protected Class<?> loadClass(String name, boolean resolve) {
        // STEP 1: Check locally FIRST (violates delegation)
        Class<?> c = findLoadedClass(name);
        if (c == null) {
            c = findClass(name);  // Force child-first loading
        }
        if (resolve) resolveClass(c);
        return c;
    }
}
```

### **Reflection + setAccessible(true)**

> Use reflection to access classes loaded by another `ClassLoader` and force visibility.
> 

Implications:

- ✖ Requires `ReflectionPermission("suppressAccessChecks")`.
- ✖ Fails under **SecurityManager**.

Example:

```java
Class<?> hiddenClass = otherClassLoader.loadClass("com.example.Secret");
Field f = hiddenClass.getDeclaredField("value");
f.setAccessible(true);  // Bypasses Java access controls
```

### Thread.contextClassLoader Hijacking

> Abuse the thread’s context classloader to load classes outside the normal hierarchy.\
> 

**Implications**:

- ✔ Used by **SPI** (e.g., JDBC, JNDI) for legitimate purposes.
- ✖ Can leak classes across **module boundaries** (Java 9+).

Example:

```java
Thread.currentThread().setContextClassLoader(hijackingLoader);
Class<?> stolenClass = Class.forName("com.example.Private", true, contextLoader);
```

### **JVM TI or Java Agents**

> Use `java.lang.instrument` or **JVMTI** to redefine classes in foreign classloaders.
> 

Implications:

- ✖ Requires `Can-Redefine-Classes` manifest attribute.
- ✖ May crash JVM if bytecode is invalid.

**Example**:

```java
instrumentation.redefineClasses(
    new ClassDefinition(
        foreignLoader.loadClass("com.example.Foo"),
        hackedBytecode
    )
);
```

### **Exploit Serialization Gadgets**

> Deserialize objects using a manipulated `ObjectInputStream` with a rogue `ClassLoader`.
> 

**Implications**:

- ✖ Classic vector for **RCE attacks** (e.g., Apache Commons Collections).

**Example**:

```java
ObjectInputStream ois = new ObjectInputStream(input) {
    @Override
    protected Class<?> resolveClass(ObjectStreamClass desc) 
        throws IOException, ClassNotFoundException {
        return hijackingLoader.loadClass(desc.getName());
    }
};
```

## **How can a class be dynamically loaded into the JVM’s Bootstrap  ClassLoader at runtime, making it visible to core JVM classes (e.g., `java.lang.*`) ?**

> This builds upon ([‣](https://app.notion.com/p/1c4c0f5171ec80e2a955c48490827eb3?pvs=21) ) …
> 

> Note: The Methods have change in Java Versions; so  need to work to
> 

If you need a class to be visible everywhere:

1. **Use the `Platform ClassLoader`** (Java 9+) for JDK-internal visibility.
2. **Leverage `Thread.contextClassLoader`** for cross-module access.
3. **Design with interfaces** (e.g., `ServiceLoader`).

### **Using `sun.misc.Unsafe` (Pre-Java 9)**

> The (now deprecated) `sun.misc.Unsafe` API allows defining classes directly in the Bootstrap ClassLoader’s namespace.
> 

```java
import sun.misc.Unsafe;

public class BootstrapLoaderHack {
    public static void main(String[] args) throws Exception {
        // 1. Get Unsafe instance (requires reflection)
        java.lang.reflect.Field f = Unsafe.class.getDeclaredField("theUnsafe");
        f.setAccessible(true);
        Unsafe unsafe = (Unsafe) f.get(null);

        // 2. Read class bytes (e.g., from a file)
        byte[] bytecode = Files.readAllBytes(Paths.get("EvilClass.class"));

        // 3. Define class in Bootstrap ClassLoader
        Class<?> hackedClass = unsafe.defineClass(
            "com.example.EvilClass",  // Class name
            bytecode,                  
            0,                        
            bytecode.length,          
            null,                     // Use Bootstrap ClassLoader
            null                      // No ProtectionDomain
        );

        // Now java.lang classes can see EvilClass!
    }
}
```

### **Using `-Xbootclasspath/a` (JVM Argument)**

> The `-Xbootclasspath/a` flag appends classes to the **Bootstrap Classpath**, making them loadable by the Bootstrap ClassLoader.
> 

```java
java -Xbootclasspath/a:/path/to/EvilClass.jar MyApp
```

### **JNI + JVMTI (Native Code)**

> Use **JVMTI** (JVM Tool Interface) to dynamically inject classes into the Bootstrap ClassLoader from native code (C/C++).
> 

## How can I make a class, such as `com.example.app.Logger`, available to the JVM in Java 11+ in a way that allows it to be used in instrumentation, even if it's not part of the Bootstrap ClassLoader?

In Java 11+, you can't directly modify the Bootstrap ClassLoader. However, you can:

1. **Add the Logger class to the classpath** using the `-add-exports` or `-add-modules` options when launching the JVM to make it globally accessible.
2. **Use a custom `URLClassLoader`** to load the `Logger` class from a JAR file, though it won’t be loaded by the Bootstrap ClassLoader, but rather by the system class loader.

## Java Code Artifacts

> 

| Artifact | Extension | Description |
| --- | --- | --- |
| **JAR** | `.jar` | **Java ARchive** - Used to package Java class files, libraries, and resources into a single archive. Typically used for libraries or standalone Java applications. |
| **WAR** | `.war` | **Web ARchive** - Used to package web applications. It contains Java servlets, JSP files, HTML, CSS, JavaScript, and other resources needed to run a web application. |
| **EAR** | `.ear` | **Enterprise ARchive** - Used for packaging enterprise-level applications, which can include multiple modules like JARs, WARs, and EJBs (Enterprise JavaBeans). |
| **RAR** | `.rar` | **Resource Adapter ARchive** - Used for packaging Java EE resource adapters that are used to integrate Java EE applications with external systems like databases or messaging services. |
| **TLF** | `.tlf` | **Technology Lifecycle Framework** - Generally used for packaging artifacts related to specific enterprise frameworks or configurations in larger enterprise Java systems. |
| **JSP** | `.jsp` | **JavaServer Pages** - Files that contain Java code embedded in HTML to create dynamic web pages. They are part of a WAR file but can be separately managed. |

## Java Archive (JAR)

> A **JAR (Java Archive)** file is a platform-independent, compressed file format used to package multiple Java class files, metadata, libraries, and resources such as images, configuration files, and text files into a single, cohesive archive. JAR files are essentially **ZIP** files with a specific structure that enables them to be used as components in the Java ecosystem. JAR files are recognized by their `.jar` extension, and they are a fundamental part of Java development, deployment, and distribution.
> 

> Java Archive (JAR):
> 

> FAT Jar:
> 

> Non Fat Jar: …
> 

> **Class Loading:** JAR files allow the Java Virtual Machine (JVM) to dynamically load classes during runtime. The JVM uses the classpath (specified by `Class-Path` in the `MANIFEST.MF` or by the runtime environment) to locate the classes and resources within the JAR file.
> 

> **Digital Signing**: JAR files can be digitally signed using public-key cryptography, which adds a layer of security. Signed JARs help ensure that the contents of the archive haven’t been tampered with and that the author of the archive can be verified.
> 

> **Execution**: Executable JAR files include a `Main-Class` entry in the `MANIFEST.MF` file, which points to the class that contains the `main()` method. These JARs can be executed directly using the `java -jar` command or by double-clicking (in supported environments).
> 

> **Dependencies (Class-Path)**: JARs can specify external dependencies via the `Class-Path` attribute in the `MANIFEST.MF` file. This allows an application packaged in a JAR to depend on other JARs, and the classpath for those dependencies is defined relative to the JAR's location.
> 

### **File Structure**

A JAR file follows the structure of a **ZIP archive,** with additional specific metadata for Java applications:

**META-INF Directory**:

- This directory contains important metadata about the JAR file and is required for certain JAR types like executable JARs.
- **MANIFEST.MF**: This is the manifest file inside the `META-INF` directory. The `MANIFEST.MF` file contains meta-information about the JAR file, such as:
    - `Manifest-Version`: The version of the manifest file format.
    - `Main-Class`: Specifies the entry point (class with the `main` method) for executable JARs.
    - `Class-Path`: Specifies the location of external libraries (JARs or directories) required by the application.
    - **Digital Signatures** (in signed JARs): Contains the digital signature of the JAR file to validate its authenticity and integrity.
1. **Bytecode (Class Files)**:
    - Java `.class` files are the compiled bytecode of Java source code. These files are packaged into the JAR file to create the application's functionality.
    - A JAR can contain any number of `.class` files, making it flexible for including entire libraries or individual applications.
2. **Resources**:
    - Non-class files like images, audio files, XML, and properties files can be included in a JAR. These files are typically accessed by Java classes via the `getResource()` or `getResourceAsStream()` methods.

### Types

> 

| Type of JAR | Description |
| --- | --- |
| **Library JAR** | A collection of Java class files and resources intended to be used as a dependency by other projects. It does not contain a `Main-Class` entry and is typically included as part of other applications. |
| **Executable JAR** | A self-contained JAR that includes the application code and resources needed to run the program. Contains a `Main-Class` attribute in its `MANIFEST.MF` file to specify the entry point. Can be launched directly from the command line using `java -jar myapp.jar`. |
| **Fat JAR (Uber JAR)** | A type of executable JAR that bundles all dependencies (other JAR files) into a single JAR file. Simplifies deployment and distribution by including everything needed in one archive. |
| **Source JAR** | Contains the original source code (i.e., `.java` files) for a library or application. Often provided alongside compiled JARs for debugging or inspection. |
| **Javadoc JAR** | A JAR that contains the Javadoc HTML documentation generated from the source code. It is packaged for easy distribution alongside the library. |
| **Signed JAR** | A JAR file that has been digitally signed with a private key to ensure it has not been modified and to establish the authenticity of its origin. |
| **Web JAR (WAR)** | While technically a `WAR` file, JARs are included to handle Java class files and libraries for web applications. WAR files aggregate JARs, HTML, JavaScript, and other web resources for deployment. |
| **EAR JAR** | In Enterprise Java (J2EE), an **EAR** file is a container for JAR files (and WAR files). These JARs may contain EJB (Enterprise JavaBeans) modules or other components of an enterprise-level Java application. |

## **Java 9+ (Modular System)**

> The **Java Platform Module System (JPMS)**, introduced in Java 9, fundamentally restructures the Java runtime and application development by enforcing strong encapsulation, explicit dependencies, and modular boundaries. Unlike the traditional JAR-based classpath system, where all public classes were accessible and dependency conflicts were common, JPMS introduces the `module-info.java` descriptor, which explicitly declares dependencies (`requires`), exposed packages (`exports`), and reflection permissions (`opens`). This modularization extends to the JDK itself, breaking it into distinct modules like `java.base` (which is always present) and optional ones such as `java.sql` and `java.desktop`. Consequently, modular Java applications can be structured with clear, compile-time-verified dependencies, reducing runtime errors and improving maintainability.
> 

> From a performance and distribution perspective, JPMS introduces the `jlink` tool, which allows developers to create **custom runtime images** that include only the necessary modules, significantly reducing application footprint and startup time. This is a key advancement for high-performance and embedded systems, as it eliminates the need to package an entire JDK. Additionally, module boundaries enforce stricter encapsulation, preventing deep reflection (a technique often used by frameworks like Spring) unless explicitly permitted via the `opens` directive. While this enhances security and maintainability, it has led to compatibility challenges with existing libraries that rely on unrestricted access to Java internals.
> 

> Despite these advancements, the adoption of JPMS in enterprise applications has been relatively slow due to its incompatibility with legacy code and dependency injection frameworks that rely on dynamic class loading. The transition from the classpath to a modular system requires significant refactoring, especially for large codebases with complex dependencies. However, for new Java applications and those seeking optimized runtime environments, JPMS provides a structured, scalable approach that enhances performance, security, and maintainability.
> 

## How does the Java Module System impact instrumentation, and what challenges does it introduce for tools that rely on reflection or bytecode manipulation?

> The **Java Module System (JPMS)**, introduced in Java 9, complicates instrumentation, particularly in areas like reflection, bytecode manipulation, and runtime class modification. JPMS enforces **strong encapsulation**, making it harder for external code to access non-exported classes unless explicitly permitted using `opens`. This is particularly problematic for reflection-based instrumentation, as deep reflection now requires additional configuration.
> 

> Access restrictions via the `java.lang.reflect` API are more stringent, often resulting in `IllegalAccessException` if non-exported classes are accessed. **Dynamic proxies** and **service loading** mechanisms are also impacted by module boundaries, limiting the ability to intercept or manipulate method calls unless the module exposes relevant classes. Bytecode manipulation tools face similar challenges, as they must navigate module boundaries to access internal classes, requiring tools to use reflective access or modify module descriptors.
> 

> Finally, **dynamic class loading** is hindered by modules controlling class visibility, necessitating special configurations to load classes across module boundaries. In summary, while JPMS enhances security and modularity, it introduces significant obstacles for traditional instrumentation, requiring adaptation through explicit module configuration or alternative approaches like bytecode manipulation.
> 

## Does the Java Platform Module System (JPMS) replace the ClassLoader system, and how do they interact with each other?

No, the **Java Platform Module System (JPMS)** does not replace the **ClassLoader** system, but rather **complements** it. The ClassLoader system still plays a crucial role in loading classes at runtime, while JPMS provides an additional layer of **modularity** and **encapsulation** for both the JDK and application code.

### Key Differences and Relationship:

1. **ClassLoader System**:
    - The ClassLoader is responsible for loading Java classes into memory at runtime. It loads classes from locations such as the file system, JAR files, or over the network.
    - ClassLoaders work on the classpath and are hierarchical in nature, meaning a class loader can delegate the responsibility of loading classes to its parent ClassLoader.
2. **Java Module System (JPMS)**:
    - JPMS introduces **modules**, which are collections of related packages with specific visibility rules and dependencies.
    - It organizes code into **modules** and provides mechanisms to define what classes and packages are **exported** or **opened** to other modules, while controlling the access to internal classes.

### How JPMS and ClassLoaders Interact:

- **Module System and ClassLoader**:
    - JPMS works **above** the ClassLoader system, and modules are loaded by ClassLoaders. Each module has its own **ModuleLayer**, which manages module loading, but ClassLoaders still perform the actual class loading within that layer.
    - The **module system** adds an extra layer of control to the ClassLoader's responsibility by specifying **module boundaries** and **access control** rules, but it does not replace how classes are physically loaded into memory.
- **Classpath vs Module Path**:
    - While the **classpath** used by the ClassLoader determines the locations of class files, the **module path** used by JPMS defines the locations of modules. The ClassLoader can be used to load classes from these modules, but JPMS determines the visibility and encapsulation of those classes based on module definitions.

### **Class Loading Mechanism**

| **Class Loader** | **Description** | **Responsibilities** |
| --- | --- | --- |
| **Bootstrap Class Loader** | Loads core Java libraries located in the JRE’s `rt.jar`. | Loads fundamental classes like `java.lang.Object`. |
| **Platform Class Loader** | Loads JDK internal classes and platform-specific libraries. | Typically loads Java SE platform classes. |
| **Application Class Loader** | Loads classes from the application’s classpath, including user-defined classes and libraries. | Loads application-specific classes. |
| **Custom Class Loaders** | Allows for creating custom class loaders to load classes from non-standard sources or perform special handling. | Extends `ClassLoader` to implement custom loading behavior. |

## References

- [Linker](note.html?n=technica/computation/language-system/conceptual-model-language-system/linker.md)
- [Loader](note.html?n=technica/computation/language-system/conceptual-model-language-system/loader.md)
- [Modularization](note.html?n=technica/computation/system/programming/conceptual-model-programming/modularization.md)
- [Java HotSpot Virtual Machine](note.html?n=technica/computation/language-system/conceptual-model-language-system/java-hotspot-virtual-machine.md)
- [https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-5.html](https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-5.html)
- [https://docs.oracle.com/javase/10/docs/api/java/lang/instrument/package-summary.html](https://docs.oracle.com/javase/10/docs/api/java/lang/instrument/package-summary.html)

Guiding Questions:

- What fundamental principles of modularization (e.g., encapsulation, separation of concerns) does the language emphasize?
- How does the language define and structure modules at the syntactic and semantic levels?
- How does the language’s modularization compare to classical module systems like those in ML, Lisp, or Java?
- How does the language handle **module-wide type aliasing** and **type exports**?
- Scope, Name Resolution, and Visibility
    - How does the language handle name resolution within and across modules? (Lexical scoping, dynamic scoping, hierarchical resolution?)
    - How does the module system prevent or resolve naming conflicts? (Shadowing, aliasing, namespace imports?)
    - What mechanisms does the language provide for **controlling visibility** (public/private/protected/internal keywords, package-private scope, sealed modules)?
    - How does the module system handle **qualified imports** and **re-exporting** of module contents?
- Encapsulation and Dependency Management
    - How does the module system enforce **information hiding** and **encapsulation**?
    - What dependency resolution strategies does the language use? (Explicit dependency declarations, implicit resolution, package managers?)
    - How does the module system interact with **versioning and backward compatibility**?
    - How does it handle **cyclic dependencies** and **mutual recursion** across modules?
- Linking, Loading, and Compilation
    - How are modules compiled, linked, and loaded? (Static linking, dynamic linking, Just-in-Time (JIT) compilation?)
    - How does the module system influence **incremental compilation** and **build performance**?
    - How does the module system interact with **ahead-of-time (AOT) compilation** vs. **runtime loading**?
    - Does the language support **hot-reloading** or **dynamic module replacement**?
    - What mechanisms exist for **cross-module inlining and optimization** at compile time?