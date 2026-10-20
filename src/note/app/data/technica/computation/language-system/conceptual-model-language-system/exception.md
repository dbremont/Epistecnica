---
tags: [effect-system]
---

# Exception

- [Effect System](note.html?n=technica/computation/language-system/conceptual-model-language-system/effect-system.md)

Exception: In programming, an exception is an event that occurs during the execution of a program that disrupts the normal flow of control. When an exception is thrown, the program transfers control to an exception handler, which is a block of code that is designed to handle the exception and recover from the error.

Exceptions are commonly used to handle errors and other exceptional conditions in a program. For example, if a program tries to divide by zero or access an invalid memory address, it will typically throw an exception. The exception handler can then take appropriate action, such as displaying an error message, logging the error, or trying to recover from the error and continue execution.

Exceptions are typically implemented using a try-catch-finally block, which is a programming construct that allows the program to catch and handle exceptions. In a try-catch-finally block, the code that might throw an exception is enclosed in a try block, and any exceptions that are thrown are caught and handled by one or more catch blocks. The finally block is used to specify code that should be executed regardless of whether an exception is thrown or not.