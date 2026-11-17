# Alexandría para agentes · Serving y gateways de LLM

Categoría 23 «Operar, evaluar y medir modelos de IA» › subcategoría `serving`. 11 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=23&sub=serving · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `vllm` | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de… | 3 Avanzado | 78 | Apache-2.0 (OSI permisiva) | recomendado |
| `litellm` | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola… | 2 Intermedio | 77 | MIT + licencia Enterprise (litellm/enterprise/) (open-core) | recomendado |
| `omniroute` | Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar… | 3 Avanzado | 76 | MIT (OSI permisiva) | alternativa |
| `tensorrt-llm` | Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de… | 3 Avanzado | 75 | Apache-2.0 (OSI permisiva) | sin grupo |
| `ray` | Motor de cómputo distribuido para IA: escala Python de un portátil a un… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `sglang` | Framework de servicio de alto rendimiento para LLM y modelos multimodales. | 3 Avanzado | 67 | Apache-2.0 (OSI permisiva) | alternativa |
| `xinference` | Plataforma abierta de inferencia para modelos de lenguaje, visión, embeddings… | 3 Avanzado | 66 | Apache-2.0 (OSI permisiva) | sin grupo |
| `gpustack` | Gestor de clústeres de GPU para servir modelos de IA: configura vLLM, SGLang o… | 3 Avanzado | 62 | Apache-2.0 (OSI permisiva) | sin grupo |
| `bentoml` | Framework Python para convertir modelos y pipelines de IA en APIs de… | 2 Intermedio | 57 | Apache-2.0 (OSI permisiva) | sin grupo |
| `claude-code-router` | Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes… | 3 Avanzado | 57 | MIT (OSI permisiva) | alternativa |
| `backdoor` | Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo… | 2 Intermedio | 36 | MIT (OSI permisiva) | alternativa |

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-23-serving.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Serving y gateways de LLM», lee `docs/alexandria/categoria-23-serving.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-23-serving.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
