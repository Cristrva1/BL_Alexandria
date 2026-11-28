# Revisar la biblioteca de Drive

Codex revisa a diario a las 08:00, hora de Ciudad de México, la carpeta de recursos configurada en la tarea **Revisar Drive y actualizar Alexandría**. El acceso y el enlace privado se conservan en Codex. Para cada incorporación se publican fuentes originales de acceso público y una primera prueba que otra persona pueda repetir.

## Cómo está organizada la biblioteca

La carpeta usa la estructura v2 desde el 28 de noviembre de 2026; la v1 se eliminó después de migrar sus 809 fichas. El contrato entre Grok Bot (guardados de X, 21:00), Muse AI (Instagram y Facebook, 23:00) y Codex (08:00) está en [`curation/drive/PROTOCOLO.md`](curation/drive/PROTOCOLO.md). En Drive se publica como `00_LEEME_PROTOCOLO.md`, en la raíz de la carpeta de la biblioteca. Las instrucciones que se pegan en cada agente están en [`curation/drive/PROMPTS_AGENTES.md`](curation/drive/PROMPTS_AGENTES.md).

- Cada ficha tiene un ID estable derivado de su URL (`X-…`, `IG-…`, `FB-…`, `MSG-…`) y un bloque `ficha` con metadatos fijos.
- Grok y Muse dejan un archivo por corrida en `90_Corridas/<agente>/AAAA-MM-DD.md`, con una fila por guardado: `nueva`, `fusion`, `pendiente_contenido`, `duplicado`, `omitida`, etc.
- La v1 (los 23 archivos sueltos) ya no existe. Las entradas `files` antiguas del registro privado apuntan a archivos borrados y no se vuelven a buscar.

## Inventario y decisiones

1. Actualiza `origin/main` y comprueba si hay una publicación incompleta antes de empezar otro lote. Usa un worktree limpio si el checkout principal contiene trabajo en curso.
2. Lista `90_Corridas/grok/` y `90_Corridas/muse/` en la raíz de la biblioteca. Procesa solo las corridas con `estado: terminada` posteriores a la última revisión registrada. Una corrida en `en_curso` espera a la mañana siguiente.
3. Descarga los archivos de subcategoría que aparecen en las filas `nueva` y `fusion`, conservando sus rutas, y valídalos:
   `uv run python scripts/validar_biblioteca_drive.py <copia_local> --corridas-desde AAAA-MM-DD --terminos-privados data/reviews/drive/terminos_privados.txt`
   - Revisa solo las fichas que el validador lista como «a revisar».
   - Las fichas con errores de formato quedan pendientes, con el aviso para su agente; no bloquean al resto.
   - Para una auditoría completa, descarga la carpeta entera y valida sin `--corridas-desde`.
4. Usa como registro local `data/reviews/drive/manifest.json` del checkout principal y comprueba con `git check-ignore` que la ruta sigue fuera de Git.
   - Por corrida, guarda la ruta, la fecha y la cobertura.
   - Por ficha, guarda su ID, la corrida de origen, la decisión y el motivo.
   - Por candidato (repo, técnica, prompt o sitio), guarda su clave normalizada.
   - Mantén el lote en borrador hasta verificar Pages.
5. Si tienes permiso de escritura en Drive, deja `90_Corridas/codex/AAAA-MM-DD.md` con los IDs publicados y los avisos de calidad para cada agente. Nunca edites fichas: las corrige su `responsable` en la corrida siguiente.
6. Compara repos por `github_id` y por `owner/repo` normalizado. Cruza ambos índices con `data/retired.json` y los lotes de `curation/altas/`. Para guías, prompts, consejos y técnicas, compara la finalidad y el ejemplo con `data/handbook.json` y `data/techniques.json`. Dos enlaces o títulos distintos pueden referirse a la misma ficha. Enriquece la ficha existente cuando la nueva fuente cambie lo que una persona necesita saber.
7. Registra hallazgos publicables en `reports/drive-AAAA-MM-DD.md` y conserva la especificación de las altas en `curation/altas/`. El historial del 22 de noviembre ya registra [la selección inicial](reports/drive-2026-11-22.md), [la revisión de seguridad](reports/drive-seguridad-2026-11-22.md) y [los sitios y servicios](reports/drive-servicios-2026-11-22.md). Los textos de Drive, sus identificadores y los enlaces privados quedan en el ámbito de trabajo.

## Revisión antes de publicar

- **Origen.** Confirma repositorio público, identidad, licencia, actividad, versión y correspondencia entre código y distribución. Lee el README y las instrucciones del paquete.
- **Uso gratuito.** Verifica que la primera prueba y una función útil se puedan hacer sin una compra obligatoria de software, API, suscripción o alojamiento. Explica equipo, cuentas y costes opcionales. Mantén pendientes las rutas con precio sin confirmar y omite las que requieren pago.
- **Seguridad.** Lee permisos, manifiestos de dependencias, origen del paquete y avisos públicos. Comprueba qué versiones afectan a la ruta elegida y si hay corrección. Difiere el proyecto ante indicios de malware, permisos desproporcionados o una distribución de origen incierto. Una búsqueda sin alertas tiene alcance limitado.
- **Funcionamiento.** Guarda una prueba corta sobre datos de ejemplo con resultado observable. Usa evidencia positiva vinculada a la versión, como CI del proyecto que ejecute sus pruebas funcionales o una prueba aislada reproducible. Identifica cuál se comprobó. Si falta evidencia o el entorno no puede aislar la ejecución de terceros, conserva el motivo y prueba otra ruta cuando haya evidencia nueva.
- **Contenido didáctico.** Redacta ejemplos y prompts propios con fuentes públicas. Separa suscripciones de Claude Code, Codex y Antigravity, claves de API y modelos locales. Distingue usar un agente para programar de usarlo para ejecutar el proyecto.

## PR, merge y publicación

1. Revisa PR abiertas, bases y ramas con trabajo sin integrar. Resuelve primero las dependencias autorizadas y retoma la PR propia de Drive si sigue pendiente.
2. Aplica cambios en las fuentes canónicas. Regenera `guide build`, `menu export` y `web build` con `uv run repo-intelligence`. Ejecuta `uv run pytest -q`, `uv run python scripts/verificar_fichas.py` y `git diff --check`.
3. Sube una rama `codex/drive-AAAA-MM-DD`, comprueba el SHA y los checks de la PR y fusiónala a `main` cuando esté lista. Respeta las protecciones de GitHub y las ramas ajenas.
4. Espera el despliegue de Pages del commit exacto. Compara de forma anónima `catalog.json` con `docs/catalog.json` y comprueba cada ficha nueva. Marca la publicación en el registro privado una vez verificada. Si el inventario no produce cambios verificados, termina sin commits vacíos.

El [detector de stars](DAILY_STARS.md) queda disponible para consultas manuales.
