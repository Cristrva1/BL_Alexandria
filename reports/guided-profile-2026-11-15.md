# Guíame: perfil y primeros pasos — 15 de noviembre de 2026

El usuario pidió recomendaciones según proyecto, experiencia, equipo y acceso a IA, y eligió responder todo en una pantalla. El formulario reúne esos cuatro bloques, permite marcar varios agentes y deja sistema, RAM y GPU por confirmar cuando la persona no los conoce.

## Selección y límites

- La descripción se compara localmente con los 22 objetivos del catálogo. El objetivo interpretado se muestra y puede corregirse. Ante una descripción desconocida o ambigua se pide elegir el resultado; no se completa la lista con herramientas arbitrarias.
- Los candidatos salen de los puntos de partida curados de cada objetivo. Se ordenan según experiencia, preparación, función y acceso documentado, con un máximo de tres proyectos distintos. Una preferencia por IA local no sustituye un objetivo concreto, como generar imágenes.
- Claude Code, Codex y Antigravity admiten selección múltiple. Un chat web no acredita una integración con esos agentes. La ruta «Solo integraciones con mis agentes» exige un cliente marcado y una integración documentada; una referencia a un proveedor no basta. Las APIs obligatorias no se presentan como incluidas en una suscripción.
- «Solo navegador o tableta» exige una aplicación web oficial verificada o una referencia de lectura. Una etiqueta cloud no demuestra que exista una interfaz. Se añadieron rutas web con fuente y fecha para Excalidraw, tldraw y Penpot.
- Las instrucciones de tldraw distinguen su pizarra web de la integración del SDK: la prueba desde el navegador propone dibujar cajas y flechas, sin crear un proyecto de código.
- RAM y GPU permiten evitar puntos de partida pesados para principiantes con recursos limitados; no acreditan que un modelo quepa. Se añadió el mínimo documental de 32 GB de RAM para la ruta CPU de Fooocus, separado de Apple Silicon/MPS. Un Windows con hasta 8 GB y sin GPU no recibe esa recomendación local. [Tabla original de Fooocus](https://github.com/lllyasviel/Fooocus/blob/main/readme.md#minimal-requirement).
- Las recomendaciones muestran motivos, requisitos, tres pasos, una prueba pequeña, resultado observable, costes y ficha con fuentes. Se puede comparar sus funciones o copiar un encargo personalizado para otro asistente.

La selección usa reglas del catálogo, no un modelo de lenguaje ni una prueba automática de compatibilidad. No se instalaron ni ejecutaron los proyectos recomendados. Las rutas alojadas conservan una advertencia sobre sus propias cuentas, límites y planes.

## Privacidad y comportamiento

Las respuestas permanecen en memoria de la pestaña. No se añaden a la URL, almacenamiento persistente ni peticiones de IA. Recargar o «Borrar respuestas» las elimina. Navegar entre fichas conserva el borrador durante esa sesión; editar una respuesta oculta los resultados anteriores hasta volver a solicitar recomendaciones.

Los controles tienen etiquetas y agrupación semántica, validación nativa y foco al resultado o al campo que requiere atención. Ninguna selección envía el formulario automáticamente. La vista móvil conserva el mismo orden de lectura y apila los grupos.

## Verificación

Las pruebas automatizadas cubren detección y corrección del objetivo, ambigüedad, cambios de orden por experiencia, límites de preparación, requisitos CPU documentados, selección múltiple de agentes, suscripción frente a API, rutas web y sus fuentes, tres pasos y carga versionada del módulo.

La suite completa terminó con **94 pruebas aprobadas** (`uv run pytest -q`).

La revisión del navegador comprobó una presentación desde PDF con Codex, diagramas sin instalación, generación local con recursos insuficientes, objetivo desconocido, validación de espacios, edición sin resultados obsoletos, navegación de ida y vuelta, copia del encargo y borrado al recargar. En un viewport de 390 × 844 no hubo desbordamiento horizontal y los controles medidos tuvieron al menos 48 px de alto. La consola no registró errores ni advertencias durante estas pruebas.

El detector de Impeccable señaló el fondo crema ya presente en la identidad de la biblioteca. Se conservó esa paleta para mantener coherencia con el producto existente; no se añadió un nuevo sistema visual.

Las salidas de `docs/`, `web/` y el menú portable se regeneraron desde las fuentes canónicas. La publicación debe verificarse contra los mismos archivos después del despliegue de Pages.
