# 3. Construir agentes y coordinar equipos de IA — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `adk-python`
role=library · exec=hybrid · setup=easy · mcp=False · prov=google,openai,anthropic · tags=agents,python

**Qué es:** Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini.
**Stack:** Python 3.11+; entorno virtual; modelo configurado
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Los modelos y servicios se facturan según el proveedor; el SDK no incluye crédito de Antigravity
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Que Google publique ADK no lo convierte en configuración de Antigravity
- Coste: El coste depende del proveedor o la ruta. Los modelos y servicios se facturan según el proveedor; el SDK no incluye crédito de Antigravity
- Equipo: Preparación según la ruta elegida. Python 3.11+; entorno virtual; modelo configurado
**Repo:** https://github.com/google/adk-python

**Instalación** [+]:

```
pip install google-adk
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar información de negocio; Evaluar la selección de herramientas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta el horario de una tienda ficticia mediante una herramienta del agente
**Qué comprobar:** El agente devuelve el dato de la herramienta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `fastmcp`, `langfuse`, `google-skills`, `awesome-llm-apps`, `gemini-skills`
**Alternativas (elige una):** `langgraph`, `openai-agents-python`

## `ag2`
role=library · exec=cloud · setup=medium · mcp=False · prov=— · tags=automation,agents,python

**Qué es:** AG2 v1 utiliza import ag2 y su propia arquitectura de agentes y redes. Los proyectos con ConversableAgent, GroupChat e import autogen deben seguir la distribución ag2-classic y su documentación de migración.
**Stack:** Python 3.11+; extra del proveedor elegido
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Ofrece extras para OpenAI, Anthropic, Gemini y Ollama; cada proveedor conserva sus costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. AG2 v1 no sustituye directamente Classic: ConversableAgent y GroupChat siguen en ag2-classic con import autogen
- Coste: El coste depende del proveedor o la ruta. Ofrece extras para OpenAI, Anthropic, Gemini y Ollama; cada proveedor conserva sus costes
- Equipo: Preparación según la ruta elegida. Python 3.11+; extra del proveedor elegido
**Repo:** https://github.com/ag2ai/ag2

**Instalación** [+]:

```
pip install ag2[openai]
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Coordinar redactor y verificador; Incluir intervención humana en un equipo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Haz que un agente resuma una conversación y otro revise las omisiones
**Qué comprobar:** Se registran los intercambios usando import ag2
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `langfuse`, `agent-framework`

## `agent-framework`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic · tags=agents,python

**Qué es:** Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Kernel.
**Stack:** Python o .NET; proveedor configurado
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Admite Ollama y otros proveedores; Foundry y despliegues gestionados pueden generar gasto
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. La skill de construcción usa el agente; el runtime tiene autenticación y costes propios; módulos Lab son experimentales
- Coste: El coste depende del proveedor o la ruta. Admite Ollama y otros proveedores; Foundry y despliegues gestionados pueden generar gasto
- Equipo: Preparación según la ruta elegida. Python o .NET; proveedor configurado
**Repo:** https://github.com/microsoft/agent-framework

**Instalación** [+]:

```
pip install agent-framework
# This installs the standard package set; install `agent-framework-lab` separately for experimental modules.
# It may take a minute on first install on Windows.
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Migrar una prueba de Semantic Kernel; Coordinar especialistas con un flujo explícito
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prueba un agente y después un workflow con dos pasos y un punto de control
**Qué comprobar:** Puedes seguir las transiciones y recuperar el estado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langfuse`, `copilotkit`, `ag2`, `ollama`, `ai-agents-for-beginners`

## `agentscope`
role=library · exec=hybrid · setup=medium · mcp=True · prov=— · tags=agents,python,mcp,framework

**Qué es:** Framework de agentes en Python de origen Alibaba: agentes ReAct, multiagente, herramientas MCP, sandbox, voz en tiempo real y servicio desplegable.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/agentscope-ai/agentscope

**Instalación** [+]:

