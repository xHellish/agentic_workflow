## Backlog de Mejoras Pendientes

> Para registrar nuevas mejoras futuras, añadirlas aquí siguiendo el formato anterior.

- ✅ **[Completada] Integración de un Framework de Testing**: Se integró `pytest` y se creó `.agents/tests/test_validate_skills.py` para verificar la funcionalidad principal del script `validate_skills.py`.

- ✅ **[Completada] Automatización de Calidad (CI/CD)**: Se creó un flujo de trabajo para GitHub Actions en `.github/workflows/verify-skills.yml` que corre validaciones, ejecuta las pruebas con `pytest` y realiza el linting los archivos `.md`.

- ✅ **[Completada] Backlog Automatizado**: Se creó el script `.agents/scripts/create_skill.py` para generar nuevas skills a partir de la plantilla y registrarlas de forma automática en el `manifest.json`. Para usarlo, ejecutar: `python .agents/scripts/create_skill.py <nombre-skill> "<descripción>"`.
