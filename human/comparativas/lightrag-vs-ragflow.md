[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# LightRAG vs RAGFlow

| | [LightRAG](../fichas/lightrag.md) | [RAGFlow](../fichas/ragflow.md) |
|---|---|---|
| Qué hace | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |
| ⭐ Estrellas | 40.6k | 94k |
| Elígelo si… | quieres RAG con grafo sin el coste de GraphRAG | tus documentos son complejos y necesitas citas fiables |
| Evítalo si… | no necesitas relaciones entre entidades; usa RAG vectorial con `llama-index` | quieres algo ligero en un portátil; mira `anything-llm` |
| Ejecución | 🔀 híbrido | 🏠 local |
| Setup | 🟡 medio | 🔴 pesado |
| Licencia | MIT | Apache-2.0 |
| Instalación | `pip install lightrag-hku` | `git clone https://github.com/infiniflow/ragflow && cd ragflow/docker && docker compose up -d` |

## Regla práctica

- Elige **LightRAG** si quieres RAG con grafo sin el coste de GraphRAG.
- Elige **RAGFlow** si tus documentos son complejos y necesitas citas fiables.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
