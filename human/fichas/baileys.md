[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › WhatsApp y mensajería

# 💬 Baileys

> Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.6k | MIT | JavaScript | 2026-11-10 |

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

Implementa el protocolo de WhatsApp Web directamente, así que consume muy pocos recursos. Es la base de muchas APIs de WhatsApp, incluida Evolution API.

## Por qué destaca

Ligera y rápida porque no necesita Chromium; ideal para muchas sesiones.

## Cómo funciona

Se conecta por WebSocket a los servidores de WhatsApp como si fuera un dispositivo vinculado, con cifrado de extremo a extremo.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Baileys para mi objetivo y necesito pasos guiados. Lee https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Bots ligeros en servidores pequeños
- Base para tu propia API de WhatsApp
- Multi-sesión con pocos recursos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas WhatsApp en código con bajo consumo de recursos | prefieres una API REST lista; mira `evolution-api` |

**Limitaciones:** No es oficial: hay riesgo de bloqueo del número.

## Stack y modelos

- **Stack:** TypeScript, Node.js, WebSocket
- **Etiquetas:** `whatsapp` `chatbot` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whatsapp-web.js](whatsapp-web-js.md) | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. |
| [WAHA](waha.md) | 7.8k | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. |

## Enlaces

- 🐙 GitHub: [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys)
- 🌐 Web: <https://baileys.wiki/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
