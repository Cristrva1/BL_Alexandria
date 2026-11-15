# Alexandría: orientación para personas que empiezan

Fecha editorial: 2026-11-14. Catálogo base: 498 proyectos públicos y tres entradas auxiliares. La carpeta histórica de clones fue eliminada por el usuario; esta actualización utiliza fuentes de GitHub sin recrearla.

## Qué cambia para el lector

- Entrada «Guíame»: dos preguntas, hasta tres opciones y un primer paso. Las selecciones se limitan a herramientas pertinentes para la tarea y al acceso solicitado.
- 18 objetivos y 14 categorías con descripciones por función. Transcribir y sintetizar voz tienen rutas distintas; también presentaciones y diagramas. Finanzas tiene su propia categoría.
- Búsqueda de tareas en español, acentos y sinónimos; filtros de objetivo, acceso, tema, sección, preparación y estado; resultados paginados.
- Fichas con función, API de IA, Claude Code, Codex, modelos locales, coste, hardware, instrucciones y procedencia. El detalle técnico se amplía cuando se necesita.
- Diccionario breve, guías de elección, acceso e instalación y un encargo por ficha para pedir ayuda paso a paso al asistente.
- Diez aplicaciones tienen una entrada a su web o descarga enlazada por el README; 121 fichas incluyen un comando de entrada seleccionado y encontrado en la fuente.
- Comparación de hasta tres herramientas y corrección del selector que impedía añadir una segunda opción.
- Las novedades se ordenan por primera aparición en Git, no por ausencia de un clon local. Las estrellas son un criterio opcional de popularidad.

## Acceso y fuentes

Los 498 README se consultaron y se almacenaron para revisión local, junto con URL, fecha y SHA del archivo. Las etiquetas editoriales distinguen ausencia de una API de IA en una ruta concreta de servicios externos, licencia, hardware o alojamiento. No se deduce el acceso al modelo por el lugar donde se instala la interfaz.

| API de IA | Proyectos |
|---|---:|
| Sin API en la ruta básica | 330 |
| Opcional | 46 |
| Depende de la ruta | 110 |
| Necesaria en la ruta documentada | 10 |
| Por confirmar | 2 |

`muse-spark` y `codex-chatgpt-web` conservan autenticación y costes por confirmar. Una integración descrita por un tercero se presenta como tal; no equivale a acceso oficial del proveedor.

Las guías de suscripción enlazan documentación oficial de OpenAI y Anthropic. Explican por separado sesión del agente, clave de API y posibles créditos del plan. No publican precios estimados ni prometen uso ilimitado.

## Estructura y mantenimiento

Los índices canónicos alimentan las fichas, categorías, comparativas, catálogo, menú portable y los dos exploradores. `docs/` y `web/` utilizan ahora la misma interfaz y los mismos datos. El ZIP permite abrir `docs/index.html` sin Python ni servidor.

`scripts/audit_sources.py` consulta documentación sin instalar los proyectos y conserva el informe completo cuando se revisa un solo id. Los scripts de curaduría son migraciones editoriales fechadas, no clasificadores que puedan confirmar requisitos mediante keywords. El mantenimiento explica cómo revisar nueva evidencia y regenerar todas las salidas.

## Verificación

- 58 pruebas automatizadas aprobadas: generación, referencias, taxonomía, acceso, instalación sin paquetes inventados, búsqueda real en JavaScript y recomendador.
- Comprobación de sintaxis de `app.js` y `search.js`; `git diff --check` sin errores.
- Reconstrucción repetida de 640 archivos sin diferencias; igualdad de HTML, JavaScript, CSS y catálogo entre ambos exploradores.
- Revisión visual en navegador a 1365 × 900 y 390 × 844: portada, búsqueda, filtros, fichas, encargo copiable, selección guiada y comparación. Sin errores de consola observados ni desbordamiento horizontal de la página; la tabla comparativa se desplaza dentro de su región.
- Caso comprobado: «crear una presentación desde documentos usando Codex» devuelve `ppt-master` sin añadir skills de otra función. La combinación de transcripción y sesión de Codex no inventa soporte: explica que no hay ruta documentada en esa selección.
- Detector visual ejecutado. Se retiraron los acentos gruesos de tarjetas; se conserva la identidad de papel y tinta que ya tenía el sitio.

La verificación es documental y del funcionamiento de la biblioteca. No se instalaron ni ejecutaron los 498 proyectos; un comando documentado no acredita una instalación completa o probada.
