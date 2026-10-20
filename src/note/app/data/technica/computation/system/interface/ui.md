# UI

> In this note, we will holistically cover **Product Development**, including Market Research, UX, and UI.
> 

> **Human-Computer Interaction (HCI)** is the interdisciplinary field that studies the design, evaluation, and improvement of interactive technology to create seamless and effective interactions between humans and computers.
> 

> A **System Interface**, commonly referred to as a **User Interface (UI)**, is the space where interactions between humans and machines occur, facilitating the control and operation of machine features by human users through graphical elements, menus, and controls.
> 

> **UX**: A multidimensional system property representing the dynamic, contextual, and affective interaction between a user and a system, emergent from the coalescence of cognitive load, usability metrics, interaction feedback loops, perceptual-motor efficiency, and system affordances within a defined task environment.
> 

> A **Design System** is a comprehensive collection of reusable components, guidelines, and standards that help teams build consistent, scalable, and efficient digital products. It serves as a single source of truth for design and development, ensuring cohesion across products and platforms.
> 

> A **design token** is a **named, platform-agnostic value** that represents a design decision such as a color, spacing, typography, or other visual style property. Design tokens are used to **ensure consistency** and **enable scalability** across different platforms and products by centralizing design choices in a **machine-readable format** (usually JSON, YAML, or SCSS variables).
> 

> **Product Development**: Understand the needs and behaviors of market participants, identify their key problems, and develop a product that effectively addresses those problems.
> 

> You give me money for this product; and this product adds value to you.
> 

> **Note:** Product development and its associated activities should maintain a laser focus on creating meaningful value for the user.
> 

> **Note:** Many areas of software engineering—such as requirements gathering—can be viewed through the lens of product development, highlighting significant overlap between the two fields. The prevailing view is that this is a specialized task requiring both business knowledge and technical expertise.
> 

> **System Status:**
> 
> - **UI Status:** This reflects the current condition or feedback of the user interface elements—what the user sees and interacts with. It includes visual indicators like loading spinners, error messages, active buttons, progress bars, or any dynamic content states that inform the user about the system’s condition or activity.
> - **System State:** This is the internal condition of the system’s components or backend logic at a given moment. It includes variables, process statuses, resource availability, connectivity, error states, and other operational details that determine how the system behaves or responds.

> In this Note we will explore the User Interface  -  the interaction layer.
> 

> A **User Interface (UI)** is the mediating system that enables reciprocal communication between a cognitive agent and a computational system by translating internal machine states into perceptible representations and user intentions into executable operations. It functions as a **semantic transducer**, aligning two distinct domains—human cognition and computational logic—through structured mappings of perception, action, and meaning. Conceptually, it integrates representational, operational, and contextual layers to maintain coherence between user goals and system behavior, regulating the flow of information and control across their boundary. In essence, the UI is not merely a surface of interaction but a **cognitive–computational coupling mechanism** that structures and stabilizes human–machine dialogue within a given environment.
> 

## Index

QA:

- How does **Amazon keep product pages** consistent across millions of items while allowing for differences like images, specs, and features? Do they use **dynamic templates based** on **categories**?
- How to **evaluate a design**?
- How to make working easier?
    - Autocomplete Data
    - Mini UI’s (Add a user;  in  a form; or other types of data)
    - …
- **How to be a good designer?**
    - Study other designs
    - Problems: Design Space
    - Future Evolution

## Breviarium

> {{ Product & Business Strategy → Market Research  → Product Design → Product Evaluation (Q/A) → Product Delivery → Product Online Evaluation}}
> 

> **Note:** All of these areas are deeply interconnected. Avoid making rigid or invisible divisions between them—the separation is artificial and meant only to organize work and assign responsibilities.
> 
> 
> It is especially important that Product Development (UX/UI) is fully integrated with Market Research and Business Strategy. Designers and developers must deeply understand the business context in order to build truly great products. 
> 
> Follow a **“Shared Cognition, Divided Execution”** model: align on understanding and intent, then divide tasks to act efficiently.
> 

Structure:

- Product & Business Strategy
- Market Research
- Product Design
    - UX/UI
    - UI Components
    - Design Systems
    - Design Tokens
    - Visual Design
- Product Evaluation (Q/A)
    - Product Analytics and Improvement.
    - …
- Product Delivery
- Product Online Evaluation
- Principles
- Check List

QA:

- How can we **formally reason** about the dynamics of user switching between products? What incentive mechanisms should be embedded in a new product to support and accelerate user transition?
- How does **product development** feet in an organization structure?

## Formulation

> A **User Interface (UI)** is the **mediating layer** between a **cognitive agent (user)** and a **computational system (machine)**, structured to enable **bidirectional semantic exchange** through **syntactic, perceptual, and operational affordances**.
> 

Formally: $UI = \langle S, U, M, \Phi, \Gamma, \Pi \rangle$

where:

