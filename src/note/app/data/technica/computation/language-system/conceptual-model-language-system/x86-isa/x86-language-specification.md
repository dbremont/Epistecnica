# x86: 📜 Language Specification

> The x86 ISA 📜 is a formal **instruction language specification** defining the syntax, semantics, operand types, encoding rules, control-flow constructs, memory and I/O models, and exception behavior that collectively constitute the **executable language of x86 processors**.
> 

## Lexical Grammar

> aka. Lexical Structure,
> 

> 🔤 **Lexical grammar defines the *tokens***—the smallest meaningful units in the source code.
> 

> **Lexical structure**: Defines how characters combine into **tokens** (identifiers, keywords, literals) and handles **whitespace, comments, and delimiters**.
> 

Guiding Questions:

- [Token Space] How are tokens (keywords, identifiers, literals) defined?
- What characters are allowed in identifiers (e.g., Unicode, sigils like `$`)?
- Does the language use significant whitespace (e.g., Python) or explicit delimiters (e.g., C)?
- What are the core language constructs (variables, functions, control flow)?
- *Does the Language Supports Macro Constructs?*

| **Lexical Construct** | **Description** | **Case(s)** |
| --- | --- | --- |
| **Identifiers** | Register names (`EAX`, `RAX`), labels, macro symbols | Case-insensitive (`EAX` ≡ `eax`) |
| **Literals** | Numeric constants, character constants | `0xFF`, `123`, `'A'` |
| **Keywords / Mnemonics** | Instruction names (`MOV`, `ADD`, `JMP`) | Case-insensitive |
| **Delimiters** | `,`, `[ ]`, `:` | Separate operands, address expressions, labels |
| **Comments** | Line (`;`) or block comments (if assembler supports) | Ignored by assembler |
| **Whitespace** | Spaces, tabs, newlines | Used to separate tokens |

## **Syntactic** Grammar

> aka. The Grammar.
> 

> 📚 The **syntactic grammar defines how tokens are combined** into valid **expressions**, **statements**, **declarations**, and **programs**.
> 

Guiding Questions:

- What class of formal grammar best describes the grammar of this language? (Note: This may include grammars within or outside the Chomsky hierarchy.)
- Are there syntactic ambiguities in the Language?
- What *statement forms* exist (e.g., loops, conditionals, jumps)?
- What *expression forms* are supported (e.g., arithmetic, lambdas, comprehensions)?
- How are *operator precedence* and *associativity* formally defined?

## Syntactical Structure

> **Syntactical Construct**: A **language feature** (e.g., loops, functions, conditionals) defined by the grammar, forming the structure of valid programs.
> 

> Literal:  In programming and computer science, a **literal** is a **notation for representing a fixed value directly in the source code**. It’s the actual value written in the code, not a variable or an expression that computes a value.
> 

> **Linguistic Abstractions:**  Set of abstraction building in the syntax of the language.
> 

> Note: This should be improved.
> 

Guiding Questions:

- What are the core language constructs (variables, functions, control flow)?
- *Does the Language Supports Macro Constructs?*
- What *statement forms* exist (e.g., loops, conditionals, jumps)?
- What *expression forms* are supported (e.g., arithmetic, lambdas, comprehensions)?
- How are *operator precedence* and *associativity* formally defined?

| **Abstraction** | **Description** | **Purpose** | **Case(s)** |
| --- | --- | --- | --- |
| **Instruction** | Atomic language statement | Represents a **single machine operation** | `MOV EAX, EBX` |
| **Label** | Named position in code | Reference target for jumps/calls | `loop_start:` |
| **Macro** | Parameterized instruction template | Reduces repetition, adds symbolic abstraction | `MACRO PUSHALL ... ENDM` |
| **Directive** | Assembler instructions affecting compilation | Control section, alignment, data allocation | `.data`, `.text` |
| **Expression** | Arithmetic/logic computations | Operand calculation | `[EBX+4*ECX+8]` |
| **Segment Definition** | Memory section | Organize code/data | `.code`, `.data`, `.bss` |

### Instruction Set

> System instructions:  …
> 

