# Alexandría para agentes · Notas, bóvedas y conocimiento personal

Categoría 15 «Organizar notas, archivos y servicios personales» › subcategoría `notas`. 19 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=15&sub=notas · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `memos` | App de notas rápidas autoalojada con línea temporal personal, Markdown… | 1 Básico | 82 | MIT (OSI permisiva) | sin grupo |
| `siyuan` | Espacio de conocimiento por bloques, local-first y autoalojable, con… | 1 Básico | 79 | AGPL-3.0 (OSI copyleft) | recomendado |
| `karakeep` | Gestor autoalojado de marcadores, notas e imágenes con búsqueda y funciones… | 2 Intermedio | 69 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `trilium` | App de notas jerárquicas para bases de conocimiento grandes: clonado de notas… | 1 Básico | 65 | AGPL-3.0 (OSI copyleft) | alternativa |
| `appflowy` | Espacio de trabajo para notas, wikis y proyectos colaborativos, con funciones… | 1 Básico | 64 | AGPL-3.0 (OSI copyleft) | recomendado |
| `obsidian-skills` | Skills para que un agente trabaje con Obsidian y sus formatos de notas, bases… | 2 Intermedio | 63 | MIT (OSI permisiva) | sin grupo |
| `obsidian-second-brain` | Sistema de memoria y notas en Markdown para compartir contexto de trabajo entre… | 2 Intermedio | 62 | MIT (OSI permisiva) | recomendado |
| `claude-obsidian` | Instrucciones para que Claude Code clasifique, enlace y consulte fuentes dentro… | 2 Intermedio | 60 | MIT (OSI permisiva) | alternativa |
| `obsidian-releases` | Repositorio de distribución de Obsidian y sus listados de plugins y temas; no… | 1 Básico | 60 | — (sin licencia detectada) | sin grupo |
| `logseq` | Plataforma de gestión del conocimiento local-first en forma de esquema, con… | 1 Básico | 59 | AGPL-3.0 (OSI copyleft) | alternativa |
| `joplin` | App de notas y tareas centrada en la privacidad, offline first, con… | 1 Básico | 58 | AGPL-3.0 (OSI copyleft) | alternativa |
| `obsidian-importer` | Plugin oficial para convertir datos de otras aplicaciones en archivos Markdown… | 1 Básico | 58 | MIT (OSI permisiva) | sin grupo |
| `obsidian-clipper` | Extensión oficial para capturar páginas y fragmentos de la web y guardarlos… | 1 Básico | 57 | MIT (OSI permisiva) | sin grupo |
| `kepano-obsidian` | Plantilla de una bóveda de Obsidian para estudiar una forma de organizar notas… | 2 Intermedio | 52 | MIT (OSI permisiva) | sin grupo |
| `jsoncanvas` | Especificación abierta de JSON Canvas para describir nodos y conexiones de un… | 1 Básico | 50 | MIT (OSI permisiva) | sin grupo |
| `obsidian-sample-plugin` | Plantilla oficial para programar un plugin de Obsidian con una estructura… | 2 Intermedio | 50 | 0BSD (OSI permisiva) | sin grupo |
| `anytype-ts` | Cliente de escritorio de Anytype para organizar notas, objetos y relaciones en… | 1 Básico | 48 | Any Source Available License 1.0 (no OSI) (source-available) | alternativa |
| `obsidian-minimal` | Tema configurable de Obsidian para ajustar la apariencia y reducir… | 1 Básico | 48 | MIT (OSI permisiva) | sin grupo |
| `obsidian-help` | Documentación oficial de Obsidian para aprender sus funciones, configuración y… | 1 Básico | 43 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Memos (`memos`)

