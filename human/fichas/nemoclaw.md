[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ NemoClaw

> Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 23k | Apache-2.0 | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Ejecuta agentes populares dentro de los sandboxes de NVIDIA OpenShell con inferencia gestionada y políticas de seguridad. Pensado para empresas.

## Por qué destaca

Añade aislamiento y control a agentes muy capaces que normalmente corren con acceso total.

## Cómo funciona

Envuelve el agente en un sandbox OpenShell con políticas de red y archivos, y le da modelos vía inferencia gestionada.

## Instalación rápida

Sigue la guía del repo (requiere el entorno de NVIDIA OpenShell).

## Casos de uso

- Desplegar OpenClaw con aislamiento
- Agentes corporativos con políticas
- Inferencia gestionada para agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres correr agentes potentes con aislamiento corporativo | solo necesitas un sandbox para ejecutar código; mira `e2b` |

## Stack y modelos

- **Stack:** TypeScript, contenedores
- **Modelos / API:** Modelos NVIDIA (Nemotron) y otros vía inferencia gestionada.
- **Etiquetas:** `agents` `security` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenClaw](openclaw.md) | 394k | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. |
| [hermes-agent](hermes-agent.md) | 262k | Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. |
| [Nemotron (NVIDIA)](nemotron.md) | 2.3k | Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [sandbox](sandbox.md) | 6.3k | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |

## Enlaces

- 🐙 GitHub: [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)
- 🌐 Web: <https://docs.nvidia.com/nemoclaw/latest/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
