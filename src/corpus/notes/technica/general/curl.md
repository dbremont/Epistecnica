---
tags: [note, shell, command-line, unix, tool]
---

# curl

> Transfers data to and from URLs across many protocols, and doubles as an inspection tool for headers, redirects and timing.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Network inspection |
| **Relation** | `curl` |
| **Main advantage** | The universal URL client |

## Typical use

```sh
curl -sI https://example.com
```

## Declarative layer: Hurl

> [Hurl](https://github.com/Orange-OpenSource/hurl) runs HTTP requests written as plain text — the request, then assertions on the status, headers and body, then captures for the next request — so a sequence of calls becomes a test that can run in CI. It is the declarative form of what curl does imperatively: the same transport, with the checks and the chaining in the file rather than in a shell script.

## References

- [curl](https://curl.se/docs/manpage.html)
- [dig](/view.html?p=notes/technica/general/dig.md)
