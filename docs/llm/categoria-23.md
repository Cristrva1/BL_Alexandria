# Alexandría para agentes · Operar, evaluar y medir modelos de IA

Categoría 23 completa (31 repos, 3 subcategorías). Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=23 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `vllm` | serving | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de… | 3 Avanzado | 78 | Apache-2.0 (OSI permisiva) | recomendado |
| `litellm` | serving | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola… | 2 Intermedio | 77 | MIT + licencia Enterprise (litellm/enterprise/) (open-core) | recomendado |
| `omniroute` | serving | Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar… | 3 Avanzado | 76 | MIT (OSI permisiva) | alternativa |
| `tensorrt-llm` | serving | Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de… | 3 Avanzado | 75 | Apache-2.0 (OSI permisiva) | sin grupo |
| `ray` | serving | Motor de cómputo distribuido para IA: escala Python de un portátil a un… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `sglang` | serving | Framework de servicio de alto rendimiento para LLM y modelos multimodales. | 3 Avanzado | 67 | Apache-2.0 (OSI permisiva) | alternativa |
| `xinference` | serving | Plataforma abierta de inferencia para modelos de lenguaje, visión, embeddings… | 3 Avanzado | 66 | Apache-2.0 (OSI permisiva) | sin grupo |
| `gpustack` | serving | Gestor de clústeres de GPU para servir modelos de IA: configura vLLM, SGLang o… | 3 Avanzado | 62 | Apache-2.0 (OSI permisiva) | sin grupo |
| `bentoml` | serving | Framework Python para convertir modelos y pipelines de IA en APIs de… | 2 Intermedio | 57 | Apache-2.0 (OSI permisiva) | sin grupo |
| `claude-code-router` | serving | Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes… | 3 Avanzado | 57 | MIT (OSI permisiva) | alternativa |
| `backdoor` | serving | Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo… | 2 Intermedio | 36 | MIT (OSI permisiva) | alternativa |
| `portkey-gateway` | serving | Centraliza llamadas a distintos proveedores de modelos mediante una pasarela… | 3 Avanzado | — | MIT | sin grupo |
| `rtk` | tokens | Proxy de terminal que compacta salidas de comandos para reducir el contexto que… | 1 Básico | 69 | Apache-2.0 (OSI permisiva) | recomendado |
| `headroom` | tokens | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | alternativa |
| `gptcache` | tokens | Reutiliza respuestas de consultas parecidas a un modelo mediante una caché… | 2 Intermedio | — | MIT | sin grupo |
| `llmlingua` | tokens | Acorta texto de entrada para modelos de lenguaje y permite medir cuánto… | 2 Intermedio | — | MIT | sin grupo |
| `toon-format` | tokens | Convierte listas de objetos JSON a un texto con encabezado y filas para… | 2 Intermedio | — | MIT | sin grupo |
| `langfuse` | observabilidad | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM… | 2 Intermedio | 79 | MIT + licencia Enterprise (ee/) (open-core) | recomendado |
| `promptfoo` | observabilidad | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de… | 1 Básico | 79 | MIT (OSI permisiva) | recomendado |
| `opik` | observabilidad | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y… | 2 Intermedio | 75 | Apache-2.0 (OSI permisiva) | alternativa |
| `mlflow` | observabilidad | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM… | 1 Básico | 70 | Apache-2.0 (OSI permisiva) | alternativa |
| `deepeval` | observabilidad | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. | 2 Intermedio | 63 | Apache-2.0 (OSI permisiva) | alternativa |
| `loguru` | observabilidad | Librería de logging para Python centrada en la simplicidad ("logging that… | 2 Intermedio | 63 | MIT (OSI permisiva) | sin grupo |
| `openllmetry` | observabilidad | Instrumentación abierta basada en OpenTelemetry para aplicaciones de LLM: traza… | 2 Intermedio | 63 | Apache-2.0 (OSI permisiva) | sin grupo |
| `lm-eval-harness` | observabilidad | Arnés estándar de EleutherAI para evaluar modelos de lenguaje en cientos de… | 2 Intermedio | 57 | MIT (OSI permisiva) | sin grupo |
| `claude-code-usage-monitor` | observabilidad | Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a… | 2 Intermedio | 53 | MIT (OSI permisiva) | sin grupo |
| `guardrails` | observabilidad | Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales… | 2 Intermedio | 53 | Apache-2.0 (OSI permisiva) | sin grupo |
| `phoenix` | observabilidad | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM… | 1 Básico | 53 | Elastic-2.0 (source-available) | alternativa |
| `ragas` | observabilidad | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos… | 2 Intermedio | 51 | Apache-2.0 (OSI permisiva) | alternativa |
| `helicone` | observabilidad | Pasarela de IA y plataforma de observabilidad de LLM abierta: registra… | 2 Intermedio | 50 | Apache-2.0 (OSI permisiva) | alternativa |
| `ccusage` | observabilidad | Resume los tokens y estima el coste de tus sesiones de asistentes a partir de… | 2 Intermedio | — | MIT | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### vLLM (`vllm`)

- **Repo:** https://github.com/vllm-project/vllm · Apache-2.0 · nivel 3 · 78/100 · recomendado en «Servidores de inferencia de alto rendimiento»
- **Qué es:** vLLM, motor de inferencia y servicio de LLM nacido en el Sky Computing Lab de UC Berkeley y mantenido por una comunidad amplia. Licencia Apache-2.0.
- **Cuándo elegirlo:** Casos: Servir un modelo propio; Estudiar rendimiento de inferencia.
- **Requisitos:** nivel 3: preparación pesada; uv y Python compatibles; hardware soportado; pesos y memoria del modelo; hardware prerequisites; API de IA: no; uv y Python compatibles; hardware soportado; pesos y memoria del modelo.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/vllm-project/vllm/blob/main/README.md

  ```bash
  uv pip install vllm
  vllm download-kernels  # precompiled kernels for faster startup
  ```
- **Primera prueba propuesta (no ejecutada):** Sigue el quickstart con un modelo que quepa en tu equipo y solicita una respuesta breve Éxito: Puedes comprobar modelo cargado y endpoint de inferencia
- **Combina con:** `litellm`, `open-webui` [8/chats], `langchain` [3/py]
- **Alternativas:** `sglang`
- **Riesgos y avisos:** Alternativas (elige una): sglang. Es un motor de serving y no una app de chat; confirma la matriz de hardware y versión antes de instalar.

### litellm (`litellm`)

- **Repo:** https://github.com/BerriAI/litellm · MIT + licencia Enterprise (litellm/enterprise/) · nivel 2 · 77/100 · recomendado en «Pasarelas y routers de proveedores LLM»
- **Qué es:** LiteLLM, gateway de IA y SDK de Python de BerriAI que unifica el acceso a más de 100 proveedores de LLM con el formato de OpenAI. El código es MIT, salvo `litellm/enterprise/`, que tiene licencia comercial (por eso GitHub muestra…
- **Cuándo elegirlo:** Casos: Unificar llamadas a varios modelos; Enrutar un agente por un gateway propio.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python y uv; proveedor o endpoint local; presupuesto de prueba; hardware prerequisites; API de IA: opcional; Python y uv; proveedor o endpoint local; presupuesto de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add litellm` — fuente: https://github.com/BerriAI/litellm/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un único proveedor y envía una petición breve antes de activar fallback y balanceo Éxito: Puedes identificar el proveedor real y su consumo
- **Combina con:** `ollama` [8/motores], `open-webui` [8/chats], `langfuse` [23/observabilidad], `claude-code` [20/terminal]
- **Alternativas:** `omniroute`, `claude-code-router`, `backdoor`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): omniroute, claude-code-router, backdoor. Incidente de cadena de suministro de marzo de 2026 (PYSEC-2026-2): si instalaste 1.82.7 o…. Documenta harnesses de Claude Code y Codex en el SDK; pasar por el gateway no incorpora suscripciones ni elimina diferencias entre protocolos.

### OmniRoute (`omniroute`)

- **Repo:** https://github.com/cheaper-inference/OmniRoute · MIT · nivel 3 · 76/100 · alternativa en «Pasarelas y routers de proveedores LLM»
- **Qué es:** OmniRoute, pasarela local de IA gratuita creada por @diegosouzapw. Licencia MIT. Tiene un recuento de estrellas inusualmente alto (~88k) y publica versiones casi a diario (v3.8.53).
- **Cuándo elegirlo:** Casos: Centralizar proveedores de un agente; Comparar rutas y límites de consumo.
- **Requisitos:** nivel 3: preparación pesada; Node o distribución compatible; cuentas de proveedores o backend local; agente opcional; hardware prerequisites; API de IA: opcional; Node o distribución compatible; cuentas de proveedores o backend local; agente opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g omniroute` — fuente: https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.55/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un proveedor autorizado y revisa una petición breve antes de activar rotación, fallback o compresión Éxito: Puedes identificar qué cuenta y modelo atendieron la petición
- **Combina con:** `claude-code` [20/terminal], `cline` [20/editor], `ollama` [8/motores]
- **Alternativas:** `litellm`, `claude-code-router`, `backdoor`
- **Riesgos y avisos:** Alternativas (elige una): claude-code-router, backdoor, litellm. Combinar cuentas gratuitas puede incumplir las condiciones de algunos proveedores; el MITM…. Documenta Claude Code, Codex y un adaptador Antigravity; OAuth y automatización de terceros dependen de permisos y términos de cada proveedor.

### TensorRT-LLM (`tensorrt-llm`)

- **Repo:** https://github.com/NVIDIA/TensorRT-LLM · Apache-2.0 · nivel 3 · 75/100
- **Qué es:** TensorRT LLM, la librería de NVIDIA para optimizar inferencia de LLM y modelos de generación visual en GPU NVIDIA. Licencia Apache-2.0 según el README (GitHub muestra NOASSERTION). Es activa (~15k estrellas, v1.2.1).
- **Cuándo elegirlo:** Casos: Optimizar inferencia en GPU propia; Estudiar kernels y runtimes de NVIDIA.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él; GPU NVIDIA compatible; CUDA y dependencias según versión; modelo soportado; hardware prerequisites; API de IA: no; GPU NVIDIA compatible; CUDA y dependencias según versión; modelo soportado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/deployment-guide/deployment-guide-for-glm-5-on-trtllm.md

  ```bash
  docker run --rm -it --ipc=host --gpus all -p 8000:8000 -v "$HOST_MODELS_DIR":/models --name tensorrt_llm nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc25 /bin/bash
  ```
- **Primera prueba propuesta (no ejecutada):** Comprueba la matriz de hardware y ejecuta el ejemplo mínimo de inferencia antes de optimizar Éxito: Puedes relacionar motor, modelo y configuración de memoria
- **Combina con:** `litellm`, `open-webui` [8/chats], `transformers` [24/entrenamiento], `deepseek-v3` [24/modelos], `gpustack`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Recoge telemetría por defecto. Exclusivo de NVIDIA. Es infraestructura especializada y no una instalación universal para cualquier portátil o GPU.

### Ray (`ray`)

- **Repo:** https://github.com/ray-project/ray · Apache-2.0 · nivel 2 · 74/100
- **Qué es:** Framework de código abierto (Apache-2.0) creado en UC Berkeley y mantenido por Anyscale, que ofrece una plataforma gestionada. Muy maduro y usado a gran escala.
- **Cuándo elegirlo:** Casos: paralelizar un procesamiento de datos o entrenamiento en varias máquinas; servir modelos con autoescalado mediante Ray Serve.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install ray` — fuente: https://github.com/ray-project/ray/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install ray` y paraleliza una función con `@ray.remote` en tu equipo. Éxito: Las tareas se ejecutan en paralelo y el panel de Ray muestra su progreso.
- **Combina con:** `vllm`, `pytorch` [24/entrenamiento], `verl` [24/entrenamiento], `openrlhf` [24/entrenamiento]
- **Riesgos y avisos:** Para un solo equipo, la complejidad de Ray puede no compensar.

### SGLang (`sglang`)

- **Repo:** https://github.com/sgl-project/sglang · Apache-2.0 · nivel 3 · 67/100 · alternativa en «Servidores de inferencia de alto rendimiento»
- **Qué es:** SGLang, framework de inferencia para modelos de lenguaje, visión-lenguaje y difusión, de la comunidad sgl-project (LMSYS). Licencia Apache-2.0. Es muy activo (~39k estrellas, v0.5.23).
- **Cuándo elegirlo:** Casos: Servir un modelo para una aplicación; Estudiar inferencia multimodal.
- **Requisitos:** nivel 3: preparación pesada; uv; hardware y drivers compatibles; modelo con memoria suficiente; hardware prerequisites; API de IA: no; uv; hardware y drivers compatibles; modelo con memoria suficiente.
- **Instalación (documentada en la fuente; no ejecutada):** `uv pip install --prerelease=allow sglang` — fuente: https://github.com/sgl-project/sglang/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el quickstart y comprueba una petición breve al modelo servido Éxito: Puedes identificar modelo, proceso y respuesta del endpoint
- **Combina con:** `litellm`, `open-webui` [8/chats], `unsloth` [24/entrenamiento], `deepseek-v3` [24/modelos], `kimi-k2-7-code` [24/modelos], `llama-factory` [24/entrenamiento]
- **Alternativas:** `vllm`
- **Riesgos y avisos:** Alternativas (elige una): vllm. El comando del README admite prereleases; selecciona una versión apropiada según la documentación de tu hardware; patrocinio a contribuidores no es integración….

### Xinference (`xinference`)

- **Repo:** https://github.com/xorbitsai/inference · Apache-2.0 · nivel 3 · 66/100
- **Qué es:** Plataforma de inferencia de código abierto (Apache-2.0) de Xorbits, con edición Enterprise aparte. Activa.
- **Cuándo elegirlo:** Casos: servir un LLM, un modelo de embeddings y uno de voz desde un mismo servidor; conectar Dify, LangChain o LlamaIndex a modelos propios.
- **Requisitos:** nivel 3: preparación media, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install xinference` — fuente: https://github.com/xorbitsai/inference/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install xinference`, arranca `xinference-local` y lanza un modelo pequeño desde la interfaz web. Éxito: El modelo responde por la API compatible con OpenAI.
- **Combina con:** `vllm`, `llama-cpp` [8/motores], `langchain` [3/py], `llama-index` [3/py]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Cercano a ollama y gpustack; elige según la variedad de modelos y la escala que necesites.

### GPUStack (`gpustack`)

- **Repo:** https://github.com/gpustack/gpustack · Apache-2.0 · nivel 3 · 62/100
- **Qué es:** Gestor de clústeres de GPU de código abierto (Apache-2.0) del equipo GPUStack (Seal). Activo.
- **Cuándo elegirlo:** Casos: servir varios modelos en las GPU de tu laboratorio con una sola consola; dar a tu equipo claves de API compatibles con OpenAI sobre modelos propios.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `sudo docker run -d --name gpustack --restart unless-stopped -p 80:80 --volume gpustack-data:/var/lib/gpustack gpustack/gpustack` — fuente: https://github.com/gpustack/gpustack/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la guía de instalación con Docker en un nodo con GPU NVIDIA, despliega un modelo pequeño y prueba la API con curl. Éxito: El modelo responde por el endpoint compatible con OpenAI.
- **Combina con:** `vllm`, `sglang`, `tensorrt-llm`
- **Riesgos y avisos:** Cercano a xinference; GPUStack se centra en gestionar clústeres de GPU.

### BentoML (`bentoml`)

- **Repo:** https://github.com/bentoml/BentoML · Apache-2.0 · nivel 2 · 57/100
- **Qué es:** Framework de serving de código abierto (Apache-2.0) de BentoML, que ofrece la plataforma BentoCloud. Maduro.
- **Cuándo elegirlo:** Casos: publicar un modelo de Transformers como API REST; empaquetar un LLM servido con vLLM en una imagen desplegable.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U bentoml` — fuente: https://github.com/bentoml/BentoML/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install -U bentoml`, define el servicio de ejemplo del README y arráncalo con `bentoml serve`. Éxito: La API responde en localhost con el resultado del modelo.
- **Combina con:** `vllm`, `transformers` [24/entrenamiento], `pytorch` [24/entrenamiento]
- **Riesgos y avisos:** Cercano a ray (Ray Serve) en serving; BentoML se centra en empaquetar servicios.

### claude-code-router (`claude-code-router`)

- **Repo:** https://github.com/musistudio/claude-code-router · MIT · nivel 3 · 57/100 · alternativa en «Pasarelas y routers de proveedores LLM»
- **Qué es:** Claude Code Router (CCR), pasarela local y plano de control para agentes de programación, de @musistudio. Licencia MIT. Es muy popular (~38k estrellas, v3.1.4).
- **Cuándo elegirlo:** Casos: Comparar proveedores desde Claude Code; Organizar perfiles para Codex.
- **Requisitos:** nivel 3: preparación pesada; Node 22+ o app; proveedor y credenciales; agente de prueba; hardware prerequisites; API de IA: depends; Node 22+ o app; proveedor y credenciales; agente de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/musistudio/claude-code-router/blob/main/README.md

  ```sh
  npm install -g @musistudio/claude-code-router
  ccr ui
  ```
- **Primera prueba propuesta (no ejecutada):** Añade un proveedor, inicia el servidor local y aplica un perfil a una sesión de prueba Éxito: Puedes identificar endpoint, modelo y ruta efectiva
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal], `claude-code-hooks-mastery` [2/metodologia]
- **Alternativas:** `litellm`, `omniroute`, `backdoor`
- **Riesgos y avisos:** Alternativas (elige una): omniroute, backdoor, litellm. Usar modelos de terceros con Claude Code puede no estar soportado por Anthropic. Documenta perfiles para Claude Code y Codex; llamar local al gateway no confirma que el modelo se ejecute localmente ni garantiza todas las capacidades de cada….

### backdoor (`backdoor`)

- **Repo:** https://github.com/ajsai47/backdoor · MIT · nivel 2 · 36/100 · alternativa en «Pasarelas y routers de proveedores LLM»
- **Qué es:** Backdoor, proxy de terceros de @ajsai47 que permite usar Claude Code con otros proveedores de modelos. Licencia MIT. Es pequeño (~300 estrellas, sin releases) y su último cambio es de mayo de 2026.
- **Cuándo elegirlo:** Casos: Probar un backend local con Claude Code; Comparar proveedores compatibles.
- **Requisitos:** nivel 2: preparación media; Sistema compatible; Claude Code; proveedor u Ollama; carpeta de prueba; hardware prerequisites; API de IA: opcional; Sistema compatible; Claude Code; proveedor u Ollama; carpeta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/ajsai47/backdoor/blob/main/README.md

  ```bash
  git clone https://github.com/ajsai47/backdoor
  cd backdoor
  ./backdoor   # animated setup wizard — picks your provider, writes your config, launches Claude Code
  ```
- **Primera prueba propuesta (no ejecutada):** Revisa la configuración que propone el asistente y solicita una explicación corta sin herramientas externas Éxito: Puedes identificar el proveedor detrás del proxy
- **Combina con:** `claude-code` [20/terminal], `ollama` [8/motores], `vllm`
- **Alternativas:** `litellm`, `omniroute`, `claude-code-router`
- **Riesgos y avisos:** Alternativas (elige una): omniroute, claude-code-router, litellm. Proyecto pequeño y sin mantenimiento reciente. Es un adaptador independiente; afirmar privacidad local requiere revisar también búsquedas, telemetría y otras herramientas y no solo el endpoint del modelo.

### Portkey AI Gateway (`portkey-gateway`)

- **Repo:** https://github.com/Portkey-AI/gateway · MIT · nivel 3 · —/100
- **Qué es:** Centraliza llamadas a distintos proveedores de modelos mediante una pasarela con reglas de ruta, presupuestos y registro de solicitudes.
- **Cuándo elegirlo:** Casos: Hacer una llamada pequeña a un solo proveedor y medir latencia.; Comparar dos rutas ante un error simulado sin enviar información privada.
- **Requisitos:** nivel 3: preparación pesada, requiere clave de API; TypeScript, Dockerfile, package.json; API de IA: sí; Node.js/npm o un contenedor compatible; para inferencia, un proveedor habilitado y una clave propia de prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Portkey-AI/gateway/blob/669825cbe89ee51569918b8f78a9db486fd69dd4/README.md
- **Primera prueba propuesta (no ejecutada):** Instala una versión posterior al mínimo corregido y prueba una llamada con texto ficticio y presupuesto reducido. Éxito: Puedes identificar el proveedor utilizado en la respuesta o el registro de prueba.
- **Riesgos y avisos:** Usa 1.14.0 o posterior por el aviso; la versión publicada verificada fue 1.15.2. El modo gestionado y los proveedores tienen facturación independiente.

### rtk (`rtk`)

- **Repo:** https://github.com/rtk-ai/rtk · Apache-2.0 · nivel 1 · 69/100 · recomendado en «Compactar contexto y tokens»
- **Qué es:** RTK (Rust Token Killer), filtro de salidas de terminal para agentes de programación, de rtk-ai. El binario por defecto combina Apache-2.0 y BUSL-1.1, y la edición `rtk-oss` es solo Apache-2.0.
- **Cuándo elegirlo:** Casos: Reducir salida repetitiva de comandos; Estudiar consumo de contexto por tarea.
- **Requisitos:** nivel 1: preparación sencilla; Binario para tu sistema; agente y proyecto de prueba; configuración por agente; hardware prerequisites; API de IA: opcional; Binario para tu sistema; agente y proyecto de prueba; configuración por agente.
- **Instalación (documentada en la fuente; no ejecutada):** `winget install rtk-ai.rtk` — fuente: https://github.com/rtk-ai/rtk/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Prueba un comando RTK y compara su salida con la versión sin comprimir antes de activar hooks Éxito: Puedes comprobar datos omitidos y contadores de ahorro
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `gemini-cli` [20/terminal], `claude-code-usage-monitor` [23/observabilidad], `mimo-code` [20/terminal]
- **Alternativas:** `headroom`
- **Riesgos y avisos:** BSL (source-available): no es OSI; revisa usos comerciales y la fecha de cambio de licencia. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): headroom. Si quieres solo código Apache-2.0, instala `rtk-oss`. Claude y Codex tienen hooks documentados; Antigravity usa un archivo de reglas y no la misma automatización; las cifras de ahorro dependen de la tarea.

