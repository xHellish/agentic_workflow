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
| `docs` | "documentar", "genera el README", "actualiza docs" (+7 more) | Genera y actualiza README.md conciso y Documentation.md técn... |
| `diagrams` | "diagrama", "diagrama C4", "diagrama de la base de datos" (+7 more) | Genera diagramas Mermaid (C4, secuencia, flujo) y DBML para ... |
| `code-quality` | "revisa este código", "qué mejorarías", "code review" (+5 more) | Revisa código en busca de problemas de lógica y claridad. Pr... |


## Convenciones del Proyecto

> Fuente de verdad: `.agents/config.yaml` → `conventions`. Aplicar SIEMPRE, no solo cuando se activa una skill.

**Al terminar cualquier tarea:**
- Revisa si `README.md` y `Documentation.md` necesitan actualizarse.
- Si el cambio afecta la arquitectura, el stack, los flujos o las decisiones técnicas → actualiza `Documentation.md`.
- Si el cambio afecta la instalación, el stack usado o la descripción del proyecto → actualiza `README.md`.
- El Decision Log siempre va al final de `Documentation.md`.

**Código** (todo código que escribas):
- Código en inglés; comentarios en español.
- Sin docstrings de triple comilla — solo `#` para comentarios.
- Solo guión simple `-` en comentarios; nunca guión largo `—`.
- Nombres en `snake_case`, descriptivos y en inglés.
- Errores siempre explícitos con mensaje específico; sin swallowing de excepciones.
- Estructura pragmática: sin patrones forzados si no hacen falta.
- Dentro de las funciones, comentarios `#` que guíen el procedimiento paso a paso.
- Separación de secciones en archivos:
  ```
  # =============================================
  # Nombre de la sección
  # ---------------------------------------------
  ```

**Commits** (todo commit que escribas):
- Título descriptivo en `es` que resuma el avance, SIN prefijo de tipo (nunca `feat:`/`fix:`/`docs:`).
- Incluye SIEMPRE el cuerpo: detalles en lista de guiones `-`, cada punto conciso, en español.
- Sin emojis.
- Sin punto final en el título.
- Título <= 72 caracteres.
- **NO** añadir `Co-Authored-By: Claude` salvo petición explícita del usuario.

## Idioma

Responde siempre en el idioma definido en `.agents/config.yaml` → `response_language` (por defecto: español).

## Validación

Tras editar skills, ejecuta `python .agents/scripts/validate_skills.py`
Tras editar manifest.json o config.yaml, ejecuta `python .agents/scripts/generate_agent_rules.py --agent claude`
