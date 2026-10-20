# Rust Attributes (Annotations)

Rust attributes, often referred to as annotations in other programming languages, provide metadata to the compiler about various elements of the code such as functions, structs, modules, etc. These attributes can instruct the compiler to perform certain actions, apply optimizations, or modify certain behaviors. Here's a comprehensive list of commonly used Rust attributes:

### 1. **Compiler Directives**

- `#[derive(...)]`: Automatically implements specified traits for structs or enums (e.g., `Debug`, `Clone`, `Copy`).
- `#[inline]`: Suggests that the compiler should inline a function.
- `#[repr(...)]`: Specifies the layout of structs, unions, and enums in memory (e.g., `C`, `packed`).
- `#[cfg(...)]`: Conditional compilation based on flags passed to the compiler.

### 2. **Lint Checks**

- `#[allow(...)]`: Disables certain compiler warnings (lint checks) for the annotated part.
- `#[warn(...)]`: Emits a compiler warning for the specified lint rule when violated.
- `#[deny(...)]`: Emits a compiler error (instead of a warning) for the specified lint rule when violated.
- `#[forbid(...)]`: Similar to `deny`, but also prevents overriding the behavior further down in the code hierarchy.

### 3. **Testing**

- `#[test]`: Marks a function as a unit test.
- `#[should_panic]`: Marks a test function that should panic to pass.
- `#[ignore]`: Ignores the test function unless specifically requested.

### 4. **Linking and Loading**

- `#[link]`: Specifies a native library to be linked.
- `#[link_name = "name"]`: Specifies the symbol name for linking.
- `#[no_link]`: Used in procedural macros to prevent linking of the specified library unless it is explicitly used.

### 5. **Function and Closure Attributes**

- `#[panic_handler]`: Defines the function as the panic handler for the application.
- `#[main]`: Indicates the entry point function when using a custom entry point.
- `#[global_allocator]`: Specifies a global memory allocator.

### 6. **Module and Crate Attributes**

- `#[path = "file.rs"]`: Specifies the path to a module file.
- `#[macro_use]`: Enables macros imported from a module to be used in the current scope.
- `#[crate_type = "..."]`: Specifies the type of the output artifact (e.g., `bin`, `lib`).
- `#[crate_name = "..."]`: Specifies the name of the crate.

### 7. **Documentation**

- `#[doc = "..."]`: Adds documentation text to the specified item.

### 8. **Visibility and Privacy**

- `#[public]`: An experimental feature to make items public.
- `#[doc(hidden)]`: Hides an item from generated documentation.

### 9. **Unsafe Code**

- `#[unsafe]`: Used for blocks of code or functions where unsafe Rust is necessary.

### 10. **Procedural Macros**

- `#[proc_macro]`: Defines a function as a procedural macro.
- `#[proc_macro_derive(...)]`: Allows custom derive macros.
- `#[proc_macro_attribute]`: Defines an attribute macro.

### 11. **Optimizations and Code Generation**

- `#[no_std]`: Indicates that the standard library is not used, typically for embedded programming.
- `#[no_mangle]`: Prevents the Rust compiler from mangling the function's name or variable.
- `#[cold]`: Suggests that a function is unlikely to be executed, potentially influencing branch prediction and code layout optimizations.

These attributes allow developers to provide instructions and metadata that can influence compilation, runtime behavior, and more, making them a powerful tool in Rust development.

## References

[Attributes](https://doc.rust-lang.org/reference/attributes.html#attributes)