[🏠 Inicio](../README.md) › [📄 Documentos & Presentaciones](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 Docling

> Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 70.4k | MIT | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Entiende la estructura del documento (tablas, layout, fórmulas, orden de lectura) y la exporta para RAG y agentes.

## Por qué destaca

Excelente con tablas y layouts complejos, y totalmente local.

## Cómo funciona

Modelos de layout y de tablas analizan cada página y construyen un documento estructurado exportable.

## Instalación rápida

`pip install docling` y `docling archivo.pdf`.

## Casos de uso

- Preparar PDFs para RAG
- Extraer tablas de reportes
- Convertir documentos Office a Markdown

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres convertir documentos a Markdown con buena estructura | solo tienes PDFs de texto simples; mira `markitdown` |

## Stack y modelos

- **Stack:** Python, PyTorch
- **Modelos / API:** Modelos propios de layout; VLM opcionales.
- **Etiquetas:** `docs` `pdf` `ocr` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [RAGFlow](ragflow.md) | 94k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |
| [Qdrant](qdrant.md) | 35.5k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marker](marker.md) | 40.8k | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. |
| [MinerU](mineru.md) | 83.4k | Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes. |
| [Unstructured](unstructured.md) | 15.7k | ETL open source que transforma documentos complejos en datos estructurados para LLM. |
| [olmOCR](olmocr.md) | 19.8k | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. |

## Enlaces

- 🐙 GitHub: [docling-project/docling](https://github.com/docling-project/docling)
- 🌐 Web: <https://docling-project.github.io/docling>
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
