# Alexandría para agentes · Búsqueda, monitoreo y research web

Categoría 4 «Buscar, extraer y monitorear información web» › subcategoría `busqueda`. 10 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=4&sub=busqueda · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `last30days-skill` | Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket… | 1 Básico | 73 | MIT (OSI permisiva) | sin grupo |
| `rsshub` | Generador de feeds RSS para miles de webs y redes sin RSS propio; instancia… | 1 Básico | 73 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `changedetection` | Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más. | 1 Básico | 70 | Apache-2.0 (OSI permisiva) | sin grupo |
| `searxng` | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal… | 1 Básico | 69 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `agent-reach` | CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube… | 1 Básico | 67 | MIT (OSI permisiva) | sin grupo |
| `archivebox` | Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y… | 1 Básico | 66 | MIT (OSI permisiva) | sin grupo |
| `freshrss` | Agregador de noticias RSS autoalojado, ligero y multiusuario, con API para apps… | 1 Básico | 65 | AGPL-3.0 (OSI copyleft) | recomendado |
| `miniflux` | Lector de feeds minimalista y rápido en Go sobre PostgreSQL, con privacidad… | 1 Básico | 58 | Apache-2.0 (OSI permisiva) | alternativa |
| `wallabag` | Aplicación autoalojada para guardar páginas web y leerlas más tarde sin… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `vane` | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity… | 1 Básico | 57 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### last30days (`last30days-skill`)

- **Repo:** https://github.com/mvanhorn/last30days-skill · MIT · nivel 1 · 73/100
- **Qué es:** Skill de investigación que resume lo ocurrido en los últimos 30 días sobre un tema a partir de señales sociales (votos, likes, mercados de predicción), de @mvanhorn. Licencia MIT. Es muy popular y activa (~68k estrellas, v4.0.5).
- **Cuándo elegirlo:** Casos: Preparar una reunión sobre una empresa; Revisar novedades de una herramienta.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente compatible; dependencias de los canales; credenciales solo donde se indiquen; hardware prerequisites; API de IA: opcional; Agente compatible; dependencias de los canales; credenciales solo donde se indiquen.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/mvanhorn/last30days-skill/blob/main/README.md

  ```bash
  /plugin marketplace add mvanhorn/last30days-skill
  /plugin install last30days
  ```
- **Primera prueba propuesta (no ejecutada):** Investiga un tema concreto y exige fechas, enlaces y distinción entre opinión y evidencia Éxito: Puedes abrir las fuentes y verificar que corresponden al periodo solicitado
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `agent-reach`
- **Alternativas:** `social-media-research-skills`
- **Riesgos y avisos:** Alternativas (elige una): social-media-research-skills. Investigar a personas concretas exige cuidado con la privacidad. No todas las fuentes están activas ni disponibles sin clave; compatibilidad por Agent Skills y no por compartir proveedor LLM.

### RSSHub (`rsshub`)

