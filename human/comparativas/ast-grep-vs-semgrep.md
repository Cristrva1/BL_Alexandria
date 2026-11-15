[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# ast-grep vs Semgrep

| | [ast-grep](../fichas/ast-grep.md) | [Semgrep](../fichas/semgrep.md) |
|---|---|---|
| Qué hace | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. |
| ⭐ Estrellas | 16.5k | 17.6k |
| Elígelo si… | necesitas buscar o reescribir código por estructura | quieres análisis de seguridad en CI |
| Evítalo si… | buscas análisis de seguridad con reglas existentes; mira `semgrep` | solo quieres refactors estructurales; mira `ast-grep` |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🟢 fácil | 🟢 fácil |
| Licencia | MIT | LGPL-2.1 |
| Instalación | `npm i -g @ast-grep/cli` | `pip install semgrep` |

## Regla práctica

- Elige **ast-grep** si necesitas buscar o reescribir código por estructura.
- Elige **Semgrep** si quieres análisis de seguridad en CI.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
