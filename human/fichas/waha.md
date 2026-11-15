[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 💬 WAHA

> API REST de WhatsApp en un contenedor Docker, con varios motores y panel web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.8k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Expone WhatsApp como API HTTP con webhooks, lista para conectar a n8n o a tu backend. Ofrece motores basados en navegador o en WebSocket.

## Por qué destaca

Se levanta con un solo `docker run` y trae Swagger y panel de sesiones.

## Cómo funciona

Envuelve motores como whatsapp-web.js o un cliente Go por WebSocket y los publica como endpoints REST.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/devlikeapro/waha/blob/core/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WAHA para mi objetivo y necesito pasos guiados. Lee https://github.com/devlikeapro/waha/blob/core/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `whatsapp` `automation` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [chatwoot](chatwoot.md) | 39.9k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [whatsapp-web.js](whatsapp-web-js.md) | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. |
| [Baileys](baileys.md) | 11.6k | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. |

## Enlaces

- 🐙 GitHub: [devlikeapro/waha](https://github.com/devlikeapro/waha)
- 🌐 Web: <https://waha.devlike.pro/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/devlikeapro/waha/blob/core/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
