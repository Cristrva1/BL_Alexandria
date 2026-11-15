[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ wshobson/agents

> Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor, OpenCode y Copilot.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.5k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Colección de Seth Hobson que agrupa subagentes especialistas, skills y comandos en plugins por área: desarrollo Python y JavaScript, revisión de código, testing, infraestructura, seguridad y más. Se escribe una sola vez en formato de plugin de Claude Code y unos adaptadores generan las versiones para Codex, Cursor, OpenCode, Antigravity CLI, GitHub Copilot y Pi.

## Por qué destaca

Instalas solo el plugin que necesitas en lugar de cientos de archivos sueltos y mantienes el mismo set en varios agentes. Incluye `plugin-eval` para puntuar skills con chequeos estáticos.

## Cómo funciona

Cada plugin de `plugins/` agrupa agentes (con alias de modelo como opus o sonnet), skills y comandos en Markdown. Los marketplaces nativos apuntan a esa fuente y adaptadores en Python generan el formato de cada herramienta.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/wshobson/agents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar wshobson/agents para mi objetivo y necesito pasos guiados. Lee https://github.com/wshobson/agents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Añadir subagentes de Python o TypeScript a Claude Code
- Lanzar un escaneo de seguridad con un comando del plugin
- Compartir el mismo set de agentes entre Claude Code y Codex

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres subagentes y comandos especializados por lenguaje o área, instalables plugin a plugin | solo quieres plugins oficiales de Anthropic y socios; mira `claude-plugins-official` |

**Limitaciones:** Las funciones dependen de la herramienta: Codex, Copilot u OpenCode reciben versiones generadas con menos capacidades que Claude Code.

## Stack y modelos

- **Stack:** Markdown, Python (uv), Make
- **Etiquetas:** `skills` `coding-agent` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [SkillSpector](skillspector.md) | 26.1k | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code Plugins Directory](claude-plugins-official.md) | 47.3k | Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. |
| [Agentic Awesome Skills](antigravity-awesome-skills.md) | 49.7k | Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local. |
| [The Agency (agency-agents)](agency-agents.md) | 168k | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes. |

## Enlaces

- 🐙 GitHub: [wshobson/agents](https://github.com/wshobson/agents)
- 🌐 Web: <https://sethhobson.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/wshobson/agents/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
