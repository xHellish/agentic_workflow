# Changelog — Agentic Workspace

Todos los cambios notables del workspace se documentan aquí.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [1.1.0] — 2026-05-28

### Añadido
- Skill `test-strategist` con `references/testing-patterns.md` y `examples/`
- Skill `security-auditor` con `references/owasp-checklist.md` y `examples/`
- Skill `docs-generator` con `references/docs-templates.md` y `examples/`
- Plantilla `_template-skill` para estandarizar la creación de nuevas skills
- `README.md` en la raíz del workspace para onboarding rápido
- `manifest.json` como catálogo central de skills con versiones y triggers
- `CHANGELOG.md` (este archivo) para trazabilidad de cambios
- Script `validate_skills.py` para validar integridad del catálogo
- Sección `## Triggers` y `## Related Skills` en todos los `SKILL.md`
- Campo `version` en frontmatter YAML de todos los `SKILL.md`
- Soporte multi-lenguaje: Go y Java en `code-improver` y `structure-analyzer`
- Plantillas Go, Java y Rust en `project-scaffolder/references/project-templates.md`
- Patrones faltantes en `design-patterns.md`: Repository, Unit of Work, Middleware/Pipeline, CQRS, DI Container
- Plantilla ADR enriquecida con participantes, fecha de revisión, tags, métricas de éxito
- Carpetas `examples/` con outputs de referencia en todas las skills
- Configuración `markdownlint` en `.markdownlint.json`
- Fecha de última actualización y nota de revisión en `project-templates.md`

### Modificado
- `.clinerules` actualizado para referenciar `manifest.json` como fuente de triggers
- `Consideraciones.md` actualizado con las nuevas skills y convenciones
- `software-architect` — añadidos patrones de concurrencia Go/Java
- `structure-analyzer` — añadidos checks para Go y Java
- `code-improver` — añadidos checks para Go y Java

---

## [1.0.0] — 2026-05-27

### Añadido
- Skill `software-architect` con `design-patterns.md` y `adr-template.md`
- Skill `structure-analyzer` con `project-patterns.md`
- Skill `code-improver` con `code-smells.md`
- Skill `project-scaffolder` con `project-templates.md`
- `Consideraciones.md` con convenciones del workspace
- `.clinerules` con instrucción de activación de skills
