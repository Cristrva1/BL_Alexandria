[🏠 Inicio](../README.md) › [📄 Documentos & Presentaciones](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 📝 markitdown

> Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 195k | MIT | Python | 2026-11-07 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Es la puerta de entrada habitual para ingesta de documentos en pipelines RAG.

## Por qué destaca

Proyecto oficial de Microsoft muy adoptado como paso previo a LLMs, por su salida ordenada y su catálogo de convertidores y plugins; se integra fácil en flujos de ingesta por su CLI y API Python.

## Cómo funciona

Detecta el tipo de archivo y aplica el extractor adecuado (parsers de Office, OCR por modelos de visión, Whisper para audio), normalizando todo a Markdown estructurado con encabezados y tablas.

## Instalación rápida

`pip install markitdown` (o `pip install 'markitdown[all]'` para todos los formatos). Los convertidores de visión/audio requieren claves de API opcionales.

## Casos de uso

- Convertir carpetas de informes (XLSX/PDF) a `.md`
- Ingesta de datos para IA
- Preprocesar documentos antes de indexarlos en un vector store

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| alimentas LLMs con documentos de formatos variados | ya tienes el texto limpio o necesitas fidelidad de layout total (no es un reconstructor de PDF) |

## Stack y modelos

- **Stack:** Python 3.8+
- **Modelos / API:** Opcional (visión para OCR, Whisper para audio), agnóstico vía variables de entorno.
- **Etiquetas:** `docs` `python`
- **Modo de instalación sugerido:** 📦 **Dependencia del proyecto** — instálalo dentro de cada proyecto que lo use

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ppt-master](ppt-master.md) | 75.5k | Generador que transforma documentos de texto en presentaciones PowerPoint (.pptx) editables nativas, listas para abrir y ajustar en Office. |
| [open-notebook](open-notebook.md) | 41.8k | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. |

## Enlaces

- 🐙 GitHub: [microsoft/markitdown](https://github.com/microsoft/markitdown)
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
