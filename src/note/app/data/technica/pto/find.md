# find

> `find` is a command-line filesystem traversal and selection utility. It takes one or more starting points, traverses the corresponding filesystem hierarchy, evaluates an expression against each encountered filesystem object, and optionally performs an action on objects for which the expression evaluates to true.

>
> Conceptually, `find` exposes a small query-and-action language over the filesystem: **traversal domain → predicates → Boolean composition → actions**. Its interface therefore combines mechanisms that, in other systems, might be separated into a tree walker, metadata query API, expression language, and command executor.

>
> The exact capability set is implementation-dependent. The POSIX `find` utility defines a portable core, while GNU `findutils`, FreeBSD, and other UNIX implementations extend that core with additional predicates, traversal controls, actions, and formatting facilities.

## Formulation

### What type of technical element is find?

> find is a technical production object: a software object produced to provide a particular operational capability over a technical substrate—in this case, the filesystem.

> Traverse a filesystem hierarchy → evaluate predicates on filesystem objects → perform actions on the objects that satisfy the predicates.

```text
Technical Production Object
└── find
    ├── Production purpose
    │   └── Locate/select filesystem objects
    │
    ├── Operational mechanism
    │   ├── filesystem traversal
    │   ├── predicate evaluation
    │   └── action execution
    │
    ├── Capability set
    │   ├── traversal
    │   ├── filtering/selection
    │   ├── metadata evaluation
    │   ├── expression composition
    │   └── actions on selected objects
    │
    └── Interface
        └── command-line expression
```

### Which are the capabilities set?

| Capability category      | Capability Set                                                                            |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| **Traversal**            | Recursively traverse directory hierarchies                                                |
| **Scope restriction**    | Specify starting paths; restrict traversal depth                                          |
| **Selection**            | Select objects by name, path, type, permissions, ownership, size, timestamps, links, etc. |
| **Boolean composition**  | Combine predicates with AND, OR, NOT, grouping                                            |
| **Pattern matching**     | Glob-style name/path matching                                                             |
| **Metadata inspection**  | Evaluate filesystem metadata                                                              |
| **Time-based selection** | Select by modification/access/change time                                                 |
| **Type selection**       | Files, directories, symbolic links, sockets, devices, etc.                                |
| **Action**               | Print, delete, execute commands, modify attributes, etc.                                  |
| **Result formatting**    | Control how selected paths are emitted                                                    |
| **Traversal control**    | Follow or avoid symbolic links; control descent and ordering                              |
| **Optimization**         | Predicate ordering and filesystem traversal optimizations                                 |

### What is the formal model of find?

GNU `find` is a **deterministic, single-threaded, depth-first filesystem graph traversal engine** that:

1. Constructs an **Abstract Syntax Tree (AST)** from a command-line–specified predicate language.
2. Iteratively enumerates directory entries via POSIX-compliant system calls (`opendir`, `readdir`, `stat`, `lstat`, `fts_read` depending on build).
3. Evaluates each inode against the compiled predicate tree using **short-circuit boolean semantics**.
4. Dispatches side-effect actions when the predicate resolves to true.
5. Maintains traversal and evaluation state under resource constraints imposed by the host OS (e.g., `ARG_MAX`, file descriptor limits).

Formally, it is:

* A **filesystem graph enumerator**
* Coupled with a **cost-optimized predicate execution planner**
* Augmented by an **action dispatch subsystem**
* Operating over a **POSIX VFS abstraction layer**

It can be modeled as a state machine:

$S_{t+1} = T_{\text{find}}(S_t, d_t, m_t, E)$

Where:

* $S_t$ = traversal stack + AST evaluation cursor + execution context
* $d_t$ = directory entry yielded at step $t$
* $m_t$ = metadata retrieved from kernel (stat buffer)
* $E$ = external environment (filesystem topology, permissions, mount graph, resource limits)
* $T_{\text{find}}$ = evaluation + dispatch operator

At its core, GNU `find` is not merely a search tool; it is a **stream-processing engine over a dynamically discovered inode graph**, with embedded logical and procedural semantics.

## Signature

> A comprehensive list of aspects to cover in order to understand a topic.

