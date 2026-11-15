[🏠 Inicio](../README.md) › [📄 Documentos & Presentaciones](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 Unstructured

> ETL open source que transforma documentos complejos en datos estructurados para LLM.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 15.7k | Apache-2.0 | HTML | 2026-11-06 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Particiona más de 25 tipos de archivo en elementos (títulos, tablas, texto) y los prepara para bases vectoriales.

## Por qué destaca

Soporta muchos formatos y conectores de entrada y salida.

## Cómo funciona

Particionadores por tipo de archivo detectan elementos y los limpian y dividen en fragmentos.

## Instalación rápida

`pip install "unstructured[all-docs]"`.

## Casos de uso

- Ingestar documentos variados para RAG
- Normalizar correos y HTML
- Pipelines ETL de documentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tienes muchos formatos de documentos distintos | solo procesas PDFs; mira `docling` |

**Limitaciones:** Lo más avanzado está en su plataforma de pago.

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** Modelos opcionales para PDFs e imágenes.
- **Etiquetas:** `docs` `data` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Docling](docling.md) | 70.4k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |

## Enlaces

- 🐙 GitHub: [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)
- 🌐 Web: <https://www.unstructured.io/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
