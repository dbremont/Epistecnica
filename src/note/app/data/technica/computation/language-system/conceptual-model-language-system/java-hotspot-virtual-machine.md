---
tags: [language-system]
---

# Java HotSpot Virtual Machine

- [Java](note.html?n=technica/computation/language-system/conceptual-model-language-system/java.md), [Java Bytecode](note.html?n=technica/computation/language-system/conceptual-model-language-system/java-bytecode.md)

> Brought to you by OpenJDK.
> 

## Compile, Build & Debug

> Hostpot **ONLY**.
> 

```bash
# Build Tools
sudo apt install build-essential autoconf zip unzip libx11-dev libxext-dev libxrender-dev libxtst-dev libxt-dev
sudo apt install libasound2-dev libcups2-dev libfontconfig1-dev libfreetype6-dev

# Clone the OpenJDK Repository
git clone git@github.com:openjdk/jdk.git --depth=1
cd jdk
git checkout jdk-20+34

# Building OpenJDK
mkdir build
cd build

# Configure
../configure
or ../configure --with-boot-jdk=/path/to/boot-jdk --enable-debug
or ../configure --with-boot-jdk=/home/dbremont/.sdkman/candidates/java/25.ea.3-open --with-debug-level=slowdebug

# Build
make images
make images LOG=debug
make java
make hostpot
```

## …

```bash
method->name()->as_C_string()
```

## Java Compiler

> 

## Java Virtual Machine

> 

Questions:

- (Java) What is the use of Class ServiceLoader?
- ~~(Java) What is Metaspace?~~
- ~~(Java) What is PermGen space?~~
- ~~(Java) What is the class path?~~
- ~~(Java) What is a class loader?~~
- ~~(Java) What is a classloader leak?~~
- ~~(Java) How can I create a memory leak in Java?~~
- ~~(Java) What is the Hotspot JVM architecture?~~
- ~~(Java) How do we measure the memory footprint?~~
- ~~(Java) What is String Pool?~~
- ~~(Java) How synchronized is implemented?~~
- ~~(Java) How many types of memory areas are allocated by JVM?~~
- ~~(Java) What is a native method?~~

