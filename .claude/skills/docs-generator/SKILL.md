---
name: docs-generator
description: "Genera documentación técnica: API docs, runbooks, guías de usuario y diagramas de onboarding."
---

# docs-generator

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/docs-generator/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/docs-generator/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/docs-generator/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "generar documentación", "documentar", "API docs", "runbook", "guía de usuario", "README", "docstrings"
