# Alexandría para agentes · Editar, grabar y generar video

Categoría 12 completa (22 repos, 2 subcategorías). Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=12 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `ffmpeg` | edicion | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio… | 2 Intermedio | 70 | LGPL-2.1-or-later (partes opcionales GPL-2.0-or-later) (OSI copyleft) | sin grupo |
| `obs-studio` | edicion | App de escritorio libre para grabar pantalla y transmitir en directo, con… | 1 Básico | 69 | GPL-2.0 (OSI copyleft) | sin grupo |
| `cap` | edicion | Graba pantalla, cámara y micrófono, edita el video en tu equipo con fondos… | 1 Básico | 68 | AGPL-3.0 (partes MIT) (open-core) | sin grupo |
| `videolingo` | edicion | App para reconocer voz, traducir subtítulos y preparar doblaje, con ASR local… | 2 Intermedio | 65 | Apache-2.0 (OSI permisiva) | sin grupo |
| `lossless-cut` | edicion | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en… | 1 Básico | 63 | GPL-2.0 (OSI copyleft) | sin grupo |
| `opencut` | edicion | Editor de video abierto cuya versión clásica puede probarse en la web mientras… | 2 Intermedio | 63 | MIT (OSI permisiva) | recomendado |
| `concat` | edicion | Editor de video local con interfaz y mecanismos de automatización mediante… | 2 Intermedio | 62 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `handbrake` | edicion | Transcodificador de vídeo libre para Linux, macOS y Windows con interfaz… | 1 Básico | 60 | GPL-2.0 (OSI copyleft) | sin grupo |
| `shotcut` | edicion | Editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de… | 1 Básico | 60 | GPL-3.0 (OSI copyleft) | alternativa |
| `davinci-resolve-mcp` | edicion | Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje… | 2 Intermedio | 59 | MIT (OSI permisiva) | sin grupo |
| `kdenlive` | edicion | Editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos… | 1 Básico | 59 | GPL-3.0 (OSI copyleft) | alternativa |
| `pysubs2` | edicion | Convierte formatos de subtítulos y ajusta sus tiempos en lote desde Python o la… | 2 Intermedio | 50 | MIT (OSI permisiva) | sin grupo |
| `libass` | edicion | Dibuja subtítulos ASS y SSA con estilos, posiciones y tiempos en programas de… | 3 Avanzado | 47 | ISC (OSI permisiva) | sin grupo |
| `openrv` | edicion | Reproductor de revisión de video y secuencias de imágenes para comparar tomas y… | 1 Básico | 47 | Apache-2.0 (OSI permisiva) | sin grupo |
| `moneyprinterturbo` | generativo | App que genera videos cortos a partir de un tema: guion con LLM, material de… | 2 Intermedio | 74 | MIT (OSI permisiva) | recomendado |
| `ltx-2` | generativo | Código oficial de inferencia y entrenamiento LoRA de LTX-2 y LTX-2.5, modelo… | 3 Avanzado | 68 | Apache-2.0 (OSI permisiva) | sin grupo |
| `wan2-2` | generativo | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o… | 3 Avanzado | 67 | Apache-2.0 (OSI permisiva) | recomendado |
| `hunyuanvideo` | generativo | Modelo abierto de Tencent de 13B parámetros para generar video a partir de… | 3 Avanzado | 57 | Tencent Hunyuan Community License (source-available) | alternativa |
| `wan2gp` | generativo | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan… | 3 Avanzado | 53 | WanGP Community License 2.0 (no OSI) (source-available) | sin grupo |
| `ai-youtube-shorts-generator` | generativo | Pipeline de Python que extrae clips verticales de videos de YouTube mediante… | 2 Intermedio | 48 | MIT (OSI permisiva) | sin grupo |
| `short-video-factory` | generativo | Aplicación de escritorio para crear videos cortos de producto combinando guion… | 2 Intermedio | 47 | AGPL-3.0 (OSI copyleft) | alternativa |
| `hunyuanvideo-1-5` | generativo | Modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o… | 3 Avanzado | 42 | Tencent Hunyuan Community License (source-available) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### FFmpeg (`ffmpeg`)

