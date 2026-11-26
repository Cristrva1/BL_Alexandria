# Alexandría para agentes · Skills y métodos de producción audiovisual

Categoría 30 «Video con código y agentes creativos» › subcategoría `skills-video`. 15 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=30&sub=skills-video · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `openmontage` | Pipelines y herramientas para producir video con un agente,recursos… | 2 Intermedio | 72 | AGPL-3.0 (OSI copyleft) | recomendado |
| `brag` | Skills para que un agente convierta un proyecto o sitio en un video breve de… | 2 Intermedio | 71 | MIT (OSI permisiva) | sin grupo |
| `ffmpeg-skill` | Da a agentes herramientas locales de FFmpeg para recortar, reencuadrar… | 2 Intermedio | 70 | MIT (OSI permisiva) | sin grupo |
| `video-shotcraft` | Skill para crear videos de producto editables con Remotion, composición de… | 2 Intermedio | 68 | Apache-2.0 (OSI permisiva) | sin grupo |
| `openfilm` | Herramientas y skill para que un agente cree proyectos de video y permita… | 2 Intermedio | 66 | MIT (OSI permisiva) | sin grupo |
| `lemo-opuscar` | Biblioteca de estilos para video por código orientada a Claude,con licencias… | 2 Intermedio | 65 | MIT (código) + CC-BY-NC-4.0 (docs) + CC-BY-4.0 (demos) (source-available) | sin grupo |
| `rea-video` | Herramienta y skills para descomponer un video plano por plano y documentar… | 2 Intermedio | 62 | Apache-2.0 (OSI permisiva) | sin grupo |
| `video-use` | Edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs… | 2 Intermedio | 60 | MIT (OSI permisiva) | alternativa |
| `papermorph` | Skill que convierte libros en experiencias web animadas y narradas, con… | 2 Intermedio | 57 | MIT (OSI permisiva) | sin grupo |
| `srt-whiteboard-animation` | Skill para crear animaciones de pizarra con trazos y contenido organizados a… | 2 Intermedio | 48 | MIT (OSI permisiva) | sin grupo |
| `claude-animated-shorts` | Skill de Claude para crear cortos animados por código combinando personajes y… | 2 Intermedio | 47 | MIT (OSI permisiva) | sin grupo |
| `remotion-superpowers` | Orquestación de video con Remotion y servicios audiovisuales externos; requiere… | 2 Intermedio | 47 | MIT (OSI permisiva) | alternativa |
| `huashu-motion` | Skill para crear videos de presentación de productos con un agente de código… | 2 Intermedio | 46 | MIT (OSI permisiva) | sin grupo |
| `skills-remotion` | Skills oficiales de Remotion para que tu agente de código cree videos con React. | 1 Básico | 42 | — (sin licencia detectada) | sin grupo |
| `motionmaxxing` | Skill para mejorar composición, ritmo y movimiento de videos creados con… | 2 Intermedio | 38 | Apache-2.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### OpenMontage (`openmontage`)

- **Repo:** https://github.com/OpenMontageInc/OpenMontage · AGPL-3.0 · nivel 2 · 72/100 · recomendado en «Skills y flujos de producción de video»
- **Qué es:** OpenMontage, «sistema de producción de vídeo agéntico» open source, de OpenMontageInc (antes calesthio). Licencia AGPL-3.0. Creado en marzo de 2026, tiene ~81k estrellas, una cifra inusual; el README anuncia un nuevo producto en…
- **Cuándo elegirlo:** Casos: Preparar un video con recursos locales; Comparar un pipeline con servicios opcionales.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Python; Node; FFmpeg; dependencias de la ruta; material autorizado; hardware prerequisites; API de IA: opcional; Python; Node; FFmpeg; dependencias de la ruta; material autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/OpenMontageInc/OpenMontage/blob/main/README.md

  ```bash
  git clone https://github.com/calesthio/OpenMontage.git
  cd OpenMontage
  make setup
  ```
