[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 👨‍💻 SWE-agent

> Agente de Princeton y Stanford que toma un issue de GitHub e intenta resolverlo solo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 20.8k | MIT | Python | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Resuelve issues reales con el modelo que elijas y sirve como base de investigación en agentes de software. También tiene usos en ciberseguridad y retos de programación.

## Por qué destaca

Referencia académica en SWE-bench, con una interfaz agente-computadora bien estudiada.

## Cómo funciona

Da al modelo comandos específicos para navegar, editar y probar código dentro de un contenedor Docker.

## Instalación rápida

`pip install sweagent` (requiere Docker) y ejecuta `sweagent run` con la URL del issue.

## Casos de uso

- Resolver issues automáticamente
- Experimentar con agentes de software
- Evaluar modelos en SWE-bench

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| investigas o automatizas la resolución de issues | quieres un asistente diario en tu terminal; mira `claude-code` |

## Stack y modelos

- **Stack:** Python, Docker
- **Modelos / API:** Agnóstico vía LiteLLM: Claude, GPT y otros.
- **Etiquetas:** `coding-agent` `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SWE-bench](swe-bench.md) | 6.2k | Benchmark para evaluar si los modelos resuelven issues reales de GitHub. |
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenHands](openhands.md) | 93.1k | Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). |
| [Open SWE](open-swe.md) | 11.2k | Agente de código asíncrono de LangChain para montar tu propio agente interno de ingeniería. |

## Enlaces

- 🐙 GitHub: [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent)
- 🌐 Web: <https://swe-agent.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
