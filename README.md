# Agentic Workspace

Workspace agéntico para Claude Code. Contiene skills especializadas que se activan automáticamente según el contexto de la conversación.

## Skills

| Skill | Qué hace | Se activa cuando... |
|-------|----------|---------------------|
| `docs` | Genera y actualiza `README.md` y `Documentation.md` | Pides documentar, crear el README, registrar una decisión |
| `diagrams` | Diagramas Mermaid (C4, secuencia, flujo) y DBML | Pides un diagrama de arquitectura, de BD, o un flujo |
| `code-quality` | Revisa lógica y claridad, propone mejoras sin editar | Pides un code review o sugerencias de mejora |

## Estructura

```
.agents/
├── manifest.json              # Catálogo de skills (fuente de verdad)
├── config.yaml                # Convenciones del workspace
├── scripts/
│   ├── generate_agent_rules.py  # Regenera CLAUDE.md desde manifest.json
│   └── validate_skills.py       # Valida integridad del catálogo
├── tests/
│   └── test_validate_skills.py
└── skills/
    ├── docs/
    ├── diagrams/
    └── code-quality/
CLAUDE.md                      # Instrucciones para Claude Code (auto-generado)
```

## Agregar una skill

1. Crear `.agents/skills/<nombre>/SKILL.md`
2. Agregar la entrada en `.agents/manifest.json`
3. Ejecutar `python .agents/scripts/generate_agent_rules.py`

## Mantenimiento

```bash
# Validar integridad de las skills
python .agents/scripts/validate_skills.py

# Regenerar CLAUDE.md tras editar manifest.json o config.yaml
python .agents/scripts/generate_agent_rules.py
```

## Usar en un proyecto nuevo

```bash
git clone <url> mi-proyecto
cd mi-proyecto
rm -rf .git
git init
```
