# 19. Aprender IA y escribir mejores prompts — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `12-factor-agents`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,learning,prompts,typescript

**Qué es:** Guía de 12 principios de ingeniería para construir agentes con LLM fiables en producción, inspirada en las 12 Factor Apps.
**Stack:** Navegador; flujo de agente dibujado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La guía no necesita API; implementar sus ideas sí puede usar modelos de pago o locales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El bloque de pseudocódigo es ilustrativo y no un instalador ejecutable; la licencia de contenido es CC BY-SA
- Coste: Sin pago a un modelo en la ruta básica. La guía no necesita API; implementar sus ideas sí puede usar modelos de pago o locales
- Equipo: Preparación según la ruta elegida. Navegador; flujo de agente dibujado
**Repo:** https://github.com/humanlayer/12-factor-agents

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar un diseño antes de programar; Estudiar recuperación de errores en agentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Aplica el principio de controlar el flujo a un agente imaginario de soporte y señala dónde pedir intervención humana
**Qué comprobar:** Obtienes un diagrama con pasos deterministas y decisiones del modelo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `context-engineering`, `langgraph`, `vercel-ai`

## `500-ai-agents-projects`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=guias,ai-agents,genai,python

**Qué es:** Colección de casos de uso y agentes autocontenidos, junto con enlaces a implementaciones externas.
**Stack:** Navegador; dependencias y proveedor de un agente elegido
**Acceso y costes:**
- API de IA: API de IA opcional. La lista es libre; ejecutar cada implementación tiene costes y requisitos propios
- Claude Code: Depende del recurso o la configuración
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: Modelos locales documentados. Actualmente incluye agentes autocontenidos además de enlaces externos; mencionar un proyecto de Claude Code no hace compatible todo el directorio
- Coste: El coste depende del proveedor o la ruta. La lista es libre; ejecutar cada implementación tiene costes y requisitos propios
- Equipo: Preparación según la ruta elegida. Navegador; dependencias y proveedor de un agente elegido
**Repo:** https://github.com/ashishpatel26/500-AI-Agents-Projects

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una idea de agente para un sector; Comparar un ejemplo local con uno por API
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Selecciona el agente de investigación web y revisa su .env.example sin añadir credenciales todavía
**Qué comprobar:** Puedes enumerar fuentes de datos, modelo y permisos necesarios
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `crewai`, `langgraph`, `agno`

## `agents-towards-production`
role=directory · exec=cloud · setup=medium · mcp=True · prov=openai,local · tags=agents,learning,notebooks,python

**Qué es:** Colección de 28 tutoriales con código para llevar agentes de IA a producción: memoria, despliegue, seguridad, trazas y evaluación.
**Stack:** Python; dependencias por tutorial; servicios o GPU según ejercicio
**Acceso y costes:**
- API de IA: API de IA opcional. Consultar no requiere API; los laboratorios pueden consumir nube, modelos y cómputo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La colección declara licencia personalizada no comercial; cada tutorial tiene entorno propio y no acredita un despliegue productivo por seguirlo
- Coste: El coste depende del proveedor o la ruta. Consultar no requiere API; los laboratorios pueden consumir nube, modelos y cómputo
- Equipo: Preparación según la ruta elegida. Python; dependencias por tutorial; servicios o GPU según ejercicio
**Repo:** https://github.com/NirDiamant/agents-towards-production

**Instalación** [+]:

```
git clone https://github.com/NirDiamant/agents-towards-production.git
cd agents-towards-production
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender a desplegar un agente; Comparar un servicio LLM con Ollama on-prem
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige un tutorial de observabilidad y enumera sus entradas, trazas y criterios de evaluación
**Qué comprobar:** Puedes reconocer qué evidencia permitiría diagnosticar un fallo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `mem0`, `ollama`

## `ai-agents-for-beginners`
role=directory · exec=cloud · setup=medium · mcp=False · prov=openai,local · tags=agents,learning,notebooks,python

**Qué es:** Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, traducido al español.
**Stack:** Navegador; Python y cuenta Azure para los ejercicios principales
**Acceso y costes:**
- API de IA: API de IA opcional. Leer no requiere API; el código actual usa Microsoft Foundry y servicios de Azure con costes y límites propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El README actual usa Agent Framework y Foundry Agent Service V2; algunos ejemplos aceptan otros proveedores compatibles y no se presupone ejecución local
- Coste: El coste depende del proveedor o la ruta. Leer no requiere API; el código actual usa Microsoft Foundry y servicios de Azure con costes y límites propios
- Equipo: Preparación según la ruta elegida. Navegador; Python y cuenta Azure para los ejercicios principales
**Repo:** https://github.com/microsoft/ai-agents-for-beginners

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender patrones de agentes; Estudiar herramientas y memoria con ejemplos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee la primera lección y dibuja las herramientas y decisiones de un agente de consultas ficticio
**Qué comprobar:** Puedes distinguir el agente de una llamada única al modelo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `agent-framework`, `generative-ai-for-beginners`, `mcp-for-beginners`

## `ai-engineering-hub`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=guias,agents,ai,llms,machine-learning,mcp,rag,jupyter notebook

**Qué es:** Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificial.
**Stack:** Python; README específico del tutorial; modelo local o proveedor
**Acceso y costes:**
- API de IA: API de IA opcional. Tutoriales públicos; APIs, nube y GPU pueden generar costes según el ejemplo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Las comparaciones con Claude Code son contenido educativo y no una integración instalada del catálogo
- Coste: El coste depende del proveedor o la ruta. Tutoriales públicos; APIs, nube y GPU pueden generar costes según el ejemplo
- Equipo: Preparación según la ruta elegida. Python; README específico del tutorial; modelo local o proveedor
**Repo:** https://github.com/patchy631/ai-engineering-hub

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender RAG con Ollama; Comparar técnicas de ajuste fino
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige Simple RAG Workflow y dibuja ingestión, recuperación y generación
**Qué comprobar:** Puedes identificar dónde se almacenan documentos y dónde se usa el modelo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `crewai`, `llama-index`, `firecrawl`, `ollama`

## `awesome-harness-engineering`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=guias,reference,python

**Qué es:** Directorio de herramientas y patrones para diseñar el entorno, memoria, evaluación y permisos de agentes de IA.
**Stack:** Navegador; flujo de agente de referencia
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La lista es gratuita; cada herramienta y proveedor enlazado tiene sus propios costes
- Claude Code: Referencia para la herramienta; no es una integración
- Codex: Referencia para la herramienta; no es una integración
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una selección de referencias que incluye Claude Code y Codex; no un paquete único de skills ni garantía de compatibilidad de todos sus enlaces
- Coste: Sin pago a un modelo en la ruta básica. La lista es gratuita; cada herramienta y proveedor enlazado tiene sus propios costes
- Equipo: Preparación según la ruta elegida. Navegador; flujo de agente de referencia
**Repo:** https://github.com/ai-boost/awesome-harness-engineering

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar el entorno de un agente; Encontrar recursos de evaluación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Selecciona las secciones de permisos y evaluación y redacta tres preguntas para revisar tu agente
**Qué comprobar:** Puedes separar ejecución, memoria, observabilidad y control de permisos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `12-factor-agents`, `loop-engineering`, `claude-code`

## `awesome-llm-apps`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google,local · tags=agents,rag,learning,python

**Qué es:** Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM.
**Stack:** Navegador; entorno y proveedor específicos del ejemplo elegido
**Acceso y costes:**
- API de IA: API de IA opcional. La colección se consulta gratis; hay apps con API, modelos locales y skills que usan el plan del anfitrión
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: Modelos locales documentados. Documenta skills para Claude Code y Codex; no todas las apps son skills ni tienen idéntica compatibilidad o instalación
- Coste: El coste depende del proveedor o la ruta. La colección se consulta gratis; hay apps con API, modelos locales y skills que usan el plan del anfitrión
- Equipo: Preparación según la ruta elegida. Navegador; entorno y proveedor específicos del ejemplo elegido
**Repo:** https://github.com/Shubhamsaboo/awesome-llm-apps

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender con un asistente de viajes; Estudiar un RAG con Llama local
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Escoge una app de RAG local y revisa su README y requisitos antes de descargar modelos
**Qué comprobar:** Sabes qué archivos, modelo y servicio necesita esa app concreta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `streamlit`, `openai-agents-python`, `adk-python`, `firecrawl`
**Alternativas (elige una):** `openai-cookbook`, `claude-cookbooks`

## `awesome-machine-learning`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=aprender,python

**Qué es:** Directorio de frameworks, bibliotecas y recursos de machine learning organizado por lenguaje y tema.
**Stack:** Navegador; lenguaje y problema de interés
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Directorio gratuito; cada recurso externo define licencia, coste y hardware
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No se instala la lista ni se hereda la compatibilidad de todos los proyectos enlazados
- Coste: Sin pago a un modelo en la ruta básica. Directorio gratuito; cada recurso externo define licencia, coste y hardware
- Equipo: Preparación según la ruta elegida. Navegador; lenguaje y problema de interés
**Repo:** https://github.com/josephmisiti/awesome-machine-learning

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Descubrir bibliotecas de clasificación; Encontrar herramientas de visión por lenguaje
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Busca dos bibliotecas del lenguaje que conoces y abre sus fuentes para comparar mantenimiento y requisitos
**Qué comprobar:** Obtienes una pequeña lista de candidatos con función diferenciada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `transformers`, `llm-course`

## `chatgpt-dan`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=prompts,chatgpt,gpt-3-5,gpt-4,jailbreak,openai,prompt

**Qué es:** Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones antiguas de ChatGPT.
**Stack:** Navegador; criterio de lectura histórica
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El archivo se consulta sin API; no incluye acceso a modelos ni créditos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Las afirmaciones de funcionamiento se refieren a GPT-3.5 en 2023 y no prueban eficacia ni compatibilidad actual
- Coste: Sin pago a un modelo en la ruta básica. El archivo se consulta sin API; no incluye acceso a modelos ni créditos
- Equipo: Preparación según la ruta elegida. Navegador; criterio de lectura histórica
**Repo:** https://github.com/0xk1h0/ChatGPT_DAN

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar la historia de prompts de roleplay; Reconocer intentos de manipulación de instrucciones
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee el aviso de fecha y analiza cómo un prompt intenta sustituir las instrucciones del sistema sin aplicarlo a servicios ajenos
**Qué comprobar:** Puedes explicar por qué no constituye una configuración soportada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `promptfoo`, `system-prompts-and-models-of-ai-tools`, `chatgpt-system-prompt`

## `chatgpt-system-prompt`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=prompts,gpt,prompt,prompt-engineering,html

**Qué es:** Colección de prompts de GPT y recursos sobre instrucciones de sistema y extracción de prompts.
**Stack:** Navegador; ejemplo propio de instrucciones
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer el repositorio no consume API; probar prompts usa el servicio elegido
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Colección comunitaria educativa; atribuciones o extracciones no son documentación oficial ni garantías sobre productos actuales
- Coste: Sin pago a un modelo en la ruta básica. Leer el repositorio no consume API; probar prompts usa el servicio elegido
- Equipo: Preparación según la ruta elegida. Navegador; ejemplo propio de instrucciones
**Repo:** https://github.com/LouisShark/chatgpt_system_prompt

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender estructura de instrucciones; Diseñar límites para un asistente propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Compara una plantilla del archivo con una instrucción de tu autoría y separa objetivo, restricciones y formato
**Qué comprobar:** Puedes identificar patrones sin asumir autenticidad de prompts atribuidos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `system-prompts-and-models-of-ai-tools`, `promptfoo`, `prompt-engineering-guide`

## `claude-cookbooks`
role=directory · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=learning,notebooks,rag,python

**Qué es:** Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización.
**Stack:** Navegador; Python y clave Anthropic para ejecutar ejemplos
**Acceso y costes:**
- API de IA: API de IA opcional. Lectura libre; la ejecución de notebooks requiere API de Claude con facturación propia
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La suscripción de Claude Code no sustituye automáticamente la clave API pedida por estos notebooks
- Coste: Consumo de APIs o servicios. Lectura libre; la ejecución de notebooks requiere API de Claude con facturación propia
- Equipo: Preparación según la ruta elegida. Navegador; Python y clave Anthropic para ejecutar ejemplos
**Repo:** https://github.com/anthropics/claude-cookbooks

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Clasificar tickets ficticios; Estudiar llamadas a herramientas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee una receta de extracción y adapta sus datos a un párrafo ficticio
**Qué comprobar:** Entiendes qué se envía al modelo y qué respuesta se valida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `prompt-eng-tutorial`, `claude-agent-sdk-python`, `promptfoo`
**Alternativas (elige una):** `openai-cookbook`, `awesome-llm-apps`

## `claude-quickstarts`
role=directory · exec=cloud · setup=medium · mcp=False · prov=anthropic · tags=guias,python

**Qué es:** Ejemplos oficiales de Anthropic para construir aplicaciones con Claude, herramientas y uso de computadora.
**Stack:** Python o TypeScript según proyecto; clave Anthropic; servicios del ejemplo
**Acceso y costes:**
- API de IA: API de IA opcional. Lectura libre; ejecutar requiere API de Claude y posibles servicios adicionales
- Claude Code: Depende del recurso o la configuración
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: Modelo local no documentado. Incluye un ejemplo MCP para Managed Agents pero no todos los quickstarts son conectores; la demo de computadora requiere un entorno aislado de prueba
- Coste: Consumo de APIs o servicios. Lectura libre; ejecutar requiere API de Claude y posibles servicios adicionales
- Equipo: Preparación según la ruta elegida. Python o TypeScript según proyecto; clave Anthropic; servicios del ejemplo
**Repo:** https://github.com/anthropics/claude-quickstarts

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar soporte con Claude; Estudiar una demo de uso de computadora
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Escoge Customer Support Agent y revisa las herramientas que permite antes de enviar una consulta ficticia
**Qué comprobar:** Puedes identificar acciones del agente y datos enviados a la API
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-agent-sdk-python`, `copilotkit`, `e2b`

