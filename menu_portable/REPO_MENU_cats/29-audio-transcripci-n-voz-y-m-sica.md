# 29. Audio, transcripción, voz y música — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ace-step-1.5`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=musica,text2music,python

**Qué es:** Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño.
**Stack:** Python 3.11–3.12; uv; modelo y equipo compatibles; espacio para descarga
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ejecución local no necesita API de pago; hardware y modelos tienen sus costes y condiciones; el servicio web tiene términos independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. CUDA es recomendado y existen rutas MPS, ROCm, XPU o CPU; disponibilidad de una ruta no garantiza igual velocidad o memoria en todas
- Coste: Sin pago a un modelo en la ruta básica. La ejecución local no necesita API de pago; hardware y modelos tienen sus costes y condiciones; el servicio web tiene términos independientes
- Equipo: Preparación según la ruta elegida. Python 3.11–3.12; uv; modelo y equipo compatibles; espacio para descarga
**Repo:** https://github.com/ace-step/ACE-Step-1.5

**Instalación** [+]:

```
# 2. Clone & install
git clone https://github.com/ACE-Step/ACE-Step-1.5.git
cd ACE-Step-1.5
uv sync

# 3. Launch Gradio UI (models auto-download on first run)
uv run acestep
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar una base musical de prueba; Comparar variantes de generación local
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera una pieza muy corta y revisa duración, coherencia y recursos consumidos
**Qué comprobar:** Puedes relacionar parámetros y salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `ffmpeg`, `rubberband`
**Alternativas (elige una):** `yue`, `audiocraft`

## `audacity`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=audio,editor,cpp,app

**Qué es:** Editor y grabador de audio multipista libre para Windows, macOS y Linux, con efectos, análisis y plugins, incluidos plugins de IA locales de Intel.
**Stack:** C++, CMakeLists.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/audacity/audacity

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/audacity/audacity/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: limpiar, cortar y normalizar una grabación de voz o podcast; editar stems separados con IA antes de mezclarlos
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga Audacity desde su web, graba o importa un audio y aplica reducción de ruido y normalización.
**Qué comprobar:** Exportas un MP3 o WAV más limpio.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `demucs`, `whisper-cpp`, `audiocraft`, `yue`

## `audiocraft`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=audio,inference,training,python

**Qué es:** Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec.
**Stack:** Python 3.9 y PyTorch 2.1 según guía; modelo; GPU según tamaño; texto propio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Código MIT y pesos CC BY-NC 4.0; ejecución propia no exige API pero hardware y licencia de uso son separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Los pesos publicados no permiten asumir uso comercial porque el código sea MIT; las alternativas de instalación del README no se ejecutan todas juntas
- Coste: El coste depende del proveedor o la ruta. Código MIT y pesos CC BY-NC 4.0; ejecución propia no exige API pero hardware y licencia de uso son separados
- Equipo: Preparación según la ruta elegida. Python 3.9 y PyTorch 2.1 según guía; modelo; GPU según tamaño; texto propio
**Repo:** https://github.com/facebookresearch/audiocraft

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/facebookresearch/audiocraft/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar generación de música; Estudiar sonidos a partir de texto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera una muestra corta y compara su relación con el prompt sin publicar el resultado
**Qué comprobar:** Puedes identificar modelo, duración y artefactos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `moviepy`, `remotion`, `rubberband`, `audacity`
**Alternativas (elige una):** `yue`, `ace-step-1.5`

## `cosyvoice`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue.
**Stack:** Conda y Python 3.10 según guía; submódulos; pesos; FFmpeg o sox según ruta
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ruta propia no necesita API; hardware, datos y modelos externos tienen sus condiciones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto pertenece a FunAudioLLM; variantes de vLLM requieren entornos específicos y no conviene mezclar todas las dependencias en uno
- Coste: Sin pago a un modelo en la ruta básica. La ruta propia no necesita API; hardware, datos y modelos externos tienen sus condiciones
- Equipo: Preparación según la ruta elegida. Conda y Python 3.10 según guía; submódulos; pesos; FFmpeg o sox según ruta
**Repo:** https://github.com/QwenAudio/CosyVoice

**Instalación** [+]:

```
git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
    # If you failed to clone the submodule due to network failures, please run the following command until success
    cd CosyVoice
    git submodule update --init --recursive
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar síntesis multilingüe; Estudiar streaming de voz
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Descarga una variante compatible y prueba una frase del idioma elegido
**Qué comprobar:** Puedes comprobar voz, texto y archivo generado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pipecat`, `vllm`, `ffmpeg`, `wan2-2`
**Alternativas (elige una):** `fish-speech`, `index-tts`, `f5-tts`

## `demucs`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=audio,music,separation,pytorch

**Qué es:** Modelo de separación de fuentes musicales (voz, batería, bajo y resto) con Hybrid Transformer; continuación mantenida por su autor tras archivarse el repo de Meta.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/adefossez/demucs

**Instalación** [+]:

```
python3 -m pip install -U demucs
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: separar la voz y la batería de una canción propia para remezclar; generar stems para karaoke o práctica musical
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `python3 -m pip install -U demucs` y ejecuta `demucs cancion.mp3`.
**Qué comprobar:** Obtienes una carpeta con las pistas separadas (drums, bass, vocals, other).
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `pytorch`, `ultimate-vocal-remover`, `audacity`

