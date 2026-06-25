# Estilo de Documentos Formales (.docx / Word)

> Aplica al generar un **documento formal en Word (.docx)**. No aplica a markdown,
> READMEs ni docstrings (eso lo cubre `conventions.documentation` en `config.yaml`).
> Preferencias del usuario. _"Luego matizo más cosas conforme ocupe."_

## Tipografía

- **Fuente**: Times New Roman en **todo** el documento.
- **Texto normal**: tamaño **12**.
- **Títulos principales**: tamaño **14**, pero con **formato de texto normal** (NO estilo
  "Título"/"Heading"). El usuario arma su propia tabla de contenido manualmente, así que los
  títulos NO deben llevar el etiquetado de Heading de Word — son solo texto en tamaño 14.
- **Color**: **negro** en todo el texto (sin azules, grises ni acentos de color).

## Tablas

- **Diseño/estilo de tabla**: siempre **"Tabla Normal 1"** (en python-docx: estilo `Table Grid`).
  Sin colores de relleno ni encabezados coloreados.
- **Fuente de celdas**: Times New Roman **12**.
- **Encabezados de columna**: tamaño **12 en negrita** (mismo tamaño que el cuerpo, solo bold).
- **Alto de fila**: **0.7 cm**.
- **Autoajuste**: **"Autoajustar a la ventana"**.

## Contenido

- **Idioma**: español.
- **Estilo**: detallado pero al grano, legible y claro para un programador. Sin relleno.

## Notas de implementación (para el agente)

Al generar el `.docx` (con `python-docx` o la skill `docx`):

- Fuente: `run.font.name = "Times New Roman"`; para alfabetos no latinos fijar también
  `rPr` con `w:eastAsia` si hace falta.
- Tamaños: `run.font.size = Pt(12)` para cuerpo, `Pt(14)` para títulos.
- Títulos como **párrafo normal** en `Pt(14)` (no usar `add_heading`, que aplica estilo Heading).
- Color negro explícito: `run.font.color.rgb = RGBColor(0, 0, 0)`.
- Tabla: `table.style = "Table Grid"` ("Tabla Normal 1").
- Encabezado de tabla: mismas dimensiones, `run.font.bold = True`.
- Alto de fila: `row.height = Cm(0.7)` y `row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST` (o `EXACTLY`).
- Autoajustar a la ventana: `table.autofit = True` y `table.allow_autofit = True`
  (equivale a "Autoajustar a la ventana" en Word).
