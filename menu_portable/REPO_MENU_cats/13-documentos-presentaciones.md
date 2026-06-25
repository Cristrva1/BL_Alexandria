# 13. Documentos & Presentaciones — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `markitdown`
role=library · exec=local · setup=easy · mcp=False · prov=['openai']

**Qué es:** utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman.
**Stack:** Python 3.8+
**Repo:** https://github.com/microsoft/markitdown

**Instalación** [~]: `pip install markitdown   (o: uv add markitdown)`
_Nombre PyPI puede diferir de 'markitdown'; verifica en pypi.org._

**Elige si:** alimentas LLMs con documentos
**Evita si:** ya tienes el texto limpio.
**Combina con:** `ppt-master`, `open-notebook`

## `pdfcraft`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada.
**Stack:** web/TS
**Repo:** https://github.com/PDFCraftTool/pdfcraft

**Instalación** [?]: `git clone https://github.com/PDFCraftTool/pdfcraft (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** manipulas PDFs con privacidad
**Evita si:** necesitas conversión a Markdown para IA ([markitdown](#-markitdown)).
**Combina con:** `markitdown`
**Alternativas (elige una):** `markitdown`

## `ppt-master`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** generador que transforma documentos de texto en presentaciones PowerPoint (.pptx) editables nativas, listas para abrir y ajustar en Office.
**Stack:** Python, python-pptx
**Repo:** https://github.com/hugohe3/ppt-master

**Instalación** [~]: `git clone https://github.com/hugohe3/ppt-master && cd ppt-master && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres PPTX editable
**Evita si:** prefieres slides web ([reveal.js](#-revealjs)).
**Combina con:** `markitdown`
**Alternativas (elige una):** `revealjs`

## `reveal.js`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** reveal.js is an open source HTML presentation framework. It enables anyone with a web browser to create beautiful presentations for free. Check out the live demo at [revealjs.com](https://revealjs.com/).
**Stack:** javascript/typescript, typescript, javascript
**Repo:** https://github.com/hakimel/reveal.js.git

**Instalación** [~]: `git clone https://github.com/hakimel/reveal.js.git && cd reveal.js && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres <p align="center">
**Evita si:** —
**Combina con:** `markitdown`, `ppt-master`, `pdfcraft`

## `revealjs`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados.
**Stack:** JavaScript/HTML
**Repo:** https://github.com/hakimel/reveal.js

**Instalación** [~]: `npm install reveal.js   (o: pnpm add reveal.js)`
_Nombre npm puede diferir de 'reveal.js'; verifica en npmjs.com._

**Elige si:** quieres slides web
**Evita si:** necesitas PPTX editable en Office ([ppt-master](#-ppt-master)).
**Combina con:** `markitdown`
**Alternativas (elige una):** `ppt-master`
