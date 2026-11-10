[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › CRM, ERP y soporte al cliente

# 💬 chatwoot

> Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 39.5k | Otra (ver repo) | Ruby | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Resuelve la primitiva de "bandeja omnicanal con handoff humano" como alternativa a Intercom/Zendesk.

## Por qué destaca

Es una de las alternativas open-source más populares a Intercom/Zendesk, valorada por centralizar el soporte multicanal con handoff humano y asignación de tickets. Su comunidad activa y su integración con canales la hacen apta para producción.

## Cómo funciona

Centraliza conversaciones por canal en una bandeja con tickets y agentes, sobre un stack Ruby on Rails con PostgreSQL y Redis para tiempo real. Los agentes responden desde un panel unificado y los bots pueden intervenir antes del handoff.

## Instalación rápida

Vía `docker compose` con la imagen oficial, o instalación manual del stack Rails; requiere PostgreSQL y Redis.

## Casos de uso

- Centralizar WhatsApp/web/correo en un panel
- Tickets y agentes con handoff bot→humano
- Soporte multicanal para una agencia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| das soporte por varios canales y necesitas handoff humano | solo necesitas enviar mensajes salientes (evolution-api) |

**Limitaciones:** Self-host con varios componentes (app, worker, Redis, Postgres); el setup y las actualizaciones corren por tu cuenta.

## Stack y modelos

- **Stack:** Ruby on Rails, Vue.js, PostgreSQL, Redis, Docker
- **Modelos / API:** Integración externa de IA vía webhooks.
- **Etiquetas:** `automation` `crm` `ruby` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [novu](novu.md) | 40.3k | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. |

## Enlaces

- 🐙 GitHub: [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)
- 🌐 Web: <https://www.chatwoot.com/help-center>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
