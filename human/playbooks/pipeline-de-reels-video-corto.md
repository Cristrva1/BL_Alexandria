# Pipeline de Reels / video corto

Generado: 2026-06-23T16:56:54.761958+00:00

## Objetivo

convertir contenido en video corto con voz y subtítulos.

## Stack sugerido

- `whisperx`: extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional.
- `supertonic`: motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU.
- `tts`: toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz.
- `comfyui`: motor local modular para crear pipelines visuales de generación con IA mediante un grafo de nodos, donde cada paso (carga de modelo, sampling, postproceso) es un bloque conectable y reutilizable.
- `fooocus`: herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes.
- `real-esrgan`: herramienta de superresolución y restauración para imágenes reales que reescala y limpia material de baja calidad sin rehacerlo.
- `moviepy`: librería Python para edición de video programática: cortar, concatenar, superponer texto, subtítulos y audio, y exportar el resultado.
- `remotion`: framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4.
- `lossless-cut`: aplicación de escritorio para recortar, fusionar y reorganizar video/audio sin recodificar, conservando la calidad original.

## Como se conecta

[videofy_minimal](#-videofy_minimal) puede orquestar el flujo simple; remotion/moviepy escalan a variantes programáticas.
