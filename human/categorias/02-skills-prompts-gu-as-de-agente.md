[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Mejorar tu agente: skills y prompts

Instrucciones, plugins y métodos que añades a un agente que ya utilizas. Distingue una skill concreta de un directorio que solo enlaza a otras.

54 repos · 6 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Anthropic Skills](../fichas/anthropic-skills.md) | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. | Sin API de IA en la ruta básica |
| [Claude Code Plugins Directory](../fichas/claude-plugins-official.md) | Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. | Sin API de IA en la ruta básica |
| [Agent Skills (Addy Osmani)](../fichas/agent-skills.md) | Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. | Sin API de IA en la ruta básica |
| [Humanizer](../fichas/humanizer.md) | Skill que reescribe texto generado por IA para que suene humano, basada en la guía de Wikipedia sobre señales de escritura IA. | Sin API de IA en la ruta básica |
| [Marketing Skills](../fichas/marketingskills.md) | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. | Sin API de IA en la ruta básica |
| [Prompt Engineering Guide](../fichas/prompt-engineering-guide.md) | Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes. | Sin API de IA en la ruta básica |
| [Fabric](../fichas/fabric.md) | CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal. | API de IA opcional |
| [Generative AI for Beginners](../fichas/generative-ai-for-beginners.md) | Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa. | Sin API de IA en la ruta básica |
| [AI Agents for Beginners](../fichas/ai-agents-for-beginners.md) | Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, traducido al español. | Sin API de IA en la ruta básica |

## Secciones

