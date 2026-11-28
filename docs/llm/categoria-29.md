# Alexandría para agentes · Audio, transcripción, voz y música

Categoría 29 completa (34 repos, 5 subcategorías). Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=29 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `whisper-cpp` | stt | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y… | 1 Básico | 70 | MIT (OSI permisiva) | recomendado |
| `faster-whisper` | stt | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU… | 2 Intermedio | 66 | MIT (OSI permisiva) | alternativa |
| `nemo` | stt | Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con… | 3 Avanzado | 66 | Apache-2.0 (OSI permisiva) | recomendado |
| `sherpa-onnx` | stt | Motor de voz offline con ONNX Runtime: reconocimiento, síntesis, VAD… | 3 Avanzado | 65 | Apache-2.0 (OSI permisiva) | sin grupo |
| `buzz` | stt | Transcribe grabaciones y exporta subtítulos en una aplicación de escritorio que… | 1 Básico | 64 | MIT (OSI permisiva) | sin grupo |
| `whisper` | stt | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución… | 2 Intermedio | 64 | MIT (OSI permisiva) | alternativa |
| `whisperx` | stt | Pipeline de transcripción que añade alineación temporal de palabras y funciones… | 2 Intermedio | 64 | BSD-2-Clause (OSI permisiva) | alternativa |
| `omnivoice-studio` | tts | App local de voz con modelos descargables,edición AGPL y una oferta comercial… | 2 Intermedio | 76 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `gpt-sovits` | tts | Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y… | 2 Intermedio | 69 | MIT (OSI permisiva) | recomendado |
| `voxcpm` | tts | VoxCPM2: modelos y herramientas locales de TTS multilingüe,diseño y adaptación… | 3 Avanzado | 68 | Apache-2.0 (OSI permisiva) | sin grupo |
| `elevenlabs-python` | tts | SDK oficial de Python para la API de pago de ElevenLabs: voz sintética… | 2 Intermedio | 66 | MIT (OSI permisiva) | sin grupo |
| `f5-tts` | tts | Síntesis de voz con clonación a partir de pocos segundos de audio de… | 3 Avanzado | 64 | MIT (OSI permisiva) | alternativa |
| `cosyvoice` | tts | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y… | 2 Intermedio | 61 | Apache-2.0 (OSI permisiva) | alternativa |
| `fish-speech` | tts | Herramientas y modelos de voz Fish Audio con licencias Community o Research… | 3 Avanzado | 61 | Fish Audio Community License 1.0 (no OSI) (source-available) | alternativa |
| `vibevoice` | tts | Familia de modelos de voz de Microsoft con herramientas para generación y… | 3 Avanzado | 61 | MIT (OSI permisiva) | sin grupo |
| `edge-tts` | tts | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado… | 2 Intermedio | 60 | LGPL-3.0 (un archivo MIT) (OSI copyleft) | recomendado |
| `rvc` | tts | Interfaz y herramientas para convertir una grabación a otra voz mediante… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `index-tts` | tts | Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. | 2 Intermedio | 53 | bilibili Model Use License (source-available) | alternativa |
| `luxtts` | tts | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una… | 2 Intermedio | 52 | Apache-2.0 (OSI permisiva) | alternativa |
| `kokoro` | tts | Modelo y biblioteca de texto a voz para generar narración localmente con… | 2 Intermedio | 48 | Apache-2.0 (OSI permisiva) | alternativa |
| `livekit-agents` | voz-agentes | Framework para agentes de voz y video en tiempo real sobre la infraestructura… | 2 Intermedio | 73 | Apache-2.0 (OSI permisiva) | alternativa |
| `pipecat` | voz-agentes | Framework open source para agentes de voz y apps multimodales en tiempo real. | 2 Intermedio | 73 | BSD-2-Clause (OSI permisiva) | recomendado |
| `dograh` | voz-agentes | Plataforma para construir agentes de voz con flujos visuales, telefonía y… | 2 Intermedio | 62 | BSD-2-Clause (OSI permisiva) | alternativa |
| `ten-framework` | voz-agentes | Framework para agentes de voz conversacionales en tiempo real, con grafo de… | 3 Avanzado | 46 | Apache-2.0 con condiciones adicionales (Agora) (source-available) | alternativa |
| `ace-step-1.5` | musica | Modelo y herramientas para generar música localmente a partir de instrucciones… | 3 Avanzado | 70 | MIT (OSI permisiva) | recomendado |
| `yue` | musica | Modelo abierto de generación de canciones completas (voz y acompañamiento) a… | 4 Experto | 67 | Apache-2.0 (OSI permisiva) | alternativa |
| `audiocraft` | musica | Librería PyTorch de Meta para generar música y efectos de sonido desde texto… | 2 Intermedio | 52 | MIT (OSI permisiva) | alternativa |
| `audacity` | audio | Editor y grabador de audio multipista libre para Windows, macOS y Linux, con… | 1 Básico | 67 | GPL-3.0 (mayoría de archivos GPL-2.0-or-later) (OSI copyleft) | sin grupo |
| `pyannote-audio` | audio | Kit de PyTorch para diarización de hablantes (quién habla y cuándo) con modelos… | 3 Avanzado | 64 | MIT (OSI permisiva) | sin grupo |
| `ultimate-vocal-remover` | audio | Aplicación de escritorio para separar voz e instrumentos de canciones con… | 3 Avanzado | 58 | MIT (OSI permisiva) | sin grupo |
| `demucs` | audio | Modelo de separación de fuentes musicales (voz, batería, bajo y resto) con… | 3 Avanzado | 56 | MIT (OSI permisiva) | sin grupo |
| `earshot` | audio | Herramientas locales de audio para que un agente escuche, analice y revise… | 2 Intermedio | 55 | MIT (OSI permisiva) | sin grupo |
| `rubberband` | audio | Biblioteca de audio para modificar duración y tono de una grabación, integrada… | 2 Intermedio | 42 | GPL-2.0 (OSI copyleft) | sin grupo |
| `rnnoise` | audio | Biblioteca de reducción de ruido de audio que utiliza una red neuronal para… | 2 Intermedio | 41 | BSD-3-Clause (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### whisper.cpp (`whisper-cpp`)

- **Repo:** https://github.com/ggml-org/whisper.cpp · MIT · nivel 1 · 70/100 · recomendado en «Transcripción con Whisper»
- **Qué es:** whisper.cpp, implementación en C/C++ sin dependencias del modelo de reconocimiento de voz Whisper de OpenAI, de ggml-org. Licencia MIT. Es muy madura (~55k estrellas, v1.9.5).
- **Cuándo elegirlo:** Casos: Transcribir una nota offline; Preparar texto base para subtítulos.
- **Requisitos:** nivel 1: preparación sencilla; Compilador y CMake según sistema; modelo Whisper; audio corto compatible; hardware prerequisites; API de IA: no; Compilador y CMake según sistema; modelo Whisper; audio corto compatible.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/ggml-org/whisper.cpp.git` — fuente: https://github.com/ggml-org/whisper.cpp/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Transcribe una grabación propia corta y compara nombres y números con el audio Éxito: Puedes identificar modelo y errores de transcripción
- **Combina con:** `ffmpeg` [12/edicion], `llama-cpp` [8/motores], `pipecat` [29/voz-agentes], `dograh` [29/voz-agentes], `kokoro` [29/tts], `livekit-agents` [29/voz-agentes]
- **Alternativas:** `faster-whisper`, `whisper`
- **Riesgos y avisos:** Alternativas (elige una): faster-whisper, whisper. Clonar es solo el comienzo: sigue compilación, descarga del modelo y formato de audio; no necesitas instalar todas las aceleraciones del README.

### faster-whisper (`faster-whisper`)

- **Repo:** https://github.com/SYSTRAN/faster-whisper · MIT · nivel 2 · 66/100 · alternativa en «Transcripción con Whisper»
- **Qué es:** faster-whisper, reimplementación de Whisper sobre CTranslate2, de SYSTRAN. Licencia MIT. Es madura (~27k estrellas, v1.2.1).
- **Cuándo elegirlo:** Casos: Transcribir lotes pequeños; Comparar CPU con GPU.
- **Requisitos:** nivel 2: pip install; funciona en CPU, la GPU acelera; Python; CTranslate2; CPU o CUDA/cuDNN compatibles; modelo y audio; hardware prerequisites; API de IA: no; Python; CTranslate2; CPU o CUDA/cuDNN compatibles; modelo y audio.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install faster-whisper` — fuente: https://github.com/SYSTRAN/faster-whisper/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Transcribe un clip corto con una configuración adecuada al equipo y compara salida y tiempo Éxito: Puedes revisar modelo, cuantización y resultado
- **Combina con:** `whisperx`, `pipecat` [29/voz-agentes], `moviepy` [30/motores], `ai-youtube-shorts-generator` [12/generativo], `moneyprinterturbo` [12/generativo], `obs-studio` [12/edicion]
- **Alternativas:** `whisper-cpp`, `whisper`
- **Riesgos y avisos:** Alternativas (elige una): whisper-cpp. Las dependencias CUDA y cuDNN cambian con CTranslate2; el ahorro de memoria y velocidad depende del modelo y parámetros.

### NeMo Speech (`nemo`)

- **Repo:** https://github.com/NVIDIA-NeMo/Speech · Apache-2.0 · nivel 3 · 66/100 · recomendado en «Transcripción con modelos NVIDIA y alineación»
- **Qué es:** NVIDIA NeMo Speech (antes parte de NeMo), framework actual de NVIDIA para reconocimiento de voz, síntesis y modelos conversacionales. Licencia Apache-2.0. Es maduro (~19k estrellas, v3.0.0).
- **Cuándo elegirlo:** Casos: Estudiar modelos de voz de NVIDIA; Preparar un experimento ASR.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él, necesita GPU; uv; entorno CUDA compatible; modelo de voz elegido; audio de prueba; hardware prerequisites; API de IA: no; uv; entorno CUDA compatible; modelo de voz elegido; audio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/NVIDIA-NeMo/Speech/blob/main/README.md

  ```bash
  git clone https://github.com/NVIDIA-NeMo/Speech.git
  cd Speech
  uv sync --extra all --extra cu13     # CUDA 13.x (recommended) — use --extra cu12 for CUDA 12.x
  ```
- **Primera prueba propuesta (no ejecutada):** Elige la receta de transcripción y prueba un clip breve antes de entrenar Éxito: Puedes identificar checkpoint, configuración y salida
- **Combina con:** `nemotron` [24/modelos], `pipecat` [29/voz-agentes], `pytorch` [24/entrenamiento], `sherpa-onnx`
- **Alternativas:** `whisperx`
- **Riesgos y avisos:** Alternativas (elige una): whisperx. El repositorio actual es NeMo Speech; las guías nightly y 3.0 estable son distintas y deben alinearse con la versión instalada.

### sherpa-onnx (`sherpa-onnx`)

- **Repo:** https://github.com/k2-fsa/sherpa-onnx · Apache-2.0 · nivel 3 · 65/100
- **Qué es:** Motor de voz de código abierto (Apache-2.0) del proyecto k2-fsa (Next-gen Kaldi). Muy activo y con muchos proyectos que lo usan en móviles y dispositivos embebidos.
- **Cuándo elegirlo:** Casos: añadir dictado o transcripción sin conexión a una app Android o iOS; poner reconocimiento y síntesis de voz en una Raspberry Pi sin nube. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 3: preparación media, necesita GPU; C++, CMakeLists.txt, pom.xml, setup.py; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/k2-fsa/sherpa-onnx/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala el paquete de Python, descarga un modelo de reconocimiento preentrenado de la documentación y transcribe un WAV de prueba. Éxito: Obtienes el texto reconocido sin conexión a internet.
- **Combina con:** `whisper`, `nemo`, `kokoro` [29/tts], `pyannote-audio` [29/audio]
- **Riesgos y avisos:** Alternativa ligera y multiplataforma a whisper.cpp o faster-whisper cuando necesitas varias tareas de voz en dispositivos.

### Buzz (`buzz`)

- **Repo:** https://github.com/chidiwilliams/buzz · MIT · nivel 1 · 64/100
- **Qué es:** Una aplicación con interfaz para convertir voz grabada en texto, basada en Whisper y otros backends compatibles.
- **Cuándo elegirlo:** Casos: Convertir una nota de voz propia en texto editable.; Crear subtítulos en SRT para una demostración grabada.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Python, Makefile, pyproject.toml; hardware model_dependent; API de IA: opcional; Distribución para tu sistema. En versiones recientes de macOS consulta la distinción entre Apple Silicon e Intel.; Espacio para el modelo y un audio de prueba; CPU o GPU según el backend..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install buzz-captions` — fuente: https://github.com/chidiwilliams/buzz/blob/ac3d9da57dd155c8f8fba5f40644392e38423e6f/README.md
- **Primera prueba propuesta (no ejecutada):** Importa diez segundos de audio propio y elige un modelo Whisper local pequeño. Éxito: Aparece una transcripción que puedes revisar y exportar como SRT.
- **Combina con:** `ffmpeg` [12/edicion]
- **Riesgos y avisos:** Instalador Windows sin firma según el autor; GitHub publica digests para los archivos del release revisado.

### whisper (`whisper`)

- **Repo:** https://github.com/openai/whisper · MIT · nivel 2 · 64/100 · alternativa en «Transcripción con Whisper»
- **Qué es:** Whisper, modelo de reconocimiento de voz de propósito general de OpenAI, entrenado con datos débilmente supervisados. Licencia MIT para código y pesos. Tiene ~113k estrellas y su release es v20250625; el repo recibe pocos cambios.
- **Cuándo elegirlo:** Casos: Preparar una transcripción local; Traducir habla al inglés como borrador.
- **Requisitos:** nivel 2: preparación media; Python; PyTorch; FFmpeg; modelo con memoria suficiente; audio autorizado; hardware prerequisites; API de IA: no; Python; PyTorch; FFmpeg; modelo con memoria suficiente; audio autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U openai-whisper` — fuente: https://github.com/openai/whisper/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Transcribe una nota de voz breve y corrige manualmente las palabras dudosas Éxito: Puedes contrastar texto con audio original
- **Combina con:** `ffmpeg` [12/edicion], `whisperx`, `pytorch` [24/entrenamiento]
- **Alternativas:** `whisper-cpp`, `faster-whisper`
- **Riesgos y avisos:** Alternativas (elige una): whisper-cpp. Para producción suelen preferirse faster-whisper o whisper.cpp por velocidad. No es la API hospedada de OpenAI y no usa créditos de ChatGPT; puede inventar texto en silencios o audio difícil y requiere revisión.

### whisperX (`whisperx`)

- **Repo:** https://github.com/m-bain/whisperX · BSD-2-Clause · nivel 2 · 64/100 · alternativa en «Transcripción con modelos NVIDIA y alineación»
- **Qué es:** WhisperX, pipeline de transcripción con marcas de tiempo precisas por palabra y diarización, de @m-bain. Licencia BSD-2-Clause. Es madura (~25k estrellas, v3.8.6); el README incluye un patrocinio (Recall.ai).
- **Cuándo elegirlo:** Casos: Preparar subtítulos por palabra; Separar intervenciones de una entrevista.
- **Requisitos:** nivel 2: preparación media; Python; modelo de transcripción y alineación; HF token y acuerdo para diarización; audio propio; hardware prerequisites; API de IA: no; Python; modelo de transcripción y alineación; HF token y acuerdo para diarización; audio propio.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install whisperx` — fuente: https://github.com/m-bain/whisperX/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Transcribe una conversación de prueba y verifica varias marcas temporales y cambios de hablante Éxito: Puedes distinguir texto, alineación y etiquetas de hablante
- **Combina con:** `faster-whisper`, `whisper`, `moviepy` [30/motores], `pyannote-audio` [29/audio]
- **Alternativas:** `nemo`
- **Riesgos y avisos:** Alternativas (elige una): nemo. Un token de descarga no equivale a facturación de API; etiquetas de hablante no identifican personas y los tiempos necesitan comprobación.

### VoiceStudio (`omnivoice-studio`)

- **Repo:** https://github.com/debpalash/VoiceStudio · AGPL-3.0 · nivel 2 · 76/100
- **Qué es:** VoiceStudio (antes OmniVoice Studio; repo debpalash/VoiceStudio), estudio de voz con IA que funciona en el dispositivo. La app es AGPL-3.0; los pesos, voces y salidas tienen licencias propias, y hay ediciones Pro y Cloud de pago con…
- **Cuándo elegirlo:** Casos: Preparar una narración local; Probar transcripción o doblaje de material propio.
- **Requisitos:** nivel 2: preparación media; Instalador VoiceStudio para tu sistema; modelos; almacenamiento; voces autorizadas; hardware prerequisites; API de IA: no; Instalador VoiceStudio para tu sistema; modelos; almacenamiento; voces autorizadas.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install --cask debpalash/tap/voicestudio` — fuente: https://github.com/debpalash/VoiceStudio/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga un modelo compatible y sintetiza un párrafo propio antes de probar clonación Éxito: Puedes comprobar modelo, licencia y salida de audio
- **Combina con:** `whisperx` [29/stt], `ffmpeg` [12/edicion], `kokoro`
- **Alternativas:** `videolingo`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): videolingo. Recuento de estrellas inusual para su edad. El nombre actual es VoiceStudio; pedir a Claude o Codex ayuda para instalar no es una integración de sus planes ni garantiza igual calidad en todos los idiomas….

