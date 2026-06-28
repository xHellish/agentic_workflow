#!/usr/bin/env python3
"""
generate_agent_rules.py — Genera las instrucciones de Claude Code desde manifest.json.

Uso:
    python .agents/scripts/generate_agent_rules.py         # genera CLAUDE.md
    python .agents/scripts/generate_agent_rules.py --agent claude

Targets disponibles:
    - claude              → CLAUDE.md  (default)
    - claude-skills-global → ~/.claude/skills/<name>/SKILL.md  (opt-in, escribe fuera del repo)
    - cline               → .clinerules  (opt-in)
    - gemini              → AGENTS.md  (opt-in)
    - copilot             → .github/copilot-instructions.md  (opt-in)
"""

import json
import sys
import argparse
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────

WORKSPACE_ROOT = Path(__file__).parent.parent.parent
AGENTS_DIR = WORKSPACE_ROOT / ".agents"
MANIFEST_PATH = AGENTS_DIR / "manifest.json"

# ── Helpers ───────────────────────────────────────────────────────────────────

def load_manifest() -> dict:
    """Load and return the manifest.json content."""
    if not MANIFEST_PATH.exists():
        print(f"[ERROR] manifest.json not found at {MANIFEST_PATH}")
        sys.exit(1)
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def build_skill_table(skills: list[dict]) -> str:
    """Build a markdown table of skills and their primary triggers."""
    lines = [
        "| Skill | Triggers Principales | Descripción |",
        "|-------|---------------------|------------|",
    ]
    for skill in skills:
        name = skill.get("name", "")
        description = skill.get("description", "")
        triggers = skill.get("triggers", [])
        trigger_str = ", ".join(f'"{t}"' for t in triggers[:3])
        if len(triggers) > 3:
            trigger_str += f" (+{len(triggers) - 3} more)"
        lines.append(f"| `{name}` | {trigger_str} | {description[:60]}... |")
    return "\n".join(lines)


def build_pipelines_section(pipelines: dict) -> str:
    """Build a markdown section describing available pipelines."""
    if not pipelines:
        return ""
    lines = ["\n## Pipelines Multi-Skill\n"]
    for name, pipeline in pipelines.items():
        desc = pipeline.get("description", "")
        steps = " → ".join(f"`{s}`" for s in pipeline.get("steps", []))
        lines.append(f"- **{name}**: {desc}")
        lines.append(f"  - Pasos: {steps}")
    return "\n".join(lines)


def load_config() -> dict:
    """Load .agents/config.yaml (returns {} if missing or unparseable)."""
    config_path = AGENTS_DIR / "config.yaml"
    if not config_path.exists():
        return {}
    try:
        import yaml
        return yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}


def build_conventions_section(config: dict) -> str:
    """Build the '## Project Conventions' section from config.yaml -> conventions.

    These rules must apply ALWAYS (e.g. every commit the agent writes), not only when a
    skill activates -- so they are surfaced directly in CLAUDE.md / AGENTS.md.
    """
    conv = (config or {}).get("conventions", {})
    if not conv:
        return ""
    commits = conv.get("commits", {})
    out = ["", "## Convenciones del Proyecto", ""]
    out.append(
        "> Fuente de verdad: `.agents/config.yaml` → `conventions`. "
        "Aplicar SIEMPRE, no solo cuando se activa una skill."
    )
    if commits:
        lang = commits.get("language", "es")
        out.append("")
        out.append("**Commits** (todo commit que escribas):")
        out.append(f"- Título descriptivo en `{lang}` que resuma el avance, SIN prefijo de tipo (nunca `feat:`/`fix:`/`docs:`).")
        out.append("- Incluye SIEMPRE el cuerpo: detalles en lista de guiones `-`, cada punto conciso, en español.")
        if not commits.get("emojis", False):
            out.append("- Sin emojis.")
        if not commits.get("trailing_period", True):
            out.append("- Sin punto final en el título.")
        if commits.get("max_subject_length"):
            out.append(f"- Título <= {commits['max_subject_length']} caracteres.")
        if commits.get("coauthor") is False:
            out.append("- **NO** añadir `Co-Authored-By: Claude` salvo petición explícita del usuario.")
    return "\n".join(out)

# ── Generators ────────────────────────────────────────────────────────────────

