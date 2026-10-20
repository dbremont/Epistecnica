---
tags: [query-language]
---

# OData (Open Data Protocol)

- [Query Language](note.html?n=technica/computation/data-system/data-system-conceptual-model/query-language.md)

> In this note, we will explore `OData (Open Data Protocol)`, a standardized data-access protocol and query language that enables clients to interact with sets of structured data resources through a uniform interface.
> 

## Formulation

### How `OData (Open Data Protocol)` is used?

### How `OData (Open Data Protocol)`  is implemented?

```
                CLIENT
                   │
                   │ "I need this data"
                   ▼
             QUERY LANGUAGE
              / API LAYER
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
   Query validation      Authorization
         │                   │
         └─────────┬─────────┘
                   ▼
             DATA / SEMANTIC
                LAYER
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼
   SQL DB      Analytics DB   Other sources
```

## EDM (Entity Data Model)

> `OData.Edm` is part of the Microsoft OData Libraries and represents the Common Schema Definition Language (CSDL) Entity Data Model (EDM) for OData services. It is used to define the metadata and schema of OData services, including the entities, properties, navigation properties, and relationships.
> 

## Performance

### **How  much  latency added by OData to the request-processing cycle?**

## References

- https://en.wikipedia.org/wiki/Open_Data_Protocol