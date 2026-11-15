[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Asistentes autónomos y equipos de agentes

# ☤ hermes-agent

> Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 263k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

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
| Otras rutas | El proyecto documenta una suscripción propia de Nous Portal además de otros proveedores; los servicios incluidos y sus límites pertenecen a ese plan. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local.

## Por qué destaca

Aprovecha el razonamiento estructurado de los modelos Hermes y prioriza la ejecución local frente a depender de la nube. Su rasgo distintivo es un learning loop: el agente crea skills desde la experiencia y persiste conocimiento entre sesiones.

## Cómo funciona

Una app de escritorio (Tauri) coordina agentes con backend Python que invocan modelos Hermes locales o APIs comerciales como fallback, guardando memoria y skills autoaprendidas.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/NousResearch/hermes-agent/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar hermes-agent para mi objetivo y necesito pasos guiados. Lee https://github.com/NousResearch/hermes-agent/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Delegar tareas en sandbox local
- Panel de control de escritorio (Tauri)
- Agente que acumula skills con el uso

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres agentes locales con UI y memoria persistente | prefieres orquestación en nube o no quieres compilar Tauri |

**Limitaciones:** El build de Tauri y los pesos locales elevan la barrera de entrada frente a una solución hosted.

## Stack y modelos

- **Stack:** Rust (Tauri), TypeScript, Python
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ECC](ecc.md) | 303k | Colección de plugins, skills, hooks y convenciones para organizar el trabajo de agentes de código en un proyecto. |
| [odysseus](odysseus.md) | 95.6k | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenClaw](openclaw.md) | 394k | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. |
| [Mercury Agent](mercury-agent.md) | 3.9k | Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. |

## Enlaces

- 🐙 GitHub: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 🌐 Web: <https://hermes-agent.nousresearch.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/NousResearch/hermes-agent/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
