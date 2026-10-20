# 🛠️ Python: Tooling & Ecosystem

> 

## **Python Virtual Environment**

> **..**  (pyenv)
> 

## Serialization

> 

### Manual

```python

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Dictionary to deserialize
data = {"name": "Alice", "age": 30}

# Deserialize into an object
obj = MyClass(**data)

print(obj.name)  # Output: Alice
print(obj.age)   # Output: 30

```

### Using `setattr` for Dynamic Attributes

```python
class MyClass:
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)

# Dictionary to deserialize
data = {"name": "Alice", "age": 30, "location": "New York"}

# Deserialize into an object
obj = MyClass(data)

print(obj.name)      # Output: Alice
print(obj.location)  # Output: New York
```

### Using `dataclasses`

```python
from dataclasses import dataclass

@dataclass
class MyClass:
    name: str
    age: int

# Dictionary to deserialize
data = {"name": "Alice", "age": 30}

# Deserialize into an object
obj = MyClass(**data)

print(obj.name)  # Output: Alice
print(obj.age)   # Output: 30
```

### Using `jsonpickle` for Complex Cases

```python
import jsonpickle

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Serialize
obj = MyClass("Alice", 30)
serialized = jsonpickle.encode(obj)

# Deserialize
deserialized_obj = jsonpickle.decode(serialized)

print(deserialized_obj.name)  # Output: Alice
```

## Type System

> Python's type system has evolved significantly with the introduction of **type hints**
 (PEP 484) and tools for static and runtime type checking. This guide 
covers key tools and libraries to help you work effectively with 
Python's type system.
> 

> Linter: …
> 

### **Static Type Checkers**

> Static type checkers analyze your code without running it to catch type-related errors early.
> 

> `mypy your_script.py`
> 

> `pyright your_script.py`
> 

> `pyre check`
> 

```bash
def greet(name: str) -> str:
    return "Hello, " + name

greet(42)  # mypy will catch this error: Argument 1 to "greet" has incompatible type "int"; expected "str"
```

### **Runtime Type Validation**

> A library for data validation and settings management using Python type annotations.
> 

```bash
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Alice", age=30)  # Valid
user = User(name="Bob", age="thirty")  # Raises ValidationError
```

```bash
from typeguard import typechecked

@typechecked
def greet(name: str) -> str:
    return "Hello, " + name

greet(42)  # Raises TypeError: type of argument "name" must be str; got int instead
```

## Program Analysis

> See more in [Program Analysis](note.html?n=technica/computation/miscelanea/program-analysis.md).
> 

| **Category** | **Tool** | **Description** | **Usage Example** |
| --- | --- | --- | --- |
| **Linting** | `pylint` | Checks for errors, enforces coding standards, and provides code quality metrics. | `pylint your_script.py` |
|  | `flake8` | Combines linting with style checking (PEP 8 compliance). | `flake8 your_script.py` |
|  | `black` | A code formatter that enforces a consistent style. | `black your_script.py` |
| **Static Type Checking** | `mypy` | Static type checker for Python, enforcing type hints. | `mypy your_script.py` |
|  | `pyright` | Fast static type checker with advanced features. | `pyright your_script.py` |
|  | `pyre` | Static type checker optimized for large codebases. | `pyre check` |
| **Code Formatting** | `autopep8` | Automatically formats Python code to conform to PEP 8. | `autopep8 --in-place your_script.py` |
|  | `yapf` | A formatter based on Google's style guide. | `yapf -i your_script.py` |
| **Security Analysis** | `bandit` | Finds common security issues in Python code. | `bandit -r your_project/` |
|  | `safety` | Checks for known vulnerabilities in dependencies. | `safety check` |
| **Dependency Management** | `pip-audit` | Audits Python environments for dependencies with known vulnerabilities. | `pip-audit` |
|  | `dephell` | Manages dependencies and converts between formats (e.g., `pip` to `poetry`). | `dephell deps convert --from=requirements.txt --to=pyproject.toml` |
| **Code Complexity** | `radon` | Analyzes code complexity (e.g., cyclomatic complexity). | `radon cc your_script.py` |
|  | `wily` | Tracks and visualizes code complexity over time. | `wily build your_project/` |
| **Test Coverage** | `coverage.py` | Measures code coverage during test execution. | `coverage run -m pytest` then `coverage report` |
|  | `pytest-cov` | Integrates coverage reporting with `pytest`. | `pytest --cov=your_module tests/` |
| **Documentation** | `pydocstyle` | Checks compliance with Python docstring conventions (e.g., PEP 257). | `pydocstyle your_script.py` |
|  | `sphinx` | Generates documentation from docstrings. | `sphinx-build -b html sourcedir/ builddir/` |
| **Runtime Analysis** | `pyinstrument` | Profiles Python code to identify performance bottlenecks. | `pyinstrument your_script.py` |
|  | `cProfile` | Built-in profiler for analyzing runtime performance. | `python -m cProfile your_script.py` |
| **Code Quality** | `sonar-scanner` | Integrates with SonarQube for comprehensive code quality analysis. | `sonar-scanner` |
|  | `codeclimate` | Provides automated code review and quality metrics. | `codeclimate analyze` |
| **Dependency Analysis** | `pipdeptree` | Displays installed packages as a dependency tree. | `pipdeptree` |
|  | `pydeps` | Visualizes dependencies between Python modules. | `pydeps your_module/` |