## `dograh`
role=app · exec=hybrid · setup=medium · mcp=True · prov=— · tags=voz-agentes,agent,python

**Qué es:** Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables.
**Stack:** Docker o entorno documentado; proveedores de voz/modelo; micrófono de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Autoalojamiento no incluye STT, TTS, LLM o telefonía; Cloud y proveedores tienen tarifas o cuotas propias
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. MCP permite consultar y guardar borradores desde clientes compatibles; los plugins Claude y Codex ayudan a configurar y no incluyen suscripciones de voz
- Coste: El coste depende del proveedor o la ruta. Autoalojamiento no incluye STT, TTS, LLM o telefonía; Cloud y proveedores tienen tarifas o cuotas propias
- Equipo: Preparación según la ruta elegida. Docker o entorno documentado; proveedores de voz/modelo; micrófono de prueba
**Repo:** https://github.com/dograh-hq/dograh

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/dograh-hq/dograh/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar un agente de voz; Editar un workflow mediante MCP
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un flujo de borrador y prueba una conversación local sin realizar llamadas telefónicas
**Qué comprobar:** Puedes inspeccionar nodos, proveedores y transiciones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `whisper-cpp`, `kokoro`
**Alternativas (elige una):** `pipecat`, `livekit-agents`, `ten-framework`

## `earshot`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=local · tags=edicion,mcp,python

**Qué es:** Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP.
**Stack:** Python; uv; espacio para modelos CPU; audio propio; cliente MCP opcional
**Acceso y costes:**
- API de IA: API de IA opcional. Análisis local en CPU con descarga inicial de modelos; agente, generación opcional y referencias musicales tienen costes o licencias separados
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Expone MCP y conserva rutas offline; el material de referencia de pago no viene incluido y hay que aportar grabaciones autorizadas
- Coste: El coste depende del proveedor o la ruta. Análisis local en CPU con descarga inicial de modelos; agente, generación opcional y referencias musicales tienen costes o licencias separados
- Equipo: Preparación según la ruta elegida. Python; uv; espacio para modelos CPU; audio propio; cliente MCP opcional
**Repo:** https://github.com/Leonxlnx/earshot

**Instalación** [+]:

```
uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
earshot doctor --fetch     # downloads the two models now (~1.1 GB)
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar una mezcla con un agente; Analizar un efecto sonoro
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta doctor y analiza un clip corto antes de solicitar modificaciones o generar sonidos
**Qué comprobar:** Puedes revisar informe, segmentos y archivo original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `remotion`, `ffmpeg`

## `edge-tts`
role=library · exec=cloud · setup=easy · mcp=False · prov=— · tags=tts,speech-synthesis,text-to-speech,python

**Qué es:** Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge.
**Stack:** Python y pipx; internet; texto no sensible
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el servicio online de Microsoft Edge sin pedir una clave propia en el ejemplo; no se confirma garantía de coste, cuota o SLA
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. No es inferencia local aunque el script se ejecute en tu PC; la biblioteca es independiente y el servicio puede cambiar sus condiciones o interfaz
- Coste: Coste por confirmar. Usa el servicio online de Microsoft Edge sin pedir una clave propia en el ejemplo; no se confirma garantía de coste, cuota o SLA
- Equipo: Preparación según la ruta elegida. Python y pipx; internet; texto no sensible
**Repo:** https://github.com/rany2/edge-tts

**Instalación** [+]:

```
pipx install edge-tts
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una voz de prueba online; Explorar voces disponibles
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera un audio y subtítulos de una frase y escucha pronunciación y pausas
**Qué comprobar:** Puedes localizar MP3 y SRT y comprobar su contenido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `moviepy`, `whisper`, `ffmpeg`, `short-video-factory`
**Alternativas (elige una):** `kokoro`

## `elevenlabs-python`
role=library · exec=hybrid · setup=easy · mcp=False · prov=elevenlabs · tags=tts,voice,api,python

