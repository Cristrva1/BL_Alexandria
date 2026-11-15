# 23. Operar, evaluar y medir modelos de IA — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `backdoor`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=— · tags=serving,ai,anthropic,claude,claude-code,deepseek,llm,ollama

**Qué es:** Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code. Traduce solicitudes y gestiona la configuración de proveedores como servicios compatibles u Ollama.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ajsai47/backdoor

**Instalación** [?]: `Seguir la instalación original: https://github.com/ajsai47/backdoor/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar cómo conectar otros modelos al harness de Claude Code
**Evita si:** el coste operativo supera el volumen de uso del proyecto

## `claude-code-router`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=serving,server,typescript

**Qué es:** Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local.
**Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El agente o la pasarela necesita un proveedor. Comprueba en su configuración la ruta de sesión, API o modelo elegida.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. El código de la aplicación no incluye el consumo de su proveedor. Comprueba plan, cuotas, infraestructura y servicios conectados.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/musistudio/claude-code-router

**Instalación** [?]: `Seguir la instalación original: https://github.com/musistudio/claude-code-router/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `claude-code-usage-monitor`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=observabilidad,app,python

**Qué es:** Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor

**Instalación** [?]: `Seguir la instalación original: https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `deepeval`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai · tags=evaluation,python

**Qué es:** Escribe pruebas para tus apps de LLM con métricas como fidelidad, relevancia o alucinación, e intégralas en tu CI.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/confident-ai/deepeval

**Instalación** [+]: `pip install -U deepeval`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres tests de LLM en Python como pytest
**Evita si:** prefieres configurar en YAML y comparar modelos; mira `promptfoo`
**Combina con:** `langfuse`
**Alternativas (elige una):** `ragas`, `promptfoo`

## `guardrails`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=security,chatbot,python

**Qué es:** Controla de qué puede hablar tu bot, bloquea jailbreaks y valida entradas y salidas con reglas en el lenguaje Colang.
**Stack:** Python, Colang
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/NVIDIA-NeMo/Guardrails

**Instalación** [?]: `Seguir la instalación original: https://github.com/NVIDIA-NeMo/Guardrails/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas políticas de seguridad en un chatbot
**Evita si:** solo quieres probar vulnerabilidades; mira `promptfoo`
**Combina con:** `langchain`

## `headroom`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=automation,llmops,python

**Qué es:** Resuelve el dolor habitual de los agentes: quedarse sin ventana de contexto a mitad de una tarea larga.
**Stack:** Python/TypeScript
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/headroomlabs-ai/headroom

**Instalación** [?]: `Seguir la instalación original: https://github.com/headroomlabs-ai/headroom/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** te quedas sin contexto en sesiones largas
**Evita si:** tus prompts ya caben holgados o la pérdida de detalle por resumen es inaceptable
**Combina con:** `context-engineering`, `codegraph`
**Alternativas (elige una):** `rtk`

## `langfuse`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,observability,typescript,docker

**Qué es:** Resuelve la opacidad: ves qué prompt, qué modelo, qué coste y qué salida tuvo cada paso de tu pipeline.
**Stack:** TypeScript, Docker, PostgreSQL, self-host/cloud
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/langfuse/langfuse

**Instalación** [?]: `Seguir la instalación original: https://github.com/langfuse/langfuse/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** operas agentes en serio y necesitas trazas/costes/eval
**Evita si:** haces prototipos triviales o no quieres operar el backend
**Combina con:** `langchain`, `litellm`, `ag2`
**Alternativas (elige una):** `phoenix`, `opik`, `mlflow`

## `litellm`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=inference,llmops,python,docker

**Qué es:** Resuelve el lock-in: cambias de proveedor o añades fallback sin reescribir el código de tu app.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/BerriAI/litellm

**Instalación** [?]: `Seguir la instalación original: https://github.com/BerriAI/litellm/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas con múltiples modelos o quieres fallback/control de costos
**Evita si:** usas un único proveedor fijo y no necesitas abstracción
**Combina con:** `langchain`, `langfuse`, `llm-council`

## `loguru`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=observability,evaluation,python

**Qué es:** Resuelve la fricción del módulo `logging` stdlib, que exige boilerplate para algo tan básico como imprimir logs legibles.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Delgan/loguru

**Instalación** [+]: `pip install loguru`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres logging fácil y legible en Python sin pelear con stdlib
**Evita si:** ya usas el stdlib `logging` configurado o tienes un stack de observabilidad corporativo
**Combina con:** `litellm`

## `mlflow`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=observability,training,evaluation,python

**Qué es:** Registra experimentos, versiona modelos y, para LLM, ofrece trazas, evaluación y gestión de prompts.
**Stack:** Python, React
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mlflow/mlflow

**Instalación** [?]: `Seguir la instalación original: https://github.com/mlflow/mlflow/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu equipo hace ML clásico y LLM y quiere una sola plataforma
**Evita si:** solo trazas LLM y quieres algo más ligero; mira `langfuse`
**Combina con:** `transformers`, `dspy`
**Alternativas (elige una):** `langfuse`

