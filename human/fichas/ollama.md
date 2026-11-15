[🏠 Inicio](../README.md) › [🏠 IA Local: Modelos, Chats & Workspaces](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 Ollama

> La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 187k | MIT | Go | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Qué es

Un comando para bajar y ejecutar modelos como Qwen, Gemma, DeepSeek o gpt-oss. Casi todas las apps de IA local lo soportan.

## Por qué destaca

Experiencia muy simple y el ecosistema de integraciones más amplio en IA local.

## Cómo funciona

Usa llama.cpp por debajo, gestiona modelos cuantizados y sirve una API REST local.

## Instalación rápida

`curl -fsSL https://ollama.com/install.sh | sh` (o el instalador de macOS/Windows) y `ollama run qwen3`.

## Casos de uso

- Usar modelos locales en n8n
- Backend local para Open WebUI
- Programar con modelos privados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres modelos locales funcionando en minutos | necesitas servir a muchos usuarios con GPU; mira `vllm` |

## Stack y modelos

- **Stack:** Go, C++
- **Modelos / API:** Modelos abiertos locales.
- **Etiquetas:** `inference` `local` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open WebUI](open-webui.md) | 158k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [AnythingLLM](anything-llm.md) | 68.1k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [llama.cpp](llama-cpp.md) | 134k | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. |
| [LocalAI](localai.md) | 50.3k | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. |
| [llamafile](llamafile.md) | 26.6k | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. |

## Enlaces

- 🐙 GitHub: [ollama/ollama](https://github.com/ollama/ollama)
- 🌐 Web: <https://ollama.com>
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
