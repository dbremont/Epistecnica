# GTK3


> GTK (GIMP Toolkit) is a **cross-platform, object-oriented, event-driven graphical user interface toolkit** implemented in C and built on top of the GLib GObject system, providing a comprehensive widget set for application development. It abstracts platform-specific windowing and input systems via GDK, supports a retained-mode scene graph rendering pipeline through GSK (GTK Scene Graph Kit) using GPU-accelerated backends such as OpenGL and Vulkan, and manages its own main event loop based on GLib’s `GMainLoop`. GTK widgets follow a hierarchical composite design with flexible layout managers, employ a CSS-based styling system for theming, and propagate input events through a signal-based mechanism with modular event controllers. The entire API is introspectable via GObject Introspection, enabling multi-language bindings, while maintaining strict single-threaded usage constrained to the main loop thread. GTK's architecture balances low-level rendering performance, high-level object orientation, and cross-platform portability through a layered abstraction stack that includes GLib, GDK, Pango, and Cairo (GTK 3) or GSK (GTK 4).
> 

## Breviarium

> 

### Technical Features

> 

| Feature | **GTK** |
| --- | --- |
| Widgets | Extensive |
| Rendering backend | Cairo (2D vector rendering) |
| Layout System | Manual packing / CSS styling |
| Custom Widgets | Complex (GObject subclassing) |
| Language Bindings | C, Python, Rust, Vala, etc. |
| Native Look & Feel | GTK4 broke many themes; improving |
| Internationalization (i18n) | Built-in |
| Accessibility | Full (ATK, a11y) |
| Theming | GTK CSS |
| Signals/Events | Signals via GObject |
| Graphics acceleration | GTK4 adds GPU via `gsk` / Vulkan |

## Paradigms

GTK3 (GIMP Toolkit 3) uses a **hybrid programming paradigm** that combines:

### 🧱 **Object-Oriented Programming (OOP)** via GObject

GTK3 is built on **GObject**, a C-based object system that brings:

| Feature | Description |
| --- | --- |
| Classes & Inheritance | Widgets are types (e.g. `GtkWindow` inherits from `GtkBin`, which inherits from `GtkContainer`, etc.). |
| Virtual Methods | Functions like `gtk_widget_show()` behave differently depending on the actual widget. |
| Signals | Events like `clicked`, `destroy`, `draw`, etc. are implemented using a flexible signal system. |
| Type Introspection | Allows dynamic behavior, used by language bindings (Python, Rust, etc.). |

### ⚙️ **Event-Driven Programming**

| Feature | Description |
| --- | --- |
| Main Loop | `gtk_main()` runs a loop that waits for events like mouse clicks or key presses. |
| Callbacks | You register functions (like `on_button_clicked`) to be invoked in response to signals. |
| Asynchronous by nature | The UI reacts to input events and redraws accordingly, not via polling. |

### 🎨 **Declarative-Style UI Construction (via UI Files)**

While GTK3 itself is imperative, you can define UI in `.ui` XML files using **GtkBuilder**:

```xml
<object class="GtkWindow">
  <child>
    <object class="GtkButton" id="my_button">
      <property name="label">Click Me</property>
    </object>
  </child>
</object>

```

Then load it in C:

```c
GtkBuilder *builder = gtk_builder_new_from_file("interface.ui");
GtkWidget *window = GTK_WIDGET(gtk_builder_get_object(builder, "my_window"));

```

This allows a **separation of concerns** between UI layout and logic — similar to HTML + JS.

### 🔁 **Imperative Layout and Control Flow**

GTK3 applications are **procedurally structured** in C:

```c
GtkWidget *button = gtk_button_new_with_label("Click Me");
gtk_container_add(GTK_CONTAINER(window), button);

```

Everything is built step-by-step and configured via function calls.

## 🧱 Core Architecture

### **Object System**

- GTK is built atop **GLib's GObject system**, a C-based runtime type and object system implementing inheritance, polymorphism, signals, and dynamic properties.
- Objects are allocated on the heap and follow reference counting via `g_object_ref()` / `g_object_unref()`.
- Supports dynamic interfaces (`GTypeInterface`) and run-time type discovery via `G_TYPE_FROM_INSTANCE`.

### **Main Loop Integration**

- GTK uses **GLib’s main event loop** (`GMainLoop`) to multiplex file descriptors, timers, and custom sources.
- The loop integrates system-level event sources (e.g., X11, Wayland, Windows message loop) via platform-specific `GSource` backends.

## 🎨 Rendering Subsystem

### **Rendering Backend Abstraction**

- GTK 3: Rendering abstracted through **Cairo** (vector graphics), using platform surfaces (Xlib, Wayland, Quartz, Win32).

### **Scene Graph Architecture**

