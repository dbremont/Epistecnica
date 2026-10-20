# Canvas Graphics

> **Canvas Graphics** refers to the **procedural raster-based rendering** of 2D (and optionally 3D via WebGL) graphics onto a bitmap surface exposed by the **HTML5 `<canvas>` element**. It uses an **immediate-mode rendering model**, in which drawing operations directly mutate the underlying pixel buffer without retaining a scene graph or DOM representation of graphical primitives.
> 

## 🔧 Technical Characteristics

- **Rendering API:** `CanvasRenderingContext2D` (or `WebGLRenderingContext` for 3D).
- **Rendering Model:** Immediate mode (as opposed to retained mode like SVG).
- **Graphics Type:** Raster (bitmap).
- **Access Model:** JavaScript-based procedural API.
- **Output Medium:** A single flat bitmap surface in the browser's DOM.

## 📦 Key Features

- **Low-level 2D drawing operations** (lines, paths, arcs, text, images).
- **No retained object model** — once drawn, shapes can't be individually manipulated.
- **Pixel-level access** via `getImageData()` / `putImageData()` (useful for filters or image processing).
- **Stateless drawing context** — must manage redraws manually (e.g., for animations).
- **High-performance rendering**, especially for real-time or frequently updated graphics (e.g., games, simulations).

## 🧪 Comparison with SVG

| Feature | Canvas | SVG |
| --- | --- | --- |
| Rendering Model | Immediate mode | Retained mode (DOM-based) |
| Graphics Type | Raster | Vector |
| Performance | High for many objects / animations | Lower for complex scenes |
| Interactivity | Manual (hit testing, etc.) | Native via DOM events |
| Scene Graph | None | Yes (each element is a DOM node) |

## 🧰 Example Use Cases

- Game engines and real-time simulations
- Image editing tools
- Custom charting libraries
- Scientific visualizations requiring pixel-level control
- Efficient animations and transitions

## References

- https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
- https://html.spec.whatwg.org/dev/canvas.html