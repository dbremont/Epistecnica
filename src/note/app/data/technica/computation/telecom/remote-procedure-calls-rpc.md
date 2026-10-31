---
tags: [computer-network, protocol]
---

# Remote Procedure Calls (RPC)


> Simplify the programmer’s job when building distributed systems. Even novice programmers can use function call!
> 

**RPC**: - **Pre-RPC**, all of the gory details were exposed to the programmer, - **Post-RPC**, a remote interaction looks (nearly) identical to a local procedure call, with the system hiding (nearly) all of the differences.

## Implementation

**RPC** ideally makes net communication look just like function call:

**Client**

```python
z = fn(x, y)
```

**Server**

```python
fn(x, y) {    compute    return z}
```

**RPC Message Diagram**

```
Client    Server
  request --->
  <---    response
```

**RPC Software Structure**

```
Client  Client   RPC       Net      RPC             Server      Handler
App     Stub     lib                lib             Stub

call    marshall    send     request   recv  dispatch  unmarshall  fn(args)
                    wait               wait                        work...
return  unmarshall  recv     response  send            marshall    return
```

## Issues

Fundamental issues that RPC Cannot Hide:

- single {process, address space} vs. multiple {processes, address spaces}
    - partial failure where caller/callee go down
    - pointers/references – either impossible, or severe coherence issues
- network failures
    - require timeouts vs. block-forever-until-reply (why?)
    - therefore, have to deal with premature timeout
- performance differences (debatable)
    - 3-6 orders of magnitude difference between LPC and RPC performance; I claim is too big to ignore, has implications for program structure

## References

- [Implementing Remote Procedure Calls](https://courses.cs.washington.edu/courses/csep552/13sp/lectures/1/rpc.txt)
- [Apache Thrift](note.html?n=technica/computation/distributed-computing/multi-node-processing-system-conceptual-model/apache-thrift.md)