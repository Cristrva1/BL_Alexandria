# 2. Skills, Prompts & Guías de Agente — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agency-agents`
role=skill · exec=cloud · setup=medium · mcp=False · prov=['anthropic', 'google']

**Qué es:** conjunto de playbooks y agentes especializados (incluye un Digital Marketing Pro) diseñados para operar una agencia multicanal a escala.
**Stack:** Python, Node.js
**Repo:** https://github.com/msitarzewski/agency-agents

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/agency-agents/). Si necesitas el código: git clone https://github.com/msitarzewski/agency-agents`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** operas una agencia
**Evita si:** eres un solo proyecto pequeño.
**Combina con:** `marketingskills`, `geo-seo-claude`

## `agent-toolkit`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación.
**Stack:** Markdown/scripts
**Repo:** https://github.com/leonardocouy/agent-toolkit

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/agent-toolkit/). Si necesitas el código: git clone https://github.com/leonardocouy/agent-toolkit`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres productividad inmediata
**Evita si:** buscas un método integral ([superpowers](#-superpowers)).
**Combina con:** `superpowers`
**Alternativas (elige una):** `superpowers`

## `agents-towards-production`
role=directory · exec=cloud · setup=medium · mcp=False · prov=—

**Qué es:** playbook open-source con tutoriales end-to-end para llevar agentes GenAI de prototipo a producto real, cubriendo el ciclo completo de producción.
**Stack:** Python, varios
**Repo:** https://github.com/NirDiamant/agents-towards-production

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/agents-towards-production/). Si necesitas el código: git clone https://github.com/NirDiamant/agents-towards-production`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** vas a producción con agentes
**Evita si:** solo experimentas localmente.
**Combina con:** `langfuse`, `ag2`

## `andrej-karpathy-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** guía de 4 principios (inspirada en las ideas de Andrej Karpathy sobre asistentes de código) que define cómo debe responder un agente para maximizar utilidad y reducir verbosidad innecesaria.
**Stack:** Markdown (`CLAUDE.md`)
**Repo:** https://github.com/multica-ai/andrej-karpathy-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/andrej-karpathy-skills/). Si necesitas el código: git clone https://github.com/multica-ai/andrej-karpathy-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres respuestas más útiles ya
**Evita si:** buscas skills ejecutables concretas.
**Combina con:** `awesome-claude-code`, `context-engineering`

## `antigravity-awesome-skills`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google', 'mcp']

**Qué es:** catálogo masivo con más de 1.678 habilidades (`SKILL.md`) categorizadas por dominio (desarrollo, QA, DevOps, seguridad, marketing) listas para instalar en distintos asistentes.
**Stack:** Node.js (CLI), Python
**Repo:** https://github.com/sickn33/antigravity-awesome-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/antigravity-awesome-skills/). Si necesitas el código: git clone https://github.com/sickn33/antigravity-awesome-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres opciones por cantidad
**Evita si:** prefieres curaduría oficial ([awesome-agent-skills](#-awesome-agent-skills)).
**Combina con:** `skillspector`, `awesome-agent-skills`
**Alternativas (elige una):** `awesome-agent-skills`

## `awesome-agent-skills`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google', 'mcp']

**Qué es:** colección curada de habilidades oficiales y comunitarias publicadas por marcas líderes (Anthropic, Google, Stripe, Netlify…) como referencia de calidad para agentes.
**Stack:** Markdown
**Repo:** https://github.com/VoltAgent/awesome-agent-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-agent-skills/). Si necesitas el código: git clone https://github.com/VoltAgent/awesome-agent-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** valoras respaldo de marca
**Evita si:** necesitas máxima cantidad.
**Combina con:** `antigravity-awesome-skills`

## `awesome-claude-code`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** lista "awesome" curada de scripts, agentes, hooks, slash commands y extensiones específicos del ecosistema de Claude Code.
**Stack:** Python / Markdown
**Repo:** https://github.com/hesreallyhim/awesome-claude-code

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-claude-code/). Si necesitas el código: git clone https://github.com/hesreallyhim/awesome-claude-code`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** vives en Claude Code
**Evita si:** usas otro asistente.
**Combina con:** `claude-plugins-official`, `superpowers`

## `claude-plugins-official`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['anthropic', 'mcp']

**Qué es:** plugins y extensiones oficiales para Claude, distribuidos junto al repositorio de Claude Code de Anthropic.
**Stack:** Markdown/JS
**Repo:** https://github.com/anthropics/claude-code

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/claude-plugins-official/). Si necesitas el código: git clone https://github.com/anthropics/claude-code`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres extensiones oficiales
**Evita si:** buscas aportes comunitarios amplios.
**Combina con:** `awesome-claude-code`

## `context-engineering`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso.
**Stack:** Markdown/notebooks
**Repo:** https://github.com/davidkimai/Context-Engineering

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Context-Engineering/). Si necesitas el código: git clone https://github.com/davidkimai/Context-Engineering`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres profundizar en contexto
**Evita si:** buscas skills ejecutables.
**Combina con:** `andrej-karpathy-skills`, `headroom`

## `geo-seo-claude`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** skill GEO-first con soporte SEO clásico para optimizar la visibilidad de sitios ante motores de búsqueda con IA (Generative Engine Optimization).
**Stack:** Markdown/skill
**Repo:** https://github.com/zubair-trabzada/geo-seo-claude

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/geo-seo-claude/). Si necesitas el código: git clone https://github.com/zubair-trabzada/geo-seo-claude`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** te importa el descubrimiento por IA
**Evita si:** solo haces SEO clásico.
**Combina con:** `marketingskills`, `agency-agents`