- $S$: System (internal computational model, data, logic)
- $U$: User (cognitive agent with intentions and goals)
- $M$: Medium (material or digital substrate: screen, haptic, audio, etc.)
- $\Phi$: Representation function — maps internal system states → perceptible forms (output).
- $\Gamma$: Action interpretation function — maps user actions → system operations (input).
- $\Pi$: Protocol of interaction — defines temporal, logical, and semantic rules governing ($\Phi$) and ($\Gamma$).

## Functional Representation

The UI can be modeled as a **bidirectional transducer** between two semantic domains: $U \xleftrightarrow[\Gamma]{\Phi} S$

- $\Phi: S \to P_U$: maps system states ($S$) to perceptual symbols $P_U$ understood by the user.
- $\Gamma: A_U \to O_S$: maps user actions $A_U$ to system operations $O_S$.

**Condition for effective UI:** $\forall g \in G_U, \exists (a \in A_U) \text{ such that } \Gamma(a) \implies S' \text{ satisfying } g$
where $G_U$ is the set of user goals.

## Linux Computer Graphics Stack

> How Linux Driver’s Models Work?
> 

> See [Linux Graphics Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-graphics-stack.md).
> 

## Conceptual Model

Conceptual Model:  Computing System Interface

## References

- https://growth.design/case-studies/tiktok-feed-psychology Best Design Site That I Know.
- Dark Patterns
    - [Dark Pattern](https://en.wikipedia.org/wiki/Dark_pattern)
    - [Deceptive Design](https://www.deceptive.design/)
- [Mcmaster](https://www.mcmaster.com/)
- https://pictogrammers.com/library/mdi/
- https://github.com/tabler/tabler-icons
- https://icones.js.org/
- https://ionic.io/ionicons/
- https://iconduck.com/
- https://icons.radix-ui.com/
- https://heroicons.com/
- [Design Systems](https://www.designsystems.com/)
- [13 outstanding design system examples from leading brands](https://www.wix.com/studio/blog/design-system-examples)
- [Designing Good Interfaces](https://news.ycombinator.com/item?id=35164997)
- [Human–Computer Interaction](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction)
- [Growth Design -](https://growth.design/course)
- [The UX Research Reckoning is Here](https://news.ycombinator.com/item?id=36113444)
- [Machine learning of GUIs at scale](https://austinhenley.com/blog/machinelearningguis.html)
- Reading List
    - [Growth Design - Dan & Louis-Xavier](https://growth.design/about)
    - [HCI Gatech Reading List](https://omscs6750.gatech.edu/spring-2022/required-reading-list/)
    - [**Ph.D. HCC — HCI Reading List**](https://ic.gatech.edu/phd-hcc-hci-reading-list)
- [Nielsen Group](https://www.nngroup.com/)
- Papers
    - Hokkanen, Laura, Kati Kuusinen, and Kaisa Väänänen. "Early product design in startups: towards a UX strategy." Product-Focused Software Process Improvement: 16th International Conference, PROFES 2015, Bolzano, Italy, December 2-4, 2015, Proceedings 16. Springer International Publishing, 2015.
    - Treder, Marcin. "UX Design for startups." UXPin, Mountain View, CA (2013).
    - Saad, Jullia, et al. "UX work in software startups: A thematic analysis of the literature." Information and Software Technology 140 (2021): 106688.
- Awesome System Design Resources
[https://github.com/ashishps1/awesome-system-design-resources?tab=readme-ov-file#system-design-interview-problems](https://github.com/ashishps1/awesome-system-design-resources?tab=readme-ov-file#system-design-interview-problems)
- https://news.ycombinator.com/item?id=31217448
- [AB Testing](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/ab-testing.md)
- [Recommender System](https://app.notion.com/p/Recommender-System-2fd52a7887cf4b5385859d9705eba39f?pvs=21)
- [**Computational Typography**](note.html?n=technica/computation/miscelanea/computational-typography.md)
- https://github.com/rothgar/awesome-tuis?tab=readme-ov-file#libraries
- https://uxcel.com/
- https://www.casestudy.club/
- https://uxplanet.org/
- https://www.nngroup.com/
- [System](note.html?n=technica/computation/system.md)
- [**A Guide to Improving Computational Systems in a Principled Way**](https://app.notion.com/p/A-Guide-to-Improving-Computational-Systems-in-a-Principled-Way-1bec0f5171ec808fb56ffd094de27a12?pvs=21)
- https://www.youtube.com/watch?v=AmPW7S97LM8
- https://www.youtube.com/watch?v=L6RKi9ZvkT4&t=851s
- https://www.youtube.com/watch?v=R7urbI0iqb0&t=6841s
- https://medium.com/onebigthought/the-ux-research-reckoning-is-here-c63710ea4084
- https://www.youtube.com/watch?v=B6Dt1sgGmLI
- https://en.wikipedia.org/wiki/New_product_development
- https://www.nngroup.com/articles/ten-usability-heuristics/
- https://www.youtube.com/watch?v=uHh0qpc1BR4
- https://en.wikipedia.org/wiki/Graphical_widget
- https://en.wikipedia.org/wiki/User_interface
- ….