**Qué es:** SDK oficial de Python para la API de pago de ElevenLabs: voz sintética, clonación, transcripción, música y agentes de voz.
**Stack:** Python, pyproject.toml, requirements.txt
**Acceso y costes:**
- API de IA: API de IA necesaria. Toda llamada usa la API de ElevenLabs con tu ELEVENLABS_API_KEY.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No ejecuta modelos localmente: es un cliente de un servicio en la nube.
- Coste: Consumo de APIs o servicios. Consumo por caracteres, minutos o créditos según el plan de ElevenLabs; el SDK es gratuito.
- Equipo: Equipo normal; revisar dependencias. Python 3.8 o superior y conexión a internet.
**Repo:** https://github.com/elevenlabs/elevenlabs-python

**Instalación** [+]:

```
pip install elevenlabs
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Generar una locución para un video; Prototipar un agente de voz conectado a la API
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Convierte una frase corta a voz con una voz predefinida
**Qué comprobar:** Obtienes un MP3 reproducible y el consumo aparece en tu cuenta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openmontage`, `pipecat`, `livekit-agents`, `video-use`, `remotion-superpowers`, `ten-framework`

## `f5-tts`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=tts,voice-cloning,pytorch,speech

**Qué es:** Síntesis de voz con clonación a partir de pocos segundos de audio de referencia, basada en flow matching con Diffusion Transformer; incluye app Gradio y CLI.
**Stack:** Python, Dockerfile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/SWivid/F5-TTS

**Instalación** [+]:

```
pip install f5-tts
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: generar narración con tu propia voz a partir de una muestra corta; prototipar voces para un proyecto de investigación sin uso comercial
**Evita si:** no tienes el hardware o no aceptas la licencia de los pesos
**Primera prueba propuesta:** Instala PyTorch y `pip install f5-tts`; ejecuta `f5-tts_infer-gradio` y genera audio con una referencia de tu voz.
**Qué comprobar:** Obtienes un audio con el texto leído imitando la voz de referencia.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `ffmpeg`, `gradio`
**Alternativas (elige una):** `fish-speech`, `cosyvoice`

## `faster-whisper`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=stt,audio,python

**Qué es:** Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización.
**Stack:** Python; CTranslate2; CPU o CUDA/cuDNN compatibles; modelo y audio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API de pago para inferencia propia; hardware y almacenamiento aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Las dependencias CUDA y cuDNN cambian con CTranslate2; el ahorro de memoria y velocidad depende del modelo y parámetros
- Coste: Sin pago a un modelo en la ruta básica. Sin API de pago para inferencia propia; hardware y almacenamiento aparte
- Equipo: Preparación según la ruta elegida. Python; CTranslate2; CPU o CUDA/cuDNN compatibles; modelo y audio
**Repo:** https://github.com/SYSTRAN/faster-whisper

**Instalación** [+]:

```
pip install faster-whisper
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Transcribir lotes pequeños; Comparar CPU con GPU
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Transcribe un clip corto con una configuración adecuada al equipo y compara salida y tiempo
**Qué comprobar:** Puedes revisar modelo, cuantización y resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `whisperx`, `pipecat`, `moviepy`, `ai-youtube-shorts-generator`, `moneyprinterturbo`, `obs-studio`
**Alternativas (elige una):** `whisper-cpp`

## `fish-speech`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante.
**Stack:** Entorno y GPU compatibles; modelo con licencia aplicable; texto y voz autorizados
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Código y pesos actuales usan Fish Audio Community License; S2-Pro conserva Research License y no se presume uso comercial idéntico
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La disponibilidad del código no equivale a Apache o MIT ni a un servicio API gratuito; sigue la guía de la variante elegida
- Coste: El coste depende del proveedor o la ruta. Código y pesos actuales usan Fish Audio Community License; S2-Pro conserva Research License y no se presume uso comercial idéntico
- Equipo: Preparación según la ruta elegida. Entorno y GPU compatibles; modelo con licencia aplicable; texto y voz autorizados
**Repo:** https://github.com/fishaudio/fish-speech

**Instalación** [?]:

```
Seguir la instalación original: https://speech.fish.audio/install/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar generación expresiva; Preparar una prueba de voz multilingüe
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige Drama 3 o S2-Pro y prueba una frase corta después de revisar sus condiciones
**Qué comprobar:** Puedes distinguir la variante y su licencia
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pipecat`, `ffmpeg`, `whisperx`
**Alternativas (elige una):** `cosyvoice`, `gpt-sovits`, `f5-tts`

