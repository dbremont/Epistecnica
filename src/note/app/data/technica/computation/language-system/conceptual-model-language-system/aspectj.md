---
tags: [metacomputation, tool]
---

# AspectJ


> **AspectJ** is an aspect-oriented programming (AOP) framework for Java that enables the modularization of cross-cutting concerns—such as logging, security, and transaction management—by allowing developers to define and apply aspects that are woven into the codebase at compile-time, load-time, or runtime.
> 

QA:

- …

## Index

```bash
mvn archetype:generate -DgroupId=com.example -DartifactId=hello-world-aspectj -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

```bash
mvn aspectj:help
```

```xml
<pluginExecution>
	<pluginExecutionFilter>
		<groupId>
			org.codehaus.mojo
		</groupId>
		<artifactId>
			aspectj-maven-plugin
		</artifactId>
		<versionRange>
			[1.4,)
		</versionRange>
		<goals>
			<goal>compile</goal>
			<goal>test-compile</goal>
		</goals>
	</pluginExecutionFilter>
	<action>
		<ignore />
	</action>
</pluginExecution>
```

## Compilation

> AspectJ primarily uses an extended version of the **Eclipse Java Compiler (ECJ)** to handle Java and AspectJ constructs. The AspectJ compiler, known as **ajc** (AspectJ Compiler), processes `.aj` files and weaves aspect-oriented constructs into Java bytecode.
> 

It operates in two modes:

1. **Source-to-bytecode compilation** – Compiles Java and AspectJ source files directly into `.class` files.
2. **Bytecode weaving** – Enhances existing compiled Java bytecode with aspects, either at compile-time, post-compile-time, or load-time.

## Debug

> **Note**: **AspectJ** uses **JDT Core** as its compiler. Download the **AspectJ** source code and debug it !!!
> 

```bash
https://help.eclipse.org/latest/index.jsp?topic=/org.eclipse.jdt.doc.isv/guide/jdt_api_compile.htm
```

```bash
-Xajruntimetarget:1.9 -encoding ISO-8859-1 -outxml -showWeaveInfo -source 1.8 -target 1.8 -verbose -classpath /home/dvictoriano/type-system/aspectjrt.jar:/home/dvictoriano/type-system/aspectjtools.jar:/home/dvictoriano/type-system/aspectjweaver.jar -d /home/dvictoriano/type-system/target/classes /home/dvictoriano/type-system/Perro.java /home/dvictoriano/type-system/Animal.java /home/dvictoriano/type-system/Main.java
```

Break points:

- AjBuildManager [line: 188] - batchBuild(AjBuildConfig, IMessageHandler)
- AjBuildManager [line: 192] - incrementalBuild(AjBuildConfig, IMessageHandler)
- AjBuildManager [line: 202] - performBuild(AjBuildConfig, IMessageHandler, boolean)
- AjBuildManager [line: 275] - performBuild(AjBuildConfig, IMessageHandler, boolean)
- AjBuildManager [line: 826] - initBcelWorld(IMessageHandler)
- AjBuildManager [line: 1016] - performCompilation(Collection
    
    )
    
- AjBuildManager [line: 1101] - performCompilation(Collection
    
    )
    
- AjdtCommand [line: 44] - runCommand(String[], IMessageHandler)
- AjdtCommand [line: 77] - doCommand(IMessageHandler, boolean)
- Compiler [line: 391] - beginToCompile(ICompilationUnit[])
- Compiler [line: 435] - compile(ICompilationUnit[], boolean)
- Compiler [line: 842] - internalBeginToCompile(ICompilationUnit[], int)
- Main [line: 230] - runMain(String[], boolean)
- Main [line: 333] - run(String[], IMessageHolder)
- Parser [line: 1345] - consumeRule(int)
- TheOriginalJDTParserClass [line: 10707] - parse()
- TheOriginalJDTParserClass [line: 10812] - parse()
- TheOriginalJDTParserClass [line: 11069] - parse(ICompilationUnit, CompilationResult, int, int)

/home/dbremont/.local/bin

https://github.com/eclipse/org.aspectj / No se como pero la clase Compiler se le agrega

public void compile(ICompilationUnit[] sourceUnits) { CompilerAdapter.aspectOf().ajc*before*org_aspectj_ajdt_internal_compiler_CompilerAdapter$14*c*37*d*260(*this*, *sourceUnits*); *this*.*compile*(*sourceUnits*, *false*); *CompilerAdapter*.*aspectOf*().*ajc*afterReturning$org_aspectj_ajdt_internal_compiler_CompilerAdapter2f9cc9ca0(this); }

---

https://gitlab.com/dbremont/commonplace/-/blob/main/loci/2022-3-st-aspejectj.md

aspectjrt - the AspectJ runtime aspectjweaver - the AspectJ weaver aspectjtools - the AspectJ compiler aspectjmatcher - the AspectJ matcher

Uses - JDT compiler Modified Compiler: - https://search.maven.org/search?q=org.eclipse.jdt.core - https://github.com/eclipse/aspectj.eclipse.jdt.core

Uses: BCEL weaving library / https://commons.apache.org/proper/commons-bcel/manual/jvm.html

===============================

First study the AspectJ model.

AjBuildManager: Orchetraste the computation. Weaving the annotations.

MessageHandler This abstraction accumulates messages. To control accumulated, clients can ignore messages of a given kind, or install a listener/interceptor. The interceptor handles all messages (even null) first and can halt further processing/accumulation by returning true.

MessageHandler Interceptors: Implement the verbose functionality.

Trace / TraceFactory / Rastro Is a history of an execution of a program in a machine.

A program trace lists the addresses of instructions executed and data referenced during a program’s execution. Earlier approaches to collecting program traces, including abstract execution and optimal control tracing, are reviewed. Two tracing systems based on these techniques are presented. Results collected when using the later systems on several programs show significant reductions in the cost of collecting traces. Reduction in trace file sizes is also significant.

ICommand: runCommand(args[], messageHandler) , repeatCommand

World: A world is a collection of known types and crosscutting members.

CrosscuttingMembersSet: This holds on to all CrosscuttingMembers for a world. It handles the management of change.

BcelWeaver:

org.aspectj.org.eclipse.jdt.internal.compiler.Compiler - Compiler

ICompilerRequestor: Callback interface for receiving compilation results.

CompilerAdapter:

AspectJBuilder:

TheOriginalJDTParserClass: AspectJ Extention made a few changes to increase accessibility. Several changes to load static tables relative to different classes.

## References

- https://github.com/eclipse-aspectj/aspectj
- https://www.mojohaus.org/aspectj-maven-plugin/ajc_reference/standard_opts.html
- https://stackoverflow.com/questions/24206634/error-while-compiling-when-using-aspectj-compiler-instead-of-javac
- https://eclipse.dev/aspectj/doc/released/devguide/index.html
- https://www.mojohaus.org/aspectj-maven-plugin/ajc_reference/standard_opts.html
- https://stackoverflow.com/questions/9248267/how-can-i-specify-the-encoding-of-java-source-files
- [How does AspectJ work?](https://stackoverflow.com/questions/41974800/how-does-aspectj-work)
- [https://bugs.eclipse.org/bugs/buglist.cgi?order=component%2Cresolution%2Cbug_status%2Cpriority%2Cassigned_to%2Cbug_id&product=AspectJ&query_format=advanced](https://bugs.eclipse.org/bugs/buglist.cgi?order=component%2Cresolution%2Cbug_status%2Cpriority%2Cassigned_to%2Cbug_id&product=AspectJ&query_format=advanced)
- [Apache Maven](note.html?n=technica/computation/system/operation/operation-conceptual-model/apache-maven.md)
- https://eclipse.dev/aspectj/
- https://eclipse.dev/aspectj/doc/latest/devguide/ajc.html
- https://eclipse.dev/aspectj/doc/released/progguide/index.html
- [https://mvnrepository.com/artifact/com.nickwongdev/aspectj-maven-plugin/1.12.6](https://mvnrepository.com/artifact/com.nickwongdev/aspectj-maven-plugin/1.12.6)
- Laddad, R. (2003). AspectJ in action : practical aspect-oriented programming. Manning.
- https://en.wikipedia.org/wiki/Trace_theory
- https://en.wikipedia.org/wiki/History_monoid
- An Explicit Strategy to Scaffold Novice Program Tracing https://dl.acm.org/doi/10.1145/3159450.3159527
- Efficient program tracing https://dl.acm.org/doi/10.1109/2.211900
- Aspects for Trace Monitoring https://link.springer.com/chapter/10.1007/11940197_2
- https://help.eclipse.org/latest/index.jsp?topic=/org.eclipse.jdt.doc.isv/guide/jdt_api_compile.htm
- [‣](https://app.notion.com/p/163598edb7908099bc04f882d42c37c1?pvs=21)