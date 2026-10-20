# Python: The Standard Library

> The **Standard Library** is extensive and includes modules for various tasks like file handling, data manipulation, networking, testing, and more.
> 

## Python Standard Library

| **Category** | **Module** | **Description** |
| --- | --- | --- |
| **Built-in Types** | `collections` | Provides specialized container datatypes like named tuples, deque, Counter, defaultdict, etc. |
|  | `datetime` | Supplies classes for manipulating dates and times. |
|  | `functools` | Higher-order functions like `reduce`, `partial`, and decorators like `lru_cache`. |
|  | `itertools` | Implements iterator building blocks such as `count`, `cycle`, `repeat`, `chain`, etc. |
|  | `math` | Provides mathematical functions like `sqrt`, `factorial`, `gcd`, `trigonometric` functions, etc. |
|  | `random` | Implements pseudo-random number generators for various distributions. |
|  | `statistics` | Functions for calculating basic statistical properties (mean, median, variance, etc.). |
| **Text Processing** | `string` | Common string operations, constants, and templates. |
|  | `re` | Regular expression matching operations. |
|  | `textwrap` | Text wrapping and filling for formatting text. |
|  | `unicodedata` | Provides access to the Unicode Character Database (UCD) and properties of Unicode characters. |
|  | `difflib` | Tools to compute and work with differences between sequences, like comparing text files. |
| **Data Formats** | `json` | Parse JSON (JavaScript Object Notation) into Python objects and vice versa. |
|  | `csv` | Reader and writer objects to handle CSV (Comma-Separated Values) file format. |
|  | `xml` | Modules for parsing and creating XML documents. |
|  | `html` | HTML parsing and handling (e.g., `html.parser`, `html.entities`). |
|  | `configparser` | For working with configuration files (similar to Windows INI files). |
| **File and Directory Access** | `os` | Interfaces with the operating system, including file and directory operations. |
|  | `shutil` | High-level file operations like copying, moving, and archiving. |
|  | `pathlib` | Object-oriented filesystem paths, providing a higher-level API than `os.path`. |
|  | `glob` | Filename pattern matching using Unix shell-style wildcards. |
|  | `tempfile` | Creates temporary files and directories. |
| **Data Compression and Archiving** | `zlib` | Compression and decompression using the `zlib` library. |
|  | `gzip` | Read and write GNU zip files (`.gz`). |
|  | `bz2` | Compression and decompression using the `bzip2` algorithm. |
|  | `tarfile` | Read and write tar archive files. |
| **Networking** | `socket` | Low-level networking interface. |
|  | `http` | Modules for HTTP protocol handling, including servers, clients, and cookies. |
|  | `urllib` | Modules for URL handling and manipulation, including opening and parsing URLs. |
|  | `ftplib` | FTP protocol client for file transfers over FTP. |
|  | `smtplib` | Client for sending emails using SMTP (Simple Mail Transfer Protocol). |
|  | `ssl` | TLS/SSL wrapper for socket objects for secure communications. |
| **Concurrent Execution** | `threading` | Higher-level threading interface for concurrent execution of code. |
|  | `multiprocessing` | Create processes that can run in parallel on multiple CPU cores. |
|  | `concurrent.futures` | High-level interface for asynchronously executing callables using threads or processes. |
|  | `asyncio` | Asynchronous I/O, event loop, coroutines, and tasks, for writing concurrent code using async/await syntax. |
| **System-Related Modules** | `sys` | Provides access to system-specific parameters and functions. |
|  | `subprocess` | Spawn new processes, connect to their input/output/error pipes, and obtain their return codes. |
|  | `signal` | Sets handlers for asynchronous events like interrupts and timers. |
|  | `getopt` | Command-line option parser for scripts that need to handle long and short options. |
| **Testing** | `unittest` | Unit testing framework, including test discovery, setup/teardown, and assertions. |
|  | `pytest` | Popular third-party testing framework with many advanced features, though not part of the Standard Library. |
|  | `doctest` | Test interactive Python examples embedded in docstrings. |
|  | `pdb` | Interactive debugger for Python programs. |
| **Cryptography** | `hashlib` | Secure hash and message digest algorithms, including SHA and MD5 families. |
|  | `hmac` | Keyed-hashing for message authentication using HMAC algorithm. |
| **Data Persistence** | `sqlite3` | DB-API 2.0 interface for SQLite databases, which provides a lightweight disk-based database. |
|  | `pickle` | Python object serialization and deserialization (not secure against untrusted sources). |
|  | `shelve` | A simple persistent storage option using a dictionary-like API. |
| **Utilities** | `argparse` | Command-line argument parsing, replacing `optparse`. |
|  | `logging` | Flexible framework for logging messages from Python programs. |
|  | `timeit` | Measure execution time of small code snippets. |
|  | `uuid` | Generate universally unique identifiers (UUIDs). |
|  | `typing` | Support for type hints and static type checking. |
| **Mathematics** | `decimal` | Decimal fixed-point and floating-point arithmetic, providing exact precision. |
|  | `fractions` | Support for rational number arithmetic using fractions. |
|  | `statistics` | Provides functions for basic statistical operations (e.g., mean, median, mode). |

