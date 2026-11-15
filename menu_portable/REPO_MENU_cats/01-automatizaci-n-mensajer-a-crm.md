# 1. Automatización, Mensajería & CRM — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `activepieces`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** Orquesta tus apps con flujos visuales sin código y conserva el control al alojarlo en tu servidor.
**Stack:** Node.js, TypeScript, self-host/web
**Repo:** https://github.com/activepieces/activepieces

**Instalación** [~]: `git clone https://github.com/activepieces/activepieces && cd activepieces && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres reemplazar Zapier con piezas propias en TypeScript
**Evita si:** ya dominas n8n y su ecosistema te basta
**Combina con:** `novu`
**Alternativas (elige una):** `n8n`

## `appsmith`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Arrastra widgets, conéctalos a más de 25 bases de datos o cualquier API y añade lógica en JavaScript. Pensada para equipos que construyen backoffices rápido.
**Stack:** TypeScript, React, Java, MongoDB, Docker
**Repo:** https://github.com/appsmithorg/appsmith

**Instalación** [~]: `git clone https://github.com/appsmithorg/appsmith && cd appsmith && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** necesitas herramientas internas con lógica y muchas fuentes de datos
**Evita si:** solo quieres hojas colaborativas; mira `nocodb`
**Combina con:** `n8n`
**Alternativas (elige una):** `tooljet`, `budibase`, `nocodb`

## `awesome-n8n-templates`
role=directory · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Reúne workflows de n8n ordenados por tema (Gmail, Telegram, WhatsApp, Notion, OpenAI y más). Sirve para arrancar rápido y aprender patrones de automatización.
**Stack:** JSON de n8n
**Repo:** https://github.com/enescingoz/awesome-n8n-templates

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Awesome n8n Templates/). Si necesitas el código: git clone https://github.com/enescingoz/awesome-n8n-templates`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** usas n8n y quieres partir de flujos hechos
**Evita si:** no usas n8n
**Combina con:** `n8n`, `n8n-mcp`, `n8n-skills`

## `baileys`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Implementa el protocolo de WhatsApp Web directamente, así que consume muy pocos recursos. Es la base de muchas APIs de WhatsApp, incluida Evolution API.
**Stack:** TypeScript, Node.js, WebSocket
**Repo:** https://github.com/WhiskeySockets/Baileys

**Instalación** [~]: `npm install baileys   (o: pnpm add baileys)`
_Nombre npm puede diferir de 'Baileys'; verifica en npmjs.com._

**Elige si:** necesitas WhatsApp en código con bajo consumo de recursos
**Evita si:** prefieres una API REST lista; mira `evolution-api`
**Combina con:** `evolution-api`, `n8n`
**Alternativas (elige una):** `whatsapp-web-js`, `waha`

## `botpress`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Combina un estudio visual con código para crear agentes que usan bases de conocimiento, herramientas y canales. Su producto principal hoy es cloud; el repo contiene SDK, integraciones y CLI.
**Stack:** TypeScript, Node.js
**Repo:** https://github.com/botpress/botpress

**Instalación** [~]: `git clone https://github.com/botpress/botpress && cd botpress && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un agente conversacional multicanal con poco código
**Evita si:** necesitas todo self-host y sin nube; mira `rasa` o `typebot`
**Combina con:** `chatwoot`, `n8n`
**Alternativas (elige una):** `typebot`, `rasa`

## `budibase`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Genera apps CRUD, formularios y flujos a partir de bases existentes y ahora añade agentes de IA agnósticos de modelo. Pensada para equipos de operaciones.
**Stack:** TypeScript, Svelte, Node.js, CouchDB, Docker
**Repo:** https://github.com/Budibase/budibase

**Instalación** [~]: `git clone https://github.com/Budibase/budibase && cd budibase && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres apps internas y agentes en una sola plataforma self-host
**Evita si:** buscas el editor más flexible para backoffices; mira `appsmith`
**Combina con:** `n8n`
**Alternativas (elige una):** `appsmith`, `tooljet`, `nocodb`