- **Repo:** https://github.com/usememos/memos · MIT · nivel 1 · 82/100
- **Qué es:** Aplicación de notas de código abierto (MIT) del proyecto usememos. Muy popular y activa; versiones con formato YY.MM.N.
- **Cuándo elegirlo:** Casos: registrar ideas y notas breves del día en tu propio servidor; conectar tus notas con scripts o agentes mediante su API o MCP.
- **Requisitos:** nivel 1: preparación sencilla; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d --name memos -p 5230:5230 -v ~/.memos:/var/opt/memos neosmemo/memos:stable` — fuente: https://github.com/usememos/memos/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca Memos con el `docker run` del README, crea una nota con etiquetas y búscala. Éxito: La nota aparece en la línea temporal y la búsqueda por etiqueta la encuentra.
- **Combina con:** `claude-code` [20/terminal], `activepieces` [1/motores], `coolify` [22/infraestructura]
- **Riesgos y avisos:** Alternativas cercanas en el catálogo: karakeep, obsidian (otros modelos de notas).

### SiYuan (`siyuan`)

- **Repo:** https://github.com/siyuan-note/siyuan · AGPL-3.0 · nivel 1 · 79/100 · recomendado en «Notas y bases de conocimiento personales»
- **Qué es:** Gestor de conocimiento de código abierto (AGPL-3.0) de B3log. Muy activo; algunas funciones de sincronización en la nube requieren suscripción.
- **Cuándo elegirlo:** Casos: construir una base de conocimiento personal con referencias entre bloques; autoalojar un espacio de notas accesible desde el navegador.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, Dockerfile; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/siyuan-note/siyuan/blob/master/README.md

  ```bash
  docker run -d -v workspace_dir_host:workspace_dir_container -p 6806:6806 -e PUID=1001 -e PGID=1002 b3log/siyuan serve --workspace=workspace_dir_container --accessAuthCode="${AuthCode:?Set AuthCode}"
  ```
- **Primera prueba propuesta (no ejecutada):** Instala la app de escritorio o la imagen Docker (`b3log/siyuan serve`), crea dos documentos y enlaza un bloque de uno en el otro. Éxito: La referencia bidireccional aparece en ambos documentos.
- **Combina con:** `ollama` [8/motores], `nextcloud-server` [15/archivos], `claude-code` [20/terminal]
- **Alternativas:** `trilium`, `logseq`, `joplin`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): joplin, trilium, logseq.

### karakeep (`karakeep`)

- **Repo:** https://github.com/karakeep-app/karakeep · AGPL-3.0 · nivel 2 · 69/100
- **Qué es:** Gestor de marcadores autoalojado «guárdalo todo» (antes Hoarder) con etiquetado por IA, de Localhost Labs Ltd. Licencia AGPL-3.0. Es activo y popular (~31k estrellas, v0.35.0).
- **Cuándo elegirlo:** Casos: Organizar una biblioteca de enlaces; Clasificar artículos con un modelo local.
- **Requisitos:** nivel 2: Docker Compose documentado; Docker; volumen persistente; modelo solo para etiquetado AI; hardware prerequisites; API de IA: opcional; Docker; volumen persistente; modelo solo para etiquetado AI.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://docs.karakeep.com/Installation/docker
- **Primera prueba propuesta (no ejecutada):** Guarda dos enlaces de prueba y comprueba búsqueda y etiquetas antes de activar resúmenes AI Éxito: Puedes abrir origen, nota y etiquetas de cada marcador
- **Combina con:** `ollama` [8/motores], `coolify` [22/infraestructura], `claude-code` [20/terminal], `archivebox` [4/busqueda]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas en el catálogo. Antes llamado Hoarder; parte de la documentación antigua usa ese nombre. Antes Hoarder; el modo de lectura offline no significa que un proveedor AI remoto procese localmente los artículos.

### Trilium Notes (`trilium`)

- **Repo:** https://github.com/TriliumNext/Trilium · AGPL-3.0 · nivel 1 · 65/100 · alternativa en «Notas y bases de conocimiento personales»
- **Qué es:** Aplicación de notas de código abierto (AGPL-3.0) mantenida por la comunidad TriliumNext, continuación del Trilium original de zadam. Muy activa, con versiones estables y nightly.
- **Cuándo elegirlo:** Casos: construir una base de conocimiento personal grande con jerarquías y atributos; sincronizar notas entre escritorio y navegador con tu propio servidor.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, docker-compose.yml, package.json; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/TriliumNext/Trilium.git` — fuente: https://github.com/TriliumNext/Trilium/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala la release de escritorio o el servidor Docker, crea un árbol de notas y clona una nota en dos ramas. Éxito: La nota clonada aparece en ambas ramas y los cambios se reflejan en las dos.
- **Combina con:** `coolify` [22/infraestructura], `claude-code` [20/terminal], `pandoc` [13/conversion]
- **Alternativas:** `siyuan`, `logseq`, `joplin`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): joplin, siyuan, logseq.