- **Primera prueba propuesta (no ejecutada):** Empieza con material propio y narración Piper y comprueba guion, timeline y exportación Éxito: Puedes revisar la procedencia de cada asset y abrir el MP4
- **Combina con:** `remotion` [30/motores], `ffmpeg` [12/edicion], `kokoro` [29/tts], `elevenlabs-python` [29/tts]
- **Alternativas:** `video-use`, `remotion-superpowers`, `moneyprinterturbo`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): remotion-superpowers, moneyprinterturbo. Documenta asistentes con archivos y ejecución de código; Piper permite voz offline, pero no implica que el modelo del agente o todos los pipelines sean locales.

### brag (`brag`)

- **Repo:** https://github.com/latent-spaces/brag · MIT · nivel 2 · 71/100
- **Qué es:** /brag, skill que convierte el proyecto que has construido en un vídeo de lanzamiento corto y compartible, con música, movimiento y textos para redes, de latent-spaces. Licencia MIT. Creado en junio de 2026, tiene ~22k estrellas (v0.6.0).
- **Cuándo elegirlo:** Casos: Presentar una demo de producto; Preparar una pieza de lanzamiento.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente; runtime y FFmpeg según variante; sitio propio de prueba; hardware prerequisites; API de IA: opcional; Agente; runtime y FFmpeg según variante; sitio propio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add https://github.com/latent-spaces/brag --skill brag-slim` — fuente: https://github.com/latent-spaces/brag/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un video corto de una función real del sitio y contrasta lo mostrado con su comportamiento Éxito: Puedes revisar guion, capturas, música y duración
- **Combina con:** `hyperframes` [30/motores], `claude-code` [20/terminal], `gsap` [26/animacion]
- **Riesgos y avisos:** Sin alternativas declaradas. Brag-slim y el flujo clásico tienen dependencias distintas; documenta plugins Claude Code y Codex y no garantiza resultados iguales con todos los modelos.

### FFmpeg Skill (`ffmpeg-skill`)

- **Repo:** https://github.com/kajisho5/ffmpeg-skill · MIT · nivel 2 · 70/100
- **Qué es:** Da a agentes herramientas locales de FFmpeg para recortar, reencuadrar, normalizar audio y exportar video con pasos trazables.
- **Cuándo elegirlo:** Casos: Recortar un anuncio de prueba a quince segundos.; Reencuadrar una toma propia para formato vertical. Evítalo si no usas un agente compatible con skills.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Python, package.json; API de IA: no; FFmpeg 6.1 o posterior con los codecs y filtros de la operación; entorno del agente para la skill..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/README.md
- **Primera prueba propuesta (no ejecutada):** Comprueba los filtros, prepara un clip propio y prueba un recorte con un archivo de salida nuevo. Éxito: El archivo resultante tiene la duración esperada y el original sigue intacto.
- **Combina con:** `ffmpeg` [12/edicion]
- **Riesgos y avisos:** FFmpeg no necesita una API de modelo. Subtítulos, plugins y ejecución del agente pueden tener requisitos y cobros aparte.

### video-shotcraft (`video-shotcraft`)

