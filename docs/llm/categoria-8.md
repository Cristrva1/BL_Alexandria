# Alexandría para agentes · Chats, modelos locales y espacios privados

Categoría 8 completa (33 repos, 4 subcategorías). Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=8 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `ollama` | motores | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible… | 1 Básico | 84 | MIT (OSI permisiva) | recomendado |
| `llama-cpp` | motores | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi… | 2 Intermedio | 78 | MIT (OSI permisiva) | alternativa |
| `localai` | motores | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y… | 2 Intermedio | 72 | MIT (OSI permisiva) | alternativa |
| `exo` | motores | Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u… | 2 Intermedio | 69 | Apache-2.0 (OSI permisiva) | sin grupo |
| `llmfit` | motores | Inspector de hardware que estima qué modelos de lenguaje y cuantizaciones caben… | 1 Básico | 64 | MIT (OSI permisiva) | sin grupo |
| `magnitude` | motores | Motor de inferencia local que adapta su ejecución al hardware y ofrece… | 3 Avanzado | 62 | Apache-2.0 (OSI permisiva) | sin grupo |
| `mlx-lm` | motores | Paquete de Apple para generar texto y afinar LLM en Apple Silicon con MLX… | 3 Avanzado | 59 | MIT (OSI permisiva) | sin grupo |
| `transformers.js` | motores | Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y… | 2 Intermedio | 59 | Apache-2.0 (OSI permisiva) | sin grupo |
| `freetoken` | motores | Herramientas para servir modelos de IA en hardware local mediante las rutas de… | 3 Avanzado | 58 | Apache-2.0 (OSI permisiva) | sin grupo |
| `mlc-llm` | motores | Motor universal de despliegue de LLM con compilación de ML: ejecuta modelos en… | 3 Avanzado | 56 | Apache-2.0 (OSI permisiva) | sin grupo |
| `llamafile` | motores | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier… | 1 Básico | 52 | Apache-2.0 (OSI permisiva) | alternativa |
| `airllm` | motores | Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante… | 3 Avanzado | 51 | Apache-2.0 (OSI permisiva) | sin grupo |
| `koboldcpp` | motores | Ejecutable único basado en llama.cpp para correr modelos GGUF en local con… | 3 Avanzado | 46 | AGPL-3.0 (OSI copyleft) | alternativa |
| `inferssd` | motores | Ejecuta modelos locales de tipo MoE leyendo partes de sus pesos desde un SSD… | 3 Avanzado | — | Apache-2.0 | sin grupo |
| `open-webui` | chats | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI… | 1 Básico | 74 | Open WebUI License (BSD-3-Clause + cláusula de marca) (source-available) | recomendado |
| `cherry-studio` | chats | App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de… | 1 Básico | 72 | AGPL-3.0 (OSI copyleft) | alternativa |
| `lobehub` | chats | Espacio de trabajo con super-agentes y una interfaz de chat moderna… | 2 Intermedio | 70 | LobeHub Community License (Apache-2.0 + condiciones) (source-available) | alternativa |
| `librechat` | chats | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola… | 2 Intermedio | 68 | MIT (OSI permisiva) | alternativa |
| `jan` | chats | Aplicación de escritorio para conversar con modelos locales y configurar… | 1 Básico | 65 | Apache-2.0 (OSI permisiva) | alternativa |
| `nextchat` | chats | Cliente de chat de IA ligero y multiplataforma (web, escritorio y móvil) para… | 2 Intermedio | 63 | MIT (OSI permisiva) | alternativa |
| `textgen` | chats | App open source para LLM locales con texto, visión, herramientas y API… | 2 Intermedio | 53 | AGPL-3.0 (OSI copyleft) | alternativa |
| `chatbox` | chats | Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos… | 1 Básico | 52 | GPL-3.0 (OSI copyleft) | alternativa |
| `sillytavern` | chats | Interfaz local avanzada para chatear con LLM: une muchas APIs, personajes, rol… | 2 Intermedio | 51 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `anything-llm` | workspaces | App todo en uno para chatear con tus documentos y usar agentes con modelos… | 1 Básico | 78 | MIT (OSI permisiva) | recomendado |
| `odysseus` | workspaces | Workspace auto-hospedado que unifica chats, research, documentos, correo… | 3 Avanzado | 73 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `private-gpt` | workspaces | Capa de API completa para apps de IA privadas sobre modelos locales: RAG… | 2 Intermedio | 67 | Apache-2.0 (OSI permisiva) | alternativa |
| `hermes-desktop` | workspaces | App de escritorio que envuelve al agente Hermes en una interfaz nativa. | 1 Básico | 54 | MIT (OSI permisiva) | sin grupo |
| `khoj` | workspaces | Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con… | 2 Intermedio | 48 | AGPL-3.0 (OSI copyleft) | alternativa |
| `claude-second-brain` | workspaces | Organiza una bóveda de Obsidian para que Claude Code consulte y mantenga notas… | 2 Intermedio | — | MIT | sin grupo |
| `open-notebook` | notebooklm | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes… | 2 Intermedio | 67 | MIT (OSI permisiva) | recomendado |
| `surfsense` | notebooklm | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | alternativa |
| `notebooklm-py` | notebooklm | API Python no oficial para interactuar programáticamente con NotebookLM de… | 2 Intermedio | 59 | MIT (OSI permisiva) | sin grupo |
| `notebooklm-mcp-cli` | notebooklm | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar… | 1 Básico | 51 | MIT (OSI permisiva) | sin grupo |

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

