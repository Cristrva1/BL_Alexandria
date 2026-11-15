[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🔌 Claude Code Plugins Directory

> Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47.3k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. Cada plugin puede tener requisitos distintos; el marketplace completo no es una aplicación que debas desplegar.

## Por qué destaca

Es la fuente oficial: viene integrada en el sistema de plugins de Claude Code y los plugins externos deben cumplir criterios de calidad y seguridad para entrar. Evita copiar archivos a mano.

## Cómo funciona

Instalas los plugins concretos desde el cliente y configuras sus dependencias o servicios.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/anthropics/claude-plugins-official/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Claude Code Plugins Directory para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/claude-plugins-official/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Añadir revisión de PR y comandos de commit a Claude Code
- Conectar Claude Code a Figma, Atlassian o Firebase con un plugin
- Usar `example-plugin` como base para publicar el tuyo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas Claude Code y quieres plugins oficiales o de socios que se instalan con un comando | buscas recursos comunitarios o trabajas con otro agente; mira `awesome-claude-code` o `wshobson-agents` |

**Limitaciones:** Anthropic no controla el contenido de los plugins externos ni de sus servidores MCP: revisa cada plugin antes de instalarlo.

## Stack y modelos

- **Stack:** Markdown, JSON, Python, MCP
- **Etiquetas:** `skills` `coding-agent` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Anthropic Skills](anthropic-skills.md) | 195k | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. |
| [Awesome Claude Code](awesome-claude-code.md) | 58k | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [wshobson/agents](wshobson-agents.md) | 42.5k | Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor, OpenCode y Copilot. |

## Enlaces

- 🐙 GitHub: [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
- 🌐 Web: <https://code.claude.com/docs/en/plugins>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/anthropics/claude-plugins-official/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
