---
tags: [note, guia]
---

# A Guide to Binary Tools


> **Binary tools** are utilities that manipulate, analyze, or transform binary executables, object files, and libraries, including assemblers, linkers, debuggers, disassemblers, and format-specific tools like `objdump`, `readelf`, and `strip`.
> 

## Taxonomy

| **Category** | **Subcategory** | **Description** | **Tools/Examples** |
| --- | --- | --- | --- |
| **Static Analysis** | **Disassembly** | Converts binary code into assembly language instructions. | IDA Pro, Ghidra, Radare2, Capstone, objdump |
|  | **Decompilation** | Translates binary code into high-level code (e.g., C, Python). | Hex-Rays Decompiler, Ghidra, RetDec, Snowman |
|  | **Binary Inspection** | Direct examination of the binary file (e.g., headers, sections, symbols). | Binwalk, readelf, PEView, objdump |
|  | **Control Flow Analysis** | Analyzes control flow graphs (CFGs) to understand the program’s logic. | IDA Pro, Ghidra, angr |
|  | **Data Flow Analysis** | Traces how data moves through the program statically. | angr, CodeQL |
|  | **ELF Analysis** |  | `readelf`, `eu-readelf`, `file`,  ldd |
| **Dynamic Analysis** | **Execution Tracing** | Monitors program execution to capture runtime behavior. | Strace, ltrace, Frida |
|  | **Debugging** | Stepping through the binary to understand its runtime behavior. | GDB, WinDbg, LLDB |
|  | **Instrumented Execution** | Modifies or hooks into the binary to monitor or manipulate its execution. | PIN, DynamoRIO, Intel PT |
|  | **Behavioral Analysis** | Observes the behavior of the binary in a controlled environment (e.g., malware). | Cuckoo Sandbox, ANY.RUN, Hybrid Analysis |
| **File Format Analysis** | **Header Analysis** | Examines binary file headers (e.g., ELF, PE, Mach-O). | readelf, PEStudio, dumpbin |
|  | **Section Analysis** | Analyzes sections (e.g., text, data, bss, resource). | objdump, Radare2, Ghidra |
|  | **Signature Matching** | Identifies known patterns in binaries, such as malware signatures or library functions. | YARA, ClamAV |
| **Symbolic Analysis** | **Symbolic Execution** | Explores binary paths using symbolic values instead of concrete inputs. | angr, KLEE, S2E |
|  | **Constraint Solving** | Solves logical constraints generated during symbolic analysis. | Z3 Solver, Boolector |
| **Fuzzing** | **Input Generation** | Generates random or structured inputs to test the binary’s behavior. | AFL (American Fuzzy Lop), LibFuzzer, Peach |
|  | **Code Coverage Analysis** | Tracks which parts of the binary were executed during fuzzing. | gcov, lcov, Sanitizers |
| **Threat Analysis** | **Malware Reverse Engineering** | Dissects malicious binaries to understand functionality, C2 mechanisms, or payloads. | IDA Pro, Ghidra, x64dbg, OllyDbg |
|  | **Exploit Development** | Analyzes vulnerabilities in binaries for potential exploitation. | Immunity Debugger, Pwntools, ROPgadget |
| **Binary Inspection & Modification** | **Patching** | Modifies binary code to alter functionality. | Radare2, HxD, Hex Fiend |
|  | **Injection** | Injects new code or data into an existing binary. | Metasploit, Shellcode injection tools, Frida |
|  |  |  | **hexdump, xxd, od** |
|  |  |  | **bvi** |
|  | **Symbol Table Inspection** |  | nm, objdump -t, readelf --syms |
|  | **Instrumentation** |  | `pin`, `dynamorio`, `frida` |
|  | **Stripping and Debug Info** |  | `strip, dwz, eu-strip` |
| **Performance Profiling** | **Runtime Profiling** | Measures performance metrics like CPU usage, memory allocation, and execution time. | perf, Valgrind, VTune |
| **Cryptographic Analysis** | **Key/Signature Extraction** | Extracts cryptographic keys or identifies cryptographic algorithms used in binaries. | Binwalk, Cryptoscan |
|  | **Entropy Analysis** | Measures randomness in binary sections to detect encrypted or packed regions. | binwalk, Detect It Easy (DIE) |
| **Obfuscation Analysis** | **Unpacking** | Identifies and removes packing layers to access the original binary. | UPX, Unpacker scripts, Generic unpackers in IDA Pro or Ghidra |
|  | **Deobfuscation** | Simplifies obfuscated code or control flows to improve readability. | Radare2, Ghidra, IDA Pro |
| **Machine Learning** | **Binary Classification** | Uses ML models to classify binaries as malicious, benign, or specific categories. | MalConv, Ember |
|  | **Feature Extraction** | Extracts features (e.g., opcode sequences) for machine learning analysis. | BinaryAI, custom feature extraction scripts |
| **Binary Editor** |  |  | binwalk |
|  |  |  | strings |
|  |  |  | fileTools |

## References

- [Binary Analysis](https://wpcdn.web.wsu.edu/wp-vcea/uploads/sites/3267/2022/06/BinaryAnalysis101.pdf)
- https://medium.com/@bugprove/basics-of-binary-analysis-e29a3d75bd56
- https://github.com/WerWolv/ImHex
- [DynamoRIO](https://dynamorio.org/)
- https://www.duplichecker.com/hex-to-text.php
- [ASCII](https://app.notion.com/p/ASCII-177c0f5171ec8048a38bfb7b0effc45f?pvs=21)
- Exploring Object File Formats ([maskray.me](http://maskray.me/))
[https://news.ycombinator.com/item?id=38998914](https://news.ycombinator.com/item?id=38998914)
- [binutils](https://www.gnu.org/software/binutils/)
- [GNU Binutils: the ELF Swiss Army Knife](https://interrupt.memfault.com/blog/gnu-binutils)
