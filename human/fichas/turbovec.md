[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# ⚡ turbovec

> Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 17.5k | MIT | Rust | 2026-10-07 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Resuelve el coste de memoria y cómputo de la búsqueda vectorial cuando una vector DB completa es demasiado para tu escala.

## Por qué destaca

Apuesta por la eficiencia, aplicando una técnica de cuantización moderna para acelerar la búsqueda con bajo coste de memoria. Sus bindings en Python y Rust la hacen usable desde ambos ecosistemas sin cambiar de stack.

## Cómo funciona

Comprime los vectores con TurboQuant y resuelve las consultas por similitud directamente sobre la representación cuantizada, con bindings disponibles en Python y Rust para integrarse en pipelines existentes.

## Instalación rápida

`pip install` (Python) o crate de Rust según el repo; sin servicios externos ni GPU obligatoria para inferencia.

## Casos de uso

- Capa de recuperación para RAG
- Vector search eficiente embebido
- Sustituto ligero de una vector DB cuando no necesitas persistencia distribuida

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas vector search veloz y embebido sin desplegar una DB | ya usas una vector DB completa con persistencia y escalado horizontal |

## Stack y modelos

- **Stack:** Python / Rust
- **Modelos / API:** N/A (infra de vectores).
- **Etiquetas:** `automation` `vector-db` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mem0](mem0.md) | 68.7k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |

## Enlaces

- 🐙 GitHub: [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec)
- 🌐 Web: <https://pypi.org/project/turbovec/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
