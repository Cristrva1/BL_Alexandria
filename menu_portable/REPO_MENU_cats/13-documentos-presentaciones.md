# 13. Documentos & Presentaciones — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `markitdown`
role=directory · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** MarkItDown performs I/O with the privileges of the current process. Like open() or requests.get(), it will access resources that the process itself can access. Sanitize your inputs in untrusted environments, and call the narrowest `convert_*` function needed for your use case (e.g., `convert_stream()`, or `convert_local()`). See the Security Considerations section of the documentation for .
**Stack:** python, typescript, docker, postgres
**Repo:** https://github.com/microsoft/markitdown.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/markitdown/). Si necesitas el código: git clone https://github.com/microsoft/markitdown.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** alimentas LLMs con documentos de formatos variados
**Evita si:** ya tienes el texto limpio o necesitas fidelidad de layout total (no es un reconstructor de PDF).
**Combina con:** `ppt-master`, `open-notebook`, `docs → presentaciones`

## `ppt-master`
role=library · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** PPT Master — AI generates natively editable PPTX from any document
**Stack:** python, typescript, postgres
**Repo:** https://github.com/hugohe3/ppt-master.git

**Instalación** [~]: `pip install ppt-master   (o: uv add ppt-master)`
_Nombre PyPI puede diferir de 'ppt-master'; verifica en pypi.org._

**Elige si:** quieres PPTX editable de Office rápido
**Evita si:** prefieres slides web por código ([reveal.js](#-revealjs)) o control de diseño pixel-perfect.
**Combina con:** `markitdown`, `docs → presentaciones`

## `reveal.js`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** reveal.js is an open source HTML presentation framework. It enables anyone with a web browser to create beautiful presentations for free. Check out the live demo at revealjs.com.
**Stack:** javascript/typescript, typescript, javascript
**Repo:** https://github.com/hakimel/reveal.js.git

**Instalación** [~]: `git clone https://github.com/hakimel/reveal.js.git && cd reveal.js && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres slides web por código, versionables
**Evita si:** necesitas PPTX editable en Office ([ppt-master](#-ppt-master)) o un editor visual de slides.
**Combina con:** `markitdown`, `ppt-master`, `revealjs`
