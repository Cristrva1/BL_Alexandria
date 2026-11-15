[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Audio, transcripción, voz y música

Transcripción, síntesis, clonación de voz, agentes de audio y música. Compara idioma, latencia, procesamiento local y servicios externos según la tarea concreta.

29 repos · 5 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [whisper.cpp](../fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | Sin API de IA en la ruta básica |
| [Kokoro](../fichas/kokoro.md) | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. | Sin API de IA en la ruta básica |
| [Pipecat](../fichas/pipecat.md) | Framework open source para agentes de voz y apps multimodales en tiempo real. | Depende de la ruta elegida |
| [AudioCraft](../fichas/audiocraft.md) | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | Sin API de IA en la ruta básica |

## Secciones

- [Transcripción (voz a texto)](#transcripción-voz-a-texto) — 5 repos
- [Síntesis y clonación de voz](#síntesis-y-clonación-de-voz) — 15 repos
- [Agentes de voz en tiempo real](#agentes-de-voz-en-tiempo-real) — 3 repos
- [Música y audio generativo](#música-y-audio-generativo) — 3 repos
- [Procesamiento y limpieza de audio](#procesamiento-y-limpieza-de-audio) — 3 repos

## Transcripción (voz a texto)

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [whisper.cpp](../fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | quieres transcribir en local sin GPU | Sin API de IA en la ruta básica |
| [whisper](../fichas/whisper.md) | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. | quieres la referencia robusta y no te obsesiona la latencia | Sin API de IA en la ruta básica |
| [faster-whisper](../fichas/faster-whisper.md) | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. | el rendimiento, la memoria o el coste de GPU importan | Sin API de IA en la ruta básica |
| [whisperX](../fichas/whisperx.md) | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. | necesitas subtítulos precisos o diarización | Sin API de IA en la ruta básica |
| [NVIDIA NeMo Speech](../fichas/nemo.md) | Framework de NVIDIA para entrenar y usar modelos de voz: reconocimiento, síntesis y más. | necesitas ASR de máxima precisión y tienes GPU | Sin API de IA en la ruta básica |

## Síntesis y clonación de voz

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Kokoro](../fichas/kokoro.md) | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. | quieres TTS ligero, rápido y con licencia permisiva | Sin API de IA en la ruta básica |
| [OmniVoice-Studio](../fichas/omnivoice-studio.md) | Alternativa local y open source a ElevenLabs: clonación, diseño y conversión de voz en una app. | quieres suite de voz completa local (dictado + clonación + dubbing) | Sin API de IA en la ruta básica |
| [GPT-SoVITS](../fichas/gpt-sovits.md) | Clonación de voz y TTS con solo un minuto de audio, con interfaz web para entrenar. | quieres entrenar una voz con pocos datos | Sin API de IA en la ruta básica |
| [VibeVoice](../fichas/vibevoice.md) | Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio. | quieres generar podcasts o diálogos largos | Sin API de IA en la ruta básica |
| [TTS](../fichas/tts.md) | Toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. | quieres flexibilidad y varios modelos en una librería | Sin API de IA en la ruta básica |
| [VoxCPM](../fichas/voxcpm.md) | Modelo de texto a voz sin tokenizador que clona voces con naturalidad y expresividad alta. | quieres voz muy natural o clonada y tienes GPU | Sin API de IA en la ruta básica |
| [RVC WebUI](../fichas/rvc.md) | Conversión de voz: entrena un modelo con menos de 10 minutos de audio y transforma una voz en otra. | quieres convertir una voz grabada en otra | Sin API de IA en la ruta básica |
| [Fish Speech](../fichas/fish-speech.md) | Sistema de texto a voz open source de alta calidad con clonación de voz multilingüe. | buscas TTS de alta calidad con clonación | Sin API de IA en la ruta básica |
| [Chatterbox](../fichas/chatterbox.md) | Modelo de texto a voz open source de Resemble AI con clonación de voz y control de emoción. | quieres clonar voces con calidad alta y licencia libre | Sin API de IA en la ruta básica |
| [IndexTTS](../fichas/index-tts.md) | Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. | necesitas controlar duración y emoción de la voz | Sin API de IA en la ruta básica |
| [CosyVoice](../fichas/cosyvoice.md) | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. | necesitas TTS multilingüe en streaming | Sin API de IA en la ruta básica |
| [supertonic](../fichas/supertonic.md) | Motor de texto a voz que ofrece modelos y ejemplos para sintetizar audio en dispositivos y navegadores compatibles. | quieres voz local en tiempo real y sin nube | Sin API de IA en la ruta básica |
| [edge-tts](../fichas/edge-tts.md) | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. | quieres generar narración sin instalar un modelo de voz local | Sin API de IA en la ruta básica |
| [MeloTTS](../fichas/melotts.md) | Biblioteca de texto a voz con modelos y ejemplos para sintetizar narración en varios idiomas compatibles. | buscas esta función: Biblioteca de texto a voz con modelos y ejemplos para sintetizar narración en varios idiomas compatibles. | Sin API de IA en la ruta básica |
| [LuxTTS](../fichas/luxtts.md) | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. | necesitas TTS con clonación muy rápido | Sin API de IA en la ruta básica |

## Agentes de voz en tiempo real

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Pipecat](../fichas/pipecat.md) | Framework open source para agentes de voz y apps multimodales en tiempo real. | construyes un agente de voz en Python | Depende de la ruta elegida |
| [LiveKit Agents](../fichas/livekit-agents.md) | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. | necesitas agentes de voz escalables con WebRTC | Depende de la ruta elegida |
| [dograh](../fichas/dograh.md) | Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables. | buscas esta función: Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables. | API de IA opcional |

## Música y audio generativo

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [AudioCraft](../fichas/audiocraft.md) | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | necesitas generar música o efectos de sonido por texto en local, o investigar modelos de audio | Sin API de IA en la ruta básica |
| [ACE-Step-1.5](../fichas/ace-step-1-5.md) | Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. | necesitas experimentar con generación musical en tu propio equipo | Sin API de IA en la ruta básica |
| [Music-Megathread](../fichas/music-megathread.md) | Directorio de reproductores, herramientas, servicios y otros recursos relacionados con música. | buscas recursos musicales y quieres comparar opciones desde una lista | Sin API de IA en la ruta básica |

## Procesamiento y limpieza de audio

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [rnnoise](../fichas/rnnoise.md) | Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente. | buscas esta función: Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente. | Sin API de IA en la ruta básica |
| [earshot](../fichas/earshot.md) | Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP. | buscas esta función: Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP. | API de IA opcional |
| [rubberband](../fichas/rubberband.md) | Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas. | buscas esta función: Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas. | Sin API de IA en la ruta básica |

## Recetas relacionadas

- [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.
- [Agente de voz en tiempo real](../playbooks/agente-de-voz.md) — Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