> A tool is a teleologically organized causal architecture whose internal mechanisms generate environment-coupled state transformations under structured triggering regimes.

| Aspect                       | Description                                                                                                                                                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nucleus (Deepest Essence)** | A recursive filesystem graph walker + boolean expression evaluator + action executor.                                                                                                                                |
| **Telos (Intent)**            | To select filesystem objects based on metadata predicates and optionally trigger side effects (print, delete, exec).                                                                                                 |
| **Gnosis (Understanding)**    | Build a mental model in three layers: (1) directory tree as a rooted graph, (2) expression as short-circuit boolean program, (3) actions as terminal operators. Understand precedence, lazy evaluation, and pruning. |
| **Relatio (Connections)**     | Complements `xargs`, `grep`, `stat`, `chmod`, `rm`, `tar`, and shell pipelines in Unix-like systems (e.g., Linux environments).                                                                                      |
| **Idoneitas (Suitability)**   | Highly expressive for metadata-driven filtering; scales well with large trees; precise selection semantics.                                                                                                          |
| **Limites (Limits)**          | Performance on huge trees without pruning; unsafe deletion if mis-specified; complex quoting; portability differences between GNU and BSD variants.                                                                  |
| **Dynamis (Evolution)**       | Integration with `-printf`, improved performance heuristics, possible parallel traversal (not native), integration with modern filesystems.                                                                          |
| **Critica (Critique)**        | Syntax complexity; surprising precedence rules; danger of destructive actions; differences across implementations.                                                                                                    |

## Structure

### What is the internal structure of this technical object?

- **Traversal Engine**: The Traversal Engine recursively descends the filesystem hierarchy using low-level system calls to retrieve inode metadata, implementing handling for mount boundaries, symbolic link cycles, and leaf-optimization techniques to minimize unnecessary `stat` calls.
- **Expression Parser & Evaluator**: The Expression Parser transforms the command-line arguments into an Abstract Syntax Tree (AST) that the Evaluator processes using short-circuit logic to determine the truth value of each file against the user's criteria.
- **Optimizer**: The Optimizer analyzes the parsed expression tree to reorder predicates based on estimated cost—prioritizing cheap tests like `-name` over expensive operations like `-exec`—before the traversal begins.
- **Action Dispatcher**: The Action Dispatcher executes specific side-effects, such as formatting output strings or spawning child processes for `-exec`, whenever a file successfully matches the evaluation criteria.

## Dynamics

### (Induced Dynamics) What types of dynamics are induced by the technical object? Which are the types of dynamics that can be trigger? What kinds of state-transformation processes can be triggered?

The **primary induced dynamic** is a **systematic, synchronous filesystem traversal** that transforms the latent, static topology of the directory graph into a linear stream of file entities. This dynamic is not merely a reading process; it is a **filtering cascade** where the flow of file metadata is successively narrowed by the predicate tree, creating a "survival of the fittest" dynamic where only compliant inodes persist to the action stage.

**Triggerable State-Transformation Processes:**

* **Informational Transformation:** Conversion of raw inode metadata (`stat` buffers) into formatted human-readable byte streams (stdout).
* **Mutating Transformation:** Alteration of the external filesystem state, such as shredding directory entries via `-delete` or modifying timestamps via `-exec touch {} \;`.
* **Process Spawning Dynamics:** The generation of new system processes (child threads/forks) to handle `-exec` actions, creating a temporary parallel execution context that forces the main traversal to pause (synchronization barrier).
* **Heuristic Reordering:** Internal dynamic optimization where the AST is restructured on-the-fly (or just prior to traversal) based on cost heuristics, transforming the logical evaluation order into a physical execution plan.

### (Conception of State) What is the most useful formal conception of “state” for analyzing this technical object? Which components of the state are external (i.e., environmental)?

The most useful formal conception of state for `find` is the **Evaluation Context Tuple**: $(C_{path}, M_{stat}, E_{cursor})$.

* **$C_{path}$ (Current Path):** The absolute or relative path string currently being resolved.
* **$M_{stat}$ (Metadata Buffer):** The `struct stat` buffer containing the inode data retrieved from the kernel; this is the "truth" against which predicates evaluate.
* **$E_{cursor}$ (Evaluation Cursor):** The specific position within the compiled Abstract Syntax Tree (AST) indicating which predicate is currently being resolved and the boolean result of the previous sibling.

