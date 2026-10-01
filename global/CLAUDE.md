# Preferencias personales

Reglas que aplican en todos mis proyectos.

## Idioma

Responde siempre en español.

## Estilo de escritura

En código, comentarios, README y documentación: nunca uses el guión largo `—`, usa siempre `-`.

## Código

- Código en inglés; comentarios en español.
- Sin docstrings de triple comilla; solo comentarios de una línea con `#`.
- Nombres en `snake_case`, descriptivos y en inglés.
- Errores siempre explícitos con mensaje específico; nunca silenciar excepciones.
- Estructura pragmática: sin patrones ni capas forzadas si no hacen falta.
- Dentro de las funciones, comentarios `#` que guíen el procedimiento paso a paso.
- Cada sección del archivo (imports, variables, clases, funciones, etc.) se separa así:

  ```
  # =============================================
  # Nombre de la sección
  # ---------------------------------------------
  ```

  El `=` solo se usa para dividir secciones; todo lo demás se separa con `-`.

## Documentación

Al terminar cualquier tarea:

- Revisa si `README.md` y `Documentation.md` necesitan actualizarse.
- Si el cambio afecta la arquitectura, el stack, los flujos o las decisiones técnicas, actualiza `Documentation.md`.
- Si el cambio afecta la instalación, el stack usado o la descripción del proyecto, actualiza `README.md`.
- El Decision Log siempre va al final de `Documentation.md`.

## Commits

- Título descriptivo que resuma el avance, en español salvo que pida inglés explícitamente.
- Sin prefijo de tipo: nunca `feat:`, `fix:`, `docs:` ni similares.
- Siempre con cuerpo: detalles en lista de guiones `-`, cada punto conciso.
- Sin emojis, sin punto final en el título, título de máximo 72 caracteres.
- No añadir `Co-Authored-By` salvo que lo pida explícitamente.
