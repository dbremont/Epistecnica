---
tags: [physical]
---

# Drepper, U. (2007). What every programmer should know about memory. Red Hat, Inc, 11(2007), 2007.


```bash
@article{drepper2007every,
  title={What every programmer should know about memory},
  author={Drepper, Ulrich},
  journal={Red Hat, Inc},
  volume={11},
  number={2007},
  pages={2007},
  year={2007}
}
```

## Index

## Notes

1. RAM is a parallel machine of its own. This document describes DDR3 (which is 2 versions out from modern DDR5), but that doesn't really matter. Today's DDR5 is just more parallel.
2. This document very precisely describes the parallelization mechanism of DDR3. Read/writes to DDR3 are parallelized by channel, rank, and bank. DDR4 added bank-group as an additional layer of parallelism (above bank below rank).
3. An individual bank has performance characteristics: an individual bank is much faster when it can stay "open", thus only getting a CAS-latency, rather than a close+precharge+RAS+CAS latency cycle.
4. CPUs try to exploit this parallelism with various mechanisms. Software prefetching, hardware prefetchers, levels of cache, and so forth.
5. NUMA is more relevant today, as EPYC systems are innately quad-NUMA. HugePages is also more relevant today as 96MB+ L3 per CCX have appeared on Ryzen/EPYC machines, meaning you need HugePages to access L3 without a TLB hit. TLB isn't really RAM, but it's closely related to RAM and could be a bottleneck before you hit a RAM bottleneck, so it's still important to learn if you're optimizing against RAM-bottlenecks.

## References

- [https://people.freebsd.org/~lstewart/articles/cpumemory.pdf](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf)