```
uv pip install agentscope
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: construir un agente con herramientas MCP y memoria que puedas inspeccionar paso a paso; orquestar un equipo de agentes con un líder que delega tareas
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `uv pip install agentscope` y ejecuta el ejemplo de inicio rápido con un modelo configurado.
**Qué comprobar:** El agente responde y usa al menos una herramienta, y puedes ver sus pasos en la salida.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `fastmcp`, `langfuse`, `litellm`

## `agno`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=agents,memory,python

**Qué es:** Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente.
**Stack:** Python; plantilla; PostgreSQL; proveedor de modelos
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El MCP de documentación no requiere autenticación; plataforma, nube y modelos pueden costar; los ingenieros Claude/Codex usan claves API
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. MCP HTTP accesible desde los tres clientes; no significa que sus planes paguen los agentes desplegados
- Coste: El coste depende del proveedor o la ruta. El MCP de documentación no requiere autenticación; plataforma, nube y modelos pueden costar; los ingenieros Claude/Codex usan claves API
- Equipo: Preparación según la ruta elegida. Python; plantilla; PostgreSQL; proveedor de modelos
**Repo:** https://github.com/agno-agi/agno

**Instalación** [?]:

```
Seguir la instalación original: https://docs.agno.com/agent-platform/overview
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Servir un agente mediante una API; Investigar fallos mediante trazas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta el MCP de documentación y pide que explique el montaje de la plataforma local
**Qué comprobar:** El agente consulta la guía y enumera servicios y credenciales necesarios
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-agent-sdk-python`, `qdrant`, `mem0`, `500-ai-agents-projects`
**Alternativas (elige una):** `crewai`, `langgraph`

## `autogpt`
role=platform · exec=hybrid · setup=heavy · mcp=True · prov=openai,anthropic · tags=agents,automation,python

**Qué es:** Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques.
**Stack:** Docker para self-hosting; credenciales o modelo local
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La plataforma alojada es de pago y ofrece acceso a modelos; self-hosting usa tus credenciales o modelo local y recursos propios
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. La plataforma actual expone MCP Streamable HTTP con clave y permisos; no confundirla con tutoriales del agente Classic ni con acceso incluido al modelo
- Coste: El coste depende del proveedor o la ruta. La plataforma alojada es de pago y ofrece acceso a modelos; self-hosting usa tus credenciales o modelo local y recursos propios
- Equipo: Preparación según la ruta elegida. Docker para self-hosting; credenciales o modelo local
**Repo:** https://github.com/Significant-Gravitas/AutoGPT

**Instalación** [+]:

```
docker run -d \
  --name autogpt \
  --restart unless-stopped \
  --shm-size 2g \
  --ulimit nofile=65536:65536 \
  --log-driver json-file \
  --log-opt max-size=50m \
  --log-opt max-file=5 \
  -p 127.0.0.1:3000:3000 \
  -e AUTOGPT_PUBLIC_URL=http://localhost:3000 \
  -v autogpt-data:/data \
  significantgravitas/autogpt:latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Procesar solicitudes recurrentes; Componer una investigación con revisión humana
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una automatización breve que transforma una entrada de texto y revisa cada bloque
**Qué comprobar:** Ves la salida y el historial de una ejecución acotada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `claude-code`, `codex`
**Alternativas (elige una):** `sim`, `langflow`

## `awesome-langgraph`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=automation,agents,javascript

**Qué es:** Repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain.
**Stack:** Navegador; necesidad concreta
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer el índice no requiere API; los proyectos enlazados tienen sus propios costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Las integraciones de los enlaces no acreditan compatibilidad del directorio completo
- Coste: Sin pago a un modelo en la ruta básica. Leer el índice no requiere API; los proyectos enlazados tienen sus propios costes
- Equipo: Preparación según la ruta elegida. Navegador; necesidad concreta
**Repo:** https://github.com/vonzosten/awesome-LangGraph

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar un flujo con memoria; Localizar evaluadores de agentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Busca una plantilla de aprobación humana y contrasta su versión con las guías oficiales
**Qué comprobar:** Tienes un candidato y sabes qué aporta al flujo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `langchain`, `deepagents`

## `camel`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,python,research,framework

**Qué es:** Framework multiagente de investigación para generar datos sintéticos, automatizar tareas y simular sociedades de agentes con muchos proveedores.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/camel-ai/camel

**Instalación** [+]:

```
pip install camel-ai
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: generar datos sintéticos con agentes que dialogan en roles; montar un experimento de simulación con muchos agentes y medir su comportamiento
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install camel-ai`, configura la clave de un modelo y ejecuta el ejemplo de ChatAgent.
**Qué comprobar:** El agente responde y el script termina sin errores mostrando la conversación.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `qdrant`, `firecrawl`, `vllm`

## `chatdev`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,python,research

**Qué es:** Plataforma multiagente sin código de OpenBMB: configura equipos de agentes por roles; la versión 1.0 simulaba una empresa de software.
**Stack:** Python, Dockerfile, package.json, pyproject.toml, requirements.txt
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OpenBMB/ChatDev

**Instalación** [+]:

