[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 📈 Marketing Skills

> Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.4k | MIT | JavaScript | 2026-06-23 |

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

Skills de Corey Haines para marketers técnicos y founders que trabajan con agentes de código: conversión, copywriting, SEO y SEO para IA, anuncios, emails, analítica y atribución, pricing, lanzamientos, retención y ventas. La skill product-marketing guarda el contexto de tu producto y las demás la consultan antes de actuar.

## Por qué destaca

Las skills se referencian entre sí y comparten un único documento de contexto, así que el agente aplica marcos coherentes (CRO, copy, A/B testing) en lugar de consejos sueltos. Es MIT y declara aparte las integraciones de partners.

## Cómo funciona

Cada skill es una carpeta con su SKILL.md y material de referencia; el agente la carga cuando detecta una tarea de marketing. Una guía en `tools/` ayuda a conectar cuentas de marketing con credenciales de solo lectura.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

**Comando de entrada documentado:**

```shell
npx skills add coreyhaines31/marketingskills
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/coreyhaines31/marketingskills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Marketing Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/coreyhaines31/marketingskills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `skills` `analytics` `email` `search`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [The Agency (agency-agents)](agency-agents.md) | 168k | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes. |
| [GEO-SEO Claude](geo-seo-claude.md) | 11.7k | Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF. |
| [mautic](mautic.md) | 11k | Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo. |
| [posthog](posthog.md) | 40.8k | Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite. |

## Enlaces

- 🐙 GitHub: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
- 🌐 Web: <https://marketing-skills.com>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/coreyhaines31/marketingskills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
