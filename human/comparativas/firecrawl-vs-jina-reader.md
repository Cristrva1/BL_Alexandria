[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# firecrawl vs Jina Reader

| | [firecrawl](../fichas/firecrawl.md) | [Jina Reader](../fichas/jina-reader.md) |
|---|---|---|
| Qué hace | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. | Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. |
| ⭐ Estrellas | 202k | 12.3k |
| Elígelo si… | alimentas agentes/RAG con web y quieres salida limpia | necesitas leer páginas como Markdown al instante |
| Evítalo si… | solo quieres HTML crudo o el presupuesto de API no encaja | vas a rastrear sitios completos; mira `crawl4ai` o `firecrawl` |
| Ejecución | ☁️ cloud/API | ☁️ cloud/API |
| API de IA | Depende de la ruta elegida | Depende de la ruta elegida |
| Coste | El coste depende del proveedor o la ruta | El coste depende del proveedor o la ruta |
| Modelos locales | Modelo local no documentado | Modelo local no documentado |
| Setup | 🟡 medio | 🟢 fácil |
| Licencia | AGPL-3.0 | Apache-2.0 |
| Instalación | `npm i @mendable/firecrawl-js` | `curl https://r.jina.ai/https://ejemplo.com` |

## Regla práctica

- Elige **firecrawl** si alimentas agentes/RAG con web y quieres salida limpia.
- Elige **Jina Reader** si necesitas leer páginas como Markdown al instante.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
