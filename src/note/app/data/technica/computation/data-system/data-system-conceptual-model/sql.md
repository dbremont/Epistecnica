---
tags: [query-language]
---

# SQL

- [Query Language](note.html?n=technica/computation/data-system/data-system-conceptual-model/query-language.md)

> SQL (Structured Query Language) is a programming language used to manage and manipulate relational databases.
> 

![Untitled](data/technica/computation/data-system/data-system-conceptual-model/assets/sql/untitled.png)

## Language Specification

| Part (Category) | Statement | Description | Semantics | Year in Standard |
| --- | --- | --- | --- | --- |
| **DDL – Data Definition Language** | `CREATE` | Defines a new database object (table, view, index, schema, etc.). | Declarative definition of structure. | 1986 (SQL-86) |
|  | `ALTER` | Modifies an existing database object. | Declarative modification of schema. | 1986 (SQL-86) |
|  | `DROP` | Deletes a database object. | Declarative removal of structure. | 1986 (SQL-86) |
|  | `VIEW` | Defines a virtual table based on a query. | Declarative query encapsulation. | 1986 (SQL-86) |
|  | `MATERIALIZED VIEW` | Defines a stored result of a query for faster access. | Declarative precomputation and persistence. | 1999 (SQL:1999) |
|  | `STORED PROCEDURE` | Encapsulates procedural logic inside the database. | Procedural abstraction within DB. | 1992 (SQL-92) |
|  | `TEMPORAL TABLE` | Maintains historical versions of data with system time. | Declarative time-based data management. | 2016 (SQL:2016) |
|  | `TRIGGER` | Executes automatically in response to events (insert, update, delete). | Event-driven procedural execution. | 1994 (SQL:1999) |
| **DQL – Data Query Language** | `SELECT` | Retrieves data from one or more tables/views. | Declarative query (logical/relational calculus semantics). | 1986 (SQL-86) |
|  | `OUTER JOIN` | Joins rows even when no match exists in one table. | Declarative relational extension of join semantics. | 1999 (SQL:1999) |
|  | `WITH (CTE)` | Defines a common table expression for reuse within a query. | Declarative temporary view inside query scope. | 1999 (SQL:1999) |
|  | `RECURSIVE QUERY` | Allows queries to reference themselves (recursive CTEs). | Declarative recursion in relational queries. | 2003 (SQL:2003) |
|  | `WINDOW FUNCTION` | Performs calculations across sets of rows related to the current row. | Declarative analytic extension. | 2003 (SQL:2003) |
|  | `ANALYTIC FUNCTION` | Advanced aggregations (e.g., ranking, moving averages). | Declarative statistical/analytical semantics. | 2003 (SQL:2003) |
|  | `PIVOT` | Rotates data from rows into columns. | Declarative restructuring of result sets. | 2003 (SQL:2003) |
|  | `CROSS APPLY` | Applies a table-valued function for each row (vendor-specific). | Procedural row-wise function application (non-standard). | Non Standard |
|  | ORDER BY | Sorts the result set by one or more columns. | Declarative ordering of query results. | 1986 (SQL-86) |
|  | FETCH - OFFSET | Limits the number of rows returned and skips initial rows. | Declarative pagination. | 2008 (SQL:2008) |
|  | INTO | Stores query results into a new table or variable. | Declarative result capture. | 1986 (SQL-86) |
| **DML – Data Manipulation Language** | `INSERT` | Adds new rows into a table. | Declarative data insertion (changes database state). | 1986 (SQL-86) |
|  | `UPDATE` | Modifies existing rows in a table. | Declarative data modification (changes database state). | 1986 (SQL-86) |
|  | `DELETE` | Removes rows from a table. | Declarative deletion (changes database state). | 1986 (SQL-86) |
|  | `MERGE` | Combines insert, update, and delete in one statement. | Declarative conditional manipulation. | 2003 (SQL:2003) |
| **DCL – Data Control Language** | `GRANT` | Provides privileges to users/roles. | Declarative assignment of rights. | 1992 (SQL-92) |
|  | `REVOKE` | Removes privileges from users/roles. | Declarative removal of rights. | 1992 (SQL-92) |
| **TCL – Transaction Control Language** | `COMMIT` | Saves all changes in the current transaction. | Procedural finalization of transaction. | 1992 (SQL-92) |
|  | `ROLLBACK` | Undoes changes in the current transaction. | Procedural undo of transaction state. | 1992 (SQL-92) |
|  | `SAVEPOINT` | Sets a point in a transaction to roll back to. | Procedural checkpoint. | 1999 (SQL:1999) |
|  | `SET TRANSACTION` | Configures transaction properties (isolation, read/write mode). | Procedural setup of transaction behavior. | 1992 (SQL-92) |