### Open WebUI (`open-webui`)

- **Repo:** https://github.com/open-webui/open-webui · Open WebUI License (BSD-3-Clause + cláusula de marca) · nivel 1 · 74/100 · recomendado en «Interfaces de chat con LLM»
- **Qué es:** Open WebUI, plataforma de chat con IA autoalojada y extensible, diseñada para poder funcionar sin conexión, de Open WebUI Inc. (creada por Timothy Jaeryang Baek).
- **Cuándo elegirlo:** Casos: Unificar chats de modelos locales; Crear una interfaz compartida para un equipo.
- **Requisitos:** nivel 1: preparación sencilla; Docker; Ollama accesible o proveedor remoto; volumen persistente; hardware prerequisites; API de IA: opcional; Docker; Ollama accesible o proveedor remoto; volumen persistente.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/open-webui/open-webui/blob/main/README.md

  ```bash
  docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
  ```
- **Primera prueba propuesta (no ejecutada):** Conecta un modelo y conversa sobre un texto ficticio antes de cargar documentos privados Éxito: Puedes ver el modelo seleccionado y conservar una conversación
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `searxng` [4/busqueda]
- **Alternativas:** `cherry-studio`, `lobehub`, `librechat`, `jan`, `nextchat`, `textgen`, `chatbox`, `anything-llm`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): librechat, lobehub, anything-llm, textgen. La cláusula de marca limita el rebranding: revisa LICENSE antes de redistribuirlo con otra…. Instalar la interfaz no instala todos los modelos; confirma que Docker puede alcanzar el servidor de inferencia.

### Cherry Studio (`cherry-studio`)

- **Repo:** https://github.com/CherryHQ/cherry-studio · AGPL-3.0 · nivel 1 · 72/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Estación de trabajo de IA de escritorio para Windows, macOS y Linux, de CherryHQ, con app móvil aparte. La edición comunitaria es AGPL-3.0 (el uso comercial se permite cumpliendo la AGPL; hay licencia comercial y una edición Enterprise)…
- **Cuándo elegirlo:** Casos: Comparar respuestas de varios modelos; Organizar una base documental de prueba.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador para Windows, macOS o Linux; proveedor o Ollama/LM Studio; hardware prerequisites; API de IA: opcional; Instalador para Windows, macOS o Linux; proveedor o Ollama/LM Studio.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://cherryai.com/docs/en/getting-started/quick-start/
- **Primera prueba propuesta (no ejecutada):** Configura un modelo y prueba una pregunta sobre una nota ficticia en un espacio de trabajo Éxito: Puedes comprobar el proveedor y la respuesta usada en la conversación
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `playwright-mcp` [5/servidores]
- **Alternativas:** `open-webui`, `lobehub`, `librechat`, `jan`, `nextchat`, `textgen`, `chatbox`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): jan, lobehub. Los agentes pueden ejecutar comandos: revisa sus permisos. Es una app multiproveedor; escoger Anthropic u OpenAI no la convierte en sesión de Claude Code o Codex.