def generate_cline(manifest: dict) -> None:
    """Generate .clinerules for Cline / Roo-Code."""
    skills = manifest.get("skills", [])
    pipelines = manifest.get("pipelines", {})

    content = f"""Antes de responder o ejecutar cualquier tarea, revisa obligatoriamente el directorio `.agents/skills/`.
Consulta `.agents/manifest.json` para identificar cuál skill corresponde al contexto actual, usando la lista de `triggers` de cada skill como referencia de activación.
Una vez identificada la skill, lee su `SKILL.md` completo, adopta ese rol, sus responsabilidades, y carga sus archivos de referencia siguiendo la sección `## Reference Loading`.
Si la tarea involucra múltiples skills (ej. análisis + refactoring), actívalas secuencialmente siguiendo el orden lógico definido en los pipelines de `.agents/config.yaml`.
Lee `.agents/config.yaml` para obtener el idioma de respuesta, stacks soportados y configuración por skill.
"""

    output_path = WORKSPACE_ROOT / ".clinerules"
    output_path.write_text(content, encoding="utf-8")
    print(f"[OK] Generated {output_path.relative_to(WORKSPACE_ROOT)}")


def generate_claude(manifest: dict) -> None:
    """Generate CLAUDE.md for Claude Code."""
    skills = manifest.get("skills", [])
    pipelines = manifest.get("pipelines", {})
    skill_table = build_skill_table(skills)
    pipelines_section = build_pipelines_section(pipelines)

    content = f"""# CLAUDE.md — Agentic Workspace

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

{skill_table}
{pipelines_section}
{build_conventions_section(load_config())}

## Idioma

Responde siempre en el idioma definido en `.agents/config.yaml` → `response_language` (por defecto: español).

## Validación

Tras editar skills, ejecuta `python .agents/scripts/validate_skills.py`
Tras editar manifest.json o config.yaml, ejecuta `python .agents/scripts/generate_agent_rules.py --agent claude`
"""

    output_path = WORKSPACE_ROOT / "CLAUDE.md"
    output_path.write_text(content, encoding="utf-8")
    print(f"[OK] Generated {output_path.relative_to(WORKSPACE_ROOT)}")


def generate_agents_md(manifest: dict) -> None:
    """Generate AGENTS.md for Gemini Code Assist / Jules / Antigravity."""
    skills = manifest.get("skills", [])
    pipelines = manifest.get("pipelines", {})
    skill_table = build_skill_table(skills)
    pipelines_section = build_pipelines_section(pipelines)

    content = f"""# AGENTS.md — Agentic Workspace

> Activation rules for Gemini Code Assist, Jules, and Antigravity agents.
> Auto-generated by `generate_agent_rules.py` — edit manifest.json to update triggers.

## Core Instruction

Before responding to or executing any task, you MUST:

1. **Check the skills catalog**: Read `.agents/manifest.json` to identify which skill applies to the current context, using the `triggers` field of each skill as activation keywords.
2. **Load the skill**: Once a skill is identified, read its full `SKILL.md` and adopt that role, responsibilities, and guidelines.
3. **Load references**: Follow the `## Reference Loading` section in the skill to determine which reference files to read.
4. **Multi-skill tasks**: If a task spans multiple skills, activate them **sequentially in logical order** as defined in the `pipelines` section of `.agents/config.yaml`.

## Configuration

Read `.agents/config.yaml` for:
- Response language (`response_language`)
- Supported language stacks
- Per-skill behavior overrides
- Available multi-skill pipelines

## Available Skills

{skill_table}
{pipelines_section}
{build_conventions_section(load_config())}

## Response Language

All responses must be in the language specified in `.agents/config.yaml` → `response_language` (default: **Spanish**).

## Autonomous Operation (`/goal` command)

When the `/goal` command is used:
- Operate autonomously without pausing for confirmations
- Self-correct: run tests, read errors, fix, repeat until passing
- Use subagents for parallel workstreams
- Follow the skill pipeline defined in `.agents/config.yaml`
"""

    output_path = WORKSPACE_ROOT / "AGENTS.md"
    output_path.write_text(content, encoding="utf-8")
    print(f"[OK] Generated {output_path.relative_to(WORKSPACE_ROOT)}")


def generate_copilot(manifest: dict) -> None:
    """Generate .github/copilot-instructions.md for GitHub Copilot."""
    skills = manifest.get("skills", [])
    pipelines = manifest.get("pipelines", {})
    skill_table = build_skill_table(skills)
    pipelines_section = build_pipelines_section(pipelines)

    content = f"""# GitHub Copilot Instructions — Agentic Workspace

> Auto-generated by `generate_agent_rules.py` — edit manifest.json to update.

This workspace uses a skill-based agent architecture. When assisting with tasks:

1. Identify the relevant skill from `.agents/manifest.json` using the trigger keywords.
2. Read the skill's `SKILL.md` for role definition, responsibilities, and output format.
3. Load reference files as specified in the skill's `## Reference Loading` section.

## Available Skills

{skill_table}
{pipelines_section}

## Language: Respond in Spanish (configurable via `.agents/config.yaml`).
"""

    output_path = WORKSPACE_ROOT / ".github" / "copilot-instructions.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    print(f"[OK] Generated {output_path.relative_to(WORKSPACE_ROOT)}")


