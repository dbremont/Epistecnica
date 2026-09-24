# Chang, F., Dean, J., Ghemawat, S., Hsieh, W. C., Wallach, D. A., Burrows, M., Chandra, T., Fikes, A., & Gruber, R. E. (2006). Bigtable: A Distributed Storage System for Structured Data.


## Notes

---

> **Bigtable is a distributed storage system** for managing **structured data** that is designed to scale to a very large size: petabytes of data across thousands of commodity servers.
> 

> In this paper we describe the **simple data model** provided by **Bigtable**, which gives clients
dynamic control over **data layout** and **format**, and we describe the design and implementation of **Bigtable**.
> 

> A **Bigtable cluster** typically operates in a shared pool of machines that run a wide variety of other distributed applications, and **Bigtable** processes often share the same machines
with processes from other applications.
> 

> **Bigtable** de-pends on a **cluster management system** for **scheduling jobs**, managing resources on shared machines, dealing with machine failures, and monitoring machine status.
> 

> The **Google SSTable** ﬁle format is used internally to store **Bigtable** data.
> 

> **Bigtable** relies on a highly-available and persistent **distributed lock service** called **Chubby**.
> 

> The **Bigtable** implementation has three major components: a library that is linked into every client, one master server, and many tablet servers.
> 

## Data Model:  Multidimensional Sorted Map

¿What informs the decision to choose this **data model**? Analysis of the potential uses of the **Bigtable** system.

```bash
(row:string, column:string, time:int64) → string
```

> Column Families: …
> 

> Timestamps: Multiversion Data Cells.
> 

## References

- 

[Burrows, M. (2006). The Chubby lock service for loosely-coupled distributed systems. Proceedings of the 7th Symposium on Operating Systems Design and Implementation, 335–350.](Burrows,%20M%20(2006)%20The%20Chubby%20lock%20service%20for%20loos%2010e598edb7908141ae37d6d1bc10ca3f.md)
