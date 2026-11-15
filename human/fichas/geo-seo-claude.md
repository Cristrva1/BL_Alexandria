[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Skills de dominio: marketing, SEO y negocio

# 🌍 GEO-SEO Claude

> Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.7k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

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

Añade a Claude Code comandos `/geo` que auditan un sitio para buscadores con IA (ChatGPT, Claude, Perplexity, Gemini, AI Overviews) sin dejar el SEO técnico: citabilidad del contenido, acceso de crawlers de IA en robots.txt, menciones de marca, datos estructurados y llms.txt. Genera informes para clientes en Markdown o PDF y lleva un pequeño CRM de prospectos.

## Por qué destaca

Está pensado para agencias y consultores: además de auditar, prepara propuestas, compara la evolución mes a mes y produce un PDF listo para entregar. Reparte la auditoría entre cinco subagentes en paralelo.

## Cómo funciona

Una skill principal enruta 13 sub-skills y 5 subagentes; scripts de Python descargan y analizan las páginas, puntúan la citabilidad y generan el PDF con ReportLab. Las dependencias van en un entorno virtual propio dentro de `~/.claude/skills/geo/`.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GEO-SEO Claude para mi objetivo y necesito pasos guiados. Lee https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Auditar la visibilidad de una web en ChatGPT y Perplexity
- Revisar robots.txt para crawlers de IA y generar un llms.txt
- Entregar a un cliente un informe GEO en PDF

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres medir y mejorar cómo te citan los buscadores con IA, no solo tu posición en Google | solo haces SEO clásico o no usas Claude Code; mira `marketingskills` |

**Limitaciones:** Depende de Claude Code y el README promociona una comunidad de pago (Skool); revisa los datos de mercado que cita antes de usarlos con clientes.

## Stack y modelos

- **Stack:** Python, Markdown, ReportLab, JSON-LD, Playwright (opcional)
- **Etiquetas:** `skills` `search` `pdf` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marketing Skills](marketingskills.md) | 60.4k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |
| [The Agency (agency-agents)](agency-agents.md) | 168k | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes. |
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |

## Enlaces

- 🐙 GitHub: [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)
- 🌐 Web: <https://www.skool.com/aiworkshop>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
