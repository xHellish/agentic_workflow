---
name: structure-analyzer
description: "Analiza estructura de proyectos existentes. Mapea dependencias y evalúa salud del código."
---

# structure-analyzer

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/structure-analyzer/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/structure-analyzer/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/structure-analyzer/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "analizar estructura", "mapa de dependencias", "analiza este proyecto", "estructura del proyecto", "organización del código", "auditoria de carpetas"
