---
tags: [data-model]
---

# Relational Data Model

- [Relational Data System](note.html?n=technica/computation/data-system/data-system-conceptual-model/relational-data-system.md)

> The **relational data model** is a conceptual framework that defines mechanisms to **represent data**, specify **operations** on that data, and provide a **formal semantics** that gives a precise meaning to the representations and operations.
> 

> A data model can be captured by **⟨Representation, Operations, Semantics⟩**, such that the representation defines the data structure, operations specify valid manipulations, and semantics assign precise meaning to both.
> 

> **Model of Computation:** Declarative. Interestingly, relational algebra is often described as procedural, which, in my view, is a misleading characterization.
> 

## Representation

> Which do the concepts provide by the model to describe …?
> 

- **A relation** is an unordered set that contain the relationship of attributes that represents entities.
- A **Tuple** is a set of attributes values (aka its domain) in the relation.
- **Primary Key:**  A mechanism to uniquely identify a tuple in a relation.
- **Foreign Key:** A mechanism that specifies that a column in one relation maps to a tuple in another relation.
- **Constraints**:  Mechanism  by which the user defines the conditions that must hold in any instance (state) of the database.

### Relation

> **A relation** is an unordered set that contains the relationship of attributes that represent entities. Mathematically, it is **bags** (duplicates), not sets (no duplicates).
> 
- **A type** is a set of attribute values (its domain) in the relation. Values are normally atomic or scalar. The unique value `NULL` is a member of every domain (if allowed).
- **Primary Key**: This uniquely identifies a single tuple. Usually, each DBMS has its way of auto-generating primary key integers.
- **Foreign key**: A foreign key is a column or attribute referencing a row in another table or relation.
- **Atomic Type**: A type is considered atomic if its values are inseparable.
- **Composite Type**: A type is considered composed if its values are divisible.

### **Constraint**

> **Constraints**:  Mechanism  by which the user defines the conditions that must hold in any instance (state) of the database.
> 

| **Mechanism** | **Description** |
| --- | --- |
| **Primary Key** | Ensures that each record in a table has a unique identifier. |
| **Foreign Key** | Enforces referential integrity by linking a column to a primary key in another table. |
| **Unique** | Ensures that values in a column or a combination of columns are unique across the table. |
| **Not Null** | Requires that a column cannot have NULL (empty) values. |
| **Check** | Specifies a condition that must be true for each row in the table. |
| **Default** | Provides a default value for a column when no value is specified during insertion. |
| **Index (with constraint)** | Improves query performance while optionally enforcing uniqueness or other integrity rules. |

## Operation

| **Symbol** | **Name** | **Description** |
| --- | --- | --- |
| σ | Select | Filters tuples based on a condition |
| π | Projection | Extracts specific columns from a relation |
| ∪ | Union | Combines tuples from two relations |
| ∩ | Intersection | Finds common tuples between two relations |
| − | Difference | Computes tuples in one relation but not in another |
| × | Product | Cartesian product of two relations |
| ⋈ | Join | Combines tuples based on a related attribute |
| τ | Sort / Order By | Orders tuples based on one or more attributes |
| δ | Duplicate Elimination | Removes duplicate tuples from a relation |
| γ | Aggregation / Group By | Groups tuples and computes summary functions (e.g., SUM, COUNT) |

## Algebra

> aka. Semantics.
> 

> Algebra = (Set of Objects, Operations, Axioms).
> 

> **Relational Algebra** is a formal system for **querying and manipulating relational data**. It provides a set of **operations on relations (tables)** that produce new relations as results.
> 

> **Relational algebra** is called **"procedural"** because it requires the user to provide a sequence of operations, specifying both the operations to perform and the order in which to perform them to obtain a desired result. This approach contrasts with **declarative methods**, where the user specifies only what data to retrieve, not how to retrieve it.
> 

> **Note:** The Relational Algebra essentially provides a formal semantics for the relational data model by defining operations on relations. In this sense, it is closely tied to the relational data model in our framework. However, it can be treated separately because the **data model** itself defines the structure, constraints, and relationships of the data, while **Relational Algebra** focuses on the **operations** that can be performed on that data and their formal meaning.
> 

### Object

> The objects are **relations** (tables) consisting of tuples over attributes.
> 

> See more in [Representation](note.html?n=technica/computation/data-system/data-system-conceptual-model/relational-data-model.md).
> 

### Operator

> The operators are standard relational algebra operations (selection, projection, join, union, etc.) that manipulate relations and produce new relations.
> 

> See more in [Operation](note.html?n=technica/computation/data-system/data-system-conceptual-model/relational-data-model.md).
> 

### Semantic

> Relational algebra operations follow **set-theoretic and algebraic properties**, such as commutativity, associativity, distributivity, idempotence, and closure.
> 
- Operations are **set-theoretic**, producing relations as outputs.
- Provides a **formal mathematical foundation** for query execution in relational databases.
- Forms the **basis for SQL** and other relational query languages.

## Implementation

> **Note:** The relational model is independent of any specific query language implementation. However, the most widely adopted standard query language for relational databases is **SQL (Structured Query Language)**.
> 

> See more in [SQL](note.html?n=technica/computation/data-system/data-system-conceptual-model/sql.md).
> 

## References

- [Algebra](https://app.notion.com/p/Algebra-18fde09aee854bbdaf5008362315f85a?pvs=21)
- [Relational Algebra](https://en.wikipedia.org/wiki/Relational_algebra)
- [Transitive Closure](https://en.wikipedia.org/wiki/Transitive_closure)
- Codd, Edgar Frank. “A relational model of data for large shared data banks.” Communications of the ACM 26.1 (1983): 64-69.