- **Repo:** https://github.com/Vincentwei1021/video-shotcraft · Apache-2.0 · nivel 2 · 68/100
- **Qué es:** video-shotcraft, skill para que Claude Code o Codex creen vídeos promocionales de producto a partir de capturas de tus páginas reales, de @Vincentwei1021.
- **Cuándo elegirlo:** Casos: Preparar una promo de producto; Organizar planos sincronizados con sonido.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente; Node y Remotion; herramientas de captura; recursos autorizados; hardware prerequisites; API de IA: opcional; Agente; Node y Remotion; herramientas de captura; recursos autorizados.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add Vincentwei1021/video-shotcraft` — fuente: https://github.com/Vincentwei1021/video-shotcraft/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Captura una pantalla propia y crea un plano corto verificando legibilidad, tiempo y audio Éxito: Puedes revisar composición editable y exportación
- **Combina con:** `remotion` [30/motores], `claude-code` [20/terminal], `codex` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Documenta Claude Code y Codex; los servicios de publicación son opcionales y no se deben activar al preparar un borrador.

### openfilm (`openfilm`)

- **Repo:** https://github.com/openfilm/openfilm · MIT · nivel 2 · 66/100
- **Qué es:** OpenFilm, «agente de vídeo con IA open source»: formato, CLI, Studio y app de escritorio, de openfilm. Licencia MIT (el nombre y el logo son marcas). Creado en octubre de 2026, tiene ~7.6k estrellas (v0.3.2).
- **Cuándo elegirlo:** Casos: Preparar un video editable; Revisar el resultado de un agente en un editor.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Node 22.2+; FFmpeg; Git para versiones; agente; recursos propios; hardware prerequisites; API de IA: opcional; Node 22.2+; FFmpeg; Git para versiones; agente; recursos propios.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add openfilm/openfilm` — fuente: https://github.com/openfilm/openfilm/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre un ejemplo y modifica un título en Studio antes de exportar un clip corto Éxito: Puedes inspeccionar el proyecto editable y el MP4
- **Combina con:** `claude-code` [20/terminal], `gsap` [26/animacion], `three.js` [26/animacion], `mediabunny` [30/motores]
- **Riesgos y avisos:** Sin alternativas declaradas. El video se describe como páginas web y puede editarse; instalar la skill y abrir Studio son pasos distintos y el nombre y logo conservan reglas de marca.

### lemo-opuscar (`lemo-opuscar`)

- **Repo:** https://github.com/lemomo-ai/lemo-opuscar · MIT (código) + CC-BY-NC-4.0 (docs) + CC-BY-4.0 (demos) · nivel 2 · 65/100
- **Qué es:** Lemo-Opuscar, colección de 99 estilos cinematográficos para que un agente de código haga películas cortas íntegramente con código, de Lemomo (@lemomo_ai).
- **Cuándo elegirlo:** Casos: Explorar una dirección visual para un video; Preparar una pieza por código.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Claude Code; dependencias del estilo; material propio; Kokoro según voz; hardware prerequisites; API de IA: opcional; Claude Code; dependencias del estilo; material propio; Kokoro según voz.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md

  ```sh
  claude plugin marketplace add lemomo-ai/lemo-opuscar
  claude plugin install lemo-opuscar@lemolab
  ```
- **Primera prueba propuesta (no ejecutada):** Elige un estilo y crea una escena de prueba revisando créditos antes de adaptar el resto Éxito: Puedes identificar código, estilo y assets de la salida
- **Combina con:** `claude-code` [20/terminal], `ffmpeg` [12/edicion], `three.js` [26/animacion]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. La documentación de los estilos es no comercial (CC BY-NC). El autor lo orienta a Claude y advierte diferencias con otros modelos; demos, guías, voz y assets no comparten una licencia única; Kokoro local no sustituye el….

### rea-video (`rea-video`)