## `gpt-sovits`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y datos.
**Stack:** Conda; Python 3.10; PyTorch compatible; modelos; audio con permiso; GPU según tarea
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ruta propia no exige API; GPU, datos y licencias de componentes aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El lema de un minuto describe few-shot y no una garantía de calidad con cualquier grabación o idioma
- Coste: Sin pago a un modelo en la ruta básica. La ruta propia no exige API; GPU, datos y licencias de componentes aparte
- Equipo: Preparación según la ruta elegida. Conda; Python 3.10; PyTorch compatible; modelos; audio con permiso; GPU según tarea
**Repo:** https://github.com/RVC-Boss/GPT-SoVITS

**Instalación** [+]:

```
conda create -n GPTSoVits python=3.10
conda activate GPTSoVits

pip install -r extra-req.txt --no-deps
pip install -r requirements.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una voz para contenido propio; Estudiar adaptación con pocos ejemplos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sintetiza una frase corta con una voz autorizada y compara inteligibilidad antes de entrenar
**Qué comprobar:** Puedes revisar referencia, modelo y resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `rvc`, `ffmpeg`, `whisperx`, `videolingo`
**Alternativas (elige una):** `fish-speech`

## `index-tts`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción.
**Stack:** uv; entorno compatible; pesos; GPU según configuración; audio autorizado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Ejecución propia sin API obligatoria; aplica bilibili Model Use License Agreement y hardware independiente
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Industrial-level es una descripción del autor y no una certificación; algunos controles emocionales requieren activar el módulo específico
- Coste: El coste depende del proveedor o la ruta. Ejecución propia sin API obligatoria; aplica bilibili Model Use License Agreement y hardware independiente
- Equipo: Preparación según la ruta elegida. uv; entorno compatible; pesos; GPU según configuración; audio autorizado
**Repo:** https://github.com/index-tts/index-tts

**Instalación** [+]:

```
git clone https://github.com/index-tts/index-tts.git && cd index-tts

pip install -U uv  # or see the link above for other install methods
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar narración con duración controlada; Estudiar expresión de voz
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sintetiza una frase con duración acotada y comprueba pronunciación y tiempo real obtenido
**Qué comprobar:** Puedes identificar controles que afectaron al resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `whisperx`, `ffmpeg`, `pipecat`
**Alternativas (elige una):** `cosyvoice`

## `kokoro`
role=library · exec=local · setup=easy · mcp=False · prov=local · tags=tts,audio,local

**Qué es:** Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles.
**Stack:** Python; Kokoro y soundfile; espeak-ng según idioma; pesos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Modelo local Apache sin API de pago; equipo y recursos de voz independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Los ejemplos con !pip y !apt son de notebook y no se pegan sin cambios en PowerShell; selecciona el idioma y sus dependencias
- Coste: Sin pago a un modelo en la ruta básica. Modelo local Apache sin API de pago; equipo y recursos de voz independientes
- Equipo: Preparación según la ruta elegida. Python; Kokoro y soundfile; espeak-ng según idioma; pesos
**Repo:** https://github.com/hexgrad/kokoro

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/hexgrad/kokoro/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Narrar una nota propia; Probar una voz para una demo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera dos frases en español y revisa pronunciación y pausas
**Qué comprobar:** Puedes localizar el archivo de audio y reconocer voz e idioma seleccionados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pipecat`, `whisper-cpp`, `moviepy`
**Alternativas (elige una):** `luxtts`, `edge-tts`

## `livekit-agents`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=openai,anthropic,google · tags=audio,agents,video,python

**Qué es:** Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit.
**Stack:** Python; LiveKit; proveedores o modelos locales; micrófono de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Modelos, STT, TTS, transporte y Cloud se costean por separado; Ollama es una ruta LLM local documentada
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. El MCP del README consulta documentación para desarrollar y no controla automáticamente tus agentes; usar Ollama no vuelve locales todos los componentes de audio o transporte
- Coste: El coste depende del proveedor o la ruta. Modelos, STT, TTS, transporte y Cloud se costean por separado; Ollama es una ruta LLM local documentada
- Equipo: Preparación según la ruta elegida. Python; LiveKit; proveedores o modelos locales; micrófono de prueba
**Repo:** https://github.com/livekit/agents

**Instalación** [+]:

```
pip install "livekit-agents[openai,deepgram,cartesia]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un asistente de voz; Evaluar conversación en tiempo real
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa terminal mode para una conversación breve y revisa cada etapa antes de añadir telefonía
**Qué comprobar:** Puedes comprobar audio de entrada, modelo y respuesta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `kokoro`, `ollama`, `whisper-cpp`, `elevenlabs-python`
**Alternativas (elige una):** `pipecat`, `dograh`, `ten-framework`

