# 31. Presentaciones, diagramas y explicación visual — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `archify`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=diagramas,agent-skills,ai-agents,architecture-diagram,claude-code,claude-skills,codex,coding-agents · tools=claude-code,codex

**Qué es:** Skill para convertir ideas, planes y bases de código en diagramas y visualizaciones HTML interactivas.
**Stack:** Agente con archivos y ejecución; idea o repositorio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La skill usa el agente; los servicios de patrocinadores y planes externos no son parte incluida del proyecto
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Documenta Claude Code y Codex; la comprobación de actualizaciones puede hacer una petición de metadatos y no instala nuevas versiones automáticamente
- Coste: Consumo del agente que ya utilizas. La skill usa el agente; los servicios de patrocinadores y planes externos no son parte incluida del proyecto
- Equipo: Preparación según la ruta elegida. Agente con archivos y ejecución; idea o repositorio de prueba
**Repo:** https://github.com/tt-a1i/archify

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/tt-a1i/archify/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar una arquitectura; Preparar un plan de trabajo visual
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Dibuja el flujo de una app pequeña y revisa que cada componente exista en la fuente
**Qué comprobar:** Puedes contrastar nodos, enlaces y responsabilidades
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `opencode`, `mermaid`
**Alternativas (elige una):** `diagram-design`

## `d2`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=diagrams,go,cli,docs-as-code

**Qué es:** Lenguaje declarativo de diagramas que convierte texto en diagramas SVG, PNG, PDF o PPTX, con temas, modo boceto y tres motores de layout incluidos.
**Stack:** Go, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/d2lang/d2

**Instalación** [+]:

```
curl -fsSL https://d2lang.com/install.sh | sh -s --
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: mantener diagramas de arquitectura como texto versionado junto al código; generar diagramas desde scripts o documentación técnica
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con el script oficial, escribe `x -> y` en `in.d2` y ejecuta `d2 --watch in.d2 out.svg`.
**Qué comprobar:** Se abre una vista en el navegador que se actualiza al guardar el archivo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `kroki`, `pandoc`, `logseq`, `claude-code`
**Alternativas (elige una):** `plantuml`, `mermaid`

## `diagram-design`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=diagramas,skill,html

**Qué es:** Skill para que un agente cree diagramas explicativos con HTML y SVG, con criterios de composición y legibilidad.
**Stack:** Agente compatible; proceso descrito; marca opcional; navegador
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el agente; el archivo puede evitar red usando fuentes del sistema en lugar de Google Fonts
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Portable en hosts Agent Skills; un solo HTML con SVG no implica que todas las fuentes o recursos externos se hayan incrustado
- Coste: Consumo del agente que ya utilizas. Usa el agente; el archivo puede evitar red usando fuentes del sistema en lugar de Google Fonts
- Equipo: Preparación según la ruta elegida. Agente compatible; proceso descrito; marca opcional; navegador
**Repo:** https://github.com/cathrynlavery/diagram-design

**Instalación** [+]:

```
npx skills add cathrynlavery/diagram-design
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar un proceso comercial; Explicar una arquitectura con SVG
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera un diagrama de cinco pasos y revisa orden, etiquetas y legibilidad a tamaño móvil
**Qué comprobar:** Puedes explicar cada relación y abrir el HTML
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `playwright`, `claude-code`, `slidev`
**Alternativas (elige una):** `archify`

## `drawio`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=diagrams,editor,javascript,app

**Qué es:** Editor de diagramas en el navegador o escritorio, sin servidor: diagramas de flujo, redes, UML y arquitectura cloud, con importación de Mermaid y PlantUML.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/jgraph/drawio

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/jgraph/drawio/blob/dev/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: dibujar diagramas de arquitectura o redes con iconos de AWS, Azure o GCP; convertir un diagrama Mermaid en uno editable a mano
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Abre app.diagrams.net en el navegador o instala draw.io Desktop, y crea un diagrama desde una plantilla.
**Qué comprobar:** Guardas un archivo .drawio editable o lo exportas a PNG, SVG o PDF.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `mermaid`, `plantuml`, `kroki`

## `kroki`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=diagrams,api,self-hosted,docker

**Qué es:** Servidor que unifica más de 25 lenguajes de diagramas (PlantUML, Mermaid, D2, Graphviz, Excalidraw…) detrás de una sola API HTTP que devuelve SVG o PNG.
**Stack:** JavaScript, package.json, pom.xml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/yuzutech/kroki

