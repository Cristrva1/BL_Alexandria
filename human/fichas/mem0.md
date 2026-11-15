[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 mem0

> Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 68.7k | Apache-2.0 | Python | 2026-11-06 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Resuelve el "amnesia" del LLM: el agente conserva preferencias y hechos entre sesiones sin reenviar todo el historial.

## Por qué destaca

Es uno de los proyectos de memoria de agentes más adoptados, con SDK estable en Python y TS e integraciones amplias en el ecosistema de frameworks (LangChain, CrewAI, etc.). Su enfoque de extracción+actualización incremental de hechos evita duplicados y desactualizaciones.

## Cómo funciona

Combina extracción de hechos vía LLM con almacenamiento en vector DBs (Qdrant, Chroma, etc.) para indexar y consultar memorias relevantes por similitud, actualizando o borrando recuerdos contradictorios en lugar de solo acumularlos.

## Instalación rápida

`pip install mem0ai` (también SDK en npm) o servicio gestionado; requiere un LLM y una vector DB configurados (o los defaults del cloud).

## Casos de uso

- Recordar preferencias del usuario entre sesiones
- Memoria long-term para agentes
- Personalización acumulativa sin inflar el prompt

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres memoria estándar lista con integraciones amplias | necesitas todo local sin llamadas a API (mempalace) o control total del almacenamiento |

## Stack y modelos

- **Stack:** Python/TypeScript, vector DBs (Qdrant, Chroma, pgvector)
- **Modelos / API:** Múltiples LLMs + vector DBs; agnóstico vía variables de entorno.
- **Etiquetas:** `memory` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [crewAI](crewai.md) | 60.7k | Framework para orquestar "crews" de agentes con roles y tareas. |
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [agentmemory](agentmemory.md) | 30.3k | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Letta](letta.md) | 25.4k | Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT). |
| [cognee](cognee.md) | 33.2k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. |
| [supermemory](supermemory.md) | 31.6k | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. |

## Enlaces

- 🐙 GitHub: [mem0ai/mem0](https://github.com/mem0ai/mem0)
- 🌐 Web: <https://mem0.ai>
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
