[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 tree-sitter

> Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 27.4k | MIT | Rust | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Genera parsers rápidos que actualizan el árbol sintáctico mientras editas. Lo usan editores, Aider, ast-grep y muchas herramientas de código con IA.

## Por qué destaca

Estándar de facto para parsing en herramientas de código.

## Cómo funciona

Gramáticas por lenguaje se compilan a parsers en C que producen árboles concretos de forma incremental.

## Instalación rápida

`npm i -g tree-sitter-cli` o los bindings de tu lenguaje (`pip install tree-sitter`).

## Casos de uso

- Construir herramientas de análisis de código
- Resaltado de sintaxis
- Mapas de repos para agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| construyes herramientas que entienden código | solo necesitas buscar patrones; mira `ast-grep` |

## Stack y modelos

- **Stack:** Rust, C
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `code` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ast-grep](ast-grep.md) | 16.5k | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. |
| [Aider](aider.md) | 50k | Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. |

## Enlaces

- 🐙 GitHub: [tree-sitter/tree-sitter](https://github.com/tree-sitter/tree-sitter)
- 🌐 Web: <https://tree-sitter.github.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
