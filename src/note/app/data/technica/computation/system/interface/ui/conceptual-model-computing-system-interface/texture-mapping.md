# Texture Mapping


> **Texture mapping** is a computer graphics technique used to apply a 2D image (called a **texture**) onto a 3D model’s surface to give it more detail, color, and realism. Instead of creating intricate details directly in the geometry of the 3D model (which would require more computing power), texture mapping allows the model to appear detailed by wrapping an image around it.
> 

### Key Concepts:

1. **Texture**: A 2D image or pattern (like wood grain, brick, or metal) that is applied to the surface of a 3D model. Textures can simulate materials, colors, and even imperfections like scratches.
2. **UV Mapping**: This process involves "unwrapping" the 3D model into a flat 2D space, where each part of the model corresponds to coordinates (U and V, which are analogous to X and Y) on the texture image. This lets the texture wrap smoothly around the object.
3. **Shader**: A shader is a program that runs on the GPU, and it decides how textures are applied to the model, influencing how light interacts with the surface of the object. Texture mapping works closely with shaders to create realistic lighting, shading, and surface appearances.
4. **Types of Texture Mapping**:
    - **Diffuse Mapping**: The basic texture that gives the model its color or material appearance.
    - **Normal Mapping**: A technique used to simulate small surface details like bumps and wrinkles without adding more geometry.
    - **Specular Mapping**: Used to control the shininess or reflectiveness of the surface.
    - **Bump Mapping**: Simulates texture height and depth, like creating the illusion of raised or recessed surfaces.

### Applications:

- **Video Games**: Texture mapping allows game environments and characters to appear detailed without having to render every detail in 3D.
- **Movies and Animation**: Used extensively in CGI to create realistic environments, characters, and objects.
- **Virtual Reality and Augmented Reality**: Enhances realism in virtual environments.

## Refereces

- https://en.wikipedia.org/wiki/Texture_mapping