**External (Environmental) State Components:**

* **Filesystem Topology:** The structural links between directories (parent/child relationships) which dictate the traversal path.
* **Inode State:** The metadata (permissions, timestamps, type) owned by the kernel, which the engine must query but cannot control.
* **System Resource Limits:** External constraints like `ARG_MAX` (limiting `-exec ... +` buffer size) and file descriptor limits (`ulimit -n`), which force the engine to change its internal buffering state.

### (Triggering) How are the dynamics trigger? Which triggers are user-initiated, system-initiated, or externally induced? Are triggers synchronous, asynchronous, event-driven, or continuous?

**How Dynamics are Triggered:**

The dynamics are triggered by a **Data-Driven Pull Mechanism**. The Traversal Engine initiates a loop calling `fts_read` (or `readdir`), which acts as the "heartbeat" of the process. Each successful return from these system calls triggers a new evaluation cycle.

**Types of Triggers:**

* **User-Initiated:** The invocation of the binary and the construction of the AST (Expression Parsing). This is the "setup" trigger.
* **System-Initiated (Synchronous):** The return of directory entries by the kernel. This is the "step" trigger. Errors (e.g., `EACCES` permission denied) are negative triggers that induce specific error-handling dynamics.
* **Logic-Induced (Internal):** The boolean result of a predicate. If `-type f` returns **True**, it triggers the evaluation of the next AST sibling; if **False**, it triggers a skip (short-circuit) dynamic, aborting the rest of the branch.

**Synchronicity:**

* **Synchronous and Blocking:** The entire operation is synchronous. The traversal blocks on I/O (disk reads) and blocks on CPU during predicate evaluation.
* **Event-Driven (File Discovery):** The engine is reactive to the "event" of discovering a file. It does not run on a timer; it runs strictly in response to filesystem enumeration events.

### (Interaction - Complementary) Which 'external elements' does the technical object require to 'induce dynamics'? Which elements are needed to trigger such dynamics?

**External Elements Required to Induce Dynamics:**

The technical object is essentially inert without a **complementary filesystem** (the "target object"). It requires a mounted filesystem hierarchy that supports the standard POSIX system calls (`stat`, `opendir`, `readdir`). Without this external topology to crawl, the engine has no substrate upon which to exert force.

**Elements Needed to Trigger Dynamics:**

* **System Call Interface (VFS):** The kernel's Virtual File System layer acts as the translation layer, triggering the internal logic by feeding it data structures (`dirent`, `stat`).
* **Process Table Capacity:** For `-exec` dynamics, the OS must have available slots in the process table to spawn child processes; if the process table is full, the dynamic (execution) fails, and the engine reports an error state.
* **Validated Arguments:** A syntactically valid and semantically actionable command line (e.g., a starting path that exists). If the starting point does not exist, the traversal dynamic is never triggered; the object immediately enters a halt state.

## Interface

> What is the interface to access the capabilities?

### Grammar

Canonical Interface Grammar:

```bash
## Grammar
find [option]  [starting-path...] [expression...]

expression
    → (test | action | operator | group)*

## Sentence
find /var/log -type f -name '*.log' -mtime -7 -print
```

Complete GNU grammar:

