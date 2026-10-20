---
tags: [data-exchange-format]
---

# MessagePack


> **MessagePack** is a **binary data serialization format** that efficiently encodes structured data, making it both compact and fast. It is designed to be more compact and faster than JSON while still being **human-readable** in its deserialized form and easily portable between different programming languages.
> 

QA:

- Does **`MessagePack` has any representation size limits?**
- Which format **`MessagePack`** for serializing strings?
- Which encoding techniques does MessagePack uses?
- What is the name of type aware **serialization formats**?
- Does MessagePack use UTF-8 for string encoding, and can it support other encoding schemes?

## **Key Characteristics of MessagePack**

- **Compact**: Compared to JSON, MessagePack uses a binary encoding, resulting in smaller data sizes for the same data, which improves storage and transmission efficiency.
- **Speed**: Its binary nature allows for faster encoding and decoding compared to text-based formats like JSON or XML, especially with large volumes of data.
- **Language Interoperability**: MessagePack supports multiple programming languages such as Python, C, Java, JavaScript, Ruby, and many more, allowing for easy cross-language communication.
- **Schema-less**: Like JSON, MessagePack does not require predefined schemas, making it flexible and easy to use without the need for complex data models.
- **Self-Describing**: While it is a binary format, MessagePack retains its ability to be used across systems without requiring specific knowledge of the structure beforehand. It encodes basic data types like integers, strings, arrays, and maps.

## Representation

> MessagePack represents data using a **type-length-value (TLV)** encoding scheme. Each value is represented by a **tag byte** followed by the actual data.
> 

```bash
{
  "name": "Alice",
  "age": 30,
  "is_student": false,
  "scores": [95, 87, 91]
}
```

```bash

```

**Design Goals**:

- Compactness: Minimize the size of serialized data.
- Speed: Enable fast serialization and deserialization.
- Interoperability: Support multiple programming languages.

### **Primitive Types**

| **Type** | **Tag Byte (Hex)** | **Description** |
| --- | --- | --- |
| **Positive FixInt** | `0x00` to `0x7F` | Small positive integers (0 to 127). |
| **Negative FixInt** | `0xE0` to `0xFF` | Small negative integers (-32 to -1). |
| **Uint8** | `0xCC` | 8-bit unsigned integer. |
| **Uint16** | `0xCD` | 16-bit unsigned integer. |
| **Uint32** | `0xCE` | 32-bit unsigned integer. |
| **Uint64** | `0xCF` | 64-bit unsigned integer. |
| **Int8** | `0xD0` | 8-bit signed integer. |
| **Int16** | `0xD1` | 16-bit signed integer. |
| **Int32** | `0xD2` | 32-bit signed integer. |
| **Int64** | `0xD3` | 64-bit signed integer. |
| **Float32** | `0xCA` | 32-bit IEEE 754 floating-point number. |
| **Float64** | `0xCB` | 64-bit IEEE 754 floating-point number. |
| **Nil** | `0xC0` | Represents a null value. |
| **True** | `0xC3` | Represents a boolean `true`. |
| **False** | `0xC2` | Represents a boolean `false`. |

### **String Types**

| **Type** | **Tag Byte (Hex)** | **Description** |
| --- | --- | --- |
| **FixStr** | `0xA0` to `0xBF` | Short strings (up to 31 bytes). |
| **Str8** | `0xD9` | Strings up to 255 bytes. |
| **Str16** | `0xDA` | Strings up to 65,535 bytes. |
| **Str32** | `0xDB` | Strings up to 4,294,967,295 bytes. |

### **Binary Data**

| **Type** | **Tag Byte (Hex)** | **Description** |
| --- | --- | --- |
| **Bin8** | `0xC4` | Binary data up to 255 bytes. |
| **Bin16** | `0xC5` | Binary data up to 65,535 bytes. |
| **Bin32** | `0xC6` | Binary data up to 4,294,967,295 bytes. |

### **Array Types**

| **Type** | **Tag Byte (Hex)** | **Description** |
| --- | --- | --- |
| **FixArray** | `0x90` to `0x9F` | Small arrays (up to 15 elements). |
| **Array16** | `0xDC` | Arrays up to 65,535 elements. |
| **Array32** | `0xDD` | Arrays up to 4,294,967,295 elements. |

### **Map Types**

| **Type** | **Tag Byte (Hex)** | **Description** |
| --- | --- | --- |
| **FixMap** | `0x80` to `0x8F` | Small maps (up to 15 key-value pairs). |
| **Map16** | `0xDE` | Maps up to 65,535 key-value pairs. |
| **Map32** | `0xDF` | Maps up to 4,294,967,295 key-value pairs. |

## Limitations

Although **MessagePack** is a highly efficient binary serialization format, it has certain **limitations** that can impact its usability in specific scenarios.

