---
tags: [code-representation, intermediate-representation]
---

# ELF (Executable and Linkable Format)

- [C++](note.html?n=technica/computation/language-system/conceptual-model-language-system/c-2.md)

> An **ELF** (Executable and Linkable Format) file is a common standard file format for executables, object code, shared libraries, and core dumps in computing systems.
> 

> An **ELF (Executable and Linkable Format)** file is a standard binary format used for executables, object code, shared libraries, and core dumps in Unix-like operating systems (e.g., Linux). It is flexible and supports different architectures (x86, ARM, etc.) and platforms.
> 

QA:

- How an ELF file is structure?
- What is the meaning of a stripped elf file?
- How to edit binary files? [A Guide to Binary Tools](https://app.notion.com/p/A-Guide-to-Binary-Tools-e44641d2394b46cf9e95a57fb6bc176b?pvs=21)
- Which are the **linking methods of an elf file**?  See here [ld](note.html?n=technica/computation/language-system/conceptual-model-language-system/ld.md).
- How is the ELF file read and executed?

## Terminology

| **Term** | **Definition** |
| --- | --- |
| **ELF (Executable and Linkable Format)** | Standard binary file format for executables, object files, shared libraries, and core dumps on Unix-like systems. |
| **ELF Header** | The first part of the ELF file; contains metadata describing the file type, target architecture, entry point, and offsets to other tables. |
| **Program Header Table (Segments)** | Table describing **segments**; used by the loader to map parts of the file into memory at runtime. |
| **Section Header Table (Sections)** | Table describing **sections**; used by linkers and compilers to organize code, data, and metadata. |
| **Segment (Program Header)** | A contiguous memory region for runtime loading; may contain multiple sections and defines permissions (R/W/X). |
| **Section** | A logical grouping of code, data, or metadata for linking and compilation; typically one type of data per section. |
| **.text** | Section containing executable code. |
| **.data** | Section containing initialized global/static variables. |
| **.bss** | Section containing uninitialized global/static variables (zero-initialized at runtime). |
| **.rodata** | Section containing read-only constants and string literals. |
| **.plt (Procedure Linkage Table)** | Section used in dynamic linking; holds stub functions for external function calls. |
| **.got (Global Offset Table)** | Section used in dynamic linking to store addresses of global variables and functions. |
| **.dynsym** | Section containing dynamic symbols for runtime linking. |
| **.symtab** | Section containing all symbols for linking. |
| **.strtab** | Section storing strings used by the symbol table. |
| **.shstrtab** | Section storing section names as strings. |
| **Entry Point** | Address in memory where execution begins (`e_entry` in ELF header). |
| **PT_LOAD** | Segment type indicating a loadable segment. |
| **PT_DYNAMIC** | Segment type containing dynamic linking information. |
| **PT_INTERP** | Segment type pointing to the program interpreter (e.g., `/lib/ld-linux.so`). |
| **PT_NOTE** | Segment type containing notes for the OS or debugger. |
| **Relocation Table** | Section containing instructions to patch addresses during linking or loading. |
| **Alignment** | Memory or file offset constraints for sections or segments. |
| **Flags** | Attributes specifying access permissions (read/write/execute) or properties of sections/segments. |

## **File Structure**

> 

![image.png](../assets/note/technica/computation/language-system/conceptual-model-language-system/elf-executable-and-linkable-format/image.png)

### **ELF Header**

> **ELF Header (`Elf64_Ehdr` / `Elf32_Ehdr`).**
> 
- Located at the start of the file.
- Describes the file's structure (32-bit or 64-bit), endianness, target architecture, and entry point.
- Points to the **Program Header Table** and **Section Header Table**.

```c
#define EI_NIDENT 16

typedef struct {
    unsigned char e_ident[EI_NIDENT];  // Magic number (0x7F 'E' 'L' 'F')
    Elf64_Half    e_type;             // ET_EXEC, ET_DYN, ET_REL
    Elf64_Half    e_machine;          // EM_X86_64, EM_ARM, etc.
    Elf64_Word    e_version;          // EV_CURRENT
    Elf64_Addr    e_entry;            // Entry point address
    Elf64_Off     e_phoff;            // Program header table offset
    Elf64_Off     e_shoff;            // Section header table offset
    Elf64_Word    e_flags;            // Architecture-specific flags
    Elf64_Half    e_ehsize;           // ELF header size
    Elf64_Half    e_phentsize;        // Size of a program header entry
    Elf64_Half    e_phnum;            // Number of program headers
    Elf64_Half    e_shentsize;        // Size of a section header entry
    Elf64_Half    e_shnum;            // Number of section headers
    Elf64_Half    e_shstrndx;         // Index of .shstrtab section
} Elf64_Ehdr;

```

### **Program Header Table (for executables & shared libraries)**

> **Program Headers (`Elf64_Phdr`)**
> 
- Defines **segments** (used at runtime by the OS for loading the program into memory).
- Each entry (`Elf32_Phdr` or `Elf64_Phdr`) describes a segment (e.g., `PT_LOAD`, `PT_DYNAMIC`).

```c
typedef struct {
    Elf64_Word  p_type;    // PT_LOAD, PT_DYNAMIC, PT_INTERP
    Elf64_Word  p_flags;   // PF_R, PF_W, PF_X (read, write, execute)
    Elf64_Off   p_offset;  // File offset of segment
    Elf64_Addr  p_vaddr;   // Virtual address in memory
    Elf64_Addr  p_paddr;   // Physical address (unused)
    Elf64_Xword p_filesz;  // Size in file
    Elf64_Xword p_memsz;   // Size in memory
    Elf64_Xword p_align;   // Alignment
} Elf64_Phdr;

```

### **Section Header Table (for linking & debugging)**

> **Section Headers (`Elf64_Shdr`)**
> 
- Defines **sections** (used by the linker and debugger).
- Each entry (`Elf32_Shdr` or `Elf64_Shdr`) describes a section (e.g., `.text`, `.data`, `.rodata`).

```c
typedef struct {
    Elf64_Word  sh_name;      // Index into .shstrtab
    Elf64_Word  sh_type;      // SHT_PROGBITS, SHT_NOBITS, etc.
    Elf64_Xword sh_flags;     // SHF_WRITE, SHF_ALLOC, etc.
    Elf64_Addr  sh_addr;      // Load address in memory
    Elf64_Off   sh_offset;    // File offset
    Elf64_Xword sh_size;      // Section size
    Elf64_Word  sh_link;      // Link to another section
    Elf64_Word  sh_info;      // Additional info
    Elf64_Xword sh_addralign; // Alignment
    Elf64_Xword sh_entsize;   // Entry size (if table)
} Elf64_Shdr;

```

### **Segments (runtime memory mapping)**

- Segments (`LOAD`, `DYNAMIC`, `INTERP`) group sections for execution.
- The OS loads segments into memory (not sections).

### **Sections (contain actual data)**

- **`.text`** – Executable machine code.
- **`.data`** – Initialized global/static variables.
- **`.rodata`** – Read-only data (constants).
- **`.bss`** – Uninitialized data (zero-filled at runtime).
- **`.symtab`** – Symbol table (function/variable names).
- **`.strtab`** – String table (for symbol names).
- **`.dynamic`** – Dynamic linking info.
- **`.shstrtab`** – Section name strings.
- **`.rel.*`** – Relocation entries.

## **File Type(s)**

| Type (`e_type`) | Description |
| --- | --- |
| `ET_REL` | Relocatable object file (`.o`) |
| `ET_EXEC` | Executable file (`/bin/ls`) |
| `ET_DYN` | Shared library (`.so`) or PIE executable |
| `ET_CORE` | Core dump file |

## Loading

> Linux Implementation
> 

| Component | Location | Purpose |
| --- | --- | --- |
| Syscalls | `execve`, `execveat` | Trigger program loading |
| Exec core | `fs/exec.c` | Common exec logic |
| ELF loader | `fs/binfmt_elf.c` | Reads & loads ELF binaries |
| Memory mapping | `mm/mmap.c` | Maps segments into memory |
| Interpreter loading | `fs/binfmt_elf.c` | Loads dynamic loader (`ld.so`) |

## Linking

> 

## **Viewing ELF Files**

```bash
# readelf – Display ELF file details:
readelf -h <file>      # Show ELF header
readelf -l <file>      # Show program headers (segments)
readelf -S <file>      # Show section headers
readelf -s <file>      # Show symbol table

```

```bash
# objdump – Disassemble sections:
objdump -d <file>      # Disassemble .text
objdump -x <file>      # Show all headers

```

```bash
# nm – List symbols:
nm <file>              # Show symbols

```

## References

- [The 101 of ELF files on Linux: Understanding and Analysis](https://linux-audit.com/elf-binaries-on-linux-understanding-and-analysis/)
- [How to find the main function’s entry point of elf executable file without any symbolic information?](https://stackoverflow.com/questions/9885545/how-to-find-the-main-functions-entry-point-of-elf-executable-file-without-any-s)
- [How a CPU works: Bare metal C on my RISC-V toy CPU](https://florian.noeding.com/posts/risc-v-toy-cpu/cpu-from-scratch/)
- Performance:
    - [Tools and Reference Code for Intel Optimizations (eg Large Pages)](https://github.com/intel/iodlr)
    - [Performance Benefits of Using Huge Pages for Code](https://easyperf.net/blog/2022/09/01/Utilizing-Huge-Pages-For-Code)
- [The 101 of ELF files on Linux: Understanding and Analysis](https://linux-audit.com/elf-binaries-on-linux-understanding-and-analysis/)
- [A minimal, complete, and correct ELF file](https://scratchpad.avikdas.com/elf-explanation/elf-explanation.html)
- [Address space layout randomization](https://www.wikiwand.com/en/Address_space_layout_randomization)
- [What is the difference between a .so and a .lo file?](https://stackoverflow.com/questions/18508510/what-is-the-difference-between-a-so-and-a-lo-file)
- https://www.wikiwand.com/en/Executable_and_Linkable_Format
- [A Guide to Binary Tools](https://app.notion.com/p/A-Guide-to-Binary-Tools-e44641d2394b46cf9e95a57fb6bc176b?pvs=21)
- https://news.ycombinator.com/item?id=40486068
- [‣](https://app.notion.com/p/1c4598edb79080769f99fdb0a357323c?pvs=21)
- [‣](https://app.notion.com/p/1c4598edb79080c3b889c2dc11f6a5b0?pvs=21)
- [PIE: Position-independent executable](https://www.wikiwand.com/en/Position-independent_executable)
- [Address space layout randomization](https://www.wikiwand.com/en/Address_space_layout_randomization)
- [Position independent code](https://isopenbsdsecu.re/mitigations/pie/)
- How can I tell, with something like objdump, if an object file has been built with -fPIC? https://stackoverflow.com/questions/1340402/how-can-i-tell-with-something-like-objdump-if-an-object-file-has-been-built-wi
- [How to find the main function’s entry point of elf executable file without any symbolic information?](https://stackoverflow.com/questions/9885545/how-to-find-the-main-functions-entry-point-of-elf-executable-file-without-any-s)
- https://lwn.net/Articles/631631/
- https://cpu.land/becoming-an-elf-lord