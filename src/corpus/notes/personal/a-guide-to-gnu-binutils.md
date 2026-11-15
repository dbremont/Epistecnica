---
tags: [note, guia, tooling]
---

# A Guide To GNU Binutils


Here’s a table summarizing the GNU Binutils tools:

| **Tool** | **Description** |
| --- | --- |
| **`as` (Assembler)** | Converts assembly language code into machine code. |
| **`ld` (Linker)** | Combines object files into a single executable or library. |
| **`objdump`** | Displays information about object files, including headers, sections, and symbols. |
| **`nm`** | Lists symbols from object files, libraries, and executables. |
| **`strip`** | Removes symbols and debugging information from object files, reducing their size. |
| **`ar`** | Creates, modifies, and extracts from archives (typically used for static libraries). |
| **`ranlib`** | Generates an index to the symbols in an archive, typically used with `ar` to improve linking performance. |
| **`size`** | Displays the sizes of sections within object files. |
| **`objcopy`** | Copies and translates object files, can be used to convert between different formats or strip information. |
| **`readelf`** | Displays information about ELF (Executable and Linkable Format) files, such as headers and sections. |
| **`addr2line`** | Converts addresses into file names and line numbers, useful for debugging. |
| **`c++filt`** | Demangles C++ symbol names to make them readable. |
| **`objdump`** | Displays detailed information about object files, such as disassembly, headers, and sections. |
| **`ld.gold`** | An alternative linker with a focus on faster linking times compared to the default `ld`. |
| **`bfd`** | The Binary File Descriptor library used internally by many GNU Binutils tools for reading and writing object files. |
| **elfedit** |  Allows alteration of ELF format files. |
| string | Lists printable strings from files. |
| strip | Discards symbols. |
| size | Lists the section sizes of an object or archive file. |
| addr2line | Converts addresses into filenames and line numbers. |

This table provides an overview of the primary tools included in GNU Binutils, each serving a specific role in the development and management of binary and object files.

## References

- https://www.gnu.org/software/binutils/
