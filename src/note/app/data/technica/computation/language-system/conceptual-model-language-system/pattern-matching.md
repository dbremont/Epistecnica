---
tags: [problem, linguistic-abstraction]
---

# Pattern Matching


> **Pattern Matching** is the process of **comparing a structured input** (such as a string, tree, term, or data structure) against a **pattern**—a template that may include fixed elements, variables, or constraints—to determine if the input **conforms to the pattern's shape or rules**, and optionally to **extract subcomponents** or **bind variables**.
> 

> **La coincidencia de patrones** (*Pattern Matching*) es el proceso de **comparar una entrada estructurada** (como una cadena, árbol, término o estructura de datos) con un **patrón** —una plantilla que puede incluir elementos fijos, variables o restricciones— para determinar si la entrada **se ajusta a la forma o reglas del patrón**, y opcionalmente **extraer subcomponentes o vincular variables**.
> 

## Formulation

> Given:
> 
> - A **subject** $S$ (e.g., string, data structure, term, tree, graph),
> - A **pattern** $P$ (a structural or symbolic template),
> - An optional **set of rules** $R$ (e.g., guards, typing, constraints),

> Determine:
> 
> - Whether $S$ **matches** $P$, and if so,
> - Extract relevant **bindings** or **substructures** from $S$ as defined by $P$.

### 🎯 **Goal**

- **Decision problem**: Does $S$ match $P$? → Boolean
- **Extraction problem**: If match succeeds, what values or structure can be extracted?
- **Search problem**: Find all $S_i \in \mathcal{D}$ such that $M(P, S_i)$ holds

### 🧪 **Pattern Matching Problem**

| Variant | Subject | Pattern | Matching Strategy | Example |
| --- | --- | --- | --- | --- |
| **Exact matching** | Symbol/string | Fixed string | Equality | `S = P` |
| **Regular matching** | String | Regex | Finite automata | `ab*` on `"abbbb"` |
| **Structural matching** | Tree/term | Pattern with variables | Structural equivalence | AST or algebraic data types |
| **Unification** | Logical terms | Terms with variables | Substitution + equality | `f(X) = f(a)` → `{X ↦ a}` |
| **Graph matching** | Graph | Subgraph pattern | Isomorphism | Subgraph isomorphism |
| **Pattern + guard** | Any | Pattern + Boolean | Pattern match + condition | `case x if x > 0 =>` |
|  |  |  |  |  |

## Pattern Taxonomy

