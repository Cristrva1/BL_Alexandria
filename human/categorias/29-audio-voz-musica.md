[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Audio, transcripción, voz y música

Transcripción, síntesis, clonación de voz, agentes de audio y música. Compara idioma, latencia, procesamiento local y servicios externos según la tarea concreta.

25 repos · 5 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [whisper.cpp](../fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | Sin clave propia de API de IA en la ruta básica |
| [Kokoro](../fichas/kokoro.md) | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. | Sin clave propia de API de IA en la ruta básica |
| [Pipecat](../fichas/pipecat.md) | Framework open source para agentes de voz y apps multimodales en tiempo real. | API de IA opcional |
| [AudioCraft](../fichas/audiocraft.md) | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Transcripción (voz a texto)](#transcripción-voz-a-texto) — 5 repos
- [Síntesis y clonación de voz](#síntesis-y-clonación-de-voz) — 11 repos
- [Agentes de voz en tiempo real](#agentes-de-voz-en-tiempo-real) — 3 repos
- [Música y audio generativo](#música-y-audio-generativo) — 3 repos
- [Procesamiento y limpieza de audio](#procesamiento-y-limpieza-de-audio) — 3 repos

## Transcripción (voz a texto)

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [whisper.cpp](../fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | Tu objetivo encaja con estos ejemplos: Transcribir una nota offline; Preparar texto base para subtítulos | Sin clave propia de API de IA en la ruta básica |
| [whisper](../fichas/whisper.md) | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. | Tu objetivo encaja con estos ejemplos: Preparar una transcripción local; Traducir habla al inglés como borrador | Sin clave propia de API de IA en la ruta básica |
| [faster-whisper](../fichas/faster-whisper.md) | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. | Tu objetivo encaja con estos ejemplos: Transcribir lotes pequeños; Comparar CPU con GPU | Sin clave propia de API de IA en la ruta básica |
| [whisperX](../fichas/whisperx.md) | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. | Tu objetivo encaja con estos ejemplos: Preparar subtítulos por palabra; Separar intervenciones de una entrevista | Sin clave propia de API de IA en la ruta básica |
| [NeMo Speech](../fichas/nemo.md) | Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con recetas de inferencia y entrenamiento. | Tu objetivo encaja con estos ejemplos: Estudiar modelos de voz de NVIDIA; Preparar un experimento ASR | Sin clave propia de API de IA en la ruta básica |

## Síntesis y clonación de voz

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Kokoro](../fichas/kokoro.md) | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. | Tu objetivo encaja con estos ejemplos: Narrar una nota propia; Probar una voz para una demo | Sin clave propia de API de IA en la ruta básica |
| [VoiceStudio](../fichas/omnivoice-studio.md) | App local de voz con modelos descargables,edición AGPL y una oferta comercial separada. | Tu objetivo encaja con estos ejemplos: Preparar una narración local; Probar transcripción o doblaje de material propio | Sin clave propia de API de IA en la ruta básica |
| [GPT-SoVITS](../fichas/gpt-sovits.md) | Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y datos. | Tu objetivo encaja con estos ejemplos: Prototipar una voz para contenido propio; Estudiar adaptación con pocos ejemplos | Sin clave propia de API de IA en la ruta básica |
| [VibeVoice](../fichas/vibevoice.md) | Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio. | Tu objetivo encaja con estos ejemplos: Estudiar transcripción por hablantes; Probar generación de voz | Sin clave propia de API de IA en la ruta básica |
| [VoxCPM](../fichas/voxcpm.md) | VoxCPM2: modelos y herramientas locales de TTS multilingüe,diseño y adaptación de voz. | Tu objetivo encaja con estos ejemplos: Preparar narración local; Explorar diseño de voz consentido | Sin clave propia de API de IA en la ruta básica |
| [RVC WebUI](../fichas/rvc.md) | Interfaz y herramientas para convertir una grabación a otra voz mediante modelos locales. | Tu objetivo encaja con estos ejemplos: Probar un efecto de voz consentido; Estudiar conversión frente a TTS | Sin clave propia de API de IA en la ruta básica |
| [Fish Speech](../fichas/fish-speech.md) | Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante. | Tu objetivo encaja con estos ejemplos: Estudiar generación expresiva; Preparar una prueba de voz multilingüe | Sin clave propia de API de IA en la ruta básica |
| [IndexTTS](../fichas/index-tts.md) | Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. | Tu objetivo encaja con estos ejemplos: Prototipar narración con duración controlada; Estudiar expresión de voz | Sin clave propia de API de IA en la ruta básica |
| [CosyVoice](../fichas/cosyvoice.md) | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. | Tu objetivo encaja con estos ejemplos: Explorar síntesis multilingüe; Estudiar streaming de voz | Sin clave propia de API de IA en la ruta básica |
| [edge-tts](../fichas/edge-tts.md) | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. | Tu objetivo encaja con estos ejemplos: Preparar una voz de prueba online; Explorar voces disponibles | Sin clave propia de API de IA en la ruta básica |
| [LuxTTS](../fichas/luxtts.md) | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. | Tu objetivo encaja con estos ejemplos: Preparar una narración local; Explorar adaptación de voz consentida | Sin clave propia de API de IA en la ruta básica |

## Agentes de voz en tiempo real

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Pipecat](../fichas/pipecat.md) | Framework open source para agentes de voz y apps multimodales en tiempo real. | Tu objetivo encaja con estos ejemplos: Prototipar un agente de voz; Comparar combinaciones STT/LLM/TTS | API de IA opcional |
| [LiveKit Agents](../fichas/livekit-agents.md) | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. | Tu objetivo encaja con estos ejemplos: Construir un asistente de voz; Evaluar conversación en tiempo real | API de IA opcional |
| [dograh](../fichas/dograh.md) | Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables. | Tu objetivo encaja con estos ejemplos: Diseñar un agente de voz; Editar un workflow mediante MCP | Depende de la ruta elegida |

## Música y audio generativo

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [AudioCraft](../fichas/audiocraft.md) | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | Tu objetivo encaja con estos ejemplos: Explorar generación de música; Estudiar sonidos a partir de texto | Sin clave propia de API de IA en la ruta básica |
| [ACE-Step-1.5](../fichas/ace-step-1-5.md) | Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. | Tu objetivo encaja con estos ejemplos: Explorar una base musical de prueba; Comparar variantes de generación local | Sin clave propia de API de IA en la ruta básica |
| [Music-Megathread](../fichas/music-megathread.md) | Directorio de reproductores, herramientas, servicios y otros recursos relacionados con música. | Tu objetivo encaja con estos ejemplos: Encontrar un reproductor; Explorar herramientas de audio | Sin clave propia de API de IA en la ruta básica |

## Procesamiento y limpieza de audio

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [rnnoise](../fichas/rnnoise.md) | Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente. | Tu objetivo encaja con estos ejemplos: Reducir ruido de una grabación; Estudiar una red de supresión de ruido | Sin clave propia de API de IA en la ruta básica |
| [earshot](../fichas/earshot.md) | Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP. | Tu objetivo encaja con estos ejemplos: Revisar una mezcla con un agente; Analizar un efecto sonoro | API de IA opcional |
| [rubberband](../fichas/rubberband.md) | Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas. | Tu objetivo encaja con estos ejemplos: Ajustar duración de una narración; Explorar cambio de tono | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.
- [Agente de voz en tiempo real](../playbooks/agente-de-voz.md) — Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