### LobeHub (`lobehub`)

- **Repo:** https://github.com/lobehub/lobehub · LobeHub Community License (Apache-2.0 + condiciones) · nivel 2 · 70/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Plataforma de agentes de código abierto de LobeHub, antes conocida como Lobe Chat, que se presenta como «superagentes en tu equipo». Su README indica Apache 2.0, aunque GitHub no reconoce la licencia como estándar [DATO NO VERIFICADO…
- **Cuándo elegirlo:** Casos: Organizar agentes para tareas de equipo; Conectar un agente de código a un espacio de trabajo.
- **Requisitos:** nivel 2: preparación sencilla, varios servicios con Docker Compose; Docker y Compose; modelo; servicios de la ruta elegida; hardware prerequisites; API de IA: depends; Docker y Compose; modelo; servicios de la ruta elegida.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/lobehub/lobehub/blob/canary/README.md

  ```bash
  mkdir lobehub && cd lobehub
  bash <(curl -fsSL https://lobe.li/setup.sh) -l en
  docker compose up -d
  ```
- **Primera prueba propuesta (no ejecutada):** Crea un asistente de prueba y distingue su modelo del agente externo que puedas conectar Éxito: Puedes identificar qué proveedor atiende cada conversación
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `playwright-mcp` [5/servidores]
- **Alternativas:** `open-webui`, `cherry-studio`, `librechat`, `jan`, `nextchat`, `textgen`, `chatbox`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): open-webui, librechat, cherry-studio. SearXNG ya viene en su Compose; no instales otro aparte. Las skills portables y conectar un agente externo son funciones distintas; la página de integración consultada aún está en migración documental.

### LibreChat (`librechat`)

- **Repo:** https://github.com/LibreChat-AI/LibreChat · MIT · nivel 2 · 68/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Plataforma de chat con IA de código abierto (MIT) y autoalojable, del equipo LibreChat-AI, con agentes, MCP y autenticación multiusuario empresarial. Muy activa (v0.8.8 descrita en el README; sin releases formales en GitHub).
- **Cuándo elegirlo:** Casos: Unificar proveedores en una interfaz; Crear asistentes con herramientas y archivos.
- **Requisitos:** nivel 2: preparación media; Ruta de despliegue elegida; base de datos; proveedor u Ollama; hardware prerequisites; API de IA: opcional; Ruta de despliegue elegida; base de datos; proveedor u Ollama.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://www.librechat.ai/docs
- **Primera prueba propuesta (no ejecutada):** Conecta un proveedor y prueba un agente sin herramientas antes de añadir archivos Éxito: Puedes identificar el modelo y revisar la conversación
- **Combina con:** `litellm` [23/serving], `ollama` [8/motores], `langfuse` [23/observabilidad], `llama-cpp` [8/motores], `pgvector` [6/vectores], `exo` [8/motores]
- **Alternativas:** `open-webui`, `cherry-studio`, `lobehub`, `jan`, `nextchat`, `textgen`, `chatbox`
- **Riesgos y avisos:** Alternativas (elige una): open-webui, lobehub. Meilisearch, pgvector y RAG API ya vienen en su Compose. Sus agentes y MCP funcionan dentro de LibreChat; no acreditan usar una suscripción de otro editor para ejecutarlo.

### Jan (`jan`)

