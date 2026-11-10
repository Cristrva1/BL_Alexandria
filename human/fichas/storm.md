[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de research autónomo

# 🔎 STORM

> Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 31.8k | MIT | Python | 2025-09-30 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Simula conversaciones entre perspectivas para hacer preguntas, busca fuentes y redacta un artículo estructurado y citado. Útil para informes de fondo.

## Por qué destaca

Método publicado y probado para artículos largos y bien citados.

## Cómo funciona

Genera preguntas desde varias perspectivas, recupera fuentes con un buscador, crea un esquema y redacta sección por sección.

## Instalación rápida

`pip install knowledge-storm` y configura un buscador (p. ej. Bing o You.com) y tu modelo.

## Casos de uso

- Informes de fondo con citas
- Borradores de artículos tipo wiki
- Revisiones de un tema nuevo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas informes largos y citados sobre un tema | quieres respuestas cortas con fuentes; mira `gpt-researcher` |

## Stack y modelos

- **Stack:** Python, DSPy
- **Modelos / API:** OpenAI y otros vía LiteLLM.
- **Etiquetas:** `research` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SearXNG](searxng.md) | 39.4k | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. |
| [firecrawl](firecrawl.md) | 200k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.6k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Enlaces

- 🐙 GitHub: [stanford-oval/storm](https://github.com/stanford-oval/storm)
- 🌐 Web: <http://storm.genie.stanford.edu>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
