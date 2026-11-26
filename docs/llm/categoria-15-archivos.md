# Alexandría para agentes · Sincronización y gestión de archivos

Categoría 15 «Organizar notas, archivos y servicios personales» › subcategoría `archivos`. 4 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=15&sub=archivos · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `immich` | Gestión autoalojada de fotos y vídeos de alto rendimiento, alternativa a Google… | 2 Intermedio | 81 | AGPL-3.0 (OSI copyleft) | recomendado |
| `syncthing` | Aplicación para sincronizar archivos entre dispositivos directamente y… | 1 Básico | 72 | MPL-2.0 (OSI copyleft) | sin grupo |
| `photoprism` | App de fotos con IA y privacidad primero para explorar, organizar y compartir… | 2 Intermedio | 66 | AGPL-3.0 (OSI copyleft) | alternativa |
| `nextcloud-server` | Servidor de Nextcloud para almacenar y compartir archivos, contactos y… | 3 Avanzado | 59 | AGPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Immich (`immich`)

- **Repo:** https://github.com/immich-app/immich · AGPL-3.0 · nivel 2 · 81/100 · recomendado en «Gestión de fotos auto-hospedada»
- **Qué es:** Solución de gestión de fotos de código abierto (AGPL-3.0) del equipo Immich, financiado por FUTO. Uno de los proyectos autoalojados más populares; desarrollo muy activo.
- **Cuándo elegirlo:** Casos: hacer copia automática de las fotos del móvil a tu propio servidor; buscar fotos por personas, lugares o descripciones sin enviar datos a la nube.
- **Requisitos:** nivel 2: Docker Compose documentado paso a paso; app móvil lista; TypeScript, package.json; hardware model_dependent; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/immich-app/immich/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Immich con su Docker Compose oficial, sube unas fotos desde la web y busca por contenido. Éxito: Las fotos aparecen en la línea temporal y la búsqueda inteligente devuelve resultados relevantes.
- **Combina con:** `nextcloud-server`, `syncthing`, `coolify` [22/infraestructura]
- **Alternativas:** `photoprism`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): photoprism. Mantén una copia de seguridad independiente: el propio proyecto lo recomienda.

### syncthing (`syncthing`)

- **Repo:** https://github.com/syncthing/syncthing · MPL-2.0 · nivel 1 · 72/100
- **Qué es:** Programa de sincronización continua de archivos entre dispositivos, sin servidor central. Licencia MPL-2.0. Es un proyecto comunitario muy maduro (~90k estrellas, v2.1.7) que prioriza la seguridad de los datos.
- **Cuándo elegirlo:** Casos: Compartir una carpeta personal entre equipos; Mantener una colección de notas sincronizada.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Dos dispositivos compatibles; carpetas de prueba; conexión entre pares; hardware prerequisites; API de IA: no; Dos dispositivos compatibles; carpetas de prueba; conexión entre pares.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/syncthing/syncthing/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sincroniza una carpeta con un archivo ficticio y observa un cambio desde el segundo equipo Éxito: Ambos equipos muestran el mismo contenido y estado de sincronización
- **Combina con:** `home-assistant` [15/domotica], `coolify` [22/infraestructura], `paperless-ngx` [13/gestion], `audiobookshelf` [15/lectura], `spotdl` [4/social]
- **Riesgos y avisos:** Sin alternativas declaradas. Complementa Syncthing con copias de seguridad reales. Sincronización no es copia de seguridad: los cambios y borrados pueden propagarse según configuración.

### PhotoPrism (`photoprism`)

- **Repo:** https://github.com/photoprism/photoprism · AGPL-3.0 · nivel 2 · 66/100 · alternativa en «Gestión de fotos auto-hospedada»
- **Qué es:** Aplicación de fotos de código abierto (AGPL-3.0) de PhotoPrism UG, financiada con membresías que desbloquean funciones adicionales. Madura y activa.
- **Cuándo elegirlo:** Casos: organizar automáticamente un archivo de fotos por lugares, etiquetas y personas; navegar y compartir una colección familiar desde tu servidor.
- **Requisitos:** nivel 2: Docker Compose documentado; GPU opcional; Go, Dockerfile, compose.yaml, go.mod, package.json; hardware model_dependent; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/photoprism/photoprism/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega PhotoPrism con Docker Compose, indexa una carpeta de fotos y busca por etiqueta. Éxito: Las fotos aparecen clasificadas y la búsqueda por etiqueta o lugar devuelve resultados.
- **Combina con:** `nextcloud-server`, `syncthing`, `coolify` [22/infraestructura]
- **Alternativas:** `immich`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): immich.

### server (`nextcloud-server`)

- **Repo:** https://github.com/nextcloud/server · AGPL-3.0 · nivel 3 · 59/100
- **Qué es:** Servidor de Nextcloud: la plataforma autoalojada de archivos, colaboración y productividad mantenida por Nextcloud GmbH y su comunidad. Licencia AGPL-3.0-or-later, sin CLA. Es muy madura y activa (~37k estrellas, v33.0.11).
- **Cuándo elegirlo:** Casos: Alojar documentos de un equipo; Sincronizar archivos y calendarios propios.
- **Requisitos:** nivel 3: preparación pesada; Servidor compatible según guía; dominio o entorno local; almacenamiento; hardware prerequisites; API de IA: no; Servidor compatible según guía; dominio o entorno local; almacenamiento.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://nextcloud.com/install/#instructions-server
- **Primera prueba propuesta (no ejecutada):** Crea una cuenta de prueba, sube un archivo y comparte un enlace con permisos limitados Éxito: Puedes abrir el archivo con los permisos configurados
- **Combina con:** `coolify` [22/infraestructura], `home-assistant` [15/domotica], `ollama` [8/motores], `casaos` [22/infraestructura], `immich`, `photoprism`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas en el catálogo. Para producción, Nextcloud AIO simplifica mucho el mantenimiento. Su función principal es almacenamiento y colaboración, por eso pasa al área de organización de archivos; IA es una extensión opcional.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-15-archivos.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Sincronización y gestión de archivos», lee `docs/alexandria/categoria-15-archivos.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-15-archivos.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
