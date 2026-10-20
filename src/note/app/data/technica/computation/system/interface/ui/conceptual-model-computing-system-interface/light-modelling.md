# Light Modelling


> In computer graphics, imaging, and related fields, **light theories** play a crucial role in simulating how light interacts with surfaces, materials, and environments. These theories are used to create realistic visuals, whether for rendering 3D scenes, processing images, or simulating physical phenomena.
> 

## Theory of Lights

> 

| **Theory** | **Description** | **Applications** | **Key Concepts / Limitations** |
| --- | --- | --- | --- |
| **Geometric Optics** | Treats light as rays that travel in straight lines and interact with surfaces through reflection and refraction. | Ray Tracing, Shadow Mapping, Reflections and Refractions | Does not account for wave-like properties (e.g., diffraction, interference). |
| **Wave Optics** | Models light as a wave, accounting for diffraction, interference, and polarization. | Holography, Anti-Aliasing, Diffraction Effects | Computationally expensive for real-time applications. |
| **Radiometry** | Measures physical properties of light, such as intensity, flux, and radiance. | Global Illumination, HDR Imaging, Light Probes | Radiance (light energy per unit area/solid angle), Irradiance (light energy received by a surface). |
| **Photometry** | Measures light as perceived by the human eye, accounting for brightness and color sensitivity. | Tone Mapping, Color Theory, Lighting Design | Luminance (perceived brightness), Luminous Flux (total perceived light emitted). |
| **Color Theory** | Studies how colors are created, combined, and perceived. | Color Spaces (RGB, CMYK, HSV), Color Grading, Material Shading | Additive vs. Subtractive Color Mixing. |
| **Physically Based Rendering (PBR)** | Uses physical laws to simulate light interactions with materials. | Realistic Material Shading, Energy Conservation | BRDF (Bidirectional Reflectance Distribution Function), Fresnel Effect. |
| **Global Illumination** | Simulates indirect lighting by accounting for light bouncing between surfaces. | Path Tracing, Radiosity, Photon Mapping | Direct vs. Indirect Lighting. |
| **Participating Media** | Models light interactions with volumetric materials like fog, smoke, or water. | Volumetric Lighting, Subsurface Scattering | Absorption (light absorbed), Scattering (light redirected by particles). |
| **Polarization** | Studies the orientation of light waves and their interactions with materials. | Anti-Glare Effects, Material Analysis | Brewster’s Angle (perfect polarization of light). |
| **Quantum Optics** | Studies light at the quantum level, including photon emission and absorption. | Quantum Rendering, Photon Mapping | Highly theoretical, computationally intensive. |