- **Repo:** https://github.com/janhq/jan · Apache-2.0 · nivel 1 · 65/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Aplicación de escritorio de código abierto presentada como reemplazo de ChatGPT, de Menlo Research (janhq). Licencia Apache 2.0 según su README (GitHub no la detecta como estándar); activa, con versiones frecuentes (v0.8.8).
- **Cuándo elegirlo:** Casos: Conversar con un modelo privado; Comparar un modelo local con una API.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador de escritorio oficial; RAM y disco; modelo compatible; hardware prerequisites; API de IA: opcional; Instalador de escritorio oficial; RAM y disco; modelo compatible.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/janhq/jan` — fuente: https://github.com/janhq/jan/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Desde la app descarga un modelo pequeño y prueba una conversación local Éxito: Ves el modelo cargado y puedes repetir la consulta sin proveedor remoto
- **Combina con:** `llmfit` [8/motores], `ollama` [8/motores], `playwright-mcp` [5/servidores]
- **Alternativas:** `open-webui`, `cherry-studio`, `lobehub`, `librechat`, `nextchat`, `textgen`, `chatbox`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): cherry-studio, textgen, chatbox. Para comenzar usa la distribución de escritorio; make dev y yarn son rutas para desarrollar el código de Jan.

### NextChat (`nextchat`)

- **Repo:** https://github.com/ChatGPTNextWeb/NextChat · MIT · nivel 2 · 63/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Cliente de chat de código abierto (MIT), antes ChatGPT-Next-Web, muy popular. Su organización ofrece además un servicio SaaS de pago por uso; el repositorio sigue siendo el cliente autoalojable.
- **Cuándo elegirlo:** Casos: desplegar un chat privado con tu propia clave para un equipo pequeño; usar un modelo autoalojado compatible con OpenAI desde una interfaz web ligera.
- **Requisitos:** nivel 2: preparación sencilla, requiere clave de API; TypeScript, Dockerfile, docker-compose.yml, package.json; API de IA: sí.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ChatGPTNextWeb/NextChat/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega NextChat con Docker o Vercel usando tu clave de API y abre un chat. Éxito: El chat responde con el modelo configurado y el historial queda en el navegador.
- **Combina con:** `localai` [8/motores], `litellm` [23/serving], `fastmcp` [5/sdk]
- **Alternativas:** `open-webui`, `cherry-studio`, `lobehub`, `librechat`, `jan`, `textgen`, `chatbox`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): lobehub, chatbox. Protege el despliegue con la variable CODE si es público.

### Text Generation WebUI (`textgen`)

- **Repo:** https://github.com/oobabooga/textgen · AGPL-3.0 · nivel 2 · 53/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Aplicación de escritorio para LLM locales, de código abierto (AGPL-3.0) y sin telemetría, de oobabooga (antes text-generation-webui). Madura y con versiones regulares (v4.9).
- **Cuándo elegirlo:** Casos: Probar modelos GGUF sin una API remota; Servir un endpoint local para otra app.
- **Requisitos:** nivel 2: instaladores de un clic por sistema; Distribución portable apropiada a tu GPU o CPU; modelo GGUF; hardware prerequisites; API de IA: no; Distribución portable apropiada a tu GPU o CPU; modelo GGUF.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up --build` — fuente: https://github.com/oobabooga/textgen/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Carga un modelo pequeño en la app y revisa texto generado y consumo de memoria Éxito: Puedes identificar backend, modelo y memoria utilizada
- **Combina con:** `librechat`, `llmfit` [8/motores], `unsloth` [24/entrenamiento], `sillytavern`
- **Alternativas:** `open-webui`, `cherry-studio`, `lobehub`, `librechat`, `jan`, `nextchat`, `chatbox`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): jan, open-webui. Antes conocida por rutas text-generation-webui; usa la distribución que corresponda a tu hardware y distingue API de inferencia de token de autenticación.

### chatbox (`chatbox`)

