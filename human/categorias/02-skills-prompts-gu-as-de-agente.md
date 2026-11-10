[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 1. Automatización, Mensajería & CRM](01-automatizaci-n-mensajer-a-crm.md) · [3. Frameworks & Orquestación de Agentes ➡️](03-frameworks-orquestaci-n-de-agentes.md)

# 🧠 2. Skills, Prompts & Guías de Agente

> Catálogos de skills, metodologías para agentes de código, escritura sin 'slop', prompts, cursos y cookbooks.

**38 repos** · 6 subcategorías · ⭐ 3.5M estrellas en total · 🆕 17 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [Anthropic Skills](../fichas/anthropic-skills.md) | 192k | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. | `/plugin marketplace add anthropics/skills` |
| [Claude Code Plugins Directory](../fichas/claude-plugins-official.md) | 46.7k | Marketplace oficial de Anthropic con plugins para Claude Code, propios y de socios: comandos, agentes, skills y servidores MCP. | `/plugin install <plugin>@claude-plugins-official` |
| [Agent Skills (Addy Osmani)](../fichas/agent-skills.md) | 115k | Colección de skills de ingeniería de producción para agentes de código, de Addy Osmani. | `.claude/skills/` |
| [Humanizer](../fichas/humanizer.md) | 67.4k | Skill que reescribe texto generado por IA para que suene humano, basada en la guía de Wikipedia sobre señales de escritura IA. | `/plugin marketplace add blader/humanizer` |
| [Marketing Skills](../fichas/marketingskills.md) | 59.5k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. | `npx skills add coreyhaines31/marketingskills` |
| [Prompt Engineering Guide](../fichas/prompt-engineering-guide.md) | 80k | Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes. | No se instala: léela en promptingguide.ai o en el repo. |
| [Fabric](../fichas/fabric.md) | 44.6k | CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal. | `go install github.com/danielmiessler/fabric/cmd/fabric@latest` |
| [Generative AI for Beginners](../fichas/generative-ai-for-beginners.md) | 123k | Curso gratuito de Microsoft con 21 lecciones para empezar a construir aplicaciones con IA generativa. | No se instala: abre el repo o haz fork y sigue las lecciones en Codespaces. |
| [AI Agents for Beginners](../fichas/ai-agents-for-beginners.md) | 79.3k | Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, traducido al español. | `00-course-setup` |

## 🧭 Subcategorías

