---
tags: [intermediate-representation]
---

# Java Bytecode

- [ASM](note.html?n=technica/computation/language-system/conceptual-model-language-system/asm.md), [Java HotSpot Virtual Machine](note.html?n=technica/computation/language-system/conceptual-model-language-system/java-hotspot-virtual-machine.md), [Byte Buddy](note.html?n=technica/computation/language-system/conceptual-model-language-system/byte-buddy.md)

> Java bytecode is a platform-independent, low-level instruction  set encoded in binary format (consisting of one-byte opcodes and  optional operands) that is executed by the Java Virtual Machine (JVM)  using a stack-based architecture, supporting features such as dynamic  class loading, verification, and just-in-time (JIT) compilation for 
optimized execution.
> 

QA:

- How are lambda expressions represented in bytecode? https://stackoverflow.com/questions/23133243/how-are-lambda-expressions-translated-into-java-byte-code
- How are classes represented in bytecode?
- 

## Structure

Java bytecode consists of the following key components:

1. **Magic Number**: The first 4 bytes (`0xCAFEBABE`) to identify the file as a valid Java bytecode file.
2. **Minor and Major Version**: 2 bytes each that indicate the version of the Java class file format.
3. **Constant Pool**: A table containing constants used in the bytecode, such as string literals, class names, method names, and field references. It is indexed by other parts of the bytecode.
4. **Access Flags**: 2 bytes that specify access modifiers and class attributes (e.g., `public`, `abstract`, `final`).
5. **This Class and Superclass**: 2-byte indices referring to the class and its superclass in the constant pool.
6. **Interfaces**: A table of indices pointing to the interfaces implemented by the class.
7. **Fields**: A table of field descriptors, each describing a class field with its access modifiers, name, and type.
8. **Methods**: A table of method descriptors, each containing method access modifiers, name, return type, and argument types, along with the bytecode instructions for the method.
9. **Attributes**: Optional data associated with the class, methods, or fields, including source file name, line numbers, or runtime annotations.

## Opcodes

> See more in https://javaalmanac.io/bytecode/
> 

## Method Calling Mechanisms

> 

| **Bytecode** | **Type of Method** | **Method Resolution** | **Key Use Cases** |
| --- | --- | --- | --- |
| `invokestatic` | Static Method | Resolved at compile-time | Calling class-level methods (e.g., utility methods, constants) |
| `invokevirtual` | Instance Method | Resolved at runtime (dynamic dispatch) | Calling overridden methods (supports polymorphism) |
| `invokedynamic` | Dynamic Method | Resolved at runtime by bootstrap method | Calling lambda expressions, method references, and other dynamic dispatch scenarios |

## Tools

> 

| **Tool/Library** | **Description** | **Primary Features** | **Use Cases** |
| --- | --- | --- | --- |
| **ASM** | A widely used library for reading, writing, and transforming Java bytecode. | Bytecode parsing and generation, class instrumentation, in-memory transformation. | Dynamic code generation, instrumentation, class modification at runtime. |
| **BCEL (Apache)** | Byte Code Engineering Library; allows analysis and modification of bytecode. | High-level bytecode manipulation, advanced control-flow analysis. | Static analysis, bytecode optimization, instrumentation. |
| **Javassist** | Simplifies bytecode manipulation with a high-level API. | Runtime code generation, dynamic proxies, and easy method injection. | Runtime bytecode transformation, proxies, instrumentation. |
| **Soot** | A framework for analyzing and transforming Java and Android bytecode. | Static analysis, control-flow graphs, bytecode optimization, and instrumentation. | Program analysis, performance optimization, security analysis. |
| **ProGuardCORE** | A library for parsing and manipulating Java class files. | Simplifies bytecode reading, writing, and optimization. | Obfuscation, shrinking, static code analysis. |
| **JByteMod** | A graphical tool for decompiling, editing, and recompiling Java bytecode. | GUI-based bytecode editor, decompiler, and recompiler. | Bytecode exploration and modification. |
| **Recaf** | An all-in-one tool for editing and exploring Java bytecode. | GUI for decompilation, bytecode editing, and obfuscation tools integration. | Reverse engineering, debugging, modification of compiled Java applications. |
| **CFR (Class File Reader)** | A Java decompiler that generates readable source code from bytecode. | Accurate and robust Java decompilation, including support for newer Java versions. | Decompilation, debugging, reverse engineering. |
| **FernFlower** | A widely used Java decompiler built into tools like IntelliJ IDEA. | Converts Java bytecode back to source code. | Source recovery, reverse engineering. |
| **Jandex** | A Java annotation indexer and bytecode analysis tool. | Efficient annotation indexing, runtime metadata processing. | Annotation processing, metadata analysis. |
| **Ghidra** | A general reverse engineering tool that includes support for Java bytecode. | Disassembler and decompiler for Java, control flow, and data analysis. | Reverse engineering Java applications, security analysis. |
| **Byte Buddy** | A high-level Java library for creating and modifying bytecode. | Runtime code generation, proxies, and instrumentation with a clean and fluent API. | Framework development, runtime instrumentation, AOP (Aspect-Oriented Programming). |
| **javap** | … | … | … |

## How are classes represented in bytecode?

> 

## How are lambda expressions represented in bytecode?

> Lambda expressions in Java are represented in bytecode as a combination of synthetic class, invokedynamic instructions, and references to functional interfaces. When a lambda expression is compiled, the Java compiler generates a synthetic method (usually named something like `lambda$X`), which contains the code for the lambda body. Additionally, it uses the `invokedynamic` instruction to dynamically link the lambda expression to the appropriate functional interface method at runtime, allowing for efficient handling of lambdas in various JVM implementations. This mechanism enables the JVM to treat lambdas as first-class citizens while maintaining compatibility with existing code.
> 

## References

- [hex-to-text](https://cryptii.com/pipes/hex-to-text)
- https://javaalmanac.io/bytecode/versions/
- JVM Bytecode Viewer [https://bytecodeviewer.com/](https://bytecodeviewer.com/)
-