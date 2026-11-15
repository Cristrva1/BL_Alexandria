# 2. Skills, Prompts & Guías de Agente — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `12-factor-agents`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Ensayo de Dex Horthy (HumanLayer) que resume lo aprendido construyendo agentes para clientes reales: los productos que funcionan son sobre todo software determinista con pasos de LLM bien colocados. Cada factor (controlar tus prompts, tu ventana de contexto y tu flujo de control, pausar y reanudar, contactar a humanos con tool calls, agentes pequeños) tiene su capítulo con diagramas y ejemplos.
**Stack:** Markdown, TypeScript (ejemplos)
**Repo:** https://github.com/humanlayer/12-factor-agents

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/12-Factor Agents/). Si necesitas el código: git clone https://github.com/humanlayer/12-factor-agents`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** vas a construir un agente para clientes reales y quieres principios de diseño antes de elegir framework
**Evita si:** buscas tutoriales con código ejecutable paso a paso; mira `agents-towards-production` o `ai-agents-for-beginners`
**Combina con:** `context-engineering`, `langgraph`, `vercel-ai`

## `agency-agents`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Plantillas de subagente en Markdown agrupadas por divisiones, como una agencia completa: ingeniería, diseño, paid media, ventas, marketing, producto, testing, seguridad, soporte, finanzas, videojuegos y más. Cada agente define identidad, misión, flujo de trabajo, entregables con ejemplos y métricas de éxito, y hay runbooks que arman equipos para escenarios como un MVP o una campaña.
**Stack:** Markdown, Bash, Python
**Repo:** https://github.com/msitarzewski/agency-agents

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/The Agency (agency-agents)/). Si necesitas el código: git clone https://github.com/msitarzewski/agency-agents`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código
**Evita si:** solo necesitas skills de marketing y growth; mira `marketingskills`
**Combina con:** `marketingskills`, `geo-seo-claude`, `claude-code`
**Alternativas (elige una):** `wshobson-agents`

## `agent-skills`
role=skill · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Skills listas para Claude Code, Codex y otros agentes que cubren pruebas, rendimiento, accesibilidad, revisión de código y buenas prácticas web. Pensadas para que el agente trabaje como un ingeniero senior.
**Stack:** Markdown, JavaScript
**Repo:** https://github.com/addyosmani/agent-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Agent Skills (Addy Osmani)/). Si necesitas el código: git clone https://github.com/addyosmani/agent-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres skills de ingeniería web de calidad para tu agente
**Evita si:** buscas un catálogo enorme de skills de todo tipo; mira `antigravity-awesome-skills`
**Combina con:** `claude-code`, `codex`
**Alternativas (elige una):** `superpowers`

## `agent-toolkit`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Te da skills listas para tareas comunes, para que tu agente sea productivo desde el primer día.
**Stack:** Markdown/scripts
**Repo:** https://github.com/softaworks/agent-toolkit

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/agent-toolkit/). Si necesitas el código: git clone https://github.com/softaworks/agent-toolkit`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres productividad inmediata con tareas comunes
**Evita si:** buscas un método integral (superpowers)
**Combina con:** `superpowers`

## `agents-towards-production`
role=directory · exec=cloud · setup=medium · mcp=True · prov=['openai', 'local']

**Qué es:** Playbook de Nir Diamant (DiamantAI) con un tutorial por carpeta, en notebooks o scripts listos para ejecutar, sobre cada pieza del stack de un agente: tool calling seguro, datos web, RAG, memoria (Redis, Mem0, Cognee), Docker, FastAPI, GPU, MCP, A2A, LangGraph, seguridad, fine-tuning, trazas y evaluación. Muchos tutoriales los aportan empresas patrocinadoras.
**Stack:** Python, Jupyter, LangGraph, FastAPI, Docker
**Repo:** https://github.com/NirDiamant/agents-towards-production

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Agents Towards Production/). Si necesitas el código: git clone https://github.com/NirDiamant/agents-towards-production`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** ya tienes un prototipo de agente y necesitas resolver memoria, despliegue, seguridad u observabilidad
**Evita si:** estás empezando con agentes desde cero; mira `ai-agents-for-beginners`
**Combina con:** `langgraph`, `mem0`, `ollama`

## `ai-agents-for-beginners`
role=directory · exec=cloud · setup=medium · mcp=False · prov=['openai', 'local']

