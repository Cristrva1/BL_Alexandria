[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📎 PageIndex

> Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 40.3k | MIT | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Genera un árbol tipo índice del documento y deja que el LLM navegue por él como un experto. Funciona bien con informes largos y estructurados.

## Por qué destaca

Evita los problemas de fragmentación de los embeddings en documentos largos.

## Cómo funciona

Construye una jerarquía de secciones con resúmenes y el modelo decide qué ramas leer para responder.

## Instalación rápida

`pip install pageindex` o clona el repo y usa su script con tu clave de OpenAI.

## Casos de uso

- Preguntas sobre informes financieros
- Navegar manuales largos
- RAG sin base vectorial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tus documentos son largos y con estructura clara | tienes miles de documentos cortos; usa búsqueda vectorial |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** OpenAI.
- **Etiquetas:** `rag` `docs` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Docling](docling.md) | 70.4k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LightRAG](lightrag.md) | 40.6k | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. |

## Enlaces

- 🐙 GitHub: [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)
- 🌐 Web: <https://pageindex.ai>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
