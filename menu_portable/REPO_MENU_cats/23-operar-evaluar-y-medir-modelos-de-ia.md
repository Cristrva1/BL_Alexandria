# 23. Operar, evaluar y medir modelos de IA — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `backdoor`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=— · tags=serving,ai,anthropic,claude,claude-code,deepseek,llm,ollama

**Qué es:** Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code.
**Stack:** Sistema compatible; Claude Code; proveedor u Ollama; carpeta de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Modelo local o API del proveedor según elección; no aporta una suscripción ni créditos de Anthropic
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es un adaptador independiente; afirmar privacidad local requiere revisar también búsquedas, telemetría y otras herramientas y no solo el endpoint del modelo
- Coste: El coste depende del proveedor o la ruta. Modelo local o API del proveedor según elección; no aporta una suscripción ni créditos de Anthropic
- Equipo: Preparación según la ruta elegida. Sistema compatible; Claude Code; proveedor u Ollama; carpeta de prueba
**Repo:** https://github.com/ajsai47/backdoor

**Instalación** [+]:

```
git clone https://github.com/ajsai47/backdoor
cd backdoor
./backdoor   # animated setup wizard — picks your provider, writes your config, launches Claude Code
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un backend local con Claude Code; Comparar proveedores compatibles
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Revisa la configuración que propone el asistente y solicita una explicación corta sin herramientas externas
**Qué comprobar:** Puedes identificar el proveedor detrás del proxy
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ollama`, `vllm`
**Alternativas (elige una):** `omniroute`, `claude-code-router`, `litellm`

## `bentoml`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=serving,python,ml,docker

**Qué es:** Framework Python para convertir modelos y pipelines de IA en APIs de producción, con empaquetado en imágenes Docker y despliegue reproducible.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/bentoml/BentoML

**Instalación** [+]:

```
pip install -U bentoml
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: publicar un modelo de Transformers como API REST; empaquetar un LLM servido con vLLM en una imagen desplegable
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install -U bentoml`, define el servicio de ejemplo del README y arráncalo con `bentoml serve`.
**Qué comprobar:** La API responde en localhost con el resultado del modelo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `transformers`, `pytorch`

## `ccusage`
role=app · exec=local · setup=medium · mcp=True · prov=— · tags=consumo,tokens,costos

**Qué es:** Resume los tokens y estima el coste de tus sesiones de asistentes a partir de los registros locales de sus terminales.
**Stack:** Rust, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El informe usa registros existentes y no llama a un LLM. Puede consultar precios si no usas el modo offline.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. El paquete es MIT. La estimación por tarifas no representa la factura, el saldo ni los límites de tu plan.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ccusage/ccusage

**Instalación** [+]:

```
npx ccusage@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Identificar el día con más tokens en Claude Code.; Comparar sesiones registradas por Codex y Antigravity sin confundir la estimación con cargos del plan.
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Usa la ruta oficial de instalación, abre el informe diario de un cliente con actividad previa y fíjate en el periodo.
**Qué comprobar:** Aparece una tabla de tokens por día para ese cliente; la cifra de coste es una estimación.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`

## `claude-code-router`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=serving,server,typescript

**Qué es:** Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local.
**Stack:** Node 22+ o app; proveedor y credenciales; agente de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El gateway usa las cuentas y claves elegidas; una interfaz local no elimina los costes remotos
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Documenta perfiles para Claude Code y Codex; llamar local al gateway no confirma que el modelo se ejecute localmente ni garantiza todas las capacidades de cada agente
- Coste: El coste depende del proveedor o la ruta. El gateway usa las cuentas y claves elegidas; una interfaz local no elimina los costes remotos
- Equipo: Preparación según la ruta elegida. Node 22+ o app; proveedor y credenciales; agente de prueba
**Repo:** https://github.com/musistudio/claude-code-router

**Instalación** [+]:

```
npm install -g @musistudio/claude-code-router
ccr ui
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar proveedores desde Claude Code; Organizar perfiles para Codex
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade un proveedor, inicia el servidor local y aplica un perfil a una sesión de prueba
**Qué comprobar:** Puedes identificar endpoint, modelo y ruta efectiva
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`, `claude-code-hooks-mastery`
**Alternativas (elige una):** `omniroute`, `backdoor`, `litellm`

## `claude-code-usage-monitor`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=observabilidad,app,python