**Qué es:** Recorre desde qué es un agente hasta producción: frameworks, patrones de diseño (uso de herramientas, planificación, multiagente, metacognición), RAG agéntico, protocolos MCP, A2A y NLWeb, context engineering, memoria, agentes que usan el navegador, despliegue, agentes locales y seguridad. Cada lección trae README, video corto y ejemplos en Python.
**Stack:** Python, Jupyter, Microsoft Agent Framework, Microsoft Foundry
**Repo:** https://github.com/microsoft/ai-agents-for-beginners

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/AI Agents for Beginners/). Si necesitas el código: git clone https://github.com/microsoft/ai-agents-for-beginners`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** estás empezando con agentes y quieres un curso guiado, gratuito y disponible en español
**Evita si:** no quieres depender de Azure o ya llevas agentes a producción; mira `agents-towards-production` o `12-factor-agents`
**Combina con:** `generative-ai-for-beginners`, `agent-framework`, `mcp-for-beginners`

## `andrej-karpathy-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Ajusta el comportamiento de tu asistente con principios claros, sin atarte a una herramienta concreta.
**Stack:** Markdown (`CLAUDE.md`)
**Repo:** https://github.com/multica-ai/andrej-karpathy-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/andrej-karpathy-skills/). Si necesitas el código: git clone https://github.com/multica-ai/andrej-karpathy-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres respuestas más útiles ya, sin curar prompts largos
**Evita si:** buscas skills ejecutables con scripts concretos
**Combina con:** `awesome-claude-code`, `context-engineering`

## `anthropic-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** Repositorio de Anthropic con skills listas para Claude Code, Claude.ai y la API: creativas, técnicas (pruebas de apps web, creación de servidores MCP) y empresariales, más las skills de docx, pptx, xlsx y PDF que Claude usa para generar archivos. Incluye la especificación del estándar Agent Skills y una plantilla para crear las tuyas.
**Stack:** Markdown, YAML, Python, JavaScript
**Repo:** https://github.com/anthropics/skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Anthropic Skills/). Si necesitas el código: git clone https://github.com/anthropics/skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres skills oficiales de Anthropic o un ejemplo de referencia para escribir las tuyas
**Evita si:** buscas volumen o skills de comunidad para varios agentes; mira `awesome-agent-skills` o `antigravity-awesome-skills`
**Combina con:** `claude-code`, `claude-plugins-official`, `superpowers`

## `antigravity-awesome-skills`
role=skill · exec=hybrid · setup=easy · mcp=True · prov=—

**Qué es:** Antes llamada Antigravity Awesome Skills, reúne miles de skills por dominio (desarrollo, seguridad, DevOps, datos, marketing) instalables en Claude Code, Codex, Cursor, Gemini CLI, Kiro, OpenCode y otros agentes. Incluye bundles por rol, plugins temáticos y AAS Core, un MCP local para que el agente busque en el catálogo y elija skills antes de instalarlas.
**Stack:** Markdown, JavaScript (Node.js 22+), Python, MCP
**Repo:** https://github.com/sickn33/agentic-awesome-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Agentic Awesome Skills/). Si necesitas el código: git clone https://github.com/sickn33/agentic-awesome-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres cubrir muchos dominios con skills ya escritas y trabajas con uno o varios agentes de código
**Evita si:** prefieres pocas skills oficiales y revisadas; mira `anthropic-skills` o `awesome-agent-skills`
**Combina con:** `skillspector`, `claude-code`, `codex`
**Alternativas (elige una):** `awesome-agent-skills`, `awesome-claude-skills`, `wshobson-agents`

## `arcads-claude-code`
role=skill · exec=cloud · setup=medium · mcp=False · prov=—

**Qué es:** Repo de trabajo que convierte Claude Code o Cursor en un estudio de anuncios: genera videos UGC, presentaciones de producto, lookbooks y miniaturas de YouTube con los modelos de Arcads, y anuncios estáticos para Meta con 37 plantillas. Incluye pipelines multipaso (estilo Pixar o plastilina con ffmpeg), subtitulado con Whisper y HyperFrames, y publicación como anuncios pausados en Meta.
**Stack:** Python, Bash, ffmpeg, Node.js (HyperFrames), Whisper
**Repo:** https://github.com/krusemediallc/arcads-claude-code

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Arcads AI Video Skill Pack/). Si necesitas el código: git clone https://github.com/krusemediallc/arcads-claude-code`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** ya tienes cuenta de Arcads y quieres producir creatividades publicitarias desde Claude Code o Cursor
**Evita si:** quieres generar video con modelos abiertos sin servicio de pago; mira `comfyui` u `openmontage`
**Combina con:** `hyperframes`, `whisper`, `ffmpeg`, `marketingskills`