### GPT-SoVITS (`gpt-sovits`)

- **Repo:** https://github.com/RVC-Boss/GPT-SoVITS · MIT · nivel 2 · 69/100 · recomendado en «Clonación de voz y TTS multilingüe»
- **Qué es:** GPT-SoVITS, WebUI de TTS y conversión de voz con pocos ejemplos, de @RVC-Boss. Licencia MIT. Es muy popular (~65k estrellas, release 20250606v2pro).
- **Cuándo elegirlo:** Casos: Prototipar una voz para contenido propio; Estudiar adaptación con pocos ejemplos.
- **Requisitos:** nivel 2: preparación media; Conda; Python 3.10; PyTorch compatible; modelos; audio con permiso; GPU según tarea; hardware prerequisites; API de IA: no; Conda; Python 3.10; PyTorch compatible; modelos; audio con permiso; GPU según tarea.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md

  ```bash
  conda create -n GPTSoVits python=3.10
  conda activate GPTSoVits

  pip install -r extra-req.txt --no-deps
  pip install -r requirements.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Sintetiza una frase corta con una voz autorizada y compara inteligibilidad antes de entrenar Éxito: Puedes revisar referencia, modelo y resultado
- **Combina con:** `rvc`, `ffmpeg` [12/edicion], `whisperx` [29/stt], `videolingo` [12/edicion]
- **Alternativas:** `f5-tts`, `cosyvoice`, `fish-speech`, `index-tts`
- **Riesgos y avisos:** Alternativas (elige una): fish-speech. Riesgo de suplantación de voz: usa voces con consentimiento. El lema de un minuto describe few-shot y no una garantía de calidad con cualquier grabación o idioma.

### VoxCPM (`voxcpm`)

- **Repo:** https://github.com/OpenBMB/VoxCPM · Apache-2.0 · nivel 3 · 68/100
- **Qué es:** VoxCPM2, TTS sin tokenizador para habla multilingüe, diseño de voces y clonación, de OpenBMB. Licencia Apache-2.0 para código y pesos, con uso comercial permitido. Tiene ~43k estrellas (2.0.3).
- **Cuándo elegirlo:** Casos: Preparar narración local; Explorar diseño de voz consentido.
- **Requisitos:** nivel 3: preparación pesada; Python >=3.10 y <3.13; PyTorch >=2.5; CUDA según ruta; pesos; audio autorizado; hardware prerequisites; API de IA: no; Python >=3.10 y <3.13; PyTorch >=2.5; CUDA según ruta; pesos; audio autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install voxcpm` — fuente: https://github.com/OpenBMB/VoxCPM/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sintetiza un texto corto y revisa pronunciación y estabilidad antes de ampliar Éxito: Puedes identificar modelo y parámetros de la prueba
- **Combina con:** `vllm` [23/serving], `pipecat` [29/voz-agentes], `ffmpeg` [12/edicion]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Riesgo de suplantación por la clonación de voz. La ruta principal y on-device usan requisitos diferentes; velocidad y naturalidad son resultados que deben comprobarse con tu idioma y equipo.