## Type System

| Category | Type | Description | Support (SQL Standard) |
| --- | --- | --- | --- |
| **Numeric** | `INT` | Integer numeric type, implementation-dependent size. | SQL-86 |
|  | `SMALLINT` | Small-range integer type. | SQL-86 |
|  | `BIGINT` | Large-range integer type. | SQL:1999 |
|  | `DECIMAL` | Exact numeric type with user-defined precision and scale. | SQL-86 |
|  | `NUMERIC` | Exact numeric type, similar to `DECIMAL`, guaranteed exact precision. | SQL-86 |
|  | `FLOAT` | Approximate numeric type, precision implementation-defined. | SQL-86 |
|  | `REAL` | Approximate numeric type (single precision). | SQL-86 |
|  | `DOUBLE PRECISION` | Approximate numeric type (double precision). | SQL-86 |
| **Character / String** | `CHAR` | Fixed-length character string. | SQL-86 |
|  | `VARCHAR` | Variable-length character string. | SQL-92 |
|  | `TEXT` | Large variable-length string, non-standard (vendor-specific, e.g. PostgreSQL). | Non-standard |
|  | `CLOB` | Character Large Object for large text storage. | SQL:1999 |
| **Date / Time** | `DATE` | Calendar date (year, month, day). | SQL-92 |
|  | `TIME` | Time of day (hour, minute, second, fractional second). | SQL-92 |
|  | `TIMESTAMP` | Date and time combination. | SQL-92 |
|  | `INTERVAL` | Span of time (difference between dates/times). | SQL-92 |
| **Boolean** | `BOOLEAN` | Logical type with values TRUE, FALSE, UNKNOWN. | SQL:1999 |
| **Binary** | `BINARY` | Fixed-length binary data. | SQL:1999 |
|  | `VARBINARY` | Variable-length binary data. | SQL:1999 |
|  | `BLOB` | Binary Large Object for large binary storage. | SQL:1999 |
| **Other / Specialized** | `XML` | XML data type for structured XML storage. | SQL:2003 |
|  | `ARRAY` | Ordered collection of elements of a specific type. | SQL:1999 |
|  | `JSON` | JSON data type for structured JSON storage. | SQL:2016 |

### **Character**

| Database | String Sensitivity | Quote Type |
| --- | --- | --- |
| MySQL | Case-insensitive by default, can be made case-sensitive with configuration changes | Single quotes (`'`) |
| PostgreSQL | Case-sensitive by default, can be made case-insensitive with configuration changes | Single quotes (`'`) or double quotes (`"`) |
| SQL Server | Case-insensitive by default, can be made case-sensitive with configuration changes | Single quotes (`'`) or double quotes (`"`) |
| Oracle | Case-sensitive | Single quotes (`'`) or double quotes (`"`) |
| SQLite | Case-insensitive | Single quotes (`'`) or double quotes (`"`) |
| IBM DB2 | Case-insensitive by default, can be made case-sensitive with configuration changes | Single quotes (`'`) |
| MariaDB | Case-insensitive by default, can be made case-sensitive with configuration changes | Single quotes (`'`) |
| Amazon Redshift | Case-sensitive by default, cannot be made case-insensitive | Single quotes (`'`) or double quotes (`"`) |
| MongoDB | Case-sensitive | Single quotes (`'`) or double quotes (`"`) |

Operations:

- **Concatenation**: Joining two or more strings together using the CONCAT function or the || operator.
- **Substring extraction**: Extracting a string portion using the SUBSTRING or SUBSTR function.
- **String length**: Determining the length of a string using the LENGTH or LEN function.
- **String case modification**: Changing the case of a string using the UPPER, LOWER, or INITCAP functions.
- **String replacement**: Replacing all occurrences of a substring in a string using the REPLACE function.
- **Pattern matching**: Finding strings that match a certain pattern using the LIKE operator or regular expressions.
- **Trimming**: Removing whitespace or other characters from the beginning or end of a string using the TRIM, LTRIM, or RTRIM function.

