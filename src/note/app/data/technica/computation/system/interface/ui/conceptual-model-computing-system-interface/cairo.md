# Cairo


> The **Cairo graphics library** is a **2D graphics** library designed to produce high-quality vector graphics across a variety of output targets. It is widely used in Linux/Unix GUI systems (like GTK and Pango), and it provides a **stateful drawing API** modeled after PostScript and PDF.
> 

## 🔧 Key Characteristics

### 📐 **Drawing Model**

- **Immediate mode**: You issue commands like `move_to()`, `line_to()`, `stroke()`, etc.
- **Retained state**: Includes current path, transformation matrix (CTM), clipping region, line width, source color/pattern, etc.
- You can **save** and **restore** this state with `cairo_save()` / `cairo_restore()`.

### 🎯 **Output Targets**

Cairo supports multiple backends for rendering:

- **X11** (via `cairo-xlib`)
- **Wayland**
- **Image surfaces** (in-memory bitmaps)
- **PDF** (`cairo-pdf-surface-create`)
- **PostScript**
- **SVG**
- **Win32 GDI/Direct2D** (Windows)
- **Quartz** (macOS)

### 🧩 **Core Features**

- **Path construction**: `move_to`, `line_to`, `curve_to`, `arc`, `close_path`
- **Painting**: `stroke`, `fill`, `paint`, `mask`
- **Patterns**: Solid colors, gradients, image surfaces
- **Transformations**: Translate, scale, rotate, skew via `cairo_matrix_t`
- **Text rendering**: Low-level glyph placement or integration with text layout libraries (e.g., Pango)
- **Clipping**: You can clip to paths or masks for complex rendering
- **Antialiasing**: High-quality rendering of text and shapes

### 📦 **Language Bindings**

Cairo has bindings for many languages:

- C (native API)
- Python (`pycairo`)
- C++ (`cairomm`)
- Rust (`cairo-rs`)
- JavaScript (via Node.js bindings)
- Haskell, Ruby, Lua, and others

### 🧠 **Conceptual Design**

Cairo operates in terms of **device-independent vectors**, but can render to **rasterized targets** (like image buffers or windows). It tries to **abstract over the device** to maintain consistent rendering output across contexts.

### 📊 **Performance**

- Optimized for **high-quality rendering**, not raw speed
- Minimal state tracking makes it easy to use but not ideal for dynamic, high-performance GUIs (e.g., animations)
- Good for **print-quality output**, **diagrams**, **charts**, **icons**, **PDF export**, etc.

## ✅ Use Cases

| Use Case | Cairo Role |
| --- | --- |
| GTK DrawingArea | Custom widget rendering |
| PDF export in apps | Vector graphics generation |
| Static diagrams (e.g., Graphviz) | High-quality 2D vector rendering |
| Game UI / sprite rendering | Raster surface drawing |
| Scientific plotting (via wrappers) | Backend for plot rendering |

## 🔄 Integration Example

In GTK4:

```c
gtk_widget_set_draw_func(widget, (GtkDrawingAreaDrawFunc)draw_cb, NULL, NULL);

```

In the callback:

```c
void draw_cb(GtkDrawingArea *area, cairo_t *cr, int width, int height, gpointer user_data) {
    cairo_set_source_rgb(cr, 0, 0, 1);
    cairo_rectangle(cr, 10, 10, 100, 100);
    cairo_fill(cr);
}

```

## References

- [Cairo Graphics Official Website](https://www.cairographics.org/)
- [API Reference (devdocs.io)](https://www.cairographics.org/manual/)
- [Pycairo Documentation](https://pycairo.readthedocs.io/en/latest/)