- [Catálogos y marketplaces de skills](#catálogos-y-marketplaces-de-skills) — 8 repos
- [Metodologías y harness para agentes de código](#metodologías-y-harness-para-agentes-de-código) — 10 repos
- [Escritura y calidad de texto](#escritura-y-calidad-de-texto) — 2 repos
- [Skills de dominio: marketing, SEO y negocio](#skills-de-dominio-marketing-seo-y-negocio) — 4 repos
- [Prompts y prompt engineering](#prompts-y-prompt-engineering) — 5 repos
- [Guías, cursos y cookbooks](#guías-cursos-y-cookbooks) — 9 repos

## Catálogos y marketplaces de skills

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Anthropic Skills](../fichas/anthropic-skills.md) 🆕 | 192k | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. | quieres skills oficiales de Anthropic o un ejemplo de referencia para escribir las tuyas | 🟢 |
| ⭐ [Claude Code Plugins Directory](../fichas/claude-plugins-official.md) | 46.7k | Marketplace oficial de Anthropic con plugins para Claude Code, propios y de socios: comandos, agentes, skills y servidores MCP. | usas Claude Code y quieres plugins oficiales o de socios que se instalan con un comando | 🟢 |
| [Awesome Claude Skills](../fichas/awesome-claude-skills.md) 🆕 | 79.2k | Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps. | usas Claude para tareas de negocio además de código y quieres skills ordenadas por área de trabajo | 🟢 |
| [Awesome Claude Code](../fichas/awesome-claude-code.md) | 57.7k | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. | usas Claude Code a diario y quieres descubrir herramientas y flujos probados por la comunidad | 🟢 |
| [Agentic Awesome Skills](../fichas/antigravity-awesome-skills.md) | 49.5k | Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local. | quieres cubrir muchos dominios con skills ya escritas y trabajas con uno o varios agentes de código | 🟢 |
| [wshobson/agents](../fichas/wshobson-agents.md) 🆕 | 42.4k | Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor, OpenCode y Copilot. | quieres subagentes y comandos especializados por lenguaje o área, instalables plugin a plugin | 🟢 |
| [Awesome GitHub Copilot](../fichas/awesome-copilot.md) 🆕 | 41k | Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y plugins para personalizar GitHub Copilot. | tu equipo trabaja con GitHub Copilot en VS Code o Copilot CLI y quiere personalizarlo | 🟢 |
| [Awesome Agent Skills](../fichas/awesome-agent-skills.md) | 37k | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes. | quieres skills con procedencia clara, publicadas por el equipo que mantiene cada herramienta | 🟢 |

## Metodologías y harness para agentes de código

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Agent Skills (Addy Osmani)](../fichas/agent-skills.md) 🆕 | 115k | Colección de skills de ingeniería de producción para agentes de código, de Addy Osmani. | quieres skills de ingeniería web de calidad para tu agente | 🟢 |
| [skills](../fichas/skills.md) | 320k | Colección de skills de referencia mantenida por el proyecto aihero.dev / Total TypeScript, pensada como ejemplos limpios y bien construidos. | buscas referencias limpias y didácticas | 🟢 |
| [superpowers](../fichas/superpowers.md) | 315k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. | quieres método, no fragmentos sueltos | 🟢 |
| [ECC](../fichas/ecc.md) | 300k | Sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura. | ejecutas agentes con acceso real a tu máquina y necesitas contención | 🔴 |
| [andrej-karpathy-skills](../fichas/andrej-karpathy-skills.md) | 232k | Guía de 4 principios inspirada en Andrej Karpathy para que tu agente de código responda útil y sin relleno. | quieres respuestas más útiles ya, sin curar prompts largos | 🟢 |
| [Ponytail](../fichas/ponytail.md) | 188k | Skill que hace que tu agente de código piense como un senior minimalista: el mejor código es el que no escribes. | tu agente tiende a sobrecomplicar las soluciones | 🟢 |
| [Spec Kit](../fichas/spec-kit.md) 🆕 | 149k | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. | quieres que el agente siga una especificación antes de programar | 🟢 |
| [BMAD Method](../fichas/bmad-method.md) 🆕 | 55.2k | Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA. | quieres un proceso completo de producto a código con agentes | 🟢 |
| [SkillSpector](../fichas/skillspector.md) | 25.2k | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. | instalas skills externas o curas catálogos | 🟢 |
| [agent-toolkit](../fichas/agent-toolkit.md) | 2.7k | Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación. | quieres productividad inmediata con tareas comunes | 🟢 |

## Escritura y calidad de texto

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Humanizer](../fichas/humanizer.md) | 67.4k | Skill que reescribe texto generado por IA para que suene humano, basada en la guía de Wikipedia sobre señales de escritura IA. | publicas textos redactados con IA y quieres que se lean como escritos por una persona | 🟢 |
| [Stop Slop](../fichas/stop-slop.md) | 18.8k | Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad. | quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt | 🟢 |

## Skills de dominio: marketing, SEO y negocio

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Marketing Skills](../fichas/marketingskills.md) | 59.5k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. | eres founder o marketer técnico y quieres que tu agente de código haga trabajo de growth con marcos probados | 🟢 |
| [The Agency (agency-agents)](../fichas/agency-agents.md) | 168k | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes. | quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código | 🟢 |
| [GEO-SEO Claude](../fichas/geo-seo-claude.md) | 11.6k | Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF. | quieres medir y mejorar cómo te citan los buscadores con IA, no solo tu posición en Google | 🟢 |
| [Arcads AI Video Skill Pack](../fichas/arcads-claude-code.md) | — | Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen con la API de Arcads (Seedance, Sora, Veo, Kling). | ya tienes cuenta de Arcads y quieres producir creatividades publicitarias desde Claude Code o Cursor | 🟡 |

## Prompts y prompt engineering

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Prompt Engineering Guide](../fichas/prompt-engineering-guide.md) 🆕 | 80k | Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes. | quieres una referencia amplia de técnicas de prompting | 🟢 |
| ⭐ [Fabric](../fichas/fabric.md) 🆕 | 44.6k | CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal. | quieres prompts reutilizables desde la terminal | 🟢 |
| [prompts.chat](../fichas/prompts-chat.md) 🆕 | 177k | La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable. | buscas prompts listos para copiar | 🟢 |
| [Anthropic's Prompt Engineering Tutorial](../fichas/prompt-eng-tutorial.md) 🆕 | 39.2k | Tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios. | quieres aprender prompts con práctica guiada | 🟢 |
| [prompt-master](../fichas/prompt-master.md) | 15.8k | Skill que ayuda a redactar prompts precisos para cualquier herramienta de IA, buscando el mejor resultado sin desperdiciar tokens. | quieres dejar de re-promptear y acertar antes | 🟢 |

## Guías, cursos y cookbooks

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Generative AI for Beginners](../fichas/generative-ai-for-beginners.md) 🆕 | 123k | Curso gratuito de Microsoft con 21 lecciones para empezar a construir aplicaciones con IA generativa. | quieres un curso estructurado y gratuito para empezar | 🟢 |
| ⭐ [AI Agents for Beginners](../fichas/ai-agents-for-beginners.md) 🆕 | 79.3k | Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, traducido al español. | estás empezando con agentes y quieres un curso guiado, gratuito y disponible en español | 🟡 |
| [Awesome LLM Apps](../fichas/awesome-llm-apps.md) 🆕 | 144k | Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM. | quieres una plantilla de app con LLM que funcione desde el primer día para adaptarla a tu proyecto | 🟡 |
| [OpenAI Cookbook](../fichas/openai-cookbook.md) 🆕 | 77k | Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. | construyes sobre la API de OpenAI y quieres ejemplos oficiales | 🟢 |
| [Claude Cookbooks](../fichas/claude-cookbooks.md) 🆕 | 54.5k | Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización. | construyes sobre la API de Claude y quieres ejemplos oficiales que puedas copiar | 🟢 |
| [12-Factor Agents](../fichas/12-factor-agents.md) 🆕 | 27.1k | Guía de 12 principios de ingeniería para construir agentes con LLM fiables en producción, inspirada en las 12 Factor Apps. | vas a construir un agente para clientes reales y quieres principios de diseño antes de elegir framework | 🟢 |
| [Agents Towards Production](../fichas/agents-towards-production.md) | 21.9k | Colección de 28 tutoriales con código para llevar agentes de IA a producción: memoria, despliegue, seguridad, trazas y evaluación. | ya tienes un prototipo de agente y necesitas resolver memoria, despliegue, seguridad u observabilidad | 🟡 |
| [Loop Engineering](../fichas/loop-engineering.md) | 11.7k | Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos. | quieres que tu agente de código itere solo con criterios medibles | 🟢 |
| [Context-Engineering](../fichas/context-engineering.md) | 9.3k | Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso. | quieres profundizar en contexto y RAG | 🟢 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### Claude Code Plugins Directory, The Agency (agency-agents), Awesome Claude Skills, Awesome Claude Code, Agentic Awesome Skills, wshobson/agents, Awesome Agent Skills

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Claude Code Plugins Directory](../fichas/claude-plugins-official.md) | 46.7k | usas Claude Code y quieres plugins oficiales o de socios que se instalan con un comando | buscas recursos comunitarios o trabajas con otro agente; mira `awesome-claude-code` o `wshobson-agents` |
| [The Agency (agency-agents)](../fichas/agency-agents.md) | 168k | quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código | solo necesitas skills de marketing y growth; mira `marketingskills` |
| [Awesome Claude Skills](../fichas/awesome-claude-skills.md) | 79.2k | usas Claude para tareas de negocio además de código y quieres skills ordenadas por área de trabajo | solo quieres skills de procedencia oficial; mira `anthropic-skills` o `awesome-agent-skills` |
| [Awesome Claude Code](../fichas/awesome-claude-code.md) | 57.7k | usas Claude Code a diario y quieres descubrir herramientas y flujos probados por la comunidad | trabajas con otro agente o solo quieres plugins oficiales; mira `claude-plugins-official` o `awesome-agent-skills` |
| [Agentic Awesome Skills](../fichas/antigravity-awesome-skills.md) | 49.5k | quieres cubrir muchos dominios con skills ya escritas y trabajas con uno o varios agentes de código | prefieres pocas skills oficiales y revisadas; mira `anthropic-skills` o `awesome-agent-skills` |
| [wshobson/agents](../fichas/wshobson-agents.md) | 42.4k | quieres subagentes y comandos especializados por lenguaje o área, instalables plugin a plugin | solo quieres plugins oficiales de Anthropic y socios; mira `claude-plugins-official` |
| [Awesome Agent Skills](../fichas/awesome-agent-skills.md) | 37k | quieres skills con procedencia clara, publicadas por el equipo que mantiene cada herramienta | prefieres instalar un lote grande con un solo comando; mira `antigravity-awesome-skills` |