### headroom (`headroom`)

- **Repo:** https://github.com/headroomlabs-ai/headroom · Apache-2.0 · nivel 2 · 60/100 · alternativa en «Compactar contexto y tokens»
- **Qué es:** Headroom, capa de compresión de contexto para agentes y LLM de Headroom Labs (paquete `headroom-ai` en PyPI y npm). Licencia Apache-2.0. Es muy activo (~80k estrellas, v0.44.0).
- **Cuándo elegirlo:** Casos: Reducir salidas extensas de herramientas; Comparar una sesión con y sin compresión.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python compatible; contenido de prueba; agente o cliente MCP si lo conectas; hardware prerequisites; API de IA: opcional; Python compatible; contenido de prueba; agente o cliente MCP si lo conectas.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install headroom-ai` — fuente: https://github.com/headroomlabs-ai/headroom/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Comprime una salida JSON pequeña y compara el resultado con el original antes de envolver un agente Éxito: Puedes identificar qué se conservó y recuperar el original cuando corresponda
- **Combina con:** `claude-code` [20/terminal], `litellm` [23/serving], `context-engineering` [19/guias], `codegraph` [7/codigo], `claude-code-usage-monitor` [23/observabilidad], `mimo-code` [20/terminal]
- **Alternativas:** `rtk`
- **Riesgos y avisos:** Alternativas (elige una): rtk. El número de estrellas crece de forma inusual para un proyecto tan joven; los ahorros son mediciones del propio proyecto. Documenta wrap para Claude y Codex y MCP para cualquier cliente compatible; los ahorros de benchmarks no garantizan iguales respuestas en toda tarea.

### GPTCache (`gptcache`)

- **Repo:** https://github.com/zilliztech/GPTCache · MIT · nivel 2 · —/100
- **Qué es:** Reutiliza respuestas de consultas parecidas a un modelo mediante una caché semántica con reglas de comparación configurables.
- **Cuándo elegirlo:** Casos: Evitar recalcular preguntas repetidas en un prototipo.; Comparar falsos aciertos de caché con dos preguntas casi iguales.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Makefile, requirements.txt, setup.py; API de IA: opcional; Python y un componente de embeddings y almacenamiento compatible; entorno de prueba con consultas ficticias..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://gptcache.readthedocs.io
- **Primera prueba propuesta (no ejecutada):** Configura el ejemplo en un entorno aislado y manda dos consultas de ejemplo similares. Éxito: Puedes observar cuándo se reutiliza una respuesta y cuándo se vuelve a calcular.
- **Riesgos y avisos:** Los ejemplos con OpenAI requieren su clave. No compartas entradas y respuestas privadas entre usuarios de distintas cuentas.

### LLMLingua (`llmlingua`)

- **Repo:** https://github.com/microsoft/LLMLingua · MIT · nivel 2 · —/100
- **Qué es:** Acorta texto de entrada para modelos de lenguaje y permite medir cuánto contexto conservas antes de enviar el prompt.
- **Cuándo elegirlo:** Casos: Comparar un prompt largo con su versión comprimida.; Medir tokens ahorrados y revisar si mantuvo una restricción importante.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Makefile, pyproject.toml, setup.py; hardware model_dependent; API de IA: no; Python, PyTorch y un modelo de compresión compatible con el hardware..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://llmlingua.com/
- **Primera prueba propuesta (no ejecutada):** Comprime un texto público breve con un modelo local pequeño del proyecto. Éxito: Obtienes dos textos y puedes comparar tamaño, instrucciones conservadas y pérdidas.
- **Riesgos y avisos:** Menos tokens no garantiza la misma calidad; si después llamas a un LLM remoto, su tarifa es independiente.

### TOON (`toon-format`)

- **Repo:** https://github.com/toon-format/toon · MIT · nivel 2 · —/100
- **Qué es:** TOON es un formato de texto y una biblioteca JavaScript de referencia para codificar datos JSON.
- **Cuándo elegirlo:** Casos: Representar un inventario ficticio de productos con los mismos tres campos en cada fila.; Preparar una tabla de registros con idéntica estructura para comparar el tamaño con JSON compacto.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; TypeScript, package.json; API de IA: no; Node.js con npm y un proyecto con módulos ES.; Dos registros JSON ficticios con los mismos campos..
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @toon-format/toon` — fuente: https://github.com/toon-format/toon/blob/92d7fc6d8af920afc99d1b6533cfc976c472fe7d/README.md
- **Primera prueba propuesta (no ejecutada):** Usa encode con dos registros ficticios que compartan campos, siguiendo el ejemplo del README de la versión 4.4.0. Éxito: La salida conserva ambos registros y enumera los campos en el encabezado. Revisa los valores y compárala con el JSON…