## `chatwoot`
role=platform · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Reúne WhatsApp, email, web chat y redes en una sola bandeja, con paso a un humano cuando el bot no basta. Alternativa abierta a Intercom o Zendesk.
**Stack:** Ruby on Rails, Vue.js, PostgreSQL, Redis, Docker
**Repo:** https://github.com/chatwoot/chatwoot

**Instalación** [~]: `git clone https://github.com/chatwoot/chatwoot && cd chatwoot && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** das soporte por varios canales y necesitas handoff humano
**Evita si:** solo necesitas enviar mensajes salientes (evolution-api)
**Combina con:** `evolution-api`, `novu`

## `erpnext`
role=platform · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Cubre la operación completa de una empresa sin licencias de pago. Muy usado por pymes y en manufactura y distribución.
**Stack:** Python, Frappe, MariaDB, JavaScript
**Repo:** https://github.com/frappe/erpnext

**Instalación** [~]: `git clone https://github.com/frappe/erpnext && cd erpnext && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un ERP completo y totalmente libre
**Evita si:** buscas el mayor ecosistema de módulos; mira `odoo`
**Combina con:** `n8n`, `metabase`
**Alternativas (elige una):** `odoo`

## `evolution-api`
role=platform · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Conecta WhatsApp a tu stack mediante una API REST propia, sin quedar atado a un proveedor cerrado.
**Stack:** Node.js/TypeScript, Fastify, Redis, Docker
**Repo:** https://github.com/evolution-foundation/evolution-api

**Instalación** [~]: `git clone https://github.com/evolution-foundation/evolution-api && cd evolution-api && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** operas WhatsApp en producción con varias instancias
**Evita si:** solo necesitas un bot de prueba o un único script (OpenWA basta)
**Combina con:** `n8n`, `chatwoot`
**Alternativas (elige una):** `whatsapp-web-js`, `waha`

## `fluxer`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Apunta a unificar varios modelos generativos tras un cliente único.
**Stack:** web/TS
**Repo:** https://github.com/fluxerapp/fluxer

**Instalación** [?]: `git clone https://github.com/fluxerapp/fluxer (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres probar algo nuevo y seguir su evolución
**Evita si:** necesitas estabilidad de producción (API aún en finalización)
**Combina con:** `open-generative-ai`

## `huginn`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Vigila webs, feeds y APIs y dispara acciones cuando algo cambia, todo alojado por ti y sin depender de terceros.
**Stack:** Ruby on Rails, MySQL/PostgreSQL, self-host
**Repo:** https://github.com/huginn/huginn

**Instalación** [?]: `git clone https://github.com/huginn/huginn (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** automatizas tareas orientadas a eventos y valoras la privacidad
**Evita si:** quieres editor visual moderno o IA nativa (n8n)
**Combina con:** `novu`
**Alternativas (elige una):** `n8n`, `node-red`

## `kestra`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Define flujos en YAML con un editor web, cientos de plugins y disparadores por calendario o eventos. Pensado para equipos de datos y plataforma que quieren orquestación como código.
**Stack:** Java, Vue, YAML, Docker
**Repo:** https://github.com/kestra-io/kestra

**Instalación** [~]: `git clone https://github.com/kestra-io/kestra && cd kestra && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres workflows declarativos en YAML con UI y control de versiones
**Evita si:** buscas automatizaciones de negocio con nodos visuales; mira `n8n`
**Combina con:** `duckdb`, `superset`
**Alternativas (elige una):** `windmill`, `trigger-dev`

## `listmonk`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Envía newsletters y campañas a miles de suscriptores desde un solo binario ligero que consume muy pocos recursos.
**Stack:** Go, PostgreSQL, self-host
**Repo:** https://github.com/knadh/listmonk

**Instalación** [?]: `git clone https://github.com/knadh/listmonk (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres email marketing simple, rápido y propio
**Evita si:** necesitas nurturing avanzado o scoring de leads (mautic)
**Combina con:** `mautic`, `n8n`

## `mautic`
role=platform · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Nutre leads por email con reglas y segmentos automáticos, sin ceder los datos de tus clientes a un SaaS.
**Stack:** PHP/Symfony, MySQL, self-host
**Repo:** https://github.com/mautic/mautic

**Instalación** [?]: `git clone https://github.com/mautic/mautic (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** necesitas automatización de marketing seria y soberana
**Evita si:** te basta una newsletter simple (listmonk)
**Combina con:** `listmonk`, `marketingskills`