**Qué es:** Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible.
**Stack:** uv o Python compatible; datos de uso de Claude Code
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El monitor no necesita API de IA para leer datos; no amplía límites ni incluye el plan de Claude
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Las previsiones son estimaciones y las fuentes tienen distinta cobertura; es una integración de lectura de Claude Code y no un modelo alternativo
- Coste: Sin pago a un modelo en la ruta básica. El monitor no necesita API de IA para leer datos; no amplía límites ni incluye el plan de Claude
- Equipo: Preparación según la ruta elegida. uv o Python compatible; datos de uso de Claude Code
**Repo:** https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor

**Instalación** [+]:

```
# Install directly from PyPI with uv (easiest)
uv tool install claude-monitor

# Run from anywhere
claude-monitor  # or cmonitor, ccmonitor for short
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar el uso de una sesión; Estudiar alertas y proyecciones de cuota
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre el monitor y compara una cifra con su etiqueta de procedencia y fecha
**Qué comprobar:** Puedes distinguir consumo observado, estado oficial y previsión
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `rtk`, `headroom`, `claude-token-efficient`

## `deepeval`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai · tags=evaluation,python

**Qué es:** Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas.
**Stack:** Python; casos con respuestas conocidas; modelo evaluador y embeddings si se usan
**Acceso y costes:**
- API de IA: API de IA opcional. Muchas métricas usan un juez LLM por consumo o uno local Ollama; Confident AI y embeddings tienen configuración propia
- Claude Code: Depende del recurso o la configuración
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: Modelos locales documentados. El MCP mencionado pertenece al servicio compañero Confident AI; no todas las métricas necesitan LLM y un juez pequeño puede fallar al seguir el esquema
- Coste: El coste depende del proveedor o la ruta. Muchas métricas usan un juez LLM por consumo o uno local Ollama; Confident AI y embeddings tienen configuración propia
- Equipo: Preparación según la ruta elegida. Python; casos con respuestas conocidas; modelo evaluador y embeddings si se usan
**Repo:** https://github.com/confident-ai/deepeval

**Instalación** [+]:

```
pip install -U deepeval
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Detectar regresiones de un chatbot; Probar relevancia de respuestas RAG
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Evalúa tres respuestas ficticias con un criterio explícito y revisa una puntuación manualmente
**Qué comprobar:** Puedes relacionar el resultado con el caso y el juez seleccionado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langchain`, `llama-index`, `mlflow`, `langfuse`
**Alternativas (elige una):** `ragas`, `promptfoo`

## `gptcache`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Reutiliza respuestas de consultas parecidas a un modelo mediante una caché semántica con reglas de comparación configurables.
**Stack:** Python, Makefile, requirements.txt, setup.py
**Acceso y costes:**
- API de IA: API de IA opcional. La ruta local o básica no necesita una clave de LLM alojado. Las modalidades remotas se configuran aparte.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La guía del proyecto documenta componentes locales. Confirma qué parte corre en tu equipo y la licencia de los modelos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume equipo; proveedores, servicios alojados y bases remotas pueden cobrar.
- Equipo: Equipo normal; revisar dependencias. Python y un componente de embeddings y almacenamiento compatible; entorno de prueba con consultas ficticias.
**Repo:** https://github.com/zilliztech/GPTCache

**Instalación** [?]:

```
Seguir la instalación original: https://gptcache.readthedocs.io
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Evitar recalcular preguntas repetidas en un prototipo.; Comparar falsos aciertos de caché con dos preguntas casi iguales.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Configura el ejemplo en un entorno aislado y manda dos consultas de ejemplo similares.
**Qué comprobar:** Puedes observar cuándo se reutiliza una respuesta y cuándo se vuelve a calcular.
Revisión documental individual; instalación no ejecutada por Alexandría.

## `gpustack`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=serving,python,gpu,self-hosted

**Qué es:** Gestor de clústeres de GPU para servir modelos de IA: configura vLLM, SGLang o TensorRT-LLM, expone APIs compatibles con OpenAI y aprovisiona instancias GPU.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/gpustack/gpustack

**Instalación** [+]:

