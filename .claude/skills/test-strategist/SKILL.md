---
name: test-strategist
description: "Define estrategia de testing, detecta anti-patrones y guía la cobertura de pruebas."
---

# test-strategist

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/test-strategist/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/test-strategist/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/test-strategist/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "escribir tests", "estrategia de testing", "cobertura", "pruebas unitarias", "TDD", "test doubles", "flaky tests"