### Agent Skills (Addy Osmani), superpowers

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Agent Skills (Addy Osmani)](../fichas/agent-skills.md) | 115k | quieres skills de ingeniería web de calidad para tu agente | buscas un catálogo enorme de skills de todo tipo; mira `antigravity-awesome-skills` |
| [superpowers](../fichas/superpowers.md) | 315k | quieres método, no fragmentos sueltos | solo necesitas una skill aislada puntual |

### Spec Kit, BMAD Method

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Spec Kit](../fichas/spec-kit.md) | 149k | quieres que el agente siga una especificación antes de programar | buscas roles completos de equipo ágil; mira `bmad-method` |
| [BMAD Method](../fichas/bmad-method.md) | 55.2k | quieres un proceso completo de producto a código con agentes | prefieres algo ligero centrado en especificaciones; mira `spec-kit` |

### Humanizer, Stop Slop

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Humanizer](../fichas/humanizer.md) | 67.4k | publicas textos redactados con IA y quieres que se lean como escritos por una persona | quieres reglas de estilo cortas para pegar en un system prompt, con rúbrica propia; mira `stop-slop` |
| [Stop Slop](../fichas/stop-slop.md) | 18.8k | quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt | prefieres una skill que reescriba mostrando su proceso y pueda imitar tu voz; mira `humanizer` |

