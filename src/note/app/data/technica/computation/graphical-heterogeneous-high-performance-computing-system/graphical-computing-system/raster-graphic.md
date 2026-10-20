# Raster Graphic

> A **raster graphic** (also called a **bitmap**) is a type of digital image composed of a grid of individual pixels (picture elements), each with a defined color. It’s one of the two main types of computer graphics—the other being **vector graphics**.
> 

## Key Characteristics

- **Pixel-based**: Made up of a fixed number of pixels (e.g., 1920×1080).
- **Resolution-dependent**: Scaling up can cause pixelation or blurring.
- **Rich detail**: Ideal for complex images like photographs.

## Common Formats

- **JPEG** (.jpg) – Lossy compression; common for photos.
- **PNG** (.png) – Lossless; supports transparency.
- **GIF** (.gif) – Supports animation; limited color palette.
- **BMP**, **TIFF**, **WEBP**

## Uses

- Digital photography
- Web graphics
- Digital painting
- Textures in 3D models

## Pros

- High detail and color depth
- Widespread support

## Cons

- Large file sizes (especially lossless formats)
- Loses quality when resized

## **GIMP**

> 

| **Workflow** | **Task** | **Description** |
| --- | --- | --- |
| 🎨 Basic Image Editing | Crop Image | Remove unwanted outer areas to focus or reframe the image. |
|  | Resize/Scale Image | Change image dimensions to fit specific use cases (e.g., web, print). |
|  | Adjust Brightness/Contrast | Modify tonal range to improve visibility or aesthetics. |
|  | Adjust Hue/Saturation | Change overall color tones or increase color intensity. |
|  | Sharpen Image | Enhance edge definition and detail clarity. |
|  | Blur Image | Soften parts of the image for depth, focus shift, or aesthetic effect. |
| 🧹 Photo Retouching | Clone/Heal | Duplicate or fix areas to remove blemishes, objects, or flaws. |
|  | Dodge/Burn | Lighten (dodge) or darken (burn) specific regions to enhance form and focus. |
|  | Warp Transform (Liquify) | Reshape image areas non-destructively for correction or artistic effects. |
| 🖼️ Compositing & Layering | Layer Composition | Combine multiple layers to build complex visuals. |
|  | Apply Blending Modes | Use math-based blending (e.g., Multiply, Overlay) for creative or photorealistic effects. |
|  | Add Layer Masks | Create transparency gradients or selective visibility without permanent changes. |
|  | Add Alpha Channel | Enable transparency on layers for clean cutouts and compositing. |
| ✍️ Digital Art & Painting | Use Custom Brushes | Apply varied textures, shapes, and dynamics while painting. |
|  | Use Brush Dynamics | Adjust brush response based on pressure, tilt, or speed from tablet/stylus input. |
|  | Draw with Tablet | Utilize pen input for pressure-sensitive, natural drawing or inking. |
| 🧰 Graphic/UI Design | Add and Style Text | Insert and customize text for posters, interfaces, or layouts. |
|  | Use Guides and Grids | Align elements precisely using non-printing visual aids. |
|  | Create Shapes with Paths Tool | Design curves and custom shapes with bezier paths. |
| 🧪 Export & Optimization | Export in Web Formats | Save in web-friendly formats like JPEG, PNG, WebP with control over quality. |
|  | Adjust Compression Settings | Balance image quality and file size by tweaking export parameters. |
|  | Optimize for GIF | Reduce file size of animations using palette and frame optimization. |
| 🧱 Batch Processing | Batch Resize/Convert Images | Automate repetitive tasks on multiple files with one operation. |
|  | Use Scripting (Script-Fu/Python) | Write scripts for custom batch operations, plugin development, or parameterized edits. |

## Layer System

> In **GIMP**, a **layer** is like a transparent sheet stacked on top of other sheets, each holding part of your image. Together, these layers make up the full image—just like in traditional collage or animation cel art.
> 

### 🧱 **Conceptual Meaning**

A **layer** is a separate image plane that can contain:

- Color pixels
- Transparency (alpha)
- Text, shapes, or photos
- Effects or adjustments

### 🛠️ **Key Properties of Layers**

| **Property** | **Meaning** |
| --- | --- |
| **Visibility (👁️)** | You can hide/show layers without deleting them. |
| **Opacity** | Controls how transparent the layer is (0–100%). |
| **Blending Mode** | Defines how the layer mixes with those beneath it (e.g., Multiply, Overlay). |
| **Alpha Channel** | Allows transparency in the layer. |
| **Masks** | Let you control the visibility of parts of the layer without erasing. |
| **Locking** | Prevents unintended edits to pixels, position, or transparency. |

### 🖼️ **Practical Uses**

- Stack a **background photo**, a **logo**, and **text** on separate layers so you can move or edit each one individually.
- Use a layer for **non-destructive retouching**, such as healing or color grading.
- Create **animations** with each frame on a different layer.

## QA

### 🟢 **Basic Knowledge**

1. What is a raster image, and how does it differ from a vector image?
2. What happens when you enlarge a raster image beyond its original resolution? Why?
3. In GIMP, what is the function of the crop tool?
4. What menu would you use to adjust brightness and contrast in GIMP?
5. How do you export a GIMP project to a JPEG or PNG file?

### 🟡 **Intermediate Concepts**

1. What is a layer in GIMP, and why are layers important in raster image editing?
2. Describe the difference between the Clone Tool and the Healing Tool. When would you use each?
3. How do layer masks work, and why are they considered non-destructive?
4. What is the purpose of blending modes in GIMP? Name and explain at least two.
5. What does adding an Alpha Channel to a layer enable you to do?
6. How can you make text editable in GIMP even after saving and re-opening the file?
7. What is the difference between saving a file as `.XCF` and exporting as `.PNG`?

### 🔵 **Advanced & Technical**

1. What are the advantages and limitations of using GIMP for professional photo retouching compared to Photoshop?
2. Explain how you would batch convert 100 images to grayscale using GIMP.
3. Describe how brush dynamics can be used to simulate pressure sensitivity on a drawing tablet.
4. What’s the role of guides and snapping in layout design within GIMP?
5. How would you simulate a film grain or texture overlay effect using layers?
6. How does GIMP handle color profiles, and what impact do they have on image export and printing?
7. Can GIMP natively handle non-destructive adjustment layers like Photoshop? If not, what is the alternative workflow?
8. How would you optimize a multi-layer GIMP animation for export as a GIF with the smallest possible file size?

## References

- https://en.wikipedia.org/wiki/Raster_graphics
- [X Window System (X11 Version)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/x-window-system-x11-version.md)
- https://en.wikipedia.org/wiki/Photographic_composition