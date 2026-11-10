[🏠 Inicio](../README.md) › [🏠 IA Local: Modelos, Chats & Workspaces](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 Open WebUI

> Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 158k | Otra (ver repo) | Svelte | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Da a tu equipo un chat privado con usuarios, documentos, búsqueda web, herramientas y modelos locales o en la nube.

## Por qué destaca

La UI de chat auto-hospedada más popular, muy completa y activa.

## Cómo funciona

Backend Python y frontend Svelte que se conectan a Ollama o a cualquier API OpenAI, con RAG integrado.

## Instalación rápida

`docker run -d -p 3000:8080 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main`.

## Casos de uso

- ChatGPT privado para tu empresa
- Chat con documentos internos
- Probar modelos locales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas un ChatGPT privado para tu equipo | solo quieres una app de escritorio individual; mira `jan` |

**Limitaciones:** La licencia exige mantener la marca Open WebUI en despliegues grandes.

## Stack y modelos

- **Stack:** Python, Svelte, Docker
- **Modelos / API:** Ollama y cualquier API compatible con OpenAI.
- **Etiquetas:** `chatbot` `local` `rag` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [SearXNG](searxng.md) | 39.4k | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. |
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LibreChat](librechat.md) | 46.9k | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. |
| [LobeHub](lobehub.md) | 84.7k | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. |
| [AnythingLLM](anything-llm.md) | 68.1k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |
| [Text Generation WebUI](textgen.md) | 47.7k | App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic. |

## Enlaces

- 🐙 GitHub: [open-webui/open-webui](https://github.com/open-webui/open-webui)
- 🌐 Web: <https://openwebui.com>
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