## `context-engineering`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,python

**Qué es:** Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso.
**Stack:** Navegador; agente si utilizas los comandos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El material es abierto; ejecutar comandos o experimentos usa recursos del agente o proveedor
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El curso está en construcción y declara comandos para Claude Code y Codex; los resultados de artículos citados no validan por sí solos todas sus propuestas
- Coste: Consumo del agente que ya utilizas. El material es abierto; ejecutar comandos o experimentos usa recursos del agente o proveedor
- Equipo: Preparación según la ruta elegida. Navegador; agente si utilizas los comandos
**Repo:** https://github.com/jasontang-ai/Context-Engineering

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar contexto para una tarea larga; Estudiar memoria y recuperación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee el mapa de contexto y reduce un encargo a objetivo, datos pertinentes y límites
**Qué comprobar:** Puedes justificar qué datos incluyes y cuáles omites
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `12-factor-agents`, `prompt-engineering-guide`, `headroom`

## `fabric`
role=app · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,local · tags=prompts,automation,go

**Qué es:** CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal.
**Stack:** Go o instalador para tu sistema; proveedor o CLI autenticado; texto breve propio
**Acceso y costes:**
- API de IA: API de IA opcional. Ollama y LM Studio permiten modelos locales; API por consumo o backends de Claude Code y Codex con sus cuentas y límites
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Las rutas de suscripción son adaptadores del proyecto; Codex usa un backend privado y no garantiza continuidad ni cobertura de todo plan
- Coste: El coste depende del proveedor o la ruta. Ollama y LM Studio permiten modelos locales; API por consumo o backends de Claude Code y Codex con sus cuentas y límites
- Equipo: Preparación según la ruta elegida. Go o instalador para tu sistema; proveedor o CLI autenticado; texto breve propio
**Repo:** https://github.com/danielmiessler/Fabric