```
sudo docker run -d --name gpustack --restart unless-stopped -p 80:80 --volume gpustack-data:/var/lib/gpustack gpustack/gpustack
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: servir varios modelos en las GPU de tu laboratorio con una sola consola; dar a tu equipo claves de API compatibles con OpenAI sobre modelos propios
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Sigue la guía de instalación con Docker en un nodo con GPU NVIDIA, despliega un modelo pequeño y prueba la API con curl.
**Qué comprobar:** El modelo responde por el endpoint compatible con OpenAI.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `sglang`, `tensorrt-llm`

## `guardrails`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=security,chatbot,python

**Qué es:** Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM.
**Stack:** Python; app conversacional; configuración Colang; modelo según rails
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Los modelos y servicios usados por las reglas pueden generar consumo; el toolkit Apache no los incluye
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. NeMo Guardrails no garantiza seguridad total ni adecuación a todo sector; develop es desarrollo y la versión publicada debe elegirse de forma explícita
- Coste: El coste depende del proveedor o la ruta. Los modelos y servicios usados por las reglas pueden generar consumo; el toolkit Apache no los incluye
- Equipo: Preparación según la ruta elegida. Python; app conversacional; configuración Colang; modelo según rails
**Repo:** https://github.com/NVIDIA-NeMo/Guardrails

**Instalación** [+]:

```
pip install nemoguardrails
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Guiar un asistente de soporte; Evaluar controles de una app propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Define un flujo de tema permitido y prueba una pregunta dentro y otra fuera de ese tema
**Qué comprobar:** Puedes comprobar la regla aplicada y registrar sus límites
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langchain`, `promptfoo`, `vllm`

## `headroom`
role=library · exec=hybrid · setup=easy · mcp=True · prov=— · tags=automation,llmops,python

**Qué es:** Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial.
**Stack:** Python compatible; contenido de prueba; agente o cliente MCP si lo conectas
**Acceso y costes:**
- API de IA: API de IA opcional. La compresión básica no pide clave ni descargar modelo; el agente y funciones opcionales pueden usar otros recursos
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Documenta wrap para Claude y Codex y MCP para cualquier cliente compatible; los ahorros de benchmarks no garantizan iguales respuestas en toda tarea
- Coste: El coste depende del proveedor o la ruta. La compresión básica no pide clave ni descargar modelo; el agente y funciones opcionales pueden usar otros recursos
- Equipo: Preparación según la ruta elegida. Python compatible; contenido de prueba; agente o cliente MCP si lo conectas
**Repo:** https://github.com/headroomlabs-ai/headroom

**Instalación** [+]:

```
pip install headroom-ai
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir salidas extensas de herramientas; Comparar una sesión con y sin compresión
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Comprime una salida JSON pequeña y compara el resultado con el original antes de envolver un agente
**Qué comprobar:** Puedes identificar qué se conservó y recuperar el original cuando corresponda
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `litellm`, `context-engineering`, `codegraph`, `claude-code-usage-monitor`, `mimo-code`
**Alternativas (elige una):** `rtk`

## `helicone`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=observability,typescript,llm,self-hosted

**Qué es:** Pasarela de IA y plataforma de observabilidad de LLM abierta: registra peticiones, costes y latencias, gestiona prompts y enruta a más de 100 modelos.
**Stack:** TypeScript, Dockerfile, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Helicone/helicone

**Instalación** [+]:

```
git clone https://github.com/Helicone/helicone.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: ver coste y latencia de todas las llamadas a modelos de tu aplicación; versionar prompts y enrutar entre proveedores con reintentos
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Despliega Helicone con su Docker Compose, cambia la URL base de un cliente OpenAI a la pasarela y haz una petición.
**Qué comprobar:** La petición aparece en el panel con coste, tokens y latencia.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `langchain`, `open-webui`
**Alternativas (elige una):** `langfuse`

## `langfuse`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,observability,typescript,docker

**Qué es:** Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente.
**Stack:** Docker o servicio Cloud; app de prueba; SDK o instrumentación
**Acceso y costes:**
- API de IA: API de IA opcional. Self-host requiere infraestructura; Cloud, LLM-as-judge y modelos tienen costes separados; integra trazas de Ollama
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. El MCP documentado en el README consulta documentación y no equivale a acceso automático a tus trazas; el núcleo MIT excluye carpetas ee
- Coste: El coste depende del proveedor o la ruta. Self-host requiere infraestructura; Cloud, LLM-as-judge y modelos tienen costes separados; integra trazas de Ollama
- Equipo: Preparación según la ruta elegida. Docker o servicio Cloud; app de prueba; SDK o instrumentación
**Repo:** https://github.com/langfuse/langfuse

**Instalación** [+]:

```
# Get a copy of the latest Langfuse repository
  git clone --depth=1 https://github.com/langfuse/langfuse.git
  cd langfuse

  # Run the langfuse docker compose
  docker compose up
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar un asistente; Comparar versiones de un prompt
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Registra una llamada de prueba y abre su traza para revisar entrada, salida y duración
**Qué comprobar:** Puedes rastrear una respuesta hasta la llamada que la produjo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `langchain`, `open-webui`, `ragas`
**Alternativas (elige una):** `phoenix`, `opik`, `mlflow`, `helicone`

