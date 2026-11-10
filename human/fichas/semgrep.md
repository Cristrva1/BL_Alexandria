[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🛡️ Semgrep

> Análisis estático ligero para muchos lenguajes con reglas que se parecen al código.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 17.6k | LGPL-2.1 | C | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

Encuentra bugs y vulnerabilidades con miles de reglas comunitarias o propias. Muy usado en CI de seguridad.

## Por qué destaca

Reglas fáciles de escribir y gran catálogo de seguridad.

## Cómo funciona

Compara patrones contra el AST de cada archivo y reporta coincidencias con contexto.

## Instalación rápida

`pip install semgrep` o `brew install semgrep`; luego `semgrep scan`.

## Casos de uso

- Escanear seguridad en CI
- Reglas internas de código
- Auditar código generado por IA

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres análisis de seguridad en CI | solo quieres refactors estructurales; mira `ast-grep` |

**Limitaciones:** Algunas funciones (análisis entre archivos, IA) son de la versión comercial.

## Stack y modelos

- **Stack:** OCaml, Python
- **Modelos / API:** No usa LLM en la versión abierta.
- **Etiquetas:** `security` `code`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Defending Code Reference Harness](defending-code-reference-harness.md) | 7.7k | Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ast-grep](ast-grep.md) | 16.5k | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. |

## Enlaces

- 🐙 GitHub: [semgrep/semgrep](https://github.com/semgrep/semgrep)
- 🌐 Web: <https://semgrep.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
