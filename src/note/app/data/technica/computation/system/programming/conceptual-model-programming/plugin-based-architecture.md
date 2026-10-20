---
tags: [architecture]
---

# Plugin Based Architecture


> **Plugin:** An independently developed software component that adds functionality to an existing application through defined extension mechanisms.
> 

> **Extension Point:** A defined interface, API, or integration location through which external components can extend a system.
> 

> **Extension Mechanism (Callback, Hook, Event Listener, …):** A technical mechanism that enables an extension to connect to and operate through an extension point.
> 

> **Plugin-Based Architecture:** An architectural style in which an application provides extension points and its functionality can be extended through independently developed plugins.
> 

> **Plugin-Based Design:** The design approach of structuring an application around a stable core and explicit extension points, allowing functionality to be added, removed, or replaced through independently developed plugins.
> 

> **Modular Application Framework:** A framework that provides the mechanisms for decomposing an application into independently managed modules, including module boundaries, dependencies, lifecycle, and often dynamic loading.
> 

> NOTE: We need to link this with software design and extension strategy.
> 

## References

- https://github.com/cordiverse/cordis
- https://felix.apache.org/documentation/index.html
- https://equinox.eclipseprojects.io/
- https://en.wikipedia.org/wiki/OSGi
- https://pf4j.org/
- https://karaf.apache.org/