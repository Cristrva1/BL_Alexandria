# Alexandría para agentes · Transcripción (voz a texto)

Categoría 29 «Audio, transcripción, voz y música» › subcategoría `stt`. 7 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=29&sub=stt · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `whisper-cpp` | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y… | 1 Básico | 70 | MIT (OSI permisiva) | recomendado |
| `faster-whisper` | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU… | 2 Intermedio | 66 | MIT (OSI permisiva) | alternativa |
| `nemo` | Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con… | 3 Avanzado | 66 | Apache-2.0 (OSI permisiva) | recomendado |
| `sherpa-onnx` | Motor de voz offline con ONNX Runtime: reconocimiento, síntesis, VAD… | 3 Avanzado | 65 | Apache-2.0 (OSI permisiva) | sin grupo |
| `buzz` | Transcribe grabaciones y exporta subtítulos en una aplicación de escritorio que… | 1 Básico | 64 | MIT (OSI permisiva) | sin grupo |
| `whisper` | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución… | 2 Intermedio | 64 | MIT (OSI permisiva) | alternativa |
| `whisperx` | Pipeline de transcripción que añade alineación temporal de palabras y funciones… | 2 Intermedio | 64 | BSD-2-Clause (OSI permisiva) | alternativa |

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-29-stt.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Transcripción (voz a texto)», lee `docs/alexandria/categoria-29-stt.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-29-stt.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