### ElevenLabs (SDK de Python) (`elevenlabs-python`)

- **Repo:** https://github.com/elevenlabs/elevenlabs-python · MIT · nivel 2 · 66/100
- **Qué es:** SDK oficial de Python para la API de ElevenLabs (organización elevenlabs), generado con Fern y con licencia MIT. El cliente es libre, pero el servicio es de pago por uso. Versión v2.78.0 (noviembre de 2026), activo.
- **Cuándo elegirlo:** Casos: Generar una locución para un video; Prototipar un agente de voz conectado a la API.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él, requiere clave de API; Python, pyproject.toml, requirements.txt; API de IA: sí; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install elevenlabs` — fuente: https://github.com/elevenlabs/elevenlabs-python/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Convierte una frase corta a voz con una voz predefinida Éxito: Obtienes un MP3 reproducible y el consumo aparece en tu cuenta
- **Combina con:** `openmontage` [30/skills-video], `pipecat` [29/voz-agentes], `livekit-agents` [29/voz-agentes], `video-use` [30/skills-video], `remotion-superpowers` [30/skills-video], `ten-framework` [29/voz-agentes]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. La clonación de voz exige el consentimiento de la persona. Vigila el consumo de créditos: el SDK no limita el gasto.

### F5-TTS (`f5-tts`)

- **Repo:** https://github.com/SWivid/F5-TTS · MIT · nivel 3 · 64/100 · alternativa en «Clonación de voz y TTS multilingüe»
- **Qué es:** Proyecto de investigación de código abierto (código MIT) del equipo SWivid, publicado con su artículo en arXiv. Los pesos preentrenados son CC-BY-NC. Activo (modelo base v1 en marzo de 2025).
- **Cuándo elegirlo:** Casos: generar narración con tu propia voz a partir de una muestra corta; prototipar voces para un proyecto de investigación sin uso comercial. Evítalo si no tienes el hardware o no aceptas la licencia de los pesos.
- **Requisitos:** nivel 3: preparación media, necesita GPU; Python, Dockerfile, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install f5-tts` — fuente: https://github.com/SWivid/F5-TTS/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala PyTorch y `pip install f5-tts`; ejecuta `f5-tts_infer-gradio` y genera audio con una referencia de tu voz. Éxito: Obtienes un audio con el texto leído imitando la voz de referencia.
- **Combina con:** `pytorch` [24/entrenamiento], `ffmpeg` [12/edicion], `gradio` [25/apps]
- **Alternativas:** `gpt-sovits`, `cosyvoice`, `fish-speech`, `index-tts`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativa de Fish Speech y CosyVoice para clonación de voz; revisa siempre la licencia de los pesos antes de usos comerciales.

