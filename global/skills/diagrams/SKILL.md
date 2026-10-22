---
name: diagrams
description: "Genera diagramas técnicos a partir del código real: Mermaid (C4, secuencia, flowchart) y DBML para el esquema de base de datos, insertados en la sección correspondiente de Documentation.md. Usar cuando el usuario pida un diagrama de arquitectura o C4, de la base de datos (ER o DBML), de secuencia, de un flujo del sistema o cualquier diagrama Mermaid."
---

# Rol

Genero diagramas técnicos precisos a partir del código real del proyecto y los integro en la sección correspondiente de `Documentation.md`.

## Cuándo activarme

Cuando el usuario pida un diagrama específico: arquitectura C4, esquema de base de datos, flujo de secuencia o cualquier otro diagrama de diseño. No hace falta pedir documentación completa: un diagrama solo ya activa esta skill.

## Formatos

### DBML: esquema de base de datos

Para la sección **Base de datos** de `Documentation.md`. Compatible con [dbdiagram.io](https://dbdiagram.io).

```dbml
Table users {
  id uuid [pk, default: `gen_random_uuid()`]
  email varchar [unique, not null]
  created_at timestamp [default: `now()`]
}
```

### Mermaid: arquitectura y flujos

Para las secciones **Arquitectura general** y **Flujos clave** de `Documentation.md`.

| Tipo | Cuándo usarlo | Sintaxis Mermaid |
|------|--------------|-----------------|
| C4 Context | Visión del sistema desde afuera (actores + sistema) | `C4Context` |
| C4 Container | Servicios, DBs, frontends y sus relaciones | `C4Container` |
| C4 Component | Módulos internos de un servicio específico | `C4Component` |
| Sequence | Flujos temporales entre actores o servicios | `sequenceDiagram` |
| Flowchart | Decisiones y procesos internos | `flowchart TD` |

## Proceso

1. **Leer primero:** lee los archivos relevantes (modelos, rutas, esquemas, estructura de carpetas) para que el diagrama refleje el código real, no suposiciones.
2. **Generar:** produce el diagrama en el formato correcto.
3. **Insertar:** actualiza la sección correspondiente en `Documentation.md`:
   - Diagrama de DB → sección **Base de datos**
   - C4 → sección **Arquitectura general**
   - Flujos → sección **Flujos clave**

## Dónde insertar en Documentation.md

El orden de las secciones lo define la skill `repo-docs` y siempre se respeta:

1. Arquitectura general
2. Base de datos
3. Flujos clave
4. DevOps
5. Decision Log (siempre al final)

- Si `Documentation.md` no existe, créalo solo con la sección necesaria.
- Si existe, léelo completo y edita únicamente la sección del diagrama.
- Si la sección todavía no existe, créala en su posición según ese orden. Nunca la agregues después del Decision Log.

## Coherencia entre niveles C4

Si el proyecto tiene múltiples diagramas C4, deben ser coherentes:
- Los contenedores del C4 Context deben aparecer en el C4 Container.
- Los componentes del C4 Container deben aparecer en el C4 Component.

## Quality Gates

- [ ] El diagrama es sintácticamente válido (sin errores de sintaxis Mermaid o DBML).
- [ ] Refleja el código real del proyecto, no una arquitectura genérica o supuesta.
- [ ] Si hay múltiples niveles C4, son coherentes entre sí (mismos nombres, mismas relaciones).
- [ ] El DBML incluye los tipos de dato correctos y las relaciones reales entre tablas.
- [ ] La sección quedó en su posición según el orden y el Decision Log sigue al final.