**Instalación** [+]:

```
go install github.com/danielmiessler/fabric/cmd/fabric@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer acciones de una reunión; Convertir notas en un esquema de artículo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un proveedor y aplica un patrón de resumen a una nota breve que ya conozcas
**Qué comprobar:** Obtienes un resumen que puedes contrastar con la nota original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `yt-dlp`, `open-webui`, `n8n`
**Alternativas (elige una):** `prompts-chat`

## `generative-ai-for-beginners`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,prompts,python

**Qué es:** Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa.
**Stack:** Navegador; Python para los laboratorios; proveedor o Foundry Local según lección
**Acceso y costes:**
- API de IA: API de IA opcional. Curso abierto; nube y APIs pueden cobrar por uso; Foundry Local ofrece una ruta offline con requisitos de equipo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. No todas las lecciones comparten dependencias ni admiten el mismo proveedor; la ruta local documentada no convierte todos los ejemplos a local
- Coste: El coste depende del proveedor o la ruta. Curso abierto; nube y APIs pueden cobrar por uso; Foundry Local ofrece una ruta offline con requisitos de equipo
- Equipo: Preparación según la ruta elegida. Navegador; Python para los laboratorios; proveedor o Foundry Local según lección
**Repo:** https://github.com/microsoft/generative-ai-for-beginners

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Empezar a construir una app generativa; Comparar nube con Foundry Local
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee la introducción y elige un ejemplo de generación de texto antes de preparar su entorno específico
**Qué comprobar:** Puedes distinguir modelo, aplicación y proveedor y localizar las dependencias de ese ejemplo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ai-agents-for-beginners`, `mcp-for-beginners`, `openai-cookbook`
**Alternativas (elige una):** `llm-course`

