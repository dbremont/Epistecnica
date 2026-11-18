---
tags: [note]
---

# htmx

> **htmx** extends HTML with attributes that issue requests and place the response into the page — `hx-get`, `hx-post`, `hx-swap`, `hx-trigger` — so that a server-rendered application can update parts of a document without a client-side rendering framework. The browser does what it already does: navigate, submit, replace HTML.

> Read as architecture rather than as a library, htmx is **HATEOAS taken literally**: hypermedia is the wire format, the server owns the state and the markup, and the client owns only the semantics of the HTML it receives. The trade is explicit — no client-side state machine and no API layer to version, at the price of a round trip per interaction and of UI logic living in templates rather than in components.

## References

- [htmx — GitHub](https://github.com/bigskysoftware/htmx)
- [htmx — website](https://htmx.org/)