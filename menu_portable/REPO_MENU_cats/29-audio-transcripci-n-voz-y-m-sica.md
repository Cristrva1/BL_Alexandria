# 29. Audio, transcripción, voz y música — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ace-step-1.5`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=musica,text2music,python

**Qué es:** Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. Combina modelos de generación musical y una interfaz de inferencia para producir audio y personalizar estilos.
**Stack:** Python, Docker, pyproject.toml, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ace-step/ACE-Step-1.5

**Instalación** [?]: `Seguir la instalación original: https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas experimentar con generación musical en tu propio equipo
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa

## `audiocraft`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=audio,inference,training,python

**Qué es:** AudioCraft reúne el código de inferencia y entrenamiento de los modelos de audio generativo de Meta: MusicGen (música a partir de texto o melodía), AudioGen (efectos de sonido), MAGNeT, JASCO (música condicionada por acordes y batería), el códec neuronal EnCodec y AudioSeal para marcas de agua. Está orientada a investigación, aunque se usa mucho para crear música de fondo.
**Stack:** Python, PyTorch, EnCodec, Hugging Face Hub
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/facebookresearch/audiocraft

**Instalación** [?]: `Seguir la instalación original: https://github.com/facebookresearch/audiocraft/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas generar música o efectos de sonido por texto en local, o investigar modelos de audio
**Evita si:** necesitas uso comercial (los pesos son CC-BY-NC 4.0) o generar voz hablada; para voz mira `kokoro` o `chatterbox`
**Combina con:** `moviepy`, `remotion`, `ffmpeg`

## `chatterbox`
role=library · exec=local · setup=easy · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Clona una voz con unos segundos de audio y ajusta la expresividad. Multilingüe y con marca de agua.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/resemble-ai/chatterbox

**Instalación** [+]: `pip install chatterbox-tts`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres clonar voces con calidad alta y licencia libre
**Evita si:** necesitas algo muy ligero en CPU; mira `kokoro`
**Combina con:** `pipecat`
**Alternativas (elige una):** `fish-speech`, `gpt-sovits`, `kokoro`, `luxtts`

## `cosyvoice`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Síntesis de voz natural con clonación y control de estilo, también en streaming.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/QwenAudio/CosyVoice

**Instalación** [?]: `Seguir la instalación original: https://github.com/QwenAudio/CosyVoice/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas TTS multilingüe en streaming
**Evita si:** quieres instalación muy simple; mira `kokoro`
**Combina con:** `pipecat`
**Alternativas (elige una):** `fish-speech`, `index-tts`

## `dograh`
role=app · exec=hybrid · setup=medium · mcp=True · prov=— · tags=voz-agentes,agent,python

**Qué es:** Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables.
**Stack:** Python
**Acceso y costes:**
- API de IA: API de IA opcional. El inicio documentado incluye claves generadas y una pila gestionada; también permite conectar proveedores propios. No se deduce de ello que sus modelos sean locales.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. Revisar el acceso a la pila de Dograh y los proveedores de voz, modelos y telefonía; sus tarifas no se cubren automáticamente con el plan del agente.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/dograh-hq/dograh

**Instalación** [?]: `Seguir la instalación original: https://github.com/dograh-hq/dograh/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `earshot`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=local · tags=edicion,mcp,python

**Qué es:** Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. La herramienta opcional llm_critique utiliza GEMINI_API_KEY; las herramientas locales de audio no implican ese consumo.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. El análisis de audio se ejecuta con modelos locales en CPU. La crítica con LLM es una función opcional separada.
- Coste: El coste depende del proveedor o la ruta. Los modelos de audio locales consumen CPU, memoria y disco. La crítica opcional mediante Gemini tiene el acceso y las cuotas de ese proveedor.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Leonxlnx/earshot

**Instalación** [?]: `Seguir la instalación original: https://github.com/Leonxlnx/earshot/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `edge-tts`
role=library · exec=cloud · setup=easy · mcp=False · prov=— · tags=tts,speech-synthesis,text-to-speech,python

**Qué es:** Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. Envía texto al servicio de voz y guarda el audio y los subtítulos desde Python o la terminal.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta documentada usa un servicio en línea mediante sesión o acceso propio; no implica ejecución local del modelo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Usa un servicio de voz de Microsoft en línea. No pide una API key en su uso documentado, pero no funciona sin conexión ni garantiza disponibilidad futura.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/rany2/edge-tts

**Instalación** [+]: `pip install edge-tts`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres generar narración sin instalar un modelo de voz local
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa
**Combina con:** `moviepy`
**Alternativas (elige una):** `kokoro`

## `faster-whisper`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=stt,audio,python

**Qué es:** Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. Puede reducir requisitos frente a otras implementaciones; mide calidad y rendimiento con tu propio audio.
**Stack:** Python, CTranslate2
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/SYSTRAN/faster-whisper

**Instalación** [+]: `pip install faster-whisper`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** el rendimiento, la memoria o el coste de GPU importan
**Evita si:** necesitas alineación/diarización (whisperX) o te basta el CLI oficial
**Combina con:** `whisperx`
**Alternativas (elige una):** `whisper-cpp`

## `fish-speech`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Clona voces con pocos segundos de audio y genera habla natural en muchos idiomas.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/fishaudio/fish-speech

**Instalación** [?]: `Seguir la instalación original: https://github.com/fishaudio/fish-speech/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas TTS de alta calidad con clonación
**Evita si:** necesitas licencia comercial sin restricciones; mira `chatterbox`
**Alternativas (elige una):** `chatterbox`, `cosyvoice`, `gpt-sovits`

