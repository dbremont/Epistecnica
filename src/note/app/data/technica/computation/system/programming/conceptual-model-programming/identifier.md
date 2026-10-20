---
tags: [building-block]
---

# Identifier

- [Sequence Identifier](note.html?n=technica/computation/system/programming/conceptual-model-programming/sequence-identifier.md)

Guiding Questions:

- What is the nature of an ‘Identifier’?
- …

> Identifier:  Name → Object
> 

> Computational Object: …
> 

> Unique Identifiers: …
> 

> Global Unique Identifier: ..
> 

Goals:

- Communicate about things with other agents.
- …

QA:

- Which are the evaluation criterias of this methods?
- Which are the tradeoffs between them?
- …

## Global Unique Identifier (**GUID)**

> **Note:** The term **GUID** suffers a tragic  duality—it is both an abstract ideal (any globally unique identifier)  and a concrete implementation (Microsoft’s UUID). This collision of  concept and concretion is a testament to the chaos of naming, where  human imperfection and social dynamics blur the lines of clarity
> 

| **Identifier Type** | **Description** | **Format** | **Use Cases** |
| --- | --- | --- | --- |
| **UUID (Universally Unique Identifier)** | A 128-bit identifier standardized by the Open Software Foundation (OSF). | 32 hexadecimal digits, often displayed in 5 groups (e.g., `123e4567-e89b-12d3-a456-426614174000`). | Distributed systems, databases, messaging systems, and unique resource identification. |
| **GUID (Globally Unique Identifier)** | Microsoft's implementation of UUID. Often used interchangeably with UUID. | Same as UUID (e.g., `123e4567-e89b-12d3-a456-426614174000`). | Windows systems, COM objects, and Microsoft technologies. |
| **ULID (Universally Unique Lexicographically Sortable Identifier)** | A 128-bit identifier that is lexicographically sortable and URL-safe. | 26-character Crockford's Base32 encoding (e.g., `01ARZ3NDEKTSV4RRFFQ69G5FAV`). | Distributed systems requiring sortable unique identifiers. |
| **Snowflake ID** | A 64-bit identifier developed by Twitter, containing a timestamp, machine ID, and sequence number. | 64-bit integer (e.g., `1234567890123456789`). | Distributed systems requiring time-ordered unique IDs (e.g., Twitter, Discord). |
| **CUID (Collision-Resistant Unique Identifier)** | A collision-resistant identifier designed for horizontal scaling and predictability. | Variable length, alphanumeric (e.g., `clmtjgk6e0000mkv66d4k6q6p`). | Web applications, databases, and distributed systems. |
| **ObjectID (MongoDB)** | A 12-byte identifier used by MongoDB, containing a timestamp, machine ID, process ID, and counter. | 24-character hexadecimal string (e.g., `507f1f77bcf86cd799439011`). | MongoDB document identification. |
| **KSUID (K-Sortable Unique Identifier)** | A sortable unique identifier designed by Segment, combining a timestamp and random payload. | 27-character Base62 encoding (e.g., `0ujsszwN8NRY24YaXiTIE2VWDTS`). | Distributed systems requiring time-sortable unique IDs. |
| **Flake ID** | A decentralized, roughly time-ordered 128-bit identifier inspired by Snowflake. | 128-bit integer or hexadecimal representation. | Distributed systems requiring decentralized unique IDs. |
| **XID** | A globally unique ID that is 12 bytes long and uses a timestamp, machine ID, process ID, and counter. | 20-character Base32 encoding (e.g., `9m4e2mr0ui3e8a215n4g`). | Distributed systems, databases, and logging systems. |
| **NanoID** | A compact, URL-friendly unique identifier. | Variable length, alphanumeric (e.g., `V1StGXR8_Z5jdHi6B-myT`). | Web applications, short URLs, and distributed systems. |

## References

- https://en.wikipedia.org/wiki/Universally_unique_identifier
- [Naming](note.html?n=technica/computation/system/programming/conceptual-model-programming/naming.md)
- [Name](note.html?n=technica/computation/language-system/conceptual-model-language-system/name.md) [Names In a  **Computer Process Object Space**]
- [Database Record Identifier Models](note.html?n=technica/computation/data-system/data-system-conceptual-model/database-record-identifier-models.md)
- [Program Element](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element.md)