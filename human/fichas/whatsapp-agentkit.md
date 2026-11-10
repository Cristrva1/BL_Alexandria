[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › WhatsApp y mensajería

# 🤖 whatsapp-agentkit

> Plantilla guiada que construye un agente conversacional de WhatsApp en menos de 30 minutos sin necesidad de programar, partiendo de preguntas sobre tu negocio.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 554 | MIT | Python | 2026-10-25 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Resuelve la primitiva de "arrancar un bot de WhatsApp sin tocar código".

## Por qué destaca

Baja drásticamente la barrera de entrada al delegar la generación del código en Claude Code, ideal para arranques rápidos y perfiles no técnicos. El resultado es código real que luego puedes editar, no una caja negra.

## Cómo funciona

Un flujo de preguntas conversacionales alimenta a Claude Code, que autogenera el código del bot (Node.js/Python) y la configuración del webhook de WhatsApp. El asistente hace las veces de scaffolder guiado por tus respuestas.

## Instalación rápida

`git clone` del repo y seguir el asistente con Claude Code; requiere una clave API de Anthropic y una cuenta/instancia de WhatsApp para el webhook.

## Casos de uso

- Prototipo de atención al cliente
- Setup de webhook por preguntas conversacionales
- Demo de ventas por WhatsApp en una tarde

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres arrancar sin partir de cero y te vale con lo que Claude Code genere | necesitas control fino del stack o ya tienes el bot hecho |

## Stack y modelos

- **Stack:** Node.js/Python, APIs de WhatsApp
- **Modelos / API:** Claude (Code / Sonnet) para la autogeneración del bot.
- **Etiquetas:** `agents` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [n8n-mcp](n8n-mcp.md) | 23.2k | Servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n (816 core + 1.029 comunitarios) para ayudar a construir y depurar flujos. |

## Enlaces

- 🐙 GitHub: [Hainrixz/whatsapp-agentkit](https://github.com/Hainrixz/whatsapp-agentkit)
- 🌐 Web: <https://hainrixz.github.io/whatsapp-agentkit/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
