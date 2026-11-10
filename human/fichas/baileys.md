[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › WhatsApp y mensajería

# 💬 Baileys

> Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 11.6k | MIT | JavaScript | 2026-11-08 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Implementa el protocolo de WhatsApp Web directamente, así que consume muy pocos recursos. Es la base de muchas APIs de WhatsApp, incluida Evolution API.

## Por qué destaca

Ligera y rápida porque no necesita Chromium; ideal para muchas sesiones.

## Cómo funciona

Se conecta por WebSocket a los servidores de WhatsApp como si fuera un dispositivo vinculado, con cifrado de extremo a extremo.

## Instalación rápida

`npm i baileys` y vincula la sesión con QR o código de emparejamiento.

## Casos de uso

- Bots ligeros en servidores pequeños
- Base para tu propia API de WhatsApp
- Multi-sesión con pocos recursos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas WhatsApp en código con bajo consumo de recursos | prefieres una API REST lista; mira `evolution-api` |

**Limitaciones:** No es oficial: hay riesgo de bloqueo del número.

## Stack y modelos

- **Stack:** TypeScript, Node.js, WebSocket
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `whatsapp` `chatbot` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whatsapp-web.js](whatsapp-web-js.md) | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. |
| [WAHA](waha.md) | 7.8k | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. |

## Enlaces

- 🐙 GitHub: [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys)
- 🌐 Web: <https://baileys.wiki/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
