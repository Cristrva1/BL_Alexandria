# Audio, Voz & Video

Generado: 2026-06-23T16:56:54.761958+00:00

| Repo | Rol | Instalacion | Decision | Uso real |
|---|---|---|---|---|
| whisper | runtime | reference_only | reference | modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. |
| faster-whisper | runtime | reference_only | reference | reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión. |
| whisperX | runtime | reference_only | reference | extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |
| supertonic | runtime | reference_only | reference | motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU. |
| VoxCPM | runtime | deferred | defer | sistema TTS de alta fidelidad de OpenBMB que prescinde del tokenizador tradicional para lograr una prosodia y fluidez muy naturales, con clonación de voz. |
| TTS | library | reference_only | reference | toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. |
| OmniVoice-Studio | app | reference_only | reference | suite de voz de escritorio open-source planteada como alternativa a ElevenLabs, con dictado en tiempo real, clonación zero-shot y doblaje de video en hasta 646 idiomas, todo local. |
| lossless-cut | app | reference_only | reference | aplicación de escritorio para recortar, fusionar y reorganizar video/audio sin recodificar, conservando la calidad original. |
| moviepy | library | reference_only | reference | librería Python para edición de video programática: cortar, concatenar, superponer texto, subtítulos y audio, y exportar el resultado. |
| remotion | library | reference_only | reference | framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4. |
| videofy_minimal | app | reference_only | reference | herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pipeline complejo. |
| OpenCut | app | reference_only | reference | editor de video open-source con UI moderna, planteado como alternativa libre tipo CapCut, usable en web o escritorio. |
| openscreen | app | reference_only | reference | herramienta ligera de grabación de pantalla para screencasts y demos; el proyecto original está archivado y continúa mediante un fork comunitario. |
| Youtube2Webpage | library | reference_only | reference | script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripción de subtítulos con capturas de pantalla del momento citado. |
| hyperframes | library | reference_only | reference | framework npm para generar animaciones frame a frame de forma programática desde código. |
