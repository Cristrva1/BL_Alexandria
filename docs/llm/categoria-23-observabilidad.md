# Alexandría para agentes · Observabilidad, evaluación y guardrails

Categoría 23 «Operar, evaluar y medir modelos de IA» › subcategoría `observabilidad`. 14 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=23&sub=observabilidad · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `langfuse` | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM… | 2 Intermedio | 79 | MIT + licencia Enterprise (ee/) (open-core) | recomendado |
| `promptfoo` | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de… | 1 Básico | 79 | MIT (OSI permisiva) | recomendado |
| `opik` | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y… | 2 Intermedio | 75 | Apache-2.0 (OSI permisiva) | alternativa |
| `mlflow` | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM… | 1 Básico | 70 | Apache-2.0 (OSI permisiva) | alternativa |
| `deepeval` | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. | 2 Intermedio | 63 | Apache-2.0 (OSI permisiva) | alternativa |
| `loguru` | Librería de logging para Python centrada en la simplicidad ("logging that… | 2 Intermedio | 63 | MIT (OSI permisiva) | sin grupo |
| `openllmetry` | Instrumentación abierta basada en OpenTelemetry para aplicaciones de LLM: traza… | 2 Intermedio | 63 | Apache-2.0 (OSI permisiva) | sin grupo |
| `lm-eval-harness` | Arnés estándar de EleutherAI para evaluar modelos de lenguaje en cientos de… | 2 Intermedio | 57 | MIT (OSI permisiva) | sin grupo |
| `claude-code-usage-monitor` | Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a… | 2 Intermedio | 53 | MIT (OSI permisiva) | sin grupo |
| `guardrails` | Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales… | 2 Intermedio | 53 | Apache-2.0 (OSI permisiva) | sin grupo |
| `phoenix` | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM… | 1 Básico | 53 | Elastic-2.0 (source-available) | alternativa |
| `ragas` | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos… | 2 Intermedio | 51 | Apache-2.0 (OSI permisiva) | alternativa |
| `helicone` | Pasarela de IA y plataforma de observabilidad de LLM abierta: registra… | 2 Intermedio | 50 | Apache-2.0 (OSI permisiva) | alternativa |
| `ccusage` | Resume los tokens y estima el coste de tus sesiones de asistentes a partir de… | 2 Intermedio | — | MIT | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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

Guarda este archivo como `docs/alexandria/categoria-23-observabilidad.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Observabilidad, evaluación y guardrails», lee `docs/alexandria/categoria-23-observabilidad.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-23-observabilidad.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
