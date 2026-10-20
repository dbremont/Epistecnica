# Java: ✨ Metaprogramming

> The **Java Metaprogramming Model** encompasses techniques and mechanisms, such as reflection, annotations, dynamic proxies, bytecode manipulation, and code generation, that enable programs to inspect, modify, and generate code and behavior dynamically at runtime or compile-time.
> 

Questions:

- What is the language’s metaprogramming paradigm?
- What constructs are available at compile-time?
- What runtime reflection capabilities exist?
- How is reflection implemented?
- How are type errors reported in metaprograms?
- What are the costs of metaprogramming?
- How does the language prevent abusive metaprogramming?
- How are metaprograms debugged?

## Mechanism

| **Mechanism** | **Description** |
| --- | --- |
| **Reflection** | Allows inspection and modification of the Java language's classes, methods, fields, and other elements at runtime. |
| **Annotations** | Provide a way to add metadata to code elements such as classes, methods, and fields, which can be processed at runtime or compile-time. |
| **Dynamic Proxies** | Allows the creation of proxy instances that implement one or more interfaces at runtime, enabling dynamic method dispatch. |
| **Bytecode Manipulation** | Involves modifying Java bytecode at runtime or compile-time to alter or extend the behavior of classes and methods. |
| **Code Generation** | The process of generating Java source code or bytecode dynamically, typically using libraries or tools to create code at runtime. |
| **Class Loaders** | Allow custom loading and definition of classes at runtime, providing a mechanism for loading classes from different sources or with modified behavior. |
| **Metaobject Protocol** | A framework that allows custom manipulation and control of object behavior and structure through the definition of metaobjects. |
| **Aspect-Oriented Programming (AOP)** | A programming paradigm that provides a way to separate cross-cutting concerns, such as logging or security, from the core business logic. |

## Instrumentation Subsystem

> The **Instrumentation Subsystem** in Java provides a way to modify and monitor applications **at runtime**. It is part of the **Java Platform Debugger Architecture (JPDA)** and is mainly exposed through the **`java.lang.instrument` package**.
> 

It allows:

- **Bytecode transformation** before a class is loaded into the JVM.
- **Runtime modification of already loaded classes**.
- **Profiling and monitoring** without modifying source code.
- **Extending the JVM’s class loading mechanism** (e.g., injecting agents for debugging).

### Uses

✅ **Profiling & Monitoring** → Injects logging/profiling code dynamically.

✅ **Code Coverage Tools** → E.g., JaCoCo modifies bytecode at runtime.

✅ **Performance Analysis**→ JVM profilers like JFR use agents.

✅ **Security & Access Control** → Enforces security policies at runtime.

✅ **Hot Patching** → Modifies classes without restarting the JVM.

### **Java Agent**

A Java Agent is a JAR file that contains a special **agent class** with one or both of these methods:

- **`premain(String agentArgs, Instrumentation inst)`** → Runs **before** `main()` (startup instrumentation).
- **`agentmain(String agentArgs, Instrumentation inst)`** → Runs **when attached to a running JVM** (dynamic instrumentation).

### Instrumentation API

> 

The **`java.lang.instrument.Instrumentation`** interface provides methods for:

- **Class transformation**: `addTransformer(ClassFileTransformer transformer, boolean canRetransform)`
- **Redefining loaded classes:** `redefineClasses(ClassDefinition... definitions)`; look this can not change the signature; or add new fields.
- **Extending class loader visibility**: `appendToBootstrapClassLoaderSearch(JarFile jar)`

```java
inst.addTransformer((loader, className, classBeingRedefined, protectionDomain, classfileBuffer) -> {
    byte[] modifiedBytecode = modifyClass(classfileBuffer); // Custom bytecode modification
    return modifiedBytecode;
});
```

### Attaching to a Running JVM (`VirtualMachine` API)

> Java agents can be attached to a running JVM **using the Attach API** (`com.sun.tools.attach.VirtualMachine`).
> 

> Requires `tools.jar` (JDK only, not JRE).
> 

```java
import com.sun.tools.attach.*;

public class AgentAttacher {
    public static void main(String[] args) throws Exception {
        VirtualMachine vm = VirtualMachine.attach("12345"); // Attach to JVM PID
        vm.loadAgent("/path/to/agent.jar"); // Load agent dynamically
        vm.detach();
    }
}
```

### **Interaction with JVM Classloading Mechanism**

- Java **agents hook into the classloading process** using `ClassFileTransformer`.
- Agents **modify class bytecode before loading** to memory.
- Using **`appendToBootstrapClassLoaderSearch()`**, agents can **inject new classes into the Bootstrap ClassLoader**.

## References

- [Metaprogramming](note.html?n=technica/computation/language-system/conceptual-model-language-system/metaprogramming.md)
- https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/

Guiding Questions:

- What is the language’s metaprogramming paradigm?
- What constructs are available at compile-time?
- What runtime reflection capabilities exist?
- How is reflection implemented?
- How are type errors reported in metaprograms?
- What are the costs of metaprogramming?
- How does the language prevent abusive metaprogramming?
- How are metaprograms debugged?