**Instalación** [+]:

```
docker run -d -p 8000:8000 yuzutech/kroki
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: renderizar diagramas de varios lenguajes en una wiki o generador de documentación; autoalojar el renderizado para no enviar diagramas a servicios públicos
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Ejecuta `docker run -d -p 8000:8000 yuzutech/kroki` y abre `http://localhost:8000/plantuml/svg/` con un diagrama codificado.
**Qué comprobar:** Obtienes el SVG del diagrama desde tu propio servidor.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `plantuml`, `d2`, `mermaid`, `excalidraw`, `drawio`

## `marp`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=slides,typescript

**Qué es:** Entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de editor se distribuyen por separado.
**Stack:** Marp CLI o extensión de VS Code; Markdown; contenido propio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El ecosistema básico no exige API de IA; recursos y distribución tienen condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Este repositorio es la entrada y web del ecosistema; el CLI y extensión están en repos separados y los formatos de exportación no prometen editabilidad nativa equivalente a PPT generado con formas
- Coste: Sin pago a un modelo en la ruta básica. El ecosistema básico no exige API de IA; recursos y distribución tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Marp CLI o extensión de VS Code; Markdown; contenido propio
**Repo:** https://github.com/marp-team/marp

**Instalación** [+]:

```
npm install --save-dev @marp-team/marp-cli
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar slides sencillas; Versionar una presentación en Git
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige la herramienta Marp CLI o VS Code y exporta tres diapositivas de muestra
**Qué comprobar:** Puedes comparar Markdown y salida exportada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `mermaid`, `pandoc`
**Alternativas (elige una):** `slidev`, `reveal.js`

## `mermaid`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=docs,dataviz,typescript

**Qué es:** Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown.
**Stack:** Editor o entorno que renderice Mermaid; texto del proceso
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El render básico MIT no necesita API de IA; servicios hospedados o AI son ofertas independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No requiere un LLM para convertir sintaxis a diagramas; un diagrama válido puede representar un proceso equivocado y necesita revisión
- Coste: Sin pago a un modelo en la ruta básica. El render básico MIT no necesita API de IA; servicios hospedados o AI son ofertas independientes
- Equipo: Preparación según la ruta elegida. Editor o entorno que renderice Mermaid; texto del proceso
**Repo:** https://github.com/mermaid-js/mermaid

**Instalación** [+]:

```
npm install mermaid
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar un proceso; Preparar un diagrama de secuencia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Escribe un flujo con una decisión y comprueba que sus flechas representan el proceso real
**Qué comprobar:** Puedes relacionar cada nodo con un paso
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `slidev`, `claude-code`, `archify`, `marp`, `reveal.js`, `drawio`
**Alternativas (elige una):** `excalidraw`, `d2`, `plantuml`

## `plantuml`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=diagrams,uml,java,docs-as-code

**Qué es:** Herramienta clásica que genera diagramas UML y técnicos (secuencia, clases, actividad, Gantt, mapas mentales) a partir de descripciones de texto.
**Stack:** Java, Dockerfile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/plantuml/plantuml

**Instalación** [+]:

```
git clone https://github.com/plantuml/plantuml.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: documentar diagramas de secuencia y clases como texto en el repositorio; generar diagramas automáticamente en la documentación técnica
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga el JAR de las releases, escribe un `@startuml` sencillo en `a.puml` y ejecuta `java -jar plantuml.jar a.puml`.
**Qué comprobar:** Obtienes un PNG con el diagrama.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `kroki`, `claude-code`, `drawio`
**Alternativas (elige una):** `d2`, `mermaid`

## `ppt-master`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=slides,python

**Qué es:** Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos.
**Stack:** Python 3.10–3.14; agente con archivos; dependencias; documento y plantilla autorizados
**Acceso y costes:**
- API de IA: API de IA opcional. Usa el agente y posibles proveedores de imagen o voz; no incluye créditos ni acceso a patrocinadores
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: Modelo local no documentado. Claude Code es la ruta más probada por el autor y Codex figura como CLI compatible; logos de patrocinadores no prueban integración ni precio de sus servicios
- Coste: El coste depende del proveedor o la ruta. Usa el agente y posibles proveedores de imagen o voz; no incluye créditos ni acceso a patrocinadores
- Equipo: Preparación según la ruta elegida. Python 3.10–3.14; agente con archivos; dependencias; documento y plantilla autorizados
**Repo:** https://github.com/hugohe3/ppt-master

**Instalación** [+]:

```
git clone https://github.com/hugohe3/ppt-master.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una presentación de un informe; Adaptar una plantilla corporativa
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera tres diapositivas de un texto breve y revisa cifras, editabilidad y fuentes en PowerPoint
**Qué comprobar:** Puedes editar formas y comprobar que el contenido coincide con el documento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `markitdown`, `pandoc`
**Alternativas (elige una):** `presenton`