## `luxtts`
role=library · exec=local · setup=easy · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local.
**Stack:** Python; dependencias; modelo; equipo; voz con permiso
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El autor declara modelo y código Apache-2.0; hardware y datos se costean aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La cifra de 150 veces tiempo real es del autor y no una garantía de latencia o calidad en cualquier equipo
- Coste: Sin pago a un modelo en la ruta básica. El autor declara modelo y código Apache-2.0; hardware y datos se costean aparte
- Equipo: Preparación según la ruta elegida. Python; dependencias; modelo; equipo; voz con permiso
**Repo:** https://github.com/ysharma3501/LuxTTS

**Instalación** [+]:

```
git clone https://github.com/ysharma3501/LuxTTS.git
cd LuxTTS
pip install -r requirements.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una narración local; Explorar adaptación de voz consentida
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sintetiza una frase y mide tiempo y calidad en tu propio equipo
**Qué comprobar:** Puedes comparar texto, referencia y audio generado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `comfyui`, `pipecat`, `moviepy`
**Alternativas (elige una):** `kokoro`

## `nemo`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=stt,tts,audio,python

**Qué es:** Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con recetas de inferencia y entrenamiento.
**Stack:** uv; entorno CUDA compatible; modelo de voz elegido; audio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Ejecución propia sin API obligatoria; GPU, pesos y datasets tienen condiciones independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El repositorio actual es NeMo Speech; las guías nightly y 3.0 estable son distintas y deben alinearse con la versión instalada
- Coste: Sin pago a un modelo en la ruta básica. Ejecución propia sin API obligatoria; GPU, pesos y datasets tienen condiciones independientes
- Equipo: Preparación según la ruta elegida. uv; entorno CUDA compatible; modelo de voz elegido; audio de prueba
**Repo:** https://github.com/NVIDIA-NeMo/Speech

**Instalación** [+]:

```
git clone https://github.com/NVIDIA-NeMo/Speech.git
cd Speech
uv sync --extra all --extra cu13     # CUDA 13.x (recommended) — use --extra cu12 for CUDA 12.x
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar modelos de voz de NVIDIA; Preparar un experimento ASR
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige la receta de transcripción y prueba un clip breve antes de entrenar
**Qué comprobar:** Puedes identificar checkpoint, configuración y salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nemotron`, `pipecat`, `pytorch`, `sherpa-onnx`
**Alternativas (elige una):** `whisperx`

## `omnivoice-studio`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=tts,audio,python

**Qué es:** App local de voz con modelos descargables,edición AGPL y una oferta comercial separada.
**Stack:** Instalador VoiceStudio para tu sistema; modelos; almacenamiento; voces autorizadas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La app AGPL puede usarse incluso comercialmente bajo sus términos; existe una edición cerrada comercial y pesos o voces con licencias separadas
- Claude Code: Referencia para la herramienta; no es una integración
- Codex: Referencia para la herramienta; no es una integración
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El nombre actual es VoiceStudio; pedir a Claude o Codex ayuda para instalar no es una integración de sus planes ni garantiza igual calidad en todos los idiomas anunciados
- Coste: El coste depende del proveedor o la ruta. La app AGPL puede usarse incluso comercialmente bajo sus términos; existe una edición cerrada comercial y pesos o voces con licencias separadas
- Equipo: Preparación según la ruta elegida. Instalador VoiceStudio para tu sistema; modelos; almacenamiento; voces autorizadas
**Repo:** https://github.com/debpalash/VoiceStudio

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/debpalash/VoiceStudio/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una narración local; Probar transcripción o doblaje de material propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Descarga un modelo compatible y sintetiza un párrafo propio antes de probar clonación
**Qué comprobar:** Puedes comprobar modelo, licencia y salida de audio
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `whisperx`, `ffmpeg`, `kokoro`
**Alternativas (elige una):** `videolingo`

## `pipecat`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google · tags=audio,agents,stt,tts,python

**Qué es:** Framework open source para agentes de voz y apps multimodales en tiempo real.
**Stack:** uv; proveedores STT, LLM y TTS; micrófono; transporte local o remoto
**Acceso y costes:**
- API de IA: API de IA opcional. Cada servicio tiene costes propios; documenta Whisper, Ollama y Piper locales además de proveedores Cloud
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: Modelos locales documentados. Tiene skills específicos de Claude Code; un agente que genera el código no aporta automáticamente el runtime ni créditos de telefonía o voz
- Coste: El coste depende del proveedor o la ruta. Cada servicio tiene costes propios; documenta Whisper, Ollama y Piper locales además de proveedores Cloud
- Equipo: Preparación según la ruta elegida. uv; proveedores STT, LLM y TTS; micrófono; transporte local o remoto
**Repo:** https://github.com/pipecat-ai/pipecat

**Instalación** [+]:

```
uv tool install "pipecat-ai[cli]"
pipecat init
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un agente de voz; Comparar combinaciones STT/LLM/TTS
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una prueba local de una pregunta y comprueba transcripción, respuesta y audio por separado
**Qué comprobar:** Puedes localizar en qué etapa falla la conversación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `kokoro`, `whisper-cpp`, `ollama`, `nemo`, `elevenlabs-python`
**Alternativas (elige una):** `livekit-agents`, `dograh`, `ten-framework`

