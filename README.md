# 🤖 Agentic Workspace

Entorno agéntico de desarrollo de software con skills especializadas para diseño, análisis, mejora y scaffolding de proyectos.

## ⚡ Inicio Rápido

Simplemente describe tu tarea en lenguaje natural. El agente detectará automáticamente la skill apropiada:

| Lo que dices | Skill activada |
|---|---|
| "Diseña la arquitectura de..." | `software-architect` |
| "Analiza la estructura de este proyecto" | `structure-analyzer` |
| "Revisa este código y mejóralo" | `code-improver` |
| "Crea un nuevo proyecto con FastAPI" | `project-scaffolder` |
| "Escribe tests para..." | `test-strategist` |
| "Audita la seguridad de..." | `security-auditor` |
| "Genera documentación para..." | `docs-generator` |
| "Crea un pipeline de CI/CD" | `devops-engineer` |
| "Define la estrategia de ramas de git" | `git-workflow` |
| "Diseña el contrato OpenAPI de..." | `api-designer` |
| "Encuentra el cuello de botella de..." | `performance-engineer` |
| "Diseña el esquema de base de datos para..." | `database-designer` |

## 📁 Estructura

```
Agentic Workspace/
├── .agents/
│   ├── config.yaml                # Configuración global y pipelines
│   ├── manifest.json              # Catálogo central de skills
│   ├── CHANGELOG.md               # Historial de cambios del workspace
│   ├── scripts/
│   │   ├── create_skill.py            # Generador de nuevas skills
│   │   ├── generate_agent_rules.py    # Generador de reglas multi-agente
│   │   └── validate_skills.py         # Validador de integridad del catálogo
│   └── skills/
│       ├── _template-skill/       # Plantilla para nuevas skills
│       ├── software-architect/    # Diseño de arquitectura y ADRs
│       ├── structure-analyzer/    # Análisis de estructura de proyectos
│       ├── code-improver/         # Detección de code smells y refactoring
│       ├── project-scaffolder/    # Scaffolding de proyectos nuevos
│       ├── test-strategist/       # Estrategia de testing y QA
│       ├── security-auditor/      # Auditoría de seguridad DevSecOps
│       ├── docs-generator/        # Generación de documentación técnica
│       ├── devops-engineer/       # CI/CD, IaC, contenedores, cloud
│       ├── git-workflow/          # Branching, commits, releases
│       ├── api-designer/          # Contratos OpenAPI / GraphQL
│       ├── performance-engineer/  # Profiling, load testing, caching
│       └── database-designer/     # Esquemas, migraciones, queries
├── .claude/
│   └── skills/                    # Lanzadores nativos de Claude Code (auto-generados)
├── .clinerules                    # Reglas auto-generadas (Roo-Code/Cline)
├── .pre-commit-config.yaml        # Hooks para validar calidad y seguridad
├── AGENTS.md                      # Reglas auto-generadas (Gemini)
├── CLAUDE.md                      # Reglas auto-generadas (Claude)
├── Consideraciones.md             # Decisiones técnicas del workspace
├── README.md                      # Este archivo
└── requirements.txt               # Dependencias Python del workspace
```

## 🛠️ Skills Disponibles

| Skill | Descripción | Lenguajes |
|---|---|---|
| `software-architect` | Diseño de sistemas, diagramas C4, ADRs | Python, JS/TS, Go, Java |
| `structure-analyzer` | Análisis de estructura y dependencias | Python, JS/TS, Go, Java |
| `code-improver` | Code smells, refactoring, SOLID | Python, JS/TS, Go, Java |
| `project-scaffolder` | Scaffolding con tooling completo | Python, JS/TS, Go, Java, Rust |
| `test-strategist` | Estrategia de testing y anti-patrones | Python, JS/TS, Go, Java |
| `security-auditor` | OWASP, secretos, supply chain | Python, JS/TS, Go, Java |
| `docs-generator` | API docs, runbooks, guías de usuario | Cualquiera |
| `devops-engineer` | CI/CD, IaC, Docker, despliegue cloud | Cualquiera |
| `git-workflow` | Branching, conventional commits, releases | Cualquiera |
| `api-designer` | OpenAPI, GraphQL, versionado, contract-first | Cualquiera |
| `performance-engineer` | Profiling, load testing, caching, APM | Cualquiera |
| `database-designer` | Diagramas ER, migraciones, optimización | Cualquiera |