### CosyVoice (`cosyvoice`)

- **Repo:** https://github.com/QwenAudio/CosyVoice · Apache-2.0 · nivel 2 · 61/100 · alternativa en «Clonación de voz y TTS multilingüe»
- **Qué es:** CosyVoice, modelo de voz multilingüe del equipo Qwen/FunAudioLLM de Alibaba, con inferencia, entrenamiento y despliegue. Licencia Apache-2.0. Tiene ~24k estrellas, la versión actual es Fun-CosyVoice 3.0 y el repo no cambia desde mayo de…
- **Cuándo elegirlo:** Casos: Explorar síntesis multilingüe; Estudiar streaming de voz.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Conda y Python 3.10 según guía; submódulos; pesos; FFmpeg o sox según ruta; hardware prerequisites; API de IA: no; Conda y Python 3.10 según guía; submódulos; pesos; FFmpeg o sox según ruta.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/QwenAudio/CosyVoice/blob/main/README.md

  ```sh
  git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
      # If you failed to clone the submodule due to network failures, please run the following command until success
      cd CosyVoice
      git submodule update --init --recursive
  ```
- **Primera prueba propuesta (no ejecutada):** Descarga una variante compatible y prueba una frase del idioma elegido Éxito: Puedes comprobar voz, texto y archivo generado
- **Combina con:** `pipecat` [29/voz-agentes], `vllm` [23/serving], `ffmpeg` [12/edicion], `wan2-2` [12/generativo]
- **Alternativas:** `gpt-sovits`, `f5-tts`, `fish-speech`, `index-tts`
- **Riesgos y avisos:** Alternativas (elige una): fish-speech, index-tts. El proyecto pertenece a FunAudioLLM; variantes de vLLM requieren entornos específicos y no conviene mezclar todas las dependencias en uno.

### Fish Speech (`fish-speech`)

- **Repo:** https://github.com/fishaudio/fish-speech · Fish Audio Community License 1.0 (no OSI) · nivel 3 · 61/100 · alternativa en «Clonación de voz y TTS multilingüe»
- **Qué es:** Fish Speech, herramientas y modelos de voz de Fish Audio. El código y los pesos usan la «Fish Audio Community License»; los pesos S2-Pro usan la Fish Audio Research License (GitHub muestra NOASSERTION). Tiene ~34k estrellas.
- **Cuándo elegirlo:** Casos: Estudiar generación expresiva; Preparar una prueba de voz multilingüe.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, necesita GPU; Entorno y GPU compatibles; modelo con licencia aplicable; texto y voz autorizados; hardware prerequisites; API de IA: no; Entorno y GPU compatibles; modelo con licencia aplicable; texto y voz autorizados.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/fishaudio/fish-speech/blob/main/docs/en/install.md

  ```bash
  docker run --gpus device=0 -v ./checkpoints:/app/checkpoints -e LLAMA_CHECKPOINT_PATH=checkpoints/drama-3 -p 8080:8080 fishaudio/fish-speech:server-cuda
  ```
- **Primera prueba propuesta (no ejecutada):** Elige Drama 3 o S2-Pro y prueba una frase corta después de revisar sus condiciones Éxito: Puedes distinguir la variante y su licencia
- **Combina con:** `pipecat` [29/voz-agentes], `ffmpeg` [12/edicion], `whisperx` [29/stt]
- **Alternativas:** `gpt-sovits`, `f5-tts`, `cosyvoice`, `index-tts`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): cosyvoice, gpt-sovits. Licencia no OSI: revisa los términos. La disponibilidad del código no equivale a Apache o MIT ni a un servicio API gratuito; sigue la guía de la variante elegida.

### VibeVoice (`vibevoice`)

