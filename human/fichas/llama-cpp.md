[🏠 Inicio](../README.md) › [🏠 IA Local: Modelos, Chats & Workspaces](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 llama.cpp

> Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 134k | MIT | C++ | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Base de Ollama, LM Studio y muchas apps. Incluye un servidor compatible con OpenAI y herramientas para cuantizar modelos GGUF.

## Por qué destaca

El motor de inferencia local de referencia, con rendimiento excelente en hardware común.

## Cómo funciona

Ejecuta modelos en formato GGUF con kernels optimizados para CPU, Metal, CUDA y Vulkan.

## Instalación rápida

`brew install llama.cpp` o binarios de releases; luego `llama-server -hf ggml-org/gemma-3-1b-it-GGUF`.

## Casos de uso

- Inferencia local con máximo control
- Cuantizar modelos propios
- Servidor ligero compatible con OpenAI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres el máximo control y rendimiento local | prefieres simplicidad; mira `ollama` |

## Stack y modelos

- **Stack:** C++, C, CUDA, Metal
- **Modelos / API:** Modelos abiertos en GGUF.
- **Etiquetas:** `inference` `local` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open WebUI](open-webui.md) | 158k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [llamafile](llamafile.md) | 26.6k | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. |
| [LocalAI](localai.md) | 50.3k | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. |

## Enlaces

- 🐙 GitHub: [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
- 🌐 Web: <https://llama.app>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
