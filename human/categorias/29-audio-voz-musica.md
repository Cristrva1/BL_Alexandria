[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Audio, transcripción, voz y música

Transcripción, síntesis, clonación de voz, agentes de audio y música. Compara idioma, latencia, procesamiento local y servicios externos según la tarea concreta.

34 repos · 5 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [whisper.cpp](../fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | Sin clave propia de API de IA en la ruta básica |
| [Kokoro](../fichas/kokoro.md) | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. | Sin clave propia de API de IA en la ruta básica |
| [Pipecat](../fichas/pipecat.md) | Framework open source para agentes de voz y apps multimodales en tiempo real. | API de IA opcional |
| [AudioCraft](../fichas/audiocraft.md) | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Transcripción (voz a texto)](#transcripción-voz-a-texto) — 7 repos
- [Síntesis y clonación de voz](#síntesis-y-clonación-de-voz) — 13 repos
- [Agentes de voz en tiempo real](#agentes-de-voz-en-tiempo-real) — 4 repos
- [Música y audio generativo](#música-y-audio-generativo) — 3 repos
- [Procesamiento y limpieza de audio](#procesamiento-y-limpieza-de-audio) — 7 repos

## Transcripción (voz a texto)

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [whisper.cpp](../fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | Tu objetivo encaja con estos ejemplos: Transcribir una nota offline; Preparar texto base para subtítulos | Sin clave propia de API de IA en la ruta básica |
| [whisper](../fichas/whisper.md) | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. | Tu objetivo encaja con estos ejemplos: Preparar una transcripción local; Traducir habla al inglés como borrador | Sin clave propia de API de IA en la ruta básica |
| [faster-whisper](../fichas/faster-whisper.md) | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. | Tu objetivo encaja con estos ejemplos: Transcribir lotes pequeños; Comparar CPU con GPU | Sin clave propia de API de IA en la ruta básica |
| [whisperX](../fichas/whisperx.md) | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. | Tu objetivo encaja con estos ejemplos: Preparar subtítulos por palabra; Separar intervenciones de una entrevista | Sin clave propia de API de IA en la ruta básica |
| [Buzz](../fichas/buzz.md) | Transcribe grabaciones y exporta subtítulos en una aplicación de escritorio que puede usar Whisper en tu propio equipo. | Tu objetivo encaja con estos ejemplos: Convertir una nota de voz propia en texto editable.; Crear subtítulos en SRT para una demostración grabada. | API de IA opcional |
| [NeMo Speech](../fichas/nemo.md) | Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con recetas de inferencia y entrenamiento. | Tu objetivo encaja con estos ejemplos: Estudiar modelos de voz de NVIDIA; Preparar un experimento ASR | Sin clave propia de API de IA en la ruta básica |
| [sherpa-onnx](../fichas/sherpa-onnx.md) | Motor de voz offline con ONNX Runtime: reconocimiento, síntesis, VAD, diarización e identificación de hablante en móvil, embebido, escritorio y servidor. | Tu objetivo encaja con estos ejemplos: añadir dictado o transcripción sin conexión a una app Android o iOS; poner reconocimiento y síntesis de voz en una Raspberry Pi sin nube | Sin clave propia de API de IA en la ruta básica |

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
| [F5-TTS](../fichas/f5-tts.md) | Síntesis de voz con clonación a partir de pocos segundos de audio de referencia, basada en flow matching con Diffusion Transformer; incluye app Gradio y CLI. | Tu objetivo encaja con estos ejemplos: generar narración con tu propia voz a partir de una muestra corta; prototipar voces para un proyecto de investigación sin uso comercial | Sin clave propia de API de IA en la ruta básica |
| [edge-tts](../fichas/edge-tts.md) | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. | Tu objetivo encaja con estos ejemplos: Preparar una voz de prueba online; Explorar voces disponibles | Sin clave propia de API de IA en la ruta básica |
| [LuxTTS](../fichas/luxtts.md) | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. | Tu objetivo encaja con estos ejemplos: Preparar una narración local; Explorar adaptación de voz consentida | Sin clave propia de API de IA en la ruta básica |
| [ElevenLabs (SDK de Python)](../fichas/elevenlabs-python.md) | SDK oficial de Python para la API de pago de ElevenLabs: voz sintética, clonación, transcripción, música y agentes de voz. | Tu objetivo encaja con estos ejemplos: Generar una locución para un video; Prototipar un agente de voz conectado a la API | API de IA necesaria |

## Agentes de voz en tiempo real

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Pipecat](../fichas/pipecat.md) | Framework open source para agentes de voz y apps multimodales en tiempo real. | Tu objetivo encaja con estos ejemplos: Prototipar un agente de voz; Comparar combinaciones STT/LLM/TTS | API de IA opcional |
| [LiveKit Agents](../fichas/livekit-agents.md) | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. | Tu objetivo encaja con estos ejemplos: Construir un asistente de voz; Evaluar conversación en tiempo real | API de IA opcional |
| [TEN Framework](../fichas/ten-framework.md) | Framework para agentes de voz conversacionales en tiempo real, con grafo de extensiones (ASR, LLM, TTS, VAD, turnos), diseñador visual y ejemplos listos. | Tu objetivo encaja con estos ejemplos: montar un asistente de voz que conversa en tiempo real con un LLM; construir un agente de voz con avatar o con transcripción en vivo | API de IA necesaria |
| [dograh](../fichas/dograh.md) | Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables. | Tu objetivo encaja con estos ejemplos: Diseñar un agente de voz; Editar un workflow mediante MCP | Depende de la ruta elegida |

## Música y audio generativo

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [AudioCraft](../fichas/audiocraft.md) | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | Tu objetivo encaja con estos ejemplos: Explorar generación de música; Estudiar sonidos a partir de texto | Sin clave propia de API de IA en la ruta básica |
| [ACE-Step-1.5](../fichas/ace-step-1-5.md) | Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. | Tu objetivo encaja con estos ejemplos: Explorar una base musical de prueba; Comparar variantes de generación local | Sin clave propia de API de IA en la ruta básica |
| [YuE2](../fichas/yue.md) | Modelo abierto de generación de canciones completas (voz y acompañamiento) a partir de letra y estilo, con partitura editable, covers y una skill para agentes. | Tu objetivo encaja con estos ejemplos: generar una maqueta de canción con letra propia para un proyecto personal o académico; editar la armonía de una canción generada manteniendo la melodía | Sin clave propia de API de IA en la ruta básica |

## Procesamiento y limpieza de audio

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Ultimate Vocal Remover (UVR)](../fichas/ultimate-vocal-remover.md) | Aplicación de escritorio para separar voz e instrumentos de canciones con modelos de IA (MDX-Net, VR, Demucs), sin necesidad de programar. | Tu objetivo encaja con estos ejemplos: obtener la pista instrumental o la voz aislada de una canción propia; preparar stems para remezclar o practicar con una canción | Sin clave propia de API de IA en la ruta básica |
| [Audacity](../fichas/audacity.md) | Editor y grabador de audio multipista libre para Windows, macOS y Linux, con efectos, análisis y plugins, incluidos plugins de IA locales de Intel. | Tu objetivo encaja con estos ejemplos: limpiar, cortar y normalizar una grabación de voz o podcast; editar stems separados con IA antes de mezclarlos | Sin clave propia de API de IA en la ruta básica |
| [pyannote.audio](../fichas/pyannote-audio.md) | Kit de PyTorch para diarización de hablantes (quién habla y cuándo) con modelos preentrenados y un servicio premium opcional. | Tu objetivo encaja con estos ejemplos: Separar por hablante la grabación de una reunión; Añadir hablantes a una transcripción | API de IA opcional |
| [rnnoise](../fichas/rnnoise.md) | Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente. | Tu objetivo encaja con estos ejemplos: Reducir ruido de una grabación; Estudiar una red de supresión de ruido | Sin clave propia de API de IA en la ruta básica |
| [earshot](../fichas/earshot.md) | Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP. | Tu objetivo encaja con estos ejemplos: Revisar una mezcla con un agente; Analizar un efecto sonoro | API de IA opcional |
| [Demucs](../fichas/demucs.md) | Modelo de separación de fuentes musicales (voz, batería, bajo y resto) con Hybrid Transformer; continuación mantenida por su autor tras archivarse el repo de Meta. | Tu objetivo encaja con estos ejemplos: separar la voz y la batería de una canción propia para remezclar; generar stems para karaoke o práctica musical | Sin clave propia de API de IA en la ruta básica |
| [rubberband](../fichas/rubberband.md) | Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas. | Tu objetivo encaja con estos ejemplos: Ajustar duración de una narración; Explorar cambio de tono | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.
- [Agente de voz en tiempo real](../playbooks/agente-de-voz.md) — Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