### AppFlowy (`appflowy`)

- **Repo:** https://github.com/AppFlowy-IO/AppFlowy · AGPL-3.0 · nivel 1 · 64/100 · recomendado en «Espacios de trabajo local-first tipo Notion»
- **Qué es:** Espacio de trabajo con IA, open source y alternativa a Notion, de AppFlowy. Licencia AGPL-3.0. Es maduro y popular (~79k estrellas, 0.15.1) y sigue versionado como 0.x.
- **Cuándo elegirlo:** Casos: Organizar un proyecto colaborativo; Construir una wiki de equipo.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador o despliegue elegido; proveedor solo si activas AI; hardware prerequisites; API de IA: opcional; Instalador o despliegue elegido; proveedor solo si activas AI.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.appflowy.io/docs/appflowy/install-appflowy/installation-methods
- **Primera prueba propuesta (no ejecutada):** Crea una página y una tabla de proyecto antes de activar funciones de IA Éxito: Puedes editar y recuperar los datos de la página y la tabla
- **Combina con:** `ollama` [8/motores], `coolify` [22/infraestructura], `markitdown` [13/conversion]
- **Alternativas:** `anytype-ts`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): anytype-ts. Usa el instalador para empezar; la guía from-source es de desarrollo; no se confirma aquí una ruta completa de modelo local.

### obsidian-skills (`obsidian-skills`)

- **Repo:** https://github.com/obsidianmd/obsidian-skills · MIT · nivel 2 · 63/100
- **Qué es:** Skills oficiales de Obsidian para agentes de IA, según la especificación Agent Skills. Licencia MIT. Es muy popular (~53k estrellas, 1.1.0).
- **Cuándo elegirlo:** Casos: Guiar un agente para trabajar con notas; Crear bases y lienzos en formatos Obsidian.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente compatible con Agent Skills; Obsidian y CLI solo para acciones que lo necesiten; hardware prerequisites; API de IA: no; Agente compatible con Agent Skills; Obsidian y CLI solo para acciones que lo necesiten.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/obsidianmd/obsidian-skills/blob/main/README.md

  ```sh
  claude plugin marketplace add obsidianmd/obsidian-skills
  claude plugin install obsidian@obsidian-skills
  ```
- **Primera prueba propuesta (no ejecutada):** Pide crear una nota y un JSON Canvas de prueba y revisa ambos archivos Éxito: Los formatos se abren correctamente y sus enlaces son válidos
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `jsoncanvas`, `defuddle` [4/crawlers]
- **Riesgos y avisos:** Sin alternativas declaradas. Se sustituye la combinación con obsidian-releases por integraciones documentadas. El formato es portable; funciones que llaman el CLI necesitan Obsidian y la versión de CLI correspondiente.

### obsidian-second-brain (`obsidian-second-brain`)

- **Repo:** https://github.com/eugeniughelbur/obsidian-second-brain · MIT · nivel 2 · 62/100 · recomendado en «Obsidian como segundo cerebro para agentes»
- **Qué es:** Skill y plugin que da memoria persistente a agentes de programación usando un vault de Obsidian, creado por @eugeniughelbur. Licencia MIT. Es muy activo (~5k estrellas, v0.20.0) y el README promociona un boletín del autor.
- **Cuándo elegirlo:** Casos: Compartir un diario de decisiones entre agentes; Consultar apuntes con búsqueda y fuentes.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Obsidian opcional para algunas funciones; agente; Git y uv; bóveda de prueba; hardware prerequisites; API de IA: opcional; Obsidian opcional para algunas funciones; agente; Git y uv; bóveda de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/README.md

  ```bash
  /plugin marketplace add eugeniughelbur/obsidian-second-brain
  /plugin install obsidian-second-brain@obsidian-second-brain
  ```