## `litellm`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=inference,llmops,python,docker

**Qué es:** Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI.
**Stack:** Python y uv; proveedor o endpoint local; presupuesto de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Las llamadas siguen usando claves, cuotas y precios de cada proveedor; Ollama y LM Studio permiten rutas locales
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Documenta harnesses de Claude Code y Codex en el SDK; pasar por el gateway no incorpora suscripciones ni elimina diferencias entre protocolos
- Coste: El coste depende del proveedor o la ruta. Las llamadas siguen usando claves, cuotas y precios de cada proveedor; Ollama y LM Studio permiten rutas locales
- Equipo: Preparación según la ruta elegida. Python y uv; proveedor o endpoint local; presupuesto de prueba
**Repo:** https://github.com/BerriAI/litellm

**Instalación** [+]:

```
uv add litellm
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar llamadas a varios modelos; Enrutar un agente por un gateway propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un único proveedor y envía una petición breve antes de activar fallback y balanceo
**Qué comprobar:** Puedes identificar el proveedor real y su consumo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `open-webui`, `langfuse`, `claude-code`
**Alternativas (elige una):** `omniroute`, `claude-code-router`, `backdoor`

## `llmlingua`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Acorta texto de entrada para modelos de lenguaje y permite medir cuánto contexto conservas antes de enviar el prompt.
**Stack:** Python, Makefile, pyproject.toml, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La prueba con los modelos locales indicados no necesita contratar una API de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La inferencia usa pesos compatibles en el equipo; comprueba memoria, acelerador y licencia.
- Coste: Sin pago a un modelo en la ruta básica. La inferencia local usa hardware, energía y almacenamiento. Una GPU alquilada y una licencia de pesos pueden tener costes aparte.
- Equipo: Memoria y GPU según el modelo. Python, PyTorch y un modelo de compresión compatible con el hardware.
**Repo:** https://github.com/microsoft/LLMLingua

**Instalación** [?]:

```
Seguir la instalación original: https://llmlingua.com/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar un prompt largo con su versión comprimida.; Medir tokens ahorrados y revisar si mantuvo una restricción importante.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Comprime un texto público breve con un modelo local pequeño del proyecto.
**Qué comprobar:** Obtienes dos textos y puedes comparar tamaño, instrucciones conservadas y pérdidas.
Revisión documental individual; instalación no ejecutada por Alexandría.

## `lm-eval-harness`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=evaluation,python,llm,benchmark

**Qué es:** Arnés estándar de EleutherAI para evaluar modelos de lenguaje en cientos de benchmarks académicos con backends Hugging Face, vLLM, SGLang o APIs.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/EleutherAI/lm-evaluation-harness

**Instalación** [+]:

```
pip install "lm_eval[hf]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: comparar un modelo ajustado con su base en MMLU, HellaSwag o GSM8K; reproducir resultados de tablas de clasificación con la misma configuración
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install "lm_eval[hf]"` y evalúa un modelo pequeño de Hugging Face en una tarea ligera con `lm_eval --model hf --tasks ...`.
**Qué comprobar:** Obtienes una tabla con la métrica de la tarea y su error estándar.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `sglang`, `transformers`, `torchtune`, `gemma`

## `loguru`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=observability,evaluation,python

**Qué es:** Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa.
**Stack:** Python; script de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa modelos ni API; almacenamiento y plataforma de logs externa se presupuestan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una biblioteca de logging general y no un sistema de observabilidad LLM completo; evita registrar secretos o datos que no necesites
- Coste: Sin pago a un modelo en la ruta básica. No usa modelos ni API; almacenamiento y plataforma de logs externa se presupuestan aparte
- Equipo: Preparación según la ruta elegida. Python; script de prueba
**Repo:** https://github.com/Delgan/loguru

**Instalación** [+]:

