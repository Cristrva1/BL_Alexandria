[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Email, marketing y notificaciones

# 🔔 novu

> Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 40.3k | Otra (ver repo) | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Envía notificaciones por email, SMS, push y chat desde una sola API, sin integrar y mantener cada proveedor por separado.

## Por qué destaca

Es el estándar open-source de referencia para notificaciones, muy adoptado por su API unificada y su inbox unificado. Su modelo de "notification workflows" abstrae el enrutamiento por canal sin acoplarte a un proveedor concreto.

## Cómo funciona

Define workflows de notificación que enrutan mensajes a distintos proveedores por canal (SendGrid, Twilio, FCM…), con un inbox unificado y plantillas, sobre un stack Node.js/TypeScript. Los proveedores se configuran por canal y se pueden intercambiar sin tocar el código de envío.

## Instalación rápida

Vía `docker compose` para self-host, o usando su plataforma cloud; el modo local requiere MongoDB/PostgreSQL y Redis.

## Casos de uso

- Mensajes transaccionales y de producto desde un backend
- Inbox unificado
- Notificaciones multicanal con fallback de proveedor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| envías notificaciones por varios canales y quieres un único backend | solo necesitas email (listmonk) |

## Stack y modelos

- **Stack:** Node.js, TypeScript, Docker
- **Modelos / API:** Compatible con agentes/automatizaciones externas vía API REST.
- **Etiquetas:** `automation` `email` `typescript`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [chatwoot](chatwoot.md) | 39.5k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |
| [activepieces](activepieces.md) | 25.5k | Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables. |

## Enlaces

- 🐙 GitHub: [novuhq/novu](https://github.com/novuhq/novu)
- 🌐 Web: <https://go.novu.co/github>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