## `awesome-agent-skills`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Índice mantenido por VoltAgent que enlaza skills publicadas por los equipos de cada producto (Anthropic, Google, Vercel, Stripe, Cloudflare, Supabase, Hugging Face, Trail of Bits...) y una sección de comunidad revisada a mano. Incluye la tabla de carpetas de skills por agente (Claude Code, Codex, Cursor, Gemini CLI, Copilot, OpenCode, Windsurf) y normas de calidad para escribir skills.
**Stack:** Markdown, formato SKILL.md, enlaces a repos de GitHub
**Repo:** https://github.com/VoltAgent/awesome-agent-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Awesome Agent Skills/). Si necesitas el código: git clone https://github.com/VoltAgent/awesome-agent-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres skills con procedencia clara, publicadas por el equipo que mantiene cada herramienta
**Evita si:** prefieres instalar un lote grande con un solo comando; mira `antigravity-awesome-skills`
**Combina con:** `skillspector`, `claude-code`, `codex`
**Alternativas (elige una):** `antigravity-awesome-skills`, `awesome-claude-skills`

## `awesome-claude-code`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** Índice comunitario del ecosistema de Claude Code organizado por temas: guías de inicio, recursos oficiales de Anthropic, skills, orquestación de agentes, memoria, observabilidad y coste, seguridad, status lines y configuración. Cada entrada incluye una breve valoración del mantenedor.
**Stack:** Markdown, Python (scripts que generan la lista)
**Repo:** https://github.com/hesreallyhim/awesome-claude-code

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Awesome Claude Code/). Si necesitas el código: git clone https://github.com/hesreallyhim/awesome-claude-code`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** usas Claude Code a diario y quieres descubrir herramientas y flujos probados por la comunidad
**Evita si:** trabajas con otro agente o solo quieres plugins oficiales; mira `claude-plugins-official` o `awesome-agent-skills`
**Combina con:** `claude-code`, `claude-plugins-official`, `superpowers`
**Alternativas (elige una):** `awesome-claude-skills`

## `awesome-claude-skills`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** Recopilación de skills por áreas (documentos, desarrollo, datos, marketing, escritura, multimedia, productividad, seguridad) que enlaza skills oficiales de Anthropic y de la comunidad, y aloja algunas propias. Incluye el plugin connect-apps, que usa Composio para que Claude envíe correos, cree issues o publique en Slack.
**Stack:** Markdown, Python, Composio (plugin connect-apps)
**Repo:** https://github.com/ComposioHQ/awesome-claude-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Awesome Claude Skills/). Si necesitas el código: git clone https://github.com/ComposioHQ/awesome-claude-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** usas Claude para tareas de negocio además de código y quieres skills ordenadas por área de trabajo
**Evita si:** solo quieres skills de procedencia oficial; mira `anthropic-skills` o `awesome-agent-skills`
**Combina con:** `composio`, `claude-code`, `skillspector`
**Alternativas (elige una):** `awesome-agent-skills`, `antigravity-awesome-skills`, `awesome-claude-code`

## `awesome-copilot`
role=skill · exec=cloud · setup=easy · mcp=True · prov=—

**Qué es:** Repositorio de la organización GitHub que reúne personalizaciones de Copilot aportadas por la comunidad: agentes especializados (algunos conectados a servidores MCP), instrucciones que se aplican por tipo de archivo, skills, plugins y un cookbook de recetas para las APIs de Copilot. Tiene web con búsqueda, un Learning Hub y un llms.txt para agentes.
**Stack:** Markdown, YAML, JavaScript (web del catálogo)
**Repo:** https://github.com/github/awesome-copilot

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Awesome GitHub Copilot/). Si necesitas el código: git clone https://github.com/github/awesome-copilot`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** tu equipo trabaja con GitHub Copilot en VS Code o Copilot CLI y quiere personalizarlo
**Evita si:** usas Claude Code u otro agente; mira `claude-plugins-official` o `antigravity-awesome-skills`
**Combina con:** `github-mcp-server`, `spec-kit`, `cli`

