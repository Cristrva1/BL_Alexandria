[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# WhatsApp, mensajería y chatbots

Conecta WhatsApp y otros canales o prepara un chatbot. Distingue el canal de mensajes, el modelo que responde y la bandeja donde una persona retoma la conversación.

11 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [whatsapp-web.js](../fichas/whatsapp-web-js.md) | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. | Sin API de IA en la ruta básica |
| [Typebot](../fichas/typebot.md) | Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más. | API de IA opcional |

## Secciones

- [WhatsApp y mensajería](#whatsapp-y-mensajería) — 8 repos
- [Chatbots y asistentes conversacionales](#chatbots-y-asistentes-conversacionales) — 3 repos

## WhatsApp y mensajería

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [whatsapp-web.js](../fichas/whatsapp-web-js.md) | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. | quieres programar un bot de WhatsApp en Node rápido | Sin API de IA en la ruta básica |
| [OpenWA](../fichas/openwa.md) | Gateway/SDK abierto para conectar y automatizar cuentas de WhatsApp de forma directa desde código, sin infraestructura pesada. | desarrollas scripts o bots individuales y quieres arrancar rápido | Sin API de IA en la ruta básica |
| [Baileys](../fichas/baileys.md) | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. | necesitas WhatsApp en código con bajo consumo de recursos | Sin API de IA en la ruta básica |
| [fluxer](../fichas/fluxer.md) | Aplicación de mensajería instantánea y llamadas de voz para comunidades, con código abierto y opciones de alojamiento propio. | quieres probar algo nuevo y seguir su evolución | Sin API de IA en la ruta básica |
| [evolution-api](../fichas/evolution-api.md) | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. | operas WhatsApp en producción con varias instancias | Sin API de IA en la ruta básica |
| [whatsmeow](../fichas/whatsmeow.md) | Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp Web. | necesitas integrar WhatsApp Web en un servicio escrito en Go | Sin API de IA en la ruta básica |
| [WAHA](../fichas/waha.md) | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. | quieres una API REST de WhatsApp lista en minutos | Sin API de IA en la ruta básica |
| [whatsapp-agentkit](../fichas/whatsapp-agentkit.md) | Plantilla guiada que construye un agente conversacional de WhatsApp en menos de 30 minutos sin necesidad de programar, partiendo de preguntas sobre tu negocio. | quieres arrancar sin partir de cero y te vale con lo que Claude Code genere | API de IA necesaria |

## Chatbots y asistentes conversacionales

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Typebot](../fichas/typebot.md) | Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más. | quieres un chatbot guiado sin programar, con buena UX | API de IA opcional |
| [Rasa](../fichas/rasa.md) | Framework Python para asistentes conversacionales con NLU y gestión de diálogo, desplegables en local. | necesitas un asistente on-premise con diálogo muy controlado | Depende de la ruta elegida |
| [Botpress](../fichas/botpress.md) | Plataforma para construir y desplegar agentes conversacionales con LLM en web, WhatsApp y más. | quieres un agente conversacional multicanal con poco código | Depende de la ruta elegida |

## Recetas relacionadas

- [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md) — Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
