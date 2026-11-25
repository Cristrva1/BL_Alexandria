# Alexandría para agentes · Motores para correr modelos en local

Categoría 8 «Chats, modelos locales y espacios privados» › subcategoría `motores`. 14 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=8&sub=motores · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `ollama` | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible… | 1 Básico | 84 | MIT (OSI permisiva) | recomendado |
| `llama-cpp` | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi… | 2 Intermedio | 78 | MIT (OSI permisiva) | alternativa |
| `localai` | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y… | 2 Intermedio | 72 | MIT (OSI permisiva) | alternativa |
| `exo` | Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u… | 2 Intermedio | 69 | Apache-2.0 (OSI permisiva) | sin grupo |
| `llmfit` | Inspector de hardware que estima qué modelos de lenguaje y cuantizaciones caben… | 1 Básico | 64 | MIT (OSI permisiva) | sin grupo |
| `magnitude` | Motor de inferencia local que adapta su ejecución al hardware y ofrece… | 3 Avanzado | 62 | Apache-2.0 (OSI permisiva) | sin grupo |
| `mlx-lm` | Paquete de Apple para generar texto y afinar LLM en Apple Silicon con MLX… | 3 Avanzado | 59 | MIT (OSI permisiva) | sin grupo |
| `transformers.js` | Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y… | 2 Intermedio | 59 | Apache-2.0 (OSI permisiva) | sin grupo |
| `freetoken` | Herramientas para servir modelos de IA en hardware local mediante las rutas de… | 3 Avanzado | 58 | Apache-2.0 (OSI permisiva) | sin grupo |
| `mlc-llm` | Motor universal de despliegue de LLM con compilación de ML: ejecuta modelos en… | 3 Avanzado | 56 | Apache-2.0 (OSI permisiva) | sin grupo |
| `llamafile` | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier… | 1 Básico | 52 | Apache-2.0 (OSI permisiva) | alternativa |
| `airllm` | Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante… | 3 Avanzado | 51 | Apache-2.0 (OSI permisiva) | sin grupo |
| `koboldcpp` | Ejecutable único basado en llama.cpp para correr modelos GGUF en local con… | 3 Avanzado | 46 | AGPL-3.0 (OSI copyleft) | alternativa |
| `inferssd` | Ejecuta modelos locales de tipo MoE leyendo partes de sus pesos desde un SSD… | 3 Avanzado | — | Apache-2.0 | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Ollama (`ollama`)

- **Repo:** https://github.com/ollama/ollama · MIT · nivel 1 · 84/100 · recomendado en «Motores para correr LLM en local»
- **Qué es:** Ollama, motor para descargar y ejecutar modelos de lenguaje abiertos en tu equipo (macOS, Windows, Linux o Docker), de Ollama Inc. Licencia MIT. Es muy madura y popular (~187k estrellas, v0.40.x).
- **Cuándo elegirlo:** Casos: Probar un LLM local; Conectar un modelo local a Codex CLI.
- **Requisitos:** nivel 1: preparación sencilla; Instalador oficial para tu sistema; RAM y disco adecuados al modelo; hardware prerequisites; API de IA: opcional; Instalador oficial para tu sistema; RAM y disco adecuados al modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install ollama` — fuente: https://github.com/ollama/ollama/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga un modelo pequeño y formula una pregunta antes de conectarlo a un agente Éxito: Puedes identificar el modelo ejecutado y ver la respuesta en tu equipo
- **Combina con:** `open-webui` [8/chats], `litellm` [23/serving], `crawl4ai` [4/crawlers], `claude-code` [20/terminal]
- **Alternativas:** `llama-cpp`, `localai`, `llamafile`, `koboldcpp`
- **Riesgos y avisos:** Alternativas (elige una): llama-cpp, localai, llamafile. Varios motores en la misma máquina compiten por GPU y memoria. Las guías del autor documentan Claude Code y Codex CLI con backend Ollama; esto cambia el modelo y no aporta modelos Anthropic/OpenAI mediante su suscripción.

### llama.cpp (`llama-cpp`)

- **Repo:** https://github.com/ggml-org/llama.cpp · MIT · nivel 2 · 78/100 · alternativa en «Motores para correr LLM en local»
- **Qué es:** Motor de inferencia de LLM y modelos de visión (VLM) en C/C++, mantenido por la organización ggml-org sobre la biblioteca de tensores ggml. Licencia MIT, desarrollo diario desde 2023 y primera versión 1.0.0 publicada en noviembre de 2026…
- **Cuándo elegirlo:** Casos: Servir un modelo en CPU; Comparar cuantizaciones de un mismo modelo.
- **Requisitos:** nivel 2: preparación media; Binario o compilación para tu sistema; modelo GGUF; memoria suficiente; hardware prerequisites; API de IA: no; Binario o compilación para tu sistema; modelo GGUF; memoria suficiente.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -LsSf https://llama.app/install.sh | sh` — fuente: https://github.com/ggml-org/llama.cpp/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta un GGUF pequeño y observa memoria y velocidad de respuesta Éxito: Puedes generar texto y reconocer qué backend y modelo se utilizan
- **Combina con:** `open-webui` [8/chats], `llmfit`, `librechat` [8/chats], `litellm` [23/serving]
- **Alternativas:** `ollama`, `localai`, `llamafile`, `koboldcpp`
- **Riesgos y avisos:** Alternativas (elige una como motor principal): ollama, llamafile, localai. No todos los modelos o backends ofrecen las mismas funciones de herramientas y visión.

