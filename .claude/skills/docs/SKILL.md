---
name: docs
description: "Genera y actualiza README.md conciso y Documentation.md técnico incremental. Siempre en español."
---

# docs

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/docs/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/docs/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/docs/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "documentar", "genera el README", "actualiza docs", "crea documentación", "escribe la documentación", "documentation", "README", "actualiza el Documentation", "registra la decisión", "Decision Log"