## `how-to-train-your-gpt`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=learning

**Qué es:** Guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción.
**Stack:** Python; Jupyter; entorno PyTorch; equipo adecuado al experimento
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere API para el recorrido local; cómputo y GPU opcional se pagan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Empieza por el capítulo de setup; los comandos del README ofrecen alternativas y no deben concatenarse como si todas fueran obligatorias
- Coste: El coste depende del proveedor o la ruta. No requiere API para el recorrido local; cómputo y GPU opcional se pagan aparte
- Equipo: Preparación según la ruta elegida. Python; Jupyter; entorno PyTorch; equipo adecuado al experimento
**Repo:** https://github.com/raiyanyahya/how-to-train-your-gpt

**Instalación** [+]:

```
# Install everything you need
pip install jupyter tiktoken torch numpy datasets matplotlib --index-url https://download.pytorch.org/whl/cpu

# Start with chapter 2 (tokenization)
jupyter notebook notebooks/02_tokenization.ipynb
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender tokenización paso a paso; Comprender atención con ejemplos pequeños
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre el notebook de tokenización y procesa una frase antes de pasar a entrenamiento
**Qué comprobar:** Puedes inspeccionar tokens y reconstrucción del texto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nanochat`, `llms-from-scratch`, `pytorch`

## `llm-course`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=learning,training,notebooks

**Qué es:** Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción.
**Stack:** Navegador; Python y cómputo al practicar
**Acceso y costes:**
- API de IA: API de IA opcional. Los recursos son públicos; Colab, GPU, nube y APIs pueden tener límites o coste
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es un mapa de aprendizaje con recursos externos y prácticas locales; no existe una instalación única para toda la ruta
- Coste: El coste depende del proveedor o la ruta. Los recursos son públicos; Colab, GPU, nube y APIs pueden tener límites o coste
- Equipo: Preparación según la ruta elegida. Navegador; Python y cómputo al practicar
**Repo:** https://github.com/mlabonne/llm-course

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un plan de aprendizaje de LLM; Estudiar cuantización GGUF
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Recorre la ruta de fundamentos y elige el notebook de cuantización solo después de revisar sus requisitos
**Qué comprobar:** Puedes ubicar la diferencia entre entrenar, cuantizar y servir un modelo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `unsloth`, `trl`, `pytorch`
**Alternativas (elige una):** `llms-from-scratch`, `generative-ai-for-beginners`

## `llm.c`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=learning

**Qué es:** Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo.
**Stack:** Compilador C; Python para preparación; CUDA y GPU para las rutas aceleradas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API; GPU, energía y alquiler de hardware pueden ser significativos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es un proyecto técnico de entrenamiento; no es una app de chat lista para personas sin programación
- Coste: El coste depende del proveedor o la ruta. No necesita API; GPU, energía y alquiler de hardware pueden ser significativos
- Equipo: Preparación según la ruta elegida. Compilador C; Python para preparación; CUDA y GPU para las rutas aceleradas
**Repo:** https://github.com/karpathy/llm.c

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/karpathy/llm.c/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar entrenamiento sin un framework pesado; Comparar una implementación C con PyTorch
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee el ejemplo GPT-2 y localiza las operaciones de forward y backward antes de compilar
**Qué comprobar:** Puedes relacionar las operaciones matemáticas con el código C
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nanochat`, `llms-from-scratch`, `pytorch`

## `llms-from-scratch`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=learning,training,python

**Qué es:** Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso.
**Stack:** Python; entorno PyTorch; nociones de programación; equipo según capítulo
**Acceso y costes:**
- API de IA: API de IA opcional. El código permite entrenamiento local; libro, GPU alquilada y evaluaciones con API son costes opcionales distintos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Requiere base de Python; la instalación está en setup y la evaluación por API no es obligatoria para todo el libro
- Coste: El coste depende del proveedor o la ruta. El código permite entrenamiento local; libro, GPU alquilada y evaluaciones con API son costes opcionales distintos
- Equipo: Preparación según la ruta elegida. Python; entorno PyTorch; nociones de programación; equipo según capítulo
**Repo:** https://github.com/rasbt/LLMs-from-scratch

**Instalación** [+]:

```
git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender cómo funciona un Transformer; Estudiar ajuste de instrucciones
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue el capítulo de tokenización con una frase corta antes de entrenar una red
**Qué comprobar:** Puedes ver la conversión de texto a tokens y explicarla
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `nanochat`, `transformers`
**Alternativas (elige una):** `llm-course`

