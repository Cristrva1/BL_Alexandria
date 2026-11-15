[🏠 Inicio](../README.md) › [🏠 IA Local: Modelos, Chats & Workspaces](../categorias/08-ia-local-modelos-chats-workspaces.md) › Workspaces privados y segundos cerebros

# ⛺ odysseus

> Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 95.5k | AGPL-3.0 | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Sustituye la dispersión entre varios SaaS por un único panel que tú controlas.

## Por qué destaca

Ofrece una alternativa local y soberana a las suites tipo Copilot/Workspace AI, juntando en un solo lugar lo que normalmente reparten varios servicios cerrados. Su enfoque todo-en-uno sobre stack open-source lo hace atractivo para perfiles técnicos que priorizan privacidad.

## Cómo funciona

Un backend Python orquesta los agentes sobre una base PostgreSQL y una UI React, conectando con modelos locales vía Ollama/Llama.cpp o con APIs comerciales para razonar sobre tus datos.

## Instalación rápida

`docker compose` para levantar backend, base de datos y frontend, o despliegue manual con Python y Node. Requiere PostgreSQL y un endpoint de modelo (Ollama local o API key comercial).

## Casos de uso

- Asistente administrativo privado que redacta correos y agenda desde tus documentos
- Research sobre tu propia base de conocimiento
- Sustituto self-host de Copilot personal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres operación privada todo-en-uno y aceptas operar la infra | prefieres SaaS gestionado sin mantenimiento |

## Stack y modelos

- **Stack:** Python, React, PostgreSQL
- **Modelos / API:** Ollama/Llama.cpp o APIs comerciales (agnóstico vía configuración).
- **Etiquetas:** `agents` `local` `python` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [open-notebook](open-notebook.md) | 41.8k | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. |
| [ECC](ecc.md) | 300k | Sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura. |
| [mem0](mem0.md) | 68.7k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |

## Enlaces

- 🐙 GitHub: [odysseus-dev/odysseus](https://github.com/odysseus-dev/odysseus)
- 🌐 Web: <https://odysseus-dev.github.io/odysseus>
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