[Here](https://craftinginterpreters.com/a-bytecode-virtual-machine.html)

- Evaluation Strategy,
- Runtime System,
    - stderr,
    - stdout,
    - …,
    - main call,
    - …
- Relational Model Machine,
- Declarative Machine,
- Environment,
- Execution State,
- Parameter Passing
    - Reference,
    - Value,
    - Call by name,
    - Call by need,
    - 
- Reflection Support,
- Evaluation Stack / Thread
- Trigger Store / For Lazy Evaluation
- Store,
    - Mutable,
    - Immutable
- Context-Based Execution / Dynamic Scoping,
- [Tail call](https://en.wikipedia.org/wiki/Tail_call)

The Java Virtual Machine (JVM) is a key component of the Java platform and is responsible for executing Java bytecode. Here are some key characteristics of the JVM:

- **Platform-independent**: The JVM provides a platform-independent execution environment for Java programs. Java code is compiled to bytecode, which can be run on any platform that has a JVM installed.
- **Memory management**: The JVM manages memory allocation and deallocation for Java programs. It provides automatic garbage collection to free up memory that is no longer in use.
- **Security**: The JVM provides a secure execution environment for Java programs by enforcing strict runtime restrictions. This helps to prevent malicious code from executing on a user’s system.
- **Just-in-time (JIT) compilation**: The JVM uses JIT compilation to optimize the performance of Java programs. When a Java program is executed, the JVM dynamically compiles bytecode to machine code, which the CPU can execute directly.
- **Class loading**: The JVM loads classes as needed by the program and can dynamically link classes at runtime. This allows for efficient memory use and can improve performance.
- **Debugging**: The JVM provides tools for debugging Java programs, including the ability to set breakpoints, step through code, and inspect the state of variables.
- **Multithreading**: The JVM supports multithreaded programming in Java, allowing concurrent execution of multiple threads within a single program.

**How does Java find classes?**  📝  Ej: a.Hola

In Java, classes are found using the **classpath mechanism**. When a Java program or application is executed, the Java Virtual Machine (JVM) searches for the required classes and resources in the directories and JAR (Java ARchive) files specified in the classpath.

The classpath can be set using the **CLASSPATH environment variable** or specified explicitly using the **-classpath** or **-cp** option when running the Java application. 

When a class is referenced in the **Java code**:

- By default, the JVM searches for classes in the current directory and the directories specified in the classpath.
- Or,   JVM searches for its corresponding .class file in the directories and **JAR files** specified in the **classpath**. If the class file is found, the JVM loads it into memory and executes the bytecode instructions contained within the class file.
- **If the JVM cannot find the required class** in any **directories** or **JAR files** specified in the classpath, it throws a ClassNotFoundException at runtime. To resolve this issue, the classpath must be configured correctly to include the directory or JAR file containing the required class.

Lambda Implementation:

- [Understanding Java method invocation with invokedynamic](https://blogs.oracle.com/javamagazine/post/understanding-java-method-invocation-with-invokedynamic)
- [What is the point of invokeinterface?](https://stackoverflow.com/questions/1504633/what-is-the-point-of-invokeinterface)
- [A First Taste of InvokeDynamic](http://blog.headius.com/2008/09/first-taste-of-invokedynamic.html)
- [InvokeDynamic: Actually Useful?](http://blog.headius.com/2007/01/invokedynamic-actually-useful)

## Java Agent

> 

```csharp
import java.lang.instrument.Instrumentation;
import java.lang.instrument.ClassFileTransformer;
import java.security.ProtectionDomain;

public class MyAgent {
    public static void premain(String agentArgs, Instrumentation inst) {
        inst.addTransformer(new ClassFileTransformer() {
            @Override
            public byte[] transform(ClassLoader loader, String className, Class<?> classBeingRedefined,
                                    ProtectionDomain protectionDomain, byte[] classfileBuffer) {
                if ("java/lang/NullPointerException".equals(className)) {
                    System.out.println("Intercepting NullPointerException...");
                    // Modify bytecode here (use ASM or Javassist)
                }
                return null;
            }
        });
    }
}
```

**Package and Run it as a Java Agent**:

- Compile it: `javac MyAgent.java`
- Create a manifest file `MANIFEST.MF`:
    
    ```
    Premain-Class: MyAgent
    ```
    
- Package it: `jar cmf MANIFEST.MF myagent.jar MyAgent.class`
- Run Java with the agent: `java -javaagent:myagent.jar -jar MyApplication.jar`
    
    
    ---
    

## References

- https://github.com/openjdk/jdk
- [GNU Autotools](note.html?n=technica/computation/system/operation/operation-conceptual-model/gnu-autotools.md)
- https://hg.openjdk.org/jdk/jdk11/raw-file/tip/doc/building.html
- https://github.com/openjdk
- https://wiki.openjdk.org/display/HotSpot/Main
- https://github.com/openjdk/guide/blob/master/src/guide/building-the-jdk.md
- [OpenJDK Architecture](https://www.dcs.gla.ac.uk/~jsinger/pdfs/sicsa_openjdk/OpenJDKArchitecture.pdf)
- [OpenJDK JVM Internals](http://www.progdoc.de/papers/Jax2012/jax2012.html#(1))
- https://www.youtube.com/watch?v=-vizTDSz8NU&list=PLmkriejCrzaewgvseWHkQPMqtjF69bQH7&index=8
- Scott, M. L. (2015). Programming language pragmatics (4th ed.). Morgan Kaufmann.
- Parr, T. (2010). Language implementation patterns. Pragmatic Programmers.
- Cooper, K. D., Torczon, L. (2012). Engineering a Compiler. Elsevier.
- Yeates, S. A. (1997). Design Pattern in Garbage Collection.
- Nystrom, R. (2021). *Crafting Interpreters*. Genever Benning.
- [On the Formalization of Programming Languages: Early History and Approaches](https://link.springer.com/content/pdf/10.1007/3-540-08766-4_8.pdf)
- [Domain Specific Languages](http://cs448h.stanford.edu/DSEL-Little.pdf)
- Name mangling https://en.wikipedia.org/wiki/Name_mangling
- Flex https://en.wikipedia.org/wiki/Flex_(lexical_analyser_generator)
- Flex Tutorial https://www.geeksforgeeks.org/flex-fast-lexical-analyzer-generator/
- GNU Bison https://en.wikipedia.org/wiki/GNU_Bison
- LLVM Tutorial: Kaleidoscope (Implementing a Language with LLVM) https://github.com/ghaiklor/llvm-kaleidoscope
- https://www.pypy.org/posts/2022/07/toy-optimizer.html
- See https://github.com/postgres/postgres/blob/master/src/backend/jit/llvm/llvmjit_inline.cpp
- https://www.wikiwand.com/en/Code_generation_(compiler)
- https://www.cs.cornell.edu/talc/papers/compile_rtcg.pdf
- https://www.itu.dk/people/sestoft/rtcg/rtcg.pdf
- https://www.youtube.com/watch?v=-ti07Z0xKKg
- Generative Programming and Verification - Nada Amin https://www.youtube.com/watch?v=QuJ-cEvH_oI
- https://github.com/namin/simple-tracing-jit
- https://eli.thegreenplace.net/2013/11/05/how-to-jit-an-introduction
- https://eli.thegreenplace.net/2014/01/15/some-thoughts-on-llvm-vs-libjit
- A Minimal LLVM JIT example for LLVM-5 https://gist.github.com/38/39e7b514d916ed6fa6a2bba629fdf6ff
- Speeding up query execution in PostgreSQL using LLVM JIT compiler https://llvm.org/devmtg/2016-09/slides/Melnik-PostgreSQLLLVM.pdf
- Everything I wish I knew when learning C (tmewett.com) https://news.ycombinator.com/item?id=33773043
- Building An Efficient JIT the best kind of jit https://llvm.org/devmtg/2008-08/Begeman_EfficientJIT.pdf
- Just-In-Time Compiler Library https://www.gnu.org/software/libjit/doc/libjit.html
- libgccjit https://gcc.gnu.org/onlinedocs/gcc-12.2.0/jit/index.html#
- Libgccjit.so: an embeddable JIT-compiler based on GCC https://news.ycombinator.com/item?id=6488120
- https://github.com/spencertipping/jit-tutorial
- Re: Lazy JIT IR code generation to increase JIT speed with partitions https://mail.google.com/mail/u/0/popout?ver=233og3h6h7x7&search=inbox&th=%23thread-f%3A1751047640390109158&cvid=1
- A Minimal LLVM JIT example for LLVM-5 https://gist.github.com/38/39e7b514d916ed6fa6a2bba629fdf6ff
- A Complete Guide to LLVM for Programming Language Creators https://mukulrathi.com/create-your-own-programming-language/llvm-ir-cpp-api-tutorial/
- Numba https://numba.pydata.org/
- How to write a very simple JIT compiler https://github.com/spencertipping/jit-tutorial
- AoT Compiled Languages Metaprogramming: A Nascent Trend Or Another Esoteric Practice? https://dic.dzinko.org/metaprogramming-overview-classification
- https://www.wikiwand.com/en/Runtime_system
- Garbage Collection: https://github.com/pebal/sgcl
- A Compiler for C89 http://tom7.org/abc/
- A Runtime System https://web.archive.org/web/20131230235941/https://users-cs.au.dk/hosc/local/LaSC-3-4-pp343-380.pdf
- [Garbage Collection is Fast, But a Stack is Faster](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.52.1119&rep=rep1&type=pdf)
- [A real-time garbage collector based on the lifetimes of objects](https://dl.acm.org/doi/10.1145/358141.358147)
- [A LISP garbage-collector for virtual-memory computer systems](https://dl.acm.org/doi/10.1145/363269.363280)
- [Garbage Collection Can Be Faster Than Stack Allocation](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.84.2064&rep=rep1&type=pdf)
- [A Unified Theory of Garbage Collection](https://courses.cs.washington.edu/courses/cse590p/05au/p50-bacon.pdf)
- https://www.oilshell.org/blog/2023/01/garbage-collector.html
- **Grammar**
    - https://www.wikiwand.com/en/Formal_grammar
    - https://www.wikiwand.com/en/Backus%E2%80%93Naur_form
- Fully Abstract Models of Programming Languages https://era.ed.ac.uk/bitstream/handle/1842/14496/Stoughton1986.Pdf?isAllowed=y&sequence=1
- [Domain Specific Languages](http://bitrary.softf1.com/images/b/bc/1997_12_15_Domain_Specific_Languages_by_Paul_Hudak.pdf)
- Scott, M. L. (2015). Programming language pragmatics (4th ed.). Morgan Kaufmann.
- Parr, T. (2010). Language implementation patterns. Pragmatic Programmers.
- Cooper, K. D., Torczon, L. (2012). Engineering a Compiler. Elsevier.
- Yeates, S. A. (1997). Design Pattern in Garbage Collection.
- [Syntax Design](https://cs.lmu.edu/~ray/notes/syntaxdesign/)
- [ON THE FORMALIZATION OF PROGRAMMING LANGUAGES: EARLY HISTORY AND MAIN APPROACHES](https://link.springer.com/content/pdf/10.1007/3-540-08766-4_8.pdf)
- https://craftinginterpreters.com/
- [Creating a language using only assembly language](https://speakerdeck.com/nineties/creating-a-language-using-only-assembly-language)
- The Java Langauge Specification
- The Java Virtual Machine
- [VM Options Explorer - OpenJDK11 HotSpot](https://chriswhocodes.com/)
- [List of Java Bytecode Instructions](https://en.wikipedia.org/wiki/List_of_Java_bytecode_instructions)
- [What’s invoke dynamic, and how do I use it?](https://stackoverflow.com/questions/6638735/whats-invokedynamic-and-how-do-i-use-it/6638764)
- [Real-World Bytecode Handling with ASM](https://blogs.oracle.com/javamagazine/post/real-world-bytecode-handling-with-asm)
- [Advanced Java Class Tutorial: A Guide to Class Reloading](https://www.toptal.com/java/java-wizardry-101-a-guide-to-java-class-reloading)
- [Behind the scenes: How do lambda expressions work in Java?](https://blogs.oracle.com/javamagazine/post/behind-the-scenes-how-do-lambda-expressions-really-work-in-java)
- [jvm.go: A JVM written in Go (github.com/zxh0)](https://news.ycombinator.com/item?id=9203045)
- [jvm.go](https://github.com/zxh0/jvm.go)
- Lindholm, T. (1999). The Java virtual machine specification. Addison-Wesley.
- [Open JDK Wiki - HotSpot Internals](https://wiki.openjdk.java.net/display/HotSpot)
- [Tail Call Optimization in the Java HotSpot™ VM](https://ssw.jku.at/Research/Papers/Schwaighofer09Master/schwaighofer09master.pdf)
- [OpenJDK Developers’ Guide](http://openjdk.java.net/guide/)
- [One VM to rule them all](https://github.com/dbremont/Notas/blob/main/Papers/Computacion/One_VM_to_rule_them_all.ipynb)
- [Exploring Aspects of Polyglot High-Performance Virtual Machine GraalVM](https://arxiv.org/pdf/2112.14716.pdf)
- [Solving Java Memory Leaks](https://javaspecialists.teachable.com/courses/enrolled/476938)
- [Linear Scan Registers Allocation for the Java HostPot Client Compiler](https://ssw.jku.at/Research/Papers/Wimmer04Master/Wimmer04Master.pdf)
- [How could I generate and execute machine code at runtime?](https://stackoverflow.com/questions/43255053/how-could-i-generate-and-execute-machine-code-at-runtime)
- [avian](https://github.com/dbremont/avian)
- https://zserge.com/posts/jvm/
- https://en.wikipedia.org/wiki/Java_Virtual_Machine_Tools_Interface