### langfuse (`langfuse`)

- **Repo:** https://github.com/langfuse/langfuse · MIT + licencia Enterprise (ee/) · nivel 2 · 79/100 · recomendado en «Observabilidad y trazas de LLM»
- **Qué es:** Langfuse, plataforma open source de ingeniería de IA para observabilidad y evaluación de agentes; forma parte de ClickHouse desde enero de 2026. Es MIT salvo las carpetas `ee` (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Depurar un asistente; Comparar versiones de un prompt.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Docker o servicio Cloud; app de prueba; SDK o instrumentación; hardware prerequisites; API de IA: opcional; Docker o servicio Cloud; app de prueba; SDK o instrumentación.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/langfuse/langfuse/blob/main/README.md

  ```bash
  # Get a copy of the latest Langfuse repository
    git clone --depth=1 https://github.com/langfuse/langfuse.git
    cd langfuse
  
    # Run the langfuse docker compose
    docker compose up
  ```
- **Primera prueba propuesta (no ejecutada):** Registra una llamada de prueba y abre su traza para revisar entrada, salida y duración Éxito: Puedes rastrear una respuesta hasta la llamada que la produjo
- **Combina con:** `litellm` [23/serving], `langchain` [3/py], `open-webui` [8/chats], `ragas`
- **Alternativas:** `opik`, `mlflow`, `phoenix`, `helicone`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): phoenix, opik, mlflow. Las funciones `ee` tienen otra licencia. El MCP documentado en el README consulta documentación y no equivale a acceso automático a tus trazas; el núcleo MIT excluye carpetas ee.

