# Simple and Fast Multimedia Library (SFML)

> 

## Install

```bash
# https://www.sfml-dev.org/download/sfml/3.0.0/
sudo apt update
sudo apt install libsfml-dev
```

## Core Abstractions

> The Simple and Fast Multimedia Library (SFML) provides several core abstractions that simplify the development of multimedia applications.
> 

### Core Abstractions of SFML

| **Abstraction** | **Description** | **Details** |
| --- | --- | --- |
| **Window** | Manages the creation and manipulation of application windows and handles input events. | **Classes**: `sf::Window`, `sf::RenderWindow`.<br>**Functions**: Creating windows, handling events, etc. |
| **Graphics** | Provides classes for drawing 2D shapes, sprites, and text on the screen. | **Classes**: `sf::Drawable`, `sf::Shape`, `sf::Sprite`, `sf::Text`.<br>**Functions**: Drawing primitives, textures. |
| **Audio** | Manages playback of sound and music, including streaming and effects. | **Classes**: `sf::Sound`, `sf::Music`, `sf::SoundBuffer`, `sf::SoundStream`.<br>**Functions**: Sound effects, background music. |
| **Network** | Provides functionality for network communication, including TCP and UDP. | **Classes**: `sf::TcpSocket`, `sf::UdpSocket`, `sf::TcpListener`, `sf::SocketSelector`.<br>**Functions**: Sending and receiving data, managing connections. |
| **System** | Offers basic system utilities such as time management, file handling, and threading. | **Classes**: `sf::Clock`, `sf::Time`, `sf::Thread`, `sf::Mutex`, `sf::FileInputStream`, `sf::FileOutputStream`.<br>**Functions**: Time measurement, multi-threading, file operations. |
| **Input** | Provides access to user input via keyboard, mouse, and joystick. | **Classes**: `sf::Keyboard`, `sf::Mouse`, `sf::Joystick`.<br>**Functions**: Detecting key presses, mouse events, joystick movements. |

## Graphics Abstractions

> Here's a table summarizing the **core graphics abstractions** in **SFML (Simple and Fast Multimedia Library)**:
> 

| **Abstraction** | **Description** | **Classes** | **Functions/Methods** |
| --- | --- | --- | --- |
| **Window** | Manages the creation and handling of windows where graphics are rendered. | `sf::Window`, `sf::RenderWindow` | `create()`, `clear()`, `display()`, `pollEvent()`, `setView()` |
| **Drawable** | Base class for all objects that can be drawn to the screen. | `sf::Drawable` | `draw()`, `setPosition()`, `setRotation()`, `setScale()` |
| **Shape** | Base class for geometric shapes such as circles and rectangles. | `sf::Shape`, `sf::CircleShape`, `sf::RectangleShape`, `sf::ConvexShape` | `setRadius()`, `setSize()`, `setPointCount()` |
| **Sprite** | Represents a drawable image or texture. | `sf::Sprite` | `setTexture()`, `setTextureRect()`, `setOrigin()`, `setColor()` |
| **Text** | Represents drawable text using a font. | `sf::Text` | `setFont()`, `setString()`, `setCharacterSize()`, `setFillColor()` |
| **Texture** | Represents an image that can be used as a texture for sprites and shapes. | `sf::Texture` | `loadFromFile()`, `loadFromImage()`, `setSmooth()` |
| **RenderTarget** | Base class for all objects that can receive drawing operations (e.g., windows, textures). | `sf::RenderTarget`, `sf::RenderWindow`, `sf::RenderTexture` | `draw()`, `setView()`, `getView()` |
| **RenderStates** | Represents the state of the renderer (e.g., transformations, blending). | `sf::RenderStates` | `setBlendMode()`, `setTransform()`, `setTexture()` |
| **View** | Represents a 2D view used for controlling what part of the scene is visible. | `sf::View` | `setCenter()`, `setSize()`, `setRotation()`, `reset()`, `zoom()` |
| **Transform** | Provides transformations (e.g., translation, rotation, scaling) for drawable objects. | `sf::Transform`, `sf::Transformable` | `translate()`, `rotate()`, `scale()`, `getTransform()` |

### Core Dependencies

> **SFML (Simple and Fast Multimedia Library)** has several dependencies that need to be installed on your system to use it effectively.
> 

> Here’s a table summarizing the dependencies for SFML:
> 

| **Dependency** | **Description** | **Platform Installation** | **Additional Notes** |
| --- | --- | --- | --- |
| **OpenGL** | Cross-platform API for 2D and 3D graphics rendering. | Typically bundled with graphics drivers or manually installed. | Essential for graphics rendering. |
| **GLU (OpenGL Utility Library)** | Provides utility functions for OpenGL. | Usually included with OpenGL packages. | Optional but commonly used with OpenGL. |
| **GLEW (OpenGL Extension Wrangler Library)** | Manages OpenGL extensions for advanced features. | Install via package managers or from [GLEW's website](http://glew.sourceforge.net/). | Useful for extended OpenGL functionality. |
| **Freetype** | Library for font rendering. | Available from package managers or [Freetype's website](https://www.freetype.org/). | Used for text rendering in SFML. |
| **ALSA (Advanced Linux Sound Architecture)** or **OpenAL** | Handles audio functionalities. OpenAL for cross-platform 3D audio; ALSA for Linux. | **Linux**: Install via package managers (`libopenal-dev`, `libasound2-dev`).<br>**Windows/macOS**: OpenAL is bundled with SFML or available from [OpenAL's website](https://www.openal.org/). | ALSA is specific to Linux; OpenAL is cross-platform. |
| **X11** (on Linux) | Provides graphical windowing system on Linux. | Typically installed via package managers (`libx11-dev`). | Necessary for window management on Linux. |
| **pthread** (POSIX threads) | Provides multithreading support. | Usually included with Linux distributions; `libpthread` library. | Essential for multithreading support. |
| **Graphics Libraries** | Additional libraries for extending graphics capabilities (e.g., shaders). | Installation varies depending on specific libraries. | Optional, depends on additional features. |
| **Network Libraries** | Used for networking functionality. | Typically included with SFML's networking module. | May have additional dependencies. |

## `libsfml-dev`

| **SFML Module** | **Depends On (Examples)** |
| --- | --- |
| `sfml-system` | pthread (Linux), stdlib |
| `sfml-window` | X11, WinAPI, Cocoa |
| `sfml-graphics` | OpenGL, FreeType, libjpeg/libpng |
| `sfml-audio` | OpenAL, libFLAC, libVorbis |
| `sfml-network` | Sockets (BSD sockets / Winsock) |

## What value does `sfml` add?

🔧 How SFML Uses OpenGL:

- `sf::RenderWindow` creates an OpenGL context.
- `sf::Texture`, `sf::Sprite`, etc., map directly to OpenGL textures and quads.
- It handles:
    - Viewports
    - Double buffering
    - GPU memory management
    - Event polling (via OS-specific backends)

---

## References

- [https://www.sfml-dev.org/learn.php](https://www.sfml-dev.org/learn.php)
- …