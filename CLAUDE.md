# Agentic Workspace

Este repo es la fuente de mi configuración global de Claude Code.

- `global/CLAUDE.md` se importa desde `~/.claude/CLAUDE.md`: sus reglas ya aplican aquí y en todos los proyectos. No dupliques reglas en este archivo.
- `global/skills/` está enlazado como `~/.claude/skills/`: cualquier cambio a una skill aplica al instante en todos los proyectos.
- Las skills se activan por su `description`. Al crear o editar una, la `description` debe decir qué hace y cuándo usarla, y `name` debe ser igual al nombre de su carpeta.
- Nunca borres de forma recursiva `~/.claude/skills` ni `~/.claude/agentic`: son enlaces a este repo y se borrarían sus archivos.
- Este repo es de configuración: mantén su `README.md` al día, pero no crees `Documentation.md`.