## `pyannote-audio`
role=library · exec=hybrid · setup=medium · mcp=False · prov=local · tags=audio,diarization,pytorch,python

**Qué es:** Kit de PyTorch para diarización de hablantes (quién habla y cuándo) con modelos preentrenados y un servicio premium opcional.
**Stack:** Jupyter Notebook, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. community-1 corre localmente con un token de Hugging Face; precision-2 corre en los servidores de pyannoteAI con su propia clave.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Los pipelines abiertos se ejecutan localmente en CPU o GPU tras aceptar sus condiciones en Hugging Face.
- Coste: El coste depende del proveedor o la ruta. La ruta local no paga por uso; pyannoteAI ofrece créditos gratuitos y después cobra. La telemetría es opcional (PYANNOTE_METRICS_ENABLED).
- Equipo: Memoria y GPU según el modelo. Python 3.11 o superior y ffmpeg; GPU recomendable para audio largo.
**Repo:** https://github.com/pyannote/pyannote-audio

**Instalación** [+]:

```
pip install pyannote.audio
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Separar por hablante la grabación de una reunión; Añadir hablantes a una transcripción
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Ejecuta community-1 sobre un audio corto con dos voces de prueba
**Qué comprobar:** Los segmentos alternan entre dos hablantes con marcas de tiempo coherentes
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `whisperx`, `pytorch`, `faster-whisper`, `ffmpeg`, `sherpa-onnx`

## `rnnoise`
role=runtime · exec=local · setup=medium · mcp=False · prov=local · tags=edicion,model,c

**Qué es:** Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente.
**Stack:** Compilador y autotools; modelo descargado; audio RAW mono 16-bit 48 kHz
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no requiere API remota; cómputo y datos propios separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La demo recibe y devuelve PCM RAW, no WAV; autogen descarga archivos de modelo y GitHub es una copia de conveniencia del repositorio Xiph
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no requiere API remota; cómputo y datos propios separados
- Equipo: Preparación según la ruta elegida. Compilador y autotools; modelo descargado; audio RAW mono 16-bit 48 kHz
**Repo:** https://github.com/xiph/rnnoise

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/xiph/rnnoise/blob/main/README
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir ruido de una grabación; Estudiar una red de supresión de ruido
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Procesa una copia corta de audio con ruido y escucha si mejora sin deformar la voz
**Qué comprobar:** Puedes comparar original y salida y verificar formato
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `obs-studio`, `whisper-cpp`

## `rubberband`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=edicion,library,c

**Qué es:** Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas.
**Stack:** Biblioteca o utilidad compilada; libsndfile; audio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. GPL con alternativa comercial para determinados usos; no necesita API de IA y hardware separado
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es procesamiento de señal, no clonación de voz; los parámetros de ejemplo son marcadores y deben sustituirse con valores reales
- Coste: El coste depende del proveedor o la ruta. GPL con alternativa comercial para determinados usos; no necesita API de IA y hardware separado
- Equipo: Preparación según la ruta elegida. Biblioteca o utilidad compilada; libsndfile; audio de prueba
**Repo:** https://github.com/breakfastquay/rubberband

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/breakfastquay/rubberband/blob/default/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Ajustar duración de una narración; Explorar cambio de tono
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Cambia ligeramente el tempo de una copia de audio y compara duración y artefactos
**Qué comprobar:** Puedes reconocer qué cambió en tiempo y tono
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `ace-step-1.5`, `audiocraft`, `ultimate-vocal-remover`

## `rvc`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=audio,tts,python

**Qué es:** Interfaz y herramientas para convertir una grabación a otra voz mediante modelos locales.
**Stack:** Python 3.12 según guía; FFmpeg; modelo de conversión; voz autorizada; equipo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere API en la ruta propia; entrenamiento, hardware y modelos externos se costean aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. RVC convierte audio existente y no es por sí solo texto a voz; menos de diez minutos es un reclamo de entrenamiento y no una garantía universal
- Coste: Sin pago a un modelo en la ruta básica. No requiere API en la ruta propia; entrenamiento, hardware y modelos externos se costean aparte
- Equipo: Preparación según la ruta elegida. Python 3.12 según guía; FFmpeg; modelo de conversión; voz autorizada; equipo
**Repo:** https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI

**Instalación** [+]:

```
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un efecto de voz consentido; Estudiar conversión frente a TTS
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte un clip propio corto y compara claridad, tono y artefactos
**Qué comprobar:** Puedes reconocer entrada y voz objetivo del modelo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gpt-sovits`, `ffmpeg`, `obs-studio`

## `sherpa-onnx`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=speech,stt,tts,onnx

**Qué es:** Motor de voz offline con ONNX Runtime: reconocimiento, síntesis, VAD, diarización e identificación de hablante en móvil, embebido, escritorio y servidor.
**Stack:** C++, CMakeLists.txt, pom.xml, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/k2-fsa/sherpa-onnx

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/k2-fsa/sherpa-onnx/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: añadir dictado o transcripción sin conexión a una app Android o iOS; poner reconocimiento y síntesis de voz en una Raspberry Pi sin nube
**Evita si:** no quieres preparar modelos, dependencias y hardware propios
**Primera prueba propuesta:** Instala el paquete de Python, descarga un modelo de reconocimiento preentrenado de la documentación y transcribe un WAV de prueba.
**Qué comprobar:** Obtienes el texto reconocido sin conexión a internet.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `whisper`, `nemo`, `kokoro`, `pyannote-audio`

## `ten-framework`
role=library · exec=hybrid · setup=hard · mcp=False · prov=— · tags=voice,agents,realtime,framework

**Qué es:** Framework para agentes de voz conversacionales en tiempo real, con grafo de extensiones (ASR, LLM, TTS, VAD, turnos), diseñador visual y ejemplos listos.
**Stack:** Python, package.json
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/TEN-framework/ten-framework

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/TEN-framework/ten-framework/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: montar un asistente de voz que conversa en tiempo real con un LLM; construir un agente de voz con avatar o con transcripción en vivo
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Clona el repo, rellena `.env` con las claves de Agora, OpenAI, Deepgram y ElevenLabs y ejecuta `docker compose up -d`; abre el ejemplo de voz en el navegador.
**Qué comprobar:** Puedes hablar con un agente que responde por voz en tiempo real.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `dify`, `openclaw`, `vibevoice`, `whisper`, `elevenlabs-python`
**Alternativas (elige una):** `pipecat`, `livekit-agents`, `dograh`

## `ultimate-vocal-remover`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=audio,music,separation,app

**Qué es:** Aplicación de escritorio para separar voz e instrumentos de canciones con modelos de IA (MDX-Net, VR, Demucs), sin necesidad de programar.
**Stack:** Python, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/Anjok07/ultimatevocalremovergui

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: obtener la pista instrumental o la voz aislada de una canción propia; preparar stems para remezclar o practicar con una canción
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga el instalador para tu sistema desde las releases, abre una canción y separa con un modelo MDX-Net.
**Qué comprobar:** Obtienes dos archivos: voz e instrumental.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `rubberband`, `demucs`

## `vibevoice`
role=library · exec=local · setup=heavy · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio.
**Stack:** Modelo y guía específicos; Python y GPU según variante; audio autorizado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ejecución propia no exige API; pesos, hardware y datos tienen condiciones por variante
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es una familia que incluye ASR, streaming y TTS; el README raíz remite a guías separadas y no tiene un único instalador universal
- Coste: Sin pago a un modelo en la ruta básica. La ejecución propia no exige API; pesos, hardware y datos tienen condiciones por variante
- Equipo: Preparación según la ruta elegida. Modelo y guía específicos; Python y GPU según variante; audio autorizado
**Repo:** https://github.com/microsoft/VibeVoice

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/microsoft/VibeVoice/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar transcripción por hablantes; Probar generación de voz
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige ASR o TTS y prueba una muestra corta siguiendo esa guía
**Qué comprobar:** Puedes distinguir transcripción, generación y variante del modelo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`, `open-notebook`, `pipecat`, `ten-framework`