- **Repo:** https://github.com/microsoft/VibeVoice · MIT · nivel 3 · 61/100
- **Qué es:** VibeVoice, familia de modelos de voz open source de Microsoft (TTS y ASR). Licencia MIT. Tiene ~57k estrellas; en septiembre de 2025 Microsoft desactivó el código de VibeVoice-TTS-1.5B tras detectar usos indebidos.
- **Cuándo elegirlo:** Casos: Estudiar transcripción por hablantes; Probar generación de voz.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él; Modelo y guía específicos; Python y GPU según variante; audio autorizado; hardware prerequisites; API de IA: no; Modelo y guía específicos; Python y GPU según variante; audio autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/microsoft/VibeVoice.git` — fuente: https://github.com/microsoft/VibeVoice/blob/main/docs/setup_gradio_demo.md
- **Primera prueba propuesta (no ejecutada):** Transcribe un audio propio corto con VibeVoice-ASR o genera una frase con VibeVoice-Realtime-0.5B siguiendo su guía Éxito: Obtienes el texto o el audio y sabes qué variante del modelo usaste
- **Combina con:** `transformers` [24/entrenamiento], `open-notebook` [8/notebooklm], `pipecat` [29/voz-agentes], `ten-framework` [29/voz-agentes]
- **Riesgos y avisos:** Sin alternativas declaradas. Partes del TTS deshabilitadas por uso indebido. Es una familia que incluye ASR, streaming y TTS; el README raíz remite a guías separadas y no tiene un único instalador universal.

### edge-tts (`edge-tts`)

- **Repo:** https://github.com/rany2/edge-tts · LGPL-3.0 (un archivo MIT) · nivel 2 · 60/100 · recomendado en «TTS ligero y rápido»
- **Qué es:** edge-tts, módulo Python y CLI no oficial para usar el servicio TTS en línea de Microsoft Edge, de @rany2. Licencia LGPL-3.0, salvo un archivo bajo MIT (GitHub muestra NOASSERTION). Es maduro (~13k estrellas, 7.3.1).
- **Cuándo elegirlo:** Casos: Preparar una voz de prueba online; Explorar voces disponibles.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python y pipx; internet; texto no sensible; hardware prerequisites; API de IA: no; Python y pipx; internet; texto no sensible.
- **Instalación (documentada en la fuente; no ejecutada):** `pipx install edge-tts` — fuente: https://github.com/rany2/edge-tts/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Genera un audio y subtítulos de una frase y escucha pronunciación y pausas Éxito: Puedes localizar MP3 y SRT y comprobar su contenido
- **Combina con:** `moviepy` [30/motores], `whisper` [29/stt], `ffmpeg` [12/edicion], `short-video-factory` [12/generativo]
- **Alternativas:** `luxtts`, `kokoro`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): kokoro. Servicio no oficial: riesgo de términos de uso y disponibilidad. No es inferencia local aunque el script se ejecute en tu PC; la biblioteca es independiente y el servicio puede cambiar sus condiciones o interfaz.

### RVC WebUI (`rvc`)

- **Repo:** https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI · MIT · nivel 2 · 58/100
- **Qué es:** RVC (Retrieval-based Voice Conversion WebUI), framework para convertir el timbre de voz, de RVC-Project. Licencia MIT. Es muy popular (~39k estrellas, 2.3.260718); el README principal está en chino.
- **Cuándo elegirlo:** Casos: Probar un efecto de voz consentido; Estudiar conversión frente a TTS.
- **Requisitos:** nivel 2: preparación media; Python 3.12 según guía; FFmpeg; modelo de conversión; voz autorizada; equipo; hardware prerequisites; API de IA: no; Python 3.12 según guía; FFmpeg; modelo de conversión; voz autorizada; equipo.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/README.md

  ```powershell
  py -3.12 -m venv .venv
  .venv\Scripts\activate
  python -m pip install --upgrade pip setuptools wheel
  ```
- **Primera prueba propuesta (no ejecutada):** Convierte un clip propio corto y compara claridad, tono y artefactos Éxito: Puedes reconocer entrada y voz objetivo del modelo
- **Combina con:** `gpt-sovits`, `ffmpeg` [12/edicion], `obs-studio` [12/edicion]
- **Riesgos y avisos:** Sin alternativas declaradas. Riesgo de suplantación de voz. RVC convierte audio existente y no es por sí solo texto a voz; menos de diez minutos es un reclamo de entrenamiento y no una garantía universal.

### IndexTTS (`index-tts`)

- **Repo:** https://github.com/index-tts/index-tts · bilibili Model Use License · nivel 2 · 53/100 · alternativa en «Clonación de voz y TTS multilingüe»
- **Qué es:** IndexTTS, sistema de TTS zero-shot «de nivel industrial» con control de duración y emoción, de bilibili (organización index-tts). Usa el «bilibili Model Use License Agreement» propio (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Prototipar narración con duración controlada; Estudiar expresión de voz.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; uv; entorno compatible; pesos; GPU según configuración; audio autorizado; hardware prerequisites; API de IA: no; uv; entorno compatible; pesos; GPU según configuración; audio autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/index-tts/index-tts/blob/main/README.md

  ```bash
  git clone https://github.com/index-tts/index-tts.git && cd index-tts

  pip install -U uv  # or see the link above for other install methods
  ```
- **Primera prueba propuesta (no ejecutada):** Sintetiza una frase con duración acotada y comprueba pronunciación y tiempo real obtenido Éxito: Puedes identificar controles que afectaron al resultado
- **Combina con:** `whisperx` [29/stt], `ffmpeg` [12/edicion], `pipecat` [29/voz-agentes]
- **Alternativas:** `gpt-sovits`, `f5-tts`, `cosyvoice`, `fish-speech`
- **Riesgos y avisos:** Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): cosyvoice. Licencia no OSI; riesgo de suplantación de voz. Industrial-level es una descripción del autor y no una certificación; algunos controles emocionales requieren activar el módulo específico.

### LuxTTS (`luxtts`)

- **Repo:** https://github.com/ysharma3501/LuxTTS · Apache-2.0 · nivel 2 · 52/100 · alternativa en «TTS ligero y rápido»
- **Qué es:** LuxTTS, modelo TTS ligero basado en ZipVoice para clonar voces, de @ysharma3501. Licencia Apache-2.0 para modelo y código. Es reciente (enero de 2026, ~5.6k estrellas) y no cambia desde junio de 2026.
- **Cuándo elegirlo:** Casos: Preparar una narración local; Explorar adaptación de voz consentida.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; dependencias; modelo; equipo; voz con permiso; hardware prerequisites; API de IA: no; Python; dependencias; modelo; equipo; voz con permiso.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/ysharma3501/LuxTTS/blob/master/README.md

  ```bash
  git clone https://github.com/ysharma3501/LuxTTS.git
  cd LuxTTS
  pip install -r requirements.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Sintetiza una frase y mide tiempo y calidad en tu propio equipo Éxito: Puedes comparar texto, referencia y audio generado
- **Combina con:** `comfyui` [11/interfaces], `pipecat` [29/voz-agentes], `moviepy` [30/motores]
- **Alternativas:** `edge-tts`, `kokoro`
- **Riesgos y avisos:** Alternativas (elige una): kokoro. Se quitan litellm y cosmos de las combinaciones (sin relación). La cifra de 150 veces tiempo real es del autor y no una garantía de latencia o calidad en cualquier equipo.

