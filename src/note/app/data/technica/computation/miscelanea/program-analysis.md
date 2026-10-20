---
tags: [language-system, program-analysis]
---

# Program Analysis


> **Program Analysis:** The systematic extraction of semantic, structural, or behavioral properties from software artifacts through formal or empirical methods.
> 

## …

1. **What are the objects of analysis in Program Analysis?**
    - Source code (AST, tokens, syntax trees)
    - Intermediate representations (IR, bytecode, SSA form)
    - Control-flow and data-flow graphs
    - Execution traces and runtime states (in dynamic analysis)
    - Build artifacts and dependency graphs
2. **What categories of properties are analyzed?**
    - Syntactic correctness
    - Type consistency
    - Control-flow integrity
    - Data-flow safety
    - Resource usage (memory, CPU, I/O)
    - Security vulnerabilities
    - Conformance to coding standards (lint rules)
3. **What types of data does Program Analysis operate on?**
    - Lexical tokens
    - Abstract Syntax Trees (AST)
    - Symbol tables
    - Type environments
    - CFG / DFG
    - Points-to graphs
    - Abstract domains (intervals, lattices, constraints)
    - Runtime logs and traces
    - Profiling samples
4. **What is the provenance of that data?**
    - Compiler front-end parsing
    - Static code inspection
    - Instrumented execution
    - Build systems
    - Version control history
5. **How is the data captured or constructed?**
    - Parsing and lexical analysis
    - Semantic analysis phases
    - IR generation
    - Static instrumentation
    - Dynamic instrumentation (profilers, tracers)
    - Constraint solving and symbolic execution
6. **What distinguishes a Linter from broader Program Analysis?**
    - Is the analysis purely syntactic, or semantic?
    - Does it reason about execution paths?
    - Does it build a full control-flow or type model?
    - Is it rule-based or flow-sensitive?
7. Which are the major branches of program analysis?

## Major Branches of Program Analysis

Program analysis can be classified along several orthogonal axes:

### A. By Execution Dependency

1. **Static Analysis**
    - No program execution required
    - Examples: abstract interpretation, type systems, data-flow analysis
2. **Dynamic Analysis**
    - Requires execution
    - Examples: profiling, tracing, runtime verification
3. **Hybrid Analysis**
    - Combines static and dynamic techniques

### B. By Theoretical Foundation

1. **Data-Flow Analysis**
2. **Control-Flow Analysis**
3. **Abstract Interpretation**
4. **Symbolic Execution**
5. **Model Checking**
6. **Type-Based Analysis**
7. **Constraint-Based Analysis**

### C. By Sensitivity Dimensions

1. Flow-sensitive vs. flow-insensitive
2. Path-sensitive vs. path-insensitive
3. Context-sensitive vs. context-insensitive
4. Field-sensitive vs. field-insensitive

### D. By Purpose

1. Correctness verification
2. Optimization
3. Security analysis
4. Refactoring and maintenance
5. Program understanding

## References

- https://en.wikipedia.org/wiki/Program_analysis
- https://en.wikipedia.org/wiki/Lint_(software)