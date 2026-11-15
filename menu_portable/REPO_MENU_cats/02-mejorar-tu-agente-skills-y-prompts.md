# 2. Mejorar tu agente: skills y prompts — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `12-factor-agents`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,learning,prompts,typescript

**Qué es:** Ensayo de Dex Horthy (HumanLayer) que resume lo aprendido construyendo agentes para clientes reales: los productos que funcionan son sobre todo software determinista con pasos de LLM bien colocados. Cada factor (controlar tus prompts, tu ventana de contexto y tu flujo de control, pausar y reanudar, contactar a humanos con tool calls, agentes pequeños) tiene su capítulo con diagramas y ejemplos.
**Stack:** Markdown, TypeScript (ejemplos)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/humanlayer/12-factor-agents

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** vas a construir un agente para clientes reales y quieres principios de diseño antes de elegir framework
**Evita si:** buscas tutoriales con código ejecutable paso a paso; mira `agents-towards-production` o `ai-agents-for-beginners`
**Combina con:** `context-engineering`, `langgraph`, `vercel-ai`

## `500-ai-agents-projects`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=guias,ai-agents,genai,python

**Qué es:** Colección de ideas, casos de uso y ejemplos de agentes de IA para distintos sectores y tareas. Organiza proyectos y enlaces que sirven como punto de partida para prototipos y aprendizaje.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ashishpatel26/500-AI-Agents-Projects

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas ejemplos de aplicaciones de agentes para adaptar a tu propio problema
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `agency-agents`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,prompts,skills,coding-agent

**Qué es:** Plantillas de subagente en Markdown agrupadas por divisiones, como una agencia completa: ingeniería, diseño, paid media, ventas, marketing, producto, testing, seguridad, soporte, finanzas, videojuegos y más. Cada agente define identidad, misión, flujo de trabajo, entregables con ejemplos y métricas de éxito, y hay runbooks que arman equipos para escenarios como un MVP o una campaña.
**Stack:** Markdown, Bash, Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/msitarzewski/agency-agents

**Instalación** [?]: `Seguir la instalación original: https://github.com/msitarzewski/agency-agents/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código
**Evita si:** solo necesitas skills de marketing y growth; mira `marketingskills`
**Combina con:** `marketingskills`, `geo-seo-claude`, `claude-code`
**Alternativas (elige una):** `wshobson-agents`

## `agent-skills`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=skills,coding-agent

**Qué es:** Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. Instala las piezas que necesitas mediante la ruta de tu agente y revisa las dependencias de cada skill.
**Stack:** Markdown, JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/addyosmani/agent-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/addyosmani/agent-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres skills de ingeniería web de calidad para tu agente
**Evita si:** buscas un catálogo enorme de skills de todo tipo; mira `antigravity-awesome-skills`
**Combina con:** `claude-code`, `codex`
**Alternativas (elige una):** `superpowers`

## `agent-toolkit`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=agents,skills,python

**Qué es:** Te da skills listas para tareas comunes, para que tu agente sea productivo desde el primer día.
**Stack:** Markdown/scripts
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/softaworks/agent-toolkit

**Instalación** [?]: `Seguir la instalación original: https://github.com/softaworks/agent-toolkit/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres productividad inmediata con tareas comunes
**Evita si:** buscas un método integral (superpowers)
**Combina con:** `superpowers`

## `agents-towards-production`
role=directory · exec=cloud · setup=medium · mcp=True · prov=openai,local · tags=agents,learning,notebooks,python

**Qué es:** Playbook de Nir Diamant (DiamantAI) con un tutorial por carpeta, en notebooks o scripts listos para ejecutar, sobre cada pieza del stack de un agente: tool calling seguro, datos web, RAG, memoria (Redis, Mem0, Cognee), Docker, FastAPI, GPU, MCP, A2A, LangGraph, seguridad, fine-tuning, trazas y evaluación. Muchos tutoriales los aportan empresas patrocinadoras.
**Stack:** Python, Jupyter, LangGraph, FastAPI, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/NirDiamant/agents-towards-production

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** ya tienes un prototipo de agente y necesitas resolver memoria, despliegue, seguridad u observabilidad
**Evita si:** estás empezando con agentes desde cero; mira `ai-agents-for-beginners`
**Combina con:** `langgraph`, `mem0`, `ollama`

## `ai-agents-for-beginners`
role=directory · exec=cloud · setup=medium · mcp=False · prov=openai,local · tags=agents,learning,notebooks,python

**Qué es:** Recorre desde qué es un agente hasta producción: frameworks, patrones de diseño (uso de herramientas, planificación, multiagente, metacognición), RAG agéntico, protocolos MCP, A2A y NLWeb, context engineering, memoria, agentes que usan el navegador, despliegue, agentes locales y seguridad. Cada lección trae README, video corto y ejemplos en Python.
**Stack:** Python, Jupyter, Microsoft Agent Framework, Microsoft Foundry
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/microsoft/ai-agents-for-beginners

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** estás empezando con agentes y quieres un curso guiado, gratuito y disponible en español
**Evita si:** no quieres depender de Azure o ya llevas agentes a producción; mira `agents-towards-production` o `12-factor-agents`
**Combina con:** `generative-ai-for-beginners`, `agent-framework`, `mcp-for-beginners`