## `gpt-sovits`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Entrena una voz con muy pocos datos y sintetiza en varios idiomas. Muy popular entre creadores.
**Stack:** Python, PyTorch, Gradio
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/RVC-Boss/GPT-SoVITS

**Instalación** [?]: `Seguir la instalación original: https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres entrenar una voz con pocos datos
**Evita si:** prefieres zero-shot sin entrenar; mira `chatterbox`
**Combina con:** `rvc`
**Alternativas (elige una):** `chatterbox`, `fish-speech`

## `index-tts`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Clona voces sin entrenar y permite controlar la duración exacta, útil para doblaje.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/index-tts/index-tts

**Instalación** [?]: `Seguir la instalación original: https://github.com/index-tts/index-tts/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas controlar duración y emoción de la voz
**Evita si:** buscas licencia totalmente libre; revisa su licencia
**Alternativas (elige una):** `cosyvoice`

## `kokoro`
role=library · exec=local · setup=easy · mcp=False · prov=local · tags=tts,audio,local

**Qué es:** Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. Comprueba los idiomas, dependencias de audio y condiciones de la variante que utilices.
**Stack:** Python, PyTorch, JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/hexgrad/kokoro

**Instalación** [+]: `pip install kokoro`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres TTS ligero, rápido y con licencia permisiva
**Evita si:** necesitas clonar voces; mira `chatterbox`
**Combina con:** `pipecat`, `whisper-cpp`
**Alternativas (elige una):** `chatterbox`, `tts`, `luxtts`, `edge-tts`

## `livekit-agents`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google · tags=audio,agents,video,python

**Qué es:** Construye agentes que hablan, escuchan y ven, con detección de turnos y telefonía, desplegables a escala.
**Stack:** Python, Node.js, WebRTC
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/livekit/agents

**Instalación** [?]: `Seguir la instalación original: https://github.com/livekit/agents/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas agentes de voz escalables con WebRTC
**Evita si:** quieres algo ligero sin servidor de medios; mira `pipecat`
**Combina con:** `kokoro`
**Alternativas (elige una):** `pipecat`

## `luxtts`
role=library · exec=local · setup=easy · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. La velocidad y el consumo de memoria dependen de la variante y del hardware.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ysharma3501/LuxTTS

**Instalación** [?]: `Seguir la instalación original: https://github.com/ysharma3501/LuxTTS/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas TTS con clonación muy rápido
**Evita si:** buscas el proyecto más maduro; mira `chatterbox`
**Combina con:** `litellm`, `cosmos`, `comfyui`
**Alternativas (elige una):** `kokoro`, `chatterbox`

## `melotts`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=tts,model,python

**Qué es:** Biblioteca de texto a voz con modelos y ejemplos para sintetizar narración en varios idiomas compatibles.
**Stack:** Python, Dockerfile
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/myshell-ai/MeloTTS

**Instalación** [?]: `Seguir la instalación original: https://github.com/myshell-ai/MeloTTS/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Biblioteca de texto a voz con modelos y ejemplos para sintetizar narración en varios idiomas compatibles.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `music-megathread`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=musica

**Qué es:** Directorio de reproductores, herramientas, servicios y otros recursos relacionados con música. Agrupa enlaces a proyectos y servicios musicales para explorar alternativas por función.
**Stack:** Recursos y documentación
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/MoonWalker440/Music-Megathread

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas recursos musicales y quieres comparar opciones desde una lista
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa

## `nemo`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=stt,tts,audio,python

**Qué es:** Incluye modelos de ASR como Parakeet y Canary, que lideran rankings de transcripción, y herramientas para afinarlos.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA-NeMo/Speech

**Instalación** [?]: `Seguir la instalación original: https://github.com/NVIDIA-NeMo/Speech/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas ASR de máxima precisión y tienes GPU
**Evita si:** quieres algo simple; mira `faster-whisper`
**Combina con:** `pipecat`
**Alternativas (elige una):** `whisperx`

## `omnivoice-studio`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=tts,audio,python

**Qué es:** Reúne STT, TTS y dubbing en una sola app sin claves de API.
**Stack:** desktop/Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/debpalash/VoiceStudio

