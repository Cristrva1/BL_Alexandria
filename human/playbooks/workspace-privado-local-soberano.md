[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 🏠 Workspace privado local soberano

> **Objetivo:** Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros.

## 🗺️ Cómo fluye

```mermaid
flowchart LR
  Usuario["Usuario"] -->|chat| odysseus["odysseus"]
  odysseus["odysseus"] -->|inferencia| ollama["Ollama"]
  Usuario["Usuario"] -->|fuentes| open_notebook["open-notebook"]
  open_notebook["open-notebook"] -->|embeddings + chat| ollama["Ollama"]
  odysseus["odysseus"] -->|memoria| mem0["mem0"]
  odysseus["odysseus"] -->|búsqueda| searxng["SearXNG"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [Ollama](../fichas/ollama.md) | Corre los modelos abiertos en local | 187k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 2 | [odysseus](../fichas/odysseus.md) | Workspace todo-en-uno: chat, documentos y tareas | 95.6k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 3 | [open-notebook](../fichas/open-notebook.md) | Cuaderno de investigación con RAG sobre tus fuentes | 42k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 4 | [mem0](../fichas/mem0.md) | Memoria persistente entre sesiones | 69k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 5 | [SearXNG](../fichas/searxng.md) | Búsqueda web privada cuando hace falta | 39.6k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |

## 🔌 Cómo se conecta

Ollama sirve los modelos en tu equipo con una API local. Odysseus centraliza chat, documentos y tareas; Open Notebook indexa tus fuentes para preguntarles como en NotebookLM; mem0 recuerda preferencias y hechos entre sesiones; SearXNG añade búsqueda web sin rastreo.

## 🚫 Cuándo NO usar esta receta

Si tu equipo no puede correr modelos (poca RAM o sin GPU), apunta las mismas apps a una API comercial vía LiteLLM. Si la privacidad no es un requisito, un SaaS es más simple.

## 🔁 Variantes

- En lugar de [Ollama](../fichas/ollama.md): [llama.cpp](../fichas/llama-cpp.md), [LocalAI](../fichas/localai.md), [llamafile](../fichas/llamafile.md)
- En lugar de [open-notebook](../fichas/open-notebook.md): [DeepTutor](../fichas/deeptutor.md), [SurfSense](../fichas/surfsense.md)
- En lugar de [mem0](../fichas/mem0.md): [Letta](../fichas/letta.md), [cognee](../fichas/cognee.md), [supermemory](../fichas/supermemory.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
