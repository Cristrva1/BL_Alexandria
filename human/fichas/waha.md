[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › WhatsApp y mensajería

# 💬 WAHA

> API REST de WhatsApp en un contenedor Docker, con varios motores y panel web.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 7.8k | Apache-2.0 | TypeScript | 2026-11-06 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Qué es

Expone WhatsApp como API HTTP con webhooks, lista para conectar a n8n o a tu backend. Ofrece motores basados en navegador o en WebSocket.

## Por qué destaca

Se levanta con un solo `docker run` y trae Swagger y panel de sesiones.

## Cómo funciona

Envuelve motores como whatsapp-web.js o un cliente Go por WebSocket y los publica como endpoints REST.

## Instalación rápida

`docker run -it -p 3000:3000 devlikeapro/waha` y abre `http://localhost:3000`.

## Casos de uso

- Conectar WhatsApp a n8n por webhook
- Atención automática con IA
- Envíos transaccionales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres una API REST de WhatsApp lista en minutos | necesitas multi-instancia avanzada gratis; mira `evolution-api` |

**Limitaciones:** Algunas funciones (varias sesiones, medios) requieren la versión Plus de pago.

## Stack y modelos

- **Stack:** TypeScript, Go, Docker
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `whatsapp` `automation` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [chatwoot](chatwoot.md) | 39.5k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [whatsapp-web.js](whatsapp-web-js.md) | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. |
| [Baileys](baileys.md) | 11.6k | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. |

## Enlaces

- 🐙 GitHub: [devlikeapro/waha](https://github.com/devlikeapro/waha)
- 🌐 Web: <https://waha.devlike.pro/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