## 🔄 Pipelines Multi-Skill

Para tareas complejas, las skills pueden encadenarse siguiendo los flujos definidos en `config.yaml`:

- **new-project**: `software-architect` → `project-scaffolder` → `test-strategist` → `security-auditor` → `docs-generator`
- **code-review**: `structure-analyzer` → `code-improver` → `security-auditor`
- **audit-full**: `structure-analyzer` → `security-auditor` → `test-strategist` → `code-improver` → `docs-generator`
- **quick-review**: `code-improver` → `security-auditor`

## 📏 Convenciones

- **Idioma de respuestas**: Siempre en **español**
- **Idioma de instrucciones internas**: Inglés (mejor procesamiento por LLMs)
- **Versionado de skills**: Semántico (`MAJOR.MINOR.PATCH`)

## 🧩 Modelo de Activación (Híbrido)

`.agents/skills/` es la **fuente única de verdad**. Desde ahí se generan dos cosas:

- **`.claude/skills/`** — lanzadores nativos para **Claude Code**. Claude Code los descubre
  y activa solos por su `description`; cada lanzador apunta al `SKILL.md` real en `.agents/`.
- **`.clinerules` / `.cursorrules` / `AGENTS.md` / `CLAUDE.md`** — reglas para otros agentes.

Así tienes activación nativa en Claude Code **sin perder** portabilidad multi-agente. Tras
editar cualquier skill o el `manifest.json`, **regenera** con `generate_agent_rules.py`.

## 🚀 Usar el Workspace en Cualquier Proyecto Nuevo

El repo es autosuficiente: clónalo, desvincúlalo de este historial y empieza tu
proyecto sobre la misma base agéntica.

```bash
git clone <url-o-ruta-de-este-repo> mi-proyecto
cd mi-proyecto
rm -rf .git        # PowerShell: Remove-Item -Recurse -Force .git
git init           # historial nuevo y limpio
```

Luego **reinicia Claude Code** en `mi-proyecto` para que cargue los lanzadores de
`.claude/skills/` y tengas las 12 skills activas.

> **Solo Claude Code:** si no usas otros agentes, puedes borrar `.clinerules`,
> `.cursorrules`, `AGENTS.md` y `.github/copilot-instructions.md`. La fuente de verdad
> (`.agents/`) se mantiene y esos archivos se regeneran cuando quieras con
> `generate_agent_rules.py`.

## 🔧 Mantenimiento

```bash
# Instalar dependencias del workspace y pre-commits
pip install -r requirements.txt
pre-commit install

# Validar integridad de todas las skills
python .agents/scripts/validate_skills.py

# Generar TODAS las reglas (incluye lanzadores nativos .claude/skills/)
python .agents/scripts/generate_agent_rules.py

# Solo regenerar los lanzadores nativos de Claude Code
python .agents/scripts/generate_agent_rules.py --agent claude-skills

# Ver catálogo de skills
cat .agents/manifest.json
```

## 📝 Contribuir una Nueva Skill

Puedes generar una nueva skill automáticamente usando el script proporcionado:

```bash
python .agents/scripts/create_skill.py <nombre-skill> "<descripción>"
```

Este script:
1. Copia la plantilla en `.agents/skills/<nombre-skill>/`
2. Registra la nueva skill en `.agents/manifest.json`

Después de ejecutarlo, recuerda:
3. Rellenar el `SKILL.md` de tu nueva skill con la información específica
4. Añadir tus archivos de referencia en `references/`
5. Añadir ejemplos de output en `examples/`
6. Actualizar este `README.md` (si es necesario documentarla) y `Consideraciones.md`
7. Ejecutar `python .agents/scripts/validate_skills.py` para asegurar que todo esté correcto.
