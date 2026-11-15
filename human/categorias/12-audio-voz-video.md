[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Editar, grabar y generar video

Editores, grabadores, utilidades de medios y modelos de video generativo. La edición de material existente y la generación de nuevas escenas tienen requisitos distintos.

17 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [FFmpeg](../fichas/ffmpeg.md) | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | Sin clave propia de API de IA en la ruta básica |
| [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. | Depende de la ruta elegida |
| [Wan2.2](../fichas/wan2-2.md) | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. | API de IA opcional |

## Secciones

- [Edición, grabación y subtítulos](#edición-grabación-y-subtítulos) — 10 repos
- [Video generativo y pipelines automáticos](#video-generativo-y-pipelines-automáticos) — 7 repos

## Edición, grabación y subtítulos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [FFmpeg](../fichas/ffmpeg.md) | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | Tu objetivo encaja con estos ejemplos: Convertir un video para una plataforma; Extraer audio de una grabación propia | Sin clave propia de API de IA en la ruta básica |
| [OpenCut](../fichas/opencut.md) | Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. | Tu objetivo encaja con estos ejemplos: Evaluar una alternativa de edición abierta; Estudiar la arquitectura de un editor con plugins | Sin clave propia de API de IA en la ruta básica |
| [OBS Studio](../fichas/obs-studio.md) | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. | Tu objetivo encaja con estos ejemplos: Grabar una explicación de pantalla; Preparar escenas para una transmisión | Sin clave propia de API de IA en la ruta básica |
| [LosslessCut](../fichas/lossless-cut.md) | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. | Tu objetivo encaja con estos ejemplos: Quitar una parte de una grabación; Separar o unir medios compatibles | Sin clave propia de API de IA en la ruta básica |
| [OpenScreen](../fichas/openscreen.md) | App de escritorio para grabar demos de producto con zoom automático, webcam y subtítulos, alternativa libre a Screen Studio. | Tu objetivo encaja con estos ejemplos: Crear una demostración de producto; Grabar un tutorial con cámara y pantalla | Sin clave propia de API de IA en la ruta básica |
| [VideoLingo](../fichas/videolingo.md) | App para reconocer voz, traducir subtítulos y preparar doblaje, con ASR local por defecto y proveedores configurables por etapa. | Tu objetivo encaja con estos ejemplos: Subtitular un tutorial propio; Preparar una traducción de una demostración | Depende de la ruta elegida |
| [Concat](../fichas/concat.md) | Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP. | Tu objetivo encaja con estos ejemplos: Editar un video sin subir el material; Automatizar una variante de montaje mediante MCP | Sin clave propia de API de IA en la ruta básica |
| [palmier-pro](../fichas/palmier-pro.md) | Editor de video para macOS con herramientas de IA y MCP cuyo repositorio conserva código histórico y binarios actuales. | Tu objetivo encaja con estos ejemplos: Preparar cortes con un agente; Revisar una secuencia desde herramientas externas | API de IA opcional |
| [DaVinci Resolve MCP](../fichas/davinci-resolve-mcp.md) | Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render. | Tu objetivo encaja con estos ejemplos: Organizar material desde un agente; Preparar ajustes de render con revisión | Sin clave propia de API de IA en la ruta básica |
| [OpenRV](../fichas/openrv.md) | Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual. | Tu objetivo encaja con estos ejemplos: Revisar una entrega de animación; Comparar versiones de un efecto visual | Sin clave propia de API de IA en la ruta básica |

## Video generativo y pipelines automáticos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. | Tu objetivo encaja con estos ejemplos: Preparar un borrador de video de producto; Generar variantes de un tutorial propio | Depende de la ruta elegida |
| [Wan2.2](../fichas/wan2-2.md) | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. | Tu objetivo encaja con estos ejemplos: Prototipar una escena desde texto; Animar una imagen propia con un modelo local | API de IA opcional |
| [HunyuanVideo](../fichas/hunyuanvideo.md) | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. | Tu objetivo encaja con estos ejemplos: Estudiar generación local de video; Probar un prompt visual con pesos abiertos | Sin clave propia de API de IA en la ruta básica |
| [WanGP](../fichas/wan2gp.md) | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas. | Tu objetivo encaja con estos ejemplos: Probar varios modelos desde una interfaz; Preparar clips locales con una GPU limitada | API de IA opcional |
| [LTX-Video](../fichas/ltx-video.md) | Modelos abiertos de Lightricks (v0.9.x) para generar video desde texto o imagen, rápidos en GPU de consumo; hoy en modo legado. | Tu objetivo encaja con estos ejemplos: Mantener un flujo LTX-Video existente; Comparar generación desde texto e imagen propios | Sin clave propia de API de IA en la ruta básica |
| [short-video-factory](../fichas/short-video-factory.md) | Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. | Tu objetivo encaja con estos ejemplos: Crear un borrador de producto; Preparar variantes de un anuncio propio | Depende de la ruta elegida |
| [AI-Youtube-Shorts-Generator](../fichas/ai-youtube-shorts-generator.md) | Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de momentos con LLM. | Tu objetivo encaja con estos ejemplos: Obtener clips de un tutorial propio; Comparar criterios de selección de momentos | API de IA necesaria |

## Recetas relacionadas

- [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
