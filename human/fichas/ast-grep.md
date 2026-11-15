[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🛡️ ast-grep

> CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 16.5k | MIT | Rust | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

Busca y reemplaza código por su estructura (AST), no por texto. Útil para refactors masivos y reglas de lint propias.

## Por qué destaca

Muy rápido y con patrones fáciles de escribir; los agentes de código lo usan bien.

## Cómo funciona

Parsea con tree-sitter y compara patrones contra el árbol sintáctico.

## Instalación rápida

`npm i -g @ast-grep/cli` o `brew install ast-grep`.

## Casos de uso

- Refactors masivos seguros
- Reglas de lint del equipo
- Buscar patrones de bugs

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas buscar o reescribir código por estructura | buscas análisis de seguridad con reglas existentes; mira `semgrep` |

## Stack y modelos

- **Stack:** Rust, tree-sitter
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `code` `security` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [tree-sitter](tree-sitter.md) | 27.4k | Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código. |
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Semgrep](semgrep.md) | 17.6k | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. |

## Enlaces

- 🐙 GitHub: [ast-grep/ast-grep](https://github.com/ast-grep/ast-grep)
- 🌐 Web: <https://ast-grep.github.io/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
