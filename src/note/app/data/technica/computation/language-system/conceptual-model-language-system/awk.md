---
tags: [language]
---

# AWK


> AWK (Aho - Weinberger - Kernighan). AWK is a DSL(Domain-specific language) design for text processing.
> 

## Model of Computation

> How does `AWK` encodes **computations**?
> 

> Thus, AWK can be viewed as a **record-oriented stream-processing machine**. Its fundamental unit of computation is not an arbitrary character sequence or a data structure in memory, but an **input record together with its fields**.
> 

### Language Spec

> Note: `{ rule }` means  `rule{0, n}`.
> 

```jsx
program      ::= { rule } ;

rule         ::= begin_rule | end_rule | pattern_rule ;

begin_rule   ::= "BEGIN" action ;
end_rule     ::= "END" action ;
pattern_rule ::= [ pattern ] action ;

action       ::= "{" { statement } "}" ;

pattern      ::= expression
               | regex
               | pattern "," pattern ;

statement    ::= expression
               | "print" [ expression_list ]
               | "printf" expression_list
               | "if" "(" expression ")" statement [ "else" statement ]
               | "while" "(" expression ")" statement
               | "for" "(" expression ";" expression ";" expression ")" statement
               | "for" "(" variable "in" array ")" statement
               | "next"
               | "exit"
               | "return" [ expression ] ;

expression   ::= literal
               | variable
               | field
               | function_call
               | expression operator expression
               | unary_operator expression
               | "(" expression ")" ;

field        ::= "$" expression ;

variable     ::= identifier ;

array        ::= variable "[" expression "]" ;

function_call ::= identifier "(" [ expression_list ] ")" ;

expression_list ::= expression { "," expression } ;

operator     ::= "+" | "-" | "*" | "/" | "%" | "^"
               | "==" | "!=" | "<" | ">" | "<=" | ">="
               | "~" | "!~"
               | "&&" | "||"
               | "=" | "+=" | "-=" | "*=" | "/=" ;

literal      ::= number | string ;
```

### Interpreter Model

> How does the descriptions become computation?
> 

> Note: **AWK** executes all `BEGIN` rules once in their source order, then evaluates all pattern rules in their source order for each input record, and finally executes all `END` rules once in their source order.
> 

```jsx
program = parse(source)

begin_rules   = rules of type BEGIN
pattern_rules = rules of type PATTERN
end_rules     = rules of type END

state = initialize_program_state()

# Phase 1: initialization
for rule in begin_rules:
    execute(rule.action, state)

# Phase 2: input processing
for record in input:

    state.record = record
    state.fields = split(record, state.FS)
    state.NF     = number_of(state.fields)

    for rule in pattern_rules:

        if evaluate(rule.pattern, state) == true:
            execute(rule.action, state)

# Phase 3: finalization
for rule in end_rules:
    execute(rule.action, state)
```

**Graphical View:**

```jsx
AWK Source
    │
    ▼
Parse
    │
    ▼
Rules
    │
    ├───────────────┐
    ▼               ▼
BEGIN rules    Pattern rules    END rules
    │               │               │
    ▼               ▼               ▼
initialize       process          finalize
state            records           state
                    │
                    ▼
              for each record
                    │
              ┌─────┴─────┐
              ▼           ▼
          evaluate      execute
           pattern       action
```

### Which are the AWK Linguistic Abstractions?

| Abstraction | Description | Role |
| --- | --- | --- |
| **Input Record** | A unit of input, normally one line of text | Defines the basic unit being processed |
| **Field** | A component of an input record, normally separated by whitespace or `FS` | Provides structured access to parts of a record |
| **Record** | The current input unit represented by `$0` | Gives access to the complete input element |
| **Pattern** | A boolean condition, regular expression, range, or expression that selects records | Determines **when** an action executes |
| **Action** | A sequence of statements enclosed in `{ ... }` | Specifies **what** to do with selected records |
| **Rule** | `pattern { action }` | Couples selection with transformation |
| **Expression** | A value-producing computation | Represents conditions, values, and computations |
| **Variable** | A named mutable value | Stores state during processing |
| **Array** | An associative mapping from keys to values | Represents collections, counters, indexes, and maps |
| **Operator** | An operation over values, e.g. `+`, `~`, `==`, `&&` | Builds computations and conditions |
| **Function** | A named computation, built-in or user-defined | Encapsulates reusable behavior |
| **Control Structure** | `if`, `while`, `for`, `for (k in array)` | Controls execution flow |
| **Output** | `print` and `printf` operations | Produces transformed or derived text |
| **Built-in Variable** | Variables such as `NF`, `NR`, `FNR`, `FS`, `OFS`, `RS`, `ORS` | Exposes the state/configuration of the text-processing machine |
| **Built-in Function** | Functions such as `length()`, `split()`, `substr()`, `match()` | Provides common text and data operations |
| **Regular Expression** | A pattern describing a class of strings | Provides textual matching and selection |
| **Record/Field Separators** | `RS`, `FS`, `OFS`, `ORS` etc. | Define how text is structurally interpreted |
| **Program State** | Variables, arrays, counters, and built-in state accumulated across records | Enables aggregation and computation across the input |
| **BEGIN/END Phase** | Special actions executed before input processing and after it finishes | Supports initialization and final aggregation/output |