## `loop-engineering`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=coding-agent,skills,typescript

**Qué es:** Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos.
**Stack:** Node; proyecto de prueba; Claude Code o Codex configurado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las plantillas usan el modelo o plan del agente; las estimaciones de coste no son facturas ni tarifas garantizadas
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La primera semana se plantea solo con informes; Claude y Codex están documentados y Antigravity no figura como adaptador
- Coste: Consumo del agente que ya utilizas. Las plantillas usan el modelo o plan del agente; las estimaciones de coste no son facturas ni tarifas garantizadas
- Equipo: Preparación según la ruta elegida. Node; proyecto de prueba; Claude Code o Codex configurado
**Repo:** https://github.com/cobusgreyling/loop-engineering

**Instalación** [+]:

```
npx @cobusgreyling/loop init . --pattern daily-triage --tool claude
npx @cobusgreyling/loop doctor .
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar un ciclo de revisión de issues; Estimar el coste de un bucle antes de automatizarlo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera la plantilla de daily-triage en una carpeta de prueba y ejecuta doctor antes de activar acciones
**Qué comprobar:** Puedes revisar la configuración y los avisos del diagnóstico
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`

## `mvanhorn`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=guias,reference

**Qué es:** Perfil público de mvanhorn para consultar sus proyectos, herramientas y contribuciones de desarrollo.
**Stack:** Navegador; proyecto de interés
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Consultar el perfil no requiere API; sus proyectos tienen condiciones independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es el README del perfil y un registro de contribuciones; las tecnologías mencionadas no son prestaciones instalables del perfil
- Coste: Sin pago a un modelo en la ruta básica. Consultar el perfil no requiere API; sus proyectos tienen condiciones independientes
- Equipo: Preparación según la ruta elegida. Navegador; proyecto de interés
**Repo:** https://github.com/mvanhorn/mvanhorn

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar herramientas de un autor; Explorar contribuciones a otros proyectos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un proyecto destacado desde el perfil y revisa su README propio antes de considerarlo para instalar
**Qué comprobar:** Puedes distinguir el perfil del repositorio de la herramienta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `last30days-skill`, `ecc`, `deer-flow`

## `nanochat`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=learning,python

**Qué es:** Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible.
**Stack:** uv; Python; CPU o GPU según ruta; presupuesto de cómputo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere API de modelos; entrenar requiere cómputo y el speedrun del autor usa un nodo de ocho H100
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El lema de cien dólares depende del benchmark, hardware y tarifas del autor; no es el coste garantizado de cualquier entrenamiento ni una configuración de portátil
- Coste: El coste depende del proveedor o la ruta. No requiere API de modelos; entrenar requiere cómputo y el speedrun del autor usa un nodo de ocho H100
- Equipo: Preparación según la ruta elegida. uv; Python; CPU o GPU según ruta; presupuesto de cómputo
**Repo:** https://github.com/karpathy/nanochat

**Instalación** [+]:

```
uv sync --extra cpu    # (or) Use for CPU-only / MPS
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una cadena de entrenamiento a chat; Reproducir un experimento con presupuesto delimitado
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prepara la ruta CPU para estudiar el código y lee speedrun antes de contratar un nodo GPU
**Qué comprobar:** Distingues la instalación de dependencias del entrenamiento completo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `llms-from-scratch`, `llm.c`

## `openai-cookbook`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,notebooks,python

**Qué es:** Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales.
**Stack:** Navegador; Python y API key de OpenAI si ejecutas notebooks
**Acceso y costes:**
- API de IA: API de IA opcional. Lectura libre; los ejemplos API requieren cuenta, clave y consumo separado de ChatGPT o Codex
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Es un recetario oficial de API; no es un paquete de plugins ni una promesa de acceso mediante suscripción
- Coste: Consumo de APIs o servicios. Lectura libre; los ejemplos API requieren cuenta, clave y consumo separado de ChatGPT o Codex
- Equipo: Preparación según la ruta elegida. Navegador; Python y API key de OpenAI si ejecutas notebooks
**Repo:** https://github.com/openai/openai-cookbook

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer campos de un texto; Aprender a evaluar respuestas de una aplicación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una receta de salida estructurada y revisa su esquema antes de ejecutar una entrada breve
**Qué comprobar:** Puedes identificar la petición, respuesta esperada y consumo de la receta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openai-python`, `openai-agents-python`, `promptfoo`
**Alternativas (elige una):** `claude-cookbooks`, `awesome-llm-apps`