## `ai-engineering-hub`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=guias,agents,ai,llms,machine-learning,mcp,rag,jupyter notebook

**Qué es:** Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificial. Cada carpeta presenta un ejemplo con sus dependencias y configuración propias.
**Stack:** Jupyter Notebook
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/patchy631/ai-engineering-hub

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres aprender implementando ejemplos de ingeniería de IA
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `andrej-karpathy-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,coding-agent

**Qué es:** Ajusta el comportamiento de tu asistente con principios claros, sin atarte a una herramienta concreta.
**Stack:** Markdown (`CLAUDE.md`)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/multica-ai/andrej-karpathy-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres respuestas más útiles ya, sin curar prompts largos
**Evita si:** buscas skills ejecutables con scripts concretos
**Combina con:** `awesome-claude-code`, `context-engineering`

## `anthropic-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=skills,docs,pdf,coding-agent,python

**Qué es:** Repositorio de Anthropic con skills listas para Claude Code, Claude.ai y la API: creativas, técnicas (pruebas de apps web, creación de servidores MCP) y empresariales, más las skills de docx, pptx, xlsx y PDF que Claude usa para generar archivos. Incluye la especificación del estándar Agent Skills y una plantilla para crear las tuyas.
**Stack:** Markdown, YAML, Python, JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/anthropics/skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres skills oficiales de Anthropic o un ejemplo de referencia para escribir las tuyas
**Evita si:** buscas volumen o skills de comunidad para varios agentes; mira `awesome-agent-skills` o `antigravity-awesome-skills`
**Combina con:** `claude-code`, `claude-plugins-official`, `superpowers`

## `antigravity-awesome-skills`
role=skill · exec=hybrid · setup=easy · mcp=True · prov=— · tags=skills,coding-agent,mcp,javascript

**Qué es:** Antes llamada Antigravity Awesome Skills, reúne miles de skills por dominio (desarrollo, seguridad, DevOps, datos, marketing) instalables en Claude Code, Codex, Cursor, Gemini CLI, Kiro, OpenCode y otros agentes. Incluye bundles por rol, plugins temáticos y AAS Core, un MCP local para que el agente busque en el catálogo y elija skills antes de instalarlas.
**Stack:** Markdown, JavaScript (Node.js 22+), Python, MCP
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/sickn33/agentic-awesome-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/sickn33/agentic-awesome-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres cubrir muchos dominios con skills ya escritas y trabajas con uno o varios agentes de código
**Evita si:** prefieres pocas skills oficiales y revisadas; mira `anthropic-skills` o `awesome-agent-skills`
**Combina con:** `skillspector`, `claude-code`, `codex`
**Alternativas (elige una):** `awesome-agent-skills`, `awesome-claude-skills`, `wshobson-agents`

## `arcads-claude-code`
role=skill · exec=cloud · setup=medium · mcp=False · prov=— · tags=video,image,skills,python

**Qué es:** Repo de trabajo que convierte Claude Code o Cursor en un estudio de anuncios: genera videos UGC, presentaciones de producto, lookbooks y miniaturas de YouTube con los modelos de Arcads, y anuncios estáticos para Meta con 37 plantillas. Incluye pipelines multipaso (estilo Pixar o plastilina con ffmpeg), subtitulado con Whisper y HyperFrames, y publicación como anuncios pausados en Meta.
**Stack:** Python, Bash, ffmpeg, Node.js (HyperFrames), Whisper
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo de APIs o servicios. La skill funciona dentro del agente, pero las generaciones consumen la API de Arcads; la suscripción del agente no paga Arcads.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial

**Instalación** [?]: `Seguir la instalación original: https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** ya tienes cuenta de Arcads y quieres producir creatividades publicitarias desde Claude Code o Cursor
**Evita si:** quieres generar video con modelos abiertos sin servicio de pago; mira `comfyui` u `openmontage`
**Combina con:** `hyperframes`, `whisper`, `ffmpeg`, `marketingskills`

## `autoskills`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=catalogos,ruby

**Qué es:** CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia. Inspecciona archivos de configuración y propone o instala skills relacionadas con el stack detectado.
**Stack:** Ruby, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/midudev/autoskills

**Instalación** [+]: `npx autoskills`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres preparar un conjunto de skills adaptado al stack de un proyecto
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones
**Combina con:** `awesome-agent-skills`

## `awesome-agent-skills`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,coding-agent,agents

**Qué es:** Índice mantenido por VoltAgent que enlaza skills publicadas por los equipos de cada producto (Anthropic, Google, Vercel, Stripe, Cloudflare, Supabase, Hugging Face, Trail of Bits...) y una sección de comunidad revisada a mano. Incluye la tabla de carpetas de skills por agente (Claude Code, Codex, Cursor, Gemini CLI, Copilot, OpenCode, Windsurf) y normas de calidad para escribir skills.
**Stack:** Markdown, formato SKILL.md, enlaces a repos de GitHub
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/VoltAgent/awesome-agent-skills

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres skills con procedencia clara, publicadas por el equipo que mantiene cada herramienta
**Evita si:** prefieres instalar un lote grande con un solo comando; mira `antigravity-awesome-skills`
**Combina con:** `skillspector`, `claude-code`, `codex`
**Alternativas (elige una):** `antigravity-awesome-skills`, `awesome-claude-skills`

## `awesome-agents`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=catalogos

**Qué es:** Directorio de herramientas y proyectos abiertos para construir y operar agentes de inteligencia artificial. Agrupa frameworks, agentes y entornos de desarrollo mediante enlaces a sus repositorios.
**Stack:** Recursos y documentación
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/kyrolabs/awesome-agents

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres explorar alternativas de agentes antes de elegir una implementación
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `awesome-claude-code`
role=directory · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=coding-agent,skills,agents

**Qué es:** Índice comunitario del ecosistema de Claude Code organizado por temas: guías de inicio, recursos oficiales de Anthropic, skills, orquestación de agentes, memoria, observabilidad y coste, seguridad, status lines y configuración. Cada entrada incluye una breve valoración del mantenedor.
**Stack:** Markdown, Python (scripts que generan la lista)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/hesreallyhim/awesome-claude-code

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** usas Claude Code a diario y quieres descubrir herramientas y flujos probados por la comunidad
**Evita si:** trabajas con otro agente o solo quieres plugins oficiales; mira `claude-plugins-official` o `awesome-agent-skills`
**Combina con:** `claude-code`, `claude-plugins-official`, `superpowers`
**Alternativas (elige una):** `awesome-claude-skills`

## `awesome-claude-skills`
role=directory · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=skills,automation,coding-agent

**Qué es:** Recopilación de skills por áreas (documentos, desarrollo, datos, marketing, escritura, multimedia, productividad, seguridad) que enlaza skills oficiales de Anthropic y de la comunidad, y aloja algunas propias. Incluye el plugin connect-apps, que usa Composio para que Claude envíe correos, cree issues o publique en Slack.
**Stack:** Markdown, Python, Composio (plugin connect-apps)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ComposioHQ/awesome-claude-skills

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** usas Claude para tareas de negocio además de código y quieres skills ordenadas por área de trabajo
**Evita si:** solo quieres skills de procedencia oficial; mira `anthropic-skills` o `awesome-agent-skills`
**Combina con:** `composio`, `claude-code`, `skillspector`
**Alternativas (elige una):** `awesome-agent-skills`, `antigravity-awesome-skills`, `awesome-claude-code`

## `awesome-copilot`
role=skill · exec=cloud · setup=easy · mcp=True · prov=— · tags=skills,coding-agent,prompts,mcp

**Qué es:** Repositorio de la organización GitHub que reúne personalizaciones de Copilot aportadas por la comunidad: agentes especializados (algunos conectados a servidores MCP), instrucciones que se aplican por tipo de archivo, skills, plugins y un cookbook de recetas para las APIs de Copilot. Tiene web con búsqueda, un Learning Hub y un llms.txt para agentes.
**Stack:** Markdown, YAML, JavaScript (web del catálogo)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/github/awesome-copilot

**Instalación** [?]: `Seguir la instalación original: https://github.com/github/awesome-copilot/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu equipo trabaja con GitHub Copilot en VS Code o Copilot CLI y quiere personalizarlo
**Evita si:** usas Claude Code u otro agente; mira `claude-plugins-official` o `antigravity-awesome-skills`
**Combina con:** `github-mcp-server`, `spec-kit`, `cli`

## `awesome-harness-engineering`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=guias,reference,python

**Qué es:** Directorio de herramientas y patrones para diseñar el entorno, memoria, evaluación y permisos de agentes de IA.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ai-boost/awesome-harness-engineering

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas esta función: Directorio de herramientas y patrones para diseñar el entorno, memoria, evaluación y permisos de agentes de IA.
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta

## `awesome-llm-apps`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google,local · tags=agents,rag,learning,python

**Qué es:** Repositorio de Shubham Saboo con plantillas de código abierto ordenadas por tipo: agentes simples de un solo archivo, agentes avanzados con herramientas y memoria, equipos multiagente, agentes de voz, agentes con MCP, RAG, chat con documentos y webs, fine-tuning y cursos rápidos de Google ADK y OpenAI Agents SDK. Según la app usa OpenAI, Anthropic, Google, xAI, DeepSeek o modelos abiertos.
**Stack:** Python, Streamlit, OpenAI Agents SDK, Google ADK, Agno
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Shubhamsaboo/awesome-llm-apps

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres una plantilla de app con LLM que funcione desde el primer día para adaptarla a tu proyecto
**Evita si:** buscas un curso estructurado con lecciones en orden; mira `ai-agents-for-beginners` o `generative-ai-for-beginners`
**Combina con:** `streamlit`, `openai-agents-python`, `adk-python`, `firecrawl`
**Alternativas (elige una):** `openai-cookbook`, `claude-cookbooks`

## `bmad-method`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=coding-agent,skills,agents