```
pip install loguru
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar una automatización; Añadir logs legibles a una app
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Registra un mensaje y una excepción ficticia en un script pequeño
**Qué comprobar:** Puedes distinguir nivel, fecha y detalle del error
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `langfuse`, `pydantic-ai`

## `mlflow`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=observability,training,evaluation,python

**Qué es:** Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro.
**Stack:** uv o Python; app y datos ficticios; agente opcional para instrumentar
**Acceso y costes:**
- API de IA: API de IA opcional. Seguimiento básico sin API de IA; evaluadores, modelos y alojamiento gestionado pueden generar costes
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El wizard documenta Claude Code y Codex para añadir instrumentación; no es una autorización para cambiar automáticamente proyectos reales
- Coste: El coste depende del proveedor o la ruta. Seguimiento básico sin API de IA; evaluadores, modelos y alojamiento gestionado pueden generar costes
- Equipo: Preparación según la ruta elegida. uv o Python; app y datos ficticios; agente opcional para instrumentar
**Repo:** https://github.com/mlflow/mlflow

**Instalación** [+]:

```
uvx mlflow server
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Registrar experimentos de ML; Añadir trazas a una app de IA
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inicia el servidor de prueba y registra una ejecución pequeña con parámetros y resultado
**Qué comprobar:** Puedes abrir la ejecución y comparar sus datos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `dspy`, `transformers`, `deepeval`, `ragas`, `qlib`, `airflow`
**Alternativas (elige una):** `langfuse`

## `omniroute`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=local · tags=serving,server,typescript

**Qué es:** Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso.
**Stack:** Node o distribución compatible; cuentas de proveedores o backend local; agente opcional
**Acceso y costes:**
- API de IA: API de IA opcional. Las cuotas gratuitas agregadas son estimaciones de servicios externos y no créditos concedidos por OmniRoute; modelos locales tienen requisitos propios
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. Documenta Claude Code, Codex y un adaptador Antigravity; OAuth y automatización de terceros dependen de permisos y términos de cada proveedor
- Coste: El coste depende del proveedor o la ruta. Las cuotas gratuitas agregadas son estimaciones de servicios externos y no créditos concedidos por OmniRoute; modelos locales tienen requisitos propios
- Equipo: Preparación según la ruta elegida. Node o distribución compatible; cuentas de proveedores o backend local; agente opcional
**Repo:** https://github.com/cheaper-inference/OmniRoute

**Instalación** [+]:

```
npm install -g omniroute
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Centralizar proveedores de un agente; Comparar rutas y límites de consumo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta un proveedor autorizado y revisa una petición breve antes de activar rotación, fallback o compresión
**Qué comprobar:** Puedes identificar qué cuenta y modelo atendieron la petición
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `cline`, `ollama`
**Alternativas (elige una):** `claude-code-router`, `backdoor`, `litellm`

## `openllmetry`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=observability,python,llm,opentelemetry

**Qué es:** Instrumentación abierta basada en OpenTelemetry para aplicaciones de LLM: traza llamadas a modelos, bases vectoriales y frameworks hacia tu backend de observabilidad.
**Stack:** Python, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/traceloop/openllmetry

**Instalación** [+]:

```
pip install traceloop-sdk
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: trazar llamadas a OpenAI, LangChain o Ollama en Grafana o Datadog; añadir observabilidad de LLM a una pila OpenTelemetry existente
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install traceloop-sdk`, inicializa el SDK en un script con una llamada a un modelo y envía las trazas a la consola o a tu backend.
**Qué comprobar:** Ves las trazas con prompts, tokens y latencias.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `grafana`, `langchain`, `llama-index`, `ollama`

## `opik`
role=platform · exec=local · setup=medium · mcp=True · prov=— · tags=observability,evaluation,python

**Qué es:** Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes.
**Stack:** Python; Cloud o instancia propia; app y datos de prueba; uv para MCP
**Acceso y costes:**
- API de IA: API de IA opcional. Plataforma Apache autoalojable o Cloud; los modelos evaluadores y la infraestructura tienen costes propios
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Documenta configuración MCP para Claude Code, Codex y otros clientes; puede registrar Ollama, pero no sirve el modelo por sí mismo
- Coste: El coste depende del proveedor o la ruta. Plataforma Apache autoalojable o Cloud; los modelos evaluadores y la infraestructura tienen costes propios
- Equipo: Preparación según la ruta elegida. Python; Cloud o instancia propia; app y datos de prueba; uv para MCP
**Repo:** https://github.com/comet-ml/opik

**Instalación** [+]:

```
pip install opik
opik configure
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar una cadena RAG; Revisar fallos con un agente de código
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Registra una traza y consúltala desde el panel o MCP con acceso de prueba
**Qué comprobar:** Puedes localizar entrada, salida y evaluación de esa ejecución
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `litellm`, `ragas`, `dspy`
**Alternativas (elige una):** `langfuse`, `phoenix`

