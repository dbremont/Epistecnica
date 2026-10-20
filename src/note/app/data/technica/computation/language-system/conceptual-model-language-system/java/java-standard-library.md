# Java: 📚 Standard Library

> Which programming building blocks are embedded in the language?
> 

> See <> for Internal Representation.
> 

## Java Standard Library (std) Types

| **Category** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Primitive Types** | Basic data types provided by Java that are not objects and have a fixed size. | `int`, `double`, `char`, `boolean` |
| **Wrapper Classes** | Classes that provide object representation for primitive types and offer utility methods. | `Integer`, `Double`, `Character`, `Boolean` |
| **String Handling** | Classes for managing and manipulating character strings. | `String`, `StringBuilder`, `StringBuffer` |
| **Collections** | Interfaces and classes for handling groups of objects, such as lists, sets, and maps. | `List` (`ArrayList`, `LinkedList`), `Set` (`HashSet`, `TreeSet`), `Map` (`HashMap`, `TreeMap`) |
| **Input/Output (I/O)** | Classes for reading and writing data, including file and network operations. | `File`, `InputStream`, `OutputStream`, `Reader`, `Writer` |
| **Concurrency** | Classes and interfaces for managing and synchronizing threads and concurrent operations. | `Thread`, `Runnable`, `ExecutorService`, `Future`, `CountDownLatch` |
| **Utilities** | Utility classes that provide common functions and operations, including mathematical and date/time functions. | `Math`, `Date`, `Calendar`, `UUID`, `Arrays`, `Collections` |
| **Networking** | Classes for networking operations, including TCP/IP and UDP protocols. | `Socket`, `ServerSocket`, `URL`, `HttpURLConnection` |
| **Reflection** | Classes for inspecting and manipulating classes, methods, and fields at runtime. | `Class`, `Method`, `Field`, `Constructor` |
| **Exceptions** | Classes for handling and creating exceptions and errors. | `Exception`, `RuntimeException`, `IOException`, `NullPointerException` |
| **Security** | Classes and interfaces for managing security features, such as encryption and access control. | `MessageDigest`, `Cipher`, `KeyPair`, `SecureRandom` |

### Java Primitive Expression