## `awesome-llm-apps`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Repositorio de Shubham Saboo con plantillas de código abierto ordenadas por tipo: agentes simples de un solo archivo, agentes avanzados con herramientas y memoria, equipos multiagente, agentes de voz, agentes con MCP, RAG, chat con documentos y webs, fine-tuning y cursos rápidos de Google ADK y OpenAI Agents SDK. Según la app usa OpenAI, Anthropic, Google, xAI, DeepSeek o modelos abiertos.
**Stack:** Python, Streamlit, OpenAI Agents SDK, Google ADK, Agno
**Repo:** https://github.com/Shubhamsaboo/awesome-llm-apps

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Awesome LLM Apps/). Si necesitas el código: git clone https://github.com/Shubhamsaboo/awesome-llm-apps`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres una plantilla de app con LLM que funcione desde el primer día para adaptarla a tu proyecto
**Evita si:** buscas un curso estructurado con lecciones en orden; mira `ai-agents-for-beginners` o `generative-ai-for-beginners`
**Combina con:** `streamlit`, `openai-agents-python`, `adk-python`, `firecrawl`
**Alternativas (elige una):** `openai-cookbook`, `claude-cookbooks`

## `bmad-method`
role=skill · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Organiza el trabajo con IA en roles y documentos (brief, PRD, arquitectura, historias) que el agente de código sigue paso a paso. Útil para proyectos medianos donde los prompts sueltos se pierden.
**Stack:** Markdown, Node.js
**Repo:** https://github.com/bmad-code-org/BMAD-METHOD

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/BMAD Method/). Si necesitas el código: git clone https://github.com/bmad-code-org/BMAD-METHOD`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres un proceso completo de producto a código con agentes
**Evita si:** prefieres algo ligero centrado en especificaciones; mira `spec-kit`
**Combina con:** `claude-code`, `codex`
**Alternativas (elige una):** `spec-kit`

## `claude-cookbooks`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** Notebooks y guías de Anthropic con código copiable para construir con Claude: clasificación, resumen, RAG (con Pinecone o embeddings de Voyage AI), tool use y un agente de atención al cliente, visión y extracción de formularios, subagentes, PDFs, salida JSON consistente, moderación, prompt caching y checklists de coste y latencia.
**Stack:** Python, Jupyter, Anthropic SDK, Claude Agent SDK
**Repo:** https://github.com/anthropics/claude-cookbooks

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Claude Cookbooks/). Si necesitas el código: git clone https://github.com/anthropics/claude-cookbooks`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** construyes sobre la API de Claude y quieres ejemplos oficiales que puedas copiar
**Evita si:** tu app usa la API de OpenAI; mira `openai-cookbook`
**Combina con:** `prompt-eng-tutorial`, `anthropic-skills`, `promptfoo`
**Alternativas (elige una):** `openai-cookbook`, `awesome-llm-apps`

## `claude-plugins-official`
role=skill · exec=cloud · setup=easy · mcp=True · prov=['anthropic']

**Qué es:** Directorio curado desde el que Claude Code instala plugins de forma nativa. En `/plugins` están los que mantiene Anthropic (revisión de código y PR, desarrollo de features, diseño frontend, hooks, gestión de CLAUDE.md, skill-creator) y en `/external_plugins` los de socios y comunidad que pasan su revisión (Figma, Atlassian, Cloudflare, Firebase, Context7, Superpowers y cientos más).
**Stack:** Markdown, JSON, Python, MCP
**Repo:** https://github.com/anthropics/claude-plugins-official

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Claude Code Plugins Directory/). Si necesitas el código: git clone https://github.com/anthropics/claude-plugins-official`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** usas Claude Code y quieres plugins oficiales o de socios que se instalan con un comando
**Evita si:** buscas recursos comunitarios o trabajas con otro agente; mira `awesome-claude-code` o `wshobson-agents`
**Combina con:** `claude-code`, `anthropic-skills`, `awesome-claude-code`
**Alternativas (elige una):** `wshobson-agents`

## `context-engineering`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Enseña de forma sistemática qué meter en el prompt y qué dejar fuera para que el modelo responda mejor.
**Stack:** Markdown/notebooks (Python)
**Repo:** https://github.com/jasontang-ai/Context-Engineering

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Context-Engineering/). Si necesitas el código: git clone https://github.com/jasontang-ai/Context-Engineering`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres profundizar en contexto y RAG
**Evita si:** buscas skills ejecutables listas para copiar
**Combina con:** `andrej-karpathy-skills`, `headroom`