- **Repo:** https://github.com/DIYgod/RSSHub · AGPL-3.0 · nivel 1 · 73/100
- **Qué es:** Red y servidor de feeds RSS de código abierto (AGPL-3.0) creado por DIYgod y mantenido por una comunidad amplia. Muy usado (más de 5.000 instancias según el proyecto) y en desarrollo continuo.
- **Cuándo elegirlo:** Casos: seguir canales, perfiles o webs sin RSS desde tu lector de feeds; alimentar un flujo de monitorización de fuentes con feeds uniformes.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, Dockerfile, docker-compose.yml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d --name rsshub -p 1200:1200 diygod/rsshub` — fuente: https://docs.rsshub.app/deploy/
- **Primera prueba propuesta (no ejecutada):** Despliega RSSHub con Docker según su documentación y abre una ruta de ejemplo en el navegador. Éxito: La ruta devuelve un feed RSS válido que tu lector puede suscribir.
- **Combina con:** `freshrss`, `miniflux`, `activepieces` [1/motores], `coolify` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. La instancia pública puede limitar peticiones; para uso intensivo conviene autoalojarla.

### changedetection.io (`changedetection`)

- **Repo:** https://github.com/dgtlmoon/changedetection.io · Apache-2.0 · nivel 1 · 70/100
- **Qué es:** Monitor autoalojado de cambios en páginas web (changedetection.io), de @dgtlmoon. Licencia Apache-2.0. Es maduro y activo (~36k estrellas, 0.70.3) y tiene versión alojada de pago.
- **Cuándo elegirlo:** Casos: Detectar cambios de precio permitidos; Monitorear avisos de una página.
- **Requisitos:** nivel 1: preparación sencilla; Docker; URL a vigilar; canal de aviso opcional; hardware prerequisites; API de IA: opcional; Docker; URL a vigilar; canal de aviso opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/dgtlmoon/changedetection.io/blob/master/README.md

  ```bash
  docker run -d --restart always -p "127.0.0.1:5000:5000" -v datastore-volume:/datastore --name changedetection.io docker.io/dgtlmoon/changedetection.io
  ```
- **Primera prueba propuesta (no ejecutada):** Vigila un texto en una página propia y modifícalo una vez para revisar la diferencia Éxito: El historial identifica el cambio concreto
- **Combina con:** `ollama` [8/motores], `claude-code` [20/terminal], `activepieces` [1/motores], `archivebox`, `cloud-mail` [18/marketing], `huginn` [1/motores]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Respeta los términos de uso de cada plataforma y la privacidad de las personas. MCP requiere versión que lo incluya; su acceso al historial no acredita que el agente haya observado cambios futuros.

### SearXNG (`searxng`)

- **Repo:** https://github.com/searxng/searxng · AGPL-3.0 · nivel 1 · 69/100
- **Qué es:** Metabuscador libre que agrega resultados de muchos motores sin rastrear ni perfilar al usuario. Licencia AGPL-3.0-or-later. Es un proyecto comunitario maduro y activo (~40k estrellas; publica desde la rama principal, sin releases en…
- **Cuándo elegirlo:** Casos: Añadir búsqueda a una herramienta de investigación; Disponer de un metabuscador propio.
- **Requisitos:** nivel 1: preparación sencilla; Servidor o Docker; configuración de motores de búsqueda; hardware prerequisites; API de IA: no; Servidor o Docker; configuración de motores de búsqueda.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.searxng.org/admin/installation.html
- **Primera prueba propuesta (no ejecutada):** Realiza una búsqueda y compara las fuentes de dos resultados Éxito: Ves resultados agregados y puedes abrir su origen
- **Combina con:** `gpt-researcher` [21/research], `open-webui` [8/chats], `vane`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. No expongas tu instancia sin limitación de peticiones. La privacidad del metabuscador no vuelve locales las consultas enviadas a motores externos.

### Agent-Reach (`agent-reach`)

- **Repo:** https://github.com/Panniantong/Agent-Reach · MIT · nivel 1 · 67/100
- **Qué es:** Herramienta para que agentes de IA de línea de comandos busquen y lean plataformas a las que no llegan solos (X, Reddit, YouTube, Xiaohongshu y otras), de @Panniantong. Licencia MIT.
- **Cuándo elegirlo:** Casos: Leer una discusión pública para investigación; Obtener transcripciones de un video permitido.
- **Requisitos:** nivel 1: preparación sencilla; Agente con terminal; uv; sesiones de sitios solo cuando corresponda; hardware prerequisites; API de IA: opcional; Agente con terminal; uv; sesiones de sitios solo cuando corresponda.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install https://github.com/Panniantong/Agent-Reach/releases/latest/download/agent-reach.zip` — fuente: https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md
- **Primera prueba propuesta (no ejecutada):** Lista los canales y lee un README público de GitHub antes de añadir canales opcionales Éxito: Puedes distinguir canales disponibles, autenticados y experimentales
- **Combina con:** `claude-code` [20/terminal], `openclaw` [21/asistentes], `last30days-skill`
- **Riesgos y avisos:** Sin alternativas declaradas. Instala solo desde GitHub (hay un paquete homónimo en PyPI que no es este). El paquete homónimo de PyPI no es este proyecto; usa la dirección GitHub del instalador oficial.

### ArchiveBox (`archivebox`)

