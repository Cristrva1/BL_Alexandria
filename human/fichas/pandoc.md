[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 Pandoc

> Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y decenas de formatos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 46.9k | GPL-2.0 | Haskell | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Conversor universal de formatos de marcado de John MacFarlane: una biblioteca Haskell y una herramienta de línea de comandos. GPL-2.0, muy madura y activa (versión 3.14).

## ¿Qué hace?

Convierte entre decenas de formatos: Markdown (CommonMark, GFM y variantes), HTML, LaTeX, DOCX, ODT, EPUB, Jupyter, AsciiDoc, DocBook, JATS, wikis (MediaWiki, DokuWiki, Jira) y bibliografías (BibTeX, CSL JSON, EndNote), y genera también presentaciones (Beamer, reveal.js y otras) y PDF mediante un motor externo. Sirve para publicar documentación, artículos académicos con citas y libros electrónicos desde una sola fuente.

## ¿Cómo lo hace?

Lee el documento a una representación interna y lo escribe al formato de destino; admite filtros en Lua para transformar el documento y lectores o escritores personalizados en Lua. Se distribuye como binario para las principales plataformas; generar PDF requiere un motor como LaTeX.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [reveal.js](reveal-js.md) | Pandoc genera presentaciones reveal.js desde Markdown. | Usa `-t revealjs`; reveal.js puede cargarse desde CDN o una copia local. |
| [markitdown](markitdown.md) | MarkItDown extrae a Markdown y Pandoc lo convierte al formato final (combinación por arquitectura). | Encadénalos en un script. |
| [Marker](marker.md) | Marker convierte PDF complejos a Markdown que luego Pandoc publica (combinación por arquitectura). | Igual que arriba. |
| [ppt-master](ppt-master.md) | Combinación recíproca: ppt-master lo enlaza como «Conversión de documentos». | Orden indicado desde ppt-master: Instala Pandoc si se necesita. |
| [Marp](marp.md) | Combinación recíproca: Marp lo enlaza como «Conversión de documentos a Markdown. (combinación por arquitectura)». | Orden indicado desde Marp: Preprocesa el contenido. |
| [pdf-craft](pdf-craft.md) | Combinación recíproca: pdf-craft lo enlaza como «Convertir el Markdown resultante a DOCX o LaTeX (combinación por arquitectura)». | Orden indicado desde pdf-craft: Encadénalos en un script. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (5). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Calibre-Web](calibre-web.md) · [D2](d2.md) · [Joplin](joplin.md) · [Logseq](logseq.md) · [Trilium Notes](trilium.md)

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 3.14 (2026-11-12) · licencia declarada GPL-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jgm/pandoc/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere IA; motores PDF, fuentes y herramientas complementarias tienen sus condiciones |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Cambiar formato no garantiza conservar cada detalle de diseño; elige plantilla y motor según la salida |
| Coste | Sin pago a un modelo en la ruta básica. No requiere IA; motores PDF, fuentes y herramientas complementarias tienen sus condiciones |
| Equipo | Preparación según la ruta elegida. Binario de tu sistema; motor PDF solo si generas PDF; archivo de prueba |

Cambiar formato no garantiza conservar cada detalle de diseño; elige plantilla y motor según la salida

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario de tu sistema
- motor PDF solo si generas PDF
- archivo de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://pandoc.org/installing.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Pandoc para mi objetivo y necesito pasos guiados. Lee https://pandoc.org/installing.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte un Markdown con títulos y tabla a DOCX y revisa el resultado.

**Qué comprobar:** Puedes abrir el documento y comprobar estructura y contenido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Generar documentos desde Markdown
- Convertir un libro propio a EPUB

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Generar documentos desde Markdown; Convertir un libro propio a EPUB | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Cambiar formato no garantiza conservar cada detalle de diseño; elige plantilla y motor según la salida

## Stack y modelos

- **Stack:** Binario de tu sistema; motor PDF solo si generas PDF; archivo de prueba
- **Etiquetas:** `docs`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [jgm/pandoc](https://github.com/jgm/pandoc)
- 🌐 Web: <https://pandoc.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jgm/pandoc/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