### promptfoo (`promptfoo`)

- **Repo:** https://github.com/promptfoo/promptfoo · MIT · nivel 1 · 79/100 · recomendado en «Evaluación y pruebas de LLM»
- **Qué es:** Promptfoo, CLI y librería para evaluar y hacer red teaming de aplicaciones con LLM. Ahora forma parte de OpenAI y sigue siendo open source con licencia MIT. Es muy activo (~27k estrellas, 0.125.1).
- **Cuándo elegirlo:** Casos: Evaluar un prompt de soporte; Probar regresiones de un RAG.
- **Requisitos:** nivel 1: preparación sencilla; Node; dataset de preguntas; proveedor o Ollama; criterio de evaluación; hardware prerequisites; API de IA: opcional; Node; dataset de preguntas; proveedor o Ollama; criterio de evaluación.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/promptfoo/promptfoo/blob/main/README.md

  ```sh
  npm install -g promptfoo
  promptfoo init --example getting-started
  ```
- **Primera prueba propuesta (no ejecutada):** Crea dos variantes de un prompt y evalúalas con tres casos conocidos Éxito: Puedes comparar respuestas y detectar un fallo concreto
- **Combina con:** `langfuse`, `litellm` [23/serving], `vllm` [23/serving]
- **Alternativas:** `deepeval`, `ragas`, `dspy`
- **Riesgos y avisos:** Alternativas (elige una): deepeval, ragas, dspy. Tras la compra por OpenAI conviene vigilar la gobernanza del proyecto. Una puntuación depende del dataset, proveedor y evaluador; los tests de seguridad deben dirigirse a sistemas propios o autorizados.

