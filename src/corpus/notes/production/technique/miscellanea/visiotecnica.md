---
tags: [note, production]
---

# Visiotecnica

> REFACTOR THIS AND MOVE SOME AREAS RELATED WITH UI; TO COMPUTATION.
> 

> Visualization  Technique:  Data - Sense → Visual Representation.
> 

> Note:  A Try to re-compose and organize a very sparse idea in many  cross-cutting fields.
> 

> A **Vision System** is an integrated set of hardware and software components designed to **acquire, process, analyze, and interpret visual information** from the physical environment to perform automated inspection, measurement, guidance, or identification tasks.
> 

> Note: The Visualization labs are distributed across  https://github.com/csiglab/visualization-lab,  https://github.com/dbremont/linux-api-labs and https://github.com/dbremont/visiotecnica-labs.
> 

## Index

## 🧭 **Meta-Structural Taxonomy**

> ***Representational Form;  Ontological Target; Encoding Technique; Dimensionality;  Purpose / Epistemic Function;  Domain / Disciplinary Context;  Medium / Interface.***
> 

| Dimension | Key Question |
| --- | --- |
| **Form** | How is it rendered? |
| **Target** | What does it show? |
| **Encoding** | How is info mapped? |
| **Dimensionality** | What spatial/temporal axes? |
| **Function** | Why is it used? |
| **Domain** | Where is it used? |
| **Medium** | How is it delivered? |

### ***Modality / Representational Form***

**What is the *form* or *type* of the representation?**

- Image (photo, satellite, microscopy)
- Diagram (flowchart, circuit, pathway)
- Graph (network, tree, matrix)
- Plot (scatter, bar, violin, time series)
- Map (topographic, choropleth, geological)
- Model (3D CAD, anatomical, FEA mesh)
- Animation / Simulation (video, 3D dynamics)
- Symbolic (mathematical notation, logic gates)

### ***Ontological Target***

**What *phenomenon or entity* does it represent?**

- Physical structure (organs, molecules, terrain)
- Process / mechanism (biological pathway, engine cycle)
- System / network (neural network, power grid)
- Temporal dynamics (weather, kinetics, evolution)
- Statistical distribution (data populations, correlation)
- Abstract logic / rules (algorithms, state transitions)
- Human-system interaction (UI mockup, medical dashboard)

### ***Encoding Technique***

**How is information *encoded* into the visual space?**

- Position (X-Y plot)
- Shape (flowchart node shapes)
- Color (heatmap, Doppler, PET scans)
- Size (bubble chart, volumetrics)
- Orientation (vector fields, flow maps)
- Motion (animation, simulation)
- Layering / Transparency (CT overlays, GIS)
- Interactivity (hover states, clickable dashboards)

### ***Dimensionality***

**What *dimensions* are involved in the representation?**

- 0D: Symbol or icon
- 1D: Time series, waveform
- 2D: Static diagram, image, map
- 2.5D: Layered slices, top-down depth maps
- 3D: CAD models, anatomical 3D structures
- 4D: Dynamic 3D simulations, spatiotemporal evolution

### ***Purpose / Epistemic Function***

**What is the *goal* of the visualization?**

- **Exploratory** (discover patterns: heatmap, PCA)
- **Explanatory** (communicate known mechanisms: diagrams, animations)
- **Diagnostic** (identify states: radiograph, pathology)
- **Design** (create/plan: blueprints, mockups)
- **Predictive** (model outcomes: simulation)
- **Comparative** (before/after, cohorts)
- **Interactive / Operational** (dashboards, control panels)

### ***Domain / Disciplinary Context***

**In what *field or setting* is the visual used?**

- Medical (radiology, pathology, surgery)
- Engineering (mechanical, electrical, civil)
- Geosciences (GIS, remote sensing, geology)
- Life sciences (molecular, anatomical, ecological)
- Physics / Math (orbital models, topologies)
- Social sciences (networks, statistics)
- Computer science (UML, data structures, neural nets)

### ***Medium / Interface***

**How is the representation delivered or consumed?**

- Static 2D print
- Digital screen
- Interactive web (Plotly, D3)
- AR/VR environment
- Physical model (3D print, sculpture)
- Embedded display (e.g. in a cockpit, MRI scanner)

## **Visual Representation**

> Look this is just a basic structure of the  space of visual representations.
> 