## `phoenix`
role=platform · exec=local · setup=easy · mcp=True · prov=— · tags=observability,evaluation,python

**Qué es:** Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry.
**Stack:** Python; app de prueba; instrumentación o cliente MCP
**Acceso y costes:**
- API de IA: API de IA opcional. Autoalojamiento, cómputo y evaluadores se costean aparte; puede observar modelos locales Ollama
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. El README declara Elastic License 2.0, por lo que no debe etiquetarse como licencia abierta sin restricciones; ofrece MCP y plugins Claude Code y Codex
- Coste: El coste depende del proveedor o la ruta. Autoalojamiento, cómputo y evaluadores se costean aparte; puede observar modelos locales Ollama
- Equipo: Preparación según la ruta elegida. Python; app de prueba; instrumentación o cliente MCP
**Repo:** https://github.com/Arize-ai/phoenix

**Instalación** [+]:

```
pip install arize-phoenix
phoenix serve
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar una app con OpenTelemetry; Consultar trazas desde un agente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una traza de muestra y consulta una ejecución antes de conectar una aplicación real
**Qué comprobar:** Puedes identificar spans, latencia y entradas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `llama-index`, `langgraph`, `ollama`, `claude-code`
**Alternativas (elige una):** `langfuse`, `opik`

## `portkey-gateway`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Centraliza llamadas a distintos proveedores de modelos mediante una pasarela con reglas de ruta, presupuestos y registro de solicitudes.
**Stack:** TypeScript, Dockerfile, package.json
**Acceso y costes:**
- API de IA: API de IA necesaria. La primera prueba documentada necesita autenticación de un proveedor o de la pasarela del modelo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Ejecución con modelos locales por confirmar. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Consumo de APIs o servicios. La licencia de código no incluye llamadas a modelos, despliegue ni almacenamiento.
- Equipo: Equipo normal; revisar dependencias. Node.js/npm o un contenedor compatible; para inferencia, un proveedor habilitado y una clave propia de prueba.
**Repo:** https://github.com/Portkey-AI/gateway

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Portkey-AI/gateway/blob/669825cbe89ee51569918b8f78a9db486fd69dd4/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Hacer una llamada pequeña a un solo proveedor y medir latencia.; Comparar dos rutas ante un error simulado sin enviar información privada.
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Instala una versión posterior al mínimo corregido y prueba una llamada con texto ficticio y presupuesto reducido.
**Qué comprobar:** Puedes identificar el proveedor utilizado en la respuesta o el registro de prueba.
Revisión documental individual; instalación no ejecutada por Alexandría.

## `promptfoo`
role=app · exec=local · setup=easy · mcp=False · prov=openai,anthropic,google,local · tags=evaluation,security,typescript

**Qué es:** CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad.
**Stack:** Node; dataset de preguntas; proveedor o Ollama; criterio de evaluación
**Acceso y costes:**
- API de IA: API de IA opcional. CLI MIT; APIs y servicios adicionales tienen costes y Ollama permite modelos locales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Una puntuación depende del dataset, proveedor y evaluador; los tests de seguridad deben dirigirse a sistemas propios o autorizados
- Coste: El coste depende del proveedor o la ruta. CLI MIT; APIs y servicios adicionales tienen costes y Ollama permite modelos locales
- Equipo: Preparación según la ruta elegida. Node; dataset de preguntas; proveedor o Ollama; criterio de evaluación
**Repo:** https://github.com/promptfoo/promptfoo

**Instalación** [+]:

```
npm install -g promptfoo
promptfoo init --example getting-started
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar un prompt de soporte; Probar regresiones de un RAG
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea dos variantes de un prompt y evalúalas con tres casos conocidos
**Qué comprobar:** Puedes comparar respuestas y detectar un fallo concreto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langfuse`, `litellm`, `vllm`
**Alternativas (elige una):** `deepeval`, `ragas`, `dspy`

## `ragas`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai · tags=evaluation,rag,python

**Qué es:** Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos.
**Stack:** Python; dataset de evaluación; modelo y embeddings configurados
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El ejemplo usa OPENAI_API_KEY y métricas que pueden consumir modelos y embeddings; cada adaptación debe presupuestarse
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El ejemplo usa OpenAI y algunas métricas consumen modelos y embeddings; el proveedor y coste dependen de la métrica elegida y deben configurarse explícitamente
- Coste: El coste depende del proveedor o la ruta. El ejemplo usa OPENAI_API_KEY y métricas que pueden consumir modelos y embeddings; cada adaptación debe presupuestarse
- Equipo: Preparación según la ruta elegida. Python; dataset de evaluación; modelo y embeddings configurados
**Repo:** https://github.com/vibrantlabsai/ragas

**Instalación** [+]:

```
pip install ragas
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Medir un RAG con datos controlados; Comparar versiones de una cadena
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Evalúa una respuesta cuyo contexto y referencia conozcas y comprueba qué mide cada métrica
**Qué comprobar:** Puedes distinguir recuperación, relevancia y fidelidad
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `llama-index`, `langfuse`, `langchain`, `opik`
**Alternativas (elige una):** `deepeval`, `promptfoo`

