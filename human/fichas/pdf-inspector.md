[🏠 Inicio](../README.md) › [📄 Documentos & Presentaciones](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 PDF Inspector

> Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 20k | MIT | Rust | 2026-10-22 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Detecta si un PDF necesita OCR para enrutarlo al proceso correcto, y extrae texto rápido cuando no hace falta. De Firecrawl.

## Por qué destaca

Ahorra OCR caro decidiendo qué PDFs lo necesitan.

## Cómo funciona

Analiza objetos del PDF para distinguir texto real de imágenes y extrae contenido con posiciones.

## Instalación rápida

Añádelo como dependencia de Rust o usa sus bindings siguiendo el README.

## Casos de uso

- Enrutar PDFs a OCR solo si hace falta
- Extracción rápida de texto
- Pipelines de documentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| procesas muchos PDFs y quieres ahorrar OCR | necesitas la conversión completa a Markdown; mira `docling` |

## Stack y modelos

- **Stack:** Rust
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `pdf` `docs` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OCRmyPDF](ocrmypdf.md) | 35.3k | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. |
| [Docling](docling.md) | 70.4k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |

## Enlaces

- 🐙 GitHub: [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector)
- 🌐 Web: <https://firecrawl.github.io/pdf-inspector/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
