# Matplotlib


> Matplotlib provides a number of core abstractions to handle various aspects of plotting. These abstractions are structured in layers, from low-level components to higher-level objects that users typically interact with.
> 

> Matplotlib's architecture is built around a layered design, comprising the **scripting interface (pyplot)** for quick plotting, the **object-oriented API** for detailed control, and the **backends** that handle rendering to various outputs like screens or files.
> 

## Core Abstraction

 Here is a table outlining these core abstractions:

| **Abstraction** | **Description** |
| --- | --- |
| **Figure** | The top-level container for everything in a plot. A figure can contain multiple subplots (Axes). |
| **Axes** | Represents a single plot or graph within a Figure. A Figure can have multiple Axes (subplots). |
| **Axis** | Represents the x-axis or y-axis of an Axes. Handles tick marks, labels, and limits. |
| **Artist** | The base class for all objects that are rendered in the plot (e.g., text, lines, patches). |
| **Line2D** | Represents a line in 2D space, used to draw lines and markers in plots. |
| **Patch** | Represents 2D shapes like rectangles, circles, polygons. |
| **Text** | Handles text elements in a plot, including titles, axis labels, and annotations. |
| **Tick** | Represents the ticks (markers) along an axis, controlling the appearance of tick marks and labels. |
| **Spine** | The borders of the plot where the axes are drawn. |
| **Transform** | Manages coordinate transformations from data coordinates to plot (display) coordinates. |
| **FigureCanvas** | Represents the area where the Figure is drawn; handles the drawing surface for the Figure. |
| **Renderer** | Backend-specific object that handles the rendering of artists (e.g., drawing lines or text). |
| **Event** | Represents user interaction events (mouse clicks, key presses) that trigger callbacks. |
| **Path** | Encapsulates complex lines and shapes via a sequence of points. |
| **Colormap** | A mapping from data values to colors, used for coloring plots. |
| **Locator** | Controls where ticks are placed on an axis. |
| **Formatter** | Controls the format of the tick labels (e.g., scientific notation, percentages). |

## Matplotlib Backends

Matplotlib supports various backends to manage rendering and user interaction, categorized into two types:

- **Interactive Backends**, which display plots in windows and allow real-time interaction, and
- **Non-Interactive (Hardcopy) Backends**, which generate static output like image or PDF files.

**List of backeds:**

```python
// setting backends

import matplotlib
matplotlib.use('QtAgg')  # Use the QtAgg backend

// or with env variables
$ MPLBACKEND=TkAgg python myscript.py

// for jupyter 
%matplotlib ipympl

```

**List of Backends:**

> 

| **Backend** | **Type** | **Description** | **Platforms** | **Notes** |
| --- | --- | --- | --- | --- |
| **QtAgg** | Interactive | Agg rendering to a Qt window. | Linux, Mac, Windows | Requires `PyQt5` or `PySide2` to be installed. |
| **TkAgg** | Interactive | Agg rendering to a Tk window. | Linux, Mac, Windows | Requires Tkinter (usually installed with Python). |
| **WXAgg** | Interactive | Agg rendering to a wxPython window. | Linux, Mac, Windows | Requires `wxPython`. |
| **GTK3Agg** | Interactive | Agg rendering to a GTK3 window. | Linux, Mac | Requires `PyGObject` and `GTK3`. |
| **MacOSX** | Interactive | Native macOS windowing. | Mac | Only available on macOS systems. |
| **nbAgg** | Interactive | Interactive backend for Jupyter notebooks, using the IPython display framework. | Cross-platform | Requires `IPython` and `notebook` packages. |
| **ipympl** | Interactive | Interactive backend for Jupyter notebooks, based on `ipywidgets`. | Cross-platform | Requires `ipympl` package. |
| **WebAgg** | Interactive | Renders plots to a web browser window, enabling interaction from a browser. | Cross-platform | Used for remote viewing, requires Tornado and HTML5. |
| **Agg** | Non-Interactive | High-quality rendering, but non-interactive. Can be used for saving plots, not for displaying in a window. | Cross-platform | No interaction capabilities, raster-based. |
| **SVG** | Non-Interactive | Scalable Vector Graphics (SVG) format. | Cross-platform | Produces vector graphics in SVG format. |
| **PDF** | Non-Interactive | Portable Document Format (PDF). | Cross-platform | Generates vector graphics in a PDF file. |
| **PS** | Non-Interactive | PostScript format. | Cross-platform | Produces vector graphics in PostScript format. |
| **Cairo** | Non-Interactive | Vector and raster output using the Cairo library. | Cross-platform | Supports various formats, including PNG, PDF, SVG. |

## **Dependencies**

> 

| **Category** | **Dependency** | **Description** |
| --- | --- | --- |
| **Core** | Python (≥ 3.8) | Required runtime for Matplotlib. |
|  | NumPy (≥ 1.21.0) | Handles numerical operations for plotting. |
|  | Pillow (≥ 6.2.0) | Enables image reading/writing (PNG, JPG). |
|  | pyparsing (≥ 2.3.1) | Parses mathematical expressions in plots. |
|  | packaging (≥ 20.0) | Manages version compatibility. |
|  | fonttools (≥ 4.22.0) | Handles font rendering and management. |
|  | kiwisolver (≥ 1.0.1) | Optimizes plot layout calculations. |
|  | cycler (≥ 0.10.0) | Manages color/style cycles in plots. |
| **GUI Backends** | Tkinter (TkAgg) | Default GUI backend (requires `python3-tk` on Linux). |
|  | PyQt5 / PyQt6 (QtAgg) | Qt-based backend for interactive plots. |
|  | PySide2 / PySide6 (QtAgg) | Alternative Qt bindings. |
|  | GTK 3/4 (GTKAgg) | GTK-based backend (needs `PyGObject`). |
| **Headless** | Agg | Non-interactive backend for PNG/PDF/SVG output. |
|  | freetype | Renders fonts in plots (required for Agg). |
|  | libpng | Handles PNG image generation (required for Agg). |
| **Animations** | FFmpeg | Encodes video animations (e.g., MP4). |
|  | ImageMagick | Creates animated GIFs. |
| **LaTeX Support** | texlive-latex-extra (Linux) | Renders text with LaTeX in plots. |
|  | MacTeX (macOS) | LaTeX distribution for macOS. |
| **Optional** | Tornado (WebAgg) | Web server for interactive browser-based plots. |
|  | ipympl | Jupyter notebook integration. |

## References

- https://aosabook.org/en/v2/matplotlib.html
- https://matplotlib.org/
- [Matplotlib tutorial for beginners](https://www.kaggle.com/code/prashant111/matplotlib-tutorial-for-beginners)
- https://matplotlib.org/ipympl/