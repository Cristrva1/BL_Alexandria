[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🦾 Mercury Agent

> Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.9k | MIT | TypeScript | 2026-08-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Recuerda lo importante, pide permiso antes de actuar y trae 31 herramientas, tableros kanban y skills extensibles, con datos en SQLite.

## Por qué destaca

Enfoque en seguridad: herramientas con permisos y límites de gasto por diseño.

## Cómo funciona

Un proceso Node mantiene la memoria en SQLite y expone el agente por varios canales con políticas de aprobación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/cosmicstack-labs/mercury-agent/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Mercury Agent para mi objetivo y necesito pasos guiados. Lee https://github.com/cosmicstack-labs/mercury-agent/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Asistente personal con límites de gasto
- Gestión de tareas en kanban por chat
- Agente siempre activo en Telegram

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un asistente personal ligero con permisos claros | buscas el ecosistema más grande; mira `openclaw` |

## Stack y modelos

- **Stack:** TypeScript, SQLite
- **Etiquetas:** `agents` `chatbot` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [claude-mem](claude-mem.md) | 117k | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenClaw](openclaw.md) | 394k | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. |
| [hermes-agent](hermes-agent.md) | 263k | Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. |

## Enlaces

- 🐙 GitHub: [cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)
- 🌐 Web: <https://mercuryagent.sh/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/cosmicstack-labs/mercury-agent/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
