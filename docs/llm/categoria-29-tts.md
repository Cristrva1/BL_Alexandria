# Alexandría para agentes · Síntesis y clonación de voz

Categoría 29 «Audio, transcripción, voz y música» › subcategoría `tts`. 13 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=29&sub=tts · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `omnivoice-studio` | App local de voz con modelos descargables,edición AGPL y una oferta comercial… | 2 Intermedio | 76 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `gpt-sovits` | Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y… | 2 Intermedio | 69 | MIT (OSI permisiva) | recomendado |
| `voxcpm` | VoxCPM2: modelos y herramientas locales de TTS multilingüe,diseño y adaptación… | 3 Avanzado | 68 | Apache-2.0 (OSI permisiva) | sin grupo |
| `elevenlabs-python` | SDK oficial de Python para la API de pago de ElevenLabs: voz sintética… | 2 Intermedio | 66 | MIT (OSI permisiva) | sin grupo |
| `f5-tts` | Síntesis de voz con clonación a partir de pocos segundos de audio de… | 3 Avanzado | 64 | MIT (OSI permisiva) | alternativa |
| `cosyvoice` | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y… | 2 Intermedio | 61 | Apache-2.0 (OSI permisiva) | alternativa |
| `fish-speech` | Herramientas y modelos de voz Fish Audio con licencias Community o Research… | 3 Avanzado | 61 | Fish Audio Community License 1.0 (no OSI) (source-available) | alternativa |
| `vibevoice` | Familia de modelos de voz de Microsoft con herramientas para generación y… | 3 Avanzado | 61 | MIT (OSI permisiva) | sin grupo |
| `edge-tts` | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado… | 2 Intermedio | 60 | LGPL-3.0 (un archivo MIT) (OSI copyleft) | recomendado |
| `rvc` | Interfaz y herramientas para convertir una grabación a otra voz mediante… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `index-tts` | Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. | 2 Intermedio | 53 | bilibili Model Use License (source-available) | alternativa |
| `luxtts` | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una… | 2 Intermedio | 52 | Apache-2.0 (OSI permisiva) | alternativa |
| `kokoro` | Modelo y biblioteca de texto a voz para generar narración localmente con… | 2 Intermedio | 48 | Apache-2.0 (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-29-tts.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Síntesis y clonación de voz», lee `docs/alexandria/categoria-29-tts.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-29-tts.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
