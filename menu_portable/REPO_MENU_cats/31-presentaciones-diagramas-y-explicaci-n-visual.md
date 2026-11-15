# 31. Presentaciones, diagramas y explicación visual — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `archify`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=diagramas,agent-skills,ai-agents,architecture-diagram,claude-code,claude-skills,codex,coding-agents · tools=claude-code,codex

**Qué es:** Skill para convertir ideas, planes y bases de código en diagramas y visualizaciones HTML interactivas. El agente transforma una descripción en una visualización que se puede abrir y explorar en el navegador.
**Stack:** JavaScript, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/tt-a1i/archify

**Instalación** [?]: `Seguir la instalación original: https://github.com/tt-a1i/archify/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres explicar una arquitectura o un plan mediante una visualización interactiva
**Evita si:** el formato de salida no encaja con tus documentos
**Combina con:** `codex`

## `diagram-design`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=diagramas,skill,html

**Qué es:** Skill para que un agente cree diagramas explicativos con HTML y SVG, con criterios de composición y legibilidad.
**Stack:** HTML
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/cathrynlavery/diagram-design

**Instalación** [?]: `Seguir la instalación original: https://github.com/cathrynlavery/diagram-design/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para que un agente cree diagramas explicativos con HTML y SVG, con criterios de composición y legibilidad.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `marp`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=slides,typescript

**Qué es:** Escribes Markdown con separadores y obtienes slides limpias; tiene extensión de VS Code.
**Stack:** TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/marp-team/marp

**Instalación** [?]: `Seguir la instalación original: https://github.com/marp-team/marp/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres slides simples en Markdown
**Evita si:** necesitas interactividad y componentes; mira `slidev`
**Alternativas (elige una):** `slidev`, `reveal.js`

## `mermaid`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=docs,dataviz,typescript

**Qué es:** GitHub, Notion y muchos editores lo renderizan de forma nativa; los LLM lo escriben muy bien.
**Stack:** TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mermaid-js/mermaid

**Instalación** [?]: `Seguir la instalación original: https://github.com/mermaid-js/mermaid/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres diagramas como texto
**Evita si:** necesitas dibujar a mano alzada; mira `excalidraw`
**Combina con:** `slidev`
**Alternativas (elige una):** `excalidraw`

## `ppt-master`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=slides,python

**Qué es:** Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos. Necesita un agente con acceso a un modelo; los servicios opcionales de imágenes o contenido se revisan por separado.
**Stack:** Python, python-pptx
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/hugohe3/ppt-master

**Instalación** [+]: `npx skills add hugohe3/ppt-master`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres PPTX editable de Office rápido
**Evita si:** prefieres slides web por código (reveal.js) o control de diseño pixel-perfect
**Combina con:** `markitdown`
**Alternativas (elige una):** `presenton`

## `presenton`
role=app · exec=hybrid · setup=easy · mcp=False · prov=openai,google,local · tags=slides,agents,typescript

**Qué es:** Crea presentaciones editables a partir de un prompt o documento, con tus plantillas, y exporta a PPTX o PDF.
**Stack:** TypeScript, Python, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/presenton/presenton

**Instalación** [?]: `Seguir la instalación original: https://github.com/presenton/presenton/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres generar presentaciones de negocio con IA
**Evita si:** prefieres control total como código; mira `slidev`
**Combina con:** `ollama`
**Alternativas (elige una):** `ppt-master`

## `reveal.js`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=slides,javascript

**Qué es:** Convierte las diapositivas en una página web versionable y reproducible por código.
**Stack:** JavaScript/HTML
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/hakimel/reveal.js

**Instalación** [?]: `Seguir la instalación original: https://github.com/hakimel/reveal.js/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres slides web por código, versionables
**Evita si:** necesitas PPTX editable en Office (ppt-master) o un editor visual de slides
**Combina con:** `markitdown`
**Alternativas (elige una):** `slidev`, `marp`

## `slidev`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=slides,typescript

**Qué es:** Escribe tus slides en Markdown y obtén resaltado de código, diagramas, animaciones y exportación a PDF. Los agentes de código lo usan bien.
**Stack:** TypeScript, Vue, Vite
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/slidevjs/slidev

**Instalación** [?]: `Seguir la instalación original: https://github.com/slidevjs/slidev/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** haces presentaciones técnicas y quieres control como código
**Evita si:** necesitas slides para negocio generadas con IA; mira `presenton`
**Combina con:** `mermaid`
**Alternativas (elige una):** `marp`, `reveal.js`
