# 2. Skills, plugins y métodos para agentes — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

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