## `voxcpm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=tts,audio,python

**Qué es:** VoxCPM2: modelos y herramientas locales de TTS multilingüe,diseño y adaptación de voz.
**Stack:** Python >=3.10 y <3.13; PyTorch >=2.5; CUDA según ruta; pesos; audio autorizado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El README declara código y pesos Apache-2.0; hardware y datos propios siguen teniendo costes y permisos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta principal y on-device usan requisitos diferentes; velocidad y naturalidad son resultados que deben comprobarse con tu idioma y equipo
- Coste: Sin pago a un modelo en la ruta básica. El README declara código y pesos Apache-2.0; hardware y datos propios siguen teniendo costes y permisos
- Equipo: Preparación según la ruta elegida. Python >=3.10 y <3.13; PyTorch >=2.5; CUDA según ruta; pesos; audio autorizado
**Repo:** https://github.com/OpenBMB/VoxCPM

**Instalación** [+]:

```
pip install voxcpm
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar narración local; Explorar diseño de voz consentido
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sintetiza un texto corto y revisa pronunciación y estabilidad antes de ampliar
**Qué comprobar:** Puedes identificar modelo y parámetros de la prueba
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `pipecat`, `ffmpeg`

## `whisper`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=stt,audio,python

**Qué es:** Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo.
**Stack:** Python; PyTorch; FFmpeg; modelo con memoria suficiente; audio autorizado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Código y pesos MIT para ejecución propia sin API; cómputo independiente
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. No es la API hospedada de OpenAI y no usa créditos de ChatGPT; puede inventar texto en silencios o audio difícil y requiere revisión
- Coste: Sin pago a un modelo en la ruta básica. Código y pesos MIT para ejecución propia sin API; cómputo independiente
- Equipo: Preparación según la ruta elegida. Python; PyTorch; FFmpeg; modelo con memoria suficiente; audio autorizado
**Repo:** https://github.com/openai/whisper

**Instalación** [+]:

```
pip install -U openai-whisper
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una transcripción local; Traducir habla al inglés como borrador
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Transcribe una nota de voz breve y corrige manualmente las palabras dudosas
**Qué comprobar:** Puedes contrastar texto con audio original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `whisperx`, `pytorch`
**Alternativas (elige una):** `whisper-cpp`