### LocalAI (`localai`)

- **Repo:** https://github.com/mudler/LocalAI · MIT · nivel 2 · 72/100 · alternativa en «Motores para correr LLM en local»
- **Qué es:** Motor de IA de código abierto (MIT) creado por Ettore Di Giacinto y mantenido por el equipo de LocalAI, que se presenta como «tu propia IA en tu propio hardware».
- **Cuándo elegirlo:** Casos: Ofrecer una API local a una aplicación; Probar texto o voz con distintos backends.
- **Requisitos:** nivel 2: preparación media; Docker; modelo y backend apropiados al equipo; hardware prerequisites; API de IA: no; Docker; modelo y backend apropiados al equipo.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -ti --name local-ai -p 8080:8080 localai/localai:latest` — fuente: https://github.com/mudler/LocalAI/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca el servidor, instala un modelo pequeño y prueba una petición de texto Éxito: El endpoint responde con el modelo elegido
- **Combina con:** `anything-llm` [8/workspaces], `open-webui` [8/chats], `librechat` [8/chats], `chatbox` [8/chats], `nextchat` [8/chats]
- **Alternativas:** `ollama`, `llama-cpp`, `llamafile`, `koboldcpp`
- **Riesgos y avisos:** Alternativas (elige una como motor principal): ollama, llama-cpp. No necesitar GPU no garantiza buen rendimiento en cualquier modelo; compatibilidad de API no confirma integración completa con cada agente.

### exo (`exo`)

- **Repo:** https://github.com/exo-explore/exo · Apache-2.0 · nivel 2 · 69/100
- **Qué es:** Software de código abierto (Apache 2.0) de exo labs para ejecutar modelos de frontera en local uniendo varios dispositivos en un clúster de IA. Activo, con app de macOS y versiones frecuentes (v1.0.71 como última release publicada).
- **Cuándo elegirlo:** Casos: Compartir memoria entre equipos compatibles; Experimentar con inferencia distribuida local.
- **Requisitos:** nivel 2: preparación media; Para app: Apple Silicon y macOS 15.1+; equipos en la misma red y versión; modelo; hardware prerequisites; API de IA: no; Para app: Apple Silicon y macOS 15.1+; equipos en la misma red y versión; modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install --cask exo` — fuente: https://github.com/exo-explore/exo/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Empieza en un Mac y añade un segundo equipo compatible antes de repartir un modelo Éxito: El panel muestra los dispositivos y la distribución de trabajo
- **Combina con:** `open-webui` [8/chats], `librechat` [8/chats], `litellm` [23/serving], `mlx-lm`
- **Riesgos y avisos:** Todos los nodos deben ejecutar la misma versión de exo. El rendimiento en Linux (solo CPU) no es comparable con el de Apple Silicon. La app macOS y la ejecución desde fuentes tienen requisitos distintos; Windows no está confirmado en la ruta revisada.

### llmfit (`llmfit`)

