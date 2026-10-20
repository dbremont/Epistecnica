# ORM


> An **Object-Relational Mapping (ORM)** is a programming technique that enables the conversion of data between incompatible type systems in object-oriented programming languages and relational databases by mapping database tables to objects, allowing for seamless interaction with data through object-oriented paradigms rather than raw SQL queries.
> 

| **Framework** | **Description** | **Language** | **Key Features** |
| --- | --- | --- | --- |
| **Hibernate** | A powerful, open-source ORM framework for Java. It provides a mapping of Java objects to database tables. | Java | - Automatic table generation - Lazy loading - Query Language (HQL) - Caching support |
| **Entity Framework** | An ORM framework for .NET that simplifies data access and manipulation using .NET objects. | C#, .NET | - LINQ support - Code-first and Database-first approaches - Lazy loading - Migration support |
| **Django ORM** | The ORM part of the Django web framework for Python, which facilitates database interactions with Python models. | Python | - Built-in migrations - QuerySet API for querying - Schema generation - Built-in admin interface |
| **SQLAlchemy** | A Python ORM that provides full power and flexibility in database interactions. It supports both high-level and low-level APIs. | Python | - Supports multiple database backends - Eager and lazy loading - Direct SQL queries alongside ORM |
| **Eloquent** | The ORM used in Laravel (PHP framework). It provides simple and expressive syntax for interacting with databases. | PHP | - ActiveRecord implementation - Relationships (one-to-many, many-to-many) - Query builder API |
| **GORM** | An ORM for Go (Golang) which supports CRUD operations and relationships. | Go | - Simple API - Supports migrations - Relationship handling (one-to-many, many-to-many) |
| **ActiveRecord** | An ORM for Ruby (typically used with Ruby on Rails), where models directly map to database tables. | Ruby | - ActiveRecord pattern - Migration support - Validation support - Associations (belongs_to, has_many) |
| **TypeORM** | A TypeScript/JavaScript ORM for Node.js that works with both SQL and NoSQL databases. | TypeScript/JS | - TypeScript-first design - QueryBuilder API - Migrations - Supports multiple database types |

## References

- https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping
- https://stackoverflow.com/questions/97197/what-is-the-n1-selects-problem-in-orm-object-relational-mapping