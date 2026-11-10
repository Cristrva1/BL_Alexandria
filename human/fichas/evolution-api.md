[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › WhatsApp y mensajería

# 🧬 evolution-api

> API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 10.1k | Otra (ver repo) | TypeScript | 2026-11-06 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Conecta WhatsApp a tu stack mediante una API REST propia, sin quedar atado a un proveedor cerrado.

## Por qué destaca

Es una de las puertas de enlace de WhatsApp open-source más usadas en LATAM y Brasil para producción, con comunidad activa y soporte de webhooks, multi-instancia y gestión de sesiones. Su adopción la convierte en el puente habitual hacia n8n o chatwoot.

## Cómo funciona

Mantiene sesiones de WhatsApp por instancia (vía Baileys/whatsapp-web.js) y reenvía eventos vía webhooks, apoyándose en Node.js/Fastify y Redis para estado y colas. Cada instancia se gestiona por API REST, lo que permite escalar horizontalmente con Docker.

## Instalación rápida

Despliegue habitual con `docker compose` usando la imagen oficial, configurando variables de entorno y Redis; requiere mantener las sesiones de WhatsApp activas.

## Casos de uso

- Notificaciones de pedidos/facturas
- Enrutar mensajes a agentes vía webhook
- Puente entre WhatsApp y un LLM en n8n

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| operas WhatsApp en producción con varias instancias | solo necesitas un bot de prueba o un único script (OpenWA basta) |

**Limitaciones:** Las sesiones de WhatsApp pueden caer y requieren supervisión; el ToS de WhatsApp limita volumen y automatización masiva.

## Stack y modelos

- **Stack:** Node.js/TypeScript, Fastify, Redis, Docker
- **Modelos / API:** No usa IA directa; es el puente al LLM que tú orquestes.
- **Etiquetas:** `automation` `whatsapp` `typescript` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [chatwoot](chatwoot.md) | 39.5k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whatsapp-web.js](whatsapp-web-js.md) | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. |
| [WAHA](waha.md) | 7.8k | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. |

## Enlaces

- 🐙 GitHub: [evolution-foundation/evolution-api](https://github.com/evolution-foundation/evolution-api)
- 🌐 Web: <https://evolutionfoundation.com.br>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
