# Preferencias personales

Reglas que aplican en todos mis proyectos.

## Idioma

Responde siempre en español.

## Forma de trabajar

- Ante una tarea grande o ambigua, entrevístame sobre el "cómo" antes de implementar.
- Después de un cambio de código, verifícalo corriéndolo (o corriendo sus tests) siempre que se pueda.
- Si una tarea necesita una dependencia nueva, prefiere la librería estándar y pregúntame antes de agregarla.

## Estilo de escritura

En código, comentarios, README y documentación: nunca uses el guión largo `—`, usa siempre `-`.

## Código

- Código en inglés; comentarios en español.
- Mensajes de error y de log en inglés.
- Sin docstrings de triple comilla; solo comentarios de una línea con `#`.
- Nombres en `snake_case`, descriptivos y en inglés.
- Errores siempre explícitos con mensaje específico; nunca silenciar excepciones.
- Estructura pragmática: sin patrones ni capas forzadas si no hacen falta.
- Dentro de las funciones, comentarios `#` que guíen el procedimiento paso a paso.
- Salida: `print` / `console.log` en scripts sueltos; logging con niveles en apps y APIs.
- Variables de entorno en `.env`, siempre ignorado por git. No crear `.env.example`.
- Cada sección del archivo (imports, variables, clases, funciones, etc.) se separa así:

  ```
  # =============================================
  # Nombre de la sección
  # ---------------------------------------------
  ```

  El `=` solo se usa para dividir secciones; todo lo demás se separa con `-`.

### Python

- Sin type hints.
- Formato y lint con Ruff.

### Node.js

- JavaScript (no TypeScript) con módulos ESM: `import` / `export` y `"type": "module"`.

## Documentación

Al terminar cualquier tarea:

- Revisa si `README.md` y `Documentation.md` necesitan actualizarse.
- Si el cambio afecta la arquitectura, el stack, los flujos o las decisiones técnicas, actualiza `Documentation.md`.
- Si el cambio afecta la instalación, el stack usado o la descripción del proyecto, actualiza `README.md`.
- El Decision Log siempre va al final de `Documentation.md`, con la entrada más reciente arriba.

## Git

- Al terminar una tarea, propón el mensaje de commit y haz el commit solo si lo confirmo.
- Nunca hagas push sin que lo pida.

Formato de los commits:

- Título descriptivo que resuma el avance, en español salvo que pida inglés explícitamente.
- Sin prefijo de tipo: nunca `feat:`, `fix:`, `docs:` ni similares.
- Siempre con cuerpo: detalles en lista de guiones `-`, cada punto conciso.
- Sin emojis, sin punto final en el título, título de máximo 72 caracteres.
- No añadir `Co-Authored-By` salvo que lo pida explícitamente.
