[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 Repomix

> Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 29.2k | MIT | TypeScript | 2026-11-08 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Genera un archivo XML, Markdown o texto con la estructura y el código del repo, respetando .gitignore y contando tokens. También funciona como servidor MCP.

## Por qué destaca

Simple y muy útil para dar contexto completo a cualquier chat de IA.

## Cómo funciona

Recorre el repo, filtra archivos, opcionalmente comprime el código con tree-sitter y escribe un único archivo.

## Instalación rápida

`npx repomix` en la carpeta del repo (o `npm i -g repomix`).

## Casos de uso

- Pasar un repo a ChatGPT o Claude
- Revisiones de código con contexto completo
- Documentar un proyecto con IA

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres dar tu repo completo a un LLM | el repo es enorme; mira `codebase-memory-mcp` o `serena` |

## Stack y modelos

- **Stack:** TypeScript, Node.js
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `code` `coding-agent` `typescript`
- **Modo de instalación sugerido:** 🌍 **Global** — instálalo una vez en tu máquina

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [GitNexus](gitnexus.md) | 48.4k | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. |

## Enlaces

- 🐙 GitHub: [yamadashy/repomix](https://github.com/yamadashy/repomix)
- 🌐 Web: <https://repomix.com>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