```
docker compose up --build
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: prototipar una pequeña aplicación con agentes que actúan como roles de un equipo; estudiar patrones de colaboración multiagente de los artículos del proyecto
**Evita si:** necesitas una herramienta estable y auditada para datos sensibles
**Primera prueba propuesta:** Arranca la aplicación con `docker compose up --build`, configura una clave de modelo y ejecuta un flujo de ejemplo.
**Qué comprobar:** El flujo termina y muestra los mensajes entre agentes y el artefacto generado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `blender`, `blender-mcp`, `litellm`

## `claude-agent-sdk-python`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=py,framework,python

**Qué es:** SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación propia.
**Stack:** Python; credenciales API de Anthropic o proveedor admitido; directorio de prueba
**Acceso y costes:**
- API de IA: API de IA necesaria. La guía oficial del SDK prescribe autenticación API; no asumas que una suscripción personal incluye tu producto o agentes de terceros
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Integra el motor Claude Code; la guía limita ofrecer login o límites claude.ai a terceros sin autorización previa
- Coste: Consumo de APIs o servicios. La guía oficial del SDK prescribe autenticación API; no asumas que una suscripción personal incluye tu producto o agentes de terceros
- Equipo: Preparación según la ruta elegida. Python; credenciales API de Anthropic o proveedor admitido; directorio de prueba
**Repo:** https://github.com/anthropics/claude-agent-sdk-python

**Instalación** [+]:

```
pip install claude-agent-sdk
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Integrar revisión de archivos en una aplicación; Conservar sesiones de un agente propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un agente con permiso de lectura y pídele localizar un fallo en un archivo ficticio
**Qué comprobar:** Puedes ver herramientas llamadas y contrastar el fallo antes de permitir ediciones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `fastmcp`, `langfuse`, `e2b`, `agno`, `pageindex`

## `crewai`
role=library · exec=cloud · setup=easy · mcp=False · prov=— · tags=automation,agents,python

**Qué es:** Framework para orquestar "crews" de agentes con roles y tareas.
**Stack:** Python >=3.10 y <3.14; uv; proveedor o Ollama/LM Studio
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Las skills consumen tu agente; la crew utiliza su propio proveedor; AMP y servicios externos pueden costar aparte
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Compatibilidad por confirmar
- Modelos locales: Modelos locales documentados. Claude Code y Codex tienen skills documentadas; Antigravity sigue sin confirmar para esta integración
- Coste: El coste depende del proveedor o la ruta. Las skills consumen tu agente; la crew utiliza su propio proveedor; AMP y servicios externos pueden costar aparte
- Equipo: Preparación según la ruta elegida. Python >=3.10 y <3.14; uv; proveedor o Ollama/LM Studio
**Repo:** https://github.com/crewAIInc/crewAI

**Instalación** [+]:

```
uv tool install crewai
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar investigación de mercado; Separar investigación y redacción de producto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una crew que investiga y luego redacta una comparación de dos productos
**Qué comprobar:** Puedes revisar la salida y las fuentes de cada tarea
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mem0`, `langfuse`, `fastmcp`, `500-ai-agents-projects`, `ai-engineering-hub`, `copilotkit`
**Alternativas (elige una):** `langgraph`, `agno`, `metagpt`

## `deepagents`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=anthropic,openai · tags=agents,python

**Qué es:** Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos.
**Stack:** Python y uv; modelo con herramientas; directorio de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Usa el modelo configurado y sus costes; Ollama, vLLM y llama.cpp requieren hardware suficiente
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Su parecido con Claude Code no acredita el uso de la suscripción de Claude Code
- Coste: El coste depende del proveedor o la ruta. Usa el modelo configurado y sus costes; Ollama, vLLM y llama.cpp requieren hardware suficiente
- Equipo: Preparación según la ruta elegida. Python y uv; modelo con herramientas; directorio de prueba
**Repo:** https://github.com/langchain-ai/deepagents

**Instalación** [+]:

```
uv add deepagents
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Resumir documentos de proyecto; Dividir una revisión de archivos en tareas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide un plan y un informe sobre tres archivos de ejemplo
**Qué comprobar:** Puedes revisar el plan, las lecturas y el informe guardado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `langchain`, `langfuse`, `awesome-langgraph`, `nemoclaw`, `open-swe`
**Alternativas (elige una):** `openai-agents-python`

## `dify`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,agents,python,docker

**Qué es:** Plataforma integral para construir apps de IA con backend y UI listos.
**Stack:** Docker y Compose >=2.35; OpenSSL; 2 CPU y 4 GiB mínimos del servidor
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Dify Cloud tiene planes y cupos; self-hosting paga infraestructura y modelos; su licencia añade condiciones a Apache-2.0
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Genera y guarda el token de sandbox antes de arrancar; un modelo Ollama local necesita una dirección accesible desde Docker
- Coste: El coste depende del proveedor o la ruta. Dify Cloud tiene planes y cupos; self-hosting paga infraestructura y modelos; su licencia añade condiciones a Apache-2.0
- Equipo: Preparación según la ruta elegida. Docker y Compose >=2.35; OpenSSL; 2 CPU y 4 GiB mínimos del servidor
**Repo:** https://github.com/langgenius/dify

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/langgenius/dify/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un asistente sobre políticas; Diseñar un workflow visual de clasificación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una app de preguntas sobre un documento ficticio tras configurar el proveedor y los embeddings
**Qué comprobar:** La respuesta recupera un fragmento comprobable del documento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langfuse`, `ollama`, `claude-code`, `evolution-api`, `paddleocr`
**Alternativas (elige una):** `sim`, `ragflow`

## `dspy`
role=library · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,local · tags=prompts,evaluation,python

