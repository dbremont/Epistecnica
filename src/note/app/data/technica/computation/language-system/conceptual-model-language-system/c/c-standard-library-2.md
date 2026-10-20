# C++: 📚 Standard Library

> Which programming building blocks are embedded in the language?
> 

> See <> for Internal Representation.
> 

Guiding Questions

- …

## Standard Library

| **Category** | **Header** | **Element(s)** | **Description** |
| --- | --- | --- | --- |
| **Core Language Support** | `<cstddef>` | `size_t`, `ptrdiff_t`, `nullptr_t` | Fundamental types and macros. |
|  | `<cstdlib>` | `malloc`, `free`, `abort`, `exit` | Memory, process control, conversions. |
|  | `<cstdint>` | Fixed-width integer types | Precise integer-size definitions. |
|  | `<typeinfo>` | `type_info`, `typeid` | Run-time type information (RTTI). |
|  | `<exception>` | `exception`, `terminate` | Base exception types. |
|  | `<new>` | `new`, `delete`, allocators | Dynamic memory allocation utilities. |
|  | `<initializer_list>` | `initializer_list` | Support for braced initializer lists. |
| **Algorithms** | `<algorithm>` | sort, find, transform | General-purpose algorithms for ranges. |
|  | `<numeric>` | `accumulate`, `inner_product` | Numeric algorithms on sequences. |
|  | `<execution>` | Execution policies | Parallel/Vectorized algorithm policies. |
|  | `<random>` | engines, distributions | Random numbers and distributions. |
| **Containers – Sequence** | `<vector>` | `std::vector` | Dynamic array. |
|  | `<array>` | `std::array` | Fixed-size array. |
|  | `<deque>` | `std::deque` | Double-ended queue. |
|  | `<list>` | `std::list` | Doubly-linked list. |
|  | `<forward_list>` | `std::forward_list` | Singly-linked list. |
|  | `<span>` | `std::span` | Non-owning view of contiguous memory. |
| **Containers – Associative** | `<set>` | `set`, `multiset` | Ordered unique elements (tree-based). |
|  | `<map>` | `map`, `multimap` | Ordered key-value pairs. |
| **Containers – Unordered** | `<unordered_set>` | unordered_set family | Hash-based sets. |
|  | `<unordered_map>` | unordered_map family | Hash-based maps. |
| **Containers – Adapters** | `<stack>` | `stack` | LIFO adapter. |
|  | `<queue>` | `queue`, `priority_queue` | FIFO and priority queue adapters. |
| **Strings & Text** | `<string>` | `std::string`, `std::wstring` | Dynamic text strings. |
|  | `<string_view>` | `std::string_view` | Non-owning text view. |
|  | `<charconv>` | `to_chars`, `from_chars` | Fast conversion to/from numbers. |
| **I/O** | `<iostream>` | `cin`, `cout`, `cerr` | Standard streams. |
|  | `<fstream>` | `ifstream`, `ofstream` | File stream interfaces. |
|  | `<sstream>` | `stringstream` | String-based I/O. |
|  | `<iomanip>` | manipulators | I/O formatting. |
|  | `<cstdio>` | `printf`, `fopen` | C I/O compatibility. |
| **Concurrency** | `<thread>` | `std::thread` | Thread abstraction. |
|  | `<mutex>` | `mutex`, `unique_lock` | Mutual exclusion primitives. |
|  | `<shared_mutex>` | `shared_mutex` | Reader-writer locking. |
|  | `<atomic>` | `atomic<T>` | Atomic operations. |
|  | `<condition_variable>` | condition_variable | Thread waiting/wake facilities. |
|  | `<future>` | `future`, `promise`, `async` | Asynchronous execution. |
|  | `<stop_token>` | `stop_token` | Cooperative cancellation support. |
|  | `<barrier>` / `<latch>` | barrier, latch | Thread coordination. |
| **Time & Date** | `<chrono>` | clocks, durations, time_point | Wall/steady clock time handling. |
| **Utility** | `<utility>` | `pair`, `move`, `forward` | General utility helpers. |
|  | `<tuple>` | `tuple` | Heterogeneous product type. |
|  | `<optional>` | optional | Optional values. |
|  | `<variant>` | variant | Discriminated union type. |
|  | `<any>` | any | Type-erased storage. |
|  | `<functional>` | `function`, bind, mem_fn | Callable wrappers. |
|  | `<bitset>` | bitset | Compile-time sized bitset. |
|  | `<bit>` | bit operations | Low-level bit manipulation. |
|  | `<ratio>` | ratio | Compile-time rational arithmetic. |
|  | `<compare>` | `<=>`, strong_ordering | Three-way comparison utilities. |
| **Memory Model** | `<memory>` | smart pointers | `unique_ptr`, `shared_ptr`, allocators. |
|  | `<memory_resource>` | PMR memory model | Polymorphic memory resources. |
| **Localization** | `<locale>` | locale, facets | Culture-sensitive formatting. |
|  | `<codecvt>` | codecvt | Character conversion facets (deprecated). |
| **C Compatibility** | `<cmath>` | math functions | C math. |
|  | `<cstring>` | memory/string ops | C char array utilities. |
|  | `<ctime>` | time utilities | C time library. |
|  | `<cfloat>` `<climits>` | limits | Numeric limits. |

## References

- https://en.wikipedia.org/wiki/Standard_library
- https://en.cppreference.com/w/cpp/standard_library
- [X: **🏷️** Type System](https://app.notion.com/p/X-Type-System-fc2456113c894e699643d8ce60a4647f?pvs=21) [In a Particular Language Change this to the Actual Langauge].