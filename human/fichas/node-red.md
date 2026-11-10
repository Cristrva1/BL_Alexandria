[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Node-RED

> Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 23.8k | Apache-2.0 | JavaScript | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Qué es

Conecta dispositivos, APIs y servicios arrastrando nodos en el navegador. Es muy usado en IoT, domótica e industria por su ligereza y su enorme biblioteca de nodos de la comunidad.

## Por qué destaca

Proyecto veterano de la OpenJS Foundation, estable y ligero; corre hasta en una Raspberry Pi.

## Cómo funciona

Cada flujo es un grafo de nodos JavaScript que intercambian mensajes; se guarda como JSON y se ejecuta en un runtime Node.js.

## Instalación rápida

`npm install -g --unsafe-perm node-red` y luego `node-red`, o `docker run -it -p 1880:1880 nodered/node-red`.

## Casos de uso

- Automatizar sensores y domótica
- Puentes MQTT, HTTP y bases de datos
- Alertas simples por eventos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas con IoT o eventos y quieres algo ligero y probado | necesitas integraciones SaaS y nodos de IA listos; mira `n8n` |

## Stack y modelos

- **Stack:** JavaScript, Node.js, Docker
- **Modelos / API:** No usa LLM de serie; hay nodos de la comunidad para OpenAI y Ollama.
- **Etiquetas:** `automation` `javascript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [huginn](huginn.md) | 50.5k | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". |

## Enlaces

- 🐙 GitHub: [node-red/node-red](https://github.com/node-red/node-red)
- 🌐 Web: <http://nodered.org>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
