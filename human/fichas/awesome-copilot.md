[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Awesome GitHub Copilot

> Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y plugins para personalizar GitHub Copilot.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.2k | MIT | JavaScript | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Repositorio de la organización GitHub que reúne personalizaciones de Copilot aportadas por la comunidad: agentes especializados (algunos conectados a servidores MCP), instrucciones que se aplican por tipo de archivo, skills, plugins y un cookbook de recetas para las APIs de Copilot. Tiene web con búsqueda, un Learning Hub y un llms.txt para agentes.

## Por qué destaca

Es el marketplace que Copilot CLI y VS Code traen registrado por defecto, así que instalar un plugin es un solo comando. También sirve de referencia para escribir instrucciones y agentes de Copilot.

## Cómo funciona

Cada recurso es un archivo Markdown con frontmatter (agentes, instrucciones con patrones de archivo, skills con sus assets) y los plugins agrupan varios para un flujo. Copilot los carga desde el marketplace `awesome-copilot` o copiándolos a tu repo.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/github/awesome-copilot/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Awesome GitHub Copilot para mi objetivo y necesito pasos guiados. Lee https://github.com/github/awesome-copilot/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Aplicar estándares de código por tipo de archivo en Copilot
- Instalar un plugin de agentes para un flujo de trabajo concreto
- Pasar a un agente el índice llms.txt de recursos de Copilot

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu equipo trabaja con GitHub Copilot en VS Code o Copilot CLI y quiere personalizarlo | usas Claude Code u otro agente; mira `claude-plugins-official` o `antigravity-awesome-skills` |

**Limitaciones:** Los recursos son de terceros: revisa cada agente o plugin antes de instalarlo, como advierte el propio repo.

## Stack y modelos

- **Stack:** Markdown, YAML, JavaScript (web del catálogo)
- **Etiquetas:** `skills` `coding-agent` `prompts` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [GitHub MCP Server](github-mcp-server.md) | 34.5k | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. |
| [Spec Kit](spec-kit.md) | 150k | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. |
| [GitHub CLI](cli.md) | 47k | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. |

## Enlaces

- 🐙 GitHub: [github/awesome-copilot](https://github.com/github/awesome-copilot)
- 🌐 Web: <https://awesome-copilot.github.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/github/awesome-copilot/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
