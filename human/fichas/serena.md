[🏠 Inicio](../README.md) › [🔌 MCP & Conectividad](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Serena

> Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 31.3k | Otra (ver repo) | Python | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

En vez de leer archivos enteros, el agente busca símbolos, referencias y edita a nivel de función usando servidores de lenguaje. Ahorra tokens en repos grandes.

## Por qué destaca

Mejora la precisión y el gasto de tokens de cualquier agente en bases de código grandes.

## Cómo funciona

Usa servidores LSP para entender el código y expone herramientas MCP de búsqueda y edición por símbolos.

## Instalación rápida

Añade a tu cliente MCP: `uvx --from git+https://github.com/oraios/serena serena start-mcp-server`.

## Casos de uso

- Navegar repos grandes con menos tokens
- Refactors por símbolo
- Dar herramientas de IDE a Claude Code

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente trabaja en un repo grande y gasta muchos tokens leyendo | tu proyecto es pequeño |

## Stack y modelos

- **Stack:** Python, LSP
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `mcp` `coding-agent` `code` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codegraph](codegraph.md) | 77.3k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. |
| [GitNexus](gitnexus.md) | 48.4k | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. |

## Enlaces

- 🐙 GitHub: [oraios/serena](https://github.com/oraios/serena)
- 🌐 Web: <https://oraios.github.io/serena>
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
