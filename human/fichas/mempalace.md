[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🏛️ mempalace

> Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 60.5k | MIT | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Resuelve la memoria privada: cero llamadas a API, tus textos no salen de tu máquina.

## Por qué destaca

Prioriza la privacidad total (cero llamadas a API) reportando recall competitivo en benchmarks de memoria de largo plazo. Su diseño verbatim evita la pérdida de detalle que sufren los enfoques que resumen con un LLM remoto.

## Cómo funciona

Guarda los textos verbatim y los recupera mediante un backend de búsqueda conectable, sin depender de un LLM remoto para almacenar ni para indexar; el backend se puede cambiar según tus necesidades.

## Instalación rápida

`pip install` desde PyPI; se configura el backend de búsqueda local según el repo. No requiere claves de API ni servicios externos.

## Casos de uso

- Memoria privada para agentes
- Recuerdo de largo plazo sin enviar datos a la nube
- Casos con requisitos de confidencialidad (sanidad, legal)

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| la privacidad es prioridad y no quieres llamadas a API | quieres un SaaS gestionado con escalado automático o integraciones de framework ya hechas (mem0) |

## Stack y modelos

- **Stack:** Python (PyPI)
- **Modelos / API:** Local, backend conectable; sin proveedor LLM obligatorio.
- **Etiquetas:** `memory` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [open-notebook](open-notebook.md) | 41.8k | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. |
| [odysseus](odysseus.md) | 95.5k | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. |

## Enlaces

- 🐙 GitHub: [MemPalace/mempalace](https://github.com/MemPalace/mempalace)
- 🌐 Web: <http://mempalaceofficial.com/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