| Java Primitive Expression Type | Evaluation Order / Strategy | Operand Evaluation Semantics | Control Semantics | Runtime Mechanism | Canonical JVM / Semantic Behavior |
| --- | --- | --- | --- | --- | --- |
| Arithmetic Expression | Left-to-right eager evaluation | Both operands fully evaluated before operation | Strict computation | JVM arithmetic opcodes (`iadd`, `imul`, etc.) | Numeric reduction over primitive values |
| Boolean Logical Expression (`&&`, `||`) | Left operand first | RHS conditionally evaluated | Short-circuit branching | Conditional jump instructions | Lazy branch-controlled evaluation |
| Boolean Bitwise Logical Expression (`&`, `|`, `^`) | Left-to-right eager evaluation | Both operands always evaluated | No short-circuiting | Bitwise logical opcodes | Full boolean/bit evaluation |
| Relational Expression | Left operand then right operand | Both operands fully reduced before comparison | Predicate computation | Comparison opcodes (`if_icmp*`) | Produces boolean truth value |
| Equality Expression | Left-to-right eager evaluation | Both references/values computed first | Identity/value comparison | Primitive compare or reference compare | `==` on refs compares identity |
| Unary Expression | Operand evaluated first | Single operand transformed | Direct local transformation | Negation/complement opcodes | Local value mutation/transformation |
| Increment / Decrement Expression | Variable reference resolved first | Read-modify-write cycle | Pre/post sequencing semantics | Load → modify → store | Postfix returns old value |
| Assignment Expression | RHS evaluated before assignment target update | RHS fully computed first | Store side effect | Store opcodes (`istore`, `putfield`) | Assignment yields assigned value |
| Compound Assignment Expression | LHS reference resolved first | Read → compute → cast → write | Atomic-looking syntactic sugar | Expanded arithmetic + assignment | Implicit narrowing conversions possible |
| Conditional (Ternary) Expression | Condition evaluated first | Only selected branch evaluated | Branch-controlled evaluation | Conditional jump structure | Lazy branch selection |
| Cast Expression | Operand evaluated first | Runtime/static conversion applied | Type reinterpretation/check | Cast/check instructions | May throw `ClassCastException` |
| Method Invocation Expression | Receiver first, then arguments left-to-right | All arguments eagerly evaluated before call | Dynamic/static dispatch | Invocation opcodes (`invokevirtual`, etc.) | Polymorphic runtime dispatch |
| Constructor Invocation Expression | Arguments evaluated before allocation completion | Constructor chain executes after allocation | Object initialization sequencing | `new` + `<init>` invocation | Partially initialized object during ctor |
| Lambda Expression | Capture environment at creation time | Body deferred until invocation | Deferred execution | Synthetic functional object | Closure semantics |
| Method Reference Expression | Receiver/type resolved first | Invocation deferred | Indirect callable binding | Method handle linkage | Functional interface adaptation |
| Object Creation Expression | Constructor arguments evaluated first | Allocation precedes constructor execution | Initialization lifecycle | Heap allocation + constructor | Reference returned after init |
| Array Access Expression | Array ref evaluated before index | Bounds checked after index evaluation | Indexed memory access | `iaload`, etc. | May throw `ArrayIndexOutOfBoundsException` |
| Array Creation Expression | Dimension expressions evaluated left-to-right | Sizes computed before allocation | Structured allocation | `newarray`, `anewarray` | Contiguous indexed structure |
| Field Access Expression | Receiver evaluated first | Field resolution after object evaluation | Member dereference | `getfield`, `getstatic` | Null check before access |
| `instanceof` Expression | Operand evaluated first | Runtime type relation check | Type predicate evaluation | Runtime type metadata lookup | Returns boolean |
| Switch Expression | Selector evaluated once | Matching branch selected afterward | Jump-table or lookup dispatch | `tableswitch` / `lookupswitch` | Exhaustive expression semantics |
| Pattern Matching Expression | Candidate evaluated first | Structural/type checks performed | Conditional binding introduction | Pattern dispatch logic | Scoped binding generation |
| String Concatenation Expression | Operands evaluated left-to-right | Each operand converted to string | Sequential accumulation | `StringBuilder` or indy concat | Immutable string production |
| Floating-Point Expression | Strict left-to-right IEEE-754 evaluation | Operands rounded per FP semantics | Deterministic FP reduction | FP arithmetic opcodes | NaN/Infinity propagation |
| Integer Expression | Fixed-width eager arithmetic | Overflow ignored silently | Two’s complement arithmetic | Integer arithmetic opcodes | Wraparound semantics |
| Constant Expression | Compile-time reduction | No runtime operand evaluation | Static folding | Compiler constant propagation | Embedded into bytecode constant pool |
| Generic Type Expression | Compile-time type substitution | Erased at runtime | Static type constraint evaluation | Type erasure | Mostly non-reified semantics |
| Annotation Expression | Compile-time metadata evaluation | Constants resolved statically | Declarative metadata attachment | Annotation table generation | Reflection-visible metadata |
| Stream Pipeline Expression | Intermediate ops deferred | Terminal operation triggers traversal | Lazy functional pipeline | Iterator/spliterator execution | Pull-based evaluation |
| Optional Expression | Wrapped value evaluated first | Transformations applied conditionally | Presence-propagation semantics | Functional wrapper dispatch | Null-safe chaining |
| Exception Expression | Normal evaluation until failure point | Stack unwinding on exception | Non-local control transfer | Exception tables + unwinder | Abrupt completion semantics |
| Synchronization Expression | Lock target evaluated first | Monitor acquired before body execution | Mutual exclusion region | `monitorenter` / `monitorexit` | Structured locking semantics |
| Class Literal Expression | Type resolved statically | No dynamic operand evaluation | Class metadata retrieval | Constant pool resolution | Produces `Class<?>` object |
| Enum Constant Expression | Constant resolved statically | Singleton instance retrieval | Static symbolic lookup | Static field access | Canonical singleton semantics |
| Functional Composition Expression | Functions resolved first | Invocation chained sequentially | Deferred composition semantics | Nested lambda invocation | Higher-order evaluation |
| Reflection Expression | Metadata lookup precedes invocation | Arguments boxed/unboxed dynamically | Indirect runtime dispatch | Reflection subsystem | Slower dynamic evaluation |
| Pattern Switch Expression | Selector evaluated once | Patterns tested sequentially | Structured dispatch + binding | Pattern dispatch engine | Exhaustive typed branching |
| Null Dereference Expression | Reference evaluated before access | Null check performed implicitly | Exceptional control transfer | Implicit JVM null checks | Throws `NullPointerException` |
| Boxing / Unboxing Expression | Primitive/reference evaluated first | Conversion wrapper applied | Representation transformation | Wrapper object creation/extraction | Autoboxing semantics |
| Varargs Expression | Arguments evaluated left-to-right | Array packing occurs before call | Argument aggregation | Synthetic array creation | Runtime variadic adaptation |
| Chained Expression | Evaluated strictly left-to-right | Intermediate values propagated | Sequential dependency evaluation | Nested expression tree execution | Deterministic sequencing |
| Sequence Expression (statement chains) | Top-to-bottom execution order | Prior side effects visible downstream | Imperative sequencing | Linear instruction stream | Program-order semantics |

