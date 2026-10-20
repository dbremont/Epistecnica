# C++: Performace

> Which programming building blocks are embedded in the language?
> 

| **Header** | **Description** | **Abstractions** |
| --- | --- | --- |
| `<algorithm>` | Provides a collection of algorithms for sorting, searching, and modifying data. | `std::sort`, `std::find`, `std::binary_search`, `std::partition`, `std::rotate` |
| `<array>` | Implements a fixed-size array container. | `std::array`, `at`, `size`, `begin`, `end` |
| `<any>` | Allows storage and manipulation of values of any type. | `std::any`, `std::any_cast`, `has_value`, `reset` |
| `<atomic>` | Provides atomic operations and types for safe multithreading. | `std::atomic`, `load`, `store`, `exchange`, `fetch_add`, `compare_exchange` |
| `<barrier>` | Synchronization for threads to wait until reaching a barrier. | `std::barrier`, `arrive`, `wait` |
| `<bit>` | Supplies utilities for low-level bit manipulation. | `std::bit_ceil`, `std::bit_floor`, `std::countl_zero`, `std::popcount` |
| `<bitset>` | Allows manipulation of fixed-size sequences of bits. | `std::bitset`, `to_string`, `count`, `reset`, `set` |
| `<charconv>` | Provides conversion between strings and numeric values. | `std::to_chars`, `std::from_chars` |
| `<chrono>` | Provides tools for time measurement and manipulation. | `std::chrono::duration`, `std::chrono::time_point`, `now`, `hours`, `seconds` |
| `<codecvt>` | Supplies tools for character encoding conversions. | `std::codecvt`, `std::wstring_convert`, `std::codecvt_base` |
| `<compare>` | Provides utilities for three-way comparison. | `std::strong_ordering`, `std::weak_ordering`, `std::partial_ordering` |
| `<complex>` | Provides tools for working with complex numbers. | `std::complex`, `real`, `imag`, `abs`, `arg`, `norm` |
| `<concepts>` | Defines concepts for constraining templates. | `std::same_as`, `std::convertible_to`, `std::integral`, `std::floating_point` |
| `<condition_variable>` | Enables thread synchronization by blocking threads until a condition is satisfied. | `std::condition_variable`, `wait`, `notify_one`, `notify_all` |
| `<coroutine>` | Supplies tools for coroutines, enabling asynchronous programming. | `std::coroutine_handle`, `std::suspend_always`, `std::suspend_never` |
| `<deque>` | Implements a double-ended queue container. | `std::deque`, `push_back`, `push_front`, `pop_back`, `pop_front` |
| `<execution>` | Provides execution policies for parallel algorithms. | `std::execution::seq`, `std::execution::par`, `std::execution::par_unseq` |
| `<expected>` | Enables operations with expected values or errors. | `std::expected`, `has_value`, `value`, `error` |
| `<exception>` | Supplies tools for handling exceptions and error conditions. | `std::exception`, `what`, `std::bad_alloc`, `std::runtime_error` |
| `<filesystem>` | Provides tools for filesystem path manipulation and file operations. | `std::filesystem::path`, `std::filesystem::exists`, `create_directory`, `remove` |
| `<flat_map>` | Implements an ordered map with flat storage. | `std::flat_map`, `insert`, `erase`, `find` |
| `<flat_set>` | Implements an ordered set with flat storage. | `std::flat_set`, `insert`, `erase`, `find` |
| `<format>` | Supplies tools for formatting strings. | `std::format`, `std::vformat`, `std::formatted_size` |
| `<forward_list>` | Implements a singly linked list container. | `std::forward_list`, `push_front`, `pop_front`, `insert_after`, `erase_after` |
| `<fstream>` | Provides file input and output streams. | `std::ifstream`, `std::ofstream`, `std::fstream`, `open`, `close` |
| `<functional>` | Includes function objects and utilities for functional programming. | `std::function`, `std::bind`, `std::less`, `std::greater`, `std::not_fn` |
| `<future>` | Supports asynchronous operations and futures for concurrency. | `std::future`, `std::promise`, `std::async`, `wait`, `get` |
| `<generator>` | Enables generation of coroutine-based lazy sequences. | `std::generator`, `std::yield_value` |
| `<hazard_pointer>` | Provides safe memory reclamation for lock-free data structures. | `std::hazard_pointer`, `retire`, `reclaim` |
| `<iomanip>` | Supplies manipulators for stream input/output formatting. | `std::setw`, `std::setprecision`, `std::fixed`, `std::hex`, `std::oct` |
| `<inplace_vector>` | Implements an in-place vector with fixed storage. | `std::inplace_vector`, `emplace_back`, `push_back`, `resize` |
| `<ios>` | Provides basic stream I/O types and utilities. | `std::ios_base`, `std::streamsize`, `std::ios::sync_with_stdio` |
| `<iosfwd>` | Forward declarations for stream I/O classes to reduce compile time. | `std::istream`, `std::ostream`, `std::fstream` |
| `<iostream>` | Provides standard I/O stream objects. | `std::cin`, `std::cout`, `std::cerr`, `std::clog` |
| `<istream>` | Defines input stream classes. | `std::istream`, `std::getline`, `std::ignore` |
| `<iterator>` | Supplies utilities for working with iterators. | `std::iterator`, `std::back_inserter`, `std::advance`, `std::next` |
| `<latch>` | Synchronization for threads to wait until a latch count reaches zero. | `std::latch`, `count_down`, `wait` |
| `<limits>` | Provides numeric limits for data types. | `std::numeric_limits`, `max`, `min`, `epsilon`, `infinity` |
| `<linalg>` | Supplies linear algebra tools for vectors and matrices. | `std::linalg::vector`, `matrix`, `dot`, `cross` |
| `<list>` | Implements a doubly linked list container. | `std::list`, `push_back`, `pop_back`, `emplace`, `remove` |
| … |  |  |

## References

- https://en.cppreference.com/w/cpp/standard_library