- **Primera prueba propuesta (no ejecutada):** Guarda una decisión ficticia y recupérala en otra sesión revisando el archivo Markdown Éxito: Puedes comprobar el texto guardado y qué contexto se inyecta
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `yt-dlp` [4/social], `obsidian-skills`, `40-questions` [15/personal], `notebooklm-py` [8/notebooklm]
- **Alternativas:** `claude-obsidian`
- **Riesgos y avisos:** Alternativas (elige una): claude-obsidian. No armes el agente en segundo plano sin revisar qué puede escribir. Los comandos y hooks no son iguales en todos los clientes; los agentes de fondo son opt-in y no deben confundirse con memoria pasiva.

### claude-obsidian (`claude-obsidian`)

- **Repo:** https://github.com/AgriciDaniel/claude-obsidian · MIT · nivel 2 · 60/100 · alternativa en «Obsidian como segundo cerebro para agentes»
- **Qué es:** Plugin de Claude Code que convierte un vault de Obsidian en una wiki de conocimiento que crece con cada fuente, creado por @AgriciDaniel. Licencia MIT.
- **Cuándo elegirlo:** Casos: Organizar apuntes por conceptos; Consultar decisiones desde una bóveda.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Python >=3.11; Obsidian; agente compatible; Bash para scripts; bóveda de prueba; hardware prerequisites; API de IA: no; Python >=3.11; Obsidian; agente compatible; Bash para scripts; bóveda de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/AgriciDaniel/claude-obsidian/blob/main/README.md

  ```bash
  claude plugin marketplace add AgriciDaniel/claude-obsidian
  claude plugin install claude-obsidian@agricidaniel-claude-obsidian
  ```
- **Primera prueba propuesta (no ejecutada):** Ingiere una nota ficticia desde inbox y revisa los enlaces antes de aceptar cambios Éxito: Puedes abrir el Markdown y comprobar origen y relaciones creadas
- **Combina con:** `claude-code` [20/terminal], `obsidian-skills`, `obsidian-clipper`, `defuddle` [4/crawlers]
- **Alternativas:** `obsidian-second-brain`
- **Riesgos y avisos:** Alternativas (elige una): obsidian-second-brain. Claude Code tiene el plugin completo; otros clientes usan skills y adaptaciones; prueba primero una copia de la bóveda.

### Obsidian: distribución y extensiones (`obsidian-releases`)

- **Repo:** https://github.com/obsidianmd/obsidian-releases · — · nivel 1 · 60/100
- **Qué es:** Repositorio de Obsidian para las releases públicas de la app y los directorios de plugins y temas de la comunidad. No tiene archivo de licencia y no contiene el código de Obsidian, que no es open source.
- **Cuándo elegirlo:** Casos: Encontrar una distribución oficial; Estudiar el catálogo de temas y plugins.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Navegador; instalador Obsidian compatible; hardware prerequisites; API de IA: no; Navegador; instalador Obsidian compatible.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/obsidianmd/obsidian-releases/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Identifica una release oficial y revisa compatibilidad de un plugin antes de usarlo Éxito: Puedes reconocer versión de app y versión mínima del complemento
- **Combina con:** `obsidian-sample-plugin`, `obsidian-minimal`, `obsidian-importer`
- **Riesgos y avisos:** Sin alternativas declaradas. Obsidian no es open source; este repo es solo distribución. Este repositorio distribuye releases y catálogos; no contiene el código completo de Obsidian ni todos los plugins listados.

### Logseq (`logseq`)

