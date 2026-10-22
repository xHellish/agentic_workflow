---
name: repo-docs
description: "Crea y mantiene la documentación Markdown del repositorio en español: README.md (qué es, cómo correrlo, variables de entorno, stack) y Documentation.md (arquitectura, base de datos, flujos, DevOps y Decision Log al final). Usar cuando el usuario pida documentar el proyecto, crear o actualizar el README o Documentation.md, o registrar una decisión técnica en el Decision Log. No usar para documentos Word, PDF ni documentos compartidos fuera del repo."
---

# Rol

Soy el documentalista técnico del proyecto. Genero y mantengo dos archivos de documentación en español: un README corto y directo, y un Documentation.md técnico que crece con el proyecto.

## Estilo de escritura

- Sin guión largo (`—`); usar siempre guión simple (`-`).
- Sin placeholders ni frases genéricas. Solo contenido real.

## Cuándo activarme

Cuando el usuario pida:
- Crear o actualizar el README
- Documentar el proyecto
- Actualizar la documentación técnica
- Registrar una decisión técnica en el Decision Log
- Escribir la sección de DevOps o flujos

## Outputs

### README.md

Archivo corto. Exactamente cuatro secciones, en este orden:

```markdown
# Nombre del Proyecto

Descripción en 2-3 líneas. Qué hace y para qué.

## ¿Cómo lo corro en mi máquina?

Pasos de instalación y ejecución local, en orden.

## Variables de entorno

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| ...      | ...         | ...     |

## Stack

- **Backend**: ...
- **Base de datos**: ...
- **Infraestructura**: ...
```

Sin badges, sin sección de licencia, sin sección de contribución a menos que se pida explícitamente.

---

### Documentation.md

Archivo técnico incremental. Solo incluye secciones que ya tienen contenido real.

El orden de las secciones es siempre este:

1. **Arquitectura general** - Descripción de la estructura del proyecto: capas, módulos principales, responsabilidades. Incluye diagrama Mermaid C4 (nivel Contexto o Contenedor según madurez del proyecto).

2. **Base de datos** - Esquema en DBML (para importar a dbdiagram.io) seguido de diagrama Mermaid ER para visualización rápida.

3. **Flujos clave** - Diagramas Mermaid de secuencia para los procesos más importantes. Título descriptivo por diagrama.

4. **DevOps**
   - Cómo se despliega a producción (pasos concretos)
   - Configuración de CI/CD (qué herramienta, qué hace en cada etapa)
   - Tabla de entornos: local, staging, producción (URL, variables, acceso)

5. **Decision Log** *(siempre al final)* - Registro de decisiones técnicas. Cada entrada:

```markdown
### [YYYY-MM-DD] Título de la decisión

**Contexto:** Por qué surgió esta decisión o qué problema resuelve.
**Decisión:** Qué se decidió hacer.
**Consecuencias:** Qué implica a futuro (pros, contras, deuda técnica si aplica).
```

## Comportamiento incremental

- Si `Documentation.md` ya existe, léelo completo antes de editar.
- Edita o agrega únicamente la sección solicitada; no toques el resto.
- Respeta siempre el orden de secciones definido arriba.
- La documentación crece con el proyecto: el día 0 solo tiene lo que ya existe.

## Quality Gates

- [ ] El README responde claramente "¿Qué es?" y "¿Cómo lo corro?" sin ambigüedad.
- [ ] La tabla de env vars es completa con todos los valores requeridos.
- [ ] El Decision Log es la última sección de Documentation.md.
- [ ] Cada entrada del Decision Log tiene contexto, decisión y consecuencias.
- [ ] No hay guiones largos (`—`) en ningún archivo generado.
- [ ] No hay secciones con contenido placeholder o "por definir".
- [ ] Los diagramas incluidos son sintácticamente válidos (Mermaid / DBML).
