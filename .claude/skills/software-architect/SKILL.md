---
name: software-architect
description: "Diseña arquitectura de software. Genera diagramas C4, contratos de API y ADRs."
---

# software-architect

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/software-architect/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/software-architect/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/software-architect/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "diseñar sistema", "arquitectura", "diagrama", "ADR", "diseña la arquitectura", "define la estructura", "patron de diseño"
