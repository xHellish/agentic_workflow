---
name: code-improver
description: "Detecta code smells y propone refactoring. Aplica principios SOLID, DRY, KISS."
---

# code-improver

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/code-improver/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/code-improver/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/code-improver/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "mejorar código", "refactorizar", "code review", "revisa este código", "code smells", "optimizar", "SOLID"