### Opik (`opik`)

- **Repo:** https://github.com/comet-ml/opik · Apache-2.0 · nivel 2 · 75/100 · alternativa en «Observabilidad y trazas de LLM»
- **Qué es:** Opik, plataforma open source de Comet para observabilidad, evaluación y trazado de agentes de IA. Licencia Apache-2.0 en toda la plataforma (servidor incluido). Es muy activa (~23k estrellas, 2.2.143).
- **Cuándo elegirlo:** Casos: Depurar una cadena RAG; Revisar fallos con un agente de código.
- **Requisitos:** nivel 2: preparación media; Python; Cloud o instancia propia; app y datos de prueba; uv para MCP; hardware prerequisites; API de IA: opcional; Python; Cloud o instancia propia; app y datos de prueba; uv para MCP.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/comet-ml/opik/blob/main/README.md

  ```bash
  pip install opik
  opik configure
  ```
- **Primera prueba propuesta (no ejecutada):** Registra una traza y consúltala desde el panel o MCP con acceso de prueba Éxito: Puedes localizar entrada, salida y evaluación de esa ejecución
- **Combina con:** `langgraph` [3/py], `litellm` [23/serving], `ragas`, `dspy` [3/py]
- **Alternativas:** `langfuse`, `mlflow`, `phoenix`, `helicone`
- **Riesgos y avisos:** Alternativas (elige una): langfuse, phoenix. Documenta configuración MCP para Claude Code, Codex y otros clientes; puede registrar Ollama, pero no sirve el modelo por sí mismo.

