[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › WhatsApp y mensajería

# 💬 whatsapp-web.js

> Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 22.9k | Apache-2.0 | JavaScript | 2026-11-08 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Permite enviar y recibir mensajes, medios y grupos desde código usando una sesión de WhatsApp Web. Muy usada para bots y prototipos.

## Por qué destaca

Muy popular y documentada, con una API sencilla orientada a eventos.

## Cómo funciona

Lanza Chromium con Puppeteer, inicia sesión con un QR y expone los eventos de WhatsApp Web como API de Node.

## Instalación rápida

`npm i whatsapp-web.js` y escanea el QR que muestra al arrancar.

## Casos de uso

- Bots de respuesta automática
- Notificaciones a clientes
- Integrar WhatsApp con tu backend

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres programar un bot de WhatsApp en Node rápido | necesitas una API REST multi-sesión lista; mira `evolution-api` o `waha` |

**Limitaciones:** No es oficial: WhatsApp puede bloquear números que automatizan; usa la API oficial para volumen.

## Stack y modelos

- **Stack:** JavaScript, Node.js, Puppeteer
- **Modelos / API:** No usa LLM; conéctalo tú a la API que quieras.
- **Etiquetas:** `whatsapp` `chatbot` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [chatwoot](chatwoot.md) | 39.5k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Baileys](baileys.md) | 11.6k | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. |
| [WAHA](waha.md) | 7.8k | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. |
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |

## Enlaces

- 🐙 GitHub: [wwebjs/whatsapp-web.js](https://github.com/wwebjs/whatsapp-web.js)
- 🌐 Web: <https://wwebjs.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
