[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Awesome Claude Skills

> Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 79.5k | — | Python | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo. |
| Coste | Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Recopilación de skills por áreas (documentos, desarrollo, datos, marketing, escritura, multimedia, productividad, seguridad) que enlaza skills oficiales de Anthropic y de la comunidad, y aloja algunas propias. Incluye el plugin connect-apps, que usa Composio para que Claude envíe correos, cree issues o publique en Slack.

## Por qué destaca

Cubre tareas de negocio y productividad además de programación, y explica bien la diferencia entre una skill y un MCP. Su plugin de Composio añade acciones reales en apps externas, algo que las skills solas no dan.

## Cómo funciona

Es un README por categorías con enlaces a cada skill, más algunas carpetas de skills dentro del propio repo. El plugin connect-apps se carga en Claude Code y delega la autenticación y las llamadas a la plataforma de Composio.

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

1. Abre el material original y elige un capítulo o ejemplo.
2. Revisa los requisitos de ese ejemplo antes de instalar dependencias.
3. Usa las alternativas y recetas para situarlo dentro de tu proyecto.

[Instrucciones originales de instalación](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Awesome Claude Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Encontrar skills de documentos, datos o marketing para Claude
- Conectar Claude a Gmail, Slack o GitHub mediante Composio
- Ver ejemplos de skills de comunidad antes de crear la tuya

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas Claude para tareas de negocio además de código y quieres skills ordenadas por área de trabajo | solo quieres skills de procedencia oficial; mira `anthropic-skills` o `awesome-agent-skills` |

**Limitaciones:** Mezcla skills de terceros de calidad desigual y promociona Composio; el plugin de apps requiere cuenta y API key de Composio.

## Stack y modelos

- **Stack:** Markdown, Python, Composio (plugin connect-apps)
- **Etiquetas:** `skills` `automation` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Composio](composio.md) | 31.1k | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. |
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [SkillSpector](skillspector.md) | 26.1k | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Agent Skills](awesome-agent-skills.md) | 37.2k | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes. |
| [Agentic Awesome Skills](antigravity-awesome-skills.md) | 49.7k | Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local. |
| [Awesome Claude Code](awesome-claude-code.md) | 58k | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. |

## Enlaces

- 🐙 GitHub: [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
