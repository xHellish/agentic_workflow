# Preferencias personales

Reglas que aplican en todos mis proyectos.

## Idioma

Responde siempre en español.

## Forma de trabajar

- Ante una tarea grande o ambigua, entrevístame sobre el "cómo" antes de implementar.
- Después de un cambio de código, verifícalo corriéndolo (o corriendo sus tests) siempre que se pueda.
- Nunca agregues dependencias ni herramientas (librerías, formateadores, linters) sin preguntarme; prefiere la librería estándar.

## Estilo de escritura

En código, comentarios, README y documentación: nunca uses el guión largo `—`, usa siempre `-`.

## Código

- Código en inglés; comentarios en español.
- Toda la salida del programa en inglés: prints, logs y mensajes de error.
- Sin docstrings de triple comilla; solo comentarios de una línea con `#`.
- Nombres descriptivos y en inglés: `snake_case` para variables y funciones; constantes en mayúsculas (`UPPER_SNAKE_CASE`, ej. `VALID_STATUSES`).
- Errores siempre explícitos con mensaje específico; nunca silenciar excepciones.
- Estructura pragmática: sin patrones ni capas forzadas si no hacen falta.
- Justo encima de cada función, un comentario `#` de una línea que diga en corto qué hace.
- Dentro de las funciones, comentarios `#` que guíen el procedimiento paso a paso.
- Ciclos y condicionales siempre en bloque, nunca en una sola línea: sin comprehensions (`[x for x in lista]`) ni ternarios (`a if cond else b`). `enumerate` y `.items()` sí se usan.
- Para saber si una lista está vacía, comparación explícita con `len()`: `if len(tasks) == 0:` o `if len(tasks) > 0:`, en lugar de `if not tasks:` o `if tasks:`.
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
- Formato y lint con Ruff: tras editar Python, corre `ruff format` y `ruff check` sobre los archivos que tocaste antes de dar el cambio por terminado.
- El logger del módulo va en minúscula (`logger = logging.getLogger(...)`); no cuenta como constante.

### Node.js

- JavaScript (no TypeScript) con módulos ESM: `import` / `export` y `"type": "module"`.
- Lo mismo en JavaScript: ciclos en bloque (`for (const item of lista)`) en lugar de `map` / `filter` en una línea, y sin ternarios `a ? b : c`.
- Comentarios con `//` y el mismo formato de secciones (`// ===`, nombre, `// ---`); sin bloques `/** */`.
- `snake_case` también en JavaScript; las APIs de Node y de librerías conservan su nombre (`readFile`).
- Sangría de 2 espacios. Sin formateador para JS por ahora.

## Documentación

Al terminar cualquier tarea en un proyecto:

- Revisa si `README.md` y `Documentation.md` necesitan actualizarse.
- Si el cambio afecta la arquitectura, el stack, los flujos o las decisiones técnicas, actualiza `Documentation.md`.
- Si el cambio afecta la instalación, el stack usado o la descripción del proyecto, actualiza `README.md`.
- El Decision Log siempre va al final de `Documentation.md`, con la entrada más reciente arriba.

Solo aplica a proyectos (carpetas con su propio repo de git o una aplicación). En scripts sueltos o carpetas de prueba no crees `README.md` ni `Documentation.md` salvo que lo pida.

## Git

- Al terminar una tarea, propón el mensaje de commit y haz el commit solo si lo confirmo.
- Nunca hagas push sin que lo pida.

Formato de los commits:

- Título descriptivo que resuma el avance, en español salvo que pida inglés explícitamente.
- Sin prefijo de tipo: nunca `feat:`, `fix:`, `docs:` ni similares.
- Siempre con cuerpo: detalles en lista de guiones `-`, cada punto conciso.
- Sin emojis, sin punto final en el título, título de máximo 72 caracteres.
- No añadir `Co-Authored-By` salvo que lo pida explícitamente.
