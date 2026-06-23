---
name: security-auditor
description: "Audita seguridad del código. Revisa OWASP Top 10, manejo de secretos y supply chain."
---

# security-auditor

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/security-auditor/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/security-auditor/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/security-auditor/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "auditar seguridad", "vulnerabilidades", "OWASP", "seguridad del código", "secretos", "autenticación", "SQL injection"