## Standard Library

> 

| **Package** | **Description** | **Core Classes** |
| --- | --- | --- |
| **java.lang** | Fundamental classes like object manipulation, basic data types, and system operations. | `Object`, `String`, `Math`, `System`, `Thread`, `Exception` |
| **java.util** | Collections framework, date/time utilities, and various utility classes. | `ArrayList`, `HashMap`, `HashSet`, `Collections`, `Date`, `Calendar` |
| **java.io** | File I/O and data stream handling. | `File`, `InputStream`, `OutputStream`, `Reader`, `Writer` |
| **java.nio** | New I/O (NIO) classes for high-performance I/O operations. | `ByteBuffer`, `CharBuffer`, `FileChannel`, `Path` |
| **java.nio.file** | File and directory manipulation with the NIO2 API. | `Files`, `Paths`, `Path`, `StandardOpenOption` |
| **java.net** | Networking classes for communication over the network. | `URL`, `URLConnection`, `Socket`, `ServerSocket` |
| **java.sql** | JDBC API for database access and manipulation. | `Connection`, `Statement`, `ResultSet`, `DriverManager` |
| **javax.swing** | GUI components and layout management for Swing-based UIs. | `JFrame`, `JButton`, `JLabel`, `JPanel`, `JTable` |
| **java.awt** | Essential GUI components and graphical operations for AWT. | `Frame`, `Button`, `Label`, `Graphics`, `Color` |
| **javax.xml.parsers** | XML parsing and transformation utilities. | `DocumentBuilder`, `SAXParser`, `Transformer` |
| **javax.xml.xpath** | XPath API for querying XML documents. | `XPath`, `XPathExpression`, `XPathFactory` |
| **java.util.concurrent** | Concurrency utilities for thread management and synchronization. | `ExecutorService`, `Future`, `CountDownLatch`, `ConcurrentHashMap` |
| **java.util.logging** | Logging framework for recording and managing log messages. | `Logger`, `Handler`, `Formatter`, `Level` |
| **java.security** | Security classes for cryptography and secure random number generation. | `MessageDigest`, `Signature`, `KeyPairGenerator`, `SecureRandom` |
| **java.rmi** | Remote Method Invocation (RMI) for distributed object communication. | `Remote`, `Naming`, `RemoteException` |
| **javax.management** | Manage and monitor Java applications using JMX. | `MBeanServer`, `ObjectName`, `MBean` |
| **javax.activation** | Activation framework for data type handling. | `DataHandler`, `DataSource` |

## Representation

> Which **computational representational** mechanisms does **Java support by default**?
> 