- **Repo:** https://github.com/chatboxai/chatbox · GPL-3.0 · nivel 1 · 52/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Cliente de escritorio para ChatGPT, Claude y otros LLM, en su edición comunitaria de código abierto (GPLv3) de chatboxai; el código se sincroniza con la versión Pro. Activo (v1.24.4).
- **Cuándo elegirlo:** Casos: Conversar con varios proveedores; Probar un modelo local desde escritorio.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador Community para tu sistema; proveedor o instancia Ollama; hardware prerequisites; API de IA: opcional; Instalador Community para tu sistema; proveedor o instancia Ollama.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/chatboxai/chatbox.git` — fuente: https://github.com/chatboxai/chatbox/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un proveedor y guarda una conversación con una nota ficticia Éxito: Puedes identificar el modelo y recuperar el chat
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `localai` [8/motores]
- **Alternativas:** `open-webui`, `cherry-studio`, `lobehub`, `librechat`, `jan`, `nextchat`, `textgen`
- **Riesgos y avisos:** Alternativa (elige una): jan. No confundas la edición comunitaria con los servicios comerciales ni un proveedor Claude con Claude Code.

### SillyTavern (`sillytavern`)

- **Repo:** https://github.com/SillyTavern/SillyTavern · AGPL-3.0 · nivel 2 · 51/100
- **Qué es:** Interfaz de usuario local de código abierto (AGPL-3.0), nacida en 2023 como fork de TavernAI 1.2.8 y mantenida por una comunidad de más de 300 contribuyentes. No ofrece servicios alojados ni rastrea datos de usuario según el proyecto.
- **Cuándo elegirlo:** Casos: escribir historias o partidas de rol con personajes y memoria persistente; probar el mismo prompt contra varios modelos locales y remotos.
- **Requisitos:** nivel 2: preparación media; JavaScript, Dockerfile, package.json; hardware model_dependent; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/SillyTavern/SillyTavern -b release` — fuente: https://docs.sillytavern.app/installation/windows/
- **Primera prueba propuesta (no ejecutada):** Instala SillyTavern con Node.js 20+, conéctalo a un backend local como KoboldCpp u Ollama y abre un chat. Éxito: El chat responde con el modelo conectado y la conversación se guarda en tu equipo.
- **Combina con:** `koboldcpp` [8/motores], `ollama` [8/motores], `comfyui` [11/interfaces], `kokoro` [29/tts], `textgen`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. La curva de aprendizaje es alta por diseño; las tarjetas de personaje de terceros pueden contener prompts no deseados.

### AnythingLLM (`anything-llm`)

- **Repo:** https://github.com/Mintplex-Labs/anything-llm · MIT · nivel 1 · 78/100 · recomendado en «Workspaces privados con documentos y chat»
- **Qué es:** Aplicación de IA «todo en uno» de código abierto (MIT) de Mintplex Labs, con versión de escritorio (Mac, Windows, Linux), Docker multiusuario, instancia alojada y app Android. Madura y activa (v1.19.0).
- **Cuándo elegirlo:** Casos: Consultar documentación propia; Separar bases de conocimiento por proyecto.
- **Requisitos:** nivel 1: preparación sencilla; App de escritorio o Docker; LLM y embeddings; documento de prueba; hardware prerequisites; API de IA: opcional; App de escritorio o Docker; LLM y embeddings; documento de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un workspace con un PDF corto y consulta un dato presente en él Éxito: Puedes abrir el fragmento que apoya la respuesta
- **Combina con:** `ollama` [8/motores], `qdrant` [6/vectores], `litellm` [23/serving], `localai` [8/motores], `chroma` [6/vectores], `milvus` [6/vectores]
- **Alternativas:** `private-gpt`, `khoj`, `open-webui`, `onyx`
- **Riesgos y avisos:** Alternativas (elige una): open-webui, khoj, private-gpt, onyx. Desktop, Docker y móvil tienen capacidades y licencias que debes comprobar; elige también embeddings locales para una ruta privada completa.

### odysseus (`odysseus`)

