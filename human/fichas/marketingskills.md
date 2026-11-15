[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Skills de dominio: marketing, SEO y negocio

# 📈 Marketing Skills

> Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 59.5k | MIT | JavaScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Skills de Corey Haines para marketers técnicos y founders que trabajan con agentes de código: conversión, copywriting, SEO y SEO para IA, anuncios, emails, analítica y atribución, pricing, lanzamientos, retención y ventas. La skill product-marketing guarda el contexto de tu producto y las demás la consultan antes de actuar.

## Por qué destaca

Las skills se referencian entre sí y comparten un único documento de contexto, así que el agente aplica marcos coherentes (CRO, copy, A/B testing) en lugar de consejos sueltos. Es MIT y declara aparte las integraciones de partners.

## Cómo funciona

Cada skill es una carpeta con su SKILL.md y material de referencia; el agente la carga cuando detecta una tarea de marketing. Una guía en `tools/` ayuda a conectar cuentas de marketing con credenciales de solo lectura.

## Instalación rápida

`npx skills add coreyhaines31/marketingskills` (o solo algunas con `--skill cro copywriting`); en Claude Code también `/plugin marketplace add coreyhaines31/marketingskills` y `/plugin install marketing-skills`.

## Casos de uso

- Auditar y reescribir el copy de una landing page
- Diseñar un test A/B o una secuencia de emails
- Planificar un lanzamiento o una estrategia de pricing

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| eres founder o marketer técnico y quieres que tu agente de código haga trabajo de growth con marcos probados | necesitas una herramienta que envíe campañas o mida resultados; mira `mautic`, `listmonk` o `posthog` |

**Limitaciones:** Son guías y marcos de trabajo: el agente no lanza campañas ni lee tus cuentas salvo que conectes herramientas aparte.

## Stack y modelos

- **Stack:** Markdown, SKILL.md, JavaScript (scripts del repo)
- **Modelos / API:** No llama a un LLM: las skills las ejecuta tu agente (Claude Code, Codex, Cursor, Windsurf u otro compatible con Agent Skills).
- **Etiquetas:** `skills` `analytics` `email` `search`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [The Agency (agency-agents)](agency-agents.md) | 168k | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes. |
| [GEO-SEO Claude](geo-seo-claude.md) | 11.6k | Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF. |
| [mautic](mautic.md) | 11k | Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo. |
| [posthog](posthog.md) | 40.7k | Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite. |

## Enlaces

- 🐙 GitHub: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
- 🌐 Web: <https://marketing-skills.com>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