### MLflow (`mlflow`)

- **Repo:** https://github.com/mlflow/mlflow · Apache-2.0 · nivel 1 · 70/100 · alternativa en «Observabilidad y trazas de LLM»
- **Qué es:** MLflow, plataforma open source de ingeniería de IA para agentes, LLM y modelos de ML. Licencia Apache-2.0. Es muy madura (~29k estrellas, v3.18.0) y el README cita más de 60 millones de descargas mensuales.
- **Cuándo elegirlo:** Casos: Registrar experimentos de ML; Añadir trazas a una app de IA.
- **Requisitos:** nivel 1: preparación sencilla; uv o Python; app y datos ficticios; agente opcional para instrumentar; hardware prerequisites; API de IA: opcional; uv o Python; app y datos ficticios; agente opcional para instrumentar.
- **Instalación (documentada en la fuente; no ejecutada):** `uvx mlflow server` — fuente: https://github.com/mlflow/mlflow/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Inicia el servidor de prueba y registra una ejecución pequeña con parámetros y resultado Éxito: Puedes abrir la ejecución y comparar sus datos
- **Combina con:** `dspy` [3/py], `transformers` [24/entrenamiento], `deepeval`, `ragas`, `qlib` [14/cuant], `airflow` [1/motores]
- **Alternativas:** `langfuse`, `opik`, `phoenix`, `helicone`
- **Riesgos y avisos:** Alternativas (elige una): langfuse. El wizard documenta Claude Code y Codex para añadir instrumentación; no es una autorización para cambiar automáticamente proyectos reales.

### DeepEval (`deepeval`)

- **Repo:** https://github.com/confident-ai/deepeval · Apache-2.0 · nivel 2 · 63/100 · alternativa en «Evaluación y pruebas de LLM»
- **Qué es:** DeepEval, framework open source de evaluación de LLM al estilo pytest, de Confident AI. Licencia Apache-2.0. Es muy activo (~19k estrellas, python-v4.2.4).
- **Cuándo elegirlo:** Casos: Detectar regresiones de un chatbot; Probar relevancia de respuestas RAG.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; casos con respuestas conocidas; modelo evaluador y embeddings si se usan; hardware prerequisites; API de IA: opcional; Python; casos con respuestas conocidas; modelo evaluador y embeddings si se usan.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U deepeval` — fuente: https://github.com/confident-ai/deepeval/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Evalúa tres respuestas ficticias con un criterio explícito y revisa una puntuación manualmente Éxito: Puedes relacionar el resultado con el caso y el juez seleccionado
- **Combina con:** `langchain` [3/py], `llama-index` [3/py], `mlflow`, `langfuse`
- **Alternativas:** `promptfoo`, `ragas`
- **Riesgos y avisos:** Alternativas (elige una): ragas, promptfoo. Las métricas con LLM juez cuestan tokens. El MCP mencionado pertenece al servicio compañero Confident AI; no todas las métricas necesitan LLM y un juez pequeño puede fallar al seguir el esquema.

### loguru (`loguru`)

- **Repo:** https://github.com/Delgan/loguru · MIT · nivel 2 · 63/100
- **Qué es:** Loguru, librería de logging para Python de @Delgan. Licencia MIT. Es madura y muy usada (~24k estrellas, 0.8.0).
- **Cuándo elegirlo:** Casos: Depurar una automatización; Añadir logs legibles a una app.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; script de prueba; hardware prerequisites; API de IA: no; Python; script de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install loguru` — fuente: https://github.com/Delgan/loguru/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Registra un mensaje y una excepción ficticia en un script pequeño Éxito: Puedes distinguir nivel, fecha y detalle del error
- **Combina con:** `litellm` [23/serving], `langfuse`, `pydantic-ai` [3/py]
- **Riesgos y avisos:** Sin alternativas declaradas. Ojo con `diagnose=True` en producción. Es una biblioteca de logging general y no un sistema de observabilidad LLM completo; evita registrar secretos o datos que no necesites.

