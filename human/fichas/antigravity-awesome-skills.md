[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Agentic Awesome Skills

> Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 49.7k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

Antes llamada Antigravity Awesome Skills, reúne miles de skills por dominio (desarrollo, seguridad, DevOps, datos, marketing) instalables en Claude Code, Codex, Cursor, Gemini CLI, Kiro, OpenCode y otros agentes. Incluye bundles por rol, plugins temáticos y AAS Core, un MCP local para que el agente busque en el catálogo y elija skills antes de instalarlas.

## Por qué destaca

Destaca por volumen y por su instalador, que filtra por categoría, nivel de riesgo o lista exacta de ids. Con AAS Core el agente consulta el catálogo bajo demanda en lugar de cargar miles de skills en su contexto.

## Cómo funciona

Cada skill vive en `skills/<nombre>/SKILL.md` y un índice JSON describe el catálogo. El CLI de npm copia la selección a la carpeta de skills de cada agente y AAS Core expone el catálogo como servidor MCP local con vista previa del plan.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/sickn33/agentic-awesome-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Agentic Awesome Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/sickn33/agentic-awesome-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Instalar solo las skills de un dominio con filtros de categoría
- Dejar que Codex o Claude elijan skills a través del MCP AAS Core
- Dar el mismo set de skills a varios agentes de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres cubrir muchos dominios con skills ya escritas y trabajas con uno o varios agentes de código | prefieres pocas skills oficiales y revisadas; mira `anthropic-skills` o `awesome-agent-skills` |

**Limitaciones:** La calidad varía entre skills de terceros y algunas dependen de servicios externos de pago; revísalas antes de instalarlas (por ejemplo con `skillspector`).

## Stack y modelos

- **Stack:** Markdown, JavaScript (Node.js 22+), Python, MCP
- **Etiquetas:** `skills` `coding-agent` `mcp` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SkillSpector](skillspector.md) | 26.1k | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. |
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Agent Skills](awesome-agent-skills.md) | 37.2k | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes. |
| [Awesome Claude Skills](awesome-claude-skills.md) | 79.5k | Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps. |
| [wshobson/agents](wshobson-agents.md) | 42.5k | Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor, OpenCode y Copilot. |

## Enlaces

- 🐙 GitHub: [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)
- 🌐 Web: <https://aaskills.tech/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/sickn33/agentic-awesome-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
