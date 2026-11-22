# Alexandría para agentes · Edición, grabación y subtítulos

Categoría 12 «Editar, grabar y generar video» › subcategoría `edicion`. 11 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=12&sub=edicion · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `ffmpeg` | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio… | 2 Intermedio | 69 | LGPL-2.1-or-later (partes opcionales GPL-2.0-or-later) (OSI copyleft) | sin grupo |
| `obs-studio` | App de escritorio libre para grabar pantalla y transmitir en directo, con… | 1 Básico | 68 | GPL-2.0 (OSI copyleft) | sin grupo |
| `videolingo` | App para reconocer voz, traducir subtítulos y preparar doblaje, con ASR local… | 2 Intermedio | 63 | Apache-2.0 (OSI permisiva) | sin grupo |
| `concat` | Editor de video local con interfaz y mecanismos de automatización mediante… | 2 Intermedio | 62 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `opencut` | Editor de video abierto cuya versión clásica puede probarse en la web mientras… | 2 Intermedio | 62 | MIT (OSI permisiva) | recomendado |
| `lossless-cut` | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en… | 1 Básico | 61 | GPL-2.0 (OSI copyleft) | sin grupo |
| `davinci-resolve-mcp` | Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje… | 2 Intermedio | 60 | MIT (OSI permisiva) | sin grupo |
| `kdenlive` | Editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos… | 1 Básico | 59 | GPL-3.0 (OSI copyleft) | alternativa |
| `shotcut` | Editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de… | 1 Básico | 59 | GPL-3.0 (OSI copyleft) | alternativa |
| `handbrake` | Transcodificador de vídeo libre para Linux, macOS y Windows con interfaz… | 1 Básico | 58 | GPL-2.0 (OSI copyleft) | sin grupo |
| `openrv` | Reproductor de revisión de video y secuencias de imágenes para comparar tomas y… | 1 Básico | 44 | Apache-2.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### FFmpeg (`ffmpeg`)