## `ecc`
role=platform · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Actúa como capa intermedia entre el modelo y tu sistema, de modo que las acciones del agente pasan por un escudo antes de tocar el filesystem o la shell.
**Stack:** Rust (core), TypeScript, Python, Go
**Repo:** https://github.com/affaan-m/ECC

**Instalación** [~]: `git clone https://github.com/affaan-m/ECC && cd ECC && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** ejecutas agentes con acceso real a tu máquina y necesitas contención
**Evita si:** solo haces prompts de chat sin ejecución de código
**Combina con:** `openhands`, `sandbox`, `hermes-agent`

## `fabric`
role=app · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** Organiza prompts reutilizables (patterns) para tareas como resumir videos, extraer ideas o analizar textos. Se encadena con pipes en la terminal.
**Stack:** Go, Markdown
**Repo:** https://github.com/danielmiessler/Fabric

**Instalación** [?]: `git clone https://github.com/danielmiessler/Fabric (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres prompts reutilizables desde la terminal
**Evita si:** buscas solo una lista de prompts para copiar; mira `prompts-chat`
**Combina con:** `ollama`, `yt-dlp`
**Alternativas (elige una):** `prompts-chat`

## `generative-ai-for-beginners`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Recorre desde qué es un LLM hasta prompts, RAG, agentes, seguridad y fine-tuning, con código en Python y TypeScript. Está traducido a muchos idiomas, incluido el español.
**Stack:** Python, TypeScript, Jupyter
**Repo:** https://github.com/microsoft/generative-ai-for-beginners

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Generative AI for Beginners/). Si necesitas el código: git clone https://github.com/microsoft/generative-ai-for-beginners`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres un curso estructurado y gratuito para empezar
**Evita si:** ya construyes con LLM y buscas recetas concretas; mira `openai-cookbook`
**Combina con:** `ai-agents-for-beginners`, `mcp-for-beginners`
**Alternativas (elige una):** `llm-course`

## `geo-seo-claude`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** Añade a Claude Code comandos `/geo` que auditan un sitio para buscadores con IA (ChatGPT, Claude, Perplexity, Gemini, AI Overviews) sin dejar el SEO técnico: citabilidad del contenido, acceso de crawlers de IA en robots.txt, menciones de marca, datos estructurados y llms.txt. Genera informes para clientes en Markdown o PDF y lleva un pequeño CRM de prospectos.
**Stack:** Python, Markdown, ReportLab, JSON-LD, Playwright (opcional)
**Repo:** https://github.com/zubair-trabzada/geo-seo-claude

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/GEO-SEO Claude/). Si necesitas el código: git clone https://github.com/zubair-trabzada/geo-seo-claude`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres medir y mejorar cómo te citan los buscadores con IA, no solo tu posición en Google
**Evita si:** solo haces SEO clásico o no usas Claude Code; mira `marketingskills`
**Combina con:** `marketingskills`, `agency-agents`, `playwright`

## `humanizer`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Detecta 26 patrones típicos de la prosa de LLM (contrastes tipo 'no es X, es Y', cierres dramáticos, tríadas forzadas, frases de falsa profundidad, importancia inflada) y reescribe el texto sin cambiar lo que dice. Puede imitar tu estilo si le das una muestra y, sobre un archivo, solo toca la prosa: no el código, los datos ni el frontmatter.
**Stack:** Markdown, SKILL.md
**Repo:** https://github.com/blader/humanizer

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Humanizer/). Si necesitas el código: git clone https://github.com/blader/humanizer`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** publicas textos redactados con IA y quieres que se lean como escritos por una persona
**Evita si:** quieres reglas de estilo cortas para pegar en un system prompt, con rúbrica propia; mira `stop-slop`
**Combina con:** `marketingskills`, `claude-code`, `codex`
**Alternativas (elige una):** `stop-slop`

## `loop-engineering`
role=skill · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Propone dejar de escribir prompts aislados y diseñar ciclos con objetivo, verificación y puntuación para que el agente itere solo. Incluye starters y herramientas de línea de comandos.
**Stack:** TypeScript, Markdown
**Repo:** https://github.com/cobusgreyling/loop-engineering

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Loop Engineering/). Si necesitas el código: git clone https://github.com/cobusgreyling/loop-engineering`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres que tu agente de código itere solo con criterios medibles
**Evita si:** solo necesitas una lista de skills; mira `awesome-agent-skills`
**Combina con:** `claude-code`, `codex`, `superpowers`

