[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › WhatsApp y mensajería

# 🌐 OpenWA

> Gateway/SDK abierto para conectar y automatizar cuentas de WhatsApp de forma directa desde código, sin infraestructura pesada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.9k | MIT | TypeScript | 2026-06-23 |

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

Envía y recibe mensajes de WhatsApp desde tu propio script con una API sencilla y expresiva.

## Por qué destaca

Muy adoptado para prototipos y bots individuales por su simplicidad y su API expresiva, con una comunidad consolidada alrededor de wa-automate. Es la opción ligera cuando evolution-api es excesivo.

## Cómo funciona

Controla una sesión de WhatsApp Web mediante automatización del navegador (Puppeteer) y expone eventos y métodos a tus scripts en Node.js, con bindings para Python. Cada sesión vive en un proceso, sin Redis ni orquestador.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/rmyndharis/OpenWA/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenWA para mi objetivo y necesito pasos guiados. Lee https://github.com/rmyndharis/OpenWA/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Bot que escucha eventos y ejecuta scripts locales
- Respuestas rápidas con panel local
- Prototipo de agente conversacional en una sola máquina

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| desarrollas scripts o bots individuales y quieres arrancar rápido | necesitas infra multi-instancia o alta disponibilidad (evolution-api) |

**Limitaciones:** Depende de automatizar el navegador, lo que es frágil ante cambios de WhatsApp Web; no está pensado para producción a escala.

## Stack y modelos

- **Stack:** Node.js, Puppeteer, bindings Python
- **Etiquetas:** `whatsapp` `chatbot` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |

## Enlaces

- 🐙 GitHub: [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA)
- 🌐 Web: <https://www.open-wa.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/rmyndharis/OpenWA/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