- **Repo:** https://github.com/odysseus-dev/odysseus · AGPL-3.0 · nivel 3 · 73/100
- **Qué es:** Espacio de trabajo de IA autoalojado de código abierto (AGPL-3.0) de odysseus-dev que reúne chat, agentes, investigación, documentos, correo, notas, calendario y flujos con modelos locales.
- **Cuándo elegirlo:** Casos: Organizar notas y tareas con IA; Comparar respuestas de modelos desde un workspace.
- **Requisitos:** nivel 3: preparación pesada, varios servicios con Docker Compose; Docker; configuración .env; proveedor o modelos locales; hardware prerequisites; API de IA: depends; Docker; configuración .env; proveedor o modelos locales.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/odysseus-dev/odysseus/blob/dev/README.md

  ```bash
  git clone https://github.com/odysseus-dev/odysseus.git
  cd odysseus
  cp .env.example .env
  docker compose up -d --build
  ```
- **Primera prueba propuesta (no ejecutada):** Abre un chat con un texto ficticio y prueba el editor de documentos sin conectar correo real Éxito: Puedes distinguir conversación, documento y herramientas habilitadas
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `playwright-mcp` [5/servidores]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Mantén `AUTH_ENABLED=true` y `LOCALHOST_BYPASS=false` en cualquier despliegue en red. ChromaDB y SearXNG ya vienen en su Compose. Local/API describe el modelo elegido; conservar la app en tu servidor no impide enviar datos a un proveedor remoto.

### PrivateGPT (`private-gpt`)

- **Repo:** https://github.com/zylon-ai/private-gpt · Apache-2.0 · nivel 2 · 67/100 · alternativa en «Workspaces privados con documentos y chat»
- **Qué es:** Capa de API de código abierto (Apache 2.0) de Zylon que convierte modelos locales en aplicaciones de IA para producción; es la base de la plataforma on-premise Zylon. Versión 1.0.1 publicada en 2026.
- **Cuándo elegirlo:** Casos: Construir una API privada sobre documentos; Usar un modelo local como backend de programación.
- **Requisitos:** nivel 2: preparación media; Servidor LLM compatible OpenAI; Python 3.11 o distribución adecuada; documentos de prueba; hardware prerequisites; API de IA: depends; Servidor LLM compatible OpenAI; Python 3.11 o distribución adecuada; documentos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install private-gpt` — fuente: https://github.com/zylon-ai/private-gpt/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta el servidor local y consulta un documento breve con la API de RAG Éxito: Puedes seguir la consulta y comprobar el fragmento recuperado
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `llama-cpp` [8/motores]
- **Alternativas:** `anything-llm`, `khoj`
- **Riesgos y avisos:** Alternativa (elige una): anything-llm. La combinación antigua con qdrant se retiró porque el README actual no la menciona. La guía documenta backend local para Claude Code; no confirma por eso integración de todas las funciones de Codex o Antigravity.

### Hermes Desktop (`hermes-desktop`)

- **Repo:** https://github.com/fathah/hermes-desktop · MIT · nivel 1 · 54/100
- **Qué es:** Aplicación de escritorio nativa mantenida por la comunidad (Hermes One, de fathah) para instalar, configurar y usar Hermes Agent de Nous Research. Licencia MIT; en desarrollo activo (v0.7.8), con funciones que pueden cambiar.
- **Cuándo elegirlo:** Casos: Usar Hermes desde una interfaz de escritorio; Consultar una instancia remota de Hermes.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador oficial del proyecto; backend Hermes local o remoto; proveedor o endpoint local; hardware prerequisites; API de IA: depends; Instalador oficial del proyecto; backend Hermes local o remoto; proveedor o endpoint local.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install hermes-desktop` — fuente: https://github.com/fathah/hermes-desktop/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un backend de prueba y confirma la dirección antes de iniciar un chat Éxito: La interfaz muestra el backend y devuelve una respuesta del proveedor elegido
- **Combina con:** `hermes-agent` [21/asistentes], `ollama` [8/motores], `mem0` [6/memoria], `vllm` [23/serving]
- **Riesgos y avisos:** El README sugiere conceder temporalmente sudo sin contraseña en WSL para instalar; revierte el cambio al terminar. Proyecto en desarrollo activo; no hace falta aplicar el ejemplo de sudoers del README para explicar o elegir la ruta de instalación.