## `n8n`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Conecta cualquier app con cualquier otra en tu propio servidor, sin pagar una suscripción mensual por cada flujo.
**Stack:** Node.js, TypeScript, Docker
**Repo:** https://github.com/n8n-io/n8n

**Instalación** [~]: `git clone https://github.com/n8n-io/n8n && cd n8n && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres el motor central de automatización con máximo catálogo
**Evita si:** buscas algo minimalista o sin self-host
**Combina con:** `n8n-mcp`, `n8n-skills`, `evolution-api`
**Alternativas (elige una):** `activepieces`, `huginn`, `windmill`, `node-red`

## `n8n-io`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** No aporta nada distinto a la ficha principal.
**Stack:** Node.js, TypeScript
**Repo:** https://github.com/n8n-io/n8n

**Instalación** [~]: `git clone https://github.com/n8n-io/n8n && cd n8n && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** — **Evita si:** ya usas la ficha n8n (es el mismo proyecto)
**Evita si:** ya usas la ficha n8n (es el mismo proyecto)
**Combina con:** `n8n`

## `n8n-mcp`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** Resuelve el problema de que un LLM invente parámetros de nodos que no existen y genere workflows rotos.
**Stack:** Node.js/TypeScript, MCP
**Repo:** https://github.com/czlonkowski/n8n-mcp

**Instalación** [~]: `git clone https://github.com/czlonkowski/n8n-mcp && cd n8n-mcp && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** generas flujos n8n con IA y quieres menos alucinaciones de parámetros
**Evita si:** no usas n8n o construyes los flujos a mano
**Combina con:** `n8n`, `n8n-skills`

## `n8n-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Enseña a tu agente de código a escribir flujos de n8n en JSON que funcionan a la primera, con menos idas y vueltas de errores.
**Stack:** `SKILL.md`, Markdown
**Repo:** https://github.com/czlonkowski/n8n-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/n8n-skills/). Si necesitas el código: git clone https://github.com/czlonkowski/n8n-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** generas workflows n8n con IA y te cansan los fallos de JSON
**Evita si:** no usas n8n
**Combina con:** `n8n`, `n8n-mcp`

## `nocodb`
role=platform · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Ofrece vistas de tabla, kanban, galería y formularios sobre PostgreSQL, MySQL o SQLite, con API REST automática. Útil como backoffice rápido para equipos no técnicos.
**Stack:** TypeScript, Vue, Node.js, Docker
**Repo:** https://github.com/nocodb/nocodb

**Instalación** [~]: `git clone https://github.com/nocodb/nocodb && cd nocodb && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un Airtable propio sobre tu base de datos
**Evita si:** necesitas apps internas con lógica compleja; mira `appsmith`
**Combina con:** `n8n`
**Alternativas (elige una):** `appsmith`, `budibase`

## `node-red`
role=platform · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Conecta dispositivos, APIs y servicios arrastrando nodos en el navegador. Es muy usado en IoT, domótica e industria por su ligereza y su enorme biblioteca de nodos de la comunidad.
**Stack:** JavaScript, Node.js, Docker
**Repo:** https://github.com/node-red/node-red

**Instalación** [~]: `git clone https://github.com/node-red/node-red && cd node-red && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** trabajas con IoT o eventos y quieres algo ligero y probado
**Evita si:** necesitas integraciones SaaS y nodos de IA listos; mira `n8n`
**Alternativas (elige una):** `n8n`, `huginn`

## `novu`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Envía notificaciones por email, SMS, push y chat desde una sola API, sin integrar y mantener cada proveedor por separado.
**Stack:** Node.js, TypeScript, Docker
**Repo:** https://github.com/novuhq/novu