- **Repo:** https://github.com/JuneYaooo/rea-video · Apache-2.0 · nivel 2 · 62/100
- **Qué es:** rea-video, herramienta y skill para hacer ingeniería inversa de vídeos plano a plano, de @JuneYaooo. Licencia Apache-2.0. Es muy reciente (octubre de 2026, ~9.3k estrellas, v0.1.0).
- **Cuándo elegirlo:** Casos: Estudiar ritmo de una pieza; Preparar un plan de recreación con material propio.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Python >=3.10; FFmpeg; video autorizado; modelo con visión solo si eliges revisión AI; hardware prerequisites; API de IA: opcional; Python >=3.10; FFmpeg; video autorizado; modelo con visión solo si eliges revisión AI.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "rea-video[ocr] @ git+https://github.com/JuneYaooo/rea-video"` — fuente: https://github.com/JuneYaooo/rea-video/blob/main/skills/rea-video/references/setup.md
- **Primera prueba propuesta (no ejecutada):** Analiza un clip corto y contrasta los planos del VIDEO.md con el original Éxito: Puedes revisar tiempos, estructura e hipótesis de técnica
- **Combina con:** `remotion` [30/motores], `ffmpeg` [12/edicion], `claude-code` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Las clasificaciones de material AI o filmado son estimaciones, no pruebas forenses; recrea técnicas con recursos de los que tengas derechos.

### video-use (`video-use`)

- **Repo:** https://github.com/browser-use/video-use · MIT · nivel 2 · 60/100 · alternativa en «Skills y flujos de producción de video»
- **Qué es:** video-use, edición de vídeo con Claude Code y FFmpeg, de browser-use. Licencia MIT. Creado en abril de 2026, tiene ~31k estrellas y no cambia desde octubre de 2026.
- **Cuándo elegirlo:** Casos: Editar una entrevista propia; Seleccionar tomas de un tutorial.
- **Requisitos:** nivel 2: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP), requiere clave de API; Agente con shell; Python y uv; FFmpeg; material propio; clave ElevenLabs; hardware prerequisites; API de IA: sí; Agente con shell; Python y uv; FFmpeg; material propio; clave ElevenLabs.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/browser-use/video-use ~/Developer/video-use` — fuente: https://github.com/browser-use/video-use/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Importa un clip corto y revisa transcripción y plan de cortes antes de exportar Éxito: Puedes contrastar el montaje con el material original
- **Combina con:** `ffmpeg` [12/edicion], `claude-code` [20/terminal], `hermes-agent` [21/asistentes], `elevenlabs-python` [29/tts]
- **Alternativas:** `openmontage`, `remotion-superpowers`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): remotion-superpowers. Depende de ElevenLabs (servicio de pago) para transcribir. Documenta Claude Code, Codex y otros agentes con shell; la ruta instalada requiere configurar la transcripción externa y no se debe anunciar como totalmente….

### Papermorph (`papermorph`)

- **Repo:** https://github.com/DozenTwelve/Papermorph · MIT · nivel 2 · 57/100
- **Qué es:** Papermorph, skill para agentes que convierte libros de texto en lecciones web narradas e interactivas, historias en películas de títeres de papel y libros en documentales o cortos verticales, de @DozenTwelve.
- **Cuándo elegirlo:** Casos: Preparar una lección animada; Explorar una historia interactiva.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); uv; FFmpeg; navegadores Playwright; libro propio o autorizado; voz local o remota; hardware prerequisites; API de IA: opcional; uv; FFmpeg; navegadores Playwright; libro propio o autorizado; voz local o remota.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code   # or --agent opencode` — fuente: https://github.com/DozenTwelve/Papermorph/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Transforma una página breve autorizada en una lección y comprueba texto, narración y controles Éxito: Puedes contrastar el contenido con la página original
- **Combina con:** `claude-code` [20/terminal], `opencode` [20/terminal], `kokoro` [29/tts]
- **Riesgos y avisos:** Sin alternativas declaradas. Documenta Claude Code y OpenCode; sus ejemplos de coste son de producciones concretas y los recursos del sitio conservan licencias separadas del código.

### srt-whiteboard-animation (`srt-whiteboard-animation`)

