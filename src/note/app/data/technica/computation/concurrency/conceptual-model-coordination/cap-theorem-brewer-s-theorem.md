# Cap Theorem (Brewer's Theorem)


> **States** that in a **distributed system**, it is impossible to simultaneously guarantee all of the following three properties: consistency, availability, and partition tolerance. According to **CAP**, a **distributed system** can only ensure at most two of these properties simultaneously.
> 

**CAP Theorem**:

- **Consistency**: All nodes in a distributed system see the same data simultaneously.
- **Availability**: Every request to the system receives a response, without guaranteeing it contains the most recent data version.
- **Partition Tolerance**: The system continues to operate even in the presence of network partitioning.

## References

- [An Illustrated Proof of the CAP Theorem](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/)