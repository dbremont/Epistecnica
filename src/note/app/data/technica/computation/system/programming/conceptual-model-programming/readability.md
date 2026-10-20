---
tags: [principle]
---

# Readability

- [Code Reading](note.html?n=technica/computation/system/programming/conceptual-model-programming/code-reading.md)

> **Understanding** is a **cognitive process** involving acquiring knowledge or comprehending a particular concept or idea. It typically consists of interpreting information, connecting different pieces, and forming a mental model of the concept or idea.
> 

> The reader has a **mental model** of the function; how hard is it to match **mental model** constructs to **function constructs**?
> 

> **Intelligibility: …**
> 

## Índice

## Criteria for Evaluating Code Readability

> Evaluating the **understandability or readability** of a program involves assessing various aspects of the code that contribute to how easily it can be read, understood, and maintained.
> 

> A theory that explains why humans **x**, **y** in their understanding of program p.
> 

| **Criteria** | **Description** | **Importance** |
| --- | --- | --- |
| **Code Structure** | The overall organization of code, including the use of functions, classes, and modules. | High |
| **Indentation and Formatting** | Consistent indentation, spacing, and line breaks make the code visually organized. | High |
| **Variable Naming** | Use meaningful, descriptive, consistent names for variables, functions, and classes. | High |
| **Commenting and Documentation** | Appropriate use of comments to explain complex logic and documentation for public interfaces. | High |
| **Function Length** | Functions should be short, focused, and do one thing well. | Medium |
| **Use of Descriptive Constants** | Use of constants instead of magic numbers or strings. | Medium |
| **Modularity** | Code is divided into well-defined, reusable modules or functions. | High |
| **Control Flow Simplicity** | Use simple control flow structures (e.g., avoiding deeply nested loops or conditionals). | High |
| **Error Handling** | Clear and consistent handling of errors and exceptions. | Medium |
| **Code Duplication** | Avoid repeated code blocks, promoting DRY (Don't Repeat Yourself) principles. | Medium |
| **Consistency** | Uniform use of coding style, conventions, and patterns throughout the codebase. | High |
| **Language Idioms** | Appropriate use of language-specific idioms and features. | Medium |
| **Use of Comments for Intent** | Comments should explain why something is done, not just what is done. | Medium |
| **Logical Grouping** | Related code elements are grouped logically. | Medium |
| **Use of Language Features** | Efficient use of the programming language's features and standard libraries. | Medium |
| **Error Messages** | Clear, informative error messages help with debugging. | Medium |
| **Code Complexity** | Low cyclomatic complexity, making the code easier to understand and test. | High |
| **Testability** | Code is written in a way that makes it easy to write unit and integration tests. | Medium |
| **Documentation** | Clear, concise, and up-to-date codebase documentation, especially for APIs. | High |
| **Naming Conventions** | Consistent use of naming conventions (e.g., camelCase, PascalCase) across the codebase. | High |

## Function

> The **theory of function** readability based on mental model mapping emphasizes the importance of aligning function constructs with the reader's mental models. By focusing on clarity, consistency, and simplicity, function design can improve readability and ease of understanding, ultimately leading to more maintainable and reliable code.
> 

> **Function Understanding**: …
> 

> The t**heory of function readability** based on "reader mental models" posits that the ease with which a reader can understand a function depends on how effectively the constructs in their mental model of the function map to the actual constructs within the function. This theory integrates cognitive psychology with software engineering to provide a framework for designing functions that align with users' mental models, thereby enhancing readability and comprehension.
> 

Here is a table that summarizes the principles and techniques for improving function readability, along with the refactoring steps applied to the example function:

| **Factors** | **Definition** | **Impact on Readability** |
| --- | --- | --- |
| **Single Responsibility Principle (SRP)** | A function should have one reason to change and only one reason. It should perform a single task or represent a single concept. | Easier to understand, test, and debug. |
| **Descriptive Naming** | Function names should clearly describe what the function does. | Understand the function's purpose without reading its implementation. |
| **Function Length** | Functions should be short, typically between 5-20 lines. | Short functions are easier to understand and navigate. |
| **Consistent Naming Conventions** | Use a consistent naming convention across the codebase. | Recognizing patterns and understanding the code faster. |
| **Minimize Side Effects** | Functions should minimize changes to the state or interactions with the outside world. | More straightforward to reason about and debug. |
| **Clear Parameter Usage** | Limit the number of parameters and use default or objects to encapsulate multiple parameters. | Functions with fewer parameters are easier to understand and use. |
| **Proper Use of Comments** | Use comments to explain why a particular code exists rather than what it does. | Comments should provide context and explanations for non-obvious logic. |
| **Avoid Deep Nesting** | Avoid deep nesting of loops and conditionals. | Deeply nested code is more complex to read and understand. |

## References

[Program Understanding: Models and Experiments](https://www.sciencedirect.com/science/article/abs/pii/S0065245808605434)