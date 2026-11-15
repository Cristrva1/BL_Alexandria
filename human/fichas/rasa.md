[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Chatbots y asistentes conversacionales

# 🤖 Rasa

> Framework Python para asistentes conversacionales con NLU y gestión de diálogo, desplegables en local.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 21.4k | Apache-2.0 | Python | 2026-07-24 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Permite crear asistentes de texto y voz con control total del diálogo y de los datos. Muy usado en empresas que necesitan bots on-premise y predecibles.

## Por qué destaca

Referencia histórica en bots empresariales; su enfoque CALM combina LLM con flujos controlados.

## Cómo funciona

Un modelo de NLU interpreta mensajes y un gestor de diálogo decide la siguiente acción siguiendo flujos e historias que entrenas.

## Instalación rápida

`pip install rasa` y `rasa init`; las versiones nuevas (Rasa Pro) requieren licencia.

## Casos de uso

- Bot bancario on-premise
- Asistente de soporte con flujos estrictos
- Bots multilingües con datos privados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas un asistente on-premise con diálogo muy controlado | quieres algo rápido con LLM y sin entrenar; mira `botpress` o `typebot` |

**Limitaciones:** El desarrollo activo pasó a Rasa Pro (licencia comercial); la versión abierta avanza poco.

## Stack y modelos

- **Stack:** Python, TensorFlow, Docker
- **Modelos / API:** Modelos propios de NLU; Rasa Pro integra LLM.
- **Etiquetas:** `chatbot` `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [chatwoot](chatwoot.md) | 39.5k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Botpress](botpress.md) | 15k | Plataforma para construir y desplegar agentes conversacionales con LLM en web, WhatsApp y más. |

## Enlaces

- 🐙 GitHub: [RasaHQ/rasa](https://github.com/RasaHQ/rasa)
- 🌐 Web: <https://rasa.com/docs/rasa/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