| **Dimension** | **Form** | **Target** | **Encoding** | **Technique/Machine** | **File Formats** | **Dimensionality** | **Function** | **Domain** | **Medium/Tools** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **2D** | Photograph | Realistic depiction | Light/color/texture | DSLR, smartphone, microscope | JPEG, TIFF, RAW | Static | Documentation, analysis | Photography, Medicine | Digital/Print |
| **2D** | Vector Graphics | Scalable shapes | Paths/strokes/fills | Illustrator, CAD software | SVG, EPS, DWG | Static/Dynamic | Design, illustration | Engineering, Design | Adobe Illustrator |
| **2D/3D** | Raster Graphics | Pixel-based images | Pixel arrays | Digital painting, scanning | PNG, JPEG, WebP | Static | Digital art, photography | Gaming, Web | Photoshop |
| **2D** | Diagram (Flowchart/UML) | Conceptual relationships | Nodes/edges/labels | Lucidchart, Graphviz | PDF, VSDX | Static | Process modeling, education | Engineering, CS | Software |
| **2D/3D** | 3D Model | Spatial representation | Meshes/textures | 3D scanning, CAD modeling | OBJ, STL, FBX | Static/Dynamic | Simulation, prototyping | Medicine, Architecture | Blender, Maya |
| **2D** | Chart (Bar/Line) | Quantitative data | Axes/scales/colors | Python, R, Tableau | CSV, JSON | Static/Dynamic | Data analysis | Business, Science | Matplotlib, D3.js |
| **2D/3D** | Map (Geospatial) | Spatial data | Layers/contours/symbols | LIDAR, satellite imaging | GeoTIFF, Shapefile | Static/Interactive | Navigation, analysis | Geography, Urban Planning | ArcGIS, Google Maps |
| **3D/Immersive** | Light Fields | Volumetric light capture | Ray bundles | Plenoptic cameras (Lytro), NeRF | EXR, PLY | Dynamic | VR/AR, computational photography | Entertainment, Research | VR headsets |
| **2D** | Schematic (Circuit/P&ID) | Technical systems | Symbols/connections | Altium, AutoCAD | SCH, DWG | Static | Design, troubleshooting | Electronics, Engineering | CAD tools |
| **2D/3D** | Medical Imaging (MRI/CT / PET / SPECT **/** X-ray) | Anatomical structures | Voxels/density maps | MRI/CT scanners, ultrasound | DICOM, NIfTI | Static/Dynamic | Diagnosis, research | Medicine | OsiriX, 3D Slicer |
| **4D** | Time Series Plot | Temporal trends | Time-axis/markers | Pandas, MATLAB | HDF5, NetCDF | Dynamic | Trend analysis | Finance, Climate Science | Python, R |
| **3D** | Holography | Light-field projection | Interference patterns | Laser holography, Pepper’s Ghost | MP4, holographic video | Dynamic | Visualization, education | Research, Marketing | Holographic displays |
| **2D/3D** | Infographic | Information synthesis | Icons/text/layouts | Canva, Illustrator | PDF, PNG | Static | Communication | Education, Journalism | Digital/Print |
| **3D+** | AR/VR Scene | Immersive interaction | 3D models/spatial audio | Unity, Unreal Engine, LiDAR | USDZ, glTF | Interactive | Training, entertainment | Gaming, Medicine | VR/AR headsets |
|  |  |  |  |  |  |  |  |  |  |

## List of Domains

| **Visual Representation** | **Description** | **Field** |
| --- | --- | --- |
| **Bar Chart** | Represents categorical data with rectangular bars proportional to values. | Data Science, Mathematics, Medical Science |
| **Line Graph** | Displays data points connected by lines, showing trends over time. | Data Science, Mathematics, Physical Sciences, Engineering |
| **Scatter Plot** | Shows relationships between two numerical variables using dots. | Data Science, Mathematics, Physical Sciences, Medical Science |
| **Histogram** | Represents the distribution of numerical data using bins. | Data Science, Mathematics, Physical Sciences, Medical Science |
| **Pie Chart** | Displays proportions of a whole as slices of a pie. | Data Science, Medical Science |
| **Heatmap** | Represents data values as colors in a matrix format. | Data Science, Medical Science, Biology |
| **Box Plot (Whisker Plot)** | Summarizes data distribution through quartiles and outliers. | Data Science, Mathematics, Medical Science |
| **Violin Plot** | Combines a box plot with a kernel density plot. | Data Science, Medical Science |
| **Network Graph** | Represents relationships between entities as nodes and edges. | Data Science, Biology, Social Sciences |
| **Geospatial Map** | Visualizes data over geographical regions (e.g., choropleth, point maps). | Data Science, Architecture, Engineering |
| **3D Surface Plot** | Displays three-dimensional data as a surface. | Mathematics, Physical Sciences, Engineering |
| **Contour Plot** | Shows 3D data in 2D using lines of constant value (isolines). | Mathematics, Physical Sciences, Engineering |
| **Vector Field Plot** | Represents vectors (magnitude and direction) in space. | Mathematics, Physical Sciences, Engineering |
| **Phase Diagram** | Shows the stability of different phases of a substance under varying conditions. | Physical Sciences, Engineering |
| **Feynman Diagram** | Depicts particle interactions in quantum field theory. | Physics |
| **Circuit Diagram** | Represents electrical circuits using standardized symbols. | Engineering, Physics |
| **Free Body Diagram** | Illustrates forces acting on an object in mechanics. | Engineering, Physics |
| **Blueprint** | Technical drawing of architectural or engineering designs. | Architecture, Engineering |
| **Isometric Drawing** | 3D representation of an object with no perspective distortion. | Architecture, Engineering |
| **CAD Model** | Computer-aided design for precise 3D modeling. | Architecture, Engineering |
| **MRI/CT Scan** | Cross-sectional imaging of internal body structures. | Medical Science |
| **Microscopy Imaging** | Visual representation of microscopic structures (e.g., cells, tissues). | Medical Science, Biology |
| **ECG/EKG Waveform** | Graphical representation of electrical activity of the heart. | Medical Science |
| **Phylogenetic Tree** | Shows evolutionary relationships among species. | Biology, Medical Science |
| **Sankey Diagram** | Visualizes flow quantities between nodes (e.g., energy, materials). | Engineering, Data Science |
| **Gantt Chart** | Displays project schedules with start and end dates. | Engineering, Architecture, Data Science |
| **Finite Element Analysis (FEA) Visualization** | Displays stress, heat, or fluid flow simulations. | Engineering, Physical Sciences |
| **Bode Plot** | Graphs frequency response of a system in engineering. | Engineering |
| **Smith Chart** | Used in electrical engineering for impedance matching. | Engineering |
| **Architectural Rendering** | Artistic or photorealistic depiction of a building design. | Architecture |
| **Floor Plan** | 2D scaled diagram of a building’s layout. | Architecture |
| **Elevation Drawing** | Orthographic projection of a building’s façade. | Architecture |
| **Sectional View** | Cross-sectional cutaway of a structure to show interior details. | Architecture, Engineering |
| **Choropleth Map** | Uses color shading to represent statistical data (e.g., population density) across geographic regions. | GIS, Data Science, Urban Planning |
| **Dot Density Map** | Represents quantities using dots, where each dot signifies a specific value (e.g., population). | GIS, Demographics, Epidemiology |
| **Heatmap (Spatial)** | Shows density or intensity of point data (e.g., crime hotspots, traffic). | GIS, Data Science, Urban Analytics |
| **Proportional Symbol Map** | Uses scaled symbols (e.g., circles) to represent numerical values at locations. | GIS, Economics, Environmental Science |
| **Flow Map** | Displays movement (e.g., migration, trade) with lines of varying thickness. | GIS, Transportation, Logistics |
| **Isoline Map** | Uses lines to connect points of equal value (e.g., elevation, temperature). | GIS, Meteorology, Geology |
| **Topographic Map** | Represents terrain features (elevation, contours, water bodies) in detail. | GIS, Geology, Military, Hiking |
| **3D Terrain Model** | Digital elevation models (DEMs) rendered in 3D for landscape analysis. | GIS, Urban Planning, Environmental Science |
| **Land Use/Land Cover Map** | Classifies land into categories (e.g., forest, urban, agricultural). | GIS, Environmental Science, Agriculture |
| **Network Analysis Map** | Visualizes connectivity (e.g., roads, utilities) and optimal paths. | GIS, Transportation, Logistics |
| **Time-Series Animation** | Shows spatial changes over time (e.g., urban expansion, deforestation). | GIS, Climate Science, History |
| **Kernel Density Estimation (KDE) Map** | Estimates probability density of point events (e.g., earthquakes, disease cases). | GIS, Epidemiology, Geology |
| **Cartogram** | Distorts geographic space to represent a variable (e.g., population, GDP). | GIS, Economics, Political Science |
| **Viewshed Analysis Map** | Identifies visible areas from a specific point (e.g., for cell towers, scenic views). | GIS, Urban Planning, Defense |
| **Hydrological Map** | Displays water flow, watersheds, and drainage patterns. | GIS, Environmental Engineering, Hydrology |
| **Cadastral Map** | Shows property boundaries, ownership, and land parcels. | GIS, Real Estate, Government |
| **Geospatial Heatmap Overlay** | Superimposes heatmap data (e.g., traffic, pollution) on satellite imagery. | GIS, Smart Cities, Environmental Monitoring |
| **Vector Tile Map** | Efficient, scalable web maps with layered vector data (e.g., OpenStreetMap). | GIS, Web Mapping, Navigation |
| **Remote Sensing Imagery** | Satellite/aerial imagery analyzed for environmental or urban features. | GIS, Agriculture, Defense, Disaster Management |
| **Space-Time Cube** | Visualizes spatiotemporal data in 3D (location + time + variable). | GIS, Epidemiology, Crime Analysis |
| Mechanism Diagram | Shows biological or chemical mechanisms, such as enzyme action | Biology, Chemistry |
| Biological Pathway | Diagrams of metabolic or signaling networks | Biology |
| Genetic Circuit / Regulatory Diagram | Represents gene expression regulation and synthetic biology constructs | Synthetic Biology |
| Molecular Interaction Map | Visualizes protein-protein or molecular interactions | Molecular Biology |
| Evolutionary / Phylogenetic Tree | Displays evolutionary relationships | Biology, Evolution |
| Protein Structure | 3D visualization (ribbon, ball-and-stick, space-filling) | Structural Biology |
| DNA/RNA Sequence Visualization | Nucleotide-level depiction of genetic sequences | Genomics |
| Genome Browser View | Genomic data aligned to reference genomes | Genomics |
| Cytogenetic Karyogram | Visual layout of chromosomes | Genetics |
| Anatomical Chart | Labeled diagrams of the human or animal body | Medicine, Anatomy |
| Surgical Pathway Diagram | Depicts steps or decisions in surgical procedures | Medicine |
| Pathophysiological Process Map | Explains disease progression and related mechanisms | Pathology |
| Clinical Algorithm / Decision Tree | Step-by-step clinical decision rules | Medicine |
| Kaplan-Meier Curve | Survival probability over time | Medicine, Statistics |
| Forest Plot | Summarizes meta-analysis results | Epidemiology |
| X-ray | Radiographic image showing tissue/bone density | Medical Imaging |
| CT (Computed Tomography) | Cross-sectional 3D X-ray imaging | Medical Imaging |
| MRI / fMRI / MRS | Magnetic resonance imaging (anatomical and functional) | Medical Imaging |
| PET / PET-CT / PET-MRI | Visualizes metabolic activity or molecular targets | Medical Imaging |
| Ultrasound / Color Doppler | Sound-wave based imaging (e.g., blood flow) | Medical Imaging |
| Thermography | Heat-based imaging of surface temperatures | Medical Imaging |
| Microscopy (Light/Fluorescence/Confocal/AFM) | Visualizes microscopic structures and cells | Cell Biology, Nanotech |
| Electron Microscopy (SEM, TEM) | Imaging with electron beams for ultra-resolution | Structural Biology |
| Live-cell Imaging | Real-time cellular video microscopy | Cell Biology |
| Image Segmentation | Software-delineated organ/tumor regions | Medical Imaging, AI |
| 3D Reconstruction | Volumetric image rendering | Medical Imaging, Simulation |
| Overlay Visualization | Combines multiple imaging modalities (e.g., CT + PET) | Medical Imaging |
| Electrical / Electronic Circuit Diagram | Symbolic layout of circuits and components | Electrical Engineering |
| P&ID (Piping & Instrumentation Diagram) | Diagrams of industrial piping systems and control elements | Chemical, Industrial Eng. |
| Block Diagram | Abstract view of a system’s components and signals | Systems Engineering |
| Ladder Logic Diagram | Relay-based industrial control diagram | Industrial Automation |
| Assembly Diagram | Shows parts and how they fit together | Mechanical Engineering |
| Kinematic Diagram | Shows motion and joints in mechanisms | Robotics, Mechanical Eng. |
| CAD Drawing / Blueprint / Schematic | Scaled technical drawing for physical design | Architecture, Engineering |
| Isometric Projection | 3D-like representation of an object | Architecture, CAD |
| 3D Model / VR / AR Scene | Fully spatial object representation | Engineering, Education |
| System Dynamics Diagram | Feedback loops and stock-flow systems | Systems Theory, Simulation |
| State Transition Diagram | Models finite state machines | Computer Science |
| Sequence Diagram | Object and message flow in time | Software Engineering |
| Automata / Petri Net / Turing Machine Diagram | Formal visual models of computation | Computer Science |
| UML Diagram | Unified Modeling Language diagrams for software | Software Engineering |
| Matrix Visualization / Adjacency Matrix | Displays numerical or connectivity data in grid form | Data Science, Networks |
| Function Graph | Mathematical functions plotted over axes | Mathematics |
| Phase Space / Bifurcation Diagram | Dynamic system behavior over state variables | Physics, Math |
| Contour Plot / Vector Field | Fields and scalar levels visualized spatially | Physics, Engineering |
| Polar Plot / Complex Plane | Circular coordinate systems or complex number plots | Math, Signal Processing |
| Parametric / Implicit Plot | Non-cartesian function plots | Mathematics |
| Time Series Plot | Value trends over time | Statistics, Finance |
| ROC / Precision-Recall Curve | Classifier performance evaluation | Machine Learning |
| Histogram, Bar, Line, Pie, Area Chart | Quantitative value comparisons | General Data Visualization |
| Scatter / Box / Violin Plot | Distributions and relationships in data | Statistics, Data Science |
| Heatmap | Color-coded matrix values (e.g., gene expression) | Bioinformatics, Data Viz |
| Correlation Matrix | Displays pairwise variable correlations | Statistics |
| PCA / t-SNE / UMAP Plot | Dimensionality reduction for high-dimensional data | Data Science |
| Flowchart | Workflow or process logic diagram | Business, Software |
| Mind Map / Concept Map | Hierarchical or network-style idea mapping | Education, Planning |
| Tree Diagram | Hierarchical branching structure | Decision Science, Logic |
| Causal Loop Diagram | Cause-effect feedback structure | Systems Thinking |
| Network Diagram / Node-Link Graph | Entities and their relationships | Computer Networks, Sociology |
| Formal Grammar Tree | Syntax tree of a language or parser | Linguistics, Comp. Science |
| Symbolic Logic Diagram | Visualizes logical relationships and structures | Philosophy, Math |
| Mathematical Notation (Structured) | Spatial layout of formulas, expressions | Mathematics |
| Perspective Drawing | Spatial illusion of depth on 2D plane | Art, Design |
| Optical Illusion | Demonstrates visual perception limits | Cognitive Psychology |
| Gestalt Patterns | Visual grouping effects | Psychology, Design |
| Abstract Art / Pattern | Visual abstraction for emotion or cognition | Art, Psychology |
| Educational Animation / Infographic | Visual learning aids | Education |
| Mental Model Visualization / Heuristic | Cognitive simplification of processes | Psychology, Education |
| Timeline | Chronological sequence of events | History, Project Management |
| Gantt Chart | Task-time scheduling chart | Project Management |
| Dashboard | Aggregated metrics and visual summaries | Business Intelligence |
| HMI Screen / Instrument Panel | Control interface for machines | Industrial Automation |
| UI Mockup / Wireframe / Widget | Prototype interfaces and elements | UX/UI Design |
| Interactive Plot (e.g., Jupyter, D3.js) | User-manipulable graphs | Data Science, Education |
| Topographic / Elevation Map | Shows terrain height contours | Geography |
| Thematic Map / Choropleth / Cartogram | Encodes non-geographic data spatially | GIS, Demography |
| GIS Layer / Overlay | Spatial data layers with attributes | Geoinformatics |
| Cross-Sectional View | Interior view through an object or region | Geology, Anatomy |
| Seismic Reflection Profile | Subsurface imaging with wave echoes | Geophysics |
| Borehole Log / Stratigraphic Column | Rock types and properties along boreholes | Geology |
| NDVI / Hyperspectral / Thermal Map | Remote sensing for vegetation, temp, etc. | Environmental Science |
| LIDAR Point Cloud | 3D surface points from laser scans | Remote Sensing |
| Fault Line / Tectonic Map | Visualizes plate boundaries and seismic risk | Geology |
| Geomagnetic / Gravimetric / Geochemical Map | Maps physical or chemical earth properties | Geosciences |
| Hydrological Basin Diagram | Shows water flow across terrain | Hydrology |
| Oceanographic Flow Map | Depicts ocean current behavior | Oceanography |
| Weather Radar / Climate Model Visualization | Meteorological data and forecasts | Meteorology |
| Redshift / Hubble Diagram | Cosmological expansion visualizations | Astrophysics |
| Sky Map / Star Chart | Positions of stars and constellations | Astronomy |
| Composite Wavelength / Radio Telescope Imagery | Multi-spectrum or radio data from space | Astronomy |
| Simulation-based Cosmological Rendering | Large-scale universe models | Astrophysics |
| Motion Capture Visualization | Tracks human or object motion in 3D | Animation, Biomechanics |
| Particle Track Visualization | Displays subatomic trajectories (e.g., LHC) | Particle Physics |
| Waveform / Spectrogram | Frequency-time sound or signal visualizations | Acoustics, Signal Processing |
| Quantum Orbital Shape | Probabilistic electron cloud models | Quantum Mechanics |
| Logo / Icon / Symbol / Emblem | Simplified visual identity or signal | Design |
| Photograph / Sketch / Painting / Illustration | Visual artistic representation | Art, Communication |
| Silhouette / Pictogram | Simplified outline or iconic representation | Semiotics, Design |
| Candlestick Chart | … | … |

## Toolbox

> …
> 

| **Library/Engine** | **Description** | **Primary Use** | **Platforms** | **Language** | **Website** |
| --- | --- | --- | --- | --- | --- |
| **SFML** | Simple and Fast Multimedia Library for handling graphics, audio, and input. | 2D Graphics, Input, Audio | Windows, macOS, Linux, Android | C++ | [SFML Official Site](https://www.sfml-dev.org/) |
| **SDL** | Cross-platform library for handling graphics, audio, and input. | 2D Graphics, Input, Audio | Windows, macOS, Linux, Android | C | [SDL Official Site](https://www.libsdl.org/) |
| **Allegro** | Cross-platform library for 2D game development, including graphics and input. | 2D Graphics, Input, Audio | Windows, macOS, Linux, Android | C | [Allegro Official Site](https://liballeg.org/) |
| **OpenGL** | Powerful graphics API for 2D and 3D rendering. | 2D/3D Graphics | Windows, macOS, Linux, Android | C/C++ | [OpenGL Official Site](https://www.opengl.org/) |
| **DirectX** | Collection of APIs for multimedia tasks, including graphics and input (Windows). | 2D/3D Graphics, Audio | Windows | C/C++ | [DirectX Official Site](https://learn.microsoft.com/en-us/windows/win32/directx) |
| **Ogre3D** | 3D rendering engine with advanced capabilities. | 3D Graphics | Windows, macOS, Linux | C++ | [Ogre3D Official Site](https://www.ogre3d.org/) |
| **Godot Engine** | Open-source game engine with a rich set of tools for 2D and 3D development. | 2D/3D Game Development | Windows, macOS, Linux, Android | GDScript, C++ | [Godot Engine Official Site](https://godotengine.org/) |
| **Unity** | Widely-used game engine with a powerful editor and cross-platform support. | 2D/3D Game Development | Windows, macOS, Linux, Android | C# (C++ plugins) | [Unity Official Site](https://unity.com/) |
| **Unreal Engine** | High-end game engine with advanced graphics capabilities and tools. | 2D/3D Game Development | Windows, macOS, Linux, Android | C++ | [Unreal Engine Official Site](https://www.unrealengine.com/) |
| **Cocos2d-x** | Open-source framework for 2D game development. | 2D Game Development | Windows, macOS, Linux, Android | C++ | [Cocos2d-x Official Site](https://www.cocos.com/en/) |

## **Scientific Foundations**

- Light, optics, and the electromagnetic spectrum
- Color science, photometry, and radiometry
- Human visual perception and cognition

## **Technical Fields**

| Category / Field | Description / Focus Area |
| --- | --- |
| Computational Photography | Techniques to enhance, manipulate, or capture images using algorithms and computation. |
| Image Processing and Computer Vision | Methods to analyze, interpret, and manipulate images and extract meaningful information. |
| Geometry and Rendering | Modeling shapes, surfaces, and generating realistic images through rendering techniques. |
| CAD (Computer-Aided Design) & Parametric Modeling | Designing objects and structures using digital tools, often with parameterized control. |
| Immersive Interfaces (AR/VR) | Interfaces and experiences that blend real and virtual environments interactively. |
| Data Visualization Techniques | Methods to visually represent data for easier understanding and insight generation. |

## Linux Computer Graphics Stack

> How Linux Driver’s Models Work?
> 

> See [Linux Graphics Stack](https://www.notion.so/Linux-Graphics-Stack-9d424b55242c442abdb9183fbd080355?pvs=21).
> 

## Computer Graphic

> Computer Graphic: … ….
> 

> **Partial screen updates** refer to the process of refreshing only specific areas of a display that have changed, rather than redrawing the entire screen, to improve rendering efficiency and performance.
> 

> **Z-Buffering: A method of depth coordination in 3D graphics, which is used to determine which objects, or parts of objects, are visible and which are hidden behind other objects.**
> 

### Core Parts

| **Component** | **Description** |
| --- | --- |
| **Modeling** | Creating 2D/3D geometric representations of objects |
| **Animation** | Defining how models change over time |
| **Rendering** | Generating final images from scene data |
| ├── **Lighting** | Computing light interaction with surfaces |
| └── **Shading** | Determining final surface color and appearance |
| **Interaction** | User input and control over the scene |

### Workload Taxonomy

> …
> 

| **Category** | **Subcategory** | **Description** |
| --- | --- | --- |
| **Rendering Technique** | Rasterization | Converts 3D models into 2D images using projection, shading, and texturing, optimized for real-time rendering. |
|  | Ray Tracing | Simulates light paths for accurate reflections, shadows, and global illumination, used in offline and real-time RTX graphics. |
|  | Path Tracing | A Monte Carlo-based rendering method achieving photorealistic lighting by tracing many light paths per pixel. |
|  | Ray Marching | Used for procedural effects and volume rendering, such as smoke, fog, and clouds. |
|  | Deferred Rendering | Separates rendering into multiple passes to optimize lighting and shading computations in modern game engines. |
|  | Tile-Based Rendering | Renders images in small tiles to reduce memory bandwidth usage, commonly used in mobile GPUs. |
| **Application Domain** | Real-Time Graphics | Focuses on fast rendering for interactive applications like video games, VR, and UI. |
|  | Offline Rendering | Prioritizes photorealism over speed, used in CGI movies, VFX, and architectural visualization. |
|  | Scientific Visualization | Processes and visualizes large datasets, such as medical imaging and fluid simulations. |
|  | Computational Photography | Uses AI and algorithms to enhance images, including HDR imaging and neural rendering. |
|  | Geospatial Rendering | Handles large-scale map and terrain visualization for GIS and weather simulations. |
|  | AI-Generated Graphics | Uses machine learning models like GANs and diffusion models for image synthesis and enhancement. |
| **Computational Characteristics** | Compute-Intensive | Requires high processing power for tasks like global illumination and physics-based rendering. |
|  | Memory-Intensive | Consumes large amounts of RAM for high-resolution textures, models, and voxel-based rendering. |
|  | Bandwidth-Intensive | Involves heavy data transfer between CPU, GPU, and memory, such as 4K real-time rendering. |
|  | Latency-Sensitive | Demands real-time responsiveness for gaming, AR/VR, and interactive UI. |
|  | Parallelism-Oriented | Optimized for SIMD/SIMT architectures, such as GPU-based rendering and AI acceleration. |
| **Hardware Target** | CPU Rendering | Uses CPU cores for rendering, often in offline applications like Blender Cycles. |
|  | GPU Rendering | Leverages GPU parallelism for rendering with APIs like DirectX, Vulkan, and OpenGL. |
|  | Hybrid CPU-GPU Rendering | Uses CPU for scene setup and GPU for rendering, common in game engines like Unreal. |
|  | Cloud Rendering | Distributes rendering workloads across cloud-based servers for large-scale tasks. |
|  | Mobile Rendering | Optimized for low-power devices using tile-based rendering and power-efficient techniques. |

## 3d Computer Graphics

> …
> 

## Data Visualization

> [Data Visualization](https://www.notion.so/Data-Visualization-29cc0f5171ec80fdbe89cd26c26feaac?pvs=21)
> 

## User Interface

> [UI](https://www.notion.so/UI-29cc0f5171ec80f2b185dab957ae7e85?pvs=21)
> 

## **Real-time Computer Graphic**

> …
> 

## **📚** References

- https://github.com/tradingview/lightweight-charts
- https://apexcharts.com/
- https://www.highcharts.com/
- https://dash.plotly.com/
- …
- https://en.wikipedia.org/wiki/3D_computer_graphics
- [Shader](https://en.wikipedia.org/wiki/Shader)
- [Rendering](https://en.wikipedia.org/wiki/Rendering_(computer_graphics))
- [Raster Graphics](https://en.wikipedia.org/wiki/Raster_graphics)
- [Computer graphics](https://en.wikipedia.org/wiki/Computer_graphics)
- [Scientific Visualization](https://en.wikipedia.org/wiki/Scientific_visualization)
- [Direct Rendering Manager](https://en.wikipedia.org/wiki/Direct_Rendering_Manager)
- [Computational Photography](https://en.wikipedia.org/wiki/Computational_photography)
- https://en.wikipedia.org/wiki/Polygon_mesh
- [Computational Geometry](https://www.notion.so/Computational-Geometry-25639283ef314965aeca56e1b05b57c9?pvs=21)
- https://en.wikipedia.org/wiki/Texture_mapping
- [Why are shaders called shader?](https://stackoverflow.com/questions/42614674/why-are-shaders-called-shader)
- https://wiki.libsdl.org/SDL3/SDL_Texture
- https://en.wikipedia.org/wiki/Real-time_computer_graphics
- https://www.youtube.com/watch?v=nIaVx-4UGUU
- https://github.com/dbremont/linux-api-labs
- https://github.com/tsoding/olive.c/tree/master
- ‣
- ‣
- ‣
- ‣
- https://www.youtube.com/playlist?list=PLplnkTzzqsZS3R5DjmCQsqupu43oS9CFN
- [**Representation Problem: Geometric Data**](https://www.notion.so/Representation-Problem-Geometric-Data-105eb11a70fb4d33b0643adbb4f66fcb?pvs=21)
- https://github.com/csiglab/visualization-lab
- [**Optical Phenomena**](https://www.notion.so/Optical-Phenomena-1aec0f5171ec802fb93dcbff1f95a8a1?pvs=21)
- [Human Vision System](https://www.notion.so/Human-Vision-System-1afc0f5171ec80f7973ef820ed1b428f?pvs=21)
- [**Acoustics P**henomena](https://www.notion.so/Acoustics-Phenomena-1aec0f5171ec806fb1f2e35f9adfd2fb?pvs=21)
- [Computational Geometry](https://www.notion.so/Computational-Geometry-25639283ef314965aeca56e1b05b57c9?pvs=21)
- [**Simple DirectMedia Layer** (**SDL**)](https://www.notion.so/Simple-DirectMedia-Layer-SDL-114c0f5171ec804abe56e12433410672?pvs=21)
- [Infographic](https://en.wikipedia.org/wiki/Infographic)
- [Data Is Uggly](https://www.reddit.com/r/dataisugly/)
- [Observable HQ](https://observablehq.com/)
- [Data Is Beautiful](https://www.reddit.com/r/dataisbeautiful/)
- [Vega & Vega-Lite](https://vega.github.io/)
- [Data visualization](https://www.reddit.com/r/datavisualization/)
- [awesome-DataViz](https://github.com/hal9ai/awesome-dataviz?tab=readme-ov-file)
- [Visualization Curriculum](https://uwdata.github.io/visualization-curriculum/intro.html)
- [List of graphical methods](https://en.wikipedia.org/wiki/List_of_graphical_methods)
- [UW Interactive Data Lab](http://idl.cs.washington.edu/)
- [The Python Graph Gallery](https://python-graph-gallery.com/)
- [Practical Business Python](https://pbpython.com/)
- [Data and information visualization](https://en.wikipedia.org/wiki/Data_and_information_visualization)
- [The 30 Best Data Visualizations of 2023](https://visme.co/blog/best-data-visualizations/)
- [Viz Hub - Gallery / Code Great Visualizations](https://vizhub.com/)
- "The Visual Display of Quantitative Information" by Edward R. Tufte
- Wilkinson, Leland. The grammar of graphics. Springer Berlin Heidelberg, 2012.
- [Data Is Beautiful: 10 Of The Best Data Visualization Examples From History & Today](https://www.tableau.com/learn/articles/best-beautiful-data-visualization-examples)
- Franconeri, Steven L., et al. "The science of visual data communication: What works." Psychological Science in the public interest 22.3 (2021): 110-161.
- Fundamentals of Data Visualization
[https://clauswilke.com/dataviz/](https://clauswilke.com/dataviz/)
- Erik Gahner Larsen  Data visualization: a reading list
[https://erikgahner.dk/2020/data-visualization-a-reading-list/](https://erikgahner.dk/2020/data-visualization-a-reading-list/)
- [https://texample.net/tikz/examples/](https://texample.net/tikz/examples/)
- Data Visualization Reading List
[https://nickreich.github.io/data-stories/pages/data-viz-reading-list.html](https://nickreich.github.io/data-stories/pages/data-viz-reading-list.html)
- Data Visualization Reading List
[https://people.engr.tamu.edu/shipman/courses/datavis/readings.html](https://people.engr.tamu.edu/shipman/courses/datavis/readings.html)
- Share your best visualizations =)
[https://www.kaggle.com/discussions/questions-and-answers/197842](https://www.kaggle.com/discussions/questions-and-answers/197842)
- Knowledge is Beautiful
[https://www.amazon.com/Knowledge-Beautiful-David-Mccandless/dp/0007427921](https://www.amazon.com/Knowledge-Beautiful-David-Mccandless/dp/0007427921)
- Introduction to Plotting with Matplotlib in Python
[https://www.datacamp.com/tutorial/matplotlib-tutorial-python](https://www.datacamp.com/tutorial/matplotlib-tutorial-python)
- Python Plotting With Matplotlib (Guide)
[https://realpython.com/python-matplotlib-guide/](https://realpython.com/python-matplotlib-guide/)
- https://github.com/AutoViML/AutoViz
- https://echarts.apache.org/examples/en/index.html#chart-type-scatter
- https://www.data-to-viz.com/
- [The Data Visualisation Catalogue](https://datavizcatalogue.com/)
- [List of graphical methods](https://en.wikipedia.org/wiki/List_of_graphical_methods)
- [OpenCV](https://www.notion.so/OpenCV-a4e07ebbe522462aa2adb94415de0d47?pvs=21)
- https://lookerstudio.google.com/u/0/navigation/reporting [Create and Share Dashboard]
- https://en.wikipedia.org/wiki/Imaging How to visualize things? How to convert many signals into visual signals?
- https://physics.stackexchange.com/questions/134870/light-matter-interaction-and-an-objects-appearance
- [Signal](https://www.notion.so/Signal-23dd50e3c6c04ebcb66e240d59608545?pvs=21)
- [Signal processing](https://en.wikipedia.org/wiki/Signal_processing)
- [Compressed Sensing](https://en.wikipedia.org/wiki/Compressed_sensing)
- https://en.wikipedia.org/wiki/Filter_(signal_processing)
- ‣
- ‣
- [A Non-Mathematical Introduction To Kalman Filters For Programmers](https://praveshkoirala.com/2023/06/13/a-non-mathematical-introduction-to-kalman-filters-for-programmers/)  https://news.ycombinator.com/item?id=36971975
- Kalman Filtering in R: https://www.stat.berkeley.edu/~brill/Stat248/kalmanfiltering.pdf
- https://en.wikipedia.org/wiki/Medical_imaging
- https://en.wikipedia.org/wiki/Signal_processing
- [Wavelet](https://www.notion.so/Wavelet-7b19eaee77db4a42bf9c1c9027f158c2?pvs=21)
- [Signal Processing](https://www.notion.so/Signal-Processing-1bbc0f5171ec8081ae7ecf54cb306d76?pvs=21)
- https://en.wikipedia.org/wiki/3D_computer_graphics
- https://en.wikipedia.org/wiki/Multimedia_framework
- [Multimedia](https://en.wikipedia.org/wiki/Multimedia)
- [GPU](https://www.notion.so/GPU-8cb6117716f54165b9759de0646bb5dd?pvs=21)
- [Real-time computer graphics](https://en.wikipedia.org/wiki/Real-time_computer_graphics)
- [Real-Time Rendering, Fourth Edition](https://www.amazon.com/Real-Time-Rendering-Fourth-Tomas-Akenine-M%C3%B6ller/dp/1138627003)
- https://www.reddit.com/r/GraphicsProgramming/comments/18lgev5/is_there_such_thing_as_a_real_time_graphics_engine/