## Representation

> **Variable-Length Objects**: Types like `int`, `str`, and `list` use variable-length storage to handle arbitrary sizes.
> 

> **Hash Tables**:  `dict` and `set` use hash tables internally for O(1) average-time complexity for lookups and insertions.
> 

> **Type Overhead**: Every Python object includes metadata (e.g., reference count, type pointer) as part of its internal representation, which adds overhead compared to lower-level languages.
> 

> **Memory Efficiency**:
> 
> - Immutable types (`int`, `str`, `tuple`, etc.) are often optimized for memory reuse (e.g., small integers and short strings are interned).
> - Mutable types (`list`, `dict`, `set`, etc.) require additional memory for dynamic resizing.

> Below is an extended table that includes Python's basic types, their descriptions, examples, and their **internal representation** (how they are stored in memory):
> 

| **Type** | **Description** | **Example** | **Internal Representation** |
| --- | --- | --- | --- |
| `int` | Integer numbers (unlimited precision). | `x = 42` | Stored as a variable-length sequence of digits (arbitrary precision). |
| `float` | Floating-point numbers (double-precision). | `y = 3.14` | Stored as a 64-bit IEEE 754 double-precision binary format. |
| `bool` | Boolean values (`True` or `False`). | `flag = True` | Internally, `True` is represented as `1` and `False` as `0` (subclass of `int`). |
| `str` | Immutable sequence of Unicode characters (strings). | `text = "Hello, World!"` | Stored as an array of Unicode code points (UTF-8, UTF-16, or UTF-32, depending on content). |
| `list` | Mutable, ordered sequence of items. | `items = [1, 2, 3]` | Stored as a dynamic array of pointers to objects. |
| `tuple` | Immutable, ordered sequence of items. | `coordinates = (10, 20)` | Stored as a fixed-length array of pointers to objects. |
| `dict` | Mutable mapping of key-value pairs (unordered). | `person = {"name": "Alice", "age": 30}` | Stored as a hash table for efficient key lookup. |
| `set` | Mutable, unordered collection of unique elements. | `unique_numbers = {1, 2, 3}` | Stored as a hash table with only keys (no values). |
| `frozenset` | Immutable version of `set`. | `frozen = frozenset({1, 2, 3})` | Same as `set`, but immutable. |
| `bytes` | Immutable sequence of bytes (raw binary data). | `data = b"hello"` | Stored as a fixed-length array of bytes (8-bit values). |
| `bytearray` | Mutable sequence of bytes. | `mutable_data = bytearray(b"hello")` | Stored as a dynamic array of bytes (8-bit values). |
| `NoneType` | Represents the absence of a value (singleton `None`). | `x = None` | Stored as a singleton object in memory. |
| `complex` | Complex numbers with real and imaginary parts. | `z = 2 + 3j` | Stored as two 64-bit floats (real and imaginary parts). |
| `range` | Immutable sequence of numbers, commonly used for looping. | `numbers = range(5)` | Stored as start, stop, and step values (lazily evaluated). |
| `type` | Represents the type of an object (used for metaprogramming). | `t = type(42)` | Stored as a metadata object describing the type. |
| `function` | Represents a function or method. | `def foo(): pass` | Stored as a code object with references to its bytecode, globals, and closure. |
| `module` | Represents a Python module. | `import math; math` | Stored as a namespace containing attributes and functions. |
| `object` | Base class for all Python classes. | `obj = object()` | Stored as a minimal structure with a reference to its type and attributes. |

## References

- https://docs.python.org/3/library/index.html
- https://peps.python.org/pep-0393/