- **Repo:** https://github.com/logseq/logseq · AGPL-3.0 · nivel 1 · 59/100 · alternativa en «Notas y bases de conocimiento personales»
- **Qué es:** Plataforma de conocimiento de código abierto (AGPL-3.0) de Logseq Inc. Muy popular; el equipo trabaja en una versión basada en base de datos que sustituirá al modelo de archivos.
- **Cuándo elegirlo:** Casos: llevar un diario y notas enlazadas en archivos de texto propios; organizar investigación con bloques, referencias y consultas.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Clojure, Dockerfile, package.json; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://raw.githubusercontent.com/logseq/logseq/master/scripts/install-linux.sh | bash` — fuente: https://github.com/logseq/logseq/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Logseq, abre una carpeta vacía como grafo y crea una página enlazada desde el diario. Éxito: La página aparece en el grafo y sus referencias se muestran en ambas notas.
- **Combina con:** `syncthing` [15/archivos], `pandoc` [13/conversion], `claude-code` [20/terminal], `d2` [31/diagramas]
- **Alternativas:** `siyuan`, `trilium`, `joplin`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): joplin, trilium, siyuan. La migración a la versión con base de datos puede cambiar el formato de almacenamiento.

### Joplin (`joplin`)

- **Repo:** https://github.com/laurent22/joplin · AGPL-3.0 · nivel 1 · 58/100 · alternativa en «Notas y bases de conocimiento personales»
- **Qué es:** Aplicación de notas de código abierto (AGPL-3.0 según el archivo de licencia) creada por Laurent Cozic. Muy madura, con ingresos por Joplin Cloud y donaciones.
- **Cuándo elegirlo:** Casos: sustituir Evernote importando tus notas a una app abierta; mantener notas cifradas sincronizadas entre el móvil y el ordenador.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; TypeScript, package.json; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/laurent22/joplin/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Joplin, crea una libreta con notas y configura la sincronización con una carpeta o WebDAV de prueba. Éxito: Las notas aparecen en un segundo dispositivo tras sincronizar.
- **Combina con:** `nextcloud-server` [15/archivos], `syncthing` [15/archivos], `pandoc` [13/conversion]
- **Alternativas:** `siyuan`, `trilium`, `logseq`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): trilium, siyuan, logseq.

### obsidian-importer (`obsidian-importer`)

- **Repo:** https://github.com/obsidianmd/obsidian-importer · MIT · nivel 1 · 58/100
- **Qué es:** Plugin oficial de Obsidian para importar notas desde otras apps y formatos. Licencia MIT. Es activo (~2k estrellas, 3.2.0).
- **Cuándo elegirlo:** Casos: Migrar una muestra desde otra app; Verificar un formato de exportación antes de migrar.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Obsidian; plugin Importer; exportación de prueba del formato admitido; hardware prerequisites; API de IA: no; Obsidian; plugin Importer; exportación de prueba del formato admitido.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/obsidianmd/obsidian-importer/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Importa dos notas ficticias a una bóveda nueva y revisa enlaces y adjuntos Éxito: Puedes comparar las notas de origen y destino sin mezclar toda tu colección
- **Combina con:** `obsidian-help`, `obsidian-releases`, `markitdown` [13/conversion]
- **Riesgos y avisos:** Sin alternativas declaradas. Los comandos npm son para desarrollar el plugin; usa el flujo de instalación de Obsidian para importaciones normales.

### obsidian-clipper (`obsidian-clipper`)

- **Repo:** https://github.com/obsidianmd/obsidian-clipper · MIT · nivel 1 · 57/100
- **Qué es:** Obsidian Web Clipper, la extensión oficial de navegador de Obsidian para capturar y subrayar la web. Código MIT; las marcas y recursos de marketing quedan excluidos. Es activa (~6k estrellas, 1.7.1).
- **Cuándo elegirlo:** Casos: Capturar lecturas con una plantilla; Extraer un resumen opcional con Interpreter.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Extensión oficial del navegador; Obsidian; modelo solo para Interpreter; hardware prerequisites; API de IA: opcional; Extensión oficial del navegador; Obsidian; modelo solo para Interpreter.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://help.obsidian.md/web-clipper
- **Primera prueba propuesta (no ejecutada):** Guarda un artículo público de prueba con título, URL y fragmento y comprueba el Markdown Éxito: La nota conserva el contenido y la referencia de origen
- **Combina con:** `defuddle` [4/crawlers], `claude-obsidian`, `kepano-obsidian`, `obsidian-help`, `obsidian-minimal`
- **Riesgos y avisos:** Sin alternativas declaradas. El Interpreter envía el contenido de la página al proveedor de modelos que configures. Guardar notas localmente no hace local una petición Interpreter a un proveedor remoto; Ollama necesita permisos de origen para la extensión.