## `marketingskills`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Skills de Corey Haines para marketers técnicos y founders que trabajan con agentes de código: conversión, copywriting, SEO y SEO para IA, anuncios, emails, analítica y atribución, pricing, lanzamientos, retención y ventas. La skill product-marketing guarda el contexto de tu producto y las demás la consultan antes de actuar.
**Stack:** Markdown, SKILL.md, JavaScript (scripts del repo)
**Repo:** https://github.com/coreyhaines31/marketingskills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Marketing Skills/). Si necesitas el código: git clone https://github.com/coreyhaines31/marketingskills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** eres founder o marketer técnico y quieres que tu agente de código haga trabajo de growth con marcos probados
**Evita si:** necesitas una herramienta que envíe campañas o mida resultados; mira `mautic`, `listmonk` o `posthog`
**Combina con:** `agency-agents`, `geo-seo-claude`, `mautic`, `posthog`

## `openai-cookbook`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Reúne recetas sobre embeddings, function calling, RAG, evaluación, agentes y voz. Sirve como referencia práctica al construir con la API de OpenAI.
**Stack:** Python, Jupyter
**Repo:** https://github.com/openai/openai-cookbook

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/OpenAI Cookbook/). Si necesitas el código: git clone https://github.com/openai/openai-cookbook`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** construyes sobre la API de OpenAI y quieres ejemplos oficiales
**Evita si:** usas Claude como modelo principal; mira `claude-cookbooks`
**Combina con:** `openai-python`, `openai-agents-python`
**Alternativas (elige una):** `claude-cookbooks`, `awesome-llm-apps`

## `ponytail`
role=skill · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Empuja al agente a reutilizar, borrar y simplificar antes de añadir código nuevo. Reduce soluciones infladas y cambios innecesarios.
**Stack:** Markdown, JavaScript
**Repo:** https://github.com/DietrichGebert/ponytail

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Ponytail/). Si necesitas el código: git clone https://github.com/DietrichGebert/ponytail`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** tu agente tiende a sobrecomplicar las soluciones
**Evita si:** necesitas una metodología completa de proyecto; mira `bmad-method`
**Combina con:** `claude-code`, `superpowers`, `andrej-karpathy-skills`

## `prompt-eng-tutorial`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** Nueve capítulos con ejercicios sobre claridad, roles, ejemplos, razonamiento paso a paso y cómo evitar alucinaciones. Cada lección se practica contra la API de Claude.
**Stack:** Python, Jupyter
**Repo:** https://github.com/anthropics/prompt-eng-interactive-tutorial

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Anthropic's Prompt Engineering Tutorial/). Si necesitas el código: git clone https://github.com/anthropics/prompt-eng-interactive-tutorial`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres aprender prompts con práctica guiada
**Evita si:** buscas una guía amplia multi-modelo; mira `prompt-engineering-guide`
**Combina con:** `claude-cookbooks`
**Alternativas (elige una):** `prompt-engineering-guide`

## `prompt-engineering-guide`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Explica técnicas de prompting, riesgos y aplicaciones con ejemplos y referencias a papers. Disponible en varios idiomas, incluido el español.
**Stack:** MDX, Next.js, Jupyter
**Repo:** https://github.com/dair-ai/Prompt-Engineering-Guide

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Prompt Engineering Guide/). Si necesitas el código: git clone https://github.com/dair-ai/Prompt-Engineering-Guide`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres una referencia amplia de técnicas de prompting
**Evita si:** prefieres ejercicios prácticos con corrección; mira `prompt-eng-tutorial`
**Combina con:** `context-engineering`
**Alternativas (elige una):** `prompt-eng-tutorial`

## `prompt-master`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Te ayuda a escribir mejores prompts con meta-prompting reutilizable, como una capa por encima de cualquier IA.
**Stack:** Markdown/skill
**Repo:** https://github.com/nidhinjs/prompt-master

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/prompt-master/). Si necesitas el código: git clone https://github.com/nidhinjs/prompt-master`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres dejar de re-promptear y acertar antes
**Evita si:** ya tienes prompts afinados y estables
**Combina con:** `andrej-karpathy-skills`

