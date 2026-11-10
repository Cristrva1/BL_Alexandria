[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# Milvus vs Qdrant

| | [Milvus](../fichas/milvus.md) | [Qdrant](../fichas/qdrant.md) |
|---|---|---|
| Qué hace | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| ⭐ Estrellas | 46.6k | 35.5k |
| Elígelo si… | esperas volúmenes muy grandes de vectores | quieres una base vectorial dedicada y rápida |
| Evítalo si… | tu proyecto es pequeño; mira `chroma` o `qdrant` | ya tienes PostgreSQL y poco volumen; mira `pgvector` |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🔴 pesado | 🟢 fácil |
| Licencia | Apache-2.0 | Apache-2.0 |
| Instalación | `pip install pymilvus` | `docker run -p 6333:6333 qdrant/qdrant` |

## Regla práctica

- Elige **Milvus** si esperas volúmenes muy grandes de vectores.
- Elige **Qdrant** si quieres una base vectorial dedicada y rápida.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
