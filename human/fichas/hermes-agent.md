[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Asistentes autónomos y equipos de agentes

# ☤ hermes-agent

> Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 262k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local.

## Por qué destaca

Aprovecha el razonamiento estructurado de los modelos Hermes y prioriza la ejecución local frente a depender de la nube. Su rasgo distintivo es un learning loop: el agente crea skills desde la experiencia y persiste conocimiento entre sesiones.

## Cómo funciona

Una app de escritorio (Tauri) coordina agentes con backend Python que invocan modelos Hermes locales o APIs comerciales como fallback, guardando memoria y skills autoaprendidas.

## Instalación rápida

`git clone` y build con Tauri/Cargo (más dependencias Python). Para modo local puro necesitas pesos de Hermes y una GPU razonable; sin GPU puede usar APIs comerciales.

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
- **Modelos / API:** Hermes-3-Llama-3 local + APIs comerciales (OpenAI, Anthropic) como fallback.
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ECC](ecc.md) | 300k | Sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura. |
| [odysseus](odysseus.md) | 95.5k | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenClaw](openclaw.md) | 394k | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. |
| [Mercury Agent](mercury-agent.md) | 3.9k | Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. |

## Enlaces

- 🐙 GitHub: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 🌐 Web: <https://hermes-agent.nousresearch.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
