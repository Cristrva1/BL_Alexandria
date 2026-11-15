[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 🧬 evolution-api

> API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.1k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

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

Conecta WhatsApp a tu stack mediante una API REST propia, sin quedar atado a un proveedor cerrado.

## Por qué destaca

Es una de las puertas de enlace de WhatsApp open-source más usadas en LATAM y Brasil para producción, con comunidad activa y soporte de webhooks, multi-instancia y gestión de sesiones. Su adopción la convierte en el puente habitual hacia n8n o chatwoot.

## Cómo funciona

Mantiene sesiones de WhatsApp por instancia (vía Baileys/whatsapp-web.js) y reenvía eventos vía webhooks, apoyándose en Node.js/Fastify y Redis para estado y colas. Cada instancia se gestiona por API REST, lo que permite escalar horizontalmente con Docker.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/evolution-foundation/evolution-api/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar evolution-api para mi objetivo y necesito pasos guiados. Lee https://github.com/evolution-foundation/evolution-api/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `automation` `whatsapp` `typescript` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [chatwoot](chatwoot.md) | 39.9k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whatsapp-web.js](whatsapp-web-js.md) | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. |
| [WAHA](waha.md) | 7.8k | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. |

## Enlaces

- 🐙 GitHub: [evolution-foundation/evolution-api](https://github.com/evolution-foundation/evolution-api)
- 🌐 Web: <https://evolutionfoundation.com.br>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/evolution-foundation/evolution-api/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
