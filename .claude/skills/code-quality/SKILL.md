---
name: code-quality
description: "Revisa código en busca de problemas de lógica y claridad. Propone mejoras con justificación. No edita archivos."
---

# code-quality

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/code-quality/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/code-quality/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/code-quality/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "revisa este código", "qué mejorarías", "code review", "revisa la calidad", "qué está mal aquí", "analiza este archivo", "revisa el código", "sugerencias de mejora"
