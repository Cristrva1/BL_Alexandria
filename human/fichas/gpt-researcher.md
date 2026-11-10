[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de research autónomo

# 🔍 gpt-researcher

> Agente autónomo que investiga en línea y consolida reportes citados y estructurados.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 30.6k | Apache-2.0 | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Planifica sub-preguntas, busca fuentes y redacta un informe con referencias.

## Por qué destaca

Muy popular para research profundo; automatiza horas de búsqueda recopilando y citando lo más relevante. Su arquitectura planificador-buscador-redactor es un patrón de referencia para research con agentes.

## Cómo funciona

Un agente planificador genera consultas, agentes de búsqueda recopilan fuentes web (vía Tavily y otros) y un redactor sintetiza el reporte; backend Python (FastAPI) con frontend Next.js.

## Instalación rápida

`pip install gpt-researcher` o vía Docker. Requiere una clave de LLM y, según configuración, una clave de búsqueda web (Tavily).

## Casos de uso

- Análisis de un tema con fuentes
- Reportes en PDF/Markdown
- Briefing automático antes de una decisión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas research profundo citado | solo quieres una respuesta corta o un chat simple |

## Stack y modelos

- **Stack:** Python, Next.js, FastAPI
- **Modelos / API:** GPT-4o, Claude, Gemini + locales; agnóstico vía variables de entorno.
- **Etiquetas:** `automation` `research` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [firecrawl](firecrawl.md) | 200k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [STORM](storm.md) | 31.8k | Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. |
| [Vane](vane.md) | 38.1k | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). |

## Enlaces

- 🐙 GitHub: [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
- 🌐 Web: <https://gptr.dev>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
