# CLAUDE.md — Agentic Workspace

> Configuración de Claude Code para este workspace.
> Para regenerar: `python .agents/scripts/generate_agent_rules.py --agent claude`

## Sistema de Skills

Este workspace usa una arquitectura basada en **skills**. Antes de responder a cualquier tarea:

1. Lee `.agents/manifest.json` para identificar la skill aplicable según los `triggers`.
2. Lee el `SKILL.md` de la skill completo y adopta su rol y lineamientos.
3. Sigue la sección `## Reference Loading` de la skill para cargar archivos de referencia relevantes.
4. Para tareas complejas, encadena skills en el orden definido en los pipelines de `.agents/config.yaml`.

## Archivos Clave

- `.agents/manifest.json` — Catálogo de skills (fuente única de verdad para triggers y metadatos)
- `.agents/config.yaml` — Configuración del workspace (idioma, pipelines, ajustes por skill)
- `.agents/skills/<name>/SKILL.md` — Instrucciones de cada skill
- `.agents/skills/<name>/references/` — Documentos de referencia en profundidad
- `.agents/skills/<name>/examples/` — Outputs de ejemplo como referencia de formato

## Skills Disponibles

| Skill | Triggers Principales | Descripción |
|-------|---------------------|------------|
| `software-architect` | "diseñar sistema", "arquitectura", "diagrama" (+4 more) | Diseña arquitectura de software. Genera diagramas C4, contra... |
| `structure-analyzer` | "analizar estructura", "mapa de dependencias", "analiza este proyecto" (+3 more) | Analiza estructura de proyectos existentes. Mapea dependenci... |
| `code-improver` | "mejorar código", "refactorizar", "code review" (+4 more) | Detecta code smells y propone refactoring. Aplica principios... |
| `project-scaffolder` | "crear proyecto", "inicializar", "setup" (+4 more) | Genera scaffolding de proyectos con estructura, configuració... |
| `test-strategist` | "escribir tests", "estrategia de testing", "cobertura" (+4 more) | Define estrategia de testing, detecta anti-patrones y guía l... |
| `security-auditor` | "auditar seguridad", "vulnerabilidades", "OWASP" (+4 more) | Audita seguridad del código. Revisa OWASP Top 10, manejo de ... |
| `docs-generator` | "generar documentación", "documentar", "API docs" (+4 more) | Genera documentación técnica: API docs, runbooks, guías de u... |
| `devops-engineer` | "crear pipeline", "configurar ci/cd", "dockerizar aplicación" (+5 more) | Diseña pipelines CI/CD, infraestructura como código (IaC), c... |
| `git-workflow` | "git workflow", "estrategia de git", "branching strategy" (+5 more) | Define estrategias de branching, conventional commits, PR te... |
| `api-designer` | "api designer", "openapi", "swagger" (+5 more) | Diseña contratos de API (OpenAPI, GraphQL schemas), estrateg... |
| `performance-engineer` | "performance engineer", "slow", "bottleneck" (+4 more) | Profiling, load testing, benchmarking, caching, APM.... |
| `database-designer` | "database designer", "diseñar base de datos", "diagrama ER" (+3 more) | ER diagrams, migration strategies, query optimization.... |

## Pipelines Multi-Skill

- **new-project**: Full pipeline for bootstrapping a new project
  - Pasos: `software-architect` → `project-scaffolder` → `test-strategist` → `security-auditor` → `docs-generator`
- **code-review**: Comprehensive code quality and security review
  - Pasos: `structure-analyzer` → `code-improver` → `security-auditor`
- **audit-full**: Full project health audit
  - Pasos: `structure-analyzer` → `security-auditor` → `test-strategist` → `code-improver` → `docs-generator`
- **quick-review**: Fast review of a single file or small module
  - Pasos: `code-improver` → `security-auditor`

## Convenciones del Proyecto

> Fuente de verdad: `.agents/config.yaml` → `conventions`. Aplicar SIEMPRE, no solo cuando se activa una skill.

**Commits** (todo commit que escribas):
- Título descriptivo en `es` que resuma el avance, SIN prefijo de tipo (nunca `feat:`/`fix:`/`docs:`).
- Incluye SIEMPRE el cuerpo: detalles en lista de guiones `-`, cada punto conciso, en español.
- Sin emojis.
- Sin punto final en el título.
- Título <= 72 caracteres.
- **NO** añadir `Co-Authored-By: Claude` salvo petición explícita del usuario.

**Documentos formales (.docx / Word):**
- Al generar un documento Word, sigue **`.agents/shared/document-style.md`** (Times New Roman 12/14, todo en negro, tablas "Tabla Normal 1", filas 0.7cm, autoajustar a la ventana).

## Idioma

Responde siempre en el idioma definido en `.agents/config.yaml` → `response_language` (por defecto: español).

## Validación

Tras editar skills, ejecuta `python .agents/scripts/validate_skills.py`
Tras editar manifest.json o config.yaml, ejecuta `python .agents/scripts/generate_agent_rules.py --agent claude`
