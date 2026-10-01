# Agentic Workspace

Mi configuración personal de Claude Code: convenciones y skills que aplican en todos mis proyectos sin copiar nada.

## Cómo funciona

La carpeta `global/` está enlazada a `~/.claude/`, que es donde Claude Code lee la configuración de usuario en cualquier proyecto. Editar un archivo de este repo cambia el comportamiento en todos los proyectos al instante.

| En el repo | Se carga como | Contenido |
|------------|---------------|-----------|
| `global/CLAUDE.md` | importado desde `~/.claude/CLAUDE.md` | Idioma, estilo de código, commits y documentación |
| `global/skills/` | `~/.claude/skills/` | Skills personales |

## Skills

| Skill | Qué hace |
|-------|----------|
| `docs` | Crea y mantiene `README.md` y `Documentation.md` |
| `diagrams` | Diagramas Mermaid (C4, secuencia, flujo) y DBML dentro de `Documentation.md` |
| `code-quality` | Revisa lógica y claridad del código con ejemplos antes/después, sin editar archivos |

Se activan solas según su `description`. También se pueden invocar a mano: `/docs`, `/diagrams`, `/code-quality`.

## Instalación (una vez por máquina)

1. Clona el repo en una ruta fija.
2. En PowerShell, desde la raíz del repo:

   ```powershell
   New-Item -ItemType Junction -Path "$HOME\.claude\skills" -Target "$PWD\global\skills"
   New-Item -ItemType Junction -Path "$HOME\.claude\agentic" -Target "$PWD\global"
   Set-Content -Path "$HOME\.claude\CLAUDE.md" -Value "@~/.claude/agentic/CLAUDE.md" -Encoding ascii
   ```

3. Reinicia Claude Code.

`~/.claude/skills` no debe existir antes del paso 2. Si ya tienes skills ahí, muévelas primero a `global/skills/`.

## Proyecto nuevo

No hay que copiar nada: crea la carpeta, haz `git init` y abre Claude Code ahí. Las convenciones y las skills ya están activas.

Lo único propio de cada proyecto es su `CLAUDE.md` (stack, cómo correrlo, estructura). Se puede generar con `/init`.

## Agregar o editar una skill

1. Crea o edita `global/skills/<nombre>/SKILL.md`.
2. El frontmatter necesita `name` (igual al nombre de la carpeta) y `description`. La `description` decide cuándo se activa la skill: debe decir qué hace y cuándo usarla.
3. Haz commit para versionar el cambio. En otras máquinas basta con `git pull`.

## Desinstalar

```powershell
cmd /c rmdir "$HOME\.claude\skills"
cmd /c rmdir "$HOME\.claude\agentic"
Remove-Item "$HOME\.claude\CLAUDE.md"
```

`rmdir` quita solo el enlace. Nunca borres esos enlaces de forma recursiva: se borrarían los archivos del repo.