- **Repo:** https://github.com/geeklee/srt-whiteboard-animation · MIT · nivel 2 · 48/100
- **Qué es:** SRT 白板动画, skill que convierte subtítulos SRT en vídeos de pizarra dibujados a mano siguiendo la narración, de @geeklee. Licencia MIT. Tiene ~5.6k estrellas (v1.0.0) y el README está en chino.
- **Cuándo elegirlo:** Casos: Crear una explicación de pizarra; Prototipar una secuencia narrada.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente con skill; Python y renderizadores del proyecto; SRT y recursos autorizados; hardware prerequisites; API de IA: no; Agente con skill; Python y renderizadores del proyecto; SRT y recursos autorizados.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/geeklee/srt-whiteboard-animation/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Usa tres líneas de subtítulos y revisa el orden de trazos y la sincronización con cada frase Éxito: Puedes comparar tiempos del SRT y salida MP4
- **Combina con:** `whisperx` [29/stt], `kokoro` [29/tts], `manim-community` [30/motores]
- **Riesgos y avisos:** Sin alternativas declaradas. Incluye metadatos Codex; no se confirma una instalación específica equivalente de otros hosts y el SRT no aporta automáticamente una narración.

### claude-animated-shorts (`claude-animated-shorts`)

- **Repo:** https://github.com/mromidev/claude-animated-shorts · MIT · nivel 2 · 47/100
- **Qué es:** Claude Animated Shorts, skill gratuita de Claude que acompaña a un vídeo tutorial, de @mromidev. Licencia MIT (los fotogramas de referencia solo sirven para estudiar el estilo).
- **Cuándo elegirlo:** Casos: Crear un corto animado de prueba; Estudiar personajes 2D en escena 3D.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Claude Code; Three.js y Remotion; dependencias de render; historia propia; hardware prerequisites; API de IA: no; Claude Code; Three.js y Remotion; dependencias de render; historia propia.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mromidev/claude-animated-shorts/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Prepara un plano de pocos segundos y revisa personajes, cámara y tiempos antes de un corto completo Éxito: Puedes reproducir la escena y contrastarla con el guion
- **Combina con:** `remotion` [30/motores], `three.js` [26/animacion], `claude-code` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Proyecto de un solo autor ligado a un vídeo. Código y documentos MIT; los frames de referencia son solo para estudio de estilo y no se entregan como assets comerciales reutilizables; viral no es garantía.

### Remotion Superpowers (`remotion-superpowers`)

- **Repo:** https://github.com/DojoCodingLabs/remotion-superpowers · MIT · nivel 2 · 47/100 · alternativa en «Skills y flujos de producción de video»
- **Qué es:** Remotion Superpowers, plugin que conecta voz en off, música, efectos, material de archivo, imágenes y clips de IA, subtítulos y un ciclo de revisión con Remotion a través del agente, de DojoCodingLabs. Licencia MIT.
- **Cuándo elegirlo:** Casos: Preparar un video narrado; Combinar clips y subtítulos.
- **Requisitos:** nivel 2: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP), requiere clave de API; Node 22.18+; Remotion; skills oficiales; claves de medios; uv para MCP opcional; hardware prerequisites; API de IA: sí; Node 22.18+; Remotion; skills oficiales; claves de medios; uv para MCP opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/DojoCodingLabs/remotion-superpowers/blob/main/README.md

  ```bash
  codex plugin marketplace add DojoCodingLabs/remotion-superpowers
  codex plugin add remotion-superpowers@remotion-superpowers
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta setup y prepara un guion corto con estimación de servicios antes de generar Éxito: Puedes identificar claves, proveedores y resultado de cada etapa
- **Combina con:** `remotion` [30/motores], `skills-remotion`, `claude-code` [20/terminal], `elevenlabs-python` [29/tts]
- **Alternativas:** `openmontage`, `video-use`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): openmontage, video-use. Depende de servicios de pago. Las captions pueden usar Whisper local pero el conjunto no es enteramente local; hooks y subagentes son extras de Claude Code y no se heredan en todos los hosts.

### huashu-motion (`huashu-motion`)

- **Repo:** https://github.com/alchaincyf/huashu-motion · MIT · nivel 2 · 46/100
- **Qué es:** huashu-motion, skill para generar vídeos de lanzamiento de producto «de calidad comercial» con un agente, de @alchaincyf (花叔). Licencia MIT; incluye GSAP (licencia Standard de GSAP) y fuentes SIL OFL.
- **Cuándo elegirlo:** Casos: Prototipar una presentación de producto; Explorar estilos de motion graphics.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente compatible; dependencias del runtime; brief y recursos propios; hardware prerequisites; API de IA: no; Agente compatible; dependencias del runtime; brief y recursos propios.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add alchaincyf/huashu-motion` — fuente: https://github.com/alchaincyf/huashu-motion/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera una escena corta y revisa ritmo, títulos y sincronía antes de extender la pieza Éxito: Puedes identificar decisiones de composición y duración
- **Combina con:** `gsap` [26/animacion], `kokoro` [29/tts], `claude-code` [20/terminal]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. GSAP no es OSI: revisa su licencia. Documenta Claude Code y Codex; comercial-grade es una descripción del autor y la licencia GSAP y fuentes siguen aplicándose.