- **Repo:** https://github.com/AlexsJones/llmfit · MIT · nivel 1 · 64/100
- **Qué es:** Herramienta de terminal de código abierto (MIT) escrita en Rust por Alex Jones que calcula qué LLM puede ejecutar tu hardware. Proyecto de 2026 muy activo (v1.1.20).
- **Cuándo elegirlo:** Casos: Elegir un modelo antes de descargarlo; Comparar requisitos de dos cuantizaciones.
- **Requisitos:** nivel 1: preparación sencilla; Binario para tu sistema; acceso a datos de hardware; hardware prerequisites; API de IA: no; Binario para tu sistema; acceso a datos de hardware.
- **Instalación (documentada en la fuente; no ejecutada):** `winget install --exact --id AlexsJones.llmfit` — fuente: https://github.com/AlexsJones/llmfit/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta el inspector y compara RAM y VRAM detectadas con tu equipo Éxito: Las recomendaciones explican qué modelos y cuantizaciones podrían caber
- **Combina con:** `ollama`, `llama-cpp`, `vllm` [23/serving], `airllm`, `jan` [8/chats], `textgen` [8/chats]
- **Riesgos y avisos:** Las estimaciones de velocidad son proyecciones; contrástalas con la función de benchmark. Estima ajuste al hardware y velocidad; no mide por sí mismo la calidad del modelo en tu tarea.

### magnitude (`magnitude`)

- **Repo:** https://github.com/magnitudedev/magnitude · Apache-2.0 · nivel 3 · 62/100
- **Qué es:** Motor de inferencia de código abierto (Apache 2.0) de magnitudedev que ajusta sus núcleos a tu hardware para ejecutar cada modelo lo más rápido posible. Reciente y muy activo (CLI 0.2.17), con app de escritorio y CLI.
- **Cuándo elegirlo:** Casos: Servir un modelo local a Codex; Comparar backends de inferencia en tu equipo.
- **Requisitos:** nivel 3: preparación pesada; Sistema y acelerador compatibles; pesos; espacio de caché para optimización; hardware prerequisites; API de IA: no; Sistema y acelerador compatibles; pesos; espacio de caché para optimización.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://magnitude.dev/install.sh | sh` — fuente: https://github.com/magnitudedev/magnitude/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Prueba un modelo pequeño y registra la latencia antes y después del ajuste de kernels Éxito: Puedes comparar rendimiento en la misma máquina y con el mismo modelo
- **Combina con:** `hermes-agent` [21/asistentes], `codex` [20/terminal], `opencode` [20/terminal]
- **Riesgos y avisos:** En modo servidor remoto protege el acceso: en local no valida claves. El README documenta conexión a Claude Code y Codex; su cifra de velocidad es un benchmark del autor, no una garantía universal.

### MLX LM (`mlx-lm`)

- **Repo:** https://github.com/ml-explore/mlx-lm · MIT · nivel 3 · 59/100
- **Qué es:** Paquete de código abierto (MIT) del equipo ml-explore de Apple, construido sobre el framework MLX. Activo; requiere un Mac con Apple Silicon.
- **Cuándo elegirlo:** Casos: ejecutar un LLM local optimizado en un Mac con chip Apple; afinar un modelo con LoRA en un Mac sin GPU NVIDIA. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 3: preparación sencilla, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install mlx-lm` — fuente: https://github.com/ml-explore/mlx-lm/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install mlx-lm` en un Mac con Apple Silicon y genera texto con un modelo cuantizado del Hub. Éxito: El modelo se descarga, genera la respuesta y la CLI informa de tokens por segundo.
- **Combina con:** `exo`, `open-webui` [8/chats], `litellm` [23/serving]
- **Riesgos y avisos:** Solo funciona en Apple Silicon; el rendimiento depende de la memoria unificada disponible.

### transformers.js (`transformers.js`)

