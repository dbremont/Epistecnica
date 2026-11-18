---
tags: [note, guia]
---

# A Guide to Improving Computational Systems in a Principled Way


> Improvement as an interacting problems.
> 

> Improvement feedback loop measure <→ interviene  <→ measure
> 

- How an optimal version of this system looks like?
- Model the system → measure the system → validate the model & measurments
- How to ‘find’  Interventions x for the system?
    - Inductive  → Propose several intevations →  Control Trial  ; It works; then apply the version that works.
    - Deductive (Understnang the system deeply) to deduce the  interveantion that willl make it better.
        - Standards Quality Checks
        - Study in a lab model what explains the changes in some  target system variables.
        - Study what works in other or similar systems.
        - Gather data from users; interviews; labs studies; etc.
- How to control for secnod-order effects; unintencdes consequences?
- How to control for temporal effects?
- How to fix a system? One really need a deep understand  of the system?  In order to find  the path of changes? Understadng the complex causal structure or interaction structure. How to create a recursive transtormation plan.
    - Root Cause Analysis https://en.wikipedia.org/wiki/Root_cause_analysis → Uncover the deep problem → symbols graph
    - Differentiate Symptoms from Causes
    - Prioritize Interventions
    - Feedback Loops
    - https://en.wikipedia.org/wiki/Five_whys
    - https://en.wikipedia.org/wiki/Issue-based_information_system
    - https://en.wikipedia.org/wiki/Issue_tree
    - https://en.wikipedia.org/wiki/Fault_tree_analysis
    - https://en.wikipedia.org/wiki/Hazard_analysis
    - https://en.wikipedia.org/wiki/Ishikawa_diagram
    - https://en.wikipedia.org/wiki/Seven_basic_tools_of_quality
    - https://en.wikipedia.org/wiki/Why%E2%80%93because_analysis
    - https://en.wikipedia.org/wiki/Five_Ws
    - **Pareto Analysis (80/20 Rule)**: Focuses on the 20% of causes that contribute to 80% of the problem to prioritize high-impact solutions.

## Abstract

> Propuesta  de **`mecanismos`** para la **organización** y **registro** de las **deudas técnicas** de los **`Sistemas de Software de Hacienda`**.
> 

> ¿**Problema**? Organizar,  dar seguimiento  Registro y  Seguimiento de las oportunidades de mejoras de los Sistemas de Hacienda.
> 

## Criterios

> Aquí tienes una tabla para los criterios del sistema de **"Informes Técnicos de Incidencias"**:
> 

| **Criterio** | **Descripción** |  |
| --- | --- | --- |
| **Colaboración** | Facilita la comunicación y colaboración entre equipos mediante comentarios y asignación de tareas. |  |
| **Escalabilidad** | Capaz de manejar un creciente número de informes y usuarios sin pérdida de rendimiento. |  |
| **Consultabilidad** | Facilidad de consultar los registros; eso indica **centralización**. |  |
| **Facilidad de Busqueda** | La interfaz debe ser intuitiva y fácil de usar para facilitar la entrada y consulta de datos. |  |
| **Historial de Incidencias** | Mantiene un registro detallado y cronológico de todas las incidencias reportadas. |  |
| **Notificaciones y Alertas** | Sistema de alertas para notificar a los responsables sobre nuevas incidencias o cambios de estado. |  |
| **Auditoría y Seguimiento** | Proporciona herramientas para auditorías y seguimiento de cambios en los informes. |  |
| **Generación de Reportes** | Capacidad para generar informes detallados y resúmenes estadísticos de las incidencias. |  |
| **Clasificación de Incidencias** | Permite la categorización de incidencias por tipo, gravedad, estado y otras etiquetas útiles. |  |
| **Integración con Otros Sistemas** | Compatibilidad con otros sistemas de gestión para importar/exportar datos. |  |

## Tecnología

> **Disponemos** de varias opciones de implementación:
> 

| **Sistema** | **Colaboración** | **Escalabilidad** | **Consultabilidad** | **Facilidad de Busqueda** |  |
| --- | --- | --- | --- | --- | --- |
| **Comentarios Tickets Jira** | Mala | Mala | Mala | Mala | … |
| Sistema Centralizado → **Projecto Jira** | Buena | Decente | Buena | Buena | … |
| Gitlab | Media | … | … | … | .. |

## Futuros Trabajos

En trabajos futuros, debemos abordar los siguientes aspectos:

- **Definir la Metadata de los Reportes:** Establecer los detalles y atributos específicos que se incluirán en la metadata de los reportes.
- **Determinar la  Ciclo de Vida de Un  Reportes:** Definir una estrategia eficaz para el seguimiento y la gestión de los reportes, asegurando prácticas adecuadas para su monitoreo y resolución.

## Referencias

- https://github.com/rstudio/rstudio/wiki/Writing-Good-Bug-Reports
- https://qawerk.com/blog/how-to-write-a-good-bug-report-best-practices/
- https://clickup.com/blog/how-to-write-a-bug-report/
- https://marker.io/blog/how-to-write-bug-report
- https://www.shakebugs.com/blog/bug-reporting-guide/

## References

- [Causality](https://app.notion.com/p/Causality-04df2d92fae547a1a119f4dea9d19554?pvs=21)
- [Modelado](https://app.notion.com/p/Modelado-a6727ea210124fb9a00ff6bb5bcf7cd5?pvs=21)
- [Complexity Science](https://app.notion.com/p/Complexity-Science-171c0f5171ec80c18335cdf06a024db6?pvs=21)
- [Dynamical Intelligence](https://app.notion.com/p/Dynamical-Intelligence-a41fde247c384e3bb5e561bf55c70f33?pvs=21)
- [Optimization](https://app.notion.com/p/Optimization-6c31e674fbe049b39869fc86154a8f15?pvs=21)
- [Performace](https://app.notion.com/p/Performace-b71afc822a2f4e2ea4e1191883035d17?pvs=21)
- [‣](https://app.notion.com/p/b0a2a8d65e9d46d3b9ccfe1614c1bd73?pvs=21)
- [System](https://app.notion.com/p/System-180c0f5171ec803391a6cb98cc236081?pvs=21)
- [Abductive Reasoning](https://app.notion.com/p/Abductive-Reasoning-1bec0f5171ec8058a4d1dfc566fd0eea?pvs=21)
- https://www.chiark.greenend.org.uk/~sgtatham/bugs.html
