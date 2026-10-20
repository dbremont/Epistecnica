---
tags: [interoperability]
---

# Interoperability


> **Interoperability** refers to the ability of code written in one language to **interact with, use, or be used by code written in another language**. It usually involves mechanisms to **exchange data, call functions, or share resources** across language boundaries without losing type safety, efficiency, or correctness.
> 

> A **language bindings model** defines the approach or methodology used to enable interaction between **different programming languages** by providing mechanisms for accessing foreign code within a native language environment.
> 

## Interoperability Model Set

| **Model** | **Description** | **Canonical Implementation Strategy** | **Cases** |
| --- | --- | --- | --- |
| **Adapter Model** *(Wrapper Model)* | Foreign code is encapsulated behind a wrapper written in the host or bridge language. The wrapper performs type conversion, memory translation, error mapping, and API reshaping. | **Wrapper Layer / Marshaling Layer** | Python `ctypes` wrappers, C++/CLI adapters, Objective-C bridges, handwritten Lua bindings |
| **Foreign Function Interface (FFI) Model** | The host language runtime directly invokes symbols exported by another language/runtime through a defined ABI, usually with minimal abstraction. | **ABI Boundary Invocation** | Rust `extern "C"`, C `dlopen()`/`dlsym()`, Python C API, Lua C API |
| **IDL Model** *(Interface Contract Model)* | Interoperability is defined via a language-neutral interface specification. Tooling generates stubs/proxies for participating languages. | **Contract Compilation / Stub Generation** | CORBA IDL, COM IDL, gRPC Protocol Buffers |
| **Generated Binding Model** *(Reflective / Metadata-Driven Model)* | Bindings are synthesized from metadata, reflection, annotations, headers, or runtime type information rather than being manually authored. | **Binding Generation from Metadata** | SWIG, Java Native Interface helpers, P/Invoke |
| **Component - Service Model** | Interoperability occurs through independently deployable components, services, or runtime modules communicating through stable protocols or binary contracts. | **Protocol Boundary / Component Contract** | COM components, WebAssembly modules, gRPC services, .NET assemblies |

## References

- [Language Binding](https://en.wikipedia.org/wiki/Language_binding)
- [Foreign Function Interface](https://en.wikipedia.org/wiki/Foreign_function_interface)
- https://en.wikipedia.org/wiki/Language_interoperability
- https://en.wikipedia.org/wiki/Component_Object_Model
- https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture