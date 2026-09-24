# Silberschatz, A., Korth, H. F., & Sudarshan, S. (2011). Database System Concepts.


```python
@article{silberschatz2011database,
  title={Database system concepts},
  author={Silberschatz, Abraham and Korth, Henry F and Sudarshan, Shashank},
  year={2011},
  publisher={McGraw-Hill Education}
}

```

## Notes

---

> This book explores a **data model**—the relational model—and its implementations in DBMSs. A data model defines what data is and how it can be represented, while a DBMS provides the concrete system to store and manipulate data according to that model.
> 

> Why does the relational model prevail—or, more generally, why do data models succeed? Because they **decouple specification from implementation**, allowing data to be represented according to a model while enabling migration across different systems that support the same model.
> 

> Continue HERE [Storage and File Structure](Silberschatz,%20A%20,%20Korth,%20H%20F%20,%20&%20Sudarshan,%20S%20(201%2010e598edb79081d89b18cd2b90790b5d.md).
> 

Key Questions:

- How the DBMS represents the database?
- How the DMBS operates on that database?
- Who can access what?
- How is the system kept consistent under failures?
- How does the system scale?

## Index

## Introduction

> A database-management system (DBMS) is a collection of interrelated data (database) and a set of programs (wrong -  a set of subsystems for …) to access those data.
> 

> A **data model** conceptual framework that defines mechanisms to **represent data**, specify **operations** on that data, and provide a **formal semantics** that gives a precise meaning to the representations and operations. That is; it provides the **semantics of the database**; and  guide the implementation of the DBMS; that must implement the data model.
> 

> **Every data model** is suited to different kinds of data — it’s a two-way match between the nature of the data and the capabilities of the model.
> 

> A **data model** is conceptually similar to a model of computation in programming language theory — it defines the fundamental structures and operations available for representing and manipulating data.
> 

The row data from the domain can be viewed in a **different level of abstractions**:

- **Physical Level** – Describes how the data is actually stored in the database (files, indexes, blocks, pages).
- **Logical / Conceptual Level** – Describes what data is stored and the relationships between them (tables, columns, constraints).
- **View / External Level** – Describes how data is presented to different users or applications (views, subsets, projections).

### Data Model

- **Relational Data Model** – Represents data as relations (tables) with tuples (rows) and attributes (columns); operations are based on relational algebra.
- **Entity–Relationship (E-R) Model** – Represents data conceptually as entities, attributes, and relationships; often used for database design before implementation.
- …

Properties of Relational Representation:

- **Normalization** – Organizing tables to reduce redundancy and avoid update, insertion, and deletion anomalies.
- **Consistency of Representation** – Each relation has a fixed schema with well-defined attributes and value domains.

### DBMS Structure

- Storage Manager
- Query Processor
- Transaction Management
- …

### Normalization

> By normalization we mean a non repetitive - and minimal representation; fundamentally - a well decomposed system.
> 

> A **functional dependency** is a relationship between two sets of attributes in a relation, where the value of one attribute (or set of attributes) **uniquely determines** the value of another attribute (or set of attributes).
> 

> Let $R$ be a relation, and let $X$ and $Y$ be subsets of attributes of $R$.  Then: $X \to Y$ means that **for any two tuples** $t_1, t_2 \in R$:  $t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$. In words: if two tuples have the same values for attributes $X$, they must have the same values for attributes $Y$.
> 

## Introduction to Relational Model

> A **data model** defines *what* data is and *how it can be represented*, while a **DBMS** provides the concrete system to store and manipulate data according to that model.
> 

> Relational algebra is a tool to formalize the operations on the objects that represented the data.
> 

Concepts:

- **Relation:** A table representing a set of entities or relationships. Each relation has a **name** and consists of **tuples** (rows) and **attributes** (columns).
- **Tuple:** A single row in a relation; an ordered set of values corresponding to the attributes.
- **Attribute:** A named column in a relation that represents a property or characteristic of the entity.
- **Domain:** The set of allowable values for a given attribute.
- **Value:** An individual data item from the domain of an attribute; a single element of a tuple.
- **Schema:** The structure of a relation, including its name, attributes, and their domains.
- **Key:** An attribute (or set of attributes) whose values uniquely identify each tuple in a relation.
- **Constraint:** A rule that restricts the data in a relation, such as a key constraint, domain constraint, or referential integrity.

## Introduction to SQL

> A SQL Statement operation on a set of bags; basically in at least one bag; or relation.
> 

> Data Types: …
> 

> Set Operations: …
> 

**Parts of SQL:**

- **Data Definition Language (DDL):** Commands that define or modify the structure of database objects, such as `CREATE`, `ALTER`, and `DROP`.
- **Data Manipulation Language (DML):** Commands that retrieve or modify data, such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.
- **Data Control Language (DCL):** Commands that manage access and permissions, such as `GRANT` and `REVOKE`.
- **Transaction Control Language (TCL):** Commands that manage transactions, such as `COMMIT`, `ROLLBACK`, and `SAVEPOINT`.

## Intermediate SQL

> An exploration on Joins, Views, Materialized Views, Transactions, Constraints, Authorization.
> 

> A Transaction combine a set of statements into an atomic unit of work; that, it’s transactional.
> 

> Note: A individual basic statement, it’s also transactional.
> 

> The authorization model defines who can do what in a database system. Conceptually, we have a set of objects (tables, views, procedures, etc.) and a set of users or roles that interact with those objects. The DBMS enforces these rules automatically, ensuring that all access to database objects complies with the defined authorizations.
> 

## Advanced SQL

> An **exploration of store procedures**, functions, triggers,  recursive queries,  prepared statements, window functions, …
> 

> **Prepared Statements** are a database feature that lets you define a SQL statement once, send it to the database for parsing and optimization, and then execute it multiple times with different parameter values. -**Note my understanding is pretty basic** — but understanding how long a prepared statement remains valid (e.g., per connection, per session) and how to manage them across different connections or connection pools is an important practical detail.
> 

## Formal Relational Query Language

> In this chapter, we take the **Relational Data Model** and develop a formal semantics for it, known as the **Relational Algebra**.
> 

> **Relational Algebra** is a **formal query language** and **algebraic system** for manipulating relations (tables) in the **Relational Model of Data**. It defines a set of **operators** that take one or more relations as input and produce a new relation as output. These operators are **closed** under the algebra, meaning the result of an operation is itself a relation and can be further composed with other operations.
> 

## Database Design and the E-R Model

> Note: This is a **design tool**.
> 

> The **Entity-Relationship (E-R)** Model is a conceptual framework that provides a set of constructs to describe a domain of data. The tools it provides are aimed at modeling entities, attributes, and relationships in a way that captures the real-world structure of the domain, facilitating database design and ensuring consistency, clarity, and completeness before implementation in a relational database.
> 

## Relational Database Design

> What makes a good database design?  How to model **temporal data**?
> 

> This chapters cover a very sophisticated treatment of dependency theory, algorithms to normalized a relation.
> 

| **Category** | **✅ Criteria** | **Description** |
| --- | --- | --- |
| **📋 Requirements** | Understand Use Cases | Identify all operations, reports, queries, and business rules the database must support. |
|  | Gather Constraints | Document regulatory, security, and domain-specific rules affecting the design. |
| **🗂 Data Modeling** | Identify Entities | Recognize all real-world objects or concepts represented in the database. |
|  | Define Attributes | List all relevant properties for each entity and determine their data types. |
|  | Establish Relationships | Map how entities relate (1:1, 1:N, N:N) using ER diagrams or similar models. |
| **🧩 Normalization** | 1NF | Ensure all columns are atomic; no repeating groups or arrays. |
|  | 2NF | All non-key attributes fully depend on the primary key; eliminate partial dependencies. |
|  | 3NF | Remove transitive dependencies; non-key fields depend only on the primary key. |
|  | BCNF (optional) | Strengthened 3NF; every determinant is a candidate key. |
| **🔒 Data Integrity** | Primary Keys | Ensure each table has a unique identifier for its records. |
|  | Foreign Keys | Maintain referential integrity between related tables. |
|  | Constraints | Enforce rules like NOT NULL, UNIQUE, CHECK to prevent invalid data. |
| **⚡ Performance** | Indexing | Create indexes on frequently queried fields to speed up retrieval. |
|  | Partitioning | Split large tables logically to improve performance and manageability. |
|  | Query Optimization | Structure tables and relationships to reduce expensive joins and computations. |
| **🌱 Flexibility** | Modular Design | Keep tables loosely coupled and logically grouped to accommodate future changes. |
|  | Extensible Fields | Plan for optional fields or additional entities to minimize schema refactoring. |
| **📏 Consistency** | Naming Conventions | Use clear, consistent, and meaningful names for tables, columns, and keys. |
|  | Documentation | Maintain schema diagrams, descriptions, and data dictionaries. |
| **🛡 Security** | Access Control | Define user roles and permissions for reading, writing, and modifying data. |
|  | Data Protection | Encrypt sensitive fields and implement auditing where required. |
| **🧰 Maintainability** | Simplicity | Avoid overcomplicated schemas; keep relationships and table structures clear. |
|  | Error Handling | Define defaults, constraints, and validation mechanisms to reduce data errors. |

### Functional Dependency Theory

> See more in [Normalization](Silberschatz,%20A%20,%20Korth,%20H%20F%20,%20&%20Sudarshan,%20S%20(201%2010e598edb79081d89b18cd2b90790b5d.md).
> 

> A **functional dependency (FD)** is a relationship between two sets of attributes in a relational database. It expresses a constraint that the value of one attribute (or set of attributes) **uniquely determines** the value of another attribute (or set of attributes).
> 

> This **grounds the process of normalization**. The procedure is based on a set of **axioms** that guide the transformation of a database schema to reduce redundancy and ensure data integrity. These axioms are collectively known as **Armstrong’s Axioms**, which include rules such as **reflexivity, augmentation, and transitivity**. Additionally, there are related **corollaries and rules**, like the **union rule, decomposition rule, and pseudotransitivity**, which are derived from Armstrong’s Axioms and are used to simplify reasoning about functional dependencies and guide schema decomposition.
> 

**Reflexivity**

- **Rule:** If $Y \subseteq X$, then $X \rightarrow Y$.
- **Meaning:** Every set of attributes functionally determines any of its subsets.

**Augmentation**

- **Rule:** If $X \rightarrow Y$, then $XZ \rightarrow YZ$ for any $Z$.
- **Meaning:** Adding extra attributes to both sides of a dependency preserves the dependency.

**Transitivity**

- **Rule:** If $X \rightarrow Y$ and $Y \rightarrow Z$, then $X \rightarrow Z$.
- **Meaning:** Dependencies can be chained together.

**Derived Rules**

> These are not axioms themselves but can be **derived** from Armstrong’s axioms:
> 
1. **Union Rule:** If $X \rightarrow Y$ and $X \rightarrow Z$, then $X \rightarrow YZ$.
2. **Decomposition Rule:** If $X \rightarrow YZ$, then $X \rightarrow Y$ and $X \rightarrow Z$.
3. **Pseudotransitivity:** If $X \rightarrow Y$ and $WY \rightarrow Z$, then $WX \rightarrow Z$.

### **Temporal Relation Modeling**

> **Temporal Relation Modeling** is the art of capturing **snapshots of a domain over time**. It involves representing how entities, their attributes, and relationships **evolve across different points in time**. Unlike static data models, temporal models allow you to **track historical changes, current states, and even future predictions** within the same framework.
> 

## Application Design and Development

> This chapter is not about DBs; is about the USED of DBs by Programs.
> 

## Storage and File Structure

## Indexing and Hashing

## Query Processing

## Query Optimization

## Transactions

## Concurrency Control

## Recovery System

## Database-System Architectures

## Parallel Databases

## Distributed Databases

## Data Warehousing and Mining

## Information Retrieval

## Object-Based Databases

## XML

## Advanced Application Development

## Spatial and Temporal Data and Mobility

## Advanced Transaction Processing

## PostgreSQL

## Oracle

## IBM DB2 Universal Database

## Microsoft SQL Server

## Detailed University Schema

## References

- https://en.wikipedia.org/wiki/SQLJ
- https://en.wikipedia.org/wiki/Database_theory
- https://en.wikipedia.org/wiki/Chase_(algorithm)
- https://en.wikipedia.org/wiki/Functional_dependency
- https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model
- https://db-book.com/
- Chen, Peter (March 1976). "The Entity-Relationship Model - Toward a Unified View of Data". ACM Transactions on Database Systems. 1 (1): 9–36. CiteSeerX 10.1.1.523.6679. doi:10.1145/320434.320440. S2CID 52801746.
