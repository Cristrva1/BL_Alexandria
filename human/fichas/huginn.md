[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🤖 huginn

> Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú".

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 50.5k | MIT | Ruby | 2026-11-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Vigila webs, feeds y APIs y dispara acciones cuando algo cambia, todo alojado por ti y sin depender de terceros.

## Por qué destaca

Proyecto veterano y muy respetado en la comunidad open-source para monitoreo y scraping, valorado por su privacidad y su modelo de agentes encadenables. Su longevidad lo hace una opción estable para flujos de vigilancia.

## Cómo funciona

Define "agents" que hacen polling o reciben webhooks y se conectan entre sí pasando eventos (la salida de uno alimenta al siguiente), sobre un stack Ruby on Rails con base de datos. Cada agent tiene un tipo (trigger, acción, filtro) y se configura por UI o YAML.

## Instalación rápida

Vía `docker` (imagen oficial) o desplegando la app Rails manualmente; requiere MySQL/PostgreSQL y un entorno Ruby.

## Casos de uso

- Vigilar fuentes externas y disparar acciones
- Scraping + reglas de automatización
- Encadenar eventos entre servicios sin SaaS

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| automatizas tareas orientadas a eventos y valoras la privacidad | quieres editor visual moderno o IA nativa (n8n) |

**Limitaciones:** Proyecto veterano con ritmo de mantenimiento lento; sin IA integrada y UI menos pulida que alternativas modernas.

## Stack y modelos

- **Stack:** Ruby on Rails, MySQL/PostgreSQL, self-host
- **Modelos / API:** No nativa; se integra vía APIs y webhooks.
- **Etiquetas:** `automation` `ruby` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [novu](novu.md) | 40.3k | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [Node-RED](node-red.md) | 23.8k | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. |

## Enlaces

- 🐙 GitHub: [huginn/huginn](https://github.com/huginn/huginn)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
