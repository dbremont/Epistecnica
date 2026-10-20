---
tags: [javascript, language-system, tool]
---

# V8 JavaScript Engine

- [NodeJS](note.html?n=technica/computation/language-system/conceptual-model-language-system/nodejs.md)

> Note: We are saved; NodeJs comes with a version of V8;   that’s a lot easier to debug; sinse  I want to understand both.
> 

QA:

- How to create  a small web service?
- …

```bash

## Well Building V8 Is Hard Stuff ???; Let's Try Using The Library !!!

## Clone
git clone https://github.com/v8/v8.git --depth 1    

## Dependencies
sudo apt update
sudo apt install -y python3 git curl build-essential clang libc++-dev libc++abi-dev
```

```cpp
g++ -std=c++17 -o node_v8_example main.cpp -I/usr/include/node -L/usr/lib/x86_64-linux-gnu -lnode -pthread  
```

```cpp

#include <v8.h>
#include <iostream>
#include <memory>
#include <libplatform/libplatform.h>

using namespace v8;

void RunV8Script() {
    // Initialize ICU and other V8 internal data
    V8::InitializeICUDefaultLocation("");
    V8::InitializeExternalStartupData("");

    // Use V8's default ArrayBuffer allocator
    v8::ArrayBuffer::Allocator* allocator = v8::ArrayBuffer::Allocator::NewDefaultAllocator();

    // Create a platform
    std::unique_ptr<Platform> platform = v8::platform::NewDefaultPlatform();
    
    // Check if the platform was created successfully
    if (!platform) {
        std::cerr << "Error: Unable to create platform." << std::endl;
        return;
    }

    // Initialize the platform and V8 itself
    V8::InitializePlatform(platform.get());
    V8::Initialize();

    // Set up Isolate with the ArrayBufferAllocator
    Isolate::CreateParams create_params;
    create_params.array_buffer_allocator = allocator;

    // Create the isolate
    Isolate* isolate = Isolate::New(create_params);

    {
        Isolate::Scope isolate_scope(isolate);
        HandleScope handle_scope(isolate);

        // Create a new V8 context
        Local<Context> context = Context::New(isolate);
        Context::Scope context_scope(context);

        // JavaScript code to run
        Local<String> source = String::NewFromUtf8(isolate, "'Hello from V8'.toUpperCase()",
                                                   NewStringType::kNormal).ToLocalChecked();

        // Compile and run the JavaScript
        Local<Script> script = Script::Compile(context, source).ToLocalChecked();
        Local<Value> result = script->Run(context).ToLocalChecked();

        // Convert result to UTF-8 and print it
        String::Utf8Value utf8(isolate, result);
        std::cout << "Result from V8: " << *utf8 << std::endl;
    }

    // Clean up and shutdown V8
    isolate->Dispose();
    V8::Dispose();
    V8::ShutdownPlatform();

    // Delete the custom allocator after usage
    delete allocator;
}

int main() {
    RunV8Script();
    return 0;
}

```

## References

- [V8 JavaScript engine](https://v8.dev/)
- [Background Compilation](https://v8.dev/blog/background-compilation)
- A Deep Dive Into V8 / [https://blog.appsignal.com/2020/07/01/a-deep-dive-into-v8.html](https://blog.appsignal.com/2020/07/01/a-deep-dive-into-v8.html)