## `ray`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=distributed,python,serving,ml

**Qué es:** Motor de cómputo distribuido para IA: escala Python de un portátil a un clúster, con bibliotecas para datos, entrenamiento, ajuste, RL y serving.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ray-project/ray

**Instalación** [+]:

```
pip install ray
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: paralelizar un procesamiento de datos o entrenamiento en varias máquinas; servir modelos con autoescalado mediante Ray Serve
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install ray` y paraleliza una función con `@ray.remote` en tu equipo.
**Qué comprobar:** Las tareas se ejecutan en paralelo y el panel de Ray muestra su progreso.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `pytorch`, `verl`, `openrlhf`

## `rtk`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=tokens,agentic-coding,ai-coding,anthropic,claude-code,cli,command-line-tool,cost-reduction

**Qué es:** Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código.
**Stack:** Binario para tu sistema; agente y proyecto de prueba; configuración por agente
**Acceso y costes:**
- API de IA: API de IA opcional. La compresión básica no necesita API; pipelines con otros modelos y el servicio Pro tienen costes separados
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Claude y Codex tienen hooks documentados; Antigravity usa un archivo de reglas y no la misma automatización; las cifras de ahorro dependen de la tarea
- Coste: El coste depende del proveedor o la ruta. La compresión básica no necesita API; pipelines con otros modelos y el servicio Pro tienen costes separados
- Equipo: Preparación según la ruta elegida. Binario para tu sistema; agente y proyecto de prueba; configuración por agente
**Repo:** https://github.com/rtk-ai/rtk

**Instalación** [+]:

```
winget install rtk-ai.rtk
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir salida repetitiva de comandos; Estudiar consumo de contexto por tarea
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prueba un comando RTK y compara su salida con la versión sin comprimir antes de activar hooks
**Qué comprobar:** Puedes comprobar datos omitidos y contadores de ahorro
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `gemini-cli`, `claude-code-usage-monitor`, `mimo-code`
**Alternativas (elige una):** `headroom`

## `sglang`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=inference,python

**Qué es:** Framework de servicio de alto rendimiento para LLM y modelos multimodales.
**Stack:** uv; hardware y drivers compatibles; modelo con memoria suficiente
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API de modelo alojado en la ruta propia; cómputo y pesos tienen sus costes y licencias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El comando del README admite prereleases; selecciona una versión apropiada según la documentación de tu hardware; patrocinio a contribuidores no es integración con sus agentes
- Coste: Sin pago a un modelo en la ruta básica. Sin API de modelo alojado en la ruta propia; cómputo y pesos tienen sus costes y licencias
- Equipo: Preparación según la ruta elegida. uv; hardware y drivers compatibles; modelo con memoria suficiente
**Repo:** https://github.com/sgl-project/sglang

**Instalación** [+]:

```
uv pip install --prerelease=allow sglang
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Servir un modelo para una aplicación; Estudiar inferencia multimodal
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue el quickstart y comprueba una petición breve al modelo servido
**Qué comprobar:** Puedes identificar modelo, proceso y respuesta del endpoint
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `open-webui`, `unsloth`, `deepseek-v3`, `kimi-k2-7-code`, `llama-factory`
**Alternativas (elige una):** `vllm`

