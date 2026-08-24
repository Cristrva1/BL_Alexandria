# Pipeline de Reels / video corto

Generado: 2026-08-24T04:31:34.499362+00:00

## Objetivo

convertir contenido en video corto con voz y subtítulos.

## Stack sugerido

- `whisperx`: If you’re looking for a transcription API for meetings, consider checking out Recall.ai's Meeting Transcription API, an API that works with Zoom, Google Meet, Microsoft Teams, and more. Recall.ai diarizes by pulling the speaker data and separate audio streams from the meeting platforms, which means 100% accurate speaker diarization with actual speaker names.
- `supertonic`: Supertonic is a lightning-fast, on-device multilingual text-to-speech system designed for local inference with minimal overhead. Powered by ONNX Runtime, it runs entirely on your device—no cloud, no API calls, no privacy concerns.
- `tts`: 📣 ⓍTTSv2 is here with 16 languages and better performance across the board. 📣 ⓍTTS fine-tuning code is out. Check the example recipes. 📣 ⓍTTS can now stream with <200ms latency. 📣 ⓍTTS, our production TTS model that can speak 13 languages, is released Blog Post, Demo, Docs.
- `comfyui`: The most powerful and modular AI engine for content creation..
- `fooocus`: Fooocus is an image generating software (based on Gradio ).
- `real-esrgan`: 🔥 RealESRGANx4plusanime6B for anime images (动漫插图模型). Please see [animemodel].
- `moviepy`: MoviePy recently upgraded to v2.0, introducing major breaking changes. You can consult the last v1 docs here but beware that v1 is no longer maintained. For more info on how to update your code from v1 to v2, see this guide.
- `remotion`: Remotion renderiza video desde componentes React. Úsalo para piezas generadas por código (intros, datos, motion graphics), no como NLE clásico.
- `lossless-cut`: The swiss army knife of lossless video/audio editing.

## Como se conecta

[videofy_minimal](#-videofy_minimal) puede orquestar el flujo simple; remotion/moviepy escalan a variantes programáticas.