| **Pattern Type** | **Structure Matched** | **Used In** | **Match Strategy** | **Examples** |
| --- | --- | --- | --- | --- |
| **Literal Pattern** | Exact values | Regex, string search | Equality | `'abc'`, `42`, `"true"` |
| **Wildcard Pattern** | Any value (anonymous) | Functional programming, regex | Match any (ignore value) | `_` in Haskell/Scala, `.*` in regex |
| **Type Pattern** | Type identity and casting | Java, Scala, ML | Instance check + binding | `case String s -> ...` |
| **Constructor / Structural Pattern** | Decompose structured data | ML, Haskell, Scala | Match data constructors | `Cons(x, xs)`, `Some(x)` |
| **Sequence Pattern** | Ordered collections (lists, arrays) | FP, pattern match libs | Positional match | `[x, y, ...]`, `[_, _, z]` |
| **Tuple Pattern** | Fixed-size product types | Functional languages | Match by position and arity | `(x, y)`, `(_, 0)` |
| **Record / Named Field Pattern** | Labeled fields in a structure | Rust, OCaml, JS (ES6) | Match by field name | `{x: 1, y}` or `{ x = x_val; y = _ }` |
| **Guarded Pattern** | Pattern + condition | Java, Scala, Haskell | Match + boolean check | `case x if x > 0 => ...` |
| **Regex Pattern** | Character sequences with rules | Text processing | DFA/NFA search | `\d+`, `[A-Z]{3}` |
| **Logical Pattern** | Boolean combination of patterns | Pattern languages (Python 3.10+, Rust, Scala) | Match via AND, OR, NOT | `case A(x) |
| **Variable Binding Pattern** | Bind value to a name | Most PLs with matching | Bind and use later | `case Some(x) => ...` |
| **Unification Pattern** | Structural + symbolic equality | Logic programming | Term unification | `likes(john, X)` in Prolog |
| **Symbolic / Algebraic Pattern** | Match math expressions or symbolic forms | Computer algebra systems | Symbolic structure | `a * x^n` in SymPy |
| **Graph Pattern** | Nodes + edges + constraints | Graph query, bioinfo | Subgraph isomorphism | Query pattern in Cypher/SPARQL |
| **Tree Pattern** | Nodes + hierarchical structure | Compilers, XML, ASTs | Tree traversal & match | Match subtree in AST |
| **Bitmask Pattern** | Binary bit patterns | Embedded systems, OS | Bitwise match & mask | `(x & 0xF0) == 0xA0` |
| **Template Pattern** | High-level code or text templates | Code gen, config | Placeholder substitution | `${var}` in YAML/HTML |

## Fuzzy Matching

> Also known as **Approximate Matching**, fuzzy matching is the process of finding patterns in data that do not exactly match the specified pattern but are close according to some similarity metric or tolerance threshold. Unlike exact or structural pattern matching, fuzzy matching allows for errors, differences, or variations such as insertions, deletions, substitutions, or transpositions.
> 

> In many real-world applications, data is noisy, incomplete, or imperfect. Exact pattern matching is often too strict, failing to identify relevant near-matches. Fuzzy matching relaxes the matching criteria to account for variations and errors, enabling robust detection of patterns under uncertainty.
> 

### Common Use Cases

- **Text processing:** Spell checking, OCR post-processing, search engines with typo tolerance, and plagiarism detection.
- **Bioinformatics:** DNA or protein sequence alignment where mutations or sequencing errors exist.
- **Data integration:** Matching records that may contain misspellings or formatting differences.
- **Natural language processing:** Matching entities or phrases with paraphrasing or morphological variation.

### Similarity Metrics and Distance Measures

Fuzzy matching relies on quantifying how close two elements are, using metrics such as:

- **Levenshtein distance (edit distance):** Minimum number of single-character edits (insertions, deletions, substitutions) required to change one string into another.
- **Damerau-Levenshtein distance:** Extends Levenshtein by including transpositions as a single edit.
- **Hamming distance:** Number of differing positions between two strings of equal length.
- **Jaccard similarity:** Measures overlap between sets of tokens or shingles derived from strings.
- **Cosine similarity:** For vector space models of text.

### Algorithms and Approaches

- **Dynamic programming:** Classical algorithms compute edit distances with O(mn)O(mn) complexity for strings of lengths mm and nn.
- **Approximate pattern matching algorithms:** Variations of KMP or automata that allow mismatches or errors within bounds.
- **Filtering techniques:** Use indexing and heuristics to quickly eliminate unlikely candidates before applying expensive matching.
- **Local vs global alignment:** In bioinformatics, algorithms like Smith-Waterman (local) and Needleman-Wunsch (global) find best approximate matches in sequences.

### Computational Complexity

Fuzzy matching is generally more computationally expensive than exact matching. Optimizations include heuristic pruning, indexing structures (e.g., BK-trees, suffix arrays), and parallelism.

## QA

- What is the formal definition of pattern matching in terms of relations or functions? How does it relate to term rewriting and unification?
- How does pattern matching differ from unification? Under what conditions are they equivalent or different?
- What algorithms and data structures enable efficient pattern matching over strings and trees? Compare algorithms like KMP, Boyer-Moore, and tree pattern matching algorithms.
- How do type systems interact with pattern matching? What are exhaustiveness and redundancy checks in pattern matching, and how are they implemented?
- How does the presence of guards or conditions in pattern matching affect the compilation or interpretation of code?
- What are the computational complexities of various pattern matching problems, e.g., string matching, tree matching, and graph matching?
- How is pattern matching implemented in functional programming languages like Haskell or ML? What role do algebraic data types play?
- How do lazy evaluation and pattern matching interact, especially in languages like Haskell?
- What are the semantics of pattern matching in languages that support advanced features like nested patterns, or-patterns, and refutable patterns?
- How do modern imperative languages (e.g., Java, C#) implement pattern matching under the hood, and how does it differ from traditional functional approaches?
- How does pattern matching relate to abstract syntax tree (AST) transformations and compiler optimizations?
- How can pattern matching be extended to support fuzzy or approximate matching? What are the use cases and challenges?
- How do graph pattern matching algorithms differ from tree and string pattern matching? What are their computational challenges?
- In logic programming, how does pattern matching contribute to resolution and proof search?
- What are the trade-offs between declarative pattern matching and imperative conditionals in terms of expressiveness and performance?
- How can pattern matching be used to implement domain-specific languages (DSLs) or embedded languages within a host language?
- How do pattern matching mechanisms support or hinder program verification and static analysis?

## References

- 
- [Pattern Matching](note.html?n=technica/computation/algorithm/conceptual-model-algorithm/pattern-matching.md)
- https://en.wikipedia.org/wiki/Pattern_matching
- https://docs.oracle.com/en/java/javase/17/language/pattern-matching.html
- [‣](https://app.notion.com/p/195598edb7908091a8bed6606187c18d?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081699183e308b3db6c7d?pvs=21)
- [‣](https://app.notion.com/p/10e598edb7908195a56bcbb2524c6c25?pvs=21)
- Robinson, John Alan. "A machine-oriented logic based on the resolution principle." Journal of the ACM (JACM) 12.1 (1965): 23-41.
- Knuth, Donald E., James H. Morris, Jr, and Vaughan R. Pratt. "Fast pattern matching in strings." SIAM journal on computing 6.2 (1977): 323-350.
- Boyer, Robert S., and J. Strother Moore. "A fast string searching algorithm." Communications of the ACM 20.10 (1977): 762-772.
- Hoffmann, Christoph M., and Michael J. O'Donnell. "Pattern matching in trees." Journal of the ACM (JACM) 29.1 (1982): 68-95.
- [Search](note.html?n=technica/computation/algorithm/conceptual-model-algorithm/search.md)
- [Full-Text Search](https://app.notion.com/p/Full-Text-Search-940280495ba1445a82ac28dbddfd435d?pvs=21)
- [Pattern Matching](note.html?n=technica/computation/algorithm/conceptual-model-algorithm/pattern-matching.md)
- [Similarity Search](https://app.notion.com/p/Similarity-Search-fa740c0947624629902569945cbe5cb8?pvs=21)
- [Retrieval System (Search System)](note.html?n=technica/computation/miscelanea/retrieval-system-search-system.md)
- - [Representation Problem: Text (String)]