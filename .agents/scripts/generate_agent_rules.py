#!/usr/bin/env python3
"""
generate_agent_rules.py — Genera CLAUDE.md desde manifest.json y config.yaml.

Uso:
    python .agents/scripts/generate_agent_rules.py            # genera CLAUDE.md
    python .agents/scripts/generate_agent_rules.py --agent claude
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
    skill activates -- so they are surfaced directly in CLAUDE.md.
    """
    conv = (config or {}).get("conventions", {})
    if not conv:
        return ""
    workflow = conv.get("workflow", {})
    code = conv.get("code", {})
    commits = conv.get("commits", {})
    out = ["", "## Convenciones del Proyecto", ""]
    out.append(
        "> Fuente de verdad: `.agents/config.yaml` → `conventions`. "
        "Aplicar SIEMPRE, no solo cuando se activa una skill."
    )
    if workflow.get("update_docs"):
        out.append("")
        out.append("**Al terminar cualquier tarea:**")
        out.append("- Revisa si `README.md` y `Documentation.md` necesitan actualizarse.")
        out.append("- Si el cambio afecta la arquitectura, el stack, los flujos o las decisiones técnicas → actualiza `Documentation.md`.")
        out.append("- Si el cambio afecta la instalación, el stack usado o la descripción del proyecto → actualiza `README.md`.")
        out.append("- El Decision Log siempre va al final de `Documentation.md`.")
    if code:
        out.append("")
        out.append("**Código** (todo código que escribas):")
        out.append("- Código en inglés; comentarios en español.")
        out.append("- Sin docstrings de triple comilla — solo `#` para comentarios.")
        out.append("- Solo guión simple `-` en comentarios; nunca guión largo `—`.")
        out.append("- Nombres en `snake_case`, descriptivos y en inglés.")
        out.append("- Errores siempre explícitos con mensaje específico; sin swallowing de excepciones.")
        out.append("- Estructura pragmática: sin patrones forzados si no hacen falta.")
        out.append("- Dentro de las funciones, comentarios `#` que guíen el procedimiento paso a paso.")
        out.append("- Separación de secciones en archivos:")
        out.append("  ```")
        out.append("  # =============================================")
        out.append("  # Nombre de la sección")
        out.append("  # ---------------------------------------------")
        out.append("  ```")
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

# ── Generator ─────────────────────────────────────────────────────────────────

def generate_claude(manifest: dict) -> None:
    """Generate CLAUDE.md for Claude Code."""
    skills = manifest.get("skills", [])
    skill_table = build_skill_table(skills)

    content = f"""# CLAUDE.md — Agentic Workspace

> Configuración de Claude Code para este workspace.
> Para regenerar: `python .agents/scripts/generate_agent_rules.py`

## Sistema de Skills

Este workspace usa una arquitectura basada en **skills**. Antes de responder a cualquier tarea:

1. Lee `.agents/manifest.json` para identificar la skill aplicable según los `triggers`.
2. Lee el `SKILL.md` de la skill completo y adopta su rol y lineamientos.
3. Verifica sus `## Quality Gates` antes de entregar.

## Archivos Clave

- `.agents/manifest.json` — Catálogo de skills (fuente única de verdad para triggers y metadatos)
- `.agents/config.yaml` — Configuración del workspace (idioma y convenciones)
- `.agents/skills/<name>/SKILL.md` — Instrucciones de cada skill

## Skills Disponibles

{skill_table}
{build_conventions_section(load_config())}

## Idioma

Responde siempre en el idioma definido en `.agents/config.yaml` → `response_language` (por defecto: español).

## Regeneración

Tras editar manifest.json o config.yaml, ejecuta `python .agents/scripts/generate_agent_rules.py`
"""

    output_path = WORKSPACE_ROOT / "CLAUDE.md"
    output_path.write_text(content, encoding="utf-8")
    print(f"[OK] Generated {output_path.relative_to(WORKSPACE_ROOT)}")

# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Genera CLAUDE.md desde manifest.json y config.yaml"
    )
    # --agent se mantiene por compatibilidad; claude es el único target
    parser.add_argument(
        "--agent",
        choices=["claude"],
        default="claude",
        help="Target a generar (único disponible: claude)",
    )
    parser.parse_args()

    manifest = load_manifest()
    print(f"[*] Loaded manifest v{manifest.get('version', '?')} with {len(manifest.get('skills', []))} skills\n")

    generate_claude(manifest)

    print("\n[OK] CLAUDE.md generado correctamente.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