**Qué es:** Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano.
**Stack:** Python; modelo elegido; casos etiquetados
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La optimización repite llamadas y puede acumular consumo; la guía también ofrece Ollama local
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Reserva ejemplos distintos para medir el resultado de la optimización
- Coste: El coste depende del proveedor o la ruta. La optimización repite llamadas y puede acumular consumo; la guía también ofrece Ollama local
- Equipo: Preparación según la ruta elegida. Python; modelo elegido; casos etiquetados
**Repo:** https://github.com/stanfordnlp/dspy

**Instalación** [+]:

```
pip install dspy
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Clasificar solicitudes de soporte; Optimizar un extractor de datos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Clasifica tema y urgencia de cinco mensajes ficticios antes de optimizar
**Qué comprobar:** Obtienes campos estructurados y una medida de aciertos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mlflow`, `langfuse`, `ragas`, `hermes-agent-self-evolution`, `opik`
**Alternativas (elige una):** `promptfoo`

## `haystack`
role=library · exec=hybrid · setup=medium · mcp=True · prov=openai,anthropic,local · tags=rag,agents,python

**Qué es:** Framework de deepset para pipelines de RAG y agentes listos para producción.
**Stack:** Python; documentos; componentes de recuperación y generación
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La biblioteca admite modelos locales y remotos; deepset gestionado, almacenamiento y modelos son costes separados
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. El MCP se publica mediante el proyecto compañero Hayhooks y requiere configurar y servir pipelines; sus modelos y claves se eligen aparte
- Coste: El coste depende del proveedor o la ruta. La biblioteca admite modelos locales y remotos; deepset gestionado, almacenamiento y modelos son costes separados
- Equipo: Preparación según la ruta elegida. Python; documentos; componentes de recuperación y generación
**Repo:** https://github.com/deepset-ai/haystack

**Instalación** [+]:

```
pip install haystack-ai
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Responder sobre manuales propios; Comparar recuperación de dos consultas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Recupera un párrafo de un manual antes de generar la respuesta
**Qué comprobar:** Puedes inspeccionar el párrafo y contrastar la salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `qdrant`, `docling`, `ollama`, `langfuse`, `turbovec`
**Alternativas (elige una):** `llama-index`, `langchain`

## `hermes-agent-self-evolution`
role=library · exec=cloud · setup=medium · mcp=False · prov=— · tags=experimentos,python

**Qué es:** Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GEPA.
**Stack:** Python; checkout de Hermes Agent; credenciales del optimizador; casos de evaluación
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada opera mediante APIs y no requiere entrenamiento GPU; el presupuesto depende de iteraciones y evaluaciones
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Solo la evolución de skills figura implementada; herramientas, prompts del sistema, código y bucle continuo son fases previstas; lee sesiones Claude Code como datos
- Coste: Consumo de APIs o servicios. La ruta documentada opera mediante APIs y no requiere entrenamiento GPU; el presupuesto depende de iteraciones y evaluaciones
- Equipo: Preparación según la ruta elegida. Python; checkout de Hermes Agent; credenciales del optimizador; casos de evaluación
**Repo:** https://github.com/NousResearch/hermes-agent-self-evolution

**Instalación** [+]:

```
# Install
git clone https://github.com/NousResearch/hermes-agent-self-evolution.git
cd hermes-agent-self-evolution
pip install -e ".[dev]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Refinar una skill de revisión de código; Comparar instrucciones con fallos observados
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Optimiza una skill pequeña con datos sintéticos y compara el candidato antes de aceptarlo
**Qué comprobar:** Puedes revisar diferencias y puntuaciones manteniendo la versión inicial
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `hermes-agent`, `dspy`, `claude-code`

## `jev-fraud`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=experimentos,template,typescript

**Qué es:** Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude.
**Stack:** Node.js y npm; claves Together y AI Gateway solo para ejecución nueva
**Acceso y costes:**
- API de IA: API de IA opcional. La reproducción no hace llamadas; una ejecución nueva o npm run benchmark consume APIs; la cifra de la grabación no es una tarifa garantizada
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una demo sobre una muestra pequeña; sus resultados no validan un detector de fraude en producción
- Coste: El coste depende del proveedor o la ruta. La reproducción no hace llamadas; una ejecución nueva o npm run benchmark consume APIs; la cifra de la grabación no es una tarifa garantizada
- Equipo: Preparación según la ruta elegida. Node.js y npm; claves Together y AI Gateway solo para ejecución nueva
**Repo:** https://github.com/Nutlope/jev-fraud

**Instalación** [+]:

```
git clone https://github.com/Nutlope/jev-fraud.git
   cd jev-fraud
   npm install
   cp .env.example .env.local

npm run dev -- --port 3017
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar clasificación con escalado de casos inciertos; Comparar confianza y aciertos sobre un conjunto ficticio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre la aplicación y usa primero 10s replay sobre la grabación incluida
**Qué comprobar:** Ves la demostración grabada sin lanzar una clasificación nueva
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vercel-ai`, `promptfoo`, `ui`