## What is the record state in AWK?

```jsx
record_state = {
    $0       : current record
    $1..$NF  : current fields
    NF       : number of fields
    NR       : current record number
    FNR      : record number within current file
    FILENAME : current input file
}
```

\

## Which are the functions provided by `AWK`?

| Category | Function | Purpose |
| --- | --- | --- |
| **String** | `length(s)` | Length of a string |
|  | `substr(s, m, n)` | Extract substring |
|  | `index(s, t)` | Find substring position |
|  | `tolower(s)` | Convert to lowercase |
|  | `toupper(s)` | Convert to uppercase |
| **Regex / text** | `match(s, r)` | Find regex match |
|  | `sub(r, t, s)` | Replace first match |
|  | `gsub(r, t, s)` | Replace all matches |
|  | `split(s, a, sep)` | Split string into array |
| **Input** | `getline` | Read an input record |
| **Output** | `print` | Output values *(technically a statement, not a function)* |
|  | `printf` | Formatted output *(statement)* |
| **Numeric** | `int(x)` | Integer portion |
|  | `sqrt(x)` | Square root |
|  | `exp(x)` | Exponential |
|  | `log(x)` | Natural logarithm |
|  | `sin(x)` | Sine |
|  | `cos(x)` | Cosine |
|  | `atan2(y,x)` | Two-argument arctangent |
| **Random** | `rand()` | Pseudorandom number |
|  | `srand(x)` | Set random seed |
| **System** | `system(command)` | Execute a shell command |
| **Time** | `mktime(s)` | Convert timestamp string to epoch time |
|  | `strftime(f,t)` | Format epoch time |
|  | `systime()` | Current epoch time |

## How to used `printf`?

> `printf` outputs formatted text according to a **format string** and a sequence of **arguments**. Unlike `print`, `printf` does **not** automatically append a newline.
> 

> `printf "format specifier", expression1, expression2, ..`
> 

> Can we have multiple format specifier and positions? Yes. `printf` can have **multiple format specifiers**, and each specifier consumes the corresponding argument **from left to right**.
> 

> `printf "%s %d %.2f\n", $1, $2, $3` .
> 

Format Specifier:

| Specifier | Value |
| --- | --- |
| `%s` | String |
| `%d` | Integer |
| `%f` | Floating-point number |
| `%.2f` | Floating-point number with 2 decimals |
| `%e` | Scientific notation |
| `%g` | Compact floating-point representation |
| `%%` | Literal `%` |

## Which are the most relevant one liners that covers the majority of the used cases?

| Pattern | What it does | Example |
| --- | --- | --- |
| `awk '{print $1}' file` | Extract a field | First column |
| `awk '{print $1, $3}' file` | Extract multiple fields | Columns 1 and 3 |
| `awk '{print $NF}' file` | Last field | Last column |
| `awk 'NF > 3' file` | Filter records | Lines with >3 fields |
| `awk '$3 > 100' file` | Filter by field value | Third field > 100 |
| `awk '$1 == "foo"' file` | Filter by exact value | First field is `foo` |
| `awk '/pattern/' file` | Filter by regex | Lines containing pattern |
| `awk '{sum += $3} END {print sum}' file` | Aggregate | Sum column 3 |
| `awk '{sum += $3} END {print sum/NR}' file` | Average | Average column 3 |
| `awk '{count[$1]++} END {for (x in count) print x, count[x]}' file` | Count by value | Frequency table |
| `awk '{print $1}' file | sort | uniq` | Extract + external processing | Unique values |
| `awk 'NR==1' file` | First record | First line |
| `awk 'NR==10' file` | Specific record | Line 10 |
| `awk 'NR > 1' file` | Skip first line | Remove header |
| `awk 'NF' file` | Remove blank lines | Non-empty lines |
| `awk 'BEGIN {...} ... END {...}' file` | Initialization/finalization | Headers, totals |

## References

- [AWK](https://en.wikipedia.org/wiki/AWK)
- [Awk: The Power and Promise of a 40-Year-Old Language](https://www.fosslife.org/awk-power-and-promise-40-year-old-language)
- [A Guide to Study Programming Language](https://app.notion.com/p/A-Guide-to-Study-Programming-Language-5a6ed523a0a94f619061f4051dcca041?pvs=21)
- [https://www.pement.org/awk/awk1line.txt](https://www.pement.org/awk/awk1line.txt)
- https://github.com/FreedomBen/awk-hack-the-planet