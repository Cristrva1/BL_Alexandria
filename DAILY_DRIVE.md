# Revisar la biblioteca de Drive

Codex revisa a diario a las 08:00, hora de Ciudad de México, la carpeta de recursos configurada en la tarea **Revisar Drive y actualizar Alexandría**. El acceso y el enlace privado se conservan en Codex. Para cada incorporación se publican fuentes originales de acceso público y una primera prueba que otra persona pueda repetir.

## Inventario y decisiones

1. Actualiza `origin/main` y comprueba si hay una publicación incompleta antes de empezar otro lote. Usa un worktree limpio si el checkout principal contiene trabajo en curso.
2. Lista la carpeta y sus subcarpetas por páginas. Cruza la revisión de cada archivo con el inventario anterior. Lee los nuevos o modificados y continúa los candidatos cuyo estado sea pendiente. Si solo recuperaste un fragmento, conserva esa revisión como incompleta.
3. Usa como registro local `data/reviews/drive/manifest.json` del checkout principal. Comprueba con `git check-ignore` que la ruta sigue fuera de Git. Conserva por archivo su identificador, fecha de modificación, fecha de lectura y cobertura. Conserva por candidato su clave normalizada, revisiones de origen, decisión y motivo. Un archivo leído puede contener decisiones pendientes. Mantén el lote en borrador hasta verificar Pages.
4. Compara repos por `github_id` y por `owner/repo` normalizado. Cruza ambos índices con `data/retired.json` y los lotes de `curation/altas/`. Para guías, prompts, consejos y técnicas, compara la finalidad y el ejemplo con `data/handbook.json` y `data/techniques.json`. Dos enlaces o títulos distintos pueden referirse a la misma ficha. Enriquece la ficha existente cuando la nueva fuente cambie lo que una persona necesita saber.
5. Registra hallazgos publicables en `reports/drive-AAAA-MM-DD.md` y conserva la especificación de las altas en `curation/altas/`. El historial del 22 de noviembre ya registra [la selección inicial](reports/drive-2026-11-22.md), [la revisión de seguridad](reports/drive-seguridad-2026-11-22.md) y [los sitios y servicios](reports/drive-servicios-2026-11-22.md). Los textos de Drive, sus identificadores y los enlaces privados quedan en el ámbito de trabajo.

## Revisión antes de publicar

- **Origen.** Confirma repositorio público, identidad, licencia, actividad, versión y correspondencia entre código y distribución. Lee el README y las instrucciones del paquete.
- **Uso gratuito.** Verifica que la primera prueba y una función útil se puedan hacer sin una compra obligatoria de software, API, suscripción o alojamiento. Explica equipo, cuentas y costes opcionales. Mantén pendientes las rutas con precio sin confirmar y omite las que requieren pago.
- **Seguridad.** Lee permisos, manifiestos de dependencias, origen del paquete y avisos públicos. Comprueba qué versiones afectan a la ruta elegida y si hay corrección. Difiere el proyecto ante indicios de malware, permisos desproporcionados o una distribución de origen incierto. Una búsqueda sin alertas tiene alcance limitado.
- **Funcionamiento.** Guarda una prueba corta sobre datos de ejemplo con resultado observable. Usa evidencia positiva vinculada a la versión, como CI del proyecto que ejecute sus pruebas funcionales o una prueba aislada reproducible. Identifica cuál se comprobó. Si falta evidencia o el entorno no puede aislar la ejecución de terceros, conserva el motivo y prueba otra ruta cuando haya evidencia nueva.
- **Contenido didáctico.** Redacta ejemplos y prompts propios con fuentes públicas. Separa suscripciones de Claude Code, Codex y Antigravity, claves de API y modelos locales. Distingue usar un agente para programar de usarlo para ejecutar el proyecto.

## PR, merge y publicación

1. Revisa PR abiertas, bases y ramas con trabajo sin integrar. Resuelve primero las dependencias autorizadas y retoma la PR propia de Drive si sigue pendiente.
2. Aplica cambios en las fuentes canónicas. Regenera `guide build`, `menu export` y `web build` con `uv run repo-intelligence`. Ejecuta `uv run pytest -q` y `git diff --check`.
3. Sube una rama `codex/drive-AAAA-MM-DD`, comprueba el SHA y los checks de la PR y fusiónala a `main` cuando esté lista. Respeta las protecciones de GitHub y las ramas ajenas.
4. Espera el despliegue de Pages del commit exacto. Compara de forma anónima `catalog.json` con `docs/catalog.json` y comprueba cada ficha nueva. Marca la publicación en el registro privado una vez verificada. Si el inventario no produce cambios verificados, termina sin commits vacíos.

El [detector de stars](DAILY_STARS.md) queda disponible para consultas manuales.
