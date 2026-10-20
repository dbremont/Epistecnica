# Texture

> A **texture** is often a 2D image applied to a 3D model’s surface to simulate the appearance of materials like wood, stone, or fabric, without modeling the actual physical detail.
> 

> An **image texture** is the small-scale structure perceived on an image, based on the spatial arrangement of color or intensities.
> 

## Denotation

| **Domain** | **Denotation of "Texture"** |
| --- | --- |
| **Material Science** | The spatial arrangement and orientation of the grains or crystals in a solid material. |
| **Food Science** | The physical feel and consistency of a food product as perceived by touch or mouthfeel. |
| **Textiles & Fabric** | The surface quality or structure of a fabric as determined by weave, fiber, or finish. |
| **Visual Arts** | The perceived surface quality of a work of art, either actual (tactile) or implied (visual). |
| **Computer Graphics** | A bitmap image applied to the surface of a 3D model to provide detail or realism. |
| **Geology** | The size, shape, and arrangement of mineral grains in a rock. |
| **Botany** | The surface quality of a plant part, such as leaf or bark, as felt or seen. |
| **Music (Sound)** | The overall quality of a musical composition as determined by the number and type of layers. |
| **Linguistics** | The coherence and structural quality of a written or spoken discourse (rare usage). |
| **Architecture** | The tactile or visual surface quality of a material or building finish. |

## Programming Abstraction

| Connotation | Description |
| --- | --- |
| **Texture Object** | An encapsulated GPU resource that stores an image or image array (1D, 2D, 3D, or cube map). Often an instance of a `Texture` class in engine code. |
| **Texture Handle / ID** | A low-level identifier (e.g., GLuint in OpenGL) used to bind a texture to a rendering pipeline stage. |
| **Shader Resource** | Textures are passed to shaders (usually fragment shaders) as read-only inputs to determine surface color, normals, etc. |
| **Sampler Object** | Paired with a texture; defines how texture is accessed (filtering, wrapping, etc.). |
| **Binding Slot / Unit** | Textures are bound to specific slots in the GPU for use during rendering (e.g., texture unit 0). |
| **Texture Format** | Defines how data is stored (e.g., RGBA8, RGB16F, DXT1). Affects memory layout and shader access. |

## References

- https://en.wikipedia.org/wiki/Image_texture