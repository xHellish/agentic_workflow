# Agentic Workspace — Consideraciones

## Propósito

Este workspace es un entorno agéntico diseñado para asistir en el diseño, análisis y mejora de proyectos de software. Contiene un conjunto de **Agent Skills** reutilizables que se activan según el contexto de la conversación.

## Skills Disponibles

| Skill | Descripción | Activación |
|-------|-------------|------------|
| `software-architect` | Diseño de arquitectura, diagramas, ADRs | "diseñar sistema", "arquitectura", "diagrama" |
| `structure-analyzer` | Análisis de estructura de proyectos | "analizar estructura", "mapa de dependencias" |
| `code-improver` | Detección de code smells y refactoring | "mejorar código", "refactorizar", "code review" |
| `project-scaffolder` | Scaffolding de proyectos nuevos | "crear proyecto", "inicializar", "setup" |

## Convenciones

### Idioma
- Las instrucciones de las skills están en **inglés** (mejor procesamiento por los modelos)
- Las **respuestas siempre deben ser en español**

### Estructura de Archivos
```
Agentic Workspace/
├── .agents/
│   └── skills/
│       ├── software-architect/    # Diseño de software
│       ├── structure-analyzer/    # Análisis de estructura
│       ├── code-improver/         # Mejoras de código
│       └── project-scaffolder/    # Scaffolding de proyectos
├── Consideraciones.md             # Este archivo
└── [proyectos futuros...]
```

### Patrones de Diseño
No hay preferencia fija — se adaptan según el proyecto. Las skills están preparadas para recomendar el patrón más adecuado según el contexto.

## Uso

Para activar una skill, simplemente describe lo que necesitas. El agente detectará automáticamente cuál skill es relevante y cargará las instrucciones correspondientes.

**Ejemplos:**
- *"Quiero diseñar una API REST para gestión de usuarios"* → `software-architect`
- *"Analiza la estructura de este proyecto"* → `structure-analyzer`
- *"Revisa este código y sugiere mejoras"* → `code-improver`
- *"Crea un nuevo proyecto con FastAPI"* → `project-scaffolder`