### OpenLLMetry (`openllmetry`)

- **Repo:** https://github.com/traceloop/openllmetry · Apache-2.0 · nivel 2 · 63/100
- **Qué es:** Conjunto de extensiones de OpenTelemetry de código abierto (Apache-2.0) de Traceloop, empresa que ofrece una plataforma comercial. Sus convenciones semánticas se han incorporado a OpenTelemetry. Activo.
- **Cuándo elegirlo:** Casos: trazar llamadas a OpenAI, LangChain o Ollama en Grafana o Datadog; añadir observabilidad de LLM a una pila OpenTelemetry existente.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install traceloop-sdk` — fuente: https://github.com/traceloop/openllmetry/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install traceloop-sdk`, inicializa el SDK en un script con una llamada a un modelo y envía las trazas a la consola o a tu backend. Éxito: Ves las trazas con prompts, tokens y latencias.
- **Combina con:** `grafana` [10/bi], `langchain` [3/py], `llama-index` [3/py], `ollama` [8/motores]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Cercano a langfuse y phoenix, que ofrecen interfaz propia; OpenLLMetry solo instrumenta y exporta.

### LM Evaluation Harness (`lm-eval-harness`)

- **Repo:** https://github.com/EleutherAI/lm-evaluation-harness · MIT · nivel 2 · 57/100
- **Qué es:** Framework de evaluación de código abierto (MIT) de EleutherAI. Estándar de facto: es el motor del Open LLM Leaderboard de Hugging Face y lo usan muchos laboratorios. Activo.
- **Cuándo elegirlo:** Casos: comparar un modelo ajustado con su base en MMLU, HellaSwag o GSM8K; reproducir resultados de tablas de clasificación con la misma configuración.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, pyproject.toml; hardware model_dependent; API de IA: opcional; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "lm_eval[hf]"` — fuente: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install "lm_eval[hf]"` y evalúa un modelo pequeño de Hugging Face en una tarea ligera con `lm_eval --model hf --tasks ...`. Éxito: Obtienes una tabla con la métrica de la tarea y su error estándar.
- **Combina con:** `vllm` [23/serving], `sglang` [23/serving], `transformers` [24/entrenamiento], `torchtune` [24/entrenamiento], `gemma` [24/modelos]
- **Riesgos y avisos:** Las puntuaciones dependen de la versión de la tarea y del prompt; regístralas junto a los resultados.

### Claude-Code-Usage-Monitor (`claude-code-usage-monitor`)

- **Repo:** https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor · MIT · nivel 2 · 53/100
- **Qué es:** Claude Code Usage Monitor (`claude-monitor` en PyPI), monitor de terminal del uso de Claude Code, de @Maciek-roboblog. Licencia MIT. Es popular (~9k estrellas, v4.0.0) y su último cambio es de julio de 2026.
- **Cuándo elegirlo:** Casos: Revisar el uso de una sesión; Estudiar alertas y proyecciones de cuota.
- **Requisitos:** nivel 2: preparación media; uv o Python compatible; datos de uso de Claude Code; hardware prerequisites; API de IA: no; uv o Python compatible; datos de uso de Claude Code.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/blob/main/README.md

  ```bash
  # Install directly from PyPI with uv (easiest)
  uv tool install claude-monitor
  
  # Run from anywhere
  claude-monitor  # or cmonitor, ccmonitor for short
  ```
- **Primera prueba propuesta (no ejecutada):** Abre el monitor y compara una cifra con su etiqueta de procedencia y fecha Éxito: Puedes distinguir consumo observado, estado oficial y previsión
- **Combina con:** `claude-code` [20/terminal], `rtk` [23/tokens], `headroom` [23/tokens], `claude-token-efficient` [2/metodologia]
- **Riesgos y avisos:** Sin alternativas declaradas. Los límites por plan son estimaciones si no hay datos oficiales. Las previsiones son estimaciones y las fuentes tienen distinta cobertura; es una integración de lectura de Claude Code y no un modelo alternativo.

### NeMo Guardrails (`guardrails`)