**Instalación** [~]: `git clone https://github.com/novuhq/novu && cd novu && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** envías notificaciones por varios canales y quieres un único backend
**Evita si:** solo necesitas email (listmonk)
**Combina con:** `chatwoot`, `activepieces`

## `odoo`
role=platform · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Integra CRM, ventas, facturación, inventario, RR. HH. y sitio web en una sola plataforma modular. La usan pymes y grandes empresas en todo el mundo.
**Stack:** Python, PostgreSQL, JavaScript
**Repo:** https://github.com/odoo/odoo

**Instalación** [~]: `git clone https://github.com/odoo/odoo && cd odoo && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas un ERP completo con CRM integrado
**Evita si:** solo quieres un CRM ligero; mira `twenty-main`
**Combina con:** `n8n`, `metabase`
**Alternativas (elige una):** `erpnext`

## `openwa`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Envía y recibe mensajes de WhatsApp desde tu propio script con una API sencilla y expresiva.
**Stack:** Node.js, Puppeteer, bindings Python
**Repo:** https://github.com/rmyndharis/OpenWA

**Instalación** [~]: `pip install openwa   (o: uv add openwa)`
_Nombre PyPI puede diferir de 'OpenWA'; verifica en pypi.org._

**Elige si:** desarrollas scripts o bots individuales y quieres arrancar rápido
**Evita si:** necesitas infra multi-instancia o alta disponibilidad (evolution-api)
**Combina con:** `n8n`, `evolution-api`

## `rasa`
role=runtime · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Permite crear asistentes de texto y voz con control total del diálogo y de los datos. Muy usado en empresas que necesitan bots on-premise y predecibles.
**Stack:** Python, TensorFlow, Docker
**Repo:** https://github.com/RasaHQ/rasa

**Instalación** [~]: `git clone https://github.com/RasaHQ/rasa && cd rasa && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** necesitas un asistente on-premise con diálogo muy controlado
**Evita si:** quieres algo rápido con LLM y sin entrenar; mira `botpress` o `typebot`
**Combina con:** `chatwoot`
**Alternativas (elige una):** `botpress`

## `self-hosted-ai-starter-kit`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Kit oficial de n8n que levanta un entorno de IA privado: n8n para orquestar, Ollama para modelos, Qdrant como base vectorial y PostgreSQL. Útil para prototipar agentes y RAG sin enviar datos fuera.
**Stack:** Docker Compose, n8n, Ollama, Qdrant, PostgreSQL
**Repo:** https://github.com/n8n-io/self-hosted-ai-starter-kit

**Instalación** [~]: `git clone https://github.com/n8n-io/self-hosted-ai-starter-kit && cd self-hosted-ai-starter-kit && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un stack de IA local funcionando hoy con n8n
**Evita si:** vas a producción con alta carga; arma tu propio despliegue
**Combina con:** `n8n`, `ollama`, `qdrant`

## `tooljet`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Construye apps internas arrastrando componentes y conectando bases y APIs, o genéralas describiéndolas con IA. Pensada para equipos de operaciones y TI.
**Stack:** TypeScript, React, Node.js, PostgreSQL
**Repo:** https://github.com/ToolJet/ToolJet

**Instalación** [~]: `git clone https://github.com/ToolJet/ToolJet && cd ToolJet && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres herramientas internas con IA para generarlas
**Evita si:** prefieres un proyecto con licencia más permisiva; mira `appsmith`
**Combina con:** `n8n`
**Alternativas (elige una):** `appsmith`, `budibase`

## `trigger-dev`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Escribe tareas largas o con reintentos en TypeScript dentro de tu app y Trigger.dev las ejecuta, reintenta y monitorea. Ideal para equipos de producto con Next.js o Node que no quieren operar colas.
**Stack:** TypeScript, Node.js, PostgreSQL, Docker
**Repo:** https://github.com/triggerdotdev/trigger.dev

**Instalación** [~]: `git clone https://github.com/triggerdotdev/trigger.dev && cd trigger.dev && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** tu app es TypeScript y necesitas tareas largas confiables sin montar colas
**Evita si:** quieres un editor visual para no programadores; mira `n8n`
**Combina con:** `vercel-ai`, `langfuse`
**Alternativas (elige una):** `windmill`, `kestra`