- GTK 4 uses a retained-mode scene graph model (`GskRenderNode` tree) rather than GTK 3’s immediate-mode draw cycle.
- Node types include `GskColorNode`, `GskTextureNode`, `GskTransformNode`, enabling GPU batching and reduced overdraw.

## 🧩 Widget Model

### **Widget Hierarchy**

- `GtkWidget` is the base class for all visual components. In GTK 4, layout, rendering, and event handling are separated more cleanly.
- GTK uses a **composite and container model**, with `GtkBox`, `GtkGrid`, etc., managing child allocation.
- Supports **CSS-like styling engine** (via `GtkStyleContext`) with pseudo-classes, style properties, and animations.

### **Layout Engine**

- GTK 3: Height-for-width layout.

## 🎛️ Input and Event System

### **Event Handling**

- Propagates input events (keyboard, pointer, touch) via a top-down delivery model, filtered by `GtkEventController` in GTK 4.
- Uses a signal-based mechanism (`g_signal_emit`) for event dispatching (e.g., `"button-press-event"`, `"key-press-event"`).

### **Event Controllers**

- GTK 4 introduced explicit `GtkEventController` objects to replace legacy event virtual methods.
- Decouples input handling from widget class hierarchy.

## 🌐 Internationalization & Accessibility

### **Accessibility**

- Implements **ATK (Accessibility Toolkit)** in GTK 3; superseded by **AT-SPI2** and native **GtkAccessible** nodes in GTK 4.
- Exposes accessibility tree via DBus on Linux.

### **Input Method Integration**

- Provides full support for IM modules (`IMContext`) for complex text input (e.g., CJK languages), integrating with IBus, Fcitx, etc.

## 🧶 Multi-threading & Concurrency

### **Thread Safety**

- GTK is **not thread-safe**; all GTK functions must be called from the main thread.
- Background tasks must marshal results to the GTK main loop using `g_idle_add()` or `g_main_context_invoke()`.

## 🔗 Bindings and Language Interoperability

### **Introspection and Bindings**

- Exposes complete API via **GObject Introspection**, enabling automatic binding generation for:
    - Python (PyGObject)
    - JavaScript (GJS)
    - Rust (gtk-rs)
    - Vala, and others
- IDL-like `.gir` and `.typelib` metadata describe APIs in machine-readable form.

## 🖥️ Platform Abstraction

### **Backend Modularization**

- Abstracted through **GDK (GIMP Drawing Kit)** layer, which isolates windowing system interactions.
- GDK backends include:
    - X11 (`GdkX11`)
    - Wayland (`GdkWayland`)
    - Windows (`GdkWin32`)
    - macOS (`GdkQuartz`, deprecated)

## 📦 Build System and Distribution

### **Build System**

- Uses **Meson** build system in GTK 4, previously Autotools.
- Modularized into several components: `glib`, `pango`, `gdk-pixbuf`, `atk`, `gtk`.

### **Dependency Stack**

- GLib (core utilities)
- GObject (OOP and signals)
- GDK (windowing + input abstraction)
- Pango (text layout and internationalization)
- Cairo (2D graphics, GTK 3)
- GSK (scene graph, GTK 4)
- GIO (I/O abstractions)

## 🧩 GTK3 & GDK Environment Variables

> 

| **Variable** | **Purpose** | **Description** |
| --- | --- | --- |
| `GTK_DEBUG` | Debugging | Enables various GTK3 internal debug modes; includes widget tree, signals, etc. |
| `GTK_MODULES` | Accessibility / Extensions | Loads additional GTK3 modules like accessibility bridges. |
| `GTK_THEME` | Theming | Forces GTK3 to use a specific theme and variant. |
| `GTK_PATH` | Resource lookup | Adds directories to search for themes, modules, icons, etc. |
| `GTK_IM_MODULE` | Input Method | Sets the GTK input method module (IME) used for complex text input. |
| `GTK_CSD` | Window Decorations | Enables (1) or disables (0) client-side decorations (CSD). |
| `GTK_OVERLAY_SCROLLING` | Scrolling Behavior | Enables or disables overlay scrollbars (touch-friendly UI). |
| `GTK_PRINT_BACKENDS` | Printing | Chooses which print backends to enable (like `file`, `cups`, `lpr`). |
| `GTK_EXE_PREFIX` | Development Overrides | Overrides prefix used to locate runtime files like schemas and resources. |
| `GTK_DATA_PREFIX` | Development Overrides | Overrides data directory lookup. |
| `GTK_INSPECTOR_DISPLAY` | GTK Inspector | Forces GTK Inspector to appear on a specific display/screen. |
| `GTK_INSPECTOR_KEY` | GTK Inspector | Customizes the keybinding to open the GTK3 Inspector. |
| `GTK_DISABLE_DEPRECATED` | Build Configuration | Hides use of deprecated GTK APIs at compile time. |
| `GDK_DEBUG` | Debugging | Set the GDK backend: x11, wayland, broadway, etc. |
| GDK_BACKEND | Backend Selection | Enable debug output for GDK. Example flags: events, updates, frames, clipboard, etc. |
| GDK_SCALE | HiDPI Scaling | Force scaling factor for HiDPI displays (e.g., 2 for 200%). |
| GDK_DPI_SCALE | HiDPI Fractional Scaling | Additional fractional scaling (e.g., 0.75) on top of GDK_SCALE. |
| GDK_SYNCHRONIZE | X11 Debugging | Forces synchronous GDK-to-X11 calls (useful for debugging but slows performance). |