- **Repo:** https://github.com/NVIDIA-NeMo/Guardrails · Apache-2.0 · nivel 2 · 53/100
- **Qué es:** NeMo Guardrails, toolkit open source de NVIDIA para añadir barreras programables a aplicaciones conversacionales con LLM. Licencia Apache-2.0 según el README (GitHub muestra NOASSERTION). Es activo (~7.5k estrellas, v0.24.1).
- **Cuándo elegirlo:** Casos: Guiar un asistente de soporte; Evaluar controles de una app propia.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; app conversacional; configuración Colang; modelo según rails; hardware prerequisites; API de IA: depends; Python; app conversacional; configuración Colang; modelo según rails.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install nemoguardrails` — fuente: https://github.com/NVIDIA-NeMo/Guardrails/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Define un flujo de tema permitido y prueba una pregunta dentro y otra fuera de ese tema Éxito: Puedes comprobar la regla aplicada y registrar sus límites
- **Combina con:** `langchain` [3/py], `promptfoo`, `vllm` [23/serving]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. No confundir con Guardrails AI (otro proyecto, no catalogado). Telemetría activa por defecto. NeMo Guardrails no garantiza seguridad total ni adecuación a todo sector; develop es desarrollo y la versión publicada debe elegirse de forma explícita.

### Phoenix (`phoenix`)

- **Repo:** https://github.com/Arize-ai/phoenix · Elastic-2.0 · nivel 1 · 53/100 · alternativa en «Observabilidad y trazas de LLM»
- **Qué es:** Arize Phoenix, plataforma de observabilidad de IA para experimentación, evaluación y depuración, de Arize. Licencia Elastic License 2.0 (código disponible, no OSI; GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Depurar una app con OpenTelemetry; Consultar trazas desde un agente.
- **Requisitos:** nivel 1: preparación sencilla; Python; app de prueba; instrumentación o cliente MCP; hardware prerequisites; API de IA: opcional; Python; app de prueba; instrumentación o cliente MCP.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Arize-ai/phoenix/blob/main/README.md

  ```shell
  pip install arize-phoenix
  phoenix serve
  ```
- **Primera prueba propuesta (no ejecutada):** Abre una traza de muestra y consulta una ejecución antes de conectar una aplicación real Éxito: Puedes identificar spans, latencia y entradas
- **Combina con:** `llama-index` [3/py], `langgraph` [3/py], `ollama` [8/motores], `claude-code` [20/terminal]
- **Alternativas:** `langfuse`, `opik`, `mlflow`, `helicone`
- **Riesgos y avisos:** Elastic License 2.0 (source-available, no OSI): limita ofrecerlo como servicio gestionado. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): langfuse, opik. La licencia ELv2 prohíbe ofrecerlo como servicio gestionado a terceros. El README declara Elastic License 2.0, por lo que no debe etiquetarse como licencia abierta sin restricciones; ofrece MCP y plugins Claude Code y Codex.

### Ragas (`ragas`)

- **Repo:** https://github.com/vibrantlabsai/ragas · Apache-2.0 · nivel 2 · 51/100 · alternativa en «Evaluación y pruebas de LLM»
- **Qué es:** Ragas, librería para evaluar y optimizar aplicaciones de LLM y RAG, ahora bajo la organización vibrantlabsai. Licencia Apache-2.0. Es activa (~16k estrellas, v0.4.4).
- **Cuándo elegirlo:** Casos: Medir un RAG con datos controlados; Comparar versiones de una cadena.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; dataset de evaluación; modelo y embeddings configurados; hardware prerequisites; API de IA: depends; Python; dataset de evaluación; modelo y embeddings configurados.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install ragas` — fuente: https://github.com/vibrantlabsai/ragas/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Evalúa una respuesta cuyo contexto y referencia conozcas y comprueba qué mide cada métrica Éxito: Puedes distinguir recuperación, relevancia y fidelidad
- **Combina con:** `llama-index` [3/py], `langfuse`, `langchain` [3/py], `opik`
- **Alternativas:** `promptfoo`, `deepeval`
- **Riesgos y avisos:** Alternativas (elige una): deepeval, promptfoo. El repo se movió de explodinggradients/ragas a vibrantlabsai/ragas (GitHub redirige). El ejemplo usa OpenAI y algunas métricas consumen modelos y embeddings; el proveedor y coste dependen de la métrica elegida y deben configurarse explícitamente.

### Helicone (`helicone`)

- **Repo:** https://github.com/Helicone/helicone · Apache-2.0 · nivel 2 · 50/100 · alternativa en «Observabilidad y trazas de LLM»
- **Qué es:** Plataforma de código abierto (Apache-2.0) de Helicone (Y Combinator W23), con nube de pago. Activa.
- **Cuándo elegirlo:** Casos: ver coste y latencia de todas las llamadas a modelos de tu aplicación; versionar prompts y enrutar entre proveedores con reintentos.
- **Requisitos:** nivel 2: preparación media; TypeScript, Dockerfile, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/Helicone/helicone.git` — fuente: https://github.com/Helicone/helicone/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Helicone con su Docker Compose, cambia la URL base de un cliente OpenAI a la pasarela y haz una petición. Éxito: La petición aparece en el panel con coste, tokens y latencia.
- **Combina con:** `litellm` [23/serving], `langchain` [3/py], `open-webui` [8/chats]
- **Alternativas:** `langfuse`, `opik`, `mlflow`, `phoenix`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): langfuse. Al usar la pasarela, las peticiones pasan por Helicone: valora la privacidad.

### ccusage (`ccusage`)

- **Repo:** https://github.com/ccusage/ccusage · MIT · nivel 2 · —/100
- **Qué es:** Una utilidad de terminal para medir el uso registrado por asistentes de programación.
- **Cuándo elegirlo:** Casos: Identificar el día con más tokens en Claude Code.; Comparar sesiones registradas por Codex y Antigravity sin confundir la estimación con cargos del plan.
- **Requisitos:** nivel 2: preparación media; Rust, package.json; API de IA: no; Node.js y npm compatibles con la versión que elijas, u otro ejecutor indicado en la guía.; Registros locales de al menos un cliente compatible; el modo offline requiere precios disponibles en caché..
- **Instalación (documentada en la fuente; no ejecutada):** `npx ccusage@latest` — fuente: https://ccusage.com/guide/installation
- **Primera prueba propuesta (no ejecutada):** Usa la ruta oficial de instalación, abre el informe diario de un cliente con actividad previa y fíjate en el periodo. Éxito: Aparece una tabla de tokens por día para ese cliente; la cifra de coste es una estimación.
- **Combina con:** `claude-code` [20/terminal]
- **Riesgos y avisos:** Puede leer registros de sesión. Usa un perfil de prueba para una primera revisión, un paquete de versión identificada y no publiques los registros.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-23.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Operar, evaluar y medir modelos de IA», lee `docs/alexandria/categoria-23.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-23.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