**Instalación** [?]: `Seguir la instalación original: https://github.com/debpalash/VoiceStudio/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres suite de voz completa local (dictado + clonación + dubbing)
**Evita si:** solo necesitas TTS simple por CLI/librería (TTS) o estabilidad de producción
**Combina con:** `whisperx`
**Alternativas (elige una):** `videolingo`

## `pipecat`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google · tags=audio,agents,stt,tts,python

**Qué es:** Encadena STT, LLM y TTS con interrupciones y baja latencia, y conecta con teléfono, WebRTC o WhatsApp.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/pipecat-ai/pipecat

**Instalación** [+]: `pip install pipecat-ai`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** construyes un agente de voz en Python
**Evita si:** quieres infraestructura WebRTC gestionada; mira `livekit-agents`
**Combina con:** `kokoro`, `whisper-cpp`
**Alternativas (elige una):** `livekit-agents`

## `rnnoise`
role=runtime · exec=local · setup=medium · mcp=False · prov=local · tags=edicion,model,c

**Qué es:** Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/xiph/rnnoise

**Instalación** [?]: `Seguir la instalación original: https://github.com/xiph/rnnoise/blob/main/README`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `rubberband`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=edicion,library,c

**Qué es:** Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas.
**Stack:** C++
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/breakfastquay/rubberband

**Instalación** [?]: `Seguir la instalación original: https://github.com/breakfastquay/rubberband/blob/default/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `rvc`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=audio,tts,python

**Qué es:** Cambia la voz de una grabación manteniendo entonación. Muy usado para covers y doblaje.
**Stack:** Python, PyTorch, Gradio
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI

**Instalación** [?]: `Seguir la instalación original: https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres convertir una voz grabada en otra
**Evita si:** necesitas generar voz desde texto; mira `chatterbox`
**Combina con:** `gpt-sovits`

## `supertonic`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=tts,audio

**Qué es:** Motor de texto a voz que ofrece modelos y ejemplos para sintetizar audio en dispositivos y navegadores compatibles. El soporte por idioma, dispositivo y variante debe comprobarse en la documentación actual.
**Stack:** Python, Rust (ONNX), Node.js, WebGPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/supertone-oss-archive/supertonic

**Instalación** [+]: `pip install supertonic`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres voz local en tiempo real y sin nube
**Evita si:** priorizas clonación de máxima fidelidad (VoxCPM) o flexibilidad multi-modelo (TTS)
**Combina con:** `whisperx`, `moviepy`

## `tts`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=tts,audio,python

**Qué es:** Reúne en una sola librería modelos como Tacotron, VITS y XTTS, con CLI y API Python.
**Stack:** Python, PyTorch, modelos descargables
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/coqui-ai/TTS

**Instalación** [+]: `pip install TTS`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres flexibilidad y varios modelos en una librería
**Evita si:** necesitas tiempo real puro (supertonic) o soporte comercial (Coqui está inactivo)
**Combina con:** `whisperx`, `moviepy`
**Alternativas (elige una):** `kokoro`

## `vibevoice`
role=library · exec=local · setup=heavy · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio. Elige una variante concreta antes de asumir idiomas, duración, hardware o soporte de tiempo real.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/microsoft/VibeVoice

**Instalación** [?]: `Seguir la instalación original: https://github.com/microsoft/VibeVoice/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres generar podcasts o diálogos largos
**Evita si:** solo necesitas frases cortas; mira `kokoro`
**Combina con:** `open-notebook`

## `voxcpm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=tts,audio,python

**Qué es:** Pertenece a la familia CPM de modelos generativos de OpenBMB.
**Stack:** Python, PyTorch, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/OpenBMB/VoxCPM

**Instalación** [+]: `pip install voxcpm`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres voz muy natural o clonada y tienes GPU
**Evita si:** priorizas latencia mínima (supertonic) o no tienes GPU
**Combina con:** `tts`

## `whisper`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=stt,audio,python

**Qué es:** Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. El idioma, el tamaño del modelo y la calidad del audio condicionan el resultado.
**Stack:** Python 3.9+, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/openai/whisper

**Instalación** [+]: `pip install -U openai-whisper`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres la referencia robusta y no te obsesiona la latencia
**Evita si:** necesitas más velocidad (faster-whisper) o timings por palabra (whisperX)
**Combina con:** `whisperx`
**Alternativas (elige una):** `whisper-cpp`

## `whisper-cpp`
role=runtime · exec=local · setup=easy · mcp=False · prov=local · tags=stt,audio,local,cpp

**Qué es:** Transcribe voz a texto en local sin Python ni GPU obligatoria, incluso en tiempo real. Base de muchas apps de dictado.
**Stack:** C++, C
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ggml-org/whisper.cpp

**Instalación** [?]: `Seguir la instalación original: https://github.com/ggml-org/whisper.cpp/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres transcribir en local sin GPU
**Evita si:** necesitas marcas de tiempo por palabra y diarización; mira `whisperx`
**Combina con:** `ffmpeg`
**Alternativas (elige una):** `faster-whisper`, `whisper`

## `whisperx`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=stt,audio,python

**Qué es:** Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. Las etapas, modelos y credenciales requeridos cambian según las funciones que actives.
**Stack:** Python, faster-whisper, wav2vec2, pyannote
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/m-bain/whisperX

**Instalación** [+]: `pip install whisperx`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas subtítulos precisos o diarización
**Evita si:** te basta texto plano (whisper) o no quieres gestionar tokens de HF
**Combina con:** `whisper`, `moviepy`
**Alternativas (elige una):** `nemo`