## `guia`
role=skill · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Catálogo operativo de los **156 repositorios** locales del workspace, diseñado para **entender, comparar, elegir y combinar** repos rápido.
**Stack:** typescript, whisper, comfy
**Repo:** —

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/guia/). Si necesitas el código: git clone <guia>`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres 🌌 catálogo de repositorios de ia & automatización
**Evita si:** —
**Combina con:** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`

## `humanizer`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** skill para Claude Code/OpenCode que elimina las señales típicas ("tells") de la escritura generada por IA para que el texto suene más natural.
**Stack:** Markdown/skill
**Repo:** https://github.com/blader/humanizer

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/humanizer/). Si necesitas el código: git clone https://github.com/blader/humanizer`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** publicas prosa generada por IA
**Evita si:** escribes a mano.
**Combina con:** `stop-slop`

## `marketingskills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['openai', 'anthropic', 'mcp']

**Qué es:** colección de skills de marketing que cubren conversión, copywriting, SEO, analítica y growth para usar con agentes de código.
**Stack:** Markdown/skills
**Repo:** https://github.com/coreyhaines31/marketingskills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/marketingskills/). Si necesitas el código: git clone https://github.com/coreyhaines31/marketingskills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** automatizas marketing con agentes
**Evita si:** necesitas ejecución (no skills).
**Combina con:** `agency-agents`, `mautic`

## `n8n-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['anthropic', 'mcp']

**Qué es:** conjunto de 14 skills estructuradas para Claude Code orientadas a construir flujos de n8n correctos, evitando errores al generar su JSON.
**Stack:** `SKILL.md`, Markdown
**Repo:** https://github.com/czlonkowski/n8n-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/n8n-skills/). Si necesitas el código: git clone https://github.com/czlonkowski/n8n-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** generas workflows n8n con IA
**Evita si:** no usas n8n.
**Combina con:** `n8n`, `n8n-mcp`

## `prompt-master`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** skill que ayuda a redactar prompts precisos para cualquier herramienta de IA, buscando el mejor resultado sin desperdiciar tokens.
**Stack:** Markdown/skill
**Repo:** https://github.com/nidhinjs/prompt-master

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/prompt-master/). Si necesitas el código: git clone https://github.com/nidhinjs/prompt-master`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres dejar de re-promptear
**Evita si:** ya tienes prompts afinados.
**Combina con:** `andrej-karpathy-skills`

## `skills`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** colección de skills de referencia mantenida por el proyecto aihero.dev / Total TypeScript, pensada como ejemplos limpios y bien construidos.
**Stack:** Markdown/TypeScript
**Repo:** https://github.com/total-typescript/skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/skills/). Si necesitas el código: git clone https://github.com/total-typescript/skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas referencias limpias
**Evita si:** quieres un catálogo masivo.
**Combina con:** `awesome-agent-skills`

## `skills-emil`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrollador (design engineering).
**Stack:** Markdown (skills)
**Repo:** https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/skills_emil/). Si necesitas el código: git clone https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** trabajas diseño+dev en equipo
**Evita si:** buscas componentes listos.
**Combina con:** `designmd`, `ui-ux-pro-max-skill`

## `skillspector`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['anthropic', 'google', 'mcp']

**Qué es:** herramienta para auditar la seguridad de skills y detectar patrones potencialmente riesgosos antes de instalarlas.
**Stack:** Python/Node
**Repo:** https://github.com/NVIDIA/SkillSpector

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/SkillSpector/). Si necesitas el código: git clone https://github.com/NVIDIA/SkillSpector`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** instalas skills externas
**Evita si:** solo usas skills propias confiables.
**Combina con:** `antigravity-awesome-skills`

## `stop-slop`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** skill que enseña al modelo a eliminar patrones y "tells" de la prosa generada por IA, mejorando ritmo y estilo.
**Stack:** Markdown/skill
**Repo:** https://github.com/hardikpandya/stop-slop

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/stop-slop/). Si necesitas el código: git clone https://github.com/hardikpandya/stop-slop`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres prosa más natural
**Evita si:** ya usas [humanizer](#-humanizer) (solapan).
**Combina con:** `humanizer`
**Alternativas (elige una):** `humanizer`

## `superpowers`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque.
**Stack:** Markdown/skills
**Repo:** https://github.com/obra/superpowers

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/superpowers/). Si necesitas el código: git clone https://github.com/obra/superpowers`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres método, no fragmentos
**Evita si:** solo necesitas una skill aislada.
**Combina con:** `awesome-claude-code`, `agent-toolkit`

## `taste-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['openai', 'anthropic']

**Qué es:** skills "anti-slop" para producir frontends premium (layout, tipografía, motion) más skills de generación de imagen para crear mood boards de referencia.
**Stack:** Markdown/skills
**Repo:** https://github.com/Leonxlnx/taste-skill

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/taste-skill/). Si necesitas el código: git clone https://github.com/Leonxlnx/taste-skill`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres frontends con gusto
**Evita si:** te basta UI funcional básica.
**Combina con:** `ui-ux-pro-max-skill`, `impeccable`

## `ui-ux-pro-max-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** habilidades que dotan al asistente de inteligencia de diseño UI/UX y estilos avanzados para producir interfaces más profesionales.
**Stack:** Node.js (uipro-cli), Python
**Repo:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/ui-ux-pro-max-skill/). Si necesitas el código: git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** generas UI con IA y quieres calidad
**Evita si:** no trabajas frontend.
**Combina con:** `taste-skill`, `impeccable`, `tailwindcss`
