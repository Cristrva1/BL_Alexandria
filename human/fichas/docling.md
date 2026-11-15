[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 Docling

> Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 70.6k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | El coste depende del proveedor o la ruta. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Entiende la estructura del documento (tablas, layout, fórmulas, orden de lectura) y la exporta para RAG y agentes.

## Por qué destaca

Excelente con tablas y layouts complejos, y totalmente local.

## Cómo funciona

Modelos de layout y de tablas analizan cada página y construyen un documento estructurado exportable.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno Python con las dependencias indicadas por el proyecto.

1. Instala la biblioteca en el entorno de tu proyecto.
2. Ejecuta la conversión de un PDF o documento pequeño siguiendo el ejemplo del README.
3. Revisa el texto, tablas y orden de lectura del resultado antes de procesar un lote.

**Comando de entrada documentado:**

```shell
pip install docling
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/docling-project/docling/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Docling para mi objetivo y necesito pasos guiados. Lee https://github.com/docling-project/docling/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `docs` `pdf` `ocr` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [RAGFlow](ragflow.md) | 94.2k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marker](marker.md) | 40.9k | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. |
| [MinerU](mineru.md) | 83.7k | Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes. |
| [Unstructured](unstructured.md) | 15.7k | ETL open source que transforma documentos complejos en datos estructurados para LLM. |
| [olmOCR](olmocr.md) | 19.8k | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. |

## Enlaces

- 🐙 GitHub: [docling-project/docling](https://github.com/docling-project/docling)
- 🌐 Web: <https://docling-project.github.io/docling>
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/docling-project/docling/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