## `presenton`
role=app · exec=hybrid · setup=easy · mcp=True · prov=openai,google,local · tags=slides,agents,typescript

**Qué es:** Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai.
**Stack:** Docker o app compatible; proveedor de texto e imagen; contraseña propia; datos ficticios
**Acceso y costes:**
- API de IA: API de IA opcional. Admite API, Ollama, LM Studio y ruta Codex con OAuth; imágenes y otros servicios pueden tener costes separados
- Claude Code: Herramienta MCP para el agente
- Codex: Integración documentada por el proyecto
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. El servidor ofrece MCP Streamable HTTP autenticado; MCP está desactivado en la app Electron y Codex como proveedor es distinto de Codex como cliente MCP
- Coste: El coste depende del proveedor o la ruta. Admite API, Ollama, LM Studio y ruta Codex con OAuth; imágenes y otros servicios pueden tener costes separados
- Equipo: Preparación según la ruta elegida. Docker o app compatible; proveedor de texto e imagen; contraseña propia; datos ficticios
**Repo:** https://github.com/presenton/presenton

**Instalación** [+]:

```
docker run -it --name presenton \
  -p 5001:80 \
  -e AUTH_USERNAME=admin \
  -e AUTH_PASSWORD=change-this-password \
  -v "./app_data:/app_data" \
  ghcr.io/presenton/presenton:latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una presentación desde un documento; Comparar una plantilla con generación libre
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera tres slides y revisa afirmaciones, diseño y exportación antes de compartir
**Qué comprobar:** Puedes identificar proveedores y editar el contenido generado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `claude-code`, `litellm`
**Alternativas (elige una):** `ppt-master`

## `reveal.js`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=slides,javascript

**Qué es:** Framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados.
**Stack:** Node según ruta; HTML; contenido propio; navegador
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El framework MIT es gratuito; curso, hosting y servicios externos son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El curso de pago no es necesario para la biblioteca y no se requiere modelo de IA para renderizar slides
- Coste: Sin pago a un modelo en la ruta básica. El framework MIT es gratuito; curso, hosting y servicios externos son independientes
- Equipo: Preparación según la ruta elegida. Node según ruta; HTML; contenido propio; navegador
**Repo:** https://github.com/hakimel/reveal.js

**Instalación** [+]:

```
npm install reveal.js
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una presentación web; Mostrar un ejemplo interactivo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea dos slides y una nota del orador y prueba navegación y presentación
**Qué comprobar:** Puedes abrir la presentación y ver las notas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mermaid`, `gsap`, `claude-code`, `pandoc`
**Alternativas (elige una):** `slidev`, `marp`

## `slidev`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=slides,typescript

**Qué es:** Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue.
**Stack:** Node; editor de texto; navegador; contenido propio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. MIT y sin API de IA obligatoria; hosting y recursos externos tienen condiciones independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una herramienta orientada a Markdown y componentes Vue; utilizar un agente para escribir el contenido no la convierte en plugin de ese agente
- Coste: Sin pago a un modelo en la ruta básica. MIT y sin API de IA obligatoria; hosting y recursos externos tienen condiciones independientes
- Equipo: Preparación según la ruta elegida. Node; editor de texto; navegador; contenido propio
**Repo:** https://github.com/slidevjs/slidev

**Instalación** [+]:

```
npm init slidev
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una charla técnica; Explicar un ejemplo de código
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea tres diapositivas Markdown y modifica una antes de exportar
**Qué comprobar:** Puedes comprobar contenido, notas y navegación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mermaid`, `claude-code`, `playwright`, `diagram-design`
**Alternativas (elige una):** `marp`, `reveal.js`
