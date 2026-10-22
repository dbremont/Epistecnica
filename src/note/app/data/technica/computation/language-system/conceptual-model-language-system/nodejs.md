---
tags: [javascript, language-system, tool]
---

# NodeJS

- [V8 JavaScript Engine](note.html?n=technica/computation/language-system/conceptual-model-language-system/v8-javascript-engine.md)

> **Node.js** is an open-source, cross-platform JavaScript runtime environment that executes JavaScript code outside a web browser.
> 

> **Node.js** is essentially a wrapper around the V8 JavaScript engine, providing additional functionality such as file system I/O, networking, and other operating system interactions that are not present in V8 by itself.\
> 

> Node.js architecture uses a non-blocking, event-driven model powered by the V8 JavaScript engine, enabling efficient handling of I/O-heavy operations through asynchronous callbacks and a single-threaded event loop.
> 

![Untitled](../assets/note/technica/computation/language-system/conceptual-model-language-system/nodejs/untitled.png)

## Parsing

Parsing Entry Point:

- v8::internal::parsing::ParseProgram
- V8 Maintains A Background Thread Compiler

## Refereces

- https://github.com/nodejs/node
- Why we developed the Node.js reference architecture
[https://developers.redhat.com/blog/2021/03/08/introduction-to-the-node-js-reference-architecture-part-1-overview#](https://developers.redhat.com/blog/2021/03/08/introduction-to-the-node-js-reference-architecture-part-1-overview#)
- Understanding the NodeJS Architecture
[https://www.turing.com/kb/understanding-the-nodejs-architecture](https://www.turing.com/kb/understanding-the-nodejs-architecture)
- Understanding Node.js Event-Driven Architecture ([freecodecamp.com](http://freecodecamp.com/))
[https://news.ycombinator.com/item?id=14289551](https://news.ycombinator.com/item?id=14289551)
- Event Driven Architecture
[https://gnugat.github.io/2016/04/27/event-driven-architecture.html](https://gnugat.github.io/2016/04/27/event-driven-architecture.html)
- An overview of Node.js: architecture, APIs, event loop, concurrency
[https://2ality.com/2022/09/nodejs-overview.html](https://2ality.com/2022/09/nodejs-overview.html)
- [https://github.com/nodejs/node/blob/main/BUILDING.md#building-a-debug-build](https://github.com/nodejs/node/blob/main/BUILDING.md#building-a-debug-build)
- [Insight into Node js Internals-Event Loop](https://lashanfaliq.medium.com/insight-into-node-js-internals-d89b91252643)
- [Exploring Node.js Internals](https://www.smashingmagazine.com/2020/04/nodejs-internals/)
- [The Node.js Event Loop](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [NodeJS Internals: Event Loop](https://eetechy.com/nodejs-internals-event-loop/)
- loop-watcher.c
[https://codingdao.com/libuv-source-analysis/pages/update/2016/04/25/prepare-check-and-idle.html](https://codingdao.com/libuv-source-analysis/pages/update/2016/04/25/prepare-check-and-idle.html)
- Do you really really know nodejs?
[https://tech.zupee.com/do-you-really-really-know-nodejs-cbcb430c3908](https://tech.zupee.com/do-you-really-really-know-nodejs-cbcb430c3908)