- **Repo:** https://github.com/FFmpeg/FFmpeg · LGPL-2.1-or-later (partes opcionales GPL-2.0-or-later) · nivel 2 · 69/100
- **Qué es:** FFmpeg, conjunto de librerías y herramientas para procesar contenido multimedia. Licencia mayoritariamente LGPL con componentes opcionales GPL (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Convertir un video para una plataforma; Extraer audio de una grabación propia.
- **Requisitos:** nivel 2: instalación simple, pero se usa con opciones de línea de comandos; Binario apropiado al sistema; archivo de video propio; espacio de salida; hardware prerequisites; API de IA: no; Binario apropiado al sistema; archivo de video propio; espacio de salida.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://ffmpeg.org/download.html
- **Primera prueba propuesta (no ejecutada):** Convierte una copia de un video breve y comprueba duración, audio y formato con ffprobe Éxito: La salida se reproduce y conserva las pistas esperadas
- **Combina con:** `whisper` [29/stt], `yt-dlp` [4/social], `moviepy` [30/motores]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Al distribuir binarios, revisa si incluyen componentes GPL o códecs con patentes. Descarga un build para tu sistema o sigue la compilación; el repositorio GitHub es un espejo de la fuente oficial.

### OBS Studio (`obs-studio`)

- **Repo:** https://github.com/obsproject/obs-studio · GPL-2.0 · nivel 1 · 68/100
- **Qué es:** OBS Studio, software libre para grabar y transmitir vídeo en directo. Licencia GPL-2.0 o posterior. Es muy maduro (~80k estrellas, 33.0.1).
- **Cuándo elegirlo:** Casos: Grabar una explicación de pantalla; Preparar escenas para una transmisión.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador oficial; permisos de captura; micrófono opcional; disco; hardware prerequisites; API de IA: no; Instalador oficial; permisos de captura; micrófono opcional; disco.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://obsproject.com/download
- **Primera prueba propuesta (no ejecutada):** Crea una escena con pantalla y micrófono y graba veinte segundos Éxito: El archivo tiene imagen, audio y niveles aceptables
- **Combina con:** `lossless-cut`, `opencut`, `faster-whisper` [29/stt], `rnnoise` [29/audio], `deep-live-cam` [28/rostros], `rvc` [29/tts]
- **Riesgos y avisos:** Sin alternativas declaradas. Prueba el archivo antes de una sesión larga; seleccionar una fuente no acredita que capture el audio deseado.

### VideoLingo (`videolingo`)

- **Repo:** https://github.com/Huanshere/VideoLingo · Apache-2.0 · nivel 2 · 63/100
- **Qué es:** VideoLingo, app para subtitular, traducir y doblar vídeos, de @Huanshere. Licencia Apache-2.0. Es activa (~19k estrellas, v3.2.0).
- **Cuándo elegirlo:** Casos: Subtitular un tutorial propio; Preparar una traducción de una demostración.
- **Requisitos:** nivel 2: preparación media; Python y uv; FFmpeg y modelos según ruta; LLM con salida JSON; video propio; hardware prerequisites; API de IA: depends; Python y uv; FFmpeg y modelos según ruta; LLM con salida JSON; video propio.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Huanshere/VideoLingo/blob/main/README.md

  ```bash
  git clone https://github.com/Huanshere/VideoLingo.git && cd VideoLingo
  uv run start.py
  ```
- **Primera prueba propuesta (no ejecutada):** Procesa un clip corto con voz clara y revisa transcripción, traducción y tiempos antes de doblar Éxito: Los subtítulos coinciden con las palabras y puedes corregir errores antes de exportar
- **Combina con:** `yt-dlp` [4/social], `gpt-sovits` [29/tts], `ffmpeg`
- **Alternativas:** `omnivoice-studio`
- **Riesgos y avisos:** Alternativas (elige una): omnivoice-studio. Se retiró whisperx de las combinaciones: ya no es el ASR por defecto y solo aparece en agradecimientos. El reconocimiento local actual usa Qwen3-ASR y ForcedAligner por defecto; no se debe seguir describiendo todo el pipeline como WhisperX.

### Concat (`concat`)

- **Repo:** https://github.com/jub0t/Concat · AGPL-3.0 · nivel 2 · 62/100
- **Qué es:** Concat, editor de vídeo libre y multiplataforma, de @jub0t. Licencia AGPL-3.0 o posterior, con licencia comercial disponible. Es reciente (~18k estrellas, v0.2.11).
- **Cuándo elegirlo:** Casos: Editar un video sin subir el material; Automatizar una variante de montaje mediante MCP.
- **Requisitos:** nivel 2: preparación media; Distribución compatible; clip propio; modelos opcionales descargados; permisos de automatización para MCP; hardware prerequisites; API de IA: no; Distribución compatible; clip propio; modelos opcionales descargados; permisos de automatización para MCP.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/jub0t/Concat/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Recorta una copia de un clip y añade subtítulos locales antes de exportar Éxito: Puedes revisar texto, puntos de corte y archivo final
- **Combina con:** `claude-code` [20/terminal], `ffmpeg`, `yt-dlp` [4/social]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Está en beta; MCP puede usar la ventana o un proceso separado y sus modos tienen límites distintos al editar el mismo proyecto.

### OpenCut (`opencut`)

- **Repo:** https://github.com/OpenCut-app/OpenCut · MIT · nivel 2 · 62/100 · recomendado en «Editores de video»
- **Qué es:** OpenCut, editor de vídeo libre para web, escritorio y móvil. Licencia MIT. Es muy popular (~99k estrellas, v0.3.0) y se está reescribiendo desde cero.
- **Cuándo elegirlo:** Casos: Evaluar una alternativa de edición abierta; Estudiar la arquitectura de un editor con plugins.
- **Requisitos:** nivel 2: preparación media, app o instalador listo para usar; Navegador para versión clásica o herramientas de la nueva rama; clip de prueba; hardware prerequisites; API de IA: no; Navegador para versión clásica o herramientas de la nueva rama; clip de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OpenCut-app/OpenCut/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Prueba un corte corto en la versión disponible y revisa qué funciones pertenecen a la reescritura Éxito: Puedes exportar o identificar con claridad qué parte aún no está disponible
- **Combina con:** `lossless-cut`, `obs-studio`, `whisperx` [29/stt]
- **Alternativas:** `shotcut`, `kdenlive`
- **Riesgos y avisos:** Sin alternativas declaradas. En reescritura: el código del repo principal aún no es un editor utilizable. El proyecto se reescribe; la versión clásica web y la rama principal no tienen necesariamente las mismas funciones ni instalación.

### LosslessCut (`lossless-cut`)

- **Repo:** https://github.com/mifi/lossless-cut · GPL-2.0 · nivel 1 · 61/100
- **Qué es:** LosslessCut, app de escritorio para editar vídeo y audio sin pérdida mediante FFmpeg, de @mifi. Licencia GPL-2.0. Es madura (~46k estrellas, v3.70.2) y la mantiene una sola persona.
- **Cuándo elegirlo:** Casos: Quitar una parte de una grabación; Separar o unir medios compatibles.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Distribución para tu sistema; archivo compatible; espacio de salida; hardware prerequisites; API de IA: no; Distribución para tu sistema; archivo compatible; espacio de salida.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://losslesscut.app/docs/getting-started
- **Primera prueba propuesta (no ejecutada):** Marca dos puntos de un video propio y exporta el segmento sin recodificar Éxito: Compruebas duración, comienzo, final y pistas del clip
- **Combina con:** `ffmpeg`, `yt-dlp` [4/social], `whisperx` [29/stt], `moviepy` [30/motores], `obs-studio`, `opencut`
- **Riesgos y avisos:** Sin alternativas declaradas. Descarga solo desde las fuentes oficiales. Los cortes sin recodificar dependen de fotogramas clave y del contenedor; no prometas precisión idéntica a un render completo.

### DaVinci Resolve MCP (`davinci-resolve-mcp`)

- **Repo:** https://github.com/samuelgursky/davinci-resolve-mcp · MIT · nivel 2 · 60/100
- **Qué es:** DaVinci Resolve MCP Server, servidor MCP que permite a asistentes de IA controlar DaVinci Resolve mediante su API oficial de scripting, de @samuelgursky. Licencia MIT. Es activo (~4k estrellas, v5.2.11).
- **Cuándo elegirlo:** Casos: Organizar material desde un agente; Preparar ajustes de render con revisión.
- **Requisitos:** nivel 2: preparación media; Resolve >=18.5; Python 64 bits; FFmpeg; Studio o puente interno para edición gratuita; hardware prerequisites; API de IA: no; Resolve >=18.5; Python 64 bits; FFmpeg; Studio o puente interno para edición gratuita.
- **Instalación (documentada en la fuente; no ejecutada):** `npx davinci-resolve-mcp setup` — fuente: https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** En un proyecto de prueba consulta el media pool y añade un marcador antes de automatizar montaje Éxito: El marcador aparece en el clip o timeline esperado
- **Combina con:** `claude-code` [20/terminal], `ffmpeg`, `whisper` [29/stt]
- **Riesgos y avisos:** Sin alternativas declaradas. Trabaja sobre copias de proyectos: el agente puede modificar la línea de tiempo. Studio permite scripting externo Local; la edición gratuita usa un puente interno documentado; instalar MCP no activa por sí solo Resolve.

### Kdenlive (`kdenlive`)

- **Repo:** https://github.com/KDE/kdenlive · GPL-3.0 · nivel 1 · 59/100 · alternativa en «Editores de video»
- **Qué es:** Editor de vídeo de código abierto (GPL-3.0 según GitHub) desarrollado por la comunidad KDE. El repositorio de GitHub es un espejo: el desarrollo canónico vive en invent.kde.org (multimedia/kdenlive). Maduro, con versiones trimestrales.
- **Cuándo elegirlo:** Casos: montar vídeos con varias pistas, efectos y corrección de color; subtitular automáticamente entrevistas o tutoriales.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; C++, CMakeLists.txt; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/KDE/kdenlive/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Kdenlive desde kdenlive.org, crea un proyecto, añade clips a la línea de tiempo y renderiza un MP4. Éxito: El render termina y el archivo reproduce el montaje.
- **Combina con:** `ffmpeg`, `whisper` [29/stt], `obs-studio`
- **Alternativas:** `opencut`, `shotcut`
- **Riesgos y avisos:** Alternativas (elige una): shotcut, opencut. Reporta incidencias y contribuye en invent.kde.org, no en el espejo de GitHub.

### Shotcut (`shotcut`)

- **Repo:** https://github.com/mltframework/shotcut · GPL-3.0 · nivel 1 · 59/100 · alternativa en «Editores de video»
- **Qué es:** Editor de vídeo de código abierto (GPL-3.0) cuyo autor principal es Dan Dennedy, también mantenedor de MLT. Maduro, con versiones regulares para Windows, macOS y Linux.
- **Cuándo elegirlo:** Casos: editar vídeos de YouTube o cursos con cortes, transiciones y títulos; generar subtítulos automáticos a partir del audio de un vídeo.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; C++, CMakeLists.txt; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mltframework/shotcut/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Shotcut desde shotcut.org, importa dos clips, córtalos en la línea de tiempo y exporta un MP4. Éxito: El MP4 exportado reproduce los dos clips con el corte aplicado.
- **Combina con:** `ffmpeg`, `whisper-cpp` [29/stt], `obs-studio`
- **Alternativas:** `opencut`, `kdenlive`
- **Riesgos y avisos:** Alternativas (elige una): kdenlive, opencut.

### HandBrake (`handbrake`)

- **Repo:** https://github.com/HandBrake/HandBrake · GPL-2.0 · nivel 1 · 58/100
- **Qué es:** Transcodificador de vídeo de código abierto (GPL-2.0 en la mayoría de archivos) mantenido por el HandBrake Team desde 2003. Muy maduro.
- **Cuándo elegirlo:** Casos: convertir grabaciones de cámara o pantalla a MP4 compatibles con móviles y webs; reducir el tamaño de una videoteca manteniendo la calidad.
- **Requisitos:** nivel 1: app de escritorio con instalador para Windows, macOS y Linux; C; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/HandBrake/HandBrake/blob/master/README.markdown
- **Primera prueba propuesta (no ejecutada):** Instala HandBrake, abre un vídeo corto y conviértelo con un preset de 1080p. Éxito: Obtienes un MP4 reproducible en el móvil con menor tamaño que el original.
- **Combina con:** `ffmpeg`, `obs-studio`, `lossless-cut`, `jellyfin` [15/lectura]
- **Riesgos y avisos:** No elimina protecciones anticopia; respeta los derechos del material que conviertes.

### OpenRV (`openrv`)

- **Repo:** https://github.com/AcademySoftwareFoundation/OpenRV · Apache-2.0 · nivel 1 · 44/100
- **Qué es:** Open RV, visor de imágenes y secuencias para artistas de VFX y animación, de la Academy Software Foundation. Licencia Apache-2.0 con componentes bajo otras licencias (GitHub muestra NOASSERTION). Tiene ~800 estrellas (v4.0.2).
- **Cuándo elegirlo:** Casos: Revisar una entrega de animación; Comparar versiones de un efecto visual.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Build compatible o herramientas de compilación; secuencia o video de prueba; hardware prerequisites; API de IA: no; Build compatible o herramientas de compilación; secuencia o video de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --recursive https://github.com/AcademySoftwareFoundation/OpenRV.git` — fuente: https://github.com/AcademySoftwareFoundation/OpenRV/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre dos versiones de una toma y compara fotogramas en el mismo punto Éxito: Puedes observar diferencias de imagen sin desalinear el tiempo
- **Combina con:** `blender` [26/creacion-3d], `ffmpeg`, `comfyui` [11/interfaces]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Es una herramienta de revisión y reproducción, no un generador de escenas ni un editor de montaje completo.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-12-edicion.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Edición, grabación y subtítulos», lee `docs/alexandria/categoria-12-edicion.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-12-edicion.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