- **Repo:** https://github.com/huggingface/transformers.js · Apache-2.0 · nivel 2 · 59/100
- **Qué es:** Biblioteca JavaScript oficial de Hugging Face para ejecutar modelos Transformers directamente en el navegador, sin servidor. Apache 2.0, madura y activa (v4.3.2); funcionalmente equivalente a la biblioteca `transformers` de Python.
- **Cuándo elegirlo:** Casos: Clasificar texto en el navegador; Procesar audio o imágenes sin servidor de modelos externo.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node o navegador compatible; modelo ONNX admitido; RAM y descarga inicial; hardware prerequisites; API de IA: no; Node o navegador compatible; modelo ONNX admitido; RAM y descarga inicial.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i @huggingface/transformers` — fuente: https://github.com/huggingface/transformers.js/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta un pipeline de clasificación de texto sobre dos frases de prueba Éxito: El modelo devuelve etiquetas que puedes comparar con las frases
- **Combina con:** `qdrant` [6/vectores], `supabase` [22/infraestructura], `whisper` [29/stt]
- **Riesgos y avisos:** Se retiró la combinación antigua con swr por no tener relación con la inferencia. No todos los Transformers se ejecutan sin conversión; confirma compatibilidad y backend WebGPU o WASM del modelo elegido.

### FreeToken (`freetoken`)

- **Repo:** https://github.com/FlashML-org/FreeToken · Apache-2.0 · nivel 3 · 58/100
- **Qué es:** Motor de servicio de modelos Mixture-of-Experts (MoE) para hardware de consumo, de FlashML, con artículo académico asociado. Apache 2.0, reciente y activo (v0.2.2).
- **Cuándo elegirlo:** Casos: Experimentar con inferencia de modelos MoE; Evaluar un backend de aceleración local.
- **Requisitos:** nivel 3: preparación pesada; Python y uv; acelerador compatible; pesos y espacio según modelo; hardware prerequisites; API de IA: no; Python y uv; acelerador compatible; pesos y espacio según modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `uv pip install "freetoken[accel]"` — fuente: https://github.com/FlashML-org/FreeToken/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el quickstart con el modelo más pequeño compatible y mide memoria y latencia Éxito: Puedes generar una salida y registrar el consumo real de tu equipo
- **Combina con:** `open-webui` [8/chats], `litellm` [23/serving], `codex` [20/terminal]
- **Riesgos y avisos:** Las afirmaciones sobre modelos enormes y velocidad pertenecen al autor y no demuestran que funcionen en cualquier PC.

### MLC LLM (`mlc-llm`)

- **Repo:** https://github.com/mlc-ai/mlc-llm · Apache-2.0 · nivel 3 · 56/100
- **Qué es:** Compilador de ML y motor de despliegue de código abierto (Apache-2.0) del proyecto MLC (CMU, OctoAI y comunidad), basado en Apache TVM. Activo; hermano de WebLLM para el navegador.
- **Cuándo elegirlo:** Casos: ejecutar un LLM en un móvil o en el navegador sin servidor; servir un modelo en GPU AMD, Intel o Apple con una API compatible con OpenAI. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python, CMakeLists.txt, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --recursive https://github.com/mlc-ai/mlc-llm.git && cd mlc-llm/` — fuente: https://llm.mlc.ai/docs/install/mlc_llm
- **Primera prueba propuesta (no ejecutada):** Sigue el quick start para instalar el paquete de tu plataforma y chatear con un modelo precompilado. Éxito: El modelo responde en local y el servidor REST devuelve respuestas al endpoint de chat.
- **Combina con:** `transformers` [24/entrenamiento], `open-webui` [8/chats], `litellm` [23/serving]
- **Riesgos y avisos:** La compilación requiere preparar el entorno de la GPU objetivo; usa modelos precompilados para la primera prueba.

### llamafile (`llamafile`)