### Date / Datetime

Here are some common datetime operations that can be performed in SQL:

- **Current datetime**: Retrieving the current date and time using the `CURRENT_TIMESTAMP` or `NOW()` function.
- **Date extraction**: Extracting a portion of a date or time, such as the year, month, or day, using the `EXTRACT` function.
- **Date arithmetic**: Performing arithmetic operations on dates, such as adding or subtracting days or months, using the DATEADD or DATEDIFF functions.
- **Date formatting**: Formatting a date or time value as a string using the `TO_CHAR` or `FORMAT` function.
- **Date comparison**: Comparing two date or time values using operators such as `<`, `>`, `<=`, `>=`, `=`, or `<>`.
- **Date conversion**: Converting a date or time value from one data type to another using the `CAST` or `CONVERT` function.
- **Timezone handling**: Adjusting datetime values to a different timezone using the AT `TIMEZONE` function.

### Null Value

> In SQL, NULL is a unique marker that indicates that a data value does not exist in the database. NULL is not the same as an empty string, blank space, or zero; it is a unique value that signifies the absence of a value.
> 

> Null values can be tricky because they don’t behave like other data types. For example, any arithmetic operation involving a NULL value will always return a NULL result, and logical operations with NULL values may also behave unexpectedly.
> 

> SQL provides several functions to handle null values, such as IS NULL, IS NOT NULL, COALESCE, and NULLIF. These functions allow developers to check for, replace, or manipulate null values as needed. Additionally, using NULL in table columns must be carefully considered during database design to ensure that it does not cause unexpected behavior or affect data integrity.
> 

## Window Function

> Performs a “sliding” calculation across a set of related tuples.
> 

> Like an aggregation but tuples are not grouped into a single output tables.
> 

```sql
<window_function>([expression]) 
OVER (
    [PARTITION BY partition_expression [, ...]]
    [ORDER BY sort_expression [ASC | DESC] [, ...]]
    [frame_clause]
)
```

### Function

- **ROW_NUMBER**: Assigns a unique number to each row within a result set.
- **RANK**: Assigns a rank to each row based on the values in one or more columns.
- **DENSE_RANK**: Similar to RANK, but assigns consecutive ranks to rows with the same values.
- **NTILE**: Divides a result set into a specified number of groups, and assigns a group number to each row.
- **LEAD**: Returns the value of a column from the next row in the result set.
- **LAG**: Returns the value of a column from the previous row in the result set.
- **FIRST_VALUE**: Returns the first value of a column in the result set.
- **LAST_VALUE**: Returns the last value of a column in the result set.
- **SUM, AVG, MIN, MAX**: Calculates aggregate values over a window of rows, rather than the entire result set.

### Partition By

> Divides the result set into partitions (like a `GROUP BY`, but without collapsing rows).
> 

### **Order By**

> Specifies the order in which rows are processed within each partition.
> 

### **Frame Clause (Optional)**

Further restricts the set of rows used for each calculation.

Frame options:

