---
name: api-designer
description: "Diseña contratos de API (OpenAPI, GraphQL schemas), estrategias de versionado y arquitecturas contract-first."
---

# api-designer

> Responde siempre en el idioma configurado en `.agents/config.yaml` (por defecto: español).

Skill del **Agentic Workspace**. La definición completa vive en `.agents/skills/api-designer/SKILL.md`
(fuente única de verdad). Este archivo es solo el lanzador nativo de Claude Code.

**Al activar esta skill:**
1. Lee `.agents/skills/api-designer/SKILL.md` completo y adopta su rol, responsabilidades y formato de salida.
2. Sigue su sección `## Reference Loading` para cargar los archivos relevantes de
   `.agents/skills/api-designer/references/`.
3. Verifica sus `## Quality Gates` antes de entregar.

**Triggers:** "api designer", "openapi", "swagger", "graphql schema", "api design", "restful", "endpoint design", "api versioning"
