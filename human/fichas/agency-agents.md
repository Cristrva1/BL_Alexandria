[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 🏢 The Agency (agency-agents)

> Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 168k | MIT | Shell | 2026-06-23 |

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

Plantillas de subagente en Markdown agrupadas por divisiones, como una agencia completa: ingeniería, diseño, paid media, ventas, marketing, producto, testing, seguridad, soporte, finanzas, videojuegos y más. Cada agente define identidad, misión, flujo de trabajo, entregables con ejemplos y métricas de éxito, y hay runbooks que arman equipos para escenarios como un MVP o una campaña.

## Por qué destaca

Cada agente es un rol concreto con proceso y entregables, no un prompt genérico, y los scripts lo adaptan a más de una docena de herramientas. Puedes instalar solo las divisiones que vayas a usar.

## Cómo funciona

Los agentes son archivos `.md` por división; `convert.sh` genera el formato de cada herramienta e `install.sh` los copia a su carpeta (por ejemplo `~/.claude/agents/`). También hay una app de escritorio que instala y actualiza el roster.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/msitarzewski/agency-agents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar The Agency (agency-agents) para mi objetivo y necesito pasos guiados. Lee https://github.com/msitarzewski/agency-agents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Activar un agente de marketing o paid media en Claude Code
- Montar un equipo de agentes para un MVP con un runbook
- Usar los mismos roles en Cursor, Codex o Gemini CLI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código | solo necesitas skills de marketing y growth; mira `marketingskills` |

**Limitaciones:** Son definiciones de rol en Markdown que no ejecutan nada por sí solas; además OpenCode solo registra unos 119 agentes, así que conviene instalar por divisiones.

## Stack y modelos

- **Stack:** Markdown, Bash, Python
- **Etiquetas:** `agents` `prompts` `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marketing Skills](marketingskills.md) | 60.4k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |
| [GEO-SEO Claude](geo-seo-claude.md) | 11.7k | Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF. |
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [wshobson/agents](wshobson-agents.md) | 42.5k | Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor, OpenCode y Copilot. |

## Enlaces

- 🐙 GitHub: [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/msitarzewski/agency-agents/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
