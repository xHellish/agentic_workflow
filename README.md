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

## 📁 Estructura

```
Agentic Workspace/
├── .agents/
│   ├── manifest.json              # Catálogo central de skills
│   ├── CHANGELOG.md               # Historial de cambios del workspace
│   ├── scripts/
│   │   └── validate_skills.py     # Validador de integridad de skills
│   └── skills/
│       ├── _template-skill/       # Plantilla para nuevas skills
│       ├── software-architect/    # Diseño de arquitectura y ADRs
│       ├── structure-analyzer/    # Análisis de estructura de proyectos
│       ├── code-improver/         # Detección de code smells y refactoring
│       ├── project-scaffolder/    # Scaffolding de proyectos nuevos
│       ├── test-strategist/       # Estrategia de testing y QA
│       ├── security-auditor/      # Auditoría de seguridad DevSecOps
│       └── docs-generator/        # Generación de documentación técnica
├── Consideraciones.md             # Decisiones técnicas del workspace
├── mejoras_actuales.md            # Backlog de mejoras pendientes
└── README.md                      # Este archivo
```

## 🛠️ Skills Disponibles

| Skill | Descripción | Lenguajes |
|---|---|---|
| `software-architect` | Diseño de sistemas, diagramas C4, ADRs | Python, JS/TS, Go, Java |
| `structure-analyzer` | Análisis de estructura y dependencias | Python, JS/TS, Go, Java |
| `code-improver` | Code smells, refactoring, SOLID | Python, JS/TS, Go, Java |
| `project-scaffolder` | Scaffolding con tooling completo | Python, JS/TS, Go, Java, Rust |
| `test-strategist` | Estrategia de testing y anti-patrones | Python, JS/TS |
| `security-auditor` | OWASP, secretos, supply chain | Python, JS/TS |
| `docs-generator` | API docs, runbooks, guías de usuario | Cualquiera |

## 📏 Convenciones

- **Idioma de respuestas**: Siempre en **español**
- **Idioma de instrucciones internas**: Inglés (mejor procesamiento por LLMs)
- **Versionado de skills**: Semántico (`MAJOR.MINOR.PATCH`)

## 🔧 Mantenimiento

```bash
# Validar integridad de todas las skills
python .agents/scripts/validate_skills.py

# Ver catálogo de skills
cat .agents/manifest.json
```

## 📝 Contribuir una Nueva Skill

1. Copia `.agents/skills/_template-skill/` con el nuevo nombre
2. Rellena `SKILL.md` siguiendo la plantilla
3. Añade tus archivos de referencia en `references/`
4. Añade ejemplos de output en `examples/`
5. Registra la skill en `.agents/manifest.json`
6. Actualiza este README y `Consideraciones.md`
7. Ejecuta `python .agents/scripts/validate_skills.py`
