---
name: diagrams
description: "Genera diagramas Mermaid (C4, secuencia, flujo) y DBML para base de datos. Los inserta en Documentation.md."
---

# diagrams

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/diagrams/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/diagrams/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/diagrams/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "diagrama", "diagrama C4", "diagrama de la base de datos", "DBML", "arquitectura del sistema", "diseño del sistema", "diagrama ER", "mermaid", "diagrama de secuencia", "flujo del sistema"
