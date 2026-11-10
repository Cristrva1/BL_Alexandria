[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Skills de dominio: marketing, SEO y negocio

# 🌍 GEO-SEO Claude

> Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 11.6k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Añade a Claude Code comandos `/geo` que auditan un sitio para buscadores con IA (ChatGPT, Claude, Perplexity, Gemini, AI Overviews) sin dejar el SEO técnico: citabilidad del contenido, acceso de crawlers de IA en robots.txt, menciones de marca, datos estructurados y llms.txt. Genera informes para clientes en Markdown o PDF y lleva un pequeño CRM de prospectos.

## Por qué destaca

Está pensado para agencias y consultores: además de auditar, prepara propuestas, compara la evolución mes a mes y produce un PDF listo para entregar. Reparte la auditoría entre cinco subagentes en paralelo.

## Cómo funciona

Una skill principal enruta 13 sub-skills y 5 subagentes; scripts de Python descargan y analizan las páginas, puntúan la citabilidad y generan el PDF con ReportLab. Las dependencias van en un entorno virtual propio dentro de `~/.claude/skills/geo/`.

## Instalación rápida

`curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/install.sh | bash` (requiere Python 3.10+ y Claude Code); después, `/geo audit <url>`.

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
- **Modelos / API:** Se ejecuta dentro de Claude Code con modelos de Anthropic.
- **Etiquetas:** `skills` `search` `pdf` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marketing Skills](marketingskills.md) | 59.5k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |
| [The Agency (agency-agents)](agency-agents.md) | 168k | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes. |
| [playwright](playwright.md) | 99.7k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |

## Enlaces

- 🐙 GitHub: [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)
- 🌐 Web: <https://www.skool.com/aiworkshop>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
