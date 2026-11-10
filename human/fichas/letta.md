[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 Letta

> Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT).

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 25.4k | Apache-2.0 | — | 2026-10-18 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Crea agentes que gestionan su propia memoria en bloques editables y archivos, y persisten entre conversaciones. Incluye servidor, API y entorno de desarrollo.

## Por qué destaca

Nació del paper MemGPT; referencia en agentes con memoria de largo plazo.

## Cómo funciona

El agente edita su memoria con herramientas; el servidor guarda el estado en una base de datos y lo expone por API.

## Instalación rápida

`docker run -p 8283:8283 letta/letta:latest` o `pip install letta-client` para su cloud.

## Casos de uso

- Asistentes que recuerdan a cada cliente
- Agentes que mejoran con el uso
- Compañeros de investigación persistentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres agentes con memoria de largo plazo gestionada | solo necesitas una capa de memoria para tu app; mira `mem0` |

## Stack y modelos

- **Stack:** Python, PostgreSQL
- **Modelos / API:** Agnóstico.
- **Etiquetas:** `memory` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mem0](mem0.md) | 68.7k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [cognee](cognee.md) | 33.2k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. |

## Enlaces

- 🐙 GitHub: [letta-ai/letta](https://github.com/letta-ai/letta)
- 🌐 Web: <https://docs.letta.com/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