### Kokoro (`kokoro`)

- **Repo:** https://github.com/hexgrad/kokoro · Apache-2.0 · nivel 2 · 48/100 · alternativa en «TTS ligero y rápido»
- **Qué es:** kokoro, librería de inferencia para Kokoro-82M, modelo TTS de pesos abiertos de 82 millones de parámetros, de @hexgrad. Licencia Apache-2.0. Tiene ~10k estrellas, pero no cambia desde agosto de 2025.
- **Cuándo elegirlo:** Casos: Narrar una nota propia; Probar una voz para una demo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; Kokoro y soundfile; espeak-ng según idioma; pesos; hardware prerequisites; API de IA: no; Python; Kokoro y soundfile; espeak-ng según idioma; pesos.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install kokoro` — fuente: https://github.com/hexgrad/kokoro/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera dos frases en español y revisa pronunciación y pausas Éxito: Puedes localizar el archivo de audio y reconocer voz e idioma seleccionados
- **Combina con:** `pipecat` [29/voz-agentes], `whisper-cpp` [29/stt], `moviepy` [30/motores]
- **Alternativas:** `edge-tts`, `luxtts`
- **Riesgos y avisos:** Alternativas (elige una): luxtts, edge-tts. Inactivo desde 2025. Los ejemplos con !pip y !apt son de notebook y no se pegan sin cambios en PowerShell; selecciona el idioma y sus dependencias.

### LiveKit Agents (`livekit-agents`)

- **Repo:** https://github.com/livekit/agents · Apache-2.0 · nivel 2 · 73/100 · alternativa en «Agentes de voz en tiempo real»
- **Qué es:** LiveKit Agents, framework para agentes de voz y vídeo en tiempo real sobre la infraestructura WebRTC de LiveKit. Licencia Apache-2.0; sus modelos de detección de turno usan la «LiveKit Model License». Es activo (~15k estrellas, 1.8.12).
- **Cuándo elegirlo:** Casos: Construir un asistente de voz; Evaluar conversación en tiempo real.
- **Requisitos:** nivel 2: preparación media; Python; LiveKit; proveedores o modelos locales; micrófono de prueba; hardware prerequisites; API de IA: opcional; Python; LiveKit; proveedores o modelos locales; micrófono de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "livekit-agents[openai,deepgram,cartesia]"` — fuente: https://github.com/livekit/agents/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Usa terminal mode para una conversación breve y revisa cada etapa antes de añadir telefonía Éxito: Puedes comprobar audio de entrada, modelo y respuesta
- **Combina con:** `kokoro` [29/tts], `ollama` [8/motores], `whisper-cpp` [29/stt], `elevenlabs-python` [29/tts]
- **Alternativas:** `pipecat`, `dograh`, `ten-framework`
- **Riesgos y avisos:** Alternativas (elige una): pipecat, dograh. El MCP del README consulta documentación para desarrollar y no controla automáticamente tus agentes; usar Ollama no vuelve locales todos los componentes de….

### Pipecat (`pipecat`)

- **Repo:** https://github.com/pipecat-ai/pipecat · BSD-2-Clause · nivel 2 · 73/100 · recomendado en «Agentes de voz en tiempo real»
- **Qué es:** Pipecat, framework open source en Python para agentes de voz y multimodales en tiempo real, creado por Daily. Licencia BSD-2-Clause. Es maduro y muy activo (~17k estrellas, v1.16.0).
- **Cuándo elegirlo:** Casos: Prototipar un agente de voz; Comparar combinaciones STT/LLM/TTS.
- **Requisitos:** nivel 2: preparación media; uv; proveedores STT, LLM y TTS; micrófono; transporte local o remoto; hardware prerequisites; API de IA: opcional; uv; proveedores STT, LLM y TTS; micrófono; transporte local o remoto.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/pipecat-ai/pipecat/blob/main/README.md

  ```bash
  uv tool install "pipecat-ai[cli]"
  pipecat init
  ```
- **Primera prueba propuesta (no ejecutada):** Crea una prueba local de una pregunta y comprueba transcripción, respuesta y audio por separado Éxito: Puedes localizar en qué etapa falla la conversación
- **Combina con:** `kokoro` [29/tts], `whisper-cpp` [29/stt], `ollama` [8/motores], `nemo` [29/stt], `elevenlabs-python` [29/tts]
- **Alternativas:** `livekit-agents`, `dograh`, `ten-framework`
- **Riesgos y avisos:** Alternativas (elige una): livekit-agents, dograh. Tiene skills específicos de Claude Code; un agente que genera el código no aporta automáticamente el runtime ni créditos de telefonía o voz.

### dograh (`dograh`)

- **Repo:** https://github.com/dograh-hq/dograh · BSD-2-Clause · nivel 2 · 62/100 · alternativa en «Agentes de voz en tiempo real»
- **Qué es:** Dograh AI, plataforma open source y autoalojable para construir agentes de voz, alternativa a Vapi y Retell. Licencia BSD-2-Clause. Tiene ~6k estrellas y es activa (dograh-v1.51.0).
- **Cuándo elegirlo:** Casos: Diseñar un agente de voz; Editar un workflow mediante MCP.
- **Requisitos:** nivel 2: preparación media; Docker o entorno documentado; proveedores de voz/modelo; micrófono de prueba; hardware prerequisites; API de IA: depends; Docker o entorno documentado; proveedores de voz/modelo; micrófono de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `/plugin marketplace add dograh-hq/dograh-plugins` — fuente: https://github.com/dograh-hq/dograh/blob/main/docs/deployment/docker.mdx
- **Primera prueba propuesta (no ejecutada):** Crea un flujo de borrador y prueba una conversación local sin realizar llamadas telefónicas Éxito: Puedes inspeccionar nodos, proveedores y transiciones
- **Combina con:** `ollama` [8/motores], `whisper-cpp` [29/stt], `kokoro` [29/tts]
- **Alternativas:** `pipecat`, `livekit-agents`, `ten-framework`
- **Riesgos y avisos:** Alternativas (elige una): pipecat, livekit-agents. Revisa el túnel público y el registro abierto por defecto. MCP permite consultar y guardar borradores desde clientes compatibles; los plugins Claude y Codex ayudan a configurar y no incluyen suscripciones de voz.

### TEN Framework (`ten-framework`)

