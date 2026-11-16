[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 📝 markitdown

> Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 195k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Utilidad Python ligera de Microsoft (MIT) para convertir archivos a Markdown destinado a LLM y análisis de texto. Activa (v0.1.9); el repositorio incluye también un servidor MCP, un complemento de OCR y un complemento de ejemplo.

## ¿Qué hace?

Convierte PDF, PowerPoint, Word, Excel, imágenes (metadatos EXIF y descripción), audio (metadatos y transcripción), HTML, CSV/JSON/XML, ZIP (recorre su contenido), URLs de YouTube y EPUB a Markdown que conserva la estructura (títulos, listas, tablas, enlaces). La descripción de imágenes y la transcripción dependen de servicios web. Advierte que hace E/S con los privilegios del proceso: hay que sanear las entradas en entornos no confiables.

## ¿Cómo lo hace?

Requiere Python 3.10–3.14; se instala con `pip install 'markitdown[all]'` o solo con los extras necesarios (`[pdf, docx, pptx]`, `[az-doc-intel]`, `[az-content-understanding]`). Ofrece CLI, API Python, complementos de terceros (desactivados por defecto) y el paquete `markitdown-mcp` para exponerlo a agentes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | El paquete `markitdown-mcp` del repositorio expone la conversión a agentes compatibles con MCP. | Instala markitdown-mcp y regístralo; limita las rutas que puede leer. |
| [Khoj](khoj.md) | Convertir formatos no soportados a Markdown antes de indexarlos (combinación por arquitectura). | Convierte primero y sincroniza la carpeta resultante. |
| [Pandoc](pandoc.md) | MarkItDown extrae a Markdown y Pandoc lo publica en DOCX, HTML, LaTeX o EPUB (combinación por arquitectura). | Independientes; encadénalos en un script. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (9). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ai-job-search](ai-job-search.md) · [annas-mcp](annas-mcp.md) · [Anytype Desktop](anytype-ts.md) · [AppFlowy](appflowy.md) · [obsidian-importer](obsidian-importer.md) · [ppt-master](ppt-master.md) · [Repomix](repomix.md) · [tools](tools.md) · [Vane](vane.md)

**Notas:** Se retiraron las combinaciones antiguas con ppt-master y open-notebook por falta de relación documentada.

Estado en GitHub: activo · último push 2026-11-07 · última versión publicada v0.1.9 (2026-10-21) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/markitdown/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La extracción básica es offline; Azure, descripciones LLM y otras extensiones pueden enviar datos y consumir servicios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Instala los extras necesarios; convertir a Markdown no conserva toda la maquetación del original |
| Coste | El coste depende del proveedor o la ruta. La extracción básica es offline; Azure, descripciones LLM y otras extensiones pueden enviar datos y consumir servicios |
| Equipo | Preparación según la ruta elegida. Python 3.10–3.14; entorno virtual; extras del formato elegido |

Instala los extras necesarios; convertir a Markdown no conserva toda la maquetación del original

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10–3.14
- entorno virtual
- extras del formato elegido

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/microsoft/markitdown/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar markitdown para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/markitdown/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte un DOCX ficticio a Markdown y revisa títulos, listas y tablas.

**Qué comprobar:** El texto y el orden se pueden contrastar con el documento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar documentos Office para consulta
- Crear una copia textual de un informe

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar documentos Office para consulta; Crear una copia textual de un informe | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instala los extras necesarios; convertir a Markdown no conserva toda la maquetación del original

## Stack y modelos

- **Stack:** Python 3.10–3.14; entorno virtual; extras del formato elegido
- **Etiquetas:** `docs` `python`
- **Modo de instalación sugerido:** 📦 **Dependencia del proyecto** — instálalo dentro de cada proyecto que lo use

## Enlaces

- 🐙 GitHub: [microsoft/markitdown](https://github.com/microsoft/markitdown)
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/markitdown/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