- **Repo:** https://github.com/mozilla-ai/llamafile · Apache-2.0 · nivel 1 · 52/100 · alternativa en «Motores para correr LLM en local»
- **Qué es:** Proyecto de Mozilla Builders, renovado por Mozilla.ai, para distribuir y ejecutar LLM como un solo archivo ejecutable. El proyecto es Apache 2.0 y sus cambios a llama.cpp y whisper.cpp son MIT; desde la versión 0.10 usa un nuevo sistema de…
- **Cuándo elegirlo:** Casos: Distribuir una demo local de un LLM; Probar inferencia sin montar un servidor complejo.
- **Requisitos:** nivel 1: preparación sencilla; Ejecutable oficial del modelo; RAM y disco; instrucciones de tu sistema; hardware prerequisites; API de IA: no; Ejecutable oficial del modelo; RAM y disco; instrucciones de tu sistema.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/mozilla-ai/llamafile.git` — fuente: https://github.com/mozilla-ai/llamafile/blob/main/docs/whisperfile/getting-started.md
- **Primera prueba propuesta (no ejecutada):** Descarga el ejemplo pequeño y pregunta algo desde su interfaz local Éxito: El ejecutable carga el modelo y devuelve texto
- **Combina con:** `open-webui` [8/chats], `anything-llm` [8/workspaces], `librechat` [8/chats]
- **Alternativas:** `ollama`, `llama-cpp`, `localai`, `koboldcpp`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una como motor principal): ollama, llama-cpp. El README separa permisos de ejecución Unix y pasos por sistema; no asumas que cualquier archivo grande funciona igual en Windows.

### airllm (`airllm`)

- **Repo:** https://github.com/lyogavin/airllm · Apache-2.0 · nivel 3 · 51/100
- **Qué es:** Biblioteca Python de código abierto (Apache 2.0) de lyogavin para reducir la memoria de inferencia de LLM grandes. Existe desde 2023 y publicó la v4.0.0 en 2026; el README incluye enlaces patrocinados ajenos al proyecto.
- **Cuándo elegirlo:** Casos: Estudiar inferencia por carga de capas; Probar un modelo que supera la VRAM disponible.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python; GPU o backend compatible; disco y memoria para capas y pesos; hardware prerequisites; API de IA: no; Python; GPU o backend compatible; disco y memoria para capas y pesos.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install airllm` — fuente: https://github.com/lyogavin/airllm/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Carga un modelo de prueba admitido y mide el tiempo de generación además de la VRAM Éxito: Obtienes texto y una medida real de latencia y almacenamiento
- **Combina con:** `llmfit`, `transformers` [24/entrenamiento], `peft` [24/entrenamiento]
- **Riesgos y avisos:** Que quepa en poca VRAM no significa que un modelo grande sea interactivo en tu equipo.

### KoboldCpp (`koboldcpp`)

- **Repo:** https://github.com/LostRuins/koboldcpp · AGPL-3.0 · nivel 3 · 46/100 · alternativa en «Motores para correr LLM en local»
- **Qué es:** Software de código abierto (AGPL-3.0) de LostRuins (Concedo), inspirado en KoboldAI y construido sobre llama.cpp. Fork establecido y muy activo, con versiones frecuentes.
- **Cuándo elegirlo:** Casos: chatear o escribir historias con un modelo local sin instalar dependencias; dar a otras apps una API local compatible con OpenAI u Ollama. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 3: preparación sencilla, necesita GPU; C++, CMakeLists.txt, requirements.txt; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/LostRuins/koboldcpp.git` — fuente: https://github.com/LostRuins/koboldcpp/blob/concedo/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el ejecutable de la release para tu sistema, elige un modelo GGUF pequeño y arráncalo. Éxito: La interfaz web local responde y el endpoint compatible con OpenAI devuelve texto.
- **Combina con:** `sillytavern` [8/chats], `open-webui` [8/chats], `kokoro` [29/tts]
- **Alternativas:** `ollama`, `llama-cpp`, `localai`, `llamafile`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): llamafile. Ajusta capas de GPU y contexto si te quedas sin memoria.

### InferSSD (`inferssd`)

- **Repo:** https://github.com/wici-ai/inferssd · Apache-2.0 · nivel 3 · —/100
- **Qué es:** Ejecuta modelos locales de tipo MoE leyendo partes de sus pesos desde un SSD cuando no caben completos en memoria o VRAM.
- **Cuándo elegirlo:** Casos: Medir si un modelo compatible arranca con la memoria disponible.; Comparar tiempos de respuesta con dos tamaños de contexto. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 3: preparación pesada; C++, CMakeLists.txt; hardware model_dependent; API de IA: no; SSD y un modelo MoE compatible; backend de sistema y GPU según las guías de la variante..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/wici-ai/inferssd/blob/910afae91c3c2578f890df7ffd9a1e55b6237680/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona un modelo de prueba compatible y registra carga, latencia y memoria con una pregunta corta. Éxito: Obtienes una respuesta y medidas de rendimiento que puedes cotejar con tu equipo.
- **Riesgos y avisos:** No acelera cualquier modelo. La velocidad del SSD y la variante influyen; las licencias de los pesos se revisan por separado.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-8-motores.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Motores para correr modelos en local», lee `docs/alexandria/categoria-8-motores.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-8-motores.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