def generate_claude_skills(manifest: dict) -> None:
    """Generate native Claude Code skill launchers in .claude/skills/<name>/SKILL.md.

    Each launcher is a thin pointer: its frontmatter (name + description) is what Claude
    Code uses to surface and activate the skill natively, while the full definition stays
    in .agents/skills/ (single source of truth). This keeps the multi-agent portability
    provided by manifest.json intact — re-run this generator after editing any skill.
    """
    skills = manifest.get("skills", [])
    lang_note = (
        "Responde siempre en el idioma configurado en `.agents/config.yaml` "
        "(por defecto: español)."
    )
    skills_root = WORKSPACE_ROOT / ".claude" / "skills"
    count = 0
    for skill in skills:
        name = skill.get("name", "")
        if not name:
            continue
        description = skill.get("description", "").replace('"', "'")
        triggers = skill.get("triggers", [])
        triggers_line = ", ".join(f'"{t}"' for t in triggers)
        source = f".agents/skills/{name}/SKILL.md"

        content = f"""---
name: {name}
description: "{description}"
---

# {name}

> {lang_note}

Skill del **Agentic Workspace**. La definición completa vive en `{source}`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `{source}` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/{name}/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** {triggers_line}
"""
        output_path = skills_root / name / "SKILL.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        count += 1

    print(f"[OK] Generated {count} native skill launcher(s) under .claude/skills/")


def generate_claude_skills_global(manifest: dict) -> None:
    """Install GLOBAL Claude Code skill launchers in ~/.claude/skills/<name>/SKILL.md.

    Unlike generate_claude_skills (project-scoped, relative paths), these point at THIS
    workspace by ABSOLUTE path, so the skills are available in every Claude Code session
    regardless of the working directory. The workspace stays the single source of truth.
    Opt-in only (excluded from the 'all' run, since it writes outside the repo).
    """
    skills = manifest.get("skills", [])
    abs_root = WORKSPACE_ROOT.resolve().as_posix()
    skills_root = Path.home() / ".claude" / "skills"
    count = 0
    for skill in skills:
        name = skill.get("name", "")
        if not name:
            continue
        description = skill.get("description", "").replace('"', "'")
        source = f"{abs_root}/.agents/skills/{name}/SKILL.md"
        skill_dir = f"{abs_root}/.agents/skills/{name}"

        content = f"""---
name: {name}
description: "{description}"
---

# {name} (global)

> Responde siempre en español (config del workspace maestro Agentic Workspace).

Skill global del **Agentic Workspace**. La definición completa y sus references viven en el
workspace maestro (fuente única de verdad):

`{source}`

**Al activar esta skill:**
1. Lee ese archivo completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su `## Reference Loading`, resolviendo `references/...` y `examples/...` **relativas a**
   `{skill_dir}` (no al proyecto actual).
3. Verifica sus `## Quality Gates` antes de entregar.

> Si mueves o borras el workspace maestro, regenera con:
> `python {abs_root}/.agents/scripts/generate_agent_rules.py --agent claude-skills-global`
"""
        output_path = skills_root / name / "SKILL.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        count += 1

    print(f"[OK] Installed {count} GLOBAL skill launcher(s) under {skills_root}")


# ── Main ──────────────────────────────────────────────────────────────────────

GENERATORS = {
    "claude": generate_claude,
    "claude-skills-global": generate_claude_skills_global,
    "cline": generate_cline,
    "gemini": generate_agents_md,
    "copilot": generate_copilot,
}

# Targets excluidos del run por defecto (opt-in solo).
ALL_EXCLUDE = {"claude-skills-global", "cline", "gemini", "copilot"}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate agent-specific rule files from manifest.json"
    )
    parser.add_argument(
        "--agent",
        choices=list(GENERATORS.keys()),
        help="Generate rules for a specific agent only (default: all agents)",
    )
    args = parser.parse_args()

    manifest = load_manifest()
    print(f"[*] Loaded manifest v{manifest.get('version', '?')} with {len(manifest.get('skills', []))} skills\n")

    if args.agent:
        GENERATORS[args.agent](manifest)
    else:
        for name, gen in GENERATORS.items():
            if name in ALL_EXCLUDE:
                continue
            gen(manifest)

    print("\n[OK] Agent rule files generated successfully.")
    print("     Run 'python .agents/scripts/validate_skills.py' to verify skill integrity.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