- [Catálogos y marketplaces de skills](#catálogos-y-marketplaces-de-skills) — 11 repos
- [Metodologías y harness para agentes de código](#metodologías-y-harness-para-agentes-de-código) — 15 repos
- [Escritura y calidad de texto](#escritura-y-calidad-de-texto) — 2 repos
- [Skills de dominio: marketing, SEO y negocio](#skills-de-dominio-marketing-seo-y-negocio) — 6 repos
- [Prompts y prompt engineering](#prompts-y-prompt-engineering) — 8 repos
- [Guías, cursos y cookbooks](#guías-cursos-y-cookbooks) — 12 repos

## Catálogos y marketplaces de skills

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Anthropic Skills](../fichas/anthropic-skills.md) | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. | quieres skills oficiales de Anthropic o un ejemplo de referencia para escribir las tuyas | Sin API de IA en la ruta básica |
| [Claude Code Plugins Directory](../fichas/claude-plugins-official.md) | Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. | usas Claude Code y quieres plugins oficiales o de socios que se instalan con un comando | Sin API de IA en la ruta básica |
| [Awesome Claude Skills](../fichas/awesome-claude-skills.md) | Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps. | usas Claude para tareas de negocio además de código y quieres skills ordenadas por área de trabajo | Sin API de IA en la ruta básica |
| [Awesome Claude Code](../fichas/awesome-claude-code.md) | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. | usas Claude Code a diario y quieres descubrir herramientas y flujos probados por la comunidad | Sin API de IA en la ruta básica |
| [Agentic Awesome Skills](../fichas/antigravity-awesome-skills.md) | Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local. | quieres cubrir muchos dominios con skills ya escritas y trabajas con uno o varios agentes de código | Sin API de IA en la ruta básica |
| [wshobson/agents](../fichas/wshobson-agents.md) | Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor, OpenCode y Copilot. | quieres subagentes y comandos especializados por lenguaje o área, instalables plugin a plugin | Sin API de IA en la ruta básica |
| [Awesome GitHub Copilot](../fichas/awesome-copilot.md) | Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y plugins para personalizar GitHub Copilot. | tu equipo trabaja con GitHub Copilot en VS Code o Copilot CLI y quiere personalizarlo | Sin API de IA en la ruta básica |
| [Awesome Agent Skills](../fichas/awesome-agent-skills.md) | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes. | quieres skills con procedencia clara, publicadas por el equipo que mantiene cada herramienta | Sin API de IA en la ruta básica |
| [autoskills](../fichas/autoskills.md) | CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia. | quieres preparar un conjunto de skills adaptado al stack de un proyecto | Depende de la ruta elegida |
| [gemini-skills](../fichas/gemini-skills.md) | Skills oficiales de Google para ayudar a agentes a trabajar con la API, los SDK y los modelos de Gemini. | construyes aplicaciones que llaman a Gemini y necesitas contexto actualizado para el agente | Sin API de IA en la ruta básica |
| [awesome-agents](../fichas/awesome-agents.md) | Directorio de herramientas y proyectos abiertos para construir y operar agentes de inteligencia artificial. | quieres explorar alternativas de agentes antes de elegir una implementación | Sin API de IA en la ruta básica |

## Metodologías y harness para agentes de código

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Agent Skills (Addy Osmani)](../fichas/agent-skills.md) | Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. | quieres skills de ingeniería web de calidad para tu agente | Sin API de IA en la ruta básica |
| [skills](../fichas/skills.md) | Colección de skills de referencia mantenida por el proyecto aihero.dev / Total TypeScript, pensada como ejemplos limpios y bien construidos. | buscas referencias limpias y didácticas | Sin API de IA en la ruta básica |
| [superpowers](../fichas/superpowers.md) | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. | quieres método, no fragmentos sueltos | Sin API de IA en la ruta básica |
| [ECC](../fichas/ecc.md) | Colección de plugins, skills, hooks y convenciones para organizar el trabajo de agentes de código en un proyecto. | ejecutas agentes con acceso real a tu máquina y necesitas contención | Depende de la ruta elegida |
| [andrej-karpathy-skills](../fichas/andrej-karpathy-skills.md) | Guía de 4 principios inspirada en Andrej Karpathy para que tu agente de código responda útil y sin relleno. | quieres respuestas más útiles ya, sin curar prompts largos | Sin API de IA en la ruta básica |
| [Ponytail](../fichas/ponytail.md) | Skill que hace que tu agente de código piense como un senior minimalista: el mejor código es el que no escribes. | tu agente tiende a sobrecomplicar las soluciones | Sin API de IA en la ruta básica |
| [Spec Kit](../fichas/spec-kit.md) | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. | quieres que el agente siga una especificación antes de programar | Sin API de IA en la ruta básica |
| [security-audit-skill](../fichas/security-audit-skill.md) | Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estructurados. | quieres un proceso reproducible de revisión de seguridad con agentes | Sin API de IA en la ruta básica |
| [BMAD Method](../fichas/bmad-method.md) | Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA. | quieres un proceso completo de producto a código con agentes | Sin API de IA en la ruta básica |
| [codex-plugin-cc](../fichas/codex-plugin-cc.md) | Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas. | quieres revisar código con Codex dentro de tu flujo de Claude Code | Sin API de IA en la ruta básica |
| [SkillSpector](../fichas/skillspector.md) | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. | instalas skills externas o curas catálogos | API de IA necesaria |
| [SuperClaude_Framework](../fichas/superclaude-framework.md) | Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code. | quieres estructurar el trabajo de Claude Code con comandos y convenciones | Sin API de IA en la ruta básica |
| [claude-token-efficient](../fichas/claude-token-efficient.md) | Instrucciones para reducir la verbosidad de Claude Code y medir el coste de respuestas y contexto. | quieres probar respuestas más breves en tareas con mucha salida de texto | Sin API de IA en la ruta básica |
| [agent-toolkit](../fichas/agent-toolkit.md) | Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación. | quieres productividad inmediata con tareas comunes | Sin API de IA en la ruta básica |
| [grok-plugin-claude-code](../fichas/grok-plugin-claude-code.md) | Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar. | usas Claude Code y quieres consultar Grok dentro de ese flujo | Sin API de IA en la ruta básica |

## Escritura y calidad de texto

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Humanizer](../fichas/humanizer.md) | Skill que reescribe texto generado por IA para que suene humano, basada en la guía de Wikipedia sobre señales de escritura IA. | publicas textos redactados con IA y quieres que se lean como escritos por una persona | Sin API de IA en la ruta básica |
| [Stop Slop](../fichas/stop-slop.md) | Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad. | quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt | Sin API de IA en la ruta básica |

## Skills de dominio: marketing, SEO y negocio

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Marketing Skills](../fichas/marketingskills.md) | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. | eres founder o marketer técnico y quieres que tu agente de código haga trabajo de growth con marcos probados | Sin API de IA en la ruta básica |
| [The Agency (agency-agents)](../fichas/agency-agents.md) | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes. | quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código | Sin API de IA en la ruta básica |
| [financial-services](../fichas/financial-services.md) | Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros. | quieres estudiar flujos financieros dentro del ecosistema de Claude | Sin API de IA en la ruta básica |
| [GEO-SEO Claude](../fichas/geo-seo-claude.md) | Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF. | quieres medir y mejorar cómo te citan los buscadores con IA, no solo tu posición en Google | Sin API de IA en la ruta básica |
| [social-media-research-skills](../fichas/social-media-research-skills.md) | Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators. | quieres investigación de contenido social desde un agente compatible con Agent Skills | Sin API de IA en la ruta básica |
| [Arcads AI Video Skill Pack](../fichas/arcads-claude-code.md) | Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen con la API de Arcads (Seedance, Sora, Veo, Kling). | ya tienes cuenta de Arcads y quieres producir creatividades publicitarias desde Claude Code o Cursor | API de IA necesaria |

## Prompts y prompt engineering

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Prompt Engineering Guide](../fichas/prompt-engineering-guide.md) | Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes. | quieres una referencia amplia de técnicas de prompting | Sin API de IA en la ruta básica |
| [Fabric](../fichas/fabric.md) | CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal. | quieres prompts reutilizables desde la terminal | API de IA opcional |
| [prompts.chat](../fichas/prompts-chat.md) | La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable. | buscas prompts listos para copiar | Sin API de IA en la ruta básica |
| [system-prompts-and-models-of-ai-tools](../fichas/system-prompts-and-models-of-ai-tools.md) | Colección de prompts y configuraciones atribuidos a herramientas de IA para estudiar sus patrones de diseño. | quieres investigar patrones de prompts utilizados por asistentes | Sin API de IA en la ruta básica |
| [Anthropic's Prompt Engineering Tutorial](../fichas/prompt-eng-tutorial.md) | Tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios. | quieres aprender prompts con práctica guiada | Sin API de IA en la ruta básica |
| [prompt-master](../fichas/prompt-master.md) | Skill que ayuda a redactar prompts precisos para cualquier herramienta de IA, buscando el mejor resultado sin desperdiciar tokens. | quieres dejar de re-promptear y acertar antes | Sin API de IA en la ruta básica |
| [ChatGPT_DAN](../fichas/chatgpt-dan.md) | Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones antiguas de ChatGPT. | quieres investigar prompts históricos y sus limitaciones | Sin API de IA en la ruta básica |
| [chatgpt_system_prompt](../fichas/chatgpt-system-prompt.md) | Colección de prompts de GPT y recursos sobre instrucciones de sistema y extracción de prompts. | quieres comparar patrones de prompts como material de investigación | Sin API de IA en la ruta básica |

## Guías, cursos y cookbooks

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Generative AI for Beginners](../fichas/generative-ai-for-beginners.md) | Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa. | quieres un curso estructurado y gratuito para empezar | Sin API de IA en la ruta básica |
| [AI Agents for Beginners](../fichas/ai-agents-for-beginners.md) | Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, traducido al español. | estás empezando con agentes y quieres un curso guiado, gratuito y disponible en español | Sin API de IA en la ruta básica |
| [Awesome LLM Apps](../fichas/awesome-llm-apps.md) | Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM. | quieres una plantilla de app con LLM que funcione desde el primer día para adaptarla a tu proyecto | Sin API de IA en la ruta básica |
| [OpenAI Cookbook](../fichas/openai-cookbook.md) | Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. | construyes sobre la API de OpenAI y quieres ejemplos oficiales | Sin API de IA en la ruta básica |
| [Claude Cookbooks](../fichas/claude-cookbooks.md) | Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización. | construyes sobre la API de Claude y quieres ejemplos oficiales que puedas copiar | Sin API de IA en la ruta básica |
| [ai-engineering-hub](../fichas/ai-engineering-hub.md) | Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificial. | quieres aprender implementando ejemplos de ingeniería de IA | Sin API de IA en la ruta básica |
| [500-AI-Agents-Projects](../fichas/500-ai-agents-projects.md) | Colección de ideas, casos de uso y ejemplos de agentes de IA para distintos sectores y tareas. | buscas ejemplos de aplicaciones de agentes para adaptar a tu propio problema | Sin API de IA en la ruta básica |
| [12-Factor Agents](../fichas/12-factor-agents.md) | Guía de 12 principios de ingeniería para construir agentes con LLM fiables en producción, inspirada en las 12 Factor Apps. | vas a construir un agente para clientes reales y quieres principios de diseño antes de elegir framework | Sin API de IA en la ruta básica |
| [Agents Towards Production](../fichas/agents-towards-production.md) | Colección de 28 tutoriales con código para llevar agentes de IA a producción: memoria, despliegue, seguridad, trazas y evaluación. | ya tienes un prototipo de agente y necesitas resolver memoria, despliegue, seguridad u observabilidad | Sin API de IA en la ruta básica |
| [claude-quickstarts](../fichas/claude-quickstarts.md) | Ejemplos oficiales de Anthropic para construir aplicaciones con Claude, herramientas y uso de computadora. | quieres partir de un ejemplo oficial al integrar la API de Claude | Sin API de IA en la ruta básica |
| [Loop Engineering](../fichas/loop-engineering.md) | Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos. | quieres que tu agente de código itere solo con criterios medibles | Sin API de IA en la ruta básica |
| [Context-Engineering](../fichas/context-engineering.md) | Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso. | quieres profundizar en contexto y RAG | Sin API de IA en la ruta básica |

## Recetas relacionadas

- [Marketing de agencia](../playbooks/marketing-de-agencia.md) — Operar campañas, contenido y email a escala con agentes y herramientas propias.
- [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
