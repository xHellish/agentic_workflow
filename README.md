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
