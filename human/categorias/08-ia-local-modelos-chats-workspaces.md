[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 7. Inteligencia de Código, Datos & Entrenamiento](07-inteligencia-de-c-digo-datos-entrenamiento.md) · [9. Diseño, UI & Frontend ➡️](09-dise-o-ui-frontend.md)

# 🏠 8. IA Local: Modelos, Chats & Workspaces

> Correr LLMs en tu máquina, interfaces tipo ChatGPT auto-hospedadas, workspaces privados y alternativas a NotebookLM.

**21 repos** · 4 subcategorías · ⭐ 1.3M estrellas en total · 🆕 15 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [Ollama](../fichas/ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. | `curl -fsSL https://ollama.com/install.sh \| sh` |
| [Open WebUI](../fichas/open-webui.md) | 158k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. | `docker run -d -p 3000:8080 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main` |
| [Jan](../fichas/jan.md) | 45.6k | App de escritorio open source, alternativa a ChatGPT que corre 100 % sin conexión. | Descarga el instalador desde jan.ai o los releases. |
| [AnythingLLM](../fichas/anything-llm.md) | 68.1k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. | `docker pull mintplexlabs/anythingllm` |
| [SurfSense](../fichas/surfsense.md) | 16.8k | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. | Self-host con Docker Compose siguiendo la guía del repo. |

## 🧭 Subcategorías

- [Motores para correr modelos en local](#motores-para-correr-modelos-en-local) — 6 repos
- [Interfaces de chat auto-hospedadas](#interfaces-de-chat-auto-hospedadas) — 6 repos
- [Workspaces privados y segundos cerebros](#workspaces-privados-y-segundos-cerebros) — 5 repos
- [NotebookLM: alternativas y clientes](#notebooklm-alternativas-y-clientes) — 4 repos

## Motores para correr modelos en local

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Ollama](../fichas/ollama.md) 🆕 | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. | quieres modelos locales funcionando en minutos | 🟢 |
| [llama.cpp](../fichas/llama-cpp.md) 🆕 | 134k | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. | quieres el máximo control y rendimiento local | 🟡 |
| [LocalAI](../fichas/localai.md) 🆕 | 50.3k | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. | quieres una API tipo OpenAI local para varias modalidades | 🟡 |
| [exo](../fichas/exo.md) 🆕 | 48.3k | Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u oficina. | tienes varios equipos y quieres correr un modelo grande | 🟡 |
| [llmfit](../fichas/llmfit.md) | 38.9k | Herramienta para evaluar y medir el "fit" y la calidad de LLMs en una tarea concreta, orientada a comparar modelos con datos. | necesitas elegir modelo con datos y reproducibilidad | 🟢 |
| [llamafile](../fichas/llamafile.md) 🆕 | 26.6k | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. | quieres repartir un modelo que funcione con doble clic | 🟢 |

## Interfaces de chat auto-hospedadas

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Open WebUI](../fichas/open-webui.md) 🆕 | 158k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. | necesitas un ChatGPT privado para tu equipo | 🟢 |
| ⭐ [Jan](../fichas/jan.md) 🆕 | 45.6k | App de escritorio open source, alternativa a ChatGPT que corre 100 % sin conexión. | quieres un ChatGPT local en tu escritorio | 🟢 |
| [LobeHub](../fichas/lobehub.md) 🆕 | 84.7k | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. | quieres un chat bonito y extensible con agentes | 🟢 |
| [Cherry Studio](../fichas/cherry-studio.md) 🆕 | 53.4k | App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad. | quieres una app de escritorio multi-proveedor completa | 🟢 |
| [Text Generation WebUI](../fichas/textgen.md) 🆕 | 47.7k | App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic. | quieres experimentar con muchos backends locales | 🟡 |
| [LibreChat](../fichas/librechat.md) 🆕 | 46.9k | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. | quieres todos los proveedores en un chat con SSO | 🟡 |

## Workspaces privados y segundos cerebros

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [AnythingLLM](../fichas/anything-llm.md) 🆕 | 68.1k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. | quieres RAG privado sin programar | 🟢 |
| [odysseus](../fichas/odysseus.md) | 95.5k | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. | quieres operación privada todo-en-uno y aceptas operar la infra | 🔴 |
| [PrivateGPT](../fichas/private-gpt.md) 🆕 | 57.6k | Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP. | construyes un producto de IA que no puede enviar datos fuera | 🟡 |
| [Khoj](../fichas/khoj.md) 🆕 | 38.1k | Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. | quieres un asistente sobre tus notas personales | 🟡 |
| [Hermes Desktop](../fichas/hermes-desktop.md) | 14.6k | App de escritorio que envuelve al agente Hermes en una interfaz nativa. | usas Hermes Agent y prefieres una app de escritorio | 🟢 |

## NotebookLM: alternativas y clientes

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [SurfSense](../fichas/surfsense.md) 🆕 | 16.8k | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. | quieres un NotebookLM propio y con más fuentes | 🟡 |
| [open-notebook](../fichas/open-notebook.md) | 41.8k | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. | quieres NotebookLM privado y sin cuotas | 🟡 |
| [notebooklm-py](../fichas/notebooklm-py.md) | 20.2k | API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código. | automatizas el NotebookLM real y aceptas el riesgo de API no oficial | 🟢 |
| [notebooklm-mcp-cli](../fichas/notebooklm-mcp-cli.md) | 6.5k | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP. | integras NotebookLM con tu asistente MCP | 🟢 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### Ollama, llama.cpp, LocalAI, llamafile

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Ollama](../fichas/ollama.md) | 187k | quieres modelos locales funcionando en minutos | necesitas servir a muchos usuarios con GPU; mira `vllm` |
| [llama.cpp](../fichas/llama-cpp.md) | 134k | quieres el máximo control y rendimiento local | prefieres simplicidad; mira `ollama` |
| [LocalAI](../fichas/localai.md) | 50.3k | quieres una API tipo OpenAI local para varias modalidades | solo necesitas chat local simple; mira `ollama` |
| [llamafile](../fichas/llamafile.md) | 26.6k | quieres repartir un modelo que funcione con doble clic | vas a cambiar de modelos a menudo; mira `ollama` |

### Open WebUI, AnythingLLM, Jan, SurfSense, LobeHub, PrivateGPT, Cherry Studio

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Open WebUI](../fichas/open-webui.md) | 158k | necesitas un ChatGPT privado para tu equipo | solo quieres una app de escritorio individual; mira `jan` |
| [AnythingLLM](../fichas/anything-llm.md) | 68.1k | quieres RAG privado sin programar | necesitas un pipeline de RAG a medida; mira `llama-index` |
| [Jan](../fichas/jan.md) | 45.6k | quieres un ChatGPT local en tu escritorio | necesitas multiusuario; mira `open-webui` |
| [SurfSense](../fichas/surfsense.md) | 16.8k | quieres un NotebookLM propio y con más fuentes | solo quieres el NotebookLM de Google por código; mira `notebooklm-py` |
| [LobeHub](../fichas/lobehub.md) | 84.7k | quieres un chat bonito y extensible con agentes | necesitas el máximo control empresarial; mira `librechat` |
| [PrivateGPT](../fichas/private-gpt.md) | 57.6k | construyes un producto de IA que no puede enviar datos fuera | quieres una app lista para usuarios finales; mira `anything-llm` |
| [Cherry Studio](../fichas/cherry-studio.md) | 53.4k | quieres una app de escritorio multi-proveedor completa | solo quieres modelos locales simples; mira `jan` |

## 🧪 Recetas que usan esta categoría

- [🏠 Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md) — Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros.
- [🦙 ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md) — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
