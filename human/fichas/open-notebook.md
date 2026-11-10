[🏠 Inicio](../README.md) › [🏠 IA Local: Modelos, Chats & Workspaces](../categorias/08-ia-local-modelos-chats-workspaces.md) › NotebookLM: alternativas y clientes

# 📓 open-notebook

> Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 41.8k | MIT | TypeScript | 2026-11-08 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

Resuelve el envío de documentos sensibles a la nube que implica el NotebookLM oficial.

## Por qué destaca

Cubre la demanda de un NotebookLM sin envío de datos a la nube y es uno de los proyectos de referencia en la comunidad open-source para este caso. Su autor (lfnovo) lo mantiene activo con soporte para modelos locales y comerciales.

## Cómo funciona

Un backend FastAPI indexa las fuentes y las consulta vía RAG contra modelos servidos por Ollama, con una UI React/Next.js para notebooks y generación de audio.

## Instalación rápida

`docker` (imagen oficial) o `pip` más Ollama para los modelos locales. Requiere Ollama instalado y al menos un modelo descargado (p. ej. Llama 3) para el modo 100% local.

## Casos de uso

- Subir un manual y generar un audio explicativo
- Chats de consulta sobre tus PDFs privados
- Síntesis temática de varias fuentes sin cuotas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres NotebookLM privado y sin cuotas | prefieres el NotebookLM real automatizado (notebooklm-py) |

## Stack y modelos

- **Stack:** Python (FastAPI), React/Next.js
- **Modelos / API:** Llama 3/Gemma 2 vía Ollama o APIs comerciales.
- **Etiquetas:** `notebooks` `research` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [odysseus](odysseus.md) | 95.5k | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. |
| [markitdown](markitdown.md) | 195k | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DeepTutor](deeptutor.md) | 57.8k | Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos. |
| [SurfSense](surfsense.md) | 16.8k | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. |

## Enlaces

- 🐙 GitHub: [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)
- 🌐 Web: <https://www.open-notebook.ai>
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