### Khoj (`khoj`)

- **Repo:** https://github.com/khoj-ai/khoj · AGPL-3.0 · nivel 2 · 48/100 · alternativa en «Workspaces privados con documentos y chat»
- **Qué es:** Aplicación de IA personal («segundo cerebro») de código abierto (AGPL-3.0) y autoalojable de Khoj, que escala de un uso individual en el dispositivo a IA empresarial.
- **Cuándo elegirlo:** Casos: Consultar notas desde Obsidian; Crear un asistente de investigación personal.
- **Requisitos:** nivel 2: preparación media; Ruta self-host o cuenta Cloud; modelo; notas de prueba; hardware prerequisites; API de IA: depends; Ruta self-host o cuenta Cloud; modelo; notas de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install 'khoj[local]'` — fuente: https://github.com/khoj-ai/khoj/blob/master/documentation/docs/get-started/setup.mdx
- **Primera prueba propuesta (no ejecutada):** Añade dos notas y pregunta por un dato que solo aparece en una Éxito: La respuesta permite revisar la nota utilizada
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `markitdown` [13/conversion]
- **Alternativas:** `anything-llm`, `private-gpt`, `surfsense`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): anything-llm, surfsense. Tiene plugin oficial para Obsidian. El README admite LLM locales y remotos; no mezcles la instalación de Khoj con su proyecto relacionado Pipali.

### Claude Second Brain (`claude-second-brain`)

- **Repo:** https://github.com/jessepinkman9900/claude-second-brain · MIT · nivel 2 · —/100
- **Qué es:** Organiza una bóveda de Obsidian para que Claude Code consulte y mantenga notas con instrucciones y búsqueda local.
- **Cuándo elegirlo:** Casos: Probar una wiki personal con notas ficticias.; Buscar referencias locales a un tema en una bóveda de demostración.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP), requiere programar con él; JavaScript, package.json; API de IA: no; Claude Code, Obsidian y una bóveda nueva; consulta la guía para qmd y dependencias..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/jessepinkman9900/claude-second-brain/blob/599f55ad50afceb9eae4f31746aa37274087d239/README.md
- **Primera prueba propuesta (no ejecutada):** Prepara una bóveda desechable con tres notas y siembra una consulta a partir del ejemplo. Éxito: El asistente encuentra la nota relevante y muestra qué documento utilizó.
- **Riesgos y avisos:** El inicio instala dependencias y crea archivos. Búsqueda local no significa que el contexto enviado a Claude sea local.

### open-notebook (`open-notebook`)

- **Repo:** https://github.com/lfnovo/open-notebook · MIT · nivel 2 · 67/100 · recomendado en «Alternativas a NotebookLM»
- **Qué es:** Alternativa de código abierto (MIT) a NotebookLM de Google, centrada en la privacidad y creada por Luis Novo (lfnovo). Activa (v1.15.1), con interfaz en 14 idiomas.
- **Cuándo elegirlo:** Casos: Estudiar documentos en una libreta; Generar un resumen o audio sobre material propio.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Docker; proveedores de chat, embeddings y audio según función; fuentes de prueba; hardware prerequisites; API de IA: depends; Docker; proveedores de chat, embeddings y audio según función; fuentes de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://github.com/lfnovo/open-notebook/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un notebook con dos fuentes y pregunta por un dato con referencia Éxito: Puedes identificar la fuente y corregir un resumen
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `activepieces` [1/motores], `scientific-agent-skills` [27/dominio], `olmocr` [13/ocr], `vibevoice` [29/tts]
- **Alternativas:** `surfsense`, `deeptutor`
- **Riesgos y avisos:** Alternativas (elige una): deeptutor, surfsense. En redes compartidas pon una contraseña o un proxy delante. La app auto-hospedada no garantiza que todos los datos se procesen localmente: depende de cada proveedor que selecciones.

### SurfSense (`surfsense`)

- **Repo:** https://github.com/MODSetter/SurfSense · Apache-2.0 · nivel 2 · 64/100 · alternativa en «Alternativas a NotebookLM»
- **Qué es:** Aplicación de escritorio de código abierto (Apache 2.0) de MODSetter, alternativa a NotebookLM que puede funcionar sin conexión («air-gapped») para documentos que no puedes subir.
- **Cuándo elegirlo:** Casos: Revisar un contrato de prueba con comentarios; Extraer datos de un archivo Excel ficticio.
- **Requisitos:** nivel 2: preparación media; Instalador para tu sistema; modelo local o remoto; LibreOffice solo para conversiones Office; hardware prerequisites; API de IA: depends; Instalador para tu sistema; modelo local o remoto; LibreOffice solo para conversiones Office.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://raw.githubusercontent.com/MODSetter/SurfSense/main/docker/scripts/install.sh \| bash` — fuente: https://github.com/MODSetter/SurfSense/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Añade un documento ficticio y pide una edición que se guarde como copia Éxito: Puedes comparar original y archivo nuevo y revisar las citas
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `playwright-mcp` [5/servidores]
- **Alternativas:** `open-notebook`, `khoj`
- **Riesgos y avisos:** Alternativas (elige una): open-notebook, khoj. El índice puede permanecer local aunque el modelo sea remoto; LibreOffice no viene incluido para las conversiones Office.