### Remotion Agent Skills (`skills-remotion`)

- **Repo:** https://github.com/remotion-dev/skills · — · nivel 1 · 42/100
- **Qué es:** Remotion Agent Skills, skills oficiales de Remotion con buenas prácticas para que agentes de código (Claude Code, Codex, Kimi Code, Cursor) trabajen en proyectos Remotion. GitHub no detecta licencia. Tiene ~7.3k estrellas.
- **Cuándo elegirlo:** Casos: Aprender Remotion con un agente; Preparar una plantilla de video.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente compatible; proyecto Remotion; Node; recursos propios; hardware prerequisites; API de IA: opcional; Agente compatible; proyecto Remotion; Node; recursos propios.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add remotion-dev/skills` — fuente: https://github.com/remotion-dev/skills/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Pide una composición corta y comprueba frames y duración antes de añadir voz o servicios Éxito: Puedes revisar la composición React y su render
- **Combina con:** `remotion` [30/motores], `claude-code` [20/terminal], `remotion-superpowers`
- **Riesgos y avisos:** Sin alternativas declaradas. Sin licencia detectada. Son instrucciones oficiales para hosts Agent Skills; no incluyen la licencia de Remotion ni créditos de medios.

### motionmaxxing (`motionmaxxing`)

- **Repo:** https://github.com/Tejashmakwana/motionmaxxing · Apache-2.0 · nivel 2 · 38/100
- **Qué es:** motionmaxxing, skill para agentes que mejora vídeos de motion graphics genéricos («AI slop») hasta parecer hechos por un diseñador, de @Tejashmakwana. Licencia Apache-2.0; GSAP y las fuentes conservan sus licencias.
- **Cuándo elegirlo:** Casos: Mejorar una pieza de lanzamiento; Preparar una animación tipográfica.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Node 22+; Python 3; FFmpeg; Chrome; agente con shell; hardware prerequisites; API de IA: opcional; Node 22+; Python 3; FFmpeg; Chrome; agente con shell.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Tejashmakwana/motionmaxxing/blob/main/README.md

  ```bash
  git clone https://github.com/Tejashmakwana/motionmaxxing ~/.claude/skills/motionmaxxing
  bash ~/.claude/skills/motionmaxxing/install.sh        # checks the requirements; installs nothing system-wide
  ```
- **Primera prueba propuesta (no ejecutada):** Revisa providers.sh y crea una escena tipográfica breve antes de añadir voces o imágenes Éxito: Puedes comparar composición y tiempos de dos versiones
- **Combina con:** `gsap` [26/animacion], `claude-code` [20/terminal], `ffmpeg` [12/edicion]
- **Riesgos y avisos:** Sin alternativas declaradas. El skill admite hosts que leen SKILL.md pero las funciones dependen de herramientas disponibles; no garantiza una valoración profesional por sus puntuaciones.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-30-skills-video.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Skills y métodos de producción audiovisual», lee `docs/alexandria/categoria-30-skills-video.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-30-skills-video.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
