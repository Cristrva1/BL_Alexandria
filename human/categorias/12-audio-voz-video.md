[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Editar, grabar y generar video

Editores, grabadores, utilidades de medios y modelos de video generativo. La edición de material existente y la generación de nuevas escenas tienen requisitos distintos.

21 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [FFmpeg](../fichas/ffmpeg.md) | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | Sin API de IA en la ruta básica |
| [MoviePy](../fichas/moviepy.md) | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. | Sin API de IA en la ruta básica |
| [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. | Depende de la ruta elegida |
| [Wan2.2](../fichas/wan2-2.md) | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. | Sin API de IA en la ruta básica |

## Secciones

- [Edición, grabación y subtítulos](#edición-grabación-y-subtítulos) — 13 repos
- [Video generativo y pipelines automáticos](#video-generativo-y-pipelines-automáticos) — 8 repos

## Edición, grabación y subtítulos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [FFmpeg](../fichas/ffmpeg.md) | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | necesitas convertir, cortar, mezclar o transmitir audio y video desde la línea de comandos o un script | Sin API de IA en la ruta básica |
| [MoviePy](../fichas/moviepy.md) | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. | ensamblas video desde Python y quieres controlar cada clip por código | Sin API de IA en la ruta básica |
| [OpenCut](../fichas/opencut.md) | Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. | quieres un editor con línea de tiempo, libre y privado, como alternativa a CapCut | Sin API de IA en la ruta básica |
| [OBS Studio](../fichas/obs-studio.md) | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. | necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas | Sin API de IA en la ruta básica |
| [LosslessCut](../fichas/lossless-cut.md) | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. | necesitas recortar o unir material rápido y sin recomprimir, con interfaz gráfica | Sin API de IA en la ruta básica |
| [OpenScreen](../fichas/openscreen.md) | App de escritorio para grabar demos de producto con zoom automático, webcam y subtítulos, alternativa libre a Screen Studio. | quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio | Sin API de IA en la ruta básica |
| [VideoLingo](../fichas/videolingo.md) | App que subtitula, traduce y dobla videos de forma automática: ASR con timestamps por palabra, traducción con LLM y TTS. | quieres subtitular, traducir o doblar videos de punta a punta con una interfaz y sin programar | Depende de la ruta elegida |
| [Concat](../fichas/concat.md) | Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP. | buscas esta función: Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP. | Sin API de IA en la ruta básica |
| [palmier-pro](../fichas/palmier-pro.md) | Editor de video para macOS con herramientas de IA y MCP cuyo repositorio conserva código histórico y binarios actuales. | usas macOS y quieres explorar edición de video asistida por agentes | Depende de la ruta elegida |
| [mediabunny](../fichas/mediabunny.md) | Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones web. | buscas esta función: Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones web. | Sin API de IA en la ruta básica |
| [DaVinci Resolve MCP](../fichas/davinci-resolve-mcp.md) | Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render. | editas en DaVinci Resolve y quieres que un agente MCP automatice montaje, render o metadatos | Sin API de IA en la ruta básica |
| [pencil](../fichas/pencil.md) | Aplicación para crear animación 2D dibujada a mano mediante herramientas de dibujo y una línea de tiempo. | buscas esta función: Aplicación para crear animación 2D dibujada a mano mediante herramientas de dibujo y una línea de tiempo. | Sin API de IA en la ruta básica |
| [OpenRV](../fichas/openrv.md) | Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual. | buscas esta función: Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual. | Sin API de IA en la ruta básica |

## Video generativo y pipelines automáticos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. | quieres producir videos cortos narrados a partir de un tema sin editar a mano | Depende de la ruta elegida |
| [Wan2.2](../fichas/wan2-2.md) | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. | quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más | Sin API de IA en la ruta básica |
| [hypit](../fichas/hypit.md) | Skills para agentes que organizan generación y edición de videos mediante modelos, servicios y recursos configurables. | buscas esta función: Skills para agentes que organizan generación y edición de videos mediante modelos, servicios y recursos configurables. | API de IA opcional |
| [HunyuanVideo](../fichas/hunyuanvideo.md) | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. | tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad | Sin API de IA en la ruta básica |
| [WanGP](../fichas/wan2gp.md) | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas. | quieres generar video e imagen con modelos abiertos en una GPU de consumo sin montar flujos a mano | Sin API de IA en la ruta básica |
| [LTX-Video](../fichas/ltx-video.md) | Modelos abiertos de Lightricks (v0.9.x) para generar video desde texto o imagen, rápidos en GPU de consumo; hoy en modo legado. | necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x | Sin API de IA en la ruta básica |
| [short-video-factory](../fichas/short-video-factory.md) | Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. | quieres producir variantes de videos promocionales desde materiales existentes | Depende de la ruta elegida |
| [AI-Youtube-Shorts-Generator](../fichas/ai-youtube-shorts-generator.md) | Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de momentos con LLM. | quieres convertir videos largos en una primera selección de shorts | Depende de la ruta elegida |

## Recetas relacionadas

- [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
