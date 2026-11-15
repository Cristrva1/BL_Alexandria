[🏠 Inicio](../README.md) › [🏠 IA Local: Modelos, Chats & Workspaces](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 LocalAI

> Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 50.3k | MIT | Go | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Sustituye la API de OpenAI por una propia que corre modelos abiertos de muchos tipos. Útil para apps que ya hablan con OpenAI.

## Por qué destaca

Reemplazo directo de la API de OpenAI con múltiples modalidades en un solo servidor.

## Cómo funciona

Orquesta varios backends (llama.cpp, whisper, diffusers) detrás de endpoints compatibles con OpenAI.

## Instalación rápida

`docker run -p 8080:8080 --name local-ai -ti localai/localai:latest`.

## Casos de uso

- Sustituir OpenAI en una app existente
- Texto, voz e imagen en un servidor
- IA privada on-premise

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres una API tipo OpenAI local para varias modalidades | solo necesitas chat local simple; mira `ollama` |

## Stack y modelos

- **Stack:** Go, C++, Docker
- **Modelos / API:** Modelos abiertos locales.
- **Etiquetas:** `inference` `local` `go` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AnythingLLM](anything-llm.md) | 68.1k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [llama.cpp](llama-cpp.md) | 134k | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. |

## Enlaces

- 🐙 GitHub: [mudler/LocalAI](https://github.com/mudler/LocalAI)
- 🌐 Web: <https://localai.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
