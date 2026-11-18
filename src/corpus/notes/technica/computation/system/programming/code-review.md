---
tags: [note, process]
---

# Code Review

> **Code review** is the practice of reading a change before it is merged. It is the cheapest defect-detection technique in software production — defects found in review cost a fraction of what they cost in production — and the only one that also transfers knowledge between the author and the reviewer.

## What review catches

| Class of defect | What detects it | Why |
| --- | --- | --- |
| **Rule-expressible** — null dereference, injection, thread-safety, style | Linters, static analysis, a reviewer with a checklist | Deterministic and local: the rule is the knowledge |
| **Context-dependent** — wrong abstraction, missing case, design drift | The reviewer who knows the subsystem | Needs repository-level context, not a rule |
| **Communication** — shared ownership, knowledge transfer | The conversation itself | Cannot be automated, and is the reason review survives |

## Automated review

> A tool-assisted review splits the work: deterministic pipelines for the classes a rule can encode, and a model for the rest. Alibaba's [open-code-review](https://github.com/alibaba/open-code-review) is the scaled instance — a multi-language ruleset (NPE, thread safety, XSS, SQL injection) running beside an LLM agent with repository context, emitting line-level comments, against OpenAI- or Anthropic-compatible backends.

> The boundary is the point. A rule detects exactly what it encodes and nothing else, which is why it is reproducible; a model generalises to what no rule anticipated, at the price of not being reproducible; and neither substitutes for a reviewer who knows why the code exists.

## References

- [open-code-review — GitHub](https://github.com/alibaba/open-code-review) — hybrid ruleset + LLM review at production scale
- [Code Review — Stack Exchange](https://codereview.stackexchange.com/)
- [Program](/view.html?p=notes/technica/production/industry/software/production/program.md) — the production process review belongs to