- **Repo:** https://github.com/TEN-framework/ten-framework · Apache-2.0 con condiciones adicionales (Agora) · nivel 3 · 46/100 · alternativa en «Agentes de voz en tiempo real»
- **Qué es:** Framework de código abierto impulsado por Agora para agentes de voz conversacionales. Muy activo. Se publica con licencia Apache-2.0 con restricciones adicionales, por lo que no es una licencia OSI.
- **Cuándo elegirlo:** Casos: montar un asistente de voz que conversa en tiempo real con un LLM; construir un agente de voz con avatar o con transcripción en vivo.
- **Requisitos:** nivel 3: framework de voz con diseñador visual y varios proveedores; Python, package.json; API de IA: sí; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://github.com/TEN-framework/ten-framework/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo, rellena `.env` con las claves de Agora, OpenAI, Deepgram y ElevenLabs y ejecuta `docker compose up -d`; abre el ejemplo de voz en el navegador. Éxito: Puedes hablar con un agente que responde por voz en tiempo real.
- **Combina con:** `dify` [3/visual], `openclaw` [21/asistentes], `vibevoice` [29/tts], `whisper` [29/stt], `elevenlabs-python` [29/tts]
- **Alternativas:** `pipecat`, `livekit-agents`, `dograh`
- **Riesgos y avisos:** Alternativa de Pipecat, LiveKit Agents y Dograh; revisa la licencia antes de usarlo en productos.

### ACE-Step-1.5 (`ace-step-1.5`)

- **Repo:** https://github.com/ace-step/ACE-Step-1.5 · MIT · nivel 3 · 70/100 · recomendado en «Generación de música»
- **Qué es:** ACE-Step 1.5, modelo y herramientas open source para generar música en local, de ace-step (ACE Studio y StepFun). Licencia MIT. Tiene ~15k estrellas (v0.1.8); la serie XL (DiT de 4B) salió en abril de 2026.
- **Cuándo elegirlo:** Casos: Explorar una base musical de prueba; Comparar variantes de generación local.
- **Requisitos:** nivel 3: preparación pesada; Python 3.11–3.12; uv; modelo y equipo compatibles; espacio para descarga; hardware prerequisites; API de IA: no; Python 3.11–3.12; uv; modelo y equipo compatibles; espacio para descarga.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md

  ```bash
  # 2. Clone & install
  git clone https://github.com/ACE-Step/ACE-Step-1.5.git
  cd ACE-Step-1.5
  uv sync

  # 3. Launch Gradio UI (models auto-download on first run)
  uv run acestep
  ```
- **Primera prueba propuesta (no ejecutada):** Genera una pieza muy corta y revisa duración, coherencia y recursos consumidos Éxito: Puedes relacionar parámetros y salida
- **Combina con:** `vllm` [23/serving], `ffmpeg` [12/edicion], `rubberband` [29/audio]
- **Alternativas:** `yue`, `audiocraft`
- **Riesgos y avisos:** Sin alternativas declaradas. CUDA es recomendado y existen rutas MPS, ROCm, XPU o CPU; disponibilidad de una ruta no garantiza igual velocidad o memoria en todas.

### YuE2 (`yue`)

- **Repo:** https://github.com/multimodal-art-projection/YuE · Apache-2.0 · nivel 4 · 67/100 · alternativa en «Generación de música»
- **Qué es:** Modelo de investigación de código abierto del proyecto Multimodal Art Projection (M-A-P). Desde septiembre de 2026 el repositorio aloja YuE2; el YuE original se conserva en la rama YuE-v1.
- **Cuándo elegirlo:** Casos: generar una maqueta de canción con letra propia para un proyecto personal o académico; editar la armonía de una canción generada manteniendo la melodía. Evítalo si no tienes el hardware o no aceptas la licencia de los pesos.
- **Requisitos:** nivel 4: preparación difícil, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/multimodal-art-projection/YuE.git` — fuente: https://github.com/multimodal-art-projection/YuE/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** En Linux con una GPU NVIDIA de 24 GB, clona el repo, ejecuta `python -m pip install .` y genera una canción con `YuE2Pipeline`. Éxito: Obtienes un audio estéreo y la partitura ABC editable.
- **Combina con:** `claude-code` [20/terminal], `pytorch` [24/entrenamiento], `audacity` [29/audio]
- **Alternativas:** `ace-step-1.5`, `audiocraft`
- **Riesgos y avisos:** Alternativa abierta de ACE-Step 1.5 y AudioCraft (MusicGen). El README dice que YuE2 compite con Suno v5/v6 en WildSongBench [DATO NO VERIFICADO: benchmark del….

### AudioCraft (`audiocraft`)

- **Repo:** https://github.com/facebookresearch/audiocraft · MIT · nivel 2 · 52/100 · alternativa en «Generación de música»
- **Qué es:** AudioCraft, librería PyTorch de Meta para investigación en generación de audio (MusicGen y AudioGen). El código es MIT y los pesos son CC-BY-NC 4.0 (no comercial). Tiene ~24k estrellas y no cambia desde marzo de 2026.
- **Cuándo elegirlo:** Casos: Explorar generación de música; Estudiar sonidos a partir de texto.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python 3.9 y PyTorch 2.1 según guía; modelo; GPU según tamaño; texto propio; hardware prerequisites; API de IA: no; Python 3.9 y PyTorch 2.1 según guía; modelo; GPU según tamaño; texto propio.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install -U audiocraft` — fuente: https://github.com/facebookresearch/audiocraft/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera una muestra corta y compara su relación con el prompt sin publicar el resultado Éxito: Puedes identificar modelo, duración y artefactos
- **Combina con:** `ffmpeg` [12/edicion], `moviepy` [30/motores], `remotion` [30/motores], `rubberband` [29/audio], `audacity` [29/audio]
- **Alternativas:** `ace-step-1.5`, `yue`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Pesos no comerciales y dependencias antiguas. Los pesos publicados no permiten asumir uso comercial porque el código sea MIT; las alternativas de instalación del README no se ejecutan todas juntas.

### Audacity (`audacity`)

- **Repo:** https://github.com/audacity/audacity · GPL-3.0 (mayoría de archivos GPL-2.0-or-later) · nivel 1 · 67/100
- **Qué es:** Editor de audio libre (GPLv3; la mayoría de archivos GPLv2 o posterior) mantenido por el equipo de Audacity con apoyo de Muse Group. Referencia histórica en edición de audio libre.
- **Cuándo elegirlo:** Casos: limpiar, cortar y normalizar una grabación de voz o podcast; editar stems separados con IA antes de mezclarlos.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; C++, CMakeLists.txt; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/audacity/audacity/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga Audacity desde su web, graba o importa un audio y aplica reducción de ruido y normalización. Éxito: Exportas un MP3 o WAV más limpio.
- **Combina con:** `ffmpeg` [12/edicion], `demucs`, `whisper-cpp` [29/stt], `audiocraft` [29/musica], `yue` [29/musica]

### pyannote.audio (`pyannote-audio`)

