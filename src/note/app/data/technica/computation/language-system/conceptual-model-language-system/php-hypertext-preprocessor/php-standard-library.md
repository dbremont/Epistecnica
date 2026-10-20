# PHP: 📚 Standard Library

> Which programming building blocks are embedded in the language?
> 

> See <> for Internal Representation.
> 

## Breviarium

PHP standard library is conceptually organized around:

1. **Core language functions** – basic string, array, math, and type handling.
2. **SAPI functions** – server APIs for HTTP, CLI, etc.
3. **Extensions** – specific libraries for DBs, crypto, image processing, XML/JSON, etc.

## Standard Library

> PHP provides a large set of built-in functions and classes organized into categories for common tasks.
> 

| **Category** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Core** | Fundamental language utilities, constants, and general functions. | `isset()`, `empty()`, `die()`, `exit()`, `var_dump()`, `define()` |
| **Arrays** | Functions for array manipulation, searching, sorting, and iteration. | `array_map()`, `array_filter()`, `array_merge()`, `sort()`, `count()` |
| **Strings** | Functions for string manipulation, pattern matching, and encoding. | `strlen()`, `strpos()`, `str_replace()`, `preg_match()`, `substr()` |
| **Mathematics** | Mathematical operations, random numbers, and numeric utilities. | `abs()`, `ceil()`, `floor()`, `rand()`, `sqrt()`, `pow()` |
| **Date & Time** | Functions and classes to handle dates, times, intervals, and time zones. | `date()`, `time()`, `strtotime()`, `DateTime`, `DateInterval` |
| **Filesystem & I/O** | File and directory handling, reading/writing, streams, and permissions. | `fopen()`, `fread()`, `file_get_contents()`, `mkdir()`, `unlink()` |
| **Network & Sockets** | Functions for HTTP, FTP, email, and socket operations. | `curl_init()`, `fsockopen()`, `file_get_contents('http://')`, `socket_create()` |
| **JSON & Serialization** | Encode/decode JSON and serialize/unserialize data structures. | `json_encode()`, `json_decode()`, `serialize()`, `unserialize()` |
| **Error Handling** | Functions and classes for exceptions, logging, and error reporting. | `error_log()`, `set_error_handler()`, `Exception`, `Error` |
| **OOP Utilities** | Standard object-oriented classes and interfaces. | `stdClass`, `ArrayObject`, `Iterator`, `Countable`, `WeakReference` |
| **Reflection** | Inspect classes, functions, properties, and parameters at runtime. | `ReflectionClass`, `ReflectionMethod`, `ReflectionFunction`, `ReflectionProperty` |
| **Filters & Validation** | Functions for input validation and sanitization. | `filter_var()`, `filter_input()`, `FILTER_VALIDATE_EMAIL` |
| **Miscellaneous** | Other utility functions not covered above. | `uniqid()`, `microtime()`, `getenv()`, `phpinfo()` |

## References

- https://en.wikipedia.org/wiki/Standard_library
- [X: **🏷️** Type System](https://app.notion.com/p/X-Type-System-fc2456113c894e699643d8ce60a4647f?pvs=21) [In a Particular Language Change this to the Actual Langauge].