| **Category** | **Mnemonic** | **Description** |
| --- | --- | --- |
| **Data Transfer** | `MOV` | Move data from source to destination |
|  | `PUSH` / `POP` | Push/pop value to/from stack |
|  | `LEA` | Load effective address |
|  | `XCHG` | Exchange two operands |
|  | `PUSHF` / `POPF` | Push/pop flags register |
| **Arithmetic** | `ADD` / `SUB` | Add / Subtract |
|  | `MUL` / `IMUL` | Unsigned / Signed multiply |
|  | `DIV` / `IDIV` | Unsigned / Signed divide |
|  | `INC` / `DEC` | Increment / Decrement |
|  | `NEG` | Negate operand |
|  | `ADC` / `SBB` | Add with carry / Subtract with borrow |
|  | `CMP` | Compare two operands |
| **Bitwise & Logical** | `AND` / `OR` / `XOR` | Bitwise operations |
|  | `NOT` | Bitwise NOT |
|  | `TEST` | Bitwise AND (sets flags only) |
| **Shift & Rotate** | `SHL` / `SAL` | Shift left (logical/arithmetic) |
|  | `SHR` / `SAR` | Shift right (logical/arithmetic) |
|  | `ROL` / `ROR` | Rotate left / right |
|  | `RCL` / `RCR` | Rotate left / right through carry |
| **Control Flow** | `JMP` | Unconditional jump |
|  | `JE` / `JZ` | Jump if equal/zero |
|  | `JNE` / `JNZ` | Jump if not equal/not zero |
|  | `JG` / `JL` | Jump if greater / less |
|  | `JA` / `JB` | Jump if above / below (unsigned) |
|  | `JC` / `JNC` | Jump if carry / not carry |
|  | `JO` / `JNO` | Jump if overflow / not overflow |
|  | `CALL` / `RET` | Call and return from procedure |
|  | `LOOP` | Loop with CX counter |
| **String Manipulation** | `MOVS` | Move string |
|  | `LODS` | Load string |
|  | `STOS` | Store string |
|  | `SCAS` | Scan string |
|  | `CMPS` | Compare strings |
| **Stack Operations** | `PUSHA` / `POPA` | Push/pop all general-purpose registers |
|  | `PUSHF` / `POPF` | Push/pop flags register |
| **Processor Control** | `STC` / `CLC` / `CMC` | Set, clear, complement carry flag |
|  | `STD` / `CLD` | Set/clear direction flag |
|  | `STI` / `CLI` | Enable/disable interrupts |
|  | `HLT` | Halt processor |
|  | `NOP` | No operation |
| **Floating Point (x87 FPU)** | `FADD` / `FSUB` | Floating-point add/subtract |
|  | `FMUL` / `FDIV` | Floating-point multiply/divide |
|  | `FLD` / `FST` | Load/store floating-point number |
|  | `FABS` | Absolute value |
|  | `FSQRT` | Square root |
| **SIMD (MMX/SSE/AVX)** | `PADDW` | Packed add words |
|  | `PMULHUW` | Packed multiply high unsigned words |
|  | `MOVDQA` / `MOVDQU` | Move aligned / unaligned packed data |
|  | `ADDSD` / `MULPD` | Add / Multiply scalar packed double-precision |
|  | `VMOVAPS` | Move aligned packed single-precision (AVX) |

### Instruction Encoding

![…](../assets/note/technica/computation/language-system/conceptual-model-language-system/x86-isa/x86-language-specification/image.png)

…

```
[ Prefix (optional) ] [ Opcode ] [ ModR/M (optional) ] [ SIB (optional) ] [ Displacement (optional) ] [ Immediate (optional) ]
```

| **Field** | **Size** | **Description** |
| --- | --- | --- |
| **Prefix** | 1–4 bytes | Modifies behavior (e.g., segment override, operand size, address size, etc.) |
| **Opcode** | 1–3 bytes | Specifies the operation (e.g., `MOV`, `ADD`, `JMP`) |
| **ModR/M** | 1 byte (optional) | Defines the addressing mode (register or memory) and the operand |
| **SIB** | 1 byte (optional) | Used for scaled-index addressing (only if ModR/M specifies it) |
| **Displacement** | 1–4 bytes (optional) | Memory address offset |
| **Immediate** | 1–4 bytes (optional) | Constant value used in operation |

### Addressing Mode(s)