- **Repo:** https://github.com/FFmpeg/FFmpeg · LGPL-2.1-or-later (partes opcionales GPL-2.0-or-later) · nivel 2 · 70/100
- **Qué es:** FFmpeg, conjunto de librerías y herramientas para procesar contenido multimedia. Licencia mayoritariamente LGPL con componentes opcionales GPL (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Convertir un video para una plataforma; Extraer audio de una grabación propia.
- **Requisitos:** nivel 2: instalación simple, pero se usa con opciones de línea de comandos; Binario apropiado al sistema; archivo de video propio; espacio de salida; hardware prerequisites; API de IA: no; Binario apropiado al sistema; archivo de video propio; espacio de salida.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://ffmpeg.org/download.html
- **Primera prueba propuesta (no ejecutada):** Convierte una copia de un video breve y comprueba duración, audio y formato con ffprobe Éxito: La salida se reproduce y conserva las pistas esperadas
- **Combina con:** `whisper` [29/stt], `yt-dlp` [4/social], `moviepy` [30/motores]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Al distribuir binarios, revisa si incluyen componentes GPL o códecs con patentes. Descarga un build para tu sistema o sigue la compilación; el repositorio GitHub es un espejo de la fuente oficial.

### OBS Studio (`obs-studio`)

- **Repo:** https://github.com/obsproject/obs-studio · GPL-2.0 · nivel 1 · 69/100
- **Qué es:** OBS Studio, software libre para grabar y transmitir vídeo en directo. Licencia GPL-2.0 o posterior. Es muy maduro (~80k estrellas, 33.0.1).
- **Cuándo elegirlo:** Casos: Grabar una explicación de pantalla; Preparar escenas para una transmisión.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador oficial; permisos de captura; micrófono opcional; disco; hardware prerequisites; API de IA: no; Instalador oficial; permisos de captura; micrófono opcional; disco.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://obsproject.com/download
- **Primera prueba propuesta (no ejecutada):** Crea una escena con pantalla y micrófono y graba veinte segundos Éxito: El archivo tiene imagen, audio y niveles aceptables
- **Combina con:** `lossless-cut`, `opencut`, `faster-whisper` [29/stt], `rnnoise` [29/audio], `deep-live-cam` [28/rostros], `rvc` [29/tts]
- **Alternativas:** `cap`
- **Riesgos y avisos:** Sin alternativas declaradas. Prueba el archivo antes de una sesión larga; seleccionar una fuente no acredita que capture el audio deseado.

### Cap (`cap`)

- **Repo:** https://github.com/CapSoftware/Cap · AGPL-3.0 (partes MIT) · nivel 1 · 68/100
- **Qué es:** App de escritorio de código abierto para grabar la pantalla y compartir los videos, pensada como alternativa a Loom.
- **Cuándo elegirlo:** Casos: Grabar un tutorial corto sobre una hoja de cálculo propia y exportarlo en MP4; Mostrar a un compañero cómo aparece un fallo en tu propia aplicación con una grabación editada. Evítalo si necesitas transmitir en directo con escenas y varias fuentes, o vas a grabar para un uso comercial sin pagar la licencia.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml, docker-compose.yml, package.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/CapSoftware/Cap/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** En el modo Studio, sin iniciar sesión, graba 15 segundos de una ventana con un documento de prueba propio mientras dices una frase al micrófono Éxito: Al detener la grabación se abre el editor. Exporta a MP4, abre el archivo en tu reproductor y comprueba que se ve la…
- **Combina con:** `ffmpeg`, `lossless-cut`, `handbrake`
- **Alternativas:** `obs-studio`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### VideoLingo (`videolingo`)

- **Repo:** https://github.com/Huanshere/VideoLingo · Apache-2.0 · nivel 2 · 65/100
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

### LosslessCut (`lossless-cut`)

- **Repo:** https://github.com/mifi/lossless-cut · GPL-2.0 · nivel 1 · 63/100
- **Qué es:** LosslessCut, app de escritorio para editar vídeo y audio sin pérdida mediante FFmpeg, de @mifi. Licencia GPL-2.0. Es madura (~46k estrellas, v3.70.2) y la mantiene una sola persona.
- **Cuándo elegirlo:** Casos: Quitar una parte de una grabación; Separar o unir medios compatibles.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Distribución para tu sistema; archivo compatible; espacio de salida; hardware prerequisites; API de IA: no; Distribución para tu sistema; archivo compatible; espacio de salida.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://losslesscut.app/docs/getting-started
- **Primera prueba propuesta (no ejecutada):** Marca dos puntos de un video propio y exporta el segmento sin recodificar Éxito: Compruebas duración, comienzo, final y pistas del clip
- **Combina con:** `ffmpeg`, `yt-dlp` [4/social], `whisperx` [29/stt], `moviepy` [30/motores], `obs-studio`, `opencut`
- **Riesgos y avisos:** Sin alternativas declaradas. Descarga solo desde las fuentes oficiales. Los cortes sin recodificar dependen de fotogramas clave y del contenedor; no prometas precisión idéntica a un render completo.

### OpenCut (`opencut`)

- **Repo:** https://github.com/OpenCut-app/OpenCut · MIT · nivel 2 · 63/100 · recomendado en «Editores de video»
- **Qué es:** OpenCut, editor de vídeo libre para web, escritorio y móvil. Licencia MIT. Es muy popular (~99k estrellas, v0.3.0) y se está reescribiendo desde cero.
- **Cuándo elegirlo:** Casos: Evaluar una alternativa de edición abierta; Estudiar la arquitectura de un editor con plugins.
- **Requisitos:** nivel 2: preparación media, app o instalador listo para usar; Navegador para versión clásica o herramientas de la nueva rama; clip de prueba; hardware prerequisites; API de IA: no; Navegador para versión clásica o herramientas de la nueva rama; clip de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OpenCut-app/OpenCut/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Prueba un corte corto en la versión disponible y revisa qué funciones pertenecen a la reescritura Éxito: Puedes exportar o identificar con claridad qué parte aún no está disponible
- **Combina con:** `lossless-cut`, `obs-studio`, `whisperx` [29/stt]
- **Alternativas:** `shotcut`, `kdenlive`
- **Riesgos y avisos:** Sin alternativas declaradas. En reescritura: el código del repo principal aún no es un editor utilizable. El proyecto se reescribe; la versión clásica web y la rama principal no tienen necesariamente las mismas funciones ni instalación.

### Concat (`concat`)

- **Repo:** https://github.com/jub0t/Concat · AGPL-3.0 · nivel 2 · 62/100
- **Qué es:** Concat, editor de vídeo libre y multiplataforma, de @jub0t. Licencia AGPL-3.0 o posterior, con licencia comercial disponible. Es reciente (~18k estrellas, v0.2.11).
- **Cuándo elegirlo:** Casos: Editar un video sin subir el material; Automatizar una variante de montaje mediante MCP.
- **Requisitos:** nivel 2: preparación media; Distribución compatible; clip propio; modelos opcionales descargados; permisos de automatización para MCP; hardware prerequisites; API de IA: no; Distribución compatible; clip propio; modelos opcionales descargados; permisos de automatización para MCP.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/jub0t/Concat/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Recorta una copia de un clip y añade subtítulos locales antes de exportar Éxito: Puedes revisar texto, puntos de corte y archivo final
- **Combina con:** `claude-code` [20/terminal], `ffmpeg`, `yt-dlp` [4/social]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Está en beta; MCP puede usar la ventana o un proceso separado y sus modos tienen límites distintos al editar el mismo proyecto.

### HandBrake (`handbrake`)

- **Repo:** https://github.com/HandBrake/HandBrake · GPL-2.0 · nivel 1 · 60/100
- **Qué es:** Transcodificador de vídeo de código abierto (GPL-2.0 en la mayoría de archivos) mantenido por el HandBrake Team desde 2003. Muy maduro.
- **Cuándo elegirlo:** Casos: convertir grabaciones de cámara o pantalla a MP4 compatibles con móviles y webs; reducir el tamaño de una videoteca manteniendo la calidad.
- **Requisitos:** nivel 1: app de escritorio con instalador para Windows, macOS y Linux; C; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/HandBrake/HandBrake/blob/master/README.markdown
- **Primera prueba propuesta (no ejecutada):** Instala HandBrake, abre un vídeo corto y conviértelo con un preset de 1080p. Éxito: Obtienes un MP4 reproducible en el móvil con menor tamaño que el original.
- **Combina con:** `ffmpeg`, `obs-studio`, `lossless-cut`, `jellyfin` [15/lectura]
- **Riesgos y avisos:** No elimina protecciones anticopia; respeta los derechos del material que conviertes.

### Shotcut (`shotcut`)

- **Repo:** https://github.com/mltframework/shotcut · GPL-3.0 · nivel 1 · 60/100 · alternativa en «Editores de video»
- **Qué es:** Editor de vídeo de código abierto (GPL-3.0) cuyo autor principal es Dan Dennedy, también mantenedor de MLT. Maduro, con versiones regulares para Windows, macOS y Linux.
- **Cuándo elegirlo:** Casos: editar vídeos de YouTube o cursos con cortes, transiciones y títulos; generar subtítulos automáticos a partir del audio de un vídeo.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; C++, CMakeLists.txt; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mltframework/shotcut/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Shotcut desde shotcut.org, importa dos clips, córtalos en la línea de tiempo y exporta un MP4. Éxito: El MP4 exportado reproduce los dos clips con el corte aplicado.
- **Combina con:** `ffmpeg`, `whisper-cpp` [29/stt], `obs-studio`
- **Alternativas:** `opencut`, `kdenlive`
- **Riesgos y avisos:** Alternativas (elige una): kdenlive, opencut.

### DaVinci Resolve MCP (`davinci-resolve-mcp`)

- **Repo:** https://github.com/samuelgursky/davinci-resolve-mcp · MIT · nivel 2 · 59/100
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

### pysubs2 (`pysubs2`)

- **Repo:** https://github.com/tkarabela/pysubs2 · MIT · nivel 2 · 50/100
- **Qué es:** pysubs2 es una biblioteca Python y una utilidad de terminal para transformar archivos de subtítulos.
- **Cuándo elegirlo:** Casos: Convertir un archivo ASS de edición a SRT para compartirlo con un reproductor.; Corregir un desfase constante de los subtítulos en varios clips propios.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; API de IA: no; Python 3.12 o posterior y entorno virtual.; Un archivo de subtítulos de ejemplo..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install pysubs2` — fuente: https://github.com/tkarabela/pysubs2/blob/6371ae8bc2f9fed19aeb51a8e09d920e8bb86ce5/README.md
- **Primera prueba propuesta (no ejecutada):** Convierte una copia de un ASS de dos líneas a SRT siguiendo el ejemplo del README fijado. Éxito: Abre el SRT y comprueba que conserva las dos líneas y sus tiempos.

### libass (`libass`)

- **Repo:** https://github.com/libass/libass · ISC · nivel 3 · 47/100
- **Qué es:** Biblioteca en C para renderizar subtítulos con formato ASS y SSA.
- **Cuándo elegirlo:** Necesitas dibujar subtítulos ASS o SSA con estilos y posiciones desde una biblioteca o una integración. Evítalo si Prefieres editar o sincronizar subtítulos desde una interfaz gráfica.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él; C; API de IA: no; Linux y terminal; Compilador C, make y pkg-config; Bibliotecas de desarrollo FreeType, FriBidi, HarfBuzz y libpng; Un ASS propio con un subtítulo activo durante el segundo 1.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/libass/libass/releases/tag/0.17.5
- **Primera prueba propuesta (no ejecutada):** En una compilación Autotools con el programa de prueba habilitado, ejecuta ./test/test subtitulo.png muestra.ass 1.0 con una línea ASS propia activa durante el segundo 1 Éxito: Abre subtitulo.png. La imagen muestra el texto con el estilo del archivo y la línea original se conserva
- **Combina con:** `ffmpeg`, `pysubs2`

### OpenRV (`openrv`)

- **Repo:** https://github.com/AcademySoftwareFoundation/OpenRV · Apache-2.0 · nivel 1 · 47/100
- **Qué es:** Open RV, visor de imágenes y secuencias para artistas de VFX y animación, de la Academy Software Foundation. Licencia Apache-2.0 con componentes bajo otras licencias (GitHub muestra NOASSERTION). Tiene ~800 estrellas (v4.0.2).
- **Cuándo elegirlo:** Casos: Revisar una entrega de animación; Comparar versiones de un efecto visual.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Build compatible o herramientas de compilación; secuencia o video de prueba; hardware prerequisites; API de IA: no; Build compatible o herramientas de compilación; secuencia o video de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --recursive https://github.com/AcademySoftwareFoundation/OpenRV.git` — fuente: https://github.com/AcademySoftwareFoundation/OpenRV/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre dos versiones de una toma y compara fotogramas en el mismo punto Éxito: Puedes observar diferencias de imagen sin desalinear el tiempo
- **Combina con:** `blender` [26/creacion-3d], `ffmpeg`, `comfyui` [11/interfaces]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Es una herramienta de revisión y reproducción, no un generador de escenas ni un editor de montaje completo.

### MoneyPrinterTurbo (`moneyprinterturbo`)

- **Repo:** https://github.com/harry0703/MoneyPrinterTurbo · MIT · nivel 2 · 74/100 · recomendado en «Generación automática de videos cortos»
- **Qué es:** MoneyPrinterTurbo, app para generar vídeos cortos a partir de un tema o palabra clave, de @harry0703. Licencia MIT. Es muy popular (~144k estrellas, v1.3.10) y su README está lleno de patrocinios y enlaces de afiliado a proveedores de…
- **Cuándo elegirlo:** Casos: Preparar un borrador de video de producto; Generar variantes de un tutorial propio.
- **Requisitos:** nivel 2: preparación media; Python; FFmpeg; proveedores de guion, voz e imágenes; material propio o autorizado; hardware prerequisites; API de IA: depends; Python; FFmpeg; proveedores de guion, voz e imágenes; material propio o autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md

  ```shell
  python -m pip install mpt
  mpt webui
  ```
- **Primera prueba propuesta (no ejecutada):** Crea un video corto de prueba con un guion revisado y comprueba voz, clips y subtítulos Éxito: Puedes rastrear el origen de cada recurso y corregir el resultado
- **Combina con:** `faster-whisper` [29/stt], `kokoro` [29/tts], `ollama` [8/motores]
- **Alternativas:** `short-video-factory`, `openmontage`, `videofy-minimal`
- **Riesgos y avisos:** Alternativas (elige una): openmontage, videofy-minimal, short-video-factory. Revisa los derechos del material de stock y de las voces antes de publicar. El adaptador Codex es del proyecto y no instala el CLI ni promete cobertura de cualquier modelo o cuenta; la imagen local no vuelve local todo el flujo.

### LTX-2 (`ltx-2`)

- **Repo:** https://github.com/Lightricks/LTX-2 · Apache-2.0 · nivel 3 · 68/100
- **Qué es:** Paquete oficial de inferencia y entrenador LoRA de Lightricks para el modelo audio-vídeo LTX-2, que alberga también LTX-2.5. El código es Apache-2.0 y los modelos tienen licencias propias.
- **Cuándo elegirlo:** Casos: generar clips cortos con audio a partir de texto o una imagen en una GPU propia; entrenar un LoRA de estilo o personaje para el modelo. Evítalo si no tienes el hardware o no aceptas la licencia de los pesos.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/Lightricks/LTX-2.git` — fuente: https://github.com/Lightricks/LTX-2/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio, instala las dependencias, descarga los pesos de LTX-2.5 y ejecuta la DistilledPipeline con un prompt corto. Éxito: Se genera un clip de vídeo con audio en la carpeta de salida sin agotar la VRAM.
- **Combina con:** `comfyui` [11/interfaces], `ffmpeg` [12/edicion], `pytorch` [24/entrenamiento]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Revisa las licencias de los pesos antes de uso comercial.

### Wan2.2 (`wan2-2`)

- **Repo:** https://github.com/Wan-Video/Wan2.2 · Apache-2.0 · nivel 3 · 67/100 · recomendado en «Modelos abiertos de video generativo»
- **Qué es:** Wan2.2, familia de modelos abiertos de generación de vídeo de Alibaba (Wan-AI). Licencia Apache-2.0 para los modelos; no reclaman derechos sobre el contenido generado.
- **Cuándo elegirlo:** Casos: Prototipar una escena desde texto; Animar una imagen propia con un modelo local.
- **Requisitos:** nivel 3: preparación pesada; Python y PyTorch >=2.4; GPU; pesos y disco según variante; hardware prerequisites; API de IA: opcional; Python y PyTorch >=2.4; GPU; pesos y disco según variante.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Wan-Video/Wan2.2/blob/main/README.md

  ```sh
  git clone https://github.com/Wan-Video/Wan2.2.git
  cd Wan2.2

  # Ensure torch >= 2.4.0
  # If the installation of `flash_attn` fails, try installing the other packages first and install `flash_attn` last
  pip install -r requirements.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Elige primero el modelo TI2V-5B y la ruta de memoria documentada y genera un clip breve Éxito: Puedes identificar pesos, tamaño, duración y recursos de la ejecución
- **Combina con:** `comfyui` [11/interfaces], `diffusers` [11/modelos], `cosyvoice` [29/tts], `real-esrgan` [11/edicion], `wan2gp`
- **Alternativas:** `hunyuanvideo`, `hunyuanvideo-1-5`
- **Riesgos y avisos:** Alternativas (elige una): hunyuanvideo, hunyuanvideo-1-5. El ejemplo 5B cita al menos 24 GB VRAM; otros ejemplos 14B citan 80 GB; no extrapoles esos mínimos a interfaces optimizadas de terceros.

### HunyuanVideo (`hunyuanvideo`)

- **Repo:** https://github.com/Tencent-Hunyuan/HunyuanVideo · Tencent Hunyuan Community License · nivel 3 · 57/100 · alternativa en «Modelos abiertos de video generativo»
- **Qué es:** HunyuanVideo, modelo abierto de generación de vídeo de 13B parámetros de Tencent Hunyuan. Usa la Tencent Hunyuan Community License, que excluye expresamente la UE, Reino Unido y Corea del Sur (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Estudiar generación local de video; Probar un prompt visual con pesos abiertos.
- **Requisitos:** nivel 3: preparación pesada; Python 3.10.9 y PyTorch según ruta; GPU grande; pesos y licencia; hardware prerequisites; API de IA: no; Python 3.10.9 y PyTorch según ruta; GPU grande; pesos y licencia.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull hunyuanvideo/hunyuanvideo:cuda_12` — fuente: https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Comprueba la resolución y memoria de la tabla antes de generar el ejemplo más pequeño viable Éxito: El clip y sus recursos se pueden comparar con la configuración elegida
- **Combina con:** `diffusers` [11/modelos], `comfyui` [11/interfaces], `wan2gp`
- **Alternativas:** `wan2-2`, `hunyuanvideo-1-5`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): wan2-2, hunyuanvideo-1-5. La licencia no aplica en la UE, Reino Unido ni Corea del Sur; para proyectos nuevos valora HunyuanVideo-1.5. La ruta original cita 45 GB VRAM para 544x960x129 y 60 GB para 720x1280x129; no es una instalación ligera para cualquier laptop.

### WanGP (`wan2gp`)

- **Repo:** https://github.com/deepbeepmeep/WanGP · WanGP Community License 2.0 (no OSI) · nivel 3 · 53/100
- **Qué es:** WanGP, superapp local para modelos generativos abiertos «para GPU modestas», de @deepbeepmeep. Usa la WanGP Community License 2.0, propia (GitHub muestra NOASSERTION), y es gratuita para uso local, también en el trabajo.
- **Cuándo elegirlo:** Casos: Probar varios modelos desde una interfaz; Preparar clips locales con una GPU limitada.
- **Requisitos:** nivel 3: preparación pesada; GPU compatible; Python y PyTorch según guía; pesos del modelo elegido; hardware prerequisites; API de IA: opcional; GPU compatible; Python y PyTorch según guía; pesos del modelo elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/deepbeepmeep/WanGP.git` — fuente: https://github.com/deepbeepmeep/WanGP/blob/main/docs/GETTING_STARTED.md
- **Primera prueba propuesta (no ejecutada):** Elige un modelo pequeño admitido y genera un clip corto antes de activar Deepy o Showrunner Éxito: Puedes comprobar memoria, duración y motor de cada tarea
- **Combina con:** `claude-code` [20/terminal], `wan2-2`, `moviepy` [30/motores], `lossless-cut` [12/edicion], `hunyuanvideo-1-5`, `hunyuanvideo`
- **Alternativas:** `comfyui`
- **Riesgos y avisos:** Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): comfyui. Licencia propia, no OSI: revísala antes de redistribuir. Documenta Claude Code y Codex como proveedores remotos auxiliares; que algunos modelos quepan en 4 GB no garantiza que todos lo hagan.

### AI-Youtube-Shorts-Generator (`ai-youtube-shorts-generator`)

- **Repo:** https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator · MIT · nivel 2 · 48/100
- **Qué es:** AI YouTube Shorts Generator, pipeline en Python para extraer clips verticales de vídeos largos de YouTube, de @Anil-matcha. Licencia MIT. Tiene ~6k estrellas (sin releases) y lo «impulsa» MuAPI, cuyas APIs de pago se promocionan en el…
- **Cuándo elegirlo:** Casos: Obtener clips de un tutorial propio; Comparar criterios de selección de momentos.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Python; FFmpeg y dependencias locales si eliges ese modo; clave LLM; video autorizado; hardware prerequisites; API de IA: sí; Python; FFmpeg y dependencias locales si eliges ese modo; clave LLM; video autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/main/README.md

  ```bash
  git clone https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator.git
     cd AI-Youtube-Shorts-Generator

  pip install -r requirements.txt
     # Only if you plan to use --mode local:
     pip install -r requirements-local.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Procesa un video propio corto y revisa los fragmentos propuestos antes de exportar Éxito: Puedes corregir puntos de corte, subtítulos y encuadre
- **Combina con:** `faster-whisper` [29/stt], `yt-dlp` [4/social], `ffmpeg` [12/edicion]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Respeta los derechos de autor y los términos de YouTube al reutilizar vídeos ajenos. Local no significa todo offline; las puntuaciones de viralidad son heurísticas del proyecto y no predicen vistas.

### short-video-factory (`short-video-factory`)

- **Repo:** https://github.com/YILS-LIN/short-video-factory · AGPL-3.0 · nivel 2 · 47/100 · alternativa en «Generación automática de videos cortos»
- **Qué es:** Short Video Factory (短视频工厂), app de escritorio para crear vídeos cortos de producto y contenido general, de @YILS-LIN. Licencia AGPL-3.0. Tiene ~6k estrellas (v1.4.0) y su README está principalmente en chino.
- **Cuándo elegirlo:** Casos: Crear un borrador de producto; Preparar variantes de un anuncio propio.
- **Requisitos:** nivel 2: preparación media; App de escritorio; proveedores de guion y voz; clips e imágenes propios; hardware prerequisites; API de IA: depends; App de escritorio; proveedores de guion y voz; clips e imágenes propios.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/YILS-LIN/short-video-factory/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Monta un borrador corto con un texto y tres clips ficticios o propios y revisa cada escena Éxito: El video exportado coincide con guion, voz y subtítulos corregidos
- **Combina con:** `edge-tts` [29/tts], `ffmpeg` [12/edicion], `ollama` [8/motores]
- **Alternativas:** `moneyprinterturbo`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativa (elige una): moneyprinterturbo. No se confirma aquí una ruta completamente local ni que la suscripción de un agente pague las funciones de generación.

### HunyuanVideo 1.5 (`hunyuanvideo-1-5`)

- **Repo:** https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5 · Tencent Hunyuan Community License · nivel 3 · 42/100 · alternativa en «Modelos abiertos de video generativo»
- **Qué es:** Modelo de generación de video de Tencent Hunyuan, publicado en noviembre de 2025 con código de inferencia y entrenamiento en Python. Usa la Tencent Hunyuan Community License (GitHub muestra NOASSERTION), que no se aplica en la UE, el Reino…
- **Cuándo elegirlo:** Casos: Generar un clip corto desde texto con GPU de consumo; Animar una imagen fija en 480p. Evítalo si no tienes una GPU NVIDIA con memoria suficiente o te afecta la exclusión territorial de la licencia.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python, requirements.txt; hardware gpu; API de IA: opcional; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5.git` — fuente: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera un clip de pocos segundos en 480p con offloading activado Éxito: El video se guarda y anotas tiempo y VRAM usados
- **Combina con:** `comfyui` [11/interfaces], `wan2gp`, `vllm` [23/serving]
- **Alternativas:** `wan2-2`, `hunyuanvideo`
- **Riesgos y avisos:** Alternativas (elige una): hunyuanvideo, wan2-2. Revisa la exclusión territorial y la política de uso aceptable antes de usarlo en un producto.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-12.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Editar, grabar y generar video», lee `docs/alexandria/categoria-12.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-12.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