## `langchain`
role=library · exec=cloud · setup=medium · mcp=False · prov=— · tags=agents,automation,python

**Qué es:** Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas).
**Stack:** Python y uv; proveedor o modelo local
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Pagas el proveedor o el hardware local; LangSmith es opcional y tiene condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Instala la integración del modelo además del paquete base; compatibilidad con Anthropic API no equivale a Claude Code
- Coste: El coste depende del proveedor o la ruta. Pagas el proveedor o el hardware local; LangSmith es opcional y tiene condiciones propias
- Equipo: Preparación según la ruta elegida. Python y uv; proveedor o modelo local
**Repo:** https://github.com/langchain-ai/langchain

**Instalación** [+]:

```
uv add langchain
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar un catálogo de prueba; Responder sobre documentos propios
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pregunta por existencias a una herramienta con tres productos ficticios
**Qué comprobar:** La respuesta coincide con los datos y muestra la llamada a la herramienta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `langfuse`, `qdrant`, `ollama`
**Alternativas (elige una):** `llama-index`, `haystack`

## `langchain4j`
role=library · exec=hybrid · setup=medium · mcp=True · prov=— · tags=ts,anthropic,chatgpt,chroma,embeddings,gemini,gpt,huggingface

**Qué es:** Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la JVM.
**Stack:** JDK y Maven o Gradle según la integración; modelo
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Ofrece Ollama local y proveedores remotos; recursos, almacenamiento y APIs se pagan según la ruta
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es una biblioteca Java independiente; no es un port con las mismas versiones o API que LangChain Python
- Coste: El coste depende del proveedor o la ruta. Ofrece Ollama local y proveedores remotos; recursos, almacenamiento y APIs se pagan según la ruta
- Equipo: Preparación según la ruta elegida. JDK y Maven o Gradle según la integración; modelo
**Repo:** https://github.com/langchain4j/langchain4j

**Instalación** [?]:

```
Seguir la instalación original: https://docs.langchain4j.dev/get-started
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir IA a Spring Boot; Recuperar documentos desde una aplicación JVM
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Integra un chat que consulta un objeto de inventario de prueba en Java
**Qué comprobar:** El resultado devuelve el dato del objeto y puede validarse con un test
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `qdrant`, `pgvector`, `milvus`

## `langflow`
role=app · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,agents,python,docker

**Qué es:** Constructor visual de flujos LLM/agentes construido sobre LangChain.
**Stack:** Python 3.10–3.14; uv; entorno virtual; contraseña de administrador
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Los modelos del flujo y del Assistant son configuraciones distintas y pueden consumir por separado; Ollama ofrece una ruta local
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Configura la contraseña antes de iniciar; las herramientas de autoría MCP pueden crear componentes que ejecutan código en el servidor
- Coste: El coste depende del proveedor o la ruta. Los modelos del flujo y del Assistant son configuraciones distintas y pueden consumir por separado; Ollama ofrece una ruta local
- Equipo: Preparación según la ruta elegida. Python 3.10–3.14; uv; entorno virtual; contraseña de administrador
**Repo:** https://github.com/langflow-ai/langflow

**Instalación** [+]:

```
uv pip install langflow -U

uv run langflow run
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un agente visual; Exponer un flujo como herramienta MCP
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre Simple Agent y conecta un modelo y una herramienta de cálculo
**Qué comprobar:** Puedes ejecutar una pregunta y revisar el recorrido por los componentes
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langfuse`, `ollama`, `claude-code`, `langchain`
**Alternativas (elige una):** `sim`, `autogpt`

## `langgraph`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google,local · tags=agents,python

**Qué es:** Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming.
**Stack:** Python y entorno virtual; modelo solo para nodos LLM
**Acceso y costes:**
- API de IA: API de IA opcional. El grafo admite funciones sin LLM; los modelos, LangSmith y el alojamiento pueden costar aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Ollama se configura mediante la integración LangChain; no es un plugin del editor
- Coste: El coste depende del proveedor o la ruta. El grafo admite funciones sin LLM; los modelos, LangSmith y el alojamiento pueden costar aparte
- Equipo: Preparación según la ruta elegida. Python y entorno virtual; modelo solo para nodos LLM
**Repo:** https://github.com/langchain-ai/langgraph

**Instalación** [+]:

```
pip install -U langgraph
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Pausar una devolución hasta su revisión; Retomar una investigación interrumpida
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un grafo que guarda un pedido y se detiene para revisión humana
**Qué comprobar:** Puedes inspeccionar el estado y reanudar el pedido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langchain`, `deepagents`, `langfuse`, `mem0`
**Alternativas (elige una):** `crewai`, `openai-agents-python`, `pydantic-ai`, `adk-python`, `agno`

## `langgraphjs`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,typescript

