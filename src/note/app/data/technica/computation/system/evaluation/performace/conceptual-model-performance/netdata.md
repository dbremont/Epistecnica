---
tags: [analysis, data-collection, tool]
---

# Netdata


> Intra-structure monitoring.
> 

QA➖

```bash
docker run -d --name=netdata -p 19999:19999 --restart=always netdata/netdata
```

See: http://localhost:19999

## References

- [Netdata](https://learn.netdata.cloud/docs)