## `tensorrt-llm`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=serving,blackwell,cuda,llm-serving,moe,pytorch,python

**Qué es:** Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes especializados.
**Stack:** GPU NVIDIA compatible; CUDA y dependencias según versión; modelo soportado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere API de modelo remota; hardware, energía, nube y licencia del modelo son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es infraestructura especializada y no una instalación universal para cualquier portátil o GPU
- Coste: Sin pago a un modelo en la ruta básica. No requiere API de modelo remota; hardware, energía, nube y licencia del modelo son independientes
- Equipo: Preparación según la ruta elegida. GPU NVIDIA compatible; CUDA y dependencias según versión; modelo soportado
**Repo:** https://github.com/NVIDIA/TensorRT-LLM

**Instalación** [+]:

```
docker run --rm -it --ipc=host --gpus all -p 8000:8000 -v "$HOST_MODELS_DIR":/models --name tensorrt_llm nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc25 /bin/bash
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Optimizar inferencia en GPU propia; Estudiar kernels y runtimes de NVIDIA
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Comprueba la matriz de hardware y ejecuta el ejemplo mínimo de inferencia antes de optimizar
**Qué comprobar:** Puedes relacionar motor, modelo y configuración de memoria
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `open-webui`, `transformers`, `deepseek-v3`, `gpustack`

## `toon-format`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=json,tokens,typescript,contexto

**Qué es:** Convierte listas de objetos JSON a un texto con encabezado y filas para experimentar con entradas más compactas para modelos.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Codificar un objeto en el equipo no necesita un modelo. Invocar uno después tiene su propia cuota.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La ruta básica procesa los datos en tu equipo sin un modelo.
- Coste: Sin pago a un modelo en la ruta básica. Código MIT. La tarea de ejemplo se ejecuta con herramientas gratuitas en tu equipo.
- Equipo: Equipo normal; revisar dependencias. Node.js con npm y proyecto que pueda importar módulos ES.
**Repo:** https://github.com/toon-format/toon

**Instalación** [+]:

```
npm install @toon-format/toon
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Representar un inventario ficticio de productos con los mismos tres campos en cada fila.; Preparar una tabla de registros con idéntica estructura para comparar el tamaño con JSON compacto.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Usa encode con dos registros ficticios que compartan campos, siguiendo el ejemplo del README de la versión 4.4.0.
**Qué comprobar:** La salida conserva ambos registros y enumera los campos en el encabezado. Revisa los valores y compárala con el JSON original.
Revisión documental individual; instalación no ejecutada por Alexandría.

## `vllm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=inference,python

**Qué es:** Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU.
**Stack:** uv y Python compatibles; hardware soportado; pesos y memoria del modelo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API de pago para inferencia propia; GPU, alquiler y licencia de pesos son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es un motor de serving y no una app de chat; confirma la matriz de hardware y versión antes de instalar
- Coste: Sin pago a un modelo en la ruta básica. No necesita API de pago para inferencia propia; GPU, alquiler y licencia de pesos son independientes
- Equipo: Preparación según la ruta elegida. uv y Python compatibles; hardware soportado; pesos y memoria del modelo
**Repo:** https://github.com/vllm-project/vllm

**Instalación** [+]:

```
uv pip install vllm
vllm download-kernels  # precompiled kernels for faster startup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Servir un modelo propio; Estudiar rendimiento de inferencia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue el quickstart con un modelo que quepa en tu equipo y solicita una respuesta breve
**Qué comprobar:** Puedes comprobar modelo cargado y endpoint de inferencia
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `open-webui`, `langchain`
**Alternativas (elige una):** `sglang`

## `xinference`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=serving,python,llm,self-hosted

**Qué es:** Plataforma abierta de inferencia para modelos de lenguaje, visión, embeddings, reranking, imagen, audio y vídeo, con API compatible con OpenAI y varios motores.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/xorbitsai/inference

**Instalación** [+]:

```
pip install xinference
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: servir un LLM, un modelo de embeddings y uno de voz desde un mismo servidor; conectar Dify, LangChain o LlamaIndex a modelos propios
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Instala con `pip install xinference`, arranca `xinference-local` y lanza un modelo pequeño desde la interfaz web.
**Qué comprobar:** El modelo responde por la API compatible con OpenAI.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `llama-cpp`, `langchain`, `llama-index`
