---
tags: [index]
---

# Skip List

- [Data Maps (Index)](note.html?n=technica/computation/data-system/data-system-conceptual-model/data-maps-index.md)

![](https://upload.wikimedia.org/wikipedia/commons/8/86/Skip_list.svg)

> Skip List: A skip list is a probabilistic data structure allowing efficient search, insertion, and deletion operations. It is similar to a sorted linked list but enhanced with multiple layers of forward pointers for faster access paths.
> 

> **Big Idea**: Probabilistic Hierarchical Indexing / Map.
> 

Doubts:

- ¿Which is the space complexity of the **skip list**?
- ¿Which is the time complexity of the **skip list**?

## **Skip List Configuration Parameter’s**

> ¿Which are the **parameters** to tune the **skip list**?
> 

Here's a table summarizing the key parameters to tune in a skip list for **optimal performance**:

| **Parameter** | **Description** |
| --- | --- |
| **Probability (p)** | Determines the fraction of nodes at one level that have pointers to the next level; influences the overall height and efficiency of the skip list. Typical values are typically around $0.5$. |
| **Maximum Level (L)** | Sets the highest possible level for nodes, calculated based on the expected number of elements, commonly as $(L = \log_{1/p}(n))$, where $(n)$ is the estimated number of elements. |
| **Random Level Generator** | The mechanism for determining the level of a new node is crucial for ensuring the node levels adhere to a geometric distribution based on $(p)$. |
| **Memory Allocation Strategy** | This involves deciding how memory is allocated for new nodes, which impacts the skip list's performance and memory usage efficiency. |
| **Update Strategy** | This refers to the method of updating pointers during insertions and deletions, which is crucial for maintaining quick and efficient modifications to the list structure. |

Each of these parameters plays a critical role in the performance and scalability of a skip list, allowing for adjustments based on specific needs such as faster search, efficient memory use, or balanced operation costs.

## References

- [Skip List](https://en.wikipedia.org/wiki/Skip_list)
- [https://github.com/arsbremontix/algorithms/blob/main/src/SkipList.ipynb](https://github.com/arsbremontix/algorithms/blob/main/src/SkipList.ipynb)
- Pugh, William (April 1989). Concurrent Maintenance of Skip Lists (PS, PDF) (Technical report). Dept. of Computer Science, U. Maryland. CS-TR-2222.
- Pugh, W. (1990). "Skip lists: A Probabilistic Alternative to Balanced Trees" (PDF). Communications of the ACM. 33 (6): 668–676. doi:10.1145/78973.78977. S2CID 207691558.
- Sen, Sandeep (1991). "Some observations on skip lists". Information Processing Letters. 39 (4): 173–176. doi:10.1016/0020-0190(91)90175-H.
- Papadakis, Thomas (1993). Skip Lists and Probabilistic Analysis of Algorithms (PDF) (Ph.D.). University of Waterloo.
- Shah, Gauri (2003). Distributed Data Structures for Peer-to-Peer Systems (PDF) (Ph.D. thesis). Yale University.
- Fomitchev, Mikhail; Ruppert, Eric (2004). Lock-free linked lists and skip lists (PDF). Proc. Annual ACM Symp. on Principles of Distributed Computing (PODC). pp. 50–59. doi:10.1145/1011767.1011776. ISBN 1581138024.
- Skip List
[https://brilliant.org/wiki/skip-lists/](https://brilliant.org/wiki/skip-lists/)
- Lock-free Data Structures / [https://en.wikipedia.org/wiki/Non-blocking_algorithm](https://en.wikipedia.org/wiki/Non-blocking_algorithm)
- Sen, Sandeep (1991). "Some observations on skip lists". Information Processing Letters. 39 (4): 173–176. doi:10.1016/0020-0190(91)90175-H.
- Papadakis, Thomas (1993). Skip Lists and Probabilistic Analysis of Algorithms (PDF) (Ph.D.). University of Waterloo.
- Fomitchev, Mikhail; Ruppert, Eric (2004). Lock-free linked lists and skip lists (PDF). Proc. Annual ACM Symp. on Principles of Distributed Computing (PODC). pp. 50–59. doi:10.1145/1011767.1011776. ISBN 1581138024.
- Pugh, William (April 1989). Concurrent Maintenance of Skip Lists (PS, PDF) (Technical report). Dept. of Computer Science, U. Maryland. CS-TR-2222.
- Pugh, W. (1990). "Skip lists: A probabilistic alternative to balanced trees" (PDF). Communications of the ACM. 33 (6): 668–676. doi:10.1145/78973.78977. S2CID 207691558.

[Augmentation](note.html?n=technica/computation/representation/conceptual-model-computational-representation/augmentation.md)

[Probabilistic Data Structure](note.html?n=technica/computation/representation/conceptual-model-computational-representation/probabilistic-data-structure.md)