| **Category** | **Limitation** | **Details** |
| --- | --- | --- |
| **Maximum Object Size** | **Limited by system memory** | MessagePack does not impose a strict limit on object size, but practical limits arise from available memory and implementation-specific constraints. |
| **Lack of Schema Support** | **No built-in schema enforcement** | Unlike Avro or Protocol Buffers, MessagePack does not enforce schemas, which can lead to compatibility issues if structure changes over time. |
| **Lack of Human Readability** | **Binary format is not human-readable** | Unlike JSON or XML, debugging and inspecting MessagePack data requires a decoder, making manual edits difficult. |
| **Floating-Point Precision** | **Supports only IEEE 754 float32 and float64** | Does not support float16, which may be useful in deep learning or low-precision applications. |
| **Data Type Ambiguity** | **No explicit type definitions** | MessagePack does not differentiate between integer types at serialization time (e.g., `int8` vs `int32`), which can lead to ambiguity when interpreting data. |
| **No Built-in Date/Time Support** | **Requires custom serialization** | MessagePack does not have a native timestamp or datetime type, requiring users to encode them as integers or strings. |
| **UTF-8 Only for Strings** | **Does not support other encodings** | All string data in MessagePack must be UTF-8 encoded, which may be limiting for certain binary text formats. |
| **Limited Extensibility** | **Custom types require `ext` extension types** | MessagePack does support extensions, but they require additional handling, making them less portable across different implementations. |
| **No Built-in Compression** | **Relies on external compression** | Unlike formats like Avro, MessagePack does not include built-in compression, requiring additional layers like gzip or zstd. |

**Workarounds & Alternatives**

- **For Schema Enforcement**: Use **MessagePack with external schemas** (e.g., **JSON Schema** or **Protobuf** for validation).
- **For Human Readability**: Convert MessagePack data to **JSON** for debugging.
- **For Datetime Support**: Use a standardized format like **ISO 8601** as a string or Unix timestamp as an integer.
- **For Compression**: Use **zlib**, **gzip**, or **zstd** for reducing serialized size.

## Performace

> Worklod  / Time  → Serialie  / Deserialize.
> 

| **Metric** | **What to Measure** | **Why It Matters** | **Metric Unit** |
| --- | --- | --- | --- |
| **Serialization Time** | Time taken to serialize the data (convert from Python object to binary format). | Helps understand how fast the system can convert data to a compact binary format. | Time per operation (e.g., seconds) |
| **Deserialization Time** | Time taken to deserialize the data (convert from binary back to Python object). | Deserialization speed is crucial for systems that need to quickly read and process data. | Time per operation (e.g., seconds) |
| **Throughput (Serialization Rate)** | How much data can be serialized per unit of time (bytes per second). | Critical for large datasets or high-frequency operations. | Bytes per second or operations/second |
| **Deserialization Throughput** | How much data can be deserialized per unit of time. | Shows efficiency of reading and unpacking data at scale. | Bytes per second or operations/second |
| **Memory Usage** | The memory footprint when serializing and deserializing data. | Important for systems with limited resources (e.g., embedded systems, high-performance systems). | Memory in bytes |
| **Compression Ratio** | How much smaller the serialized data is compared to the original data. | Key for storage efficiency, especially with large data. | Size of serialized data / Size of original data |
| **Latency (Round Trip Time)** | Time taken for a single round-trip: serialize, transmit (if applicable), and deserialize. | Key for networked or distributed systems where data is serialized, sent, and deserialized. | Time per round-trip operation |
| **Scalability (With Data Size)** | Performance as the data size increases. Measure how serialization/deserialization times change with data size. | Identifies potential bottlenecks as the data grows. | Time as a function of data size |
| **Thread/Concurrency Performance** | How the system performs under multithreaded conditions. | Ensures serialization/deserialization doesn't become a bottleneck in high-concurrency systems. | Throughput with multi-threading vs. single-threaded, CPU usage |
| **CPU Usage** | Measure CPU consumption during serialization and deserialization. | High CPU usage could indicate inefficiency, especially in resource-constrained environments. | CPU time / Percentage of total CPU usage |
| **Error Handling (Exception Rate)** | Track how often errors (e.g., deserialization errors) occur under normal and edge cases. | Stability is important for production systems; high error rates can indicate reliability issues. | Number of errors per operation or per test |

## References

- https://msgpack.org/index.html
- [UTF-8](note.html?n=technica/computation/representation/conceptual-model-computational-representation/utf-8.md)
- https://github.com/dbremont/snippets
- - [Python: Type System]
- https://github.com/csiglab/language-system-labs
- - [Representation Problem: Text (String)]
- https://news.ycombinator.com/item?id=42663047
- See https://github.com/pydantic/pydantic
- [How to conduct a performance evaluation?](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/how-to-conduct-a-performance-evaluation.md)
- https://github.com/fabianoriccardi/benchmark-json-messagepack/blob/master/data_analysis.ipynb
- https://jsonjoy.com/blog/json-codec-benchmarks
- [‣](https://app.notion.com/p/b0a2a8d65e9d46d3b9ccfe1614c1bd73?pvs=21)
- [Performace](note.html?n=technica/computation/system/evaluation/performace.md)
- 
- https://en.wikipedia.org/wiki/Speedup
- [https://acg.cis.upenn.edu/milom/cis501-Fall12/lectures/04_performance.pdf](https://acg.cis.upenn.edu/milom/cis501-Fall12/lectures/04_performance.pdf)
- https://math.stackexchange.com/questions/3108221/a-is-x-more-than-b
- https://svn.vsp.tu-berlin.de/repos/public-svn/publications/kn-old/strc/html/node9.html
- [https://people.cs.pitt.edu/~childers/CS0447/lectures/lect-performance.pdf](https://people.cs.pitt.edu/~childers/CS0447/lectures/lect-performance.pdf)
- Speed-Up Ratio Normalized Time → …
- https://news.ycombinator.com/item?id=4090831