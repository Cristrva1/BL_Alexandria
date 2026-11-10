[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 🔎 Agente de research profundo

> **Objetivo:** Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.

## 🗺️ Cómo fluye

```mermaid
flowchart LR
  Pregunta["Pregunta"] -->|tema| gpt_researcher["gpt-researcher"]
  gpt_researcher["gpt-researcher"] -->|consultas| searxng["SearXNG"]
  searxng["SearXNG"] -->|URLs| crawl4ai["crawl4ai"]
  gpt_researcher["gpt-researcher"] -->|sitios dinámicos| browser_use["browser-use"]
  markitdown["markitdown"] -->|documentos| gpt_researcher["gpt-researcher"]
  crawl4ai["crawl4ai"] -->|Markdown| gpt_researcher["gpt-researcher"]
  gpt_researcher["gpt-researcher"] -->|trazas| langfuse["langfuse"]
  gpt_researcher["gpt-researcher"] -->|citas| Informe["Informe"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [gpt-researcher](../fichas/gpt-researcher.md) | Orquestador: planifica preguntas, delega y redacta el informe | 30.6k | `pip install gpt-researcher` |
| 2 | [SearXNG](../fichas/searxng.md) | Buscador privado y sin claves de API | 39.4k | `docker run -d -p 8080:8080 searxng/searxng` |
| 3 | [crawl4ai](../fichas/crawl4ai.md) | Convierte cada página en Markdown limpio para el LLM | 87.2k | `pip install crawl4ai` |
| 4 | [browser-use](../fichas/browser-use.md) | Navega sitios dinámicos o con login | 121k | `pip install browser-use` |
| 5 | [markitdown](../fichas/markitdown.md) | Ingiere PDFs y documentos locales | 195k | `pip install markitdown` |
| 6 | [langfuse](../fichas/langfuse.md) | Trazas, costos y depuración de cada paso | 37.3k | Docker Compose para self-host (Postgres + backend + frontend) o cuenta cloud; SDKs vía… |

## 🔌 Cómo se conecta

GPT Researcher divide la pregunta en sub-preguntas, busca con SearXNG y pasa las URLs a Crawl4AI, que devuelve Markdown listo para el modelo. Browser Use cubre las páginas que necesitan clics o sesión, y MarkItDown suma tus documentos. Langfuse registra cada llamada para revisar costos y errores. DeerFlow es la alternativa si prefieres un harness con sandbox y más autonomía.

## 🚫 Cuándo NO usar esta receta

Si la investigación es solo sobre documentos internos, no necesitas buscador ni crawler: usa la receta de RAG sobre documentos.

## 🔁 Variantes

- En lugar de [gpt-researcher](../fichas/gpt-researcher.md): [STORM](../fichas/storm.md), [Vane](../fichas/vane.md)
- En lugar de [crawl4ai](../fichas/crawl4ai.md): [Jina Reader](../fichas/jina-reader.md)
- En lugar de [browser-use](../fichas/browser-use.md): [Gemini Computer Use (preview)](../fichas/computer-use-preview.md), [Stagehand](../fichas/stagehand.md), [Skyvern](../fichas/skyvern.md)
- En lugar de [langfuse](../fichas/langfuse.md): [Phoenix](../fichas/phoenix.md), [Opik](../fichas/opik.md), [MLflow](../fichas/mlflow.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
