# Changelog — Agentic Workspace

Todos los cambios notables del workspace se documentan aquí.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [1.2.0] — 2026-05-29

### Añadido
- Sección `## Reference Loading` en **todas las skills** (7/7) para instrucción explícita de carga de referencias
- Nuevo archivo `references/auth-patterns.md` en `security-auditor` con JWT (Python + TS), RBAC, OAuth2 PKCE y session security
- Nuevo archivo `references/concurrency-patterns.md` en `software-architect` con patrones para Go, Java, Python async y TypeScript
- Archivo `.agents/config.yaml` con configuración centralizada del workspace (idioma, lenguajes, pipelines, overrides por skill)
- Archivo `requirements.txt` con dependencias Python del workspace (pytest, pyyaml, pip-audit)
- Archivo `.pre-commit-config.yaml` con hooks de markdownlint, validate-skills y pre-commit-hooks
- Script `generate_agent_rules.py` que genera reglas para múltiples agentes (Cline, Claude, Gemini, Copilot) desde `manifest.json`
- Archivos `AGENTS.md` y `CLAUDE.md` para portabilidad multi-agente
- Archivo `.github/copilot-instructions.md` para GitHub Copilot
- Sección `pipelines` en `manifest.json` con 4 workflows orquestados (new-project, code-review, audit-full, quick-review)
- Directorio `examples/` en `_template-skill` con `.gitkeep`
- Sección `## Technology-Specific Checks` placeholder en `_template-skill`
- Docstring conventions para Go (godoc) y Java (Javadoc) en `docs-generator`
- Rúbrica objetiva para scorecards (🟢🟡🔴) en `structure-analyzer`
- Scope guidance blockquote en `code-improver` Workflow section
- Nota de pipelines disponibles en `.agents/config.yaml` referenciada en todas las reglas de agente

### Corregido
- **[BUG]** Lógica RBAC invertida en `security-auditor` — `current_user.role not in ROLE_HIERARCHY[minimum_role]` → `minimum_role not in ROLE_HIERARCHY[current_user.role]`
- **[BUG]** Header HTTP deprecado `X-XSS-Protection: 1; mode=block` comentado con nota en `security-auditor`
- **[BUG]** Template list mismatch en `project-scaffolder` — lista reducida a los 6 templates que realmente existen; nota agregada para stacks parciales (Go, Java, Rust)
- **[BUG]** `_template-skill` frontmatter `name: skill-name` → `name: _template` para evitar registro como skill activa
- **[BUG]** Typo "módigo" → "módulo" en `code-improver/examples/example-review.md`
- **[BUG]** `create_skill.py` actualizó el string de reemplazo para coincidir con el nuevo frontmatter del template

### Modificado
- Persona descriptions de todas las skills ampliadas para reflejar soporte real (Python, JS/TS, Go, Java)
- `software-architect` Section 7 (Concurrency) — código Go/Java movido a `references/concurrency-patterns.md`; sección condensada a principios + referencia
- `test-strategist` bloque Vitest monolítico dividido en 3 bloques separados (config, setup, component test)
- `_template-skill` expandido con meta-instrucciones, guía de directorio, Technology-Specific Checks placeholder y Language rule configurable
- `validate_skills.py` — `## Reference Loading` añadida a secciones requeridas
- `manifest.json` — versión bumped a 1.2.0, nuevas references para security-auditor y software-architect, sección `pipelines` añadida
- `.clinerules` regenerado con instrucción de `## Reference Loading` y `config.yaml`

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
