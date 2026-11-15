[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › WhatsApp y mensajería

# 💬 whatsapp-web.js

> Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 22.9k | Apache-2.0 | JavaScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

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

Permite enviar y recibir mensajes, medios y grupos desde código usando una sesión de WhatsApp Web. Muy usada para bots y prototipos.

## Por qué destaca

Muy popular y documentada, con una API sencilla orientada a eventos.

## Cómo funciona

Lanza Chromium con Puppeteer, inicia sesión con un QR y expone los eventos de WhatsApp Web como API de Node.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
npm install whatsapp-web.js
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/wwebjs/whatsapp-web.js/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whatsapp-web.js para mi objetivo y necesito pasos guiados. Lee https://github.com/wwebjs/whatsapp-web.js/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `whatsapp` `chatbot` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [chatwoot](chatwoot.md) | 39.9k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Baileys](baileys.md) | 11.6k | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. |
| [WAHA](waha.md) | 7.8k | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. |
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |

## Enlaces

- 🐙 GitHub: [wwebjs/whatsapp-web.js](https://github.com/wwebjs/whatsapp-web.js)
- 🌐 Web: <https://wwebjs.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/wwebjs/whatsapp-web.js/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
