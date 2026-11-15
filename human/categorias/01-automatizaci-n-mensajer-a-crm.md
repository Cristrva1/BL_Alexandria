[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Automatizar procesos y crear herramientas internas

Motores de flujos, ecosistema n8n y aplicaciones internas. Elige el motor del proceso y conecta después sus fuentes de datos, canales y modelos.

16 repos · 3 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [n8n](../fichas/n8n.md) | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. | API de IA opcional |
| [Self-hosted AI Starter Kit](../fichas/self-hosted-ai-starter-kit.md) | Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos. | Sin API de IA en la ruta básica |
| [NocoDB](../fichas/nocodb.md) | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | Sin API de IA en la ruta básica |

## Secciones

- [Motores de workflow y automatización](#motores-de-workflow-y-automatización) — 8 repos
- [Ecosistema n8n](#ecosistema-n8n) — 4 repos
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

## Apps internas y bases de datos no-code

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [NocoDB](../fichas/nocodb.md) | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | quieres un Airtable propio sobre tu base de datos | Sin API de IA en la ruta básica |
| [Appsmith](../fichas/appsmith.md) | Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. | necesitas herramientas internas con lógica y muchas fuentes de datos | API de IA opcional |
| [ToolJet](../fichas/tooljet.md) | Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA. | quieres herramientas internas con IA para generarlas | API de IA opcional |
| [Budibase](../fichas/budibase.md) | Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. | quieres apps internas y agentes en una sola plataforma self-host | API de IA opcional |

## Recetas relacionadas

- [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md) — Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
