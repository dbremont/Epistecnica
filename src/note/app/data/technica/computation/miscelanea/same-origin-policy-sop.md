# Same-origin Policy (SOP)


> What is SOP?
> 

## Formulation

> What is SOP? Which are the guiding ‘regulary documents’? Which are the institutions behind this?
> 

### What is SOP?

SOP specifies that:

- Scripts running in one origin **cannot read or modify** the DOM, cookies, storage, or most response data of another origin.
- Certain interactions (e.g., navigation, form submission) are allowed but **write-only** with respect to cross-origin data.

In effect, SOP defines **read access boundaries**, not absolute communication prohibition.

### Normative Documents

SOP is not defined in a single canonical document. Instead, it emerges from multiple overlapping specifications and de facto browser behaviors:

- **HTML Living Standard (WHATWG)** — defines document origins, browsing contexts, and navigation rules.
- **ECMAScript Specifications** — indirectly relevant via execution contexts.
- **Fetch Standard (WHATWG)** — formalizes request modes, CORS, opaque responses, and tainting.
- **RFC 6454 — The Web Origin Concept** — provides a formal definition of "origin".

### Institutions Behind SOP

- **Browser vendors** (historically decisive):
    - Netscape (originator of SOP concepts)
    - Mozilla
    - Google (Chromium)
    - Apple (WebKit)
    - Microsoft (legacy Trident, now Chromium-based Edge)
- **Standards bodies**:
    - WHATWG (primary modern authority)
    - W3C (historical and complementary role)

SOP is best understood as a **convergent security equilibrium**, not a centrally legislated policy.

## History

- **1995–1996 (Netscape Navigator)**: SOP emerges pragmatically to prevent malicious scripts from accessing private user data across sites.
- **Early 2000s**: SOP becomes entrenched across browsers, though inconsistently implemented.
- **2006–2010**: Increased attention due to AJAX, mashups, and early Web 2.0 architectures.
- **2010–2014**: Formalization of origin concepts and cross-origin exceptions; CORS introduced.
- **2015–present**: SOP integrated into a broader isolation stack including CSP, CORP, COOP, COEP, and site isolation.

## **Browser Support**

| **Browser** | **Notes** | **Time** |
| --- | --- | --- |
| **Netscape Navigator** | Originated the Same-Origin Policy as an ad hoc security measure to prevent script-based data leakage across sites | ~1996 |
| **Internet Explorer (Trident)** | Implemented SOP with multiple historical inconsistencies; legacy exceptions and security zones weakened isolation | ~1997–2015 |
| **Mozilla Firefox (Gecko)** | Early and comparatively strict SOP enforcement; later formal alignment with WHATWG standards | ~2002–present |
| **Google Chrome / Chromium (Blink)** | Strong SOP enforcement combined with Site Isolation, strict origin-keyed processes, and modern Fetch/CORS semantics | ~2008–present |
| **Apple Safari (WebKit)** | SOP enforced with tighter storage and privacy partitioning; historically conservative CORS behavior | ~2003–present |
| **Microsoft Edge (Chromium-based)** | Inherits Chromium SOP model; legacy EdgeHTML retired | ~2020–present |

## Implementation

> How SOP is implemented? What is the History of the Implementation?
> 

### How SOP Is Implemented

SOP is implemented primarily at the **browser runtime level**, across several subsystems:

- **JavaScript Engine**
    - Restricts object references across origins
    - Enforces access checks on DOM APIs
- **Networking Stack**
    - Enforces Fetch modes (`same-origin`, `no-cors`, `cors`)
    - Applies response tainting rules
- **Storage Subsystems**
    - Cookies (scoped by domain/path + SameSite)
    - LocalStorage / IndexedDB (origin-bound)
- **Process Isolation (modern browsers)**
    - Site Isolation maps origins (or site groups) to OS processes

### History of Implementation

- **Pre-2008**: Largely monolithic browser processes; SOP enforced via runtime checks only.
- **2008–2015**: Gradual hardening; increased spec alignment; introduction of CORS.
- **2015–present**: Multi-process architectures, stricter origin-keyed storage, speculative execution mitigations.

Implementation shifted from **policy checks** to **architectural isolation**.

## Bypassing Mechanism(s)

> SOP is intentionally strict but includes *designed escape hatches*.
> 

| Mechanism | Description |
| --- | --- |
| **CORS** | Server-declared relaxation of read access for specific origins via HTTP headers |
| **PostMessage** | Explicit, structured cross-origin message passing between windows/frames |
| **JSONP** (legacy) | Script-tag–based data exfiltration; largely deprecated |
| **WebSockets** | Cross-origin connections allowed, but SOP still governs data exposure |
| **document.domain** (deprecated) | Legacy domain relaxation; strongly discouraged |
| **Server-side proxying** | Same-origin facade implemented on the backend |

These mechanisms do not *break* SOP; they **negotiate controlled exceptions**.

## QA

### How to disable the SOP?

**SOP cannot be safely disabled in production environments.**

For testing and debugging only:

- **Browser flags** (highly insecure):
    - Chromium: `-disable-web-security`
    - Firefox: custom `about:config` overrides
- **Development servers**:
    - Proper CORS headers
    - Reverse proxies (e.g., Nginx)

Disabling SOP exposes users to:

- Cross-site data exfiltration
- Credential leakage
- Arbitrary session hijacking

From a QA standpoint, SOP should be **tested against**, not disabled.

## References

- https://en.wikipedia.org/wiki/Same-origin_policy
- https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
- https://aosabook.org/en/500L/the-same-origin-policy.html
- * RFC 6454 — The Web Origin Concept
- WHATWG HTML Living Standard
- WHATWG Fetch Standard