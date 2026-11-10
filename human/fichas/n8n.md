[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 n8n

> Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 210k | Otra (ver repo) | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Resuelve la primitiva de "conectar todo con todo" en self-host, sin el coste recurrente de un SaaS.

## Por qué destaca

Se ha convertido en un estándar de facto para automatización self-hosted, muy adoptado por su enorme catálogo de nodos y su fuerte integración de IA (LangChain, MCP). Su comunidad y su documentación lo hacen el punto de partida habitual.

## Cómo funciona

Encadena nodos (triggers, transformaciones, integraciones) en un grafo de workflow ejecutado por un runtime Node.js, con nodos de IA basados en LangChain y soporte MCP. Los workflows se exportan como JSON, lo que permite versionarlos.

## Instalación rápida

Vía `docker compose` o imagen Docker oficial; también `npx n8n` para una prueba rápida local. Requiere una base de datos (SQLite por defecto, PostgreSQL para producción).

## Casos de uso

- Extraer leads → enriquecer con IA → notificar
- Pipelines de negocio sin SaaS cerrado
- Workflows versionados como JSON junto al código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres el motor central de automatización con máximo catálogo | buscas algo minimalista o sin self-host |

**Limitaciones:** La versión self-host comunitaria tiene límites en ejecuciones y usuarios; algunas funciones avanzadas requieren licencia.

## Stack y modelos

- **Stack:** Node.js, TypeScript, Docker
- **Modelos / API:** Múltiples por nodo (OpenAI, Anthropic…); se potencia con MCP y LLMs.
- **Etiquetas:** `automation` `typescript` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n-mcp](n8n-mcp.md) | 23.2k | Servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n (816 core + 1.029 comunitarios) para ayudar a construir y depurar flujos. |
| [n8n-skills](n8n-skills.md) | 6.6k | Conjunto de 14 skills estructuradas para Claude Code orientadas a construir flujos de n8n correctos, evitando errores al generar su JSON. |
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [activepieces](activepieces.md) | 25.5k | Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables. |
| [huginn](huginn.md) | 50.5k | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". |
| [Windmill](windmill.md) | 18.5k | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. |
| [Node-RED](node-red.md) | 23.8k | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. |

## Enlaces

- 🐙 GitHub: [n8n-io/n8n](https://github.com/n8n-io/n8n)
- 🌐 Web: <https://n8n.io>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