```ebnf
(* 1. Top-Level Command Structure *)
find_command = 'find', [ global_option ], { global_option },
               [ starting_point_list ], [ expression ] ;

(* 2. Starting Points (Paths) *)
starting_point_list = path, { path } ;
path                = string_literal ;

(* 3. Global Options (Pre-expression flags) *)
global_option       = ( '-H' | '-L' | '-P' )
                    | '-D', debug_flag
                    | '-O', optimization_level ;

debug_flag          = string_literal ; (* e.g., "help", "tree", "search" *)
optimization_level  = digit ;          (* 0, 1, 2, 3 *)

(* 4. Expression Structure (Operators, Tests, Actions) *)
(* Precedence is handled by the structure: NOT > AND > OR > List (Comma) *)

expression          = list_expression ;

list_expression     = or_expression, { ',', or_expression } ;

or_expression       = and_expression, { ( '-o' | '-or' ), and_expression } ;

and_expression      = not_expression, { [ '-a' | '-and' ], not_expression } ;
(* Note: Adjacent expressions are implicitly AND-ed, hence -a is optional *)

not_expression      = ( '!' | '-not' ), not_expression
                    | primary ;

(* 5. Primaries (Tests, Actions, and Positional Options) *)
primary             = '(' expression ')'
                    | positional_option
                    | test
                    | action ;

(* 6. Positional Options (Affect tests following them *)
positional_option   = '-daystart'
                    | '-follow'
                    | '-regextype', regex_type
                    | '-maxdepth', number
                    | '-mindepth', number
                    | '-mount'
                    | '-noleaf'
                    | '-xdev' ;

(* 7. Tests (Return True or False) *)
test                = ( '-name' | '-iname' ), pattern
                    | ( '-path' | '-ipath' ), pattern
                    | ( '-regex' | '-iregex' ), pattern
                    | '-type', file_type
                    | ( '-size' ), size_spec
                    | ( '-mtime' | '-atime' | '-ctime' ), time_spec
                    | ( '-user' | '-uid' ), user_spec
                    | ( '-group' | '-gid' ), group_spec
                    | '-perm', permission_spec
                    | '-empty'
                    | '-false'
                    | '-true'
                    | '-executable'
                    | '-readable'
                    | '-writable' ;

(* 8. Actions (Perform side effects) *)
action              = '-delete'
                    | '-print'
                    | '-print0'
                    | '-printf', format_string
                    | '-ls'
                    | '-fls', output_file
                    | '-fprint', output_file
                    | '-fprint0', output_file
                    | '-fprintf', output_file, format_string
                    | '-prune'
                    | '-quit'
                    | exec_action ;

(* 9. Exec Action Structure (Complex) *)
exec_action         = exec_command, exec_terminator ;

exec_command        = ( '-exec' | '-execdir' | '-ok' | '-okdir' ),
                      utility_name, [ argument_list ] ;

argument_list       = exec_argument, { exec_argument } ;
exec_argument       = string_literal ; (* May contain '{}' for substitution *)

(* Terminators: ';' usually requires shell escaping as \;, '+' creates a list *)
exec_terminator     = ';' | '+' ;

(* 10. Terminals and Primitive Types *)
string_literal      = ? any sequence of characters passed by the shell ? ;
number              = ? a sequence of digits [0-9]+ ? ;
digit               = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;

(* Specific arguments *)
file_type           = 'b' | 'c' | 'd' | 'p' | 'f' | 'l' | 's' | 'D' ;
pattern             = string_literal ; (* Glob pattern *)
regex_type          = string_literal ; (* e.g., "emacs", "posix-awk" *)
user_spec           = string_literal | number ;
group_spec          = string_literal | number ;
output_file         = path ;
format_string       = string_literal ;

(* Time/Size Specs (e.g., +5, -2, 10) *)
time_spec           = [ '+' | '-' ], number ;
size_spec           = [ '+' | '-' ], number, [ size_unit ] ;
size_unit           = 'b' | 'c' | 'w' | 'k' | 'M' | 'G' ;

(* Permissions can be symbolic or octal *)
permission_spec     = string_literal ;
```

Example:

```text
find
 ├── traversal domain: /var/log
 ├── predicates:
 │    ├── type = regular-file
 │    ├── name matches *.log
 │    └── modification-time < 7 days
 └── action:
      └── print pathname
```

### Option Set

