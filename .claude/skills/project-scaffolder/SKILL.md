---
name: project-scaffolder
description: "Genera scaffolding de proyectos con estructura, configuración y tooling listos para producción."
---

# project-scaffolder

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/project-scaffolder/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/project-scaffolder/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/project-scaffolder/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "crear proyecto", "inicializar", "setup", "nuevo proyecto", "scaffolding", "boilerplate", "estructura base"