### kepano-obsidian (`kepano-obsidian`)

- **Repo:** https://github.com/kepano/kepano-obsidian · MIT · nivel 2 · 52/100
- **Qué es:** Plantilla personal de vault de Obsidian de @kepano, con su enfoque «de abajo arriba» para tomar notas. Licencia MIT. Es estable (~6k estrellas, 2.2.0) y poco activa (último cambio en enero de 2026).
- **Cuándo elegirlo:** Casos: Estudiar una organización de notas; Adaptar una plantilla personal de conocimiento.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Obsidian; bóveda nueva de prueba; hardware prerequisites; API de IA: no; Obsidian; bóveda nueva de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/kepano/kepano-obsidian/blob/main/Readme.md
- **Primera prueba propuesta (no ejecutada):** Abre una copia de la plantilla y añade una nota con dos enlaces a temas propios Éxito: Puedes reconocer qué convenciones te sirven sin alterar tu bóveda habitual
- **Combina con:** `obsidian-minimal`, `obsidian-clipper`, `obsidian-skills`, `40-questions` [15/personal]
- **Riesgos y avisos:** Sin alternativas declaradas. Es un ejemplo personal que el autor propone adaptar, no una metodología obligatoria ni la aplicación Obsidian completa.

### jsoncanvas (`jsoncanvas`)

- **Repo:** https://github.com/obsidianmd/jsoncanvas · MIT · nivel 1 · 50/100
- **Qué es:** Especificación abierta JSON Canvas para datos de lienzos infinitos, creada por Obsidian. Licencia MIT. Es estable (~4k estrellas, especificación 1.0) y se actualiza poco.
- **Cuándo elegirlo:** Casos: Intercambiar un mapa de ideas; Estudiar un formato abierto de lienzo.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Editor de texto; aplicación compatible con JSON Canvas; hardware prerequisites; API de IA: no; Editor de texto; aplicación compatible con JSON Canvas.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/obsidianmd/jsoncanvas/blob/main/readme.md
- **Primera prueba propuesta (no ejecutada):** Lee el esquema y crea un lienzo de dos notas conectadas usando una app compatible Éxito: Puedes abrir el archivo y reconocer nodos y conexión en JSON
- **Combina con:** `obsidian-skills`, `claude-code` [20/terminal], `obsidian-help`
- **Riesgos y avisos:** Sin alternativas declaradas. Es un formato, no un editor de canvas listo para instalar.

### obsidian-sample-plugin (`obsidian-sample-plugin`)

- **Repo:** https://github.com/obsidianmd/obsidian-sample-plugin · 0BSD · nivel 2 · 50/100
- **Qué es:** Plantilla oficial para crear plugins de Obsidian en TypeScript. Licencia 0BSD. Es estable (~5k estrellas, 1.0.0).
- **Cuándo elegirlo:** Casos: Aprender a programar un plugin; Prototipar una función para notas.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node; TypeScript; Git; Obsidian con bóveda de desarrollo; hardware prerequisites; API de IA: no; Node; TypeScript; Git; Obsidian con bóveda de desarrollo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/obsidianmd/obsidian-sample-plugin/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Copia la plantilla a un proyecto propio y añade un comando que muestre un mensaje ficticio Éxito: El comando aparece y funciona en la bóveda de desarrollo
- **Combina con:** `obsidian-releases`, `obsidian-skills`, `claude-code` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Es una plantilla para desarrolladores; no ofrece una función de usuario final con solo instalarla como plugin.