## `prompt-eng-tutorial`
role=directory · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=learning,prompts,notebooks

**Qué es:** Tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios.
**Stack:** Navegador; cuenta y acceso al modelo para ejecutar ejercicios
**Acceso y costes:**
- API de IA: API de IA opcional. Leer es gratuito; los ejercicios en notebooks o Claude for Sheets pueden requerir API y consumo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Las referencias a Claude 3 Haiku y modelos superiores son históricas del tutorial; consulta disponibilidad actual antes de ejecutar
- Coste: El coste depende del proveedor o la ruta. Leer es gratuito; los ejercicios en notebooks o Claude for Sheets pueden requerir API y consumo
- Equipo: Preparación según la ruta elegida. Navegador; cuenta y acceso al modelo para ejecutar ejercicios
**Repo:** https://github.com/anthropics/prompt-eng-interactive-tutorial

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Practicar instrucciones claras; Aprender a separar datos y órdenes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Completa Basic Prompt Structure y compara una respuesta ambigua con otra que pide un formato concreto
**Qué comprobar:** Puedes reconocer la diferencia entre instrucción y contenido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-cookbooks`, `promptfoo`, `marimo`
**Alternativas (elige una):** `prompt-engineering-guide`

## `prompt-engineering-guide`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,prompts,rag

**Qué es:** Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes.
**Stack:** Navegador; pregunta de ejemplo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La guía pública es consultable sin API; los cursos de Academy y el modelo donde pruebes prompts tienen sus propias condiciones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una referencia y no un programa que se instala; los resultados de un modelo no garantizan el mismo resultado en otro
- Coste: Sin pago a un modelo en la ruta básica. La guía pública es consultable sin API; los cursos de Academy y el modelo donde pruebes prompts tienen sus propias condiciones
- Equipo: Preparación según la ruta elegida. Navegador; pregunta de ejemplo
**Repo:** https://github.com/dair-ai/Prompt-Engineering-Guide

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender a pedir un resumen estructurado; Comparar técnicas de prompting antes de elegir una
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee la sección de ejemplos y reformula una petición de resumen indicando formato y audiencia
**Qué comprobar:** Puedes explicar qué información añadiste y por qué
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `prompt-master`, `context-engineering`, `promptfoo`
**Alternativas (elige una):** `prompt-eng-tutorial`

## `prompt-master`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,prompts

**Qué es:** Skill que recopila contexto y restricciones para redactar prompts destinados a herramientas de código, imagen y otros servicios. La instalación documentada corresponde a Claude; los nombres de otros productos describen destinos de los prompts generados.
**Stack:** Claude con skills o Claude Code; descripción de una tarea
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El skill no trae créditos; lo ejecuta el modelo del anfitrión y los destinos tienen sus propios costes
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Referencia para la herramienta; no es una integración
- Antigravity: Referencia para la herramienta; no es una integración
- Modelos locales: La función básica no necesita un modelo. La instalación documentada es para Claude y Claude Code; Codex y Antigravity aparecen como destinos del prompt generado y no prueban instalación nativa en ellos; cero desperdicio es una afirmación promocional
- Coste: Consumo del agente que ya utilizas. El skill no trae créditos; lo ejecuta el modelo del anfitrión y los destinos tienen sus propios costes
- Equipo: Preparación según la ruta elegida. Claude con skills o Claude Code; descripción de una tarea
**Repo:** https://github.com/nidhinjs/prompt-master

**Instalación** [+]:

```
mkdir -p ~/.claude/skills
git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Redactar un encargo de programación; Preparar un prompt de imagen con requisitos concretos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide al skill que formule preguntas para redactar un prompt de una página de reservas
**Qué comprobar:** El prompt especifica objetivo, contexto, restricciones y criterio de aceptación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `prompt-engineering-guide`, `anthropic-skills`

## `prompts-chat`
role=directory · exec=local · setup=easy · mcp=True · prov=— · tags=prompts,chatbot