**Qué es:** Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador.
**Stack:** Node.js; TypeScript; modelo solo para nodos LLM
**Acceso y costes:**
- API de IA: API de IA opcional. El grafo no necesita necesariamente un modelo; los nodos LLM, alojamiento y observabilidad pueden costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Ollama está documentado mediante @langchain/ollama; revisa que el modelo soporte las herramientas necesarias
- Coste: El coste depende del proveedor o la ruta. El grafo no necesita necesariamente un modelo; los nodos LLM, alojamiento y observabilidad pueden costar
- Equipo: Preparación según la ruta elegida. Node.js; TypeScript; modelo solo para nodos LLM
**Repo:** https://github.com/langchain-ai/langgraphjs

**Instalación** [+]:

```
npm install @langchain/langgraph @langchain/core
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Controlar aprobación de una solicitud; Reanudar un agente en una app JavaScript
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Monta un grafo que clasifica una solicitud y espera revisión antes de continuar
**Qué comprobar:** Se conserva el estado y se ve el siguiente paso
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langchain`, `langfuse`, `copilotkit`, `langgraph`, `agent-protocol`, `social-media-agent`
**Alternativas (elige una):** `mastra`, `vercel-ai`

## `llama-index`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,local · tags=rag,agents,python

**Qué es:** Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos.
**Stack:** Python; dos documentos; modelo generativo y embeddings
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. OpenAI consume API; Ollama y embeddings locales evitan esa API; LlamaParse se presupuesta aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Configura también embeddings locales si quieres que todo el procesamiento sea local
- Coste: El coste depende del proveedor o la ruta. OpenAI consume API; Ollama y embeddings locales evitan esa API; LlamaParse se presupuesta aparte
- Equipo: Preparación según la ruta elegida. Python; dos documentos; modelo generativo y embeddings
**Repo:** https://github.com/run-llama/llama_index

**Instalación** [+]:

```
# custom selection of integrations to work with core
pip install llama-index-core
pip install llama-index-llms-openai
pip install llama-index-llms-ollama
pip install llama-index-embeddings-huggingface
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar políticas internas; Encontrar cláusulas en contratos ficticios
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pregunta por una cifra que solo aparece en uno de tus dos documentos
**Qué comprobar:** Se recupera el documento correcto y puedes contrastar el fragmento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `qdrant`, `docling`, `ragas`, `ollama`
**Alternativas (elige una):** `haystack`, `langchain`

## `llm-council`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,python

**Qué es:** "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder.
**Stack:** Python y uv; Node.js; clave OpenRouter
**Acceso y costes:**
- API de IA: API de IA necesaria. Cada pregunta puede producir varias llamadas mediante OpenRouter; el coste crece con los miembros y sus revisiones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Una mayoría de modelos puede compartir el mismo error; comprueba las afirmaciones con fuentes
- Coste: Consumo de APIs o servicios. Cada pregunta puede producir varias llamadas mediante OpenRouter; el coste crece con los miembros y sus revisiones
- Equipo: Preparación según la ruta elegida. Python y uv; Node.js; clave OpenRouter
**Repo:** https://github.com/karpathy/llm-council

**Instalación** [+]:

```
uv sync

cd frontend
npm install
cd ..
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar explicaciones de un concepto; Revisar opciones para una decisión técnica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Envía una pregunta acotada y compara las respuestas y las revisiones entre modelos
**Qué comprobar:** Se distinguen propuestas iniciales, evaluaciones y síntesis final
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `ollama`, `promptfoo`

## `mastra`
role=library · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=agents,rag,typescript

**Qué es:** Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby.
**Stack:** Node.js y npm; proveedor elegido
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El framework base es Apache-2.0; nube, modelos y partes con otra licencia tienen condiciones separadas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. No copies el bloque de prompt del README como comando de terminal; el instalador es npm create mastra
- Coste: El coste depende del proveedor o la ruta. El framework base es Apache-2.0; nube, modelos y partes con otra licencia tienen condiciones separadas
- Equipo: Preparación según la ruta elegida. Node.js y npm; proveedor elegido
**Repo:** https://github.com/mastra-ai/mastra

**Instalación** [+]:

```
npm create mastra@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir un agente a una app TypeScript; Pausar y reanudar un flujo de aprobación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un proyecto y añade una herramienta que devuelva el precio de un producto ficticio
**Qué comprobar:** Puedes probar el agente y ver la herramienta usada en sus trazas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `copilotkit`, `langfuse`, `ollama`, `composio`, `openbot`
**Alternativas (elige una):** `langgraphjs`, `vercel-ai`

## `metagpt`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=— · tags=py,agent,gpt,llm,metagpt,multi-agent,python

**Qué es:** Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo.
**Stack:** Python según guía estable; proveedor o Ollama; directorio de salida de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Cada rol puede llamar varias veces al modelo; Ollama está en la configuración; APIs y herramientas externas cuestan según uso
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Los artefactos generados no acreditan una aplicación lista ni sustituyen pruebas y revisión
- Coste: El coste depende del proveedor o la ruta. Cada rol puede llamar varias veces al modelo; Ollama está en la configuración; APIs y herramientas externas cuestan según uso
- Equipo: Preparación según la ruta elegida. Python según guía estable; proveedor o Ollama; directorio de salida de prueba
**Repo:** https://github.com/FoundationAgents/MetaGPT

**Instalación** [+]:

```
pip install --upgrade metagpt
# or `pip install --upgrade git+https://github.com/geekan/MetaGPT.git`
# or `git clone https://github.com/geekan/MetaGPT && cd MetaGPT && pip install --upgrade -e .`
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Bocetar requisitos de una app; Simular roles de un equipo de software
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide el diseño de una lista de tareas mínima y revisa requisitos y estructura antes del código
**Qué comprobar:** Obtienes artefactos separados que puedes revisar y corregir
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `e2b`, `claude-code`
**Alternativas (elige una):** `crewai`