> 
- **Immediate**: A constant value specified in the instruction itself.
- **Direct**: A direct address to the operand in memory.
- **Indirect**: A register that holds the address of the operand.
- **Indexed**: Combines a base register and an offset.
- **Base-Register Plus Index**: Combines a base register, index register, and an optional scale factor.

## Language Semantics

Guiding Questions

- **What formal or informal semantic model describes the language's execution?** (e.g., operational, axiomatic, denotational semantics)
- **How does the language define and enforce correctness?** (e.g., static type checking, contracts, runtime assertions)
- **What are the rules for function calls and argument passing?** (e.g., pass-by-value, pass-by-reference, copy-on-write, closures)
- **What memory model does the language enforce?** (e.g., stack allocation, heap management, reference counting)
- **How does the language handle undefined behavior or execution anomalies?** (e.g., segmentation faults, runtime errors, exception handling)
- **What guarantees does the language provide regarding execution determinism or non-determinism?**
- **What constraints exist on execution order, and how does this affect parallel computation?**

Semantics:

- **Execution Model**: Operational semantics (instructions map to CPU micro-operations affecting state).
- **Correctness Enforcement**: Determined by CPU rules; some static checking via assembler.
- **Function Calls**: Stack-based call/return semantics, with argument passing via registers or stack.
- **Memory Model**: Linear or virtual memory; segment overrides possible; read/write ordering defined by CPU architecture.
- **Undefined Behavior**: Accessing invalid memory, illegal opcode → exception/fault.
- **Determinism**: Sequential instructions are deterministic; parallel execution may involve cache coherency and memory ordering issues.

## Binding

> **Binding**: Associates **names** (variables, functions) with **memory locations, values, or behaviors**, either at compile-time or runtime.
> 

> **Mutability:  Mutability** refers to the ability of an object or variable to be modified after it is created or assigned a value.
> 

Guiding Questions:

- How are *values bound to names* (e.g., `let` in Rust, `=` in Python)?
- Which binding semantics does the language provides (mutable binding, inmutable binding)
- What categories of values and identifiable constructs does the language support?

### Identifiable Constructs

| **Identifier Type** | **Description** |
| --- | --- |
| **Variable Names** | Labels for data memory locations |
| **Function Names** | Labels for callable code sections |
| **Struct / Data Segment Names** | Named memory blocks |
| **Macro Names** | Parameterized code templates |
| **Register Names** | Architectural CPU registers |
| **Instruction Mnemonics** | Fixed semantic operations |

### Binding Type

> **Binding Type** refers to the method by which a variable or identifier is associated with a value, address, or resource, determining its scope, lifetime, and mutability in a program.
> 

| **Binding Type** | **Description** |
| --- | --- |
| **Static Binding** | Most labels and registers resolved at assembly time. |
| **Dynamic Binding** | Runtime binding for memory addresses via stack/frame pointer offsets. |
| **Lexical Binding** | Local label visibility within section/block. |
| **Global Binding** | Symbols accessible across modules. |
| **Local Binding** | Labels and variables confined to a function/segment. |

## Scoping Rules

> **Note:** Visibility and scoping rules are synonymous.
> 

> **Visibility**: **Visibility** refers to the scope or access control of an identifier (such as a variable, function, or class) within a program, determining where and how it can be referenced or modified, often enforced by rules such as access modifiers or name resolution mechanisms.
> 

> **Scoping Rules**: Determine **where and when** a binding is accessible (e.g., `block scope`, `function scope`, `global scope`).
> 

Guiding Questions:

- What is the *scope* of a name (lexical vs. dynamic, block vs. function)?
- How are shadowing, closures, and hoisting handled?
- Which are the  visibility rules associated with a binding?

Rules:

- **Visibility**: Labels and variables follow section-level or module-level scope.
- **Lexical Scope**: Determined by position in source file; local labels visible until end of section.
- **Global Scope**: Exported symbols visible across object modules.
- **Shadowing**: Local labels may override global labels within a block.
- **Closures / Hoisting**: Not applicable in x86 assembly.

## References

- [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md)
- [GDB (GNU Project Debugger)](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/gdb-gnu-project-debugger.md)
- https://en.wikibooks.org/wiki/X86_Disassembly