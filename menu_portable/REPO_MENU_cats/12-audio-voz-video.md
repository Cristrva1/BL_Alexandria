# 12. Audio, Voz & Video — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `faster-whisper`
role=runtime · exec=local · setup=medium · mcp=False · prov=['openai']

**Qué es:** reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión.
**Stack:** Python, CTranslate2
**Repo:** https://github.com/SYSTRAN/faster-whisper

**Instalación** [~]: `git clone https://github.com/SYSTRAN/faster-whisper && cd faster-whisper && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** el rendimiento importa
**Evita si:** necesitas alineación/diarización ([whisperX](#-whisperx)).
**Combina con:** `whisperx`
**Alternativas (elige una):** `whisperx`

## `hyperframes`
role=library · exec=local · setup=medium · mcp=False · prov=['anthropic', 'google']

**Qué es:** framework npm para generar animaciones frame a frame de forma programática desde código.
**Stack:** Node.js/TypeScript
**Repo:** https://github.com/heygen-com/hyperframes

**Instalación** [~]: `npm install hyperframes   (o: pnpm add hyperframes)`
_Nombre npm puede diferir de 'hyperframes'; verifica en npmjs.com._

**Elige si:** generas animación por frames
**Evita si:** prefieres video en React ([remotion](#-remotion)).
**Combina con:** `remotion`
**Alternativas (elige una):** `remotion`

## `lossless-cut`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** aplicación de escritorio para recortar, fusionar y reorganizar video/audio sin recodificar, conservando la calidad original.
**Stack:** Node.js/Electron, ffmpeg
**Repo:** https://github.com/mifi/lossless-cut

**Instalación** [~]: `git clone https://github.com/mifi/lossless-cut && cd lossless-cut && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** cortas material rápido
**Evita si:** necesitas edición compositiva ([moviepy](#-moviepy)).
**Combina con:** `moviepy`
**Alternativas (elige una):** `moviepy`

## `moviepy`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** librería Python para edición de video programática: cortar, concatenar, superponer texto, subtítulos y audio, y exportar el resultado.
**Stack:** Python, ffmpeg
**Repo:** https://github.com/Zulko/moviepy

**Instalación** [~]: `pip install moviepy   (o: uv add moviepy)`
_Nombre PyPI puede diferir de 'moviepy'; verifica en pypi.org._

**Elige si:** ensamblas video por código
**Evita si:** prefieres React/programático web ([remotion](#-remotion)).
**Combina con:** `whisperx`, `tts`
**Alternativas (elige una):** `remotion`

## `omnivoice-studio`
role=app · exec=local · setup=medium · mcp=False · prov=['anthropic', 'mcp']

**Qué es:** suite de voz de escritorio open-source planteada como alternativa a ElevenLabs, con dictado en tiempo real, clonación zero-shot y doblaje de video en hasta 646 idiomas, todo local.
**Stack:** desktop/Python
**Repo:** https://github.com/debpalash/OmniVoice-Studio

**Instalación** [~]: `git clone https://github.com/debpalash/OmniVoice-Studio && cd OmniVoice-Studio && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres suite de voz completa local
**Evita si:** solo necesitas TTS simple ([TTS](#-tts)).
**Combina con:** `whisperx`
**Alternativas (elige una):** `tts`

## `opencut`
role=app · exec=hybrid · setup=medium · mcp=False · prov=['mcp']

**Qué es:** editor de video open-source con UI moderna, planteado como alternativa libre tipo CapCut, usable en web o escritorio.
**Stack:** web/TS
**Repo:** https://github.com/OpenCut-app/OpenCut

**Instalación** [?]: `git clone https://github.com/OpenCut-app/OpenCut (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres un editor libre con UI
**Evita si:** prefieres edición por código ([moviepy](#-moviepy)).
**Combina con:** `lossless-cut`
**Alternativas (elige una):** `moviepy`

## `openscreen`
role=app · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** herramienta ligera de grabación de pantalla para screencasts y demos; el proyecto original está archivado y continúa mediante un fork comunitario.
**Stack:** web/TS
**Repo:** https://github.com/lacymorrow/openscreen

**Instalación** [?]: `git clone https://github.com/lacymorrow/openscreen (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** necesitas screencast simple
**Evita si:** quieres algo mantenido (está archivado).
**Combina con:** `opencut`

## `remotion`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4.
**Stack:** Node.js, React
**Repo:** https://github.com/remotion-dev/remotion

**Instalación** [~]: `npm install remotion   (o: pnpm add remotion)`
_Nombre npm puede diferir de 'remotion'; verifica en npmjs.com._

**Elige si:** generas video a escala con React
**Evita si:** trabajas en Python ([moviepy](#-moviepy)).
**Combina con:** `open-generative-ai`
**Alternativas (elige una):** `moviepy`

## `supertonic`
role=runtime · exec=local · setup=medium · mcp=False · prov=['openai', 'local']

**Qué es:** motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU.
**Stack:** Python, Rust (ONNX/PyTorch), Node.js
**Repo:** https://github.com/supertone-inc/supertonic

**Instalación** [~]: `git clone https://github.com/supertone-inc/supertonic && cd supertonic && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres voz local en tiempo real
**Evita si:** priorizas clonación de máxima fidelidad ([VoxCPM](#-voxcpm)).
**Combina con:** `whisperx`, `moviepy`
**Alternativas (elige una):** `voxcpm`

## `tts`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz.
**Stack:** Python, modelos descargables
**Repo:** https://github.com/coqui-ai/TTS

**Instalación** [~]: `pip install tts   (o: uv add tts)`
_Nombre PyPI puede diferir de 'TTS'; verifica en pypi.org._

**Elige si:** quieres flexibilidad
**Evita si:** necesitas tiempo real puro ([supertonic](#-supertonic)).
**Combina con:** `whisperx`, `moviepy`
**Alternativas (elige una):** `supertonic`

## `videofy-minimal`
role=app · exec=local · setup=easy · mcp=False · prov=['openai']

**Qué es:** herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pipeline complejo.
**Stack:** Python/Node
**Repo:** https://github.com/schibsted/videofy_minimal

**Instalación** [~]: `git clone https://github.com/schibsted/videofy_minimal && cd videofy_minimal && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres reels simples ya
**Evita si:** necesitas variantes programáticas ([remotion](#-remotion)).
**Combina con:** `whisper`, `supertonic`
**Alternativas (elige una):** `remotion`

## `voxcpm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['openai']

**Qué es:** sistema TTS de alta fidelidad de OpenBMB que prescinde del tokenizador tradicional para lograr una prosodia y fluidez muy naturales, con clonación de voz.
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/OpenBMB/VoxCPM

**Instalación** [~]: `git clone https://github.com/OpenBMB/VoxCPM && cd VoxCPM && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres voz muy natural/clonada
**Evita si:** priorizas latencia mínima ([supertonic](#-supertonic)).
**Combina con:** `tts`
**Alternativas (elige una):** `supertonic`

## `whisper`
role=runtime · exec=local · setup=medium · mcp=False · prov=['openai']

**Qué es:** modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo.
**Stack:** Python 3.9+, PyTorch
**Repo:** https://github.com/openai/whisper

**Instalación** [~]: `git clone https://github.com/openai/whisper && cd whisper && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres la referencia
**Evita si:** necesitas más velocidad ([faster-whisper](#-faster-whisper)).
**Combina con:** `whisperx`
**Alternativas (elige una):** `faster-whisper`

## `whisperx`
role=runtime · exec=local · setup=medium · mcp=False · prov=['openai']

**Qué es:** extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional.
**Stack:** Python, modelos Whisper
**Repo:** https://github.com/m-bain/whisperX

**Instalación** [~]: `git clone https://github.com/m-bain/whisperX && cd whisperX && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas subtítulos precisos
**Evita si:** te basta texto plano ([whisper](#-whisper)).
**Combina con:** `whisper`, `moviepy`
**Alternativas (elige una):** `whisper`

## `youtube2webpage`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripción de subtítulos con capturas de pantalla del momento citado.
**Stack:** Perl, yt-dlp
**Repo:** https://github.com/obra/Youtube2Webpage

**Instalación** [?]: `git clone https://github.com/obra/Youtube2Webpage (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres video → artículo
**Evita si:** necesitas edición de video.
**Combina con:** `whisper`
