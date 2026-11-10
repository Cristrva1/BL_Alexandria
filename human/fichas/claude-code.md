[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 👨‍💻 Claude Code

> Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 155k | — | TypeScript | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Lee y edita archivos, ejecuta comandos, hace commits y abre PRs a partir de instrucciones en lenguaje natural. Se extiende con skills, plugins, subagentes, hooks y servidores MCP.

## Por qué destaca

Referencia en agentes de código por su autonomía en tareas largas y su ecosistema de skills y plugins.

## Cómo funciona

Un bucle agéntico con Claude decide qué herramientas usar (leer, editar, bash, MCP) y pide permiso según el modo configurado.

## Instalación rápida

`curl -fsSL https://claude.ai/install.sh | bash` (o `npm install -g @anthropic-ai/claude-code`) y ejecuta `claude` en tu proyecto.

## Casos de uso

- Implementar funciones completas con tests
- Migrar o refactorizar código grande
- Automatizar tareas con skills y hooks

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres el agente de código más capaz para tareas largas en tu repo | necesitas un agente totalmente abierto y multi-modelo; mira `opencode` |

**Limitaciones:** Requiere suscripción o clave de API de Anthropic; el código no es open source.

## Stack y modelos

- **Stack:** TypeScript, Node.js
- **Modelos / API:** Modelos Claude de Anthropic (o vía Bedrock y Vertex).
- **Etiquetas:** `coding-agent` `agents` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [superpowers](superpowers.md) | 315k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |
| [Anthropic Skills](anthropic-skills.md) | 192k | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. |
| [claude-mem](claude-mem.md) | 116k | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. |
| [Context7](context7.md) | 64.5k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [Gemini CLI](gemini-cli.md) | 109k | Agente de IA open source de Google que lleva Gemini a tu terminal, con cuota gratuita generosa. |
| [OpenCode](opencode.md) | 226k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| [goose](goose.md) | 56.4k | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. |

## Enlaces

- 🐙 GitHub: [anthropics/claude-code](https://github.com/anthropics/claude-code)
- 🌐 Web: <https://code.claude.com/docs/en/overview>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