| Category                  | Flag      | Description                                                      | Option set (If Any)                      |
| ------------------------- | ---------------------- | ---------------------------------------------------------------- | ---------------------------------------- |
| **Global**                | `-D DEBUG`             | Enable debug options (e.g. `help`, `tree`, `search`)             | Debug flag                               |
| **Global**                | `-O LEVEL`             | Set the optimization level                                       | `0`–`3`                                  |
| **Traversal**             | `-H`                   | Follow symbolic links specified as starting points               | —                                        |
| **Traversal**             | `-L`                   | Follow symbolic links during traversal                           | —                                        |
| **Traversal**             | `-P`                   | Never follow symbolic links; default                             | —                                        |
| **Traversal**             | `-depth`               | Process directory contents before the directory itself           | —                                        |
| **Traversal**             | `-maxdepth N`          | Limit traversal depth                                            | `N ∈ ℕ`                                  |
| **Traversal**             | `-mindepth N`          | Ignore objects above minimum depth                               | `N ∈ ℕ`                                  |
| **Traversal**             | `-xdev` / `-mount`     | Do not descend into other filesystems                            | —                                        |
| **Traversal**             | `-daystart`            | Measure times from the beginning of today rather than 24 hours ago | —                                      |
| **Traversal**             | `-follow`              | Deprecated synonym for `-L`                                      | —                                        |
| **Traversal**             | `-noleaf`              | Do not optimize for directories with a fixed link count          | —                                        |
| **Traversal**             | `-ignore_readdir_race` | Suppress certain directory-entry race errors                     | —                                        |
| **Name / Path Selection** | `-name PATTERN`        | Match basename                                                   | Shell-style pattern                      |
| **Name / Path Selection** | `-iname PATTERN`       | Case-insensitive basename match                                  | Shell-style pattern                      |
| **Name / Path Selection** | `-path PATTERN`        | Match complete pathname                                          | Shell-style pattern                      |
| **Name / Path Selection** | `-ipath PATTERN`       | Case-insensitive pathname match                                  | Shell-style pattern                      |
| **Name / Path Selection** | `-regex PATTERN`       | Match pathname against regular expression                        | Regular expression                       |
| **Name / Path Selection** | `-iregex PATTERN`      | Case-insensitive regular-expression match                        | Regular expression                       |
| **Name / Path Selection** | `-regextype TYPE`      | Set the regular-expression syntax for `-regex`/`-iregex`         | `emacs`, `posix-awk`, …                  |
| **Type Selection**        | `-type TYPE`           | Select by filesystem object type                                 | `b c d p f l s D`*                       |
| **Type Selection**        | `-xtype TYPE`          | Select by type after symbolic-link resolution                    | `b c d p f l s D`*                       |
| **Size Selection**        | `-size N`              | Select by file size                                              | Numeric value + unit + comparison prefix |
| **Time Selection**        | `-mtime N`             | Select by modification age in days                               | `+N`, `N`, `-N`                          |
| **Time Selection**        | `-atime N`             | Select by access age in days                                     | `+N`, `N`, `-N`                          |
| **Time Selection**        | `-ctime N`             | Select by status-change age in days                              | `+N`, `N`, `-N`                          |
| **Time Selection**        | `-mmin N`              | Select by modification age in minutes                            | `+N`, `N`, `-N`                          |
| **Time Selection**        | `-amin N`              | Select by access age in minutes                                  | `+N`, `N`, `-N`                          |
| **Time Selection**        | `-cmin N`              | Select by status-change age in minutes                           | `+N`, `N`, `-N`                          |
| **Ownership**             | `-user USER`           | Select by username                                               | User name                                |
| **Ownership**             | `-group GROUP`         | Select by group name                                             | Group name                               |
| **Ownership**             | `-uid N`               | Select by numeric user ID                                        | `N ∈ ℕ`                                  |
| **Ownership**             | `-gid N`               | Select by numeric group ID                                       | `N ∈ ℕ`                                  |
| **Permissions**           | `-perm MODE`           | Select by permission bits                                        | Permission mode                          |
| **Links**                 | `-links N`             | Select by hard-link count                                        | `+N`, `N`, `-N`                          |
| **Filesystem**            | `-fstype TYPE`         | Select by filesystem type                                        | Filesystem type                          |
| **Filesystem**            | `-inum N`              | Select by inode number                                           | `N ∈ ℕ`                                  |
| **Filesystem**            | `-samefile FILE`       | Select objects referring to same inode                           | Pathname                                 |
| **Content / Attributes**  | `-empty`               | Select empty files/directories                                   | —                                        |
| **Content / Attributes**  | `-readable`            | Select objects readable by current user                          | —                                        |
| **Content / Attributes**  | `-writable`            | Select objects writable by current user                          | —                                        |
| **Content / Attributes**  | `-executable`          | Select executable/searchable objects                             | —                                        |
| **Content / Attributes**  | `-true`                | Always true                                                      | —                                        |
| **Content / Attributes**  | `-false`               | Always false                                                     | —                                        |
| **Boolean Composition**   | `-a` / `-and`          | Logical conjunction                                              | —                                        |
| **Boolean Composition**   | `-o` / `-or`           | Logical disjunction                                              | —                                        |
| **Boolean Composition**   | `!` / `-not`           | Logical negation                                                 | Expression                               |
| **Boolean Composition**   | `\( EXPRESSION \)`     | Group expression                                                 | Expression                               |
| **Actions**               | `-print`               | Print pathname                                                   | —                                        |
| **Actions**               | `-print0`              | Print pathname terminated by NUL                                 | —                                        |
| **Actions**               | `-printf FORMAT`       | Produce formatted output                                         | Format string                            |
| **Actions**               | `-fls FILE`            | Write `ls`-style information to a file                           | Output file                              |
| **Actions**               | `-fprint FILE`         | Write pathname to a file                                         | Output file                              |
| **Actions**               | `-fprint0 FILE`        | Write NUL-terminated pathnames to a file                         | Output file                              |
| **Actions**               | `-fprintf FILE FORMAT` | Write formatted output to a file                                 | Output file + format string              |
| **Actions**               | `-ls`                  | Display `ls`-style information                                   | —                                        |
| **Actions**               | `-delete`              | Delete selected objects                                          | —                                        |
| **Actions**               | `-prune`               | Do not descend into the current directory                        | —                                        |
| **Actions**               | `-exec COMMAND {} \;`  | Execute command once per match                                   | Command + arguments                      |
| **Actions**               | `-exec COMMAND {} +`   | Execute command with batches of matches                          | Command + arguments                      |
| **Actions**               | `-execdir COMMAND {} \;` | Execute command from the object's directory                    | Command + arguments                      |
| **Actions**               | `-ok COMMAND {} \;`    | Execute command with interactive confirmation                    | Command + arguments                      |
| **Actions**               | `-okdir COMMAND {} \;` | Execute command from the object's directory, with confirmation   | Command + arguments                      |
| **Actions**               | `-quit`                | Terminate traversal                                              | —                                        |
| **Reference Comparison**  | `-newer FILE`          | Select objects newer than reference file                         | Pathname                                 |
| **Reference Comparison**  | `-newermt DATE`        | Select objects newer than specified timestamp                    | Date/time expression                     |
| **Reference Comparison**  | `-anewer FILE`         | Select objects accessed more recently than reference             | Pathname                                 |
| **Reference Comparison**  | `-cnewer FILE`         | Select objects whose status changed more recently than reference | Pathname                                 |