| **Representation Type** | **Instance(s)** | **What the Data Can Represent** |
| --- | --- | --- |
| **Scalar Values** | `byte`, `short`, `int`, `long`, `float`, `double`, `boolean`, `char` | Quantities, counts, measurements, truth values, codes |
| **Symbolic Identifiers** | `String`, `CharSequence`, `Enum`, `UUID` | Names, labels, identifiers, categories, symbolic domains |
| **Structured Records / Entities** | `class`, `record`, POJOs | Objects, entities, structured facts, domain models |
| **Product Types (Tuples)** | `record`, small classes, `Map.Entry` | Fixed-arity composite values |
| **Sequential Structures** | Arrays (`T[]`), `List`, `ArrayList`, `LinkedList`, `Deque`, `Queue`, `ArrayDeque` | Ordered sequences, logs, time series, workflows |
| **Set Structures** | `Set`, `HashSet`, `LinkedHashSet`, `TreeSet`, `EnumSet` | Membership, uniqueness, collections without duplication |
| **Associative Structures** | `Map`, `HashMap`, `LinkedHashMap`, `TreeMap`, `EnumMap`, `WeakHashMap`, `IdentityHashMap`, `ConcurrentHashMap`, `Properties`, `ConcurrentHashMap`, `ConcurrentSkipListMap`, `Map.of(...)`, `Collections.unmodifiableMap(Map)` | Key–value associations, attribute maps, environments, indexes |
| **Hierarchical Structures** | Object containment, `org.w3c.dom.Node`, `Document`, `Element`, file trees (`Path`) | Part–whole relations, nested structures, trees |
| **Graph Structures** | Object reference graphs, adjacency maps (`Map<T, Set<T>>`) | Networks, dependencies, relations |
| **Relational / Tabular Data** | `ResultSet`, `RowSet`, `TableModel` | Datasets, relations, rows of entities |
| **Multidimensional Data** | Multi-dimensional arrays (`T[][]`), nested maps, `DoubleBuffer`, `FloatBuffer` | Matrices, tensors, grids |
| **Interval / Piecewise Representations** | `NavigableMap`, `TreeMap`, decision logic, switch expressions | Ranges, piecewise functions, rules |
| **State Representations** | Mutable objects, fields, `Atomic*` classes | System state, configuration, world models |
| **Behavioral Representations** | `Runnable`, `Callable`, `Function`, `Predicate`, `Supplier`, lambdas | Actions, transformations, policies |
| **Control Abstractions** | `Thread`, `Executor`, `CompletableFuture`, `ForkJoinTask` | Concurrent processes, workflows |
| **Event Representations** | `EventObject`, listeners, callbacks | Signals, events, notifications |
| **Executable Metadata** | `Class`, `Method`, `Field`, `Constructor`, `Annotation` | Programs-as-data, reflection |
| **Type-Level Representations** | `Class<T>`, generics, bounds, wildcards | Type information, constraints |
| **Temporal Representations** | `Instant`, `LocalDate`, `Duration`, `Period`, `ZonedDateTime` | Time points, intervals, durations |
| **Spatial / Structural Data** | `Point`, `Rectangle`, `Shape`, `AffineTransform` | Geometric and spatial relations |
| **Textual / Document Models** | `String`, `StringBuilder`, `Reader`, `Writer`, DOM, SAX | Text, documents, structured text |
| **Binary / Raw Data** | `byte[]`, `ByteBuffer`, `InputStream`, `OutputStream` | Binary payloads, serialized data |
| **Serialization Models** | `Serializable`, `Externalizable`, `ObjectInputStream` | Persisted object graphs |
| **Configuration Models** | `Properties`, XML, JSON (via std APIs) | System and application configuration |
| **Error / Exceptional States** | `Throwable`, `Exception`, `Error` | Failure states, abnormal conditions |
| **Constraint / Rule Encoding** | Enums, predicates, validators | Business rules, invariants |
| **Meta-Models** | Reflection + annotations | Schemas, models of models |

## Miscellanea

Java: 📚 Standard Library

## References

- [The Date Time API](https://dev.java/learn/date-time/)
- Java: **🏷️** Type System
- [An introduction to java.time](https://yawk.at/java.time/)
- https://en.wikipedia.org/wiki/Standard_library
- [Java SE 8 Date and Time (oracle.com)](https://news.ycombinator.com/item?id=7258115)
- [Should I use Java date and time classes or go with a 3rd party library like Joda Time?](https://stackoverflow.com/questions/589870/should-i-use-java-date-and-time-classes-or-go-with-a-3rd-party-library-like-joda)
- https://github.com/carrotsearch/hppc