**Qué es:** Organiza el trabajo con IA en roles y documentos (brief, PRD, arquitectura, historias) que el agente de código sigue paso a paso. Útil para proyectos medianos donde los prompts sueltos se pierden.
**Stack:** Markdown, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/bmad-code-org/BMAD-METHOD

**Instalación** [?]: `Seguir la instalación original: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un proceso completo de producto a código con agentes
**Evita si:** prefieres algo ligero centrado en especificaciones; mira `spec-kit`
**Combina con:** `claude-code`, `codex`
**Alternativas (elige una):** `spec-kit`

## `book-to-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=metodologia,skill,python

**Qué es:** Herramientas para convertir un libro técnico en PDF en una skill que un agente pueda consultar durante el trabajo.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/virgiliojr94/book-to-skill

**Instalación** [?]: `Seguir la instalación original: https://github.com/virgiliojr94/book-to-skill/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Herramientas para convertir un libro técnico en PDF en una skill que un agente pueda consultar durante el trabajo.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `chatgpt-dan`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=prompts,chatgpt,gpt-3-5,gpt-4,jailbreak,openai,prompt

**Qué es:** Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones antiguas de ChatGPT. Recopila variantes de instrucciones para estudiar intentos de alterar el comportamiento de asistentes.
**Stack:** Recursos y documentación
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/0xk1h0/ChatGPT_DAN

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres investigar prompts históricos y sus limitaciones
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `chatgpt-system-prompt`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=prompts,gpt,prompt,prompt-engineering,html

**Qué es:** Colección de prompts de GPT y recursos sobre instrucciones de sistema y extracción de prompts. Organiza documentos de referencia para estudiar estructuras de instrucciones y comportamiento de asistentes.
**Stack:** HTML
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/LouisShark/chatgpt_system_prompt

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres comparar patrones de prompts como material de investigación
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `claude-code-hooks-mastery`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=metodologia,reference,python

**Qué es:** Ejemplos y material para aprender a configurar hooks de Claude Code y ejecutar comprobaciones en su flujo de trabajo.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/disler/claude-code-hooks-mastery

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas esta función: Ejemplos y material para aprender a configurar hooks de Claude Code y ejecutar comprobaciones en su flujo de trabajo.
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta

## `claude-cookbooks`
role=directory · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=learning,notebooks,rag,python

**Qué es:** Notebooks y guías de Anthropic con código copiable para construir con Claude: clasificación, resumen, RAG (con Pinecone o embeddings de Voyage AI), tool use y un agente de atención al cliente, visión y extracción de formularios, subagentes, PDFs, salida JSON consistente, moderación, prompt caching y checklists de coste y latencia.
**Stack:** Python, Jupyter, Anthropic SDK, Claude Agent SDK
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/claude-cookbooks

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** construyes sobre la API de Claude y quieres ejemplos oficiales que puedas copiar
**Evita si:** tu app usa la API de OpenAI; mira `openai-cookbook`
**Combina con:** `prompt-eng-tutorial`, `anthropic-skills`, `promptfoo`
**Alternativas (elige una):** `openai-cookbook`, `awesome-llm-apps`

## `claude-plugins-official`
role=skill · exec=cloud · setup=easy · mcp=True · prov=anthropic · tags=skills,coding-agent,mcp

**Qué es:** Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. Cada plugin puede tener requisitos distintos; el marketplace completo no es una aplicación que debas desplegar.
**Stack:** Markdown, JSON, Python, MCP
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/claude-plugins-official

**Instalación** [?]: `Seguir la instalación original: https://github.com/anthropics/claude-plugins-official/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** usas Claude Code y quieres plugins oficiales o de socios que se instalan con un comando
**Evita si:** buscas recursos comunitarios o trabajas con otro agente; mira `awesome-claude-code` o `wshobson-agents`
**Combina con:** `claude-code`, `anthropic-skills`, `awesome-claude-code`
**Alternativas (elige una):** `wshobson-agents`

## `claude-quickstarts`
role=directory · exec=cloud · setup=medium · mcp=False · prov=anthropic · tags=guias,python

**Qué es:** Ejemplos oficiales de Anthropic para construir aplicaciones con Claude, herramientas y uso de computadora. Cada quickstart ofrece una aplicación base con código y pasos de configuración específicos.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/claude-quickstarts

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres partir de un ejemplo oficial al integrar la API de Claude
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `claude-seo`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/AgriciDaniel/claude-seo

**Instalación** [?]: `Seguir la instalación original: https://github.com/AgriciDaniel/claude-seo/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `claude-token-efficient`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=metodologia,python · tools=claude-code

**Qué es:** Instrucciones para reducir la verbosidad de Claude Code y medir el coste de respuestas y contexto. Añade reglas de concisión al contexto del proyecto e incluye perfiles y ejemplos de evaluación.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/drona23/claude-token-efficient

**Instalación** [?]: `Seguir la instalación original: https://github.com/drona23/claude-token-efficient/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres probar respuestas más breves en tareas con mucha salida de texto
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `codex-plugin-cc`
role=skill · exec=cloud · setup=easy · mcp=False · prov=openai · tags=metodologia,javascript · tools=claude-code