### notebooklm-py (`notebooklm-py`)

- **Repo:** https://github.com/teng-lin/notebooklm-py · MIT · nivel 2 · 59/100
- **Qué es:** API de Python no oficial y skill para agentes para Google NotebookLM, rebautizado como Gemini Notebook en julio de 2026, creada por teng-lin. MIT y muy activa (v0.8.6); usa APIs no documentadas de Google que pueden cambiar sin aviso y no…
- **Cuándo elegirlo:** Casos: Automatizar consultas documentales; Exportar mapas o resúmenes propios.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python y uv o pipx; sesión Google; Chromium para login; notebook de prueba; hardware prerequisites; API de IA: no; Python y uv o pipx; sesión Google; Chromium para login; notebook de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install "notebooklm-py[browser]"` — fuente: https://github.com/teng-lin/notebooklm-py/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un notebook con una fuente propia breve y pregunta por un dato verificable Éxito: La consulta y las referencias aparecen en el mismo notebook de Google
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `obsidian-second-brain` [15/notas]
- **Riesgos y avisos:** Se retiró la combinación con notebooklm-mcp-cli: ambos son clientes no oficiales de la misma API y se solapan; elige uno. API no oficial con endpoints que pueden cambiar; los archivos descargados quedan locales pero la generación ocurre en Google.

### notebooklm-mcp-cli (`notebooklm-mcp-cli`)

- **Repo:** https://github.com/jacob-bd/gemini-notebook-mcp-cli · MIT · nivel 1 · 51/100
- **Qué es:** CLI y servidor MCP no oficiales para Gemini Notebook (antes Google NotebookLM), de jacob-bd. MIT y muy activo (v0.16.5); el repositorio se renombró a `gemini-notebook-mcp-cli`.
- **Cuándo elegirlo:** Casos: Administrar fuentes desde un agente; Exportar contenido generado por NotebookLM.
- **Requisitos:** nivel 1: preparación sencilla; Python; cuenta Google; cliente MCP; sesión del navegador; hardware prerequisites; API de IA: no; Python; cuenta Google; cliente MCP; sesión del navegador.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install notebooklm-mcp-cli` — fuente: https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta el asistente de setup, conecta un cliente y consulta una fuente ficticia en un notebook de prueba Éxito: Puedes contrastar la respuesta y comprobar el estado de autenticación
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `gemini-cli` [20/terminal]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Activa el almacenamiento protegido en equipos personales. Se retiraron las combinaciones con notebooklm-py (solapamiento) y awesome-mcp-servers (es una lista…. Documenta los tres clientes; instalar CLI o MCP no vuelve local la generación ni evita los cupos de NotebookLM.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-8.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Chats, modelos locales y espacios privados», lee `docs/alexandria/categoria-8.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-8.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