### Prompt Engineering Guide, Anthropic's Prompt Engineering Tutorial

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Prompt Engineering Guide](../fichas/prompt-engineering-guide.md) | 80k | quieres una referencia amplia de técnicas de prompting | prefieres ejercicios prácticos con corrección; mira `prompt-eng-tutorial` |
| [Anthropic's Prompt Engineering Tutorial](../fichas/prompt-eng-tutorial.md) | 39.2k | quieres aprender prompts con práctica guiada | buscas una guía amplia multi-modelo; mira `prompt-engineering-guide` |

### Fabric, prompts.chat

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Fabric](../fichas/fabric.md) | 44.6k | quieres prompts reutilizables desde la terminal | buscas solo una lista de prompts para copiar; mira `prompts-chat` |
| [prompts.chat](../fichas/prompts-chat.md) | 177k | buscas prompts listos para copiar | quieres ejecutarlos como comandos encadenables; mira `fabric` |

### Awesome LLM Apps, OpenAI Cookbook, Claude Cookbooks

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Awesome LLM Apps](../fichas/awesome-llm-apps.md) | 144k | quieres una plantilla de app con LLM que funcione desde el primer día para adaptarla a tu proyecto | buscas un curso estructurado con lecciones en orden; mira `ai-agents-for-beginners` o `generative-ai-for-beginners` |
| [OpenAI Cookbook](../fichas/openai-cookbook.md) | 77k | construyes sobre la API de OpenAI y quieres ejemplos oficiales | usas Claude como modelo principal; mira `claude-cookbooks` |
| [Claude Cookbooks](../fichas/claude-cookbooks.md) | 54.5k | construyes sobre la API de Claude y quieres ejemplos oficiales que puedas copiar | tu app usa la API de OpenAI; mira `openai-cookbook` |

## 🧪 Recetas que usan esta categoría

- [📈 Marketing de agencia](../playbooks/marketing-de-agencia.md) — Operar campañas, contenido y email a escala con agentes y herramientas propias.
- [🛠️ Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