## `omniroute`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=local · tags=serving,server,typescript

**Qué es:** Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso.
**Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/cheaper-inference/OmniRoute

**Instalación** [?]: `Seguir la instalación original: https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.54/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `opik`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=observability,evaluation,python

**Qué es:** Traza llamadas, ejecuta evaluaciones automáticas y monitorea producción con paneles. Incluye optimizador de prompts.
**Stack:** Python, Java, TypeScript, ClickHouse
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/comet-ml/opik

**Instalación** [+]: `pip install opik`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres observabilidad y evaluación en un solo producto abierto
**Evita si:** prefieres la opción más extendida; mira `langfuse`
**Combina con:** `langgraph`
**Alternativas (elige una):** `langfuse`, `phoenix`

## `phoenix`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=observability,evaluation,python

**Qué es:** Visualiza trazas de agentes y RAG, ejecuta evaluaciones y gestiona datasets y experimentos. Corre en local o en tu servidor.
**Stack:** Python, TypeScript, OpenTelemetry
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Arize-ai/phoenix

**Instalación** [+]: `pip install arize-phoenix`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres observabilidad basada en OpenTelemetry
**Evita si:** buscas la plataforma más usada; mira `langfuse`
**Combina con:** `llama-index`, `langgraph`
**Alternativas (elige una):** `langfuse`, `opik`

## `promptfoo`
role=app · exec=local · setup=easy · mcp=False · prov=openai,anthropic,google,local · tags=evaluation,security,typescript

**Qué es:** Defines casos de prueba en YAML y comparas salidas de varios modelos con aserciones. También escanea vulnerabilidades como inyección de prompts.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/promptfoo/promptfoo

**Instalación** [?]: `Seguir la instalación original: https://github.com/promptfoo/promptfoo/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres pruebas automáticas de prompts y seguridad
**Evita si:** necesitas observabilidad en producción; mira `langfuse`
**Combina con:** `langfuse`, `litellm`
**Alternativas (elige una):** `deepeval`, `ragas`, `dspy`

## `ragas`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai · tags=evaluation,rag,python

**Qué es:** Mide fidelidad, relevancia del contexto y calidad de respuestas, y genera conjuntos de prueba a partir de tus documentos.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/vibrantlabsai/ragas

**Instalación** [+]: `pip install ragas`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** evalúas un sistema RAG
**Evita si:** necesitas red teaming de seguridad; mira `promptfoo`
**Combina con:** `llama-index`, `langfuse`
**Alternativas (elige una):** `deepeval`, `promptfoo`

## `rtk`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=tokens,agentic-coding,ai-coding,anthropic,claude-code,cli,command-line-tool,cost-reduction

**Qué es:** Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. Resume resultados de pruebas, diffs y logs antes de entregarlos al agente y registra el ahorro observado.
**Stack:** Rust, Cargo
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/rtk-ai/rtk

**Instalación** [+]: `winget install rtk-ai.rtk`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** tu agente consume demasiado contexto leyendo salidas extensas de terminal
**Evita si:** el coste operativo supera el volumen de uso del proyecto
**Alternativas (elige una):** `headroom`

## `sglang`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=inference,python

**Qué es:** Compite con vLLM en velocidad, con caché de prefijos RadixAttention y buen soporte de salidas estructuradas. Muy usado para modelos grandes como DeepSeek.
**Stack:** Python, CUDA
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/sgl-project/sglang

**Instalación** [?]: `Seguir la instalación original: https://github.com/sgl-project/sglang/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas el máximo rendimiento en servicio de LLM
**Evita si:** quieres la opción más documentada; mira `vllm`
**Combina con:** `litellm`
**Alternativas (elige una):** `vllm`

## `tensorrt-llm`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=serving,blackwell,cuda,llm-serving,moe,pytorch,python

**Qué es:** Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes especializados. Transforma modelos compatibles y los ejecuta con optimizaciones de memoria, precisión y paralelismo.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA/TensorRT-LLM

**Instalación** [?]: `Seguir la instalación original: https://github.com/NVIDIA/TensorRT-LLM/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** despliegas LLM en GPU NVIDIA y necesitas optimizar la inferencia
**Evita si:** el coste operativo supera el volumen de uso del proyecto

## `vllm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=inference,python

**Qué es:** Sirve modelos abiertos a muchos usuarios con una API compatible con OpenAI, gracias a PagedAttention y batching continuo.
**Stack:** Python, CUDA, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/vllm-project/vllm

**Instalación** [+]: `pip install vllm`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas servir LLM abiertos a muchos usuarios en GPU
**Evita si:** solo los usas tú en un portátil; mira `ollama`
**Combina con:** `litellm`, `open-webui`
**Alternativas (elige una):** `sglang`