## `prompts-chat`
role=directory · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Reúne miles de prompts de rol y tarea para ChatGPT, Claude y otros, con buscador web. Puedes desplegar tu propia copia para tu organización.
**Stack:** Next.js, TypeScript, CSV
**Repo:** https://github.com/f/prompts.chat

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/prompts.chat/). Si necesitas el código: git clone https://github.com/f/prompts.chat`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas prompts listos para copiar
**Evita si:** quieres ejecutarlos como comandos encadenables; mira `fabric`
**Alternativas (elige una):** `fabric`

## `skills`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Muestra cómo se escribe una buena skill para agentes, con pocos ejemplos pero de alta calidad para usarlos como plantilla.
**Stack:** Markdown/TypeScript
**Repo:** https://github.com/mattpocock/skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/skills/). Si necesitas el código: git clone https://github.com/mattpocock/skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas referencias limpias y didácticas
**Evita si:** quieres un catálogo masivo (antigravity-awesome-skills)
**Combina con:** `awesome-agent-skills`

## `skillspector`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el riesgo de ejecutar skills de terceros sin revisión.
**Stack:** Python/Node, Docker
**Repo:** https://github.com/NVIDIA/SkillSpector

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/SkillSpector/). Si necesitas el código: git clone https://github.com/NVIDIA/SkillSpector`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** instalas skills externas o curas catálogos
**Evita si:** solo usas skills propias de confianza
**Combina con:** `antigravity-awesome-skills`

## `spec-kit`
role=skill · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Te guía para escribir especificación, plan y tareas antes de que el agente programe. Funciona con Copilot, Claude Code, Gemini CLI y otros.
**Stack:** Python, Markdown
**Repo:** https://github.com/github/spec-kit

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Spec Kit/). Si necesitas el código: git clone https://github.com/github/spec-kit`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres que el agente siga una especificación antes de programar
**Evita si:** buscas roles completos de equipo ágil; mira `bmad-method`
**Combina con:** `claude-code`, `codex`, `gemini-cli`
**Alternativas (elige una):** `bmad-method`

## `stop-slop`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Un SKILL.md con tres archivos de referencia (frases a eliminar, estructuras a evitar y ejemplos antes/después) que enseña a Claude o a cualquier LLM a quitar muletillas, contrastes binarios, fragmentos dramáticos, voz pasiva y otros patrones predecibles. Cierra con una rúbrica de cinco dimensiones para decidir si el texto necesita otra vuelta.
**Stack:** Markdown, SKILL.md
**Repo:** https://github.com/hardikpandya/stop-slop

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Stop Slop/). Si necesitas el código: git clone https://github.com/hardikpandya/stop-slop`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt
**Evita si:** prefieres una skill que reescriba mostrando su proceso y pueda imitar tu voz; mira `humanizer`
**Combina con:** `marketingskills`, `claude-code`
**Alternativas (elige una):** `humanizer`

## `superpowers`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Le da a tu agente de código un método de trabajo completo y coherente (planear, probar, revisar), no piezas sueltas.
**Stack:** Markdown/skills
**Repo:** https://github.com/obra/superpowers

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/superpowers/). Si necesitas el código: git clone https://github.com/obra/superpowers`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres método, no fragmentos sueltos
**Evita si:** solo necesitas una skill aislada puntual
**Combina con:** `awesome-claude-code`, `agent-toolkit`
**Alternativas (elige una):** `agent-skills`

## `wshobson-agents`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Colección de Seth Hobson que agrupa subagentes especialistas, skills y comandos en plugins por área: desarrollo Python y JavaScript, revisión de código, testing, infraestructura, seguridad y más. Se escribe una sola vez en formato de plugin de Claude Code y unos adaptadores generan las versiones para Codex, Cursor, OpenCode, Antigravity CLI, GitHub Copilot y Pi.
**Stack:** Markdown, Python (uv), Make
**Repo:** https://github.com/wshobson/agents

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/wshobson/agents/). Si necesitas el código: git clone https://github.com/wshobson/agents`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres subagentes y comandos especializados por lenguaje o área, instalables plugin a plugin
**Evita si:** solo quieres plugins oficiales de Anthropic y socios; mira `claude-plugins-official`
**Combina con:** `claude-code`, `codex`, `skillspector`
**Alternativas (elige una):** `claude-plugins-official`, `antigravity-awesome-skills`, `agency-agents`
