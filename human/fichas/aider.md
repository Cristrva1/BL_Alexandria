[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 👨‍💻 Aider

> Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 50k | Apache-2.0 | Python | 2026-05-22 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Qué es

Le pides cambios en lenguaje natural y Aider edita los archivos y confirma cada cambio en Git. Funciona con casi cualquier modelo.

## Por qué destaca

Pionero del género, con un mapa del repo eficiente y benchmarks públicos de modelos.

## Cómo funciona

Construye un mapa del repositorio con tree-sitter, envía al modelo solo el contexto relevante y aplica las ediciones como diffs.

## Instalación rápida

`python -m pip install aider-install && aider-install` y luego `aider` en tu repo.

## Casos de uso

- Cambios rápidos con commits limpios
- Programar con modelos locales
- Pair programming en la terminal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un agente sencillo que trabaje con Git paso a paso | necesitas autonomía en tareas largas; mira `claude-code` |

## Stack y modelos

- **Stack:** Python, tree-sitter, Git
- **Modelos / API:** Agnóstico: Claude, GPT, DeepSeek, Ollama y más.
- **Etiquetas:** `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenCode](opencode.md) | 226k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| [Cline](cline.md) | 71.5k | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. |
| [Continue](continue.md) | 36.5k | Agente de código open source para VS Code, JetBrains y CI, con chat, autocompletado y revisiones. |

## Enlaces

- 🐙 GitHub: [Aider-AI/aider](https://github.com/Aider-AI/aider)
- 🌐 Web: <https://aider.chat/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