- **RANGE**: Based on logical values (e.g., RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
- **ROWS**: Based on physical row positions
- **GROUPS**: Based on peer groups with the same ordering value

## Query (Select)

### Form

A `SELECT` query retrieves data from one or more tables or views in a relational database. The general syntax is:

```sql
SELECT [DISTINCT] column1, column2, ...
FROM table_name
[JOIN table2 ON condition]
[WHERE condition]
[GROUP BY column]
[HAVING condition]
[ORDER BY column [ASC|DESC]]
[LIMIT n];

```

**Components:**

- `SELECT`: Lists columns or expressions to return.
- `DISTINCT`: Optional; eliminates duplicate rows.
- `FROM`: Specifies the source table(s) or view(s).
- `JOIN`: Optional; combines rows from multiple tables.
- `WHERE`: Optional; filters rows based on a condition.
- `GROUP BY`: Optional; aggregates data by columns.
- `HAVING`: Optional; filters groups after aggregation.
- `ORDER BY`: Optional; sorts the result set.
- `LIMIT`: Optional; restricts the number of rows returned.

### Execution Order

SQL execution order differs from the written syntax. The logical processing order is:

1. **FROM / JOIN** → Combine and identify source tables.
2. **WHERE** → Filter rows before grouping.
3. **GROUP BY** → Aggregate rows into groups.
4. **HAVING** → Filter groups after aggregation.
5. **SELECT** → Choose columns or expressions to return.
6. **DISTINCT** → Remove duplicates from the result.
7. **ORDER BY** → Sort the final result set.
8. **LIMIT** → Restrict the number of returned rows.

### Filter Operator

Filter operators are used in the `WHERE` or `HAVING` clauses to restrict which rows or groups are included. Common operators include:

| Operator | Description | Case |
| --- | --- | --- |
| `=` | Equal to | `WHERE age = 30` |
| `<>` / `!=` | Not equal to | `WHERE status <> 'active'` |
| `<` | Less than | `WHERE price < 100` |
| `<=` | Less than or equal | `WHERE quantity <= 50` |
| `>` | Greater than | `WHERE score > 70` |
| `>=` | Greater than or equal | `WHERE rating >= 4` |
| `BETWEEN ... AND ...` | Inclusive range | `WHERE date BETWEEN '2025-01-01' AND '2025-06-30'` |
| `IN (...)` | Value is in a list | `WHERE category IN ('A','B','C')` |
| `NOT IN (...)` | Value is not in a list | `WHERE category NOT IN ('X','Y')` |
| `LIKE` | Pattern matching | `WHERE name LIKE 'J%'` |
| `NOT LIKE` | Pattern does not match | `WHERE name NOT LIKE 'J%'` |
| `IS NULL` | Checks for NULL | `WHERE deleted_at IS NULL` |
| `IS NOT NULL` | Checks for not NULL | `WHERE deleted_at IS NOT NULL` |
| `AND` | Logical AND | `WHERE age > 18 AND status = 'active'` |
| `OR` | Logical OR | `WHERE city = 'Paris' OR city = 'London'` |
| `NOT` | Logical NOT | `WHERE NOT (status = 'inactive')` |
| `EXISTS` | Checks if a subquery returns rows | `WHERE EXISTS (SELECT 1 FROM orders WHERE orders.user_id = users.id)` |
| `ANY` / `SOME` | Compares with any value in a subquery | `WHERE score > ANY (SELECT score FROM exams)` |
| `ALL` | Compares with all values in a subquery | `WHERE score > ALL (SELECT score FROM exams)` |
| ` |  | `or`CONCAT()` |
| `%` | Wildcard for LIKE | `WHERE name LIKE 'A%'` |
| `_` | Single-character wildcard for LIKE | `WHERE name LIKE 'J_n'` |

## Join

> A **join** combines rows from two or more tables based on a related column between them. Joins allow querying across multiple tables in a relational database.
> 

```bash
FROM table1
[INNER | LEFT | RIGHT | FULL | CROSS] JOIN table2
    ON join_condition
```

**Types of Joins**

1. **INNER JOIN** – Returns rows with matching values in both tables.
2. **LEFT (OUTER) JOIN** – Returns all rows from the left table, with matching rows from the right table (NULL if no match).
3. **RIGHT (OUTER) JOIN** – Returns all rows from the right table, with matching rows from the left table (NULL if no match).
4. **FULL (OUTER) JOIN** – Returns all rows from both tables; unmatched rows are NULL on the opposite side.
5. **CROSS JOIN** – Returns the Cartesian product of both tables (all possible combinations).
6. **APPLY** – Conceptually, it behaves like a join, but at the implementation level, it operates more like a row-by-row subquery. [Apply](note.html?n=technica/computation/data-system/data-system-conceptual-model/sql.md).

### Group By

| Function | Description |
| --- | --- |
| `COUNT(column*)` | Returns the number of non-NULL values in a column (or the total row count) |
| `SUM(column)` | Returns the sum of values in a numeric column |
| `AVG(column)` | Returns the average of values in a numeric column |
| `MIN(column)` | Returns the minimum value in a column |
| `MAX(column)` | Returns the maximum value in a column |
| `STDDEV(column)` | Returns the standard deviation of numeric values |
| `VARIANCE(column)` | Returns the variance of numeric values |
| `GROUP_CONCAT(column)` / `STRING_AGG(column, ',')` | Concatenates values from multiple rows into a single string (syntax depends on DBMS) |
| `FIRST_VALUE(column)` | Returns the first value in a group (requires window function syntax in many DBMS) |
| `LAST_VALUE(column)` | Returns the last value in a group (window function) |

### Nested Query

> A **nested query** (or **subquery**) is a query **embedded inside another SQL query**. It can return a single value, a set of values, or a table, and is used to filter, compute, or derive data for the outer query.
> 

Notes:

- Can appear in `SELECT`, `FROM`, or `WHERE` clauses.
- Types of nested queries:
    - **Scalar subquery** → returns a single value.
    - **Column subquery** → returns a single column.
    - **Row subquery** → returns a single row.
    - **Table subquery** → returns a table (used in FROM).

### Lateral Join

> `LATERAL` allows a **subquery in the FROM clause** to reference columns from preceding tables in the same FROM clause. It is similar in behavior to **CROSS APPLY / OUTER APPLY** in SQL Server.
> 

```bash
SELECT ...
FROM table1
[ CROSS | LEFT OUTER ] JOIN LATERAL (subquery referencing table1) alias
ON ...
```

```bash
SELECT e.employee_id, p.project_name
FROM employees e
CROSS JOIN LATERAL (
    SELECT project_name
    FROM projects
    WHERE employee_id = e.employee_id
) p;
```

### Apply

> `APPLY` is a SQL operator that allows a table-valued function or subquery to be **evaluated for each row of an outer table**.
> 

It comes in two forms:

- **CROSS APPLY** – Returns only rows where the function/subquery produces results (like an INNER JOIN).
- **OUTER APPLY** – Returns all rows from the outer table, filling with NULLs if the function/subquery produces no results (like a LEFT JOIN).

```bash
FROM outer_table
[ CROSS | OUTER ] APPLY table_valued_function_or_subquery(outer_table.column_list) AS alias
```

### Output Control

> Output control refers to SQL clauses that **modify how the result set of a query is returned**, including ordering, limiting, or directing the output.
> 

Order by 

> Specifies the sort order of the result set.
> 

```bash
ORDER BY sort_expression [ASC | DESC] [, ...]
```

Fetch

> Limits or paginates rows returned after sorting.
> 

```bash
OFFSET <n> {ROW | ROWS}
FETCH {FIRST | NEXT} <m> {ROW | ROWS} ONLY
```

Into

> Directs the output of a query into a new table or variables (dialect-specific).
> 

```bash
SELECT column_list
INTO target_table
FROM source_table
[WHERE ...];
```

## CTE (Commmon Table Expression)

> A Common Table Expression (CTE) is a temporary named result set that can be referred to within a SELECT, INSERT, UPDATE, or DELETE statement in SQL, allowing complex queries to be broken down into smaller, more manageable pieces.
> 

> Support Recursion.
> 

> Provides a way to write auxiliary statements for use in a larger query. → Think of it like a temp table just for one query.
> 

> Alternative to nested queries and views.
> 

### Evaluation Model

1. Evaluate the non-recursive term. Include those rows in `result table` and `working table`.
2. Until the `working table` is empty:
    - Evaluate the recursive term:
        - Bound the `recursive self reference` to the working table
        - Evaluate
        - Add the results to `result table`.
        - Make `working table` = result of the evaluation.

Case:

```sql
WITH cte(n) AS (      
      select 1 as n 
      from dual        
      UNION ALL
      
      SELECT n + 1
      FROM cte 
      WHERE n < 100
)
SELECT sum(n) FROM t;
```

### Why having an internal model is important?

> In oracle this will generate an error message `SQL Error [32044] [99999]: ORA-32044: cycle detected while executing recursive WITH query`.
> 

> Without the evaluation model, how to interpret this result?
> 

```sql
WITH cte(n) AS (    
  select 1 as n from dual    
  UNION ALL    
  select n from cte where  n < 100)
SELECT n FROM cte;
```

## Pivot

> In SQL, the PIVOT operator is used to transform a set of input values into a pivot table format by rotating rows into columns, and aggregating data based on specified column values, thereby simplifying complex data transformations and analysis. The PIVOT operator was introduced in SQL Server 2005, and later added to the SQL standard in SQL:2003.
> 

**Example**

```sql
WITH CTE (tipo_0, tipo, nombre, valor) AS (
	SELECT 	          'b', 	'a', 	'z', 	23 FROM dual
	UNION ALL SELECT 	'b', 	'a', 	't', 	5  FROM dual
	UNION ALL SELECT 	's',  'a',	'z', 	12 FROM dual
	UNION ALL SELECT 	't', 	'b', 	'y', 	20 FROM dual
	UNION ALL SELECT 	't', 	'b', 	'y', 	20 FROM dual
	UNION ALL SELECT 	't',	'b',	'y',	20 FROM	dual
	UNION ALL SELECT	't', 	'b', 	'y', 	20 FROM dual
)
SELECT 	*
FROM CTE 
PIVOT ( COUNT(CTE.VALOR) FOR nombre IN ('z', 't', 'y'))
```

**Pivot Semantics**

```sql
select first_colunn, [pivot_columns]
from <table>
pivot (
  aggregate_function (<aggregate_column>)    
  for <pivot_column>  
  in (<pivot_value_1>, <pivot_value_2>, <pivot_value_3>, ..., <pivot_value_n>))
```

## API

> SQL is a standard language for managing and querying relational databases. As such, there are many programming APIs available for SQL that provide different levels of abstraction and functionality.
> 

### Implementation

| API Name | Language | Description |
| --- | --- | --- |
| **JDBC (Java Database Connectivity)** | Java | Standard Java API with interfaces and classes to connect to databases, send SQL queries, and retrieve/manipulate data. |
| **ODBC (Open Database Connectivity)** | Cross-language / Platform-independent | Standard API with functions and data types for database access, SQL execution, and data retrieval across many languages. |
| **ADO.NET (ActiveX Data Objects .NET)** | .NET Framework / C# | High-level, object-oriented libraries for managing connections, executing SQL, and working with data in .NET. |
| **PDO (PHP Data Objects)** | PHP | Extension offering a uniform interface to access multiple databases via SQL with classes and methods. |
| **Python DB-API** | Python | Standard API with modules and functions to connect to databases, execute SQL, and manipulate results. |

### Java Database Connectivity (JDBC)

> JDBC (Java Database Connectivity) is a Java API that provides a standard way for Java applications to access and manipulate relational databases using SQL. JDBC is part of the Java Standard Edition (Java SE) and is included in the JDK (Java Development Kit).
> 

| Component | Type | Description |
| --- | --- | --- |
| **DriverManager** | Class | Manages installed JDBC drivers and provides methods to establish connections to a database via JDBC URL. |
| **Connection** | Interface | Represents a connection to a database; provides methods to create statements and manage transactions. |
| **Statement** | Interface | Represents an SQL statement that can be executed. Types include: Statement (simple queries), PreparedStatement (parameterized queries), and CallableStatement (stored procedures). |
| **ResultSet** | Interface | Represents the result of an SQL query; provides methods to iterate over rows and retrieve column values. |
| **ResultSetMetaData** | Interface | Provides metadata about columns in a ResultSet, such as names, types, and sizes. |
| **SQLException** | Class | Represents exceptions occurring during JDBC operations, e.g., failed connection or invalid SQL statements. |

## References

- [Contingency table](https://en.wikipedia.org/wiki/Contingency_table)
- [Cross Tabulation: How It Works and Why You Should Use It](https://humansofdata.atlan.com/2016/01/cross-tabulation-how-why)
- [SQL Server: PIVOT Clause](https://www.techonthenet.com/sql_server/pivot.php)
- [WITH Queries (Common Table Expressions)](https://www.postgresql.org/docs/current/queries-with.html)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [Database SQL Language Reference](https://docs.oracle.com/cd/B28359_01/server.111/b28286/toc.htm)
- [CTE as Lookup Tables](https://news.ycombinator.com/item?id=34346411)
- [Isolation Level](https://www.wikiwand.com/en/Isolation_(database_systems))
- [A Guide to Study Programming Language](https://app.notion.com/p/A-Guide-to-Study-Programming-Language-5a6ed523a0a94f619061f4051dcca041?pvs=21)
- [Relational Data Model](note.html?n=technica/computation/data-system/data-system-conceptual-model/relational-data-model.md)
- Praxis
    - https://www.hackerrank.com/domains/sql
    - https://leetcode.com/studyplan/top-sql-50/
    - https://leetcode.com/studyplan/premium-sql-50/