## `twenty-main`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** La premisa es tratar el CRM como una pieza más de tu stack: lo construyes, lo despliegas y lo versionas igual que el código.
**Stack:** TypeScript, React, NestJS, PostgreSQL, Docker
**Repo:** https://github.com/twentyhq/twenty

**Instalación** [~]: `git clone https://github.com/twentyhq/twenty && cd twenty && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un CRM que se adapte 1:1 a tu negocio y vivir en self-host
**Evita si:** buscas algo plug-and-play gestionado o no quieres operar PostgreSQL y Docker
**Combina con:** `evolution-api`, `n8n`

## `typebot`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Diseña conversaciones con bloques arrastrables (preguntas, condiciones, integraciones, IA) y publícalas en web o WhatsApp. Pensado para captar leads y formularios conversacionales.
**Stack:** TypeScript, Next.js, PostgreSQL, Docker
**Repo:** https://github.com/baptisteArno/typebot.io

**Instalación** [~]: `git clone https://github.com/baptisteArno/typebot.io && cd typebot.io && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un chatbot guiado sin programar, con buena UX
**Evita si:** necesitas un agente abierto con razonamiento libre; mira `botpress`
**Combina con:** `n8n`, `evolution-api`
**Alternativas (elige una):** `botpress`

## `waha`
role=platform · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Expone WhatsApp como API HTTP con webhooks, lista para conectar a n8n o a tu backend. Ofrece motores basados en navegador o en WebSocket.
**Stack:** TypeScript, Go, Docker
**Repo:** https://github.com/devlikeapro/waha

**Instalación** [~]: `git clone https://github.com/devlikeapro/waha && cd waha && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres una API REST de WhatsApp lista en minutos
**Evita si:** necesitas multi-instancia avanzada gratis; mira `evolution-api`
**Combina con:** `n8n`, `chatwoot`
**Alternativas (elige una):** `evolution-api`, `whatsapp-web-js`, `baileys`

## `whatsapp-agentkit`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Arranca un bot de WhatsApp con IA sin escribir código, a partir de una plantilla guiada.
**Stack:** Node.js/Python, APIs de WhatsApp
**Repo:** https://github.com/Hainrixz/whatsapp-agentkit

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/whatsapp-agentkit/). Si necesitas el código: git clone https://github.com/Hainrixz/whatsapp-agentkit`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres arrancar sin partir de cero y te vale con lo que Claude Code genere
**Evita si:** necesitas control fino del stack o ya tienes el bot hecho
**Combina con:** `evolution-api`, `n8n-mcp`

## `whatsapp-web-js`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Permite enviar y recibir mensajes, medios y grupos desde código usando una sesión de WhatsApp Web. Muy usada para bots y prototipos.
**Stack:** JavaScript, Node.js, Puppeteer
**Repo:** https://github.com/wwebjs/whatsapp-web.js

**Instalación** [~]: `npm install whatsapp-web.js   (o: pnpm add whatsapp-web.js)`
_Nombre npm puede diferir de 'whatsapp-web.js'; verifica en npmjs.com._

**Elige si:** quieres programar un bot de WhatsApp en Node rápido
**Evita si:** necesitas una API REST multi-sesión lista; mira `evolution-api` o `waha`
**Combina con:** `n8n`, `chatwoot`
**Alternativas (elige una):** `baileys`, `waha`, `evolution-api`

## `windmill`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Convierte scripts de Python, TypeScript, Go o SQL en workflows, endpoints y apps con UI generada. Sirve a equipos técnicos que quieren la flexibilidad del código con la comodidad de un orquestador visual.
**Stack:** Rust, TypeScript, Svelte, PostgreSQL, Docker
**Repo:** https://github.com/windmill-labs/windmill

**Instalación** [~]: `git clone https://github.com/windmill-labs/windmill && cd windmill && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** tu equipo programa y quiere workflows versionados en código
**Evita si:** prefieres arrastrar nodos sin escribir código; mira `n8n`
**Combina con:** `langfuse`
**Alternativas (elige una):** `n8n`, `kestra`, `trigger-dev`
