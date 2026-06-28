---
name: diagrams
description: "Genera diagramas Mermaid (C4, secuencia, flujo) y DBML para base de datos. Los inserta en Documentation.md."
---

# Rol

Genero diagramas técnicos precisos a partir del código real del proyecto y los integro en la sección correspondiente de `Documentation.md`.

## Cuándo activarme

Cuando el usuario pida un diagrama específico: arquitectura C4, esquema de base de datos, flujo de secuencia, o cualquier otro diagrama de diseño. No es necesario pedir documentación completa — un diagrama solo ya activa esta skill.

## Formatos

### DBML — Esquema de base de datos

Para la sección **Base de datos** de `Documentation.md`. Compatible con [dbdiagram.io](https://dbdiagram.io).

```dbml
Table users {
  id uuid [pk, default: `gen_random_uuid()`]
  email varchar [unique, not null]
  created_at timestamp [default: `now()`]
}
```

### Mermaid — Arquitectura y flujos

Para las secciones **Arquitectura general** y **Flujos clave** de `Documentation.md`.

| Tipo | Cuándo usarlo | Sintaxis Mermaid |
|------|--------------|-----------------|
| C4 Context | Visión del sistema desde afuera (actores + sistema) | `C4Context` |
| C4 Container | Servicios, DBs, frontends y sus relaciones | `C4Container` |
| C4 Component | Módulos internos de un servicio específico | `C4Component` |
| Sequence | Flujos temporales entre actores o servicios | `sequenceDiagram` |
| Flowchart | Decisiones y procesos internos | `flowchart TD` |

## Proceso

1. **Leer primero** — Lee los archivos relevantes (modelos, rutas, esquemas, estructura de carpetas) para que el diagrama refleje el código real, no suposiciones.
2. **Generar** — Produce el diagrama en el formato correcto.
3. **Insertar** — Actualiza la sección correspondiente en `Documentation.md`:
   - Diagrama de DB → sección **Base de datos**
   - C4 → sección **Arquitectura general**
   - Flujos → sección **Flujos clave**

Si `Documentation.md` no existe, créalo con solo la sección necesaria.
Si ya existe, léelo completo y edita únicamente la sección del diagrama.

## Coherencia entre niveles C4

Si el proyecto tiene múltiples diagramas C4, deben ser coherentes:
- Los contenedores del C4 Context deben aparecer en el C4 Container.
- Los componentes del C4 Container deben aparecer en el C4 Component.

## Quality Gates

- [ ] El diagrama es sintácticamente válido (sin errores de sintaxis Mermaid o DBML).
- [ ] Refleja el código real del proyecto, no una arquitectura genérica o supuesta.
- [ ] Si hay múltiples niveles C4, son coherentes entre sí (mismos nombres, mismas relaciones).
- [ ] El DBML incluye los tipos de dato correctos y las relaciones reales entre tablas.
