---
tags: [browser]
---

# Firefox


> **Firefox** is an open-source, multi-platform web browser developed by Mozilla, featuring the **Gecko rendering engine**, **SpiderMonkey JavaScript engine**, strong **privacy protections**, support for **WebExtensions**, and a highly customizable UI, optimized for **standards compliance** and **performance efficiency**.
> 

Source Code:

- **files:** 336957
- **blank:** 5611054
- **comment:** 6663746
- **code:** 40720305

![image.png](data/technica/computation/system/interface/ui/conceptual-model-computing-system-interface/assets/firefox/image.png)

![image.png](data/technica/computation/system/interface/ui/conceptual-model-computing-system-interface/assets/firefox/image-1.png)

## Building

```bash
git config --global http.postBuffer 524288000
git config --global http.maxRequestBuffer 1048576000

git clone --depth=1 https://github.com/mozilla/gecko-dev.git firefox
./mach bootstrap

echo 'ac_add_options --enable-debug
ac_add_options --disable-optimize
ac_add_options --enable-tests
ac_add_options --disable-elf-hack' > mozconfig

./mach build

./mach run --debug
./mach run --debug --debugger=gdb

## Enable logging for JavaScript debugging:
MOZ_LOG="nsHttp:5" ./mach run

```

## Debugging

```bash
break mozilla::dom::Element::Element
break  mozilla::dom::VisualViewport::Page
break break mozilla::dom::Document::Document
break nsWindow::DispatchEvent
```

## **Subsystems**

| **Subsystem** | **Description** |
| --- | --- |
| **Rendering Engine** | Responsible for rendering HTML, CSS, and JavaScript into the visual representation of the webpage. It interprets and displays the content to the user. |
| **JavaScript Engine** | Interprets and executes JavaScript code. It optimizes the execution of JavaScript using Just-In-Time (JIT) compilation and garbage collection. |
| **Document Object Model (DOM)** | A tree-like structure representing the HTML document. It allows JavaScript to interact with and manipulate the content of the web page. |
| **CSS Object Model (CSSOM)** | A model that represents the styles applied to HTML elements. It is built alongside the DOM and is used to determine the final rendering of elements. |
| **Networking Subsystem** | Handles network communication (e.g., HTTP/HTTPS requests) between the browser and the web server. It manages APIs like **Fetch**, **XMLHttpRequest**. |
| **Event Handling Subsystem** | Manages events (e.g., user interactions like clicks, keystrokes) and triggers the appropriate callbacks. It allows asynchronous programming. |
| **Storage Subsystem** | Responsible for local data storage on the client side. This includes storing data in **cookies**, **localStorage**, **sessionStorage**, and **IndexedDB**. |
| **Security Subsystem** | Manages security features such as **Cross-Origin Resource Sharing (CORS)**, **sandboxing**, and **same-origin policy** to protect the browser environment. |
| **Layout and Paint Subsystem** | Calculates the layout of elements and paints the content to the screen, based on the DOM and CSSOM. Responsible for rendering the UI. |
| **Web Workers** | Provides a way to run JavaScript code in the background on a separate thread, allowing for parallel computation without blocking the main thread. |
| **Audio/Video Subsystem** | Handles playback and control of multimedia content (audio and video) in web pages. It interfaces with native media playback features of the browser. |
| **Geolocation Subsystem** | Allows the browser to determine the user's physical location through GPS, Wi-Fi, or IP address. |
| **Graphics Subsystem** | Handles rendering and manipulation of visual content using APIs such as **Canvas**, **WebGL**, and **SVG** for graphics and visualizations. |
| **Browser UI Subsystem** | Controls the user interface components like the address bar, tabs, and the browser window. It interacts with the rest of the subsystems to display content. |
| **Performance Subsystem** | Handles optimizations related to the browser’s resource management, such as memory usage, CPU usage, and network latency. |
| **Cache Subsystem** | Allows the browser to store copies of resources to reduce loading time and improve the user experience for repeated requests (e.g., caching images, CSS). |

## **Gecko**

> aka **Rendering Engine.**
> 

> 

## SpiderMonkey

> JS Runtime
> 

## **Security Subsystem**

> 

### CORS

> Cross-Origin Resource Sharing (CORS) is a mechanism that allows web pages from different domains or origins to access each other’s resources, such as APIs or web services.
> 

> By default, web browsers restrict cross-origin HTTP requests initiated by JavaScript code, as a security measure to prevent attacks like cross-site scripting (XSS). CORS provides a way to enable cross-origin requests while still protecting the user’s privacy and security.
> 

> CORS works by adding HTTP headers to the request and response messages that allow a web application running at one origin to access resources from a different origin. These headers specify which origins are allowed to access the resource, what types of HTTP methods are permitted, and what types of data can be transmitted.
> 

## **Audio/Video Subsystem**

> 

## QA

### How rendering works? What is rendering?  How  a the DOM get’s render?

> **What is rendering?** Rendering is the process of transforming structured graphical or document data into visible pixels on a display surface.
> 

> **How rendering works?** Rendering works by traversing graphical or document structures, computing layout, style, geometry, and compositing operations, then rasterizing the result into framebuffer pixels.
> 

> **How does the DOM get rendered?** The browser renders the DOM by parsing HTML into a DOM tree, combining it with CSS into a render tree, performing layout and paint operations, then compositing layers onto the screen.
> 

> **Does the browser bypass X11 or Wayland?** Modern browsers usually do not fully bypass X11 or Wayland, but instead render through their compositor and graphics APIs while delegating window management and display presentation to the display server or compositor.
> 

## Firefox: Conceptual Model

Conceptual Model: Firefox

## References

- https://searchfox.org/
- https://firefox-source-docs.mozilla.org/overview/index.html
- [WebDriver](note.html?n=technica/computation/telecom/telecom-conceptual-model/webdriver.md)
- https://firefox-source-docs.mozilla.org/overview/gecko.html
- [How Back/forward Cache Helped Yahoo! JAPAN News Increase Revenue by 9% on Mobile](https://web.dev/yahoo-japan-news-bfcache/)
- [Javascript](note.html?n=technica/computation/language-system/conceptual-model-language-system/javascript.md)
- [**WebAssembly**](note.html?n=technica/computation/language-system/conceptual-model-language-system/webassembly.md)
- https://browser.engineering/
- [X Window System (X11 Version)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/x-window-system-x11-version.md)
- [Rendering](note.html?n=technica/computation/graphical-heterogeneous-high-performance-computing-system/graphical-computing-system/rendering.md)
- https://news.ycombinator.com/item?id=49522137