- **Repo:** https://github.com/pyannote/pyannote-audio · MIT · nivel 3 · 64/100
- **Qué es:** Kit de diarización de hablantes en Python sobre PyTorch (organización pyannote; pyannoteAI ofrece el servicio premium). Licencia MIT para el código; los modelos se publican en Hugging Face con condiciones propias.
- **Cuándo elegirlo:** Casos: Separar por hablante la grabación de una reunión; Añadir hablantes a una transcripción.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, necesita GPU; Jupyter Notebook, pyproject.toml; hardware model_dependent; API de IA: opcional; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install pyannote.audio` — fuente: https://github.com/pyannote/pyannote-audio/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta community-1 sobre un audio corto con dos voces de prueba Éxito: Los segmentos alternan entre dos hablantes con marcas de tiempo coherentes
- **Combina con:** `whisperx` [29/stt], `pytorch` [24/entrenamiento], `faster-whisper` [29/stt], `ffmpeg` [12/edicion], `sherpa-onnx` [29/stt]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Diarizar personas tiene implicaciones de privacidad: informa a los participantes. Las cifras del README (DER, velocidad en H100) son del autor.

### Ultimate Vocal Remover (UVR) (`ultimate-vocal-remover`)

- **Repo:** https://github.com/Anjok07/ultimatevocalremovergui · MIT · nivel 3 · 58/100
- **Qué es:** Aplicación de código abierto (MIT) de Anjok07 y aufr33, referencia popular para separar voces. La última versión publicada es la v5.6 (2023); el README remite a una actualización de desarrollo de octubre de 2026.
- **Cuándo elegirlo:** Casos: obtener la pista instrumental o la voz aislada de una canción propia; preparar stems para remezclar o practicar con una canción.
- **Requisitos:** nivel 3: preparación sencilla, app o instalador listo para usar, necesita GPU; Python, requirements.txt; hardware model_dependent; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el instalador para tu sistema desde las releases, abre una canción y separa con un modelo MDX-Net. Éxito: Obtienes dos archivos: voz e instrumental.
- **Combina con:** `ffmpeg` [12/edicion], `rubberband`, `demucs`

### Demucs (`demucs`)

- **Repo:** https://github.com/adefossez/demucs · MIT · nivel 3 · 56/100
- **Qué es:** Versión mantenida oficialmente por Alexandre Défossez, autor de Demucs, tras dejar Meta (y archivarse facebookresearch/demucs). El código es MIT. El propio autor avisa de que no trabaja activamente en él: respuestas lentas y sin funciones…
- **Cuándo elegirlo:** Casos: separar la voz y la batería de una canción propia para remezclar; generar stems para karaoke o práctica musical.
- **Requisitos:** nivel 3: preparación sencilla, requiere programar con él, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `python3 -m pip install -U demucs` — fuente: https://github.com/adefossez/demucs/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `python3 -m pip install -U demucs` y ejecuta `demucs cancion.mp3`. Éxito: Obtienes una carpeta con las pistas separadas (drums, bass, vocals, other).
- **Combina con:** `ffmpeg` [12/edicion], `pytorch` [24/entrenamiento], `ultimate-vocal-remover`, `audacity`

### earshot (`earshot`)

- **Repo:** https://github.com/Leonxlnx/earshot · MIT · nivel 2 · 55/100
- **Qué es:** earshot, «oídos para agentes de código»: herramientas locales de análisis de audio, de @Leonxlnx. Licencia MIT. Es muy reciente (octubre de 2026, ~4.9k estrellas, v0.4.1).
- **Cuándo elegirlo:** Casos: Revisar una mezcla con un agente; Analizar un efecto sonoro.
- **Requisitos:** nivel 2: preparación media; Python; uv; espacio para modelos CPU; audio propio; cliente MCP opcional; hardware prerequisites; API de IA: opcional; Python; uv; espacio para modelos CPU; audio propio; cliente MCP opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Leonxlnx/earshot/blob/main/README.md

  ```bash
  uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
  earshot doctor --fetch     # downloads the two models now (~1.1 GB)
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta doctor y analiza un clip corto antes de solicitar modificaciones o generar sonidos Éxito: Puedes revisar informe, segmentos y archivo original
- **Combina con:** `claude-code` [20/terminal], `remotion` [30/motores], `ffmpeg` [12/edicion]
- **Riesgos y avisos:** Sin alternativas declaradas. Expone MCP y conserva rutas offline; el material de referencia de pago no viene incluido y hay que aportar grabaciones autorizadas.

### rubberband (`rubberband`)

- **Repo:** https://github.com/breakfastquay/rubberband · GPL-2.0 · nivel 2 · 42/100
- **Qué es:** Rubber Band Library, biblioteca y utilidad para estirar el tiempo y cambiar el tono de audio, de Chris Cannam (Breakfast Quay). Licencia GPL-2.0+, con licencia comercial disponible.
- **Cuándo elegirlo:** Casos: Ajustar duración de una narración; Explorar cambio de tono.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Biblioteca o utilidad compilada; libsndfile; audio de prueba; hardware prerequisites; API de IA: no; Biblioteca o utilidad compilada; libsndfile; audio de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/breakfastquay/rubberband/blob/default/README.md
- **Primera prueba propuesta (no ejecutada):** Cambia ligeramente el tempo de una copia de audio y compara duración y artefactos Éxito: Puedes reconocer qué cambió en tiempo y tono
- **Combina con:** `ffmpeg` [12/edicion], `ace-step-1.5` [29/musica], `audiocraft` [29/musica], `ultimate-vocal-remover`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Es procesamiento de señal, no clonación de voz; los parámetros de ejemplo son marcadores y deben sustituirse con valores reales.

### rnnoise (`rnnoise`)

- **Repo:** https://github.com/xiph/rnnoise · BSD-3-Clause · nivel 2 · 41/100
- **Qué es:** RNNoise, biblioteca de supresión de ruido basada en una red neuronal recurrente, de Xiph.Org (algoritmo de Jean-Marc Valin). Licencia BSD-3-Clause. Es madura y estable (~6k estrellas, v0.2) y no cambia desde febrero de 2025.
- **Cuándo elegirlo:** Casos: Reducir ruido de una grabación; Estudiar una red de supresión de ruido.
- **Requisitos:** nivel 2: preparación media; Compilador y autotools; modelo descargado; audio RAW mono 16-bit 48 kHz; hardware prerequisites; API de IA: no; Compilador y autotools; modelo descargado; audio RAW mono 16-bit 48 kHz.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/xiph/rnnoise/blob/main/README
- **Primera prueba propuesta (no ejecutada):** Procesa una copia corta de audio con ruido y escucha si mejora sin deformar la voz Éxito: Puedes comparar original y salida y verificar formato
- **Combina con:** `ffmpeg` [12/edicion], `obs-studio` [12/edicion], `whisper-cpp` [29/stt]
- **Riesgos y avisos:** Sin alternativas declaradas. La demo recibe y devuelve PCM RAW, no WAV; autogen descarga archivos de modelo y GitHub es una copia de conveniencia del repositorio Xiph.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-29.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Audio, transcripción, voz y música», lee `docs/alexandria/categoria-29.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-29.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