### Evaluation Model

For each filesystem entry:

- Traverse directory tree.
- Evaluate expression left-to-right.
- Apply short-circuit logic.
- If expression is true:
  - Execute action
  - If no explicit action → -print is implied

### Alternatives

| Tool      | Traversal Model | Predicate Model         | Execution Model       |
| --------- | --------------- | ----------------------- | --------------------- |
| `find`    | DFS walk        | Boolean expression tree | Sequential evaluation |
| `fd`      | Parallel walk   | Simplified filter model | Multithreaded         |
| `ripgrep` | Parallel walk   | Content-focused         | Multithreaded         |
| `bfs`     | Parallel walk   | GNU-compatible          | Optimized evaluator   |
| `locate`  | Indexed lookup  | Name-only               | Database query        |

## References

- [find](https://en.wikipedia.org/wiki/Find_(Unix))
- [man pages - find](https://www.man7.org/linux/man-pages/man1/find.1.html)
- [GNU Find manual](https://www.gnu.org/software/findutils/manual/html_mono/find.html)
- [GNU Findutils](https://www.gnu.org/software/findutils/)
- [Difference between find and GNU find](https://unix.stackexchange.com/questions/475020/difference-between-find-and-gnu-find)
- [Find source code](https://github.com/aixoss/findutils/tree/r4.4.2-aix/find)
- [fd](https://github.com/sharkdp/fd)
- [A list of new(ish) command line tools](https://jvns.ca/blog/2022/04/12/a-list-of-new-ish--command-line-tools/)
