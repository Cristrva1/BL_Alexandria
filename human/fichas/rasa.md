[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Chatbots y asistentes conversacionales

# 🤖 Rasa

> Framework Python para asistentes conversacionales con NLU y gestión de diálogo, desplegables en local.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 21.4k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Permite crear asistentes de texto y voz con control total del diálogo y de los datos. Muy usado en empresas que necesitan bots on-premise y predecibles.

## Por qué destaca

Referencia histórica en bots empresariales; su enfoque CALM combina LLM con flujos controlados.

## Cómo funciona

Un modelo de NLU interpreta mensajes y un gestor de diálogo decide la siguiente acción siguiendo flujos e historias que entrenas.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/RasaHQ/rasa/blob/3.6.x/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Rasa para mi objetivo y necesito pasos guiados. Lee https://github.com/RasaHQ/rasa/blob/3.6.x/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `chatbot` `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [chatwoot](chatwoot.md) | 39.9k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Botpress](botpress.md) | 15k | Plataforma para construir y desplegar agentes conversacionales con LLM en web, WhatsApp y más. |

## Enlaces

- 🐙 GitHub: [RasaHQ/rasa](https://github.com/RasaHQ/rasa)
- 🌐 Web: <https://rasa.com/docs/rasa/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/RasaHQ/rasa/blob/3.6.x/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