### Anytype Desktop (`anytype-ts`)

- **Repo:** https://github.com/anyproto/anytype-ts · Any Source Available License 1.0 (no OSI) · nivel 1 · 48/100 · alternativa en «Espacios de trabajo local-first tipo Notion»
- **Qué es:** Cliente de escritorio de Anytype, una base de conocimiento local-first, P2P y cifrada de extremo a extremo, de Any, una asociación suiza (organización anyproto).
- **Cuándo elegirlo:** Casos: Organizar notas y proyectos personales; Diseñar una colección con campos propios.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador de escritorio para tu sistema; espacio local; cuenta según ruta; hardware prerequisites; API de IA: no; Instalador de escritorio para tu sistema; espacio local; cuenta según ruta.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/anyproto/anytype-ts.git && cd anytype-ts` — fuente: https://github.com/anyproto/anytype-ts/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Crea dos objetos de prueba y relaciónalos en una vista sin añadir datos privados Éxito: Puedes navegar de un objeto al otro y revisar dónde se guardan
- **Combina con:** `claude-code` [20/terminal], `markitdown` [13/conversion], `activepieces` [1/motores]
- **Alternativas:** `appflowy`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): appflowy. La licencia restringe usos comerciales concretos; léela antes de redistribuir. Es source-available con licencia específica; construir el cliente desde fuente requiere también middleware y motor, no solo bun install.

### obsidian-minimal (`obsidian-minimal`)

- **Repo:** https://github.com/kepano/obsidian-minimal · MIT · nivel 1 · 48/100
- **Qué es:** Tema Minimal para Obsidian (escritorio, móvil y tablet), de @kepano. Licencia MIT. Es uno de los temas más usados y maduros (~6k estrellas, 9.1.4, activo).
- **Cuándo elegirlo:** Casos: Ajustar tipografía de una bóveda; Crear una interfaz de notas con menos distracciones.
- **Requisitos:** nivel 1: preparación sencilla; Obsidian; tema Minimal; complementos solo si deseas sus opciones; hardware prerequisites; API de IA: no; Obsidian; tema Minimal; complementos solo si deseas sus opciones.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://minimal.guide/
- **Primera prueba propuesta (no ejecutada):** Activa el tema en una bóveda de prueba y compara lectura, tablas y modo oscuro Éxito: Puedes cambiar de tema y distinguir apariencia de contenido
- **Combina con:** `obsidian-releases`, `kepano-obsidian`, `obsidian-clipper`, `40-questions` [15/personal]
- **Riesgos y avisos:** Sin alternativas declaradas. No necesitas compilar con npm para usar el tema; las opciones avanzadas pueden depender de plugins adicionales.

### obsidian-help (`obsidian-help`)

- **Repo:** https://github.com/obsidianmd/obsidian-help · — · nivel 1 · 43/100
- **Qué es:** Fuente de la documentación oficial de ayuda de Obsidian y sus traducciones. El repo no tiene archivo de licencia. Lo mantiene Obsidian y es activo (~2k estrellas).
- **Cuándo elegirlo:** Casos: Aprender funciones básicas de Obsidian; Consultar cómo configurar una bóveda.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; Obsidian solo para practicar; hardware prerequisites; API de IA: no; Navegador; Obsidian solo para practicar.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/obsidianmd/obsidian-help/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Lee la guía de enlaces y crea dos notas conectadas en una bóveda de prueba Éxito: Puedes navegar entre ambas y localizar la ayuda correspondiente
- **Combina con:** `obsidian-importer`, `obsidian-clipper`, `obsidian-skills`, `jsoncanvas`
- **Riesgos y avisos:** Sin alternativas declaradas. Sin licencia explícita. Contiene fuentes y traducciones de la ayuda, no el código fuente completo del producto.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-15-notas.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Notas, bóvedas y conocimiento personal», lee `docs/alexandria/categoria-15-notas.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-15-notas.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