## `whisper-cpp`
role=runtime · exec=local · setup=easy · mcp=False · prov=local · tags=stt,audio,local,cpp

**Qué es:** Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles.
**Stack:** Compilador y CMake según sistema; modelo Whisper; audio corto compatible
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Modelo local sin API de pago; hardware y energía independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Clonar es solo el comienzo: sigue compilación, descarga del modelo y formato de audio; no necesitas instalar todas las aceleraciones del README
- Coste: Sin pago a un modelo en la ruta básica. Modelo local sin API de pago; hardware y energía independientes
- Equipo: Preparación según la ruta elegida. Compilador y CMake según sistema; modelo Whisper; audio corto compatible
**Repo:** https://github.com/ggml-org/whisper.cpp

**Instalación** [+]:

```
git clone https://github.com/ggml-org/whisper.cpp.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Transcribir una nota offline; Preparar texto base para subtítulos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Transcribe una grabación propia corta y compara nombres y números con el audio
**Qué comprobar:** Puedes identificar modelo y errores de transcripción
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `llama-cpp`, `pipecat`, `dograh`, `kokoro`, `livekit-agents`
**Alternativas (elige una):** `faster-whisper`, `whisper`

## `whisperx`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=stt,audio,python

**Qué es:** Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes.
**Stack:** Python; modelo de transcripción y alineación; HF token y acuerdo para diarización; audio propio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige API de transcripción de pago; diarización requiere acceso autorizado al modelo de Hugging Face y cómputo propio
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Un token de descarga no equivale a facturación de API; etiquetas de hablante no identifican personas y los tiempos necesitan comprobación
- Coste: Sin pago a un modelo en la ruta básica. No exige API de transcripción de pago; diarización requiere acceso autorizado al modelo de Hugging Face y cómputo propio
- Equipo: Preparación según la ruta elegida. Python; modelo de transcripción y alineación; HF token y acuerdo para diarización; audio propio
**Repo:** https://github.com/m-bain/whisperX

**Instalación** [+]:

```
pip install whisperx
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar subtítulos por palabra; Separar intervenciones de una entrevista
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Transcribe una conversación de prueba y verifica varias marcas temporales y cambios de hablante
**Qué comprobar:** Puedes distinguir texto, alineación y etiquetas de hablante
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `faster-whisper`, `whisper`, `moviepy`, `pyannote-audio`
**Alternativas (elige una):** `nemo`

## `yue`
role=runtime · exec=local · setup=hard · mcp=False · prov=— · tags=music,generation,audio,model

**Qué es:** Modelo abierto de generación de canciones completas (voz y acompañamiento) a partir de letra y estilo, con partitura editable, covers y una skill para agentes.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/multimodal-art-projection/YuE

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/multimodal-art-projection/YuE/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: generar una maqueta de canción con letra propia para un proyecto personal o académico; editar la armonía de una canción generada manteniendo la melodía
**Evita si:** no tienes el hardware o no aceptas la licencia de los pesos
**Primera prueba propuesta:** En Linux con una GPU NVIDIA de 24 GB, clona el repo, ejecuta `python -m pip install .` y genera una canción con `YuE2Pipeline`.
**Qué comprobar:** Obtienes un audio estéreo y la partitura ABC editable.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `pytorch`, `audacity`
**Alternativas (elige una):** `ace-step-1.5`, `audiocraft`
