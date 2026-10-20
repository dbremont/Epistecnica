---
tags: [query-language]
---

# Query Language

- [OData (Open Data Protocol)](note.html?n=technica/computation/data-system/data-system-conceptual-model/odata-open-data-protocol.md), [SQL](note.html?n=technica/computation/data-system/data-system-conceptual-model/sql.md), [GraphQL](note.html?n=technica/computation/data-system/data-system-conceptual-model/graphql.md)

> A **query language** is a formal language used to request, filter, and manipulate data stored in a database or information system. Unlike general-purpose programming languages, query languages are typically **declarative**: they let users specify *what* data they want rather than *how* to retrieve it, leaving the execution strategy to the database engine.
> 

## Query Language Space

| **Category** | **Query Language** | **Description** | **Year** |
| --- | --- | --- | --- |
| Navigational Database | **COBOL DML** | Procedural database access embedded in COBOL programs, particularly for hierarchical and network databases. | 1960s |
| Navigational Database | **IMS DLI** | Procedural language interface for navigating and accessing hierarchical IMS databases. | 1960s |
| Relational Database | **SQUARE** | Experimental IBM language for specifying queries as relational expressions; an early relational query language. | 1971 |
| Relational Database | **SEQUEL** | English-like declarative language developed for IBM System R and the direct predecessor of SQL. | 1972 |
| Relational Database | **QUEL** | Declarative relational query language developed for the Ingres relational database system. | 1974 |
| Relational Database | **SQL** | Declarative language for defining, querying, manipulating, and controlling relational data. | 1974 |
| Commercial Database | **Oracle SQL** | Commercial implementation of SQL introduced with the Oracle relational database system. | 1979 |
| Commercial Database | **IBM SQL / SQL/DS** | IBM's commercial SQL implementation for relational database management. | 1981 |
| Commercial Database | **IBM DB2 SQL** | SQL implementation developed for IBM's DB2 relational database system. | 1983 |
| SQL Standard | **SQL-86** | First ANSI-standardized version of the SQL language. | 1986 |
| SQL Standard | **SQL-89** | Revised SQL standard introducing additional integrity and data-management capabilities. | 1989 |
| SQL Standard | **SQL-92** | Major SQL standard expanding querying, joins, data definition, integrity, and other capabilities. | 1992 |
| Object Database | **OQL** | Declarative query language designed for object-oriented database systems. | 1993 |
| Procedural Database | **PL/SQL** | Oracle's procedural extension of SQL, combining SQL with procedural programming constructs. | 1990s |
| Procedural Database | **T-SQL** | Procedural extension of SQL associated with Sybase and Microsoft SQL Server. | 1990s |
| Multidimensional Database | **MDX** | Query language for retrieving and analyzing data in multidimensional OLAP cubes. | 1997 |
| XML Database | **XPath** | Expression language for navigating and selecting nodes and values within XML trees. | 1999 |
| Semantic Database | **SPARQL** | Declarative query language for querying RDF datasets and semantic graphs. | 2004 |
| XML Database | **XQuery** | Declarative language for querying, constructing, and transforming XML data. | 2007 |
| JSON Database | **JSONPath** | Expression syntax for navigating and selecting elements within JSON documents. | 2007 |
| Social Graph | **Facebook Query Language (FQL)** | SQL-like language developed by Facebook for querying objects and relationships in its social graph. | 2007 |
| Distributed Database | **HiveQL** | SQL-like query language for querying large datasets through Apache Hive and Hadoop. | 2008 |
| Wide-Column Database | **CQL** | Cassandra Query Language for interacting with Cassandra's distributed wide-column data model. | 2008 |
| API Resource | **OData** | Standardized query conventions for filtering, sorting, projecting, expanding, and paging resources exposed through HTTP APIs. | 2010 |
| Document Database | **MongoDB Query Language** | Query and update language for retrieving and manipulating documents in MongoDB. | 2009 |
| API Filter | **FIQL** | URI-based language for expressing filters over resource collections. | 2009 |
| Graph Database | **Cypher** | Declarative pattern-matching language for querying property graphs. | 2011 |
| Time-Series Database | **PromQL** | Query language for selecting, aggregating, and calculating over Prometheus time-series metrics. | 2012 |
| API Query | **GraphQL** | Declarative API query language allowing clients to specify precisely the data and fields they require. | 2015 |
| Identity Database | **SCIM Filter** | Standard filtering expression for querying identity resources such as users and groups. | 2015 |
| JSON Database | **JMESPath** | Declarative language for extracting and transforming structured data from JSON documents. | 2014 |
| Analytical Database | **DAX** | Expression language for querying and defining calculations over tabular analytical models. | 2010 |
| Telemetry Database | **KQL** | Query language designed for large-scale logs, events, telemetry, and operational data analysis. | 2010s |
| API Filter | **RSQL** | Extended URI-based query syntax for filtering resource collections, derived from FIQL. | 2010s |
| Relational Database | **PRQL** | Modern pipeline-oriented relational query language designed as an alternative representation of SQL queries. | 2022 |
| Analytical Database | **Malloy** | Declarative language designed for analytical querying of relational data and semantic modeling. | 2021 |
| Graph Database | **GQL** | ISO-standard declarative query language for property-graph databases. | 2024 |

## References

- [SQL](note.html?n=technica/computation/data-system/data-system-conceptual-model/sql.md)
- https://en.wikipedia.org/wiki/Query_language
- https://en.wikipedia.org/wiki/Facebook_Query_Language