## Performance Analysis

> 

| **Tool** | **Description** | **Usage Example** |
| --- | --- | --- |
| **cProfile** | Built-in profiler for analyzing runtime performance. | `python -m cProfile your_script.py` |
| **pyinstrument** | A statistical profiler that provides a simple, high-level view of performance. | `pyinstrument your_script.py` |
| **line_profiler** | Line-by-line profiling to identify bottlenecks in specific functions. | Decorate functions with `@profile`, then run: `kernprof -l -v your_script.py` |
| **memory_profiler** | Tracks memory usage line-by-line in Python code. | Decorate functions with `@profile`, then run: `python -m memory_profiler your_script.py` |
| **scalene** | A high-performance CPU, GPU, and memory profiler for Python. | `scalene your_script.py` |
| **yappi** | Yet Another Python Profiler, supporting multithreading and coroutine profiling. | `yappi -c your_script.py` |
| **Py-Spy** | A sampling profiler that can profile running Python programs without modifying code. | `py-spy top -- python your_script.py` |
| **snakeviz** | A browser-based visualization tool for profiling data (works with `cProfile`). | `python -m cProfile -o output.prof your_script.py` then `snakeviz output.prof` |
| **gprof2dot** | Converts profiling output into a visual call graph. | `python -m cProfile -o output.prof your_script.py` then `gprof2dot -f pstats output.prof |
| **vprof** | A visual profiler providing interactive charts for CPU, memory, and more. | `vprof -c c your_script.py` |
| **objgraph** | Visualizes object references and memory leaks in Python. | `objgraph.show_refs(your_object)` |
| **pympler** | Tracks memory usage and object lifetimes. | `from pympler import tracker; tr = tracker.SummaryTracker()` |
| **tuna** | A graphical tool for visualizing profiling data. | `python -m cProfile -o output.prof your_script.py` then `tuna output.prof` |

References:

- https://github-pages.arc.ucl.ac.uk/python-tooling/
- https://jiffyclub.github.io/snakeviz/
- https://switowski.com/blog/how-to-benchmark-python-code/

## Documentation

> 

## Package Manager

> [uv](note.html?n=technica/computation/system/operation/operation-conceptual-model/uv.md)
> 

> pip - https://pip.pypa.io/en/stable/
> 

> https://github.com/tox-dev/pipdeptree - A command line utility to display dependency tree of the installed Python packages .
> 

## References

- [Pygame](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/pygame.md)
- https://realpython.com/python-virtual-environments-a-primer/
- https://docs.python.org/3/library/contextlib.html
- 
- https://flake8.pycqa.org/en/latest/
- https://www.pylint.org/
- https://pypi.org/project/scspell3k/