### `GTK_DEBUG` flags:

- `updates` – Paint region updates
- `resize` – Widget resize requests
- `layout` – GtkLayout debug
- `text` – Text rendering
- `tree` – Widget tree updates
- `signals` – Signal emissions
- `bindings` – Key/mouse binding resolution
- `interactive` – Enables GTK Inspector
- `modules` – Module loading
- `icon_theme` – Icon loading

### `GDK_DEBUG` flags:

- `events` – Input events
- `dnd` – Drag and drop
- `clipboard` – Clipboard operations
- `frames` – Frame clock
- `gl` – OpenGL rendering details
- `cairo` – Cairo rendering backend

## Debugging

> 

### Summary

- ltrace
- GTK Inspector
- Interposing
- perf record -e 'probe_libgtk:gtk_button_new' -p $(pidof your-gtk3-app)
- valgrind --tool=callgrind ./your-gtk3-app
- strace
- LD_AUDIT
- LD_PRELOAD
- xtruss → https://www.chiark.greenend.org.uk/~sgtatham/xtruss/ [Note I Try This and It Works]

### 🧪 GTK Inspector

> **GTK Inspector** is a **runtime introspection and debugging tool** built into **GTK** (starting from **GTK** 3.14). It allows developers to **visually inspect and manipulate the widget hierarchy, properties, signals, CSS styling, and rendering details** of a running GTK application.
> 

```bash
gsettings set org.gtk.Settings.Debug enable-inspector-keybinding true
GTK_DEBUG=interactive ./main
```

### Interposing

> 

### X11 Interaction

- xtrace
- GDK_DEBUG
- strace
- ltrace
- LD_PRELOAD
- Create a Fake x-11 Socket → Then  Re-Route the calls to the real server.

## Development Ecosystem

> 

| Feature | **GTK** |
| --- | --- |
| GUI Designer Tool | Glade (for GTK3) |
| IDE Support | GNOME Builder, VS Code, etc. |
| Documentation | Good (GNOME Dev Docs) |
| Build System | `Meson`, `Autotools`, `CMake` |
| Licensing | LGPL |
| Static Linking | Harder to do legally |

## Performance

> 

| Area | GTK |
| --- | --- |
| Startup Time | Generally faster |
| Runtime Performance | GTK4 with Vulkan catching up |
| Memory Usage | Lower in raw GTK3 |
| GPU Acceleration | GTK4’s new rendering stack is fast |

## 🧠 Developer Experience

> 

| **Aspect** | **GTK** |
| --- | --- |
| Learning Curve | Higher (C + GObject) |
| Debugging UI | Glade & logs |
| Productivity | Medium |
| Code Verbosity | Higher (manual boilerplate) |

## Case Studies

> https://github.com/valpackett/awesome-gtk
> 

## References

- https://en.wikipedia.org/wiki/GTK
- https://github.com/dbremont/visiotecnica-labs
- https://github.com/dbremont/language-system-labs/
- https://www.gtk.org/docs/
- [https://gitlab.gnome.org/GNOME/gtk/-/tree/gtk-3-24/](https://gitlab.gnome.org/GNOME/gtk/-/tree/gtk-3-24/)
- Docs
    - [https://docs.gtk.org/gtk3/](https://docs.gtk.org/gtk3/)
    - [https://docs.gtk.org/gdk3/](https://docs.gtk.org/gdk3/)
    - [https://docs.gtk.org/glib/](https://docs.gtk.org/glib/)
    - [https://docs.gtk.org/gobject/](https://docs.gtk.org/gobject/)
    - [https://docs.gtk.org/Pango/](https://docs.gtk.org/Pango/)
    - [https://www.cairographics.org/manual/cairo-Paths.html#](https://www.cairographics.org/manual/cairo-Paths.html#)
    - [https://docs.gtk.org/gio/](https://docs.gtk.org/gio/)
- https://askubuntu.com/questions/597259/how-do-i-open-gtk-inspector
- https://developer.gnome.org/documentation/index.html
- https://xrl1.sh/posts/Leveraging-LD_AUDIT/
- [X Window System (X11 Version)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/x-window-system-x11-version.md)
- …