**Qué es:** Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas. Añade comandos de revisión y delegación y conecta Claude Code con el runtime de Codex.
**Stack:** JavaScript, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Claude Code aloja el plugin y Codex utiliza su propia cuenta o API key. Cada sesión conserva los límites de su proveedor.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/openai/codex-plugin-cc

**Instalación** [?]: `Seguir la instalación original: https://github.com/openai/codex-plugin-cc/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres revisar código con Codex dentro de tu flujo de Claude Code
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `context-engineering`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,python

**Qué es:** Enseña de forma sistemática qué meter en el prompt y qué dejar fuera para que el modelo responda mejor.
**Stack:** Markdown/notebooks (Python)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/jasontang-ai/Context-Engineering

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres profundizar en contexto y RAG
**Evita si:** buscas skills ejecutables listas para copiar
**Combina con:** `andrej-karpathy-skills`, `headroom`

## `ecc`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=automation,skills,javascript

**Qué es:** Colección de plugins, skills, hooks y convenciones para organizar el trabajo de agentes de código en un proyecto. Se integra con distintos agentes mediante rutas de instalación específicas; no es una plataforma de modelos locales.
**Stack:** Rust (core), TypeScript, Python, Go
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/affaan-m/ECC

**Instalación** [?]: `Seguir la instalación original: https://github.com/affaan-m/ECC/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** ejecutas agentes con acceso real a tu máquina y necesitas contención
**Evita si:** solo haces prompts de chat sin ejecución de código
**Combina con:** `openhands`, `sandbox`, `hermes-agent`

## `elephant-goldfish-model`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=metodologia,skill,python

**Qué es:** Plugin con instrucciones para diseñar y revisar software con agentes mediante contextos y perspectivas complementarias.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/google/elephant-goldfish-model

**Instalación** [?]: `Seguir la instalación original: https://github.com/google/elephant-goldfish-model/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plugin con instrucciones para diseñar y revisar software con agentes mediante contextos y perspectivas complementarias.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `fabric`
role=app · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,local · tags=prompts,automation,go

**Qué es:** Organiza prompts reutilizables (patterns) para tareas como resumir videos, extraer ideas o analizar textos. Se encadena con pipes en la terminal.
**Stack:** Go, Markdown
**Acceso y costes:**
- API de IA: API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. El proyecto documenta un backend de OAuth de Codex; es una integración del proyecto, no una garantía general para otras apps.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/danielmiessler/Fabric

**Instalación** [?]: `Seguir la instalación original: https://github.com/danielmiessler/Fabric/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres prompts reutilizables desde la terminal
**Evita si:** buscas solo una lista de prompts para copiar; mira `prompts-chat`
**Combina con:** `ollama`, `yt-dlp`
**Alternativas (elige una):** `prompts-chat`

## `financial-services`
role=skill · exec=cloud · setup=medium · mcp=False · prov=anthropic · tags=dominio,python

**Qué es:** Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros. Reúne instrucciones y conectores para tareas como análisis de empresas y gestión de documentos financieros.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/financial-services

**Instalación** [?]: `Seguir la instalación original: https://github.com/anthropics/financial-services/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar flujos financieros dentro del ecosistema de Claude
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones
**Combina con:** `claude-code`

## `gemini-skills`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=google · tags=catalogos,gemini,gemini-api,skills,python

**Qué es:** Skills oficiales de Google para ayudar a agentes a trabajar con la API, los SDK y los modelos de Gemini. Añaden instrucciones y referencias sobre las interacciones y patrones de desarrollo de Gemini.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/google-gemini/gemini-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/google-gemini/gemini-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** construyes aplicaciones que llaman a Gemini y necesitas contexto actualizado para el agente
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `generative-ai-for-beginners`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,prompts,python

**Qué es:** Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa. Leer el curso no requiere una API; ejecutar cada práctica puede requerir servicios o modelos específicos.
**Stack:** Python, TypeScript, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/microsoft/generative-ai-for-beginners

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres un curso estructurado y gratuito para empezar
**Evita si:** ya construyes con LLM y buscas recetas concretas; mira `openai-cookbook`
**Combina con:** `ai-agents-for-beginners`, `mcp-for-beginners`
**Alternativas (elige una):** `llm-course`

## `geo-seo-claude`
role=skill · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=skills,search,pdf,python

**Qué es:** Añade a Claude Code comandos `/geo` que auditan un sitio para buscadores con IA (ChatGPT, Claude, Perplexity, Gemini, AI Overviews) sin dejar el SEO técnico: citabilidad del contenido, acceso de crawlers de IA en robots.txt, menciones de marca, datos estructurados y llms.txt. Genera informes para clientes en Markdown o PDF y lleva un pequeño CRM de prospectos.
**Stack:** Python, Markdown, ReportLab, JSON-LD, Playwright (opcional)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/zubair-trabzada/geo-seo-claude

**Instalación** [?]: `Seguir la instalación original: https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres medir y mejorar cómo te citan los buscadores con IA, no solo tu posición en Google
**Evita si:** solo haces SEO clásico o no usas Claude Code; mira `marketingskills`
**Combina con:** `marketingskills`, `agency-agents`, `playwright`

## `google-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=catalogos,skill,python

**Qué es:** Colección de skills para trabajar con productos y tecnologías de Google desde agentes de programación compatibles.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/google/skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/google/skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Colección de skills para trabajar con productos y tecnologías de Google desde agentes de programación compatibles.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `grok-plugin-claude-code`
role=skill · exec=cloud · setup=easy · mcp=False · prov=xai · tags=metodologia,ai-agents,claude-code,grok,grok-cli,plugin,xai,javascript · tools=claude-code

**Qué es:** Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar. Envuelve el modo no interactivo de Grok CLI para ejecutar encargos y recuperar sus resultados.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/zachdunn/grok-plugin-claude-code

**Instalación** [?]: `Seguir la instalación original: https://github.com/zachdunn/grok-plugin-claude-code/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** usas Claude Code y quieres consultar Grok dentro de ese flujo
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `gstack`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=metodologia,skill,typescript

**Qué es:** Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude Code.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/garrytan/gstack

**Instalación** [?]: `Seguir la instalación original: https://github.com/garrytan/gstack/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude Code.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `humanizer`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,prompts,docs

**Qué es:** Detecta 26 patrones típicos de la prosa de LLM (contrastes tipo 'no es X, es Y', cierres dramáticos, tríadas forzadas, frases de falsa profundidad, importancia inflada) y reescribe el texto sin cambiar lo que dice. Puede imitar tu estilo si le das una muestra y, sobre un archivo, solo toca la prosa: no el código, los datos ni el frontmatter.
**Stack:** Markdown, SKILL.md
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/blader/humanizer

**Instalación** [?]: `Seguir la instalación original: https://github.com/blader/humanizer/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** publicas textos redactados con IA y quieres que se lean como escritos por una persona
**Evita si:** quieres reglas de estilo cortas para pegar en un system prompt, con rúbrica propia; mira `stop-slop`
**Combina con:** `marketingskills`, `claude-code`, `codex`
**Alternativas (elige una):** `stop-slop`

## `i-have-adhd`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=escritura,skill,python

**Qué es:** Skill para que un agente presente primero la respuesta y organice su salida con menos distracciones y rodeos.
**Stack:** Python, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ayghri/i-have-adhd

**Instalación** [?]: `Seguir la instalación original: https://github.com/ayghri/i-have-adhd/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para que un agente presente primero la respuesta y organice su salida con menos distracciones y rodeos.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `instagram-agent-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de Instagram.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Jakeschincariol/instagram-agent-skill

**Instalación** [?]: `Seguir la instalación original: https://github.com/Jakeschincariol/instagram-agent-skill/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de Instagram.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `linkedin-agent-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de LinkedIn.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Jakeschincariol/linkedin-agent-skill

**Instalación** [?]: `Seguir la instalación original: https://github.com/Jakeschincariol/linkedin-agent-skill/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de LinkedIn.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `loop-engineering`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=coding-agent,skills,typescript

**Qué es:** Propone dejar de escribir prompts aislados y diseñar ciclos con objetivo, verificación y puntuación para que el agente itere solo. Incluye starters y herramientas de línea de comandos.
**Stack:** TypeScript, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/cobusgreyling/loop-engineering

**Instalación** [?]: `Seguir la instalación original: https://github.com/cobusgreyling/loop-engineering/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres que tu agente de código itere solo con criterios medibles
**Evita si:** solo necesitas una lista de skills; mira `awesome-agent-skills`
**Combina con:** `claude-code`, `codex`, `superpowers`

## `marketingskills`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,analytics,email,search

**Qué es:** Skills de Corey Haines para marketers técnicos y founders que trabajan con agentes de código: conversión, copywriting, SEO y SEO para IA, anuncios, emails, analítica y atribución, pricing, lanzamientos, retención y ventas. La skill product-marketing guarda el contexto de tu producto y las demás la consultan antes de actuar.
**Stack:** Markdown, SKILL.md, JavaScript (scripts del repo)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/coreyhaines31/marketingskills

**Instalación** [+]: `npx skills add coreyhaines31/marketingskills`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** eres founder o marketer técnico y quieres que tu agente de código haga trabajo de growth con marcos probados
**Evita si:** necesitas una herramienta que envíe campañas o mida resultados; mira `mautic`, `listmonk` o `posthog`
**Combina con:** `agency-agents`, `geo-seo-claude`, `mautic`, `posthog`

## `minimalist-entrepreneur-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,reference

**Qué es:** Skills basadas en ideas de The Minimalist Entrepreneur para orientar trabajo de negocio y emprendimiento con un agente.
**Stack:** —
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/slavingia/skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/slavingia/skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills basadas en ideas de The Minimalist Entrepreneur para orientar trabajo de negocio y emprendimiento con un agente.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `mvanhorn`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=guias,reference

**Qué es:** Perfil público de mvanhorn para consultar sus proyectos, herramientas y contribuciones de desarrollo.
**Stack:** —
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/mvanhorn/mvanhorn

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas esta función: Perfil público de mvanhorn para consultar sus proyectos, herramientas y contribuciones de desarrollo.
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta

## `no-ai-slop`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=escritura,skill,python

**Qué es:** Skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con IA.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/petergyang/no-ai-slop

**Instalación** [?]: `Seguir la instalación original: https://github.com/petergyang/no-ai-slop/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con IA.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `openai-cookbook`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,notebooks,python

**Qué es:** Reúne recetas sobre embeddings, function calling, RAG, evaluación, agentes y voz. Sirve como referencia práctica al construir con la API de OpenAI.
**Stack:** Python, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/openai/openai-cookbook

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** construyes sobre la API de OpenAI y quieres ejemplos oficiales
**Evita si:** usas Claude como modelo principal; mira `claude-cookbooks`
**Combina con:** `openai-python`, `openai-agents-python`
**Alternativas (elige una):** `claude-cookbooks`, `awesome-llm-apps`

## `plugins`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=catalogos,reference,typescript

**Qué es:** Especificación y colección oficial de plugins de Cursor para estudiar e instalar extensiones de ese agente.
**Stack:** TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/cursor/plugins

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas esta función: Especificación y colección oficial de plugins de Cursor para estudiar e instalar extensiones de ese agente.
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta

## `ponytail`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=skills,coding-agent

**Qué es:** Empuja al agente a reutilizar, borrar y simplificar antes de añadir código nuevo. Reduce soluciones infladas y cambios innecesarios.
**Stack:** Markdown, JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/DietrichGebert/ponytail

**Instalación** [?]: `Seguir la instalación original: https://github.com/DietrichGebert/ponytail/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu agente tiende a sobrecomplicar las soluciones
**Evita si:** necesitas una metodología completa de proyecto; mira `bmad-method`
**Combina con:** `claude-code`, `superpowers`, `andrej-karpathy-skills`

## `prompt-eng-tutorial`
role=directory · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=learning,prompts,notebooks

**Qué es:** Nueve capítulos con ejercicios sobre claridad, roles, ejemplos, razonamiento paso a paso y cómo evitar alucinaciones. Cada lección se practica contra la API de Claude.
**Stack:** Python, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/prompt-eng-interactive-tutorial

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres aprender prompts con práctica guiada
**Evita si:** buscas una guía amplia multi-modelo; mira `prompt-engineering-guide`
**Combina con:** `claude-cookbooks`
**Alternativas (elige una):** `prompt-engineering-guide`

## `prompt-engineering-guide`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,prompts,rag

**Qué es:** Explica técnicas de prompting, riesgos y aplicaciones con ejemplos y referencias a papers. Disponible en varios idiomas, incluido el español.
**Stack:** MDX, Next.js, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/dair-ai/Prompt-Engineering-Guide

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres una referencia amplia de técnicas de prompting
**Evita si:** prefieres ejercicios prácticos con corrección; mira `prompt-eng-tutorial`
**Combina con:** `context-engineering`
**Alternativas (elige una):** `prompt-eng-tutorial`

## `prompt-master`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,prompts

**Qué es:** Te ayuda a escribir mejores prompts con meta-prompting reutilizable, como una capa por encima de cualquier IA.
**Stack:** Markdown/skill
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/nidhinjs/prompt-master

**Instalación** [?]: `Seguir la instalación original: https://github.com/nidhinjs/prompt-master/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres dejar de re-promptear y acertar antes
**Evita si:** ya tienes prompts afinados y estables
**Combina con:** `andrej-karpathy-skills`

## `prompts-chat`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=prompts,chatbot

**Qué es:** Reúne miles de prompts de rol y tarea para ChatGPT, Claude y otros, con buscador web. Puedes desplegar tu propia copia para tu organización.
**Stack:** Next.js, TypeScript, CSV
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/f/prompts.chat

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas prompts listos para copiar
**Evita si:** quieres ejecutarlos como comandos encadenables; mira `fabric`
**Alternativas (elige una):** `fabric`

## `scientific-agent-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas de dominio.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/K-Dense-AI/scientific-agent-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas de dominio.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `security-audit-skill`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=— · tags=metodologia,javascript

**Qué es:** Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estructurados. Divide la revisión en reconocimiento, búsqueda por cobertura y verificación de candidatos antes del informe.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/cloudflare/security-audit-skill

**Instalación** [?]: `Seguir la instalación original: https://github.com/cloudflare/security-audit-skill/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un proceso reproducible de revisión de seguridad con agentes
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones
**Combina con:** `codex`

## `skills`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,coding-agent

**Qué es:** Muestra cómo se escribe una buena skill para agentes, con pocos ejemplos pero de alta calidad para usarlos como plantilla.
**Stack:** Markdown/TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mattpocock/skills

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas referencias limpias y didácticas
**Evita si:** quieres un catálogo masivo (antigravity-awesome-skills)
**Combina con:** `awesome-agent-skills`

## `skillspector`
role=app · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,coding-agent,python

**Qué es:** Resuelve el riesgo de ejecutar skills de terceros sin revisión.
**Stack:** Python/Node, Docker
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo de APIs o servicios. El escaneo con LLM documenta proveedores con API key. Una propuesta de añadir Ollama no demuestra soporte local implementado.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/NVIDIA/SkillSpector

**Instalación** [?]: `Seguir la instalación original: https://github.com/NVIDIA/SkillSpector/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** instalas skills externas o curas catálogos
**Evita si:** solo usas skills propias de confianza
**Combina con:** `antigravity-awesome-skills`

## `social-media-research-skills`
role=skill · exec=cloud · setup=medium · mcp=False · prov=— · tags=dominio,agent-skills,ai-agents,claude-code,claude-skills,competitor-analysis,content-marketing,cursor · tools=claude-code,codex

**Qué es:** Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators. Guía al agente por flujos de investigación que consultan datos sociales y producen informes de negocio.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La clave exigida es de un servicio externo. No es una API de un modelo de lenguaje; el agente o aplicación que use sus datos tiene su propio acceso a IA.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo de APIs o servicios. El modelo lo aporta tu agente; las consultas de datos requieren acceso a ScrapeCreators por separado.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ScrapeCreators/social-media-research-skills

**Instalación** [+]: `npx skills add ScrapeCreators/social-media-research-skills`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres investigación de contenido social desde un agente compatible con Agent Skills
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones
**Alternativas (elige una):** `last30days-skill`

## `spec-kit`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=coding-agent,skills,python

**Qué es:** Te guía para escribir especificación, plan y tareas antes de que el agente programe. Funciona con Copilot, Claude Code, Gemini CLI y otros.
**Stack:** Python, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/github/spec-kit

**Instalación** [?]: `Seguir la instalación original: https://github.com/github/spec-kit/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres que el agente siga una especificación antes de programar
**Evita si:** buscas roles completos de equipo ágil; mira `bmad-method`
**Combina con:** `claude-code`, `codex`, `gemini-cli`
**Alternativas (elige una):** `bmad-method`

## `stop-slop`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,prompts,docs

**Qué es:** Un SKILL.md con tres archivos de referencia (frases a eliminar, estructuras a evitar y ejemplos antes/después) que enseña a Claude o a cualquier LLM a quitar muletillas, contrastes binarios, fragmentos dramáticos, voz pasiva y otros patrones predecibles. Cierra con una rúbrica de cinco dimensiones para decidir si el texto necesita otra vuelta.
**Stack:** Markdown, SKILL.md
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/hardikpandya/stop-slop

**Instalación** [?]: `Seguir la instalación original: https://github.com/hardikpandya/stop-slop/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt
**Evita si:** prefieres una skill que reescriba mostrando su proceso y pueda imitar tu voz; mira `humanizer`
**Combina con:** `marketingskills`, `claude-code`
**Alternativas (elige una):** `humanizer`

## `superclaude-framework`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=— · tags=metodologia,python · tools=claude-code

**Qué es:** Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code. Instala instrucciones y componentes de flujo para organizar fases del desarrollo asistido.
**Stack:** Python, pyproject.toml, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/SuperClaude-Org/SuperClaude_Framework

**Instalación** [+]: `pipx install superclaude`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres estructurar el trabajo de Claude Code con comandos y convenciones
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `superpowers`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,coding-agent

**Qué es:** Le da a tu agente de código un método de trabajo completo y coherente (planear, probar, revisar), no piezas sueltas.
**Stack:** Markdown/skills
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/obra/superpowers

**Instalación** [?]: `Seguir la instalación original: https://github.com/obra/superpowers/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres método, no fragmentos sueltos
**Evita si:** solo necesitas una skill aislada puntual
**Combina con:** `awesome-claude-code`, `agent-toolkit`
**Alternativas (elige una):** `agent-skills`

## `system-prompts-and-models-of-ai-tools`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=prompts,ai,bolt,cluely,copilot,cursor,cursorai,devin

**Qué es:** Colección de prompts y configuraciones atribuidos a herramientas de IA para estudiar sus patrones de diseño. Organiza archivos por herramienta para consultar y comparar instrucciones y formatos.
**Stack:** Recursos y documentación
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres investigar patrones de prompts utilizados por asistentes
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `wshobson-agents`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,coding-agent,agents,python

**Qué es:** Colección de Seth Hobson que agrupa subagentes especialistas, skills y comandos en plugins por área: desarrollo Python y JavaScript, revisión de código, testing, infraestructura, seguridad y más. Se escribe una sola vez en formato de plugin de Claude Code y unos adaptadores generan las versiones para Codex, Cursor, OpenCode, Antigravity CLI, GitHub Copilot y Pi.
**Stack:** Markdown, Python (uv), Make
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/wshobson/agents

**Instalación** [?]: `Seguir la instalación original: https://github.com/wshobson/agents/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres subagentes y comandos especializados por lenguaje o área, instalables plugin a plugin
**Evita si:** solo quieres plugins oficiales de Anthropic y socios; mira `claude-plugins-official`
**Combina con:** `claude-code`, `codex`, `skillspector`
**Alternativas (elige una):** `claude-plugins-official`, `antigravity-awesome-skills`, `agency-agents`
