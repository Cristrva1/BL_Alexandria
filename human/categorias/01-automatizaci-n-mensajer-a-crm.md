[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Automatizar negocios y comunicación

Conecta aplicaciones, organiza clientes, atiende mensajes o programa procesos. Empieza por un motor de flujos; añade canales y CRM según tu objetivo.

39 repos · 7 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [n8n](../fichas/n8n.md) | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. | API de IA opcional |
| [Self-hosted AI Starter Kit](../fichas/self-hosted-ai-starter-kit.md) | Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos. | Sin API de IA en la ruta básica |
| [whatsapp-web.js](../fichas/whatsapp-web-js.md) | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. | Sin API de IA en la ruta básica |
| [Typebot](../fichas/typebot.md) | Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más. | API de IA opcional |
| [Odoo](../fichas/odoo.md) | Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web. | Sin API de IA en la ruta básica |
| [novu](../fichas/novu.md) | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. | Sin API de IA en la ruta básica |
| [NocoDB](../fichas/nocodb.md) | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | Sin API de IA en la ruta básica |

## Secciones

- [Motores de workflow y automatización](#motores-de-workflow-y-automatización) — 8 repos
- [Ecosistema n8n](#ecosistema-n8n) — 4 repos
- [WhatsApp y mensajería](#whatsapp-y-mensajería) — 8 repos
- [Chatbots y asistentes conversacionales](#chatbots-y-asistentes-conversacionales) — 3 repos
- [CRM, ERP y soporte al cliente](#crm-erp-y-soporte-al-cliente) — 5 repos
- [Email, marketing y notificaciones](#email-marketing-y-notificaciones) — 7 repos
- [Apps internas y bases de datos no-code](#apps-internas-y-bases-de-datos-no-code) — 4 repos

## Motores de workflow y automatización

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [n8n](../fichas/n8n.md) | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. | quieres el motor central de automatización con máximo catálogo | API de IA opcional |
| [huginn](../fichas/huginn.md) | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". | automatizas tareas orientadas a eventos y valoras la privacidad | Sin API de IA en la ruta básica |
| [cal.diy](../fichas/cal-diy.md) | Edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia. | quieres estudiar una agenda autoalojada para uso personal | Sin API de IA en la ruta básica |
| [Kestra](../fichas/kestra.md) | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. | quieres workflows declarativos en YAML con UI y control de versiones | API de IA opcional |
| [activepieces](../fichas/activepieces.md) | Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables. | quieres reemplazar Zapier con piezas propias en TypeScript | API de IA opcional |
| [Node-RED](../fichas/node-red.md) | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. | trabajas con IoT o eventos y quieres algo ligero y probado | Sin API de IA en la ruta básica |
| [Windmill](../fichas/windmill.md) | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. | tu equipo programa y quiere workflows versionados en código | API de IA opcional |
| [Trigger.dev](../fichas/trigger-dev.md) | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. | tu app es TypeScript y necesitas tareas largas confiables sin montar colas | API de IA opcional |

## Ecosistema n8n

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Self-hosted AI Starter Kit](../fichas/self-hosted-ai-starter-kit.md) | Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos. | quieres un stack de IA local funcionando hoy con n8n | Sin API de IA en la ruta básica |
| [Awesome n8n Templates](../fichas/awesome-n8n-templates.md) | Colección de plantillas de n8n para estudiar o importar automatizaciones de servicios y tareas habituales. | usas n8n y quieres partir de flujos hechos | Sin API de IA en la ruta básica |
| [n8n-mcp](../fichas/n8n-mcp.md) | Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows. | generas flujos n8n con IA y quieres menos alucinaciones de parámetros | Sin API de IA en la ruta básica |
| [n8n-skills](../fichas/n8n-skills.md) | Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas. | generas workflows n8n con IA y te cansan los fallos de JSON | Sin API de IA en la ruta básica |

## WhatsApp y mensajería

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [whatsapp-web.js](../fichas/whatsapp-web-js.md) | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. | quieres programar un bot de WhatsApp en Node rápido | Sin API de IA en la ruta básica |
| [OpenWA](../fichas/openwa.md) | Gateway/SDK abierto para conectar y automatizar cuentas de WhatsApp de forma directa desde código, sin infraestructura pesada. | desarrollas scripts o bots individuales y quieres arrancar rápido | Sin API de IA en la ruta básica |
| [Baileys](../fichas/baileys.md) | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. | necesitas WhatsApp en código con bajo consumo de recursos | Sin API de IA en la ruta básica |
| [fluxer](../fichas/fluxer.md) | Aplicación de mensajería instantánea y llamadas de voz para comunidades, con código abierto y opciones de alojamiento propio. | quieres probar algo nuevo y seguir su evolución | Sin API de IA en la ruta básica |
| [evolution-api](../fichas/evolution-api.md) | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. | operas WhatsApp en producción con varias instancias | Sin API de IA en la ruta básica |
| [whatsmeow](../fichas/whatsmeow.md) | Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp Web. | necesitas integrar WhatsApp Web en un servicio escrito en Go | Sin API de IA en la ruta básica |
| [WAHA](../fichas/waha.md) | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. | quieres una API REST de WhatsApp lista en minutos | Sin API de IA en la ruta básica |
| [whatsapp-agentkit](../fichas/whatsapp-agentkit.md) | Plantilla guiada que construye un agente conversacional de WhatsApp en menos de 30 minutos sin necesidad de programar, partiendo de preguntas sobre tu negocio. | quieres arrancar sin partir de cero y te vale con lo que Claude Code genere | API de IA necesaria |

## Chatbots y asistentes conversacionales

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Typebot](../fichas/typebot.md) | Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más. | quieres un chatbot guiado sin programar, con buena UX | API de IA opcional |
| [Rasa](../fichas/rasa.md) | Framework Python para asistentes conversacionales con NLU y gestión de diálogo, desplegables en local. | necesitas un asistente on-premise con diálogo muy controlado | Depende de la ruta elegida |
| [Botpress](../fichas/botpress.md) | Plataforma para construir y desplegar agentes conversacionales con LLM en web, WhatsApp y más. | quieres un agente conversacional multicanal con poco código | Depende de la ruta elegida |

## CRM, ERP y soporte al cliente

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Odoo](../fichas/odoo.md) | Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web. | necesitas un ERP completo con CRM integrado | Sin API de IA en la ruta básica |
| [twenty-main](../fichas/twenty-main.md) | CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modelas con tus propios objetos, campos y relaciones. | quieres un CRM que se adapte 1:1 a tu negocio y vivir en self-host | API de IA opcional |
| [ERPNext](../fichas/erpnext.md) | ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura. | quieres un ERP completo y totalmente libre | Sin API de IA en la ruta básica |
| [chatwoot](../fichas/chatwoot.md) | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. | das soporte por varios canales y necesitas handoff humano | API de IA opcional |
| [crm](../fichas/compai-crm.md) | CRM de Comp AI diseñado alrededor de agentes que investigan contactos, organizan tareas y registran evidencia. | quieres estudiar un CRM donde el agente organiza el seguimiento | API de IA opcional |

## Email, marketing y notificaciones

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [novu](../fichas/novu.md) | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. | envías notificaciones por varios canales y quieres un único backend | Sin API de IA en la ruta básica |
| [postiz-app](../fichas/postiz-app.md) | Plataforma para preparar, programar y gestionar publicaciones en redes sociales, con integraciones y funciones de IA. | buscas esta función: Plataforma para preparar, programar y gestionar publicaciones en redes sociales, con integraciones y funciones de IA. | API de IA opcional |
| [open-seo](../fichas/open-seo.md) | Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO y permite alojamiento propio. | buscas esta función: Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO y permite alojamiento propio. | Sin API de IA en la ruta básica |
| [listmonk](../fichas/listmonk.md) | Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS. | quieres email marketing simple, rápido y propio | Sin API de IA en la ruta básica |
| [cloud-mail](../fichas/cloud-mail.md) | Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y funciones de mensajería de un dominio. | buscas esta función: Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y funciones de mensajería de un dominio. | Sin API de IA en la ruta básica |
| [mautic](../fichas/mautic.md) | Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo. | necesitas automatización de marketing seria y soberana | Sin API de IA en la ruta básica |
| [sellbird](../fichas/sellbird.md) | Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes. | buscas esta función: Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes. | Sin API de IA en la ruta básica |

## Apps internas y bases de datos no-code

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [NocoDB](../fichas/nocodb.md) | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | quieres un Airtable propio sobre tu base de datos | Sin API de IA en la ruta básica |
| [Appsmith](../fichas/appsmith.md) | Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. | necesitas herramientas internas con lógica y muchas fuentes de datos | API de IA opcional |
| [ToolJet](../fichas/tooljet.md) | Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA. | quieres herramientas internas con IA para generarlas | API de IA opcional |
| [Budibase](../fichas/budibase.md) | Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. | quieres apps internas y agentes en una sola plataforma self-host | API de IA opcional |

## Recetas relacionadas

- [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md) — Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta.
- [Marketing de agencia](../playbooks/marketing-de-agencia.md) — Operar campañas, contenido y email a escala con agentes y herramientas propias.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
