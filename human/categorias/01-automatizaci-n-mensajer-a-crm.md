[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [2. Skills, Prompts & Guías de Agente ➡️](02-skills-prompts-gu-as-de-agente.md)

# 🤖 1. Automatización, Mensajería & CRM

> Motores de workflow, ecosistema n8n, WhatsApp y chat, chatbots, CRM/ERP, email y apps internas.

**32 repos** · 7 subcategorías · ⭐ 1M estrellas en total · 🆕 15 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [n8n](../fichas/n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. | `docker compose` |
| [Self-hosted AI Starter Kit](../fichas/self-hosted-ai-starter-kit.md) | 15.3k | Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos. | `git clone https://github.com/n8n-io/self-hosted-ai-starter-kit` |
| [whatsapp-web.js](../fichas/whatsapp-web-js.md) | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. | `npm i whatsapp-web.js` |
| [Typebot](../fichas/typebot.md) | 10.6k | Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más. | Self-host con Docker Compose siguiendo la guía del repo (requiere PostgreSQL y SMTP), o… |
| [Odoo](../fichas/odoo.md) | 55.7k | Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web. | `docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:16` |
| [novu](../fichas/novu.md) | 40.3k | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. | `docker compose` |
| [NocoDB](../fichas/nocodb.md) | 65.5k | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | `docker run -d -p 8080:8080 nocodb/nocodb:latest` |

## 🧭 Subcategorías

- [Motores de workflow y automatización](#motores-de-workflow-y-automatización) — 7 repos
- [Ecosistema n8n](#ecosistema-n8n) — 4 repos
- [WhatsApp y mensajería](#whatsapp-y-mensajería) — 7 repos
- [Chatbots y asistentes conversacionales](#chatbots-y-asistentes-conversacionales) — 3 repos
- [CRM, ERP y soporte al cliente](#crm-erp-y-soporte-al-cliente) — 4 repos
- [Email, marketing y notificaciones](#email-marketing-y-notificaciones) — 3 repos
- [Apps internas y bases de datos no-code](#apps-internas-y-bases-de-datos-no-code) — 4 repos

## Motores de workflow y automatización

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [n8n](../fichas/n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. | quieres el motor central de automatización con máximo catálogo | 🟡 |
| [huginn](../fichas/huginn.md) | 50.5k | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". | automatizas tareas orientadas a eventos y valoras la privacidad | 🟡 |
| [Kestra](../fichas/kestra.md) 🆕 | 30.2k | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. | quieres workflows declarativos en YAML con UI y control de versiones | 🟡 |
| [activepieces](../fichas/activepieces.md) | 25.5k | Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables. | quieres reemplazar Zapier con piezas propias en TypeScript | 🟡 |
| [Node-RED](../fichas/node-red.md) 🆕 | 23.8k | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. | trabajas con IoT o eventos y quieres algo ligero y probado | 🟢 |
| [Windmill](../fichas/windmill.md) 🆕 | 18.5k | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. | tu equipo programa y quiere workflows versionados en código | 🟡 |
| [Trigger.dev](../fichas/trigger-dev.md) 🆕 | 16.7k | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. | tu app es TypeScript y necesitas tareas largas confiables sin montar colas | 🟡 |

## Ecosistema n8n

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Self-hosted AI Starter Kit](../fichas/self-hosted-ai-starter-kit.md) 🆕 | 15.3k | Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos. | quieres un stack de IA local funcionando hoy con n8n | 🟡 |
| [Awesome n8n Templates](../fichas/awesome-n8n-templates.md) 🆕 | 26.3k | Colección de más de 280 plantillas gratuitas de n8n listas para importar, con IA y apps populares. | usas n8n y quieres partir de flujos hechos | 🟢 |
| [n8n-mcp](../fichas/n8n-mcp.md) | 23.2k | Servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n (816 core + 1.029 comunitarios) para ayudar a construir y depurar flujos. | generas flujos n8n con IA y quieres menos alucinaciones de parámetros | 🟡 |
| [n8n-skills](../fichas/n8n-skills.md) | 6.6k | Conjunto de 14 skills estructuradas para Claude Code orientadas a construir flujos de n8n correctos, evitando errores al generar su JSON. | generas workflows n8n con IA y te cansan los fallos de JSON | 🟢 |

## WhatsApp y mensajería

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [whatsapp-web.js](../fichas/whatsapp-web-js.md) 🆕 | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. | quieres programar un bot de WhatsApp en Node rápido | 🟢 |
| [OpenWA](../fichas/openwa.md) | 16.7k | Gateway/SDK abierto para conectar y automatizar cuentas de WhatsApp de forma directa desde código, sin infraestructura pesada. | desarrollas scripts o bots individuales y quieres arrancar rápido | 🟢 |
| [Baileys](../fichas/baileys.md) 🆕 | 11.6k | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. | necesitas WhatsApp en código con bajo consumo de recursos | 🟢 |
| [fluxer](../fichas/fluxer.md) | 10.8k | Plataforma generativa emergente con foco en audio y video mejorados, ofrecida como cliente Canary web/desktop; su API y self-host aún están en finalización. | quieres probar algo nuevo y seguir su evolución | 🟡 |
| [evolution-api](../fichas/evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. | operas WhatsApp en producción con varias instancias | 🔴 |
| [WAHA](../fichas/waha.md) 🆕 | 7.8k | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. | quieres una API REST de WhatsApp lista en minutos | 🟢 |
| [whatsapp-agentkit](../fichas/whatsapp-agentkit.md) | 554 | Plantilla guiada que construye un agente conversacional de WhatsApp en menos de 30 minutos sin necesidad de programar, partiendo de preguntas sobre tu negocio. | quieres arrancar sin partir de cero y te vale con lo que Claude Code genere | 🟢 |

## Chatbots y asistentes conversacionales

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Typebot](../fichas/typebot.md) 🆕 | 10.6k | Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más. | quieres un chatbot guiado sin programar, con buena UX | 🟡 |
| [Rasa](../fichas/rasa.md) 🆕 | 21.4k | Framework Python para asistentes conversacionales con NLU y gestión de diálogo, desplegables en local. | necesitas un asistente on-premise con diálogo muy controlado | 🔴 |
| [Botpress](../fichas/botpress.md) 🆕 | 15k | Plataforma para construir y desplegar agentes conversacionales con LLM en web, WhatsApp y más. | quieres un agente conversacional multicanal con poco código | 🟡 |

## CRM, ERP y soporte al cliente

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Odoo](../fichas/odoo.md) 🆕 | 55.7k | Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web. | necesitas un ERP completo con CRM integrado | 🔴 |
| [twenty-main](../fichas/twenty-main.md) | 60.7k | CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modelas con tus propios objetos, campos y relaciones. | quieres un CRM que se adapte 1:1 a tu negocio y vivir en self-host | 🔴 |
| [ERPNext](../fichas/erpnext.md) 🆕 | 41.1k | ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura. | quieres un ERP completo y totalmente libre | 🔴 |
| [chatwoot](../fichas/chatwoot.md) | 39.5k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. | das soporte por varios canales y necesitas handoff humano | 🔴 |

## Email, marketing y notificaciones

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [novu](../fichas/novu.md) | 40.3k | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. | envías notificaciones por varios canales y quieres un único backend | 🟡 |
| [listmonk](../fichas/listmonk.md) | 24.2k | Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS. | quieres email marketing simple, rápido y propio | 🟡 |
| [mautic](../fichas/mautic.md) | 11k | Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo. | necesitas automatización de marketing seria y soberana | 🔴 |

## Apps internas y bases de datos no-code

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [NocoDB](../fichas/nocodb.md) 🆕 | 65.5k | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | quieres un Airtable propio sobre tu base de datos | 🟢 |
| [ToolJet](../fichas/tooljet.md) | 41.2k | Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA. | quieres herramientas internas con IA para generarlas | 🟡 |
| [Appsmith](../fichas/appsmith.md) | 41.2k | Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. | necesitas herramientas internas con lógica y muchas fuentes de datos | 🟡 |
| [Budibase](../fichas/budibase.md) | 28.4k | Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. | quieres apps internas y agentes en una sola plataforma self-host | 🟡 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### n8n, huginn, Kestra, activepieces, Node-RED, Windmill, Trigger.dev

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [n8n](../fichas/n8n.md) | 210k | quieres el motor central de automatización con máximo catálogo | buscas algo minimalista o sin self-host |
| [huginn](../fichas/huginn.md) | 50.5k | automatizas tareas orientadas a eventos y valoras la privacidad | quieres editor visual moderno o IA nativa (n8n) |
| [Kestra](../fichas/kestra.md) | 30.2k | quieres workflows declarativos en YAML con UI y control de versiones | buscas automatizaciones de negocio con nodos visuales; mira `n8n` |
| [activepieces](../fichas/activepieces.md) | 25.5k | quieres reemplazar Zapier con piezas propias en TypeScript | ya dominas n8n y su ecosistema te basta |
| [Node-RED](../fichas/node-red.md) | 23.8k | trabajas con IoT o eventos y quieres algo ligero y probado | necesitas integraciones SaaS y nodos de IA listos; mira `n8n` |
| [Windmill](../fichas/windmill.md) | 18.5k | tu equipo programa y quiere workflows versionados en código | prefieres arrastrar nodos sin escribir código; mira `n8n` |
| [Trigger.dev](../fichas/trigger-dev.md) | 16.7k | tu app es TypeScript y necesitas tareas largas confiables sin montar colas | quieres un editor visual para no programadores; mira `n8n` |

### whatsapp-web.js, Baileys, evolution-api, WAHA

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [whatsapp-web.js](../fichas/whatsapp-web-js.md) | 22.9k | quieres programar un bot de WhatsApp en Node rápido | necesitas una API REST multi-sesión lista; mira `evolution-api` o `waha` |
| [Baileys](../fichas/baileys.md) | 11.6k | necesitas WhatsApp en código con bajo consumo de recursos | prefieres una API REST lista; mira `evolution-api` |
| [evolution-api](../fichas/evolution-api.md) | 10.1k | operas WhatsApp en producción con varias instancias | solo necesitas un bot de prueba o un único script (OpenWA basta) |
| [WAHA](../fichas/waha.md) | 7.8k | quieres una API REST de WhatsApp lista en minutos | necesitas multi-instancia avanzada gratis; mira `evolution-api` |

### Typebot, Rasa, Botpress

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Typebot](../fichas/typebot.md) | 10.6k | quieres un chatbot guiado sin programar, con buena UX | necesitas un agente abierto con razonamiento libre; mira `botpress` |
| [Rasa](../fichas/rasa.md) | 21.4k | necesitas un asistente on-premise con diálogo muy controlado | quieres algo rápido con LLM y sin entrenar; mira `botpress` o `typebot` |
| [Botpress](../fichas/botpress.md) | 15k | quieres un agente conversacional multicanal con poco código | necesitas todo self-host y sin nube; mira `rasa` o `typebot` |

### Odoo, ERPNext

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Odoo](../fichas/odoo.md) | 55.7k | necesitas un ERP completo con CRM integrado | solo quieres un CRM ligero; mira `twenty-main` |
| [ERPNext](../fichas/erpnext.md) | 41.1k | quieres un ERP completo y totalmente libre | buscas el mayor ecosistema de módulos; mira `odoo` |

### NocoDB, ToolJet, Appsmith, Budibase

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [NocoDB](../fichas/nocodb.md) | 65.5k | quieres un Airtable propio sobre tu base de datos | necesitas apps internas con lógica compleja; mira `appsmith` |
| [ToolJet](../fichas/tooljet.md) | 41.2k | quieres herramientas internas con IA para generarlas | prefieres un proyecto con licencia más permisiva; mira `appsmith` |
| [Appsmith](../fichas/appsmith.md) | 41.2k | necesitas herramientas internas con lógica y muchas fuentes de datos | solo quieres hojas colaborativas; mira `nocodb` |
| [Budibase](../fichas/budibase.md) | 28.4k | quieres apps internas y agentes en una sola plataforma self-host | buscas el editor más flexible para backoffices; mira `appsmith` |

## 🧪 Recetas que usan esta categoría

- [💬 Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md) — Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta.
- [📈 Marketing de agencia](../playbooks/marketing-de-agencia.md) — Operar campañas, contenido y email a escala con agentes y herramientas propias.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