## `mirofish`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=agents,python

**Qué es:** Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios.
**Stack:** Docker o Node 18+ y Python 3.11–3.12; clave LLM; Zep Cloud
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada usa API compatible OpenAI y Zep; muchas rondas multiplican consumo; los cupos gratuitos pueden cambiar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Son simulaciones generadas, no predicciones validadas del mercado ni evidencia de cómo actuarán personas reales
- Coste: Consumo de APIs o servicios. La ruta documentada usa API compatible OpenAI y Zep; muchas rondas multiplican consumo; los cupos gratuitos pueden cambiar
- Equipo: Preparación según la ruta elegida. Docker o Node 18+ y Python 3.11–3.12; clave LLM; Zep Cloud
**Repo:** https://github.com/666ghj/MiroFish

**Instalación** [+]:

```
# 1. Configure environment variables (same as source deployment)
cp .env.example .env

# 2. Pull image and start
docker compose up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar reacciones hipotéticas a un anuncio; Comparar escenarios narrativos antes de investigar datos reales
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un escenario ficticio y realiza una simulación corta con menos de 40 rondas
**Qué comprobar:** Puedes inspeccionar los agentes simulados y el informe del escenario
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `graphiti`, `litellm`, `ollama`, `pythia`

## `openai-agents-python`
role=library · exec=hybrid · setup=easy · mcp=True · prov=openai · tags=agents,python

**Qué es:** SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas.
**Stack:** Python y uv; modelo y credenciales
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El ejemplo usa OPENAI_API_KEY; otros proveedores tienen condiciones propias; Codex no aporta créditos a este SDK
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Es una biblioteca de aplicaciones; la disponibilidad de adaptadores no confirma por sí sola una ruta local completa
- Coste: El coste depende del proveedor o la ruta. El ejemplo usa OPENAI_API_KEY; otros proveedores tienen condiciones propias; Codex no aporta créditos a este SDK
- Equipo: Preparación según la ruta elegida. Python y uv; modelo y credenciales
**Repo:** https://github.com/openai/openai-agents-python

**Instalación** [+]:

```
uv init
uv add openai-agents
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Enrutar consultas por departamento; Validar una respuesta antes de aceptarla
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Deriva una consulta a un especialista de facturación ficticio
**Qué comprobar:** La traza muestra el traspaso y su respuesta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `openai-python`, `langfuse`, `fastmcp`, `awesome-llm-apps`, `composio`
**Alternativas (elige una):** `pydantic-ai`, `langgraph`, `smolagents`, `deepagents`, `adk-python`

## `openevolve`
role=runtime · exec=cloud · setup=heavy · mcp=False · prov=— · tags=automation,agents,python

**Qué es:** Agente de codificación evolutivo que optimiza algoritmos por simulación genética.
**Stack:** Python 3.10+; evaluador de calidad; API o CLI compatible autenticado
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Admite APIs y los CLI de Claude Code o Codex; cada ruta mantiene sus límites; la búsqueda repetida puede acumular consumo
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Es una implementación independiente de AlphaEvolve; una puntuación mejor solo vale para el evaluador definido
- Coste: El coste depende del proveedor o la ruta. Admite APIs y los CLI de Claude Code o Codex; cada ruta mantiene sus límites; la búsqueda repetida puede acumular consumo
- Equipo: Preparación según la ruta elegida. Python 3.10+; evaluador de calidad; API o CLI compatible autenticado
**Repo:** https://github.com/algorithmicsuperintelligence/openevolve

**Instalación** [+]:

```
git clone https://github.com/algorithmicsuperintelligence/openevolve.git
cd openevolve
pip install -e .
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Optimizar una función medible; Buscar mejores reglas de ordenación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prueba la minimización de una función con pocas iteraciones y revisa cada candidato
**Qué comprobar:** El evaluador permite comparar la puntuación inicial y la final
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `vllm`, `litellm`

## `openmanus`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,python,browser

**Qué es:** Agente general de código abierto inspirado en Manus: planifica tareas y usa navegador, Python y archivos mediante herramientas y MCP.
**Stack:** Python, Dockerfile, requirements.txt, setup.py
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/FoundationAgents/OpenManus

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/FoundationAgents/OpenManus/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: delegar una investigación web que termine en un informe guardado en disco; experimentar con un agente general en local antes de elegir un framework
**Evita si:** necesitas una herramienta estable y auditada para datos sensibles
**Primera prueba propuesta:** Crea el entorno con uv según el README, configura la clave del modelo en config.toml y lanza una tarea pequeña de búsqueda.
**Qué comprobar:** El agente completa los pasos visibles en consola y deja el resultado en el espacio de trabajo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `browser-use`, `playwright`, `litellm`

## `pydantic-ai`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,google,local · tags=agents,python

**Qué es:** Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo.
**Stack:** Python y uv; esquema de salida; modelo
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Admite Ollama y APIs; Logfire opcional y servicios asociados se presupuestan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Empieza con el paquete base; el harness de programación es un componente adicional
- Coste: El coste depende del proveedor o la ruta. Admite Ollama y APIs; Logfire opcional y servicios asociados se presupuestan aparte
- Equipo: Preparación según la ruta elegida. Python y uv; esquema de salida; modelo
**Repo:** https://github.com/pydantic/pydantic-ai

**Instalación** [+]:

```
uv add pydantic-ai
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer campos de mensajes; Validar datos generados antes de guardarlos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Extrae nombre, importe y moneda de una factura ficticia
**Qué comprobar:** El resultado respeta los tipos o informa del fallo de validación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langfuse`, `fastmcp`, `ollama`, `browser-use`, `loguru`, `mcp-python-sdk`
**Alternativas (elige una):** `openai-agents-python`, `smolagents`, `langgraph`

## `sim`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=openai,anthropic,local · tags=agents,automation,typescript

**Qué es:** Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual.
**Stack:** Node.js 20+; Docker; proveedor o modelo local
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Cloud y servicios adicionales tienen planes; self-hosting añade infraestructura; las llamadas a modelos se presupuestan según ruta
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. MCP HTTP permite operar workflows desde clientes; inicia sesión y distingue ese acceso de las credenciales del modelo
- Coste: El coste depende del proveedor o la ruta. Cloud y servicios adicionales tienen planes; self-hosting añade infraestructura; las llamadas a modelos se presupuestan según ruta
- Equipo: Preparación según la ruta elegida. Node.js 20+; Docker; proveedor o modelo local
**Repo:** https://github.com/simstudioai/sim

**Instalación** [+]:

```
npx sim-setup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar una clasificación de mensajes; Probar un flujo con Ollama antes de usar una API
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Construye un flujo visual que recibe texto, lo resume y registra la salida
**Qué comprobar:** La ejecución muestra cada bloque y el resumen final
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `vllm`, `claude-code`, `codex`
**Alternativas (elige una):** `langflow`, `dify`, `autogpt`

## `smolagents`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,local · tags=agents,python

**Qué es:** Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python.
**Stack:** Python; modelo; ejecutor aislado
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Admite Transformers u Ollama locales y APIs; aislamiento y búsqueda externa pueden costar aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El agente ejecuta código: usa el aislamiento documentado y archivos de prueba
- Coste: El coste depende del proveedor o la ruta. Admite Transformers u Ollama locales y APIs; aislamiento y búsqueda externa pueden costar aparte
- Equipo: Preparación según la ruta elegida. Python; modelo; ejecutor aislado
**Repo:** https://github.com/huggingface/smolagents

**Instalación** [+]:

```
pip install "smolagents[toolkit]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Calcular indicadores de un CSV; Transformar datos consultados en un resumen
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Calcula el total y promedio de cinco importes ficticios y revisa el código generado
**Qué comprobar:** Los resultados coinciden con los números de entrada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `e2b`, `transformers`, `litellm`, `langfuse`
**Alternativas (elige una):** `pydantic-ai`, `openai-agents-python`

## `vercel-ai`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,google,local · tags=agents,ui,typescript,react

**Qué es:** Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat.
**Stack:** Node.js; proyecto TypeScript; paquete del proveedor
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El SDK no incluye modelos ni créditos; proveedores, AI Gateway y alojamiento tienen costes separados
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Compatibilidad por confirmar
- Antigravity: Compatibilidad por confirmar
- Modelos locales: Modelo local no documentado. El README ofrece una skill para Claude Code; instalarla no paga la inferencia de la aplicación
- Coste: El coste depende del proveedor o la ruta. El SDK no incluye modelos ni créditos; proveedores, AI Gateway y alojamiento tienen costes separados
- Equipo: Preparación según la ruta elegida. Node.js; proyecto TypeScript; paquete del proveedor
**Repo:** https://github.com/vercel/ai

**Instalación** [+]:

```
npm install ai
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una interfaz de chat; Extraer datos tipados de un mensaje
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade una respuesta de chat en streaming y una herramienta de consulta de estado
**Qué comprobar:** El texto llega por partes y la llamada devuelve el estado ficticio
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `assistant-ui`, `ui`, `langfuse`, `ollama`, `mem0`
**Alternativas (elige una):** `langgraphjs`, `mastra`