- **Repo:** https://github.com/ArchiveBox/ArchiveBox · MIT · nivel 1 · 66/100
- **Qué es:** Aplicación autoalojada para archivar sitios web en varios formatos. Licencia MIT. Es madura y activa (~29k estrellas, v0.9.77).
- **Cuándo elegirlo:** Casos: Preservar documentación que cambia; Crear una biblioteca de fuentes de una investigación.
- **Requisitos:** nivel 1: preparación sencilla; Docker o dependencias nativas; directorio persistente; espacio en disco; hardware prerequisites; API de IA: no; Docker o dependencias nativas; directorio persistente; espacio en disco.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install archivebox` — fuente: https://github.com/ArchiveBox/ArchiveBox/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Archiva una página propia y abre las copias HTML y captura desde el panel Éxito: La captura conserva la URL y se puede consultar después
- **Combina con:** `yt-dlp` [4/social], `changedetection`, `karakeep` [15/notas], `instaloader` [4/social]
- **Riesgos y avisos:** Sin alternativas declaradas. Desactiva el envío a archive.org si archivas páginas privadas. El README menciona herramientas MCP pero falta confirmar aquí su configuración por cliente; los archivos no garantizan capturar toda web dinámica.

### FreshRSS (`freshrss`)

- **Repo:** https://github.com/FreshRSS/FreshRSS · AGPL-3.0 · nivel 1 · 65/100 · recomendado en «Lectores RSS auto-hospedados»
- **Qué es:** Agregador RSS autoalojado de código abierto (AGPL-3.0) mantenido por la comunidad FreshRSS. Proyecto maduro y traducido a más de 20 idiomas.
- **Cuándo elegirlo:** Casos: centralizar en tu servidor los feeds de noticias y blogs que sigues; seguir webs sin RSS con reglas de extracción XPath.
- **Requisitos:** nivel 1: preparación sencilla; PHP, composer.json, package.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/FreshRSS/FreshRSS/blob/edge/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega FreshRSS con Docker, importa un archivo OPML pequeño y actualiza los feeds. Éxito: Los artículos aparecen en la interfaz y un cliente móvil compatible puede sincronizarlos.
- **Combina con:** `rsshub`, `wallabag`, `coolify` [22/infraestructura]
- **Alternativas:** `miniflux`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): miniflux.

### Miniflux (`miniflux`)

- **Repo:** https://github.com/miniflux/v2 · Apache-2.0 · nivel 1 · 58/100 · alternativa en «Lectores RSS auto-hospedados»
- **Qué es:** Lector de feeds de código abierto (Apache-2.0) creado por Frédéric Guillot. Proyecto maduro, deliberadamente minimalista y «opinionated».
- **Cuándo elegirlo:** Casos: leer feeds sin rastreadores en una instancia propia ligera; enviar artículos automáticamente a un servicio de lectura o notas.
- **Requisitos:** nivel 1: preparación sencilla; Go, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/miniflux/v2/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Miniflux con PostgreSQL según la guía, importa un OPML y lee un artículo. Éxito: Los feeds se actualizan, la búsqueda devuelve resultados y no aparecen píxeles de seguimiento.
- **Combina con:** `rsshub`, `wallabag`, `coolify` [22/infraestructura]
- **Alternativas:** `freshrss`
- **Riesgos y avisos:** Alternativas (elige una): freshrss.

### wallabag (`wallabag`)

- **Repo:** https://github.com/wallabag/wallabag · MIT · nivel 2 · 58/100
- **Qué es:** Aplicación «leer más tarde» de código abierto (MIT) mantenida por la comunidad wallabag desde 2013. Madura, con apps oficiales para Android e iOS y servicio alojado (wallabag.it) aparte.
- **Cuándo elegirlo:** Casos: guardar artículos para leerlos sin conexión en el móvil; archivar lecturas con etiquetas y anotaciones en tu propio servidor.
- **Requisitos:** nivel 2: preparación media; PHP, compose.yaml, composer.json, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/wallabag/wallabag.git` — fuente: https://github.com/wallabag/wallabag/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala wallabag con Docker o según su documentación y guarda un artículo desde la extensión del navegador. Éxito: El artículo aparece limpio en la lista de lectura y se puede exportar.
- **Combina con:** `freshrss`, `miniflux`, `coolify` [22/infraestructura]
- **Riesgos y avisos:** Alternativa cercana en el catálogo: karakeep (marcadores con IA).

### Vane (`vane`)

- **Repo:** https://github.com/ItzCrazyKns/Vane · MIT · nivel 1 · 57/100
- **Qué es:** Motor de respuestas con IA centrado en la privacidad que se ejecuta en tu propio equipo, de @ItzCrazyKns. Licencia MIT. Es popular (~38k estrellas, v1.12.2) y su último cambio es de septiembre de 2026.
- **Cuándo elegirlo:** Casos: Investigar un tema con citas; Consultar la web usando Ollama.
- **Requisitos:** nivel 1: preparación sencilla; Docker; modelo local accesible o clave de proveedor; hardware prerequisites; API de IA: depends; Docker; modelo local accesible o clave de proveedor.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest` — fuente: https://github.com/ItzCrazyKns/Vane/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Busca una pregunta de actualidad sencilla y abre las referencias antes de aceptar el resumen Éxito: La respuesta muestra enlaces que apoyan sus afirmaciones
- **Combina con:** `searxng`, `ollama` [8/motores], `markitdown` [13/conversion]
- **Alternativas:** `gpt-researcher`
- **Riesgos y avisos:** Alternativas (elige una): gpt-researcher. Antes llamado Perplexica; búsqueda web privada no significa que los sitios externos no reciban consultas.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-4-busqueda.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Búsqueda, monitoreo y research web», lee `docs/alexandria/categoria-4-busqueda.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-4-busqueda.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