**Qué es:** La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable.
**Stack:** Navegador para explorar; Node y cliente MCP si conectas la biblioteca
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Consultar la biblioteca no consume una API de modelos; ejecutar prompts depende del asistente y alojar tu copia tiene costes propios
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Documenta plugin para Claude Code y MCP remoto o local estándar para clientes compatibles; las herramientas de escritura necesitan permisos propios
- Coste: Sin pago a un modelo en la ruta básica. Consultar la biblioteca no consume una API de modelos; ejecutar prompts depende del asistente y alojar tu copia tiene costes propios
- Equipo: Preparación según la ruta elegida. Navegador para explorar; Node y cliente MCP si conectas la biblioteca
**Repo:** https://github.com/f/prompts.chat

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una plantilla para estudiar; Compartir una biblioteca interna de prompts
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Busca un prompt de resumen y adapta sus variables a una nota propia antes de probarlo en tu asistente
**Qué comprobar:** Puedes identificar tarea, datos de entrada y formato esperado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `promptfoo`, `open-webui`
**Alternativas (elige una):** `fabric`

## `python-machine-learning-book`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,data-mining,data-science,logistic-regression,machine-learning,machine-learning-algorithms,neural-network,python

**Qué es:** Código de la primera edición del libro Python Machine Learning, con ejemplos de algoritmos y evaluación.
**Stack:** Python; dependencias correspondientes a la primera edición; datos educativos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El código se consulta libremente; el libro y cómputo tienen condiciones separadas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Este repositorio corresponde a la primera edición de 2015; el autor enlaza ediciones más nuevas y no se debe presentar como entorno actual
- Coste: Sin pago a un modelo en la ruta básica. El código se consulta libremente; el libro y cómputo tienen condiciones separadas
- Equipo: Preparación según la ruta elegida. Python; dependencias correspondientes a la primera edición; datos educativos
**Repo:** https://github.com/rasbt/python-machine-learning-book

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender regresión y clasificación; Entender validación de modelos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre el capítulo de clasificación y compara una predicción con su etiqueta de prueba
**Qué comprobar:** Puedes reconocer el objetivo y la métrica del ejemplo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `llms-from-scratch`, `pytorch`, `awesome-machine-learning`

## `system-prompts-and-models-of-ai-tools`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=prompts,ai,bolt,cluely,copilot,cursor,cursorai,devin

**Qué es:** Colección de prompts y configuraciones atribuidos a herramientas de IA para estudiar sus patrones de diseño.
**Stack:** Navegador; interés en diseño de instrucciones
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Consultar el archivo no usa una API; no entrega acceso a ninguno de los productos mencionados
- Claude Code: Referencia para la herramienta; no es una integración
- Codex: Referencia para la herramienta; no es una integración
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Las atribuciones son del recopilador; listar Claude Code o Codex no equivale a un plugin compatible ni autentica su configuración interna
- Coste: Sin pago a un modelo en la ruta básica. Consultar el archivo no usa una API; no entrega acceso a ninguno de los productos mencionados
- Equipo: Preparación según la ruta elegida. Navegador; interés en diseño de instrucciones
**Repo:** https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar instrucciones de herramientas de código; Preparar una plantilla propia de sistema
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Compara dos estructuras atribuidas a asistentes y anota sus diferencias sin introducirlas como configuración oficial
**Qué comprobar:** Puedes distinguir patrones de diseño de afirmaciones no verificadas de procedencia
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `chatgpt-system-prompt`, `promptfoo`, `claude-code`

## `train-llm-from-scratch`
role=directory · exec=local · setup=heavy · mcp=False · prov=— · tags=aprender,gemini,large-language-models,llm,openai,training,transformers,python

**Qué es:** Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generación.
**Stack:** Python y PyTorch; datos pequeños; CPU o GPU según escala
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige API; GPU, almacenamiento y seguimiento externo opcional tienen sus costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Los extras train, ui, docs y all son alternativas; empezar por un corpus pequeño evita confundir la demostración con entrenar un modelo grande
- Coste: El coste depende del proveedor o la ruta. No exige API; GPU, almacenamiento y seguimiento externo opcional tienen sus costes
- Equipo: Preparación según la ruta elegida. Python y PyTorch; datos pequeños; CPU o GPU según escala
**Repo:** https://github.com/FareedKhan-dev/train-llm-from-scratch

**Instalación** [+]:

```
git clone https://github.com/FareedKhan-dev/train-llm-from-scratch.git
cd train-llm-from-scratch
pip install -e .
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comprender la preparación de un corpus; Explorar un entrenamiento pequeño controlado
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala el paquete en un entorno de prueba y estudia la configuración de un entrenamiento mínimo
**Qué comprobar:** Puedes identificar tamaño del modelo, datos y salida de checkpoints
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `trl`, `nanochat`
