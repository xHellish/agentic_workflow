# Agentic Workspace

Workspace de Claude Code con skills especializadas para documentación, diagramas y revisión de código.

## Skills

| Skill | Qué hace | Se activa cuando... |
|-------|----------|---------------------|
| `docs` | Genera y actualiza `README.md` y `Documentation.md` | Pides documentar, crear el README, registrar una decisión técnica |
| `diagrams` | Genera diagramas Mermaid (C4, secuencia, flujo) y DBML para base de datos | Pides un diagrama de arquitectura, de la DB, o un flujo |
| `code-quality` | Revisa lógica y claridad del código. Propone mejoras con antes/después. No edita archivos. | Pides revisar código o un code review |

La activación es automática por contexto — no necesitas invocar la skill explícitamente.

## Usar en un proyecto nuevo

Clona el repo, desvinculalo del historial y empieza tu proyecto:

```bash
git clone <url> mi-proyecto
cd mi-proyecto
rm -rf .git          # PowerShell: Remove-Item -Recurse -Force .git
git init
```

Reinicia Claude Code en el directorio del proyecto para que cargue el `CLAUDE.md`.

## Estructura

```
.agents/
├── manifest.json          # Catálogo de skills (fuente de verdad)
├── config.yaml            # Convenciones de commits y configuración
├── skills/
│   ├── docs/SKILL.md
│   ├── diagrams/SKILL.md
│   └── code-quality/SKILL.md
├── scripts/
│   ├── generate_agent_rules.py   # Regenera CLAUDE.md desde manifest.json
│   └── validate_skills.py        # Valida integridad de las skills
└── tests/
    └── test_validate_skills.py
```

## Mantenimiento

```bash
# Instalar dependencias (necesario para los comandos de abajo)
pip install -r requirements.txt

# Después de editar una skill o el manifest.json
python .agents/scripts/generate_agent_rules.py

# Validar integridad de las skills
python .agents/scripts/validate_skills.py

# Correr tests del workspace
pytest .agents/tests/
```
