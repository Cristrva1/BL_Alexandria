# Alexandría para agentes · Presentaciones, diagramas y explicación visual

Categoría 31 completa (12 repos, 2 subcategorías). Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=31 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `slidev` | slides | Presentaciones para desarrolladores escritas en Markdown, con código en vivo y… | 1 Básico | 73 | MIT (OSI permisiva) | recomendado |
| `ppt-master` | slides | Herramientas e instrucciones para que un agente cree presentaciones PowerPoint… | 1 Básico | 69 | MIT (OSI permisiva) | recomendado |
| `presenton` | slides | Generador de presentaciones con IA, open source y con API, alternativa a Gamma… | 1 Básico | 60 | Apache-2.0 (OSI permisiva) | alternativa |
| `reveal.js` | slides | Framework veterano para crear presentaciones (slides) en HTML, con… | 2 Intermedio | 59 | MIT (OSI permisiva) | alternativa |
| `marp` | slides | Entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de… | 1 Básico | 47 | MIT (OSI permisiva) | alternativa |
| `mermaid` | diagramas | Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a… | 2 Intermedio | 78 | MIT (OSI permisiva) | recomendado |
| `archify` | diagramas | Skill para convertir ideas, planes y bases de código en diagramas y… | 1 Básico | 70 | Apache-2.0 (OSI permisiva) | recomendado |
| `drawio` | diagramas | Editor de diagramas en el navegador o escritorio, sin servidor: diagramas de… | 1 Básico | 69 | Apache-2.0 (OSI permisiva) | sin grupo |
| `kroki` | diagramas | Servidor que unifica más de 25 lenguajes de diagramas (PlantUML, Mermaid, D2… | 1 Básico | 60 | MIT (OSI permisiva) | sin grupo |
| `d2` | diagramas | Lenguaje declarativo de diagramas que convierte texto en diagramas SVG, PNG… | 1 Básico | 58 | MPL-2.0 (OSI copyleft) | alternativa |
| `diagram-design` | diagramas | Skill para que un agente cree diagramas explicativos con HTML y SVG, con… | 2 Intermedio | 56 | MIT (OSI permisiva) | alternativa |
| `plantuml` | diagramas | Herramienta clásica que genera diagramas UML y técnicos (secuencia, clases… | 1 Básico | 55 | Multilicencia (GPL-3.0, LGPL-3.0, Apache-2.0, EPL-2.0 o MIT) (OSI copyleft) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Slidev (`slidev`)

- **Repo:** https://github.com/slidevjs/slidev · MIT · nivel 1 · 73/100 · recomendado en «Presentaciones desde Markdown»
- **Qué es:** Slidev, presentaciones para desarrolladores escritas en Markdown, de Anthony Fu y slidevjs. Licencia MIT. Es madura (~49k estrellas, v53.1.0).
- **Cuándo elegirlo:** Casos: Preparar una charla técnica; Explicar un ejemplo de código.
- **Requisitos:** nivel 1: preparación sencilla; Node; editor de texto; navegador; contenido propio; hardware prerequisites; API de IA: no; Node; editor de texto; navegador; contenido propio.
- **Instalación (documentada en la fuente; no ejecutada):** `npm init slidev` — fuente: https://github.com/slidevjs/slidev/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea tres diapositivas Markdown y modifica una antes de exportar Éxito: Puedes comprobar contenido, notas y navegación
- **Combina con:** `mermaid` [31/diagramas], `claude-code` [20/terminal], `playwright` [32/bibliotecas], `diagram-design` [31/diagramas]
- **Alternativas:** `reveal.js`, `marp`
- **Riesgos y avisos:** Alternativas (elige una): marp, reveal.js. Es una herramienta orientada a Markdown y componentes Vue; utilizar un agente para escribir el contenido no la convierte en plugin de ese agente.

### ppt-master (`ppt-master`)

- **Repo:** https://github.com/hugohe3/ppt-master · MIT · nivel 1 · 69/100 · recomendado en «Generación de presentaciones con IA»
- **Qué es:** PPT Master, workflow (skill) que genera presentaciones PowerPoint nativas y editables a partir de cualquier documento, de @hugohe3. Licencia MIT. Creado en diciembre de 2025, tiene ~77k estrellas (v6.9.0); el README incluye patrocinios de…
- **Cuándo elegirlo:** Casos: Preparar una presentación de un informe; Adaptar una plantilla corporativa.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Python 3.10–3.14; agente con archivos; dependencias; documento y plantilla autorizados; hardware prerequisites; API de IA: opcional; Python 3.10–3.14; agente con archivos; dependencias; documento y plantilla autorizados.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/hugohe3/ppt-master.git` — fuente: https://github.com/hugohe3/ppt-master/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera tres diapositivas de un texto breve y revisa cifras, editabilidad y fuentes en PowerPoint Éxito: Puedes editar formas y comprobar que el contenido coincide con el documento
- **Combina con:** `claude-code` [20/terminal], `markitdown` [13/conversion], `pandoc` [13/conversion]
- **Alternativas:** `presenton`
- **Riesgos y avisos:** Alternativas (elige una): presenton. Claude Code es la ruta más probada por el autor y Codex figura como CLI compatible; logos de patrocinadores no prueban integración ni precio de sus servicios.

### Presenton (`presenton`)

- **Repo:** https://github.com/presenton/presenton · Apache-2.0 · nivel 1 · 60/100 · alternativa en «Generación de presentaciones con IA»
- **Qué es:** Presenton, generador open source de presentaciones con IA y API, alternativa a Gamma o Beautiful AI. Licencia Apache-2.0. Tiene ~12k estrellas; app web autoalojada con Docker y app de escritorio en beta.
- **Cuándo elegirlo:** Casos: Preparar una presentación desde un documento; Comparar una plantilla con generación libre.
- **Requisitos:** nivel 1: preparación sencilla; Docker o app compatible; proveedor de texto e imagen; contraseña propia; datos ficticios; hardware prerequisites; API de IA: opcional; Docker o app compatible; proveedor de texto e imagen; contraseña propia; datos ficticios.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/presenton/presenton/blob/main/README.md

  ```bash
  docker run -it --name presenton \
    -p 5001:80 \
    -e AUTH_USERNAME=admin \
    -e AUTH_PASSWORD=change-this-password \
    -v "./app_data:/app_data" \
    ghcr.io/presenton/presenton:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Genera tres slides y revisa afirmaciones, diseño y exportación antes de compartir Éxito: Puedes identificar proveedores y editar el contenido generado
- **Combina con:** `ollama` [8/motores], `claude-code` [20/terminal], `litellm` [23/serving]
- **Alternativas:** `ppt-master`
- **Riesgos y avisos:** Alternativas (elige una): ppt-master. El servidor ofrece MCP Streamable HTTP autenticado; MCP está desactivado en la app Electron y Codex como proveedor es distinto de Codex como cliente MCP.

### reveal.js (`reveal.js`)

- **Repo:** https://github.com/hakimel/reveal.js · MIT · nivel 2 · 59/100 · alternativa en «Presentaciones desde Markdown»
- **Qué es:** reveal.js, framework HTML de presentaciones de @hakimel. Licencia MIT. Es veterano y estable (creado en 2011, ~73k estrellas, v6.0.2).
- **Cuándo elegirlo:** Casos: Preparar una presentación web; Mostrar un ejemplo interactivo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node según ruta; HTML; contenido propio; navegador; hardware prerequisites; API de IA: no; Node según ruta; HTML; contenido propio; navegador.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install reveal.js` — fuente: https://revealjs.com/installation
- **Primera prueba propuesta (no ejecutada):** Crea dos slides y una nota del orador y prueba navegación y presentación Éxito: Puedes abrir la presentación y ver las notas
- **Combina con:** `mermaid` [31/diagramas], `gsap` [26/animacion], `claude-code` [20/terminal], `pandoc` [13/conversion]
- **Alternativas:** `slidev`, `marp`
- **Riesgos y avisos:** Alternativas (elige una): slidev, marp. El curso de pago no es necesario para la biblioteca y no se requiere modelo de IA para renderizar slides.

### Marp (`marp`)

- **Repo:** https://github.com/marp-team/marp · MIT · nivel 1 · 47/100 · alternativa en «Presentaciones desde Markdown»
- **Qué es:** Marp, ecosistema para escribir presentaciones en Markdown plano, de marp-team. Licencia MIT. Es maduro (~13k estrellas); este repo es el punto de entrada (web y documentación) a Marpit, Marp Core, Marp CLI y Marp for VS Code.
- **Cuándo elegirlo:** Casos: Preparar slides sencillas; Versionar una presentación en Git.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Marp CLI o extensión de VS Code; Markdown; contenido propio; hardware prerequisites; API de IA: no; Marp CLI o extensión de VS Code; Markdown; contenido propio.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install --save-dev @marp-team/marp-cli` — fuente: https://github.com/marp-team/marp/blob/main/website/docs/introduction/install.md
- **Primera prueba propuesta (no ejecutada):** Elige la herramienta Marp CLI o VS Code y exporta tres diapositivas de muestra Éxito: Puedes comparar Markdown y salida exportada
- **Combina con:** `claude-code` [20/terminal], `mermaid` [31/diagramas], `pandoc` [13/conversion]
- **Alternativas:** `slidev`, `reveal.js`
- **Riesgos y avisos:** Alternativas (elige una): slidev, reveal.js. Este repositorio es la entrada y web del ecosistema; el CLI y extensión están en repos separados y los formatos de exportación no prometen editabilidad nativa….

### Mermaid (`mermaid`)

- **Repo:** https://github.com/mermaid-js/mermaid · MIT · nivel 2 · 78/100 · recomendado en «Diagramas como código»
- **Qué es:** Mermaid, herramienta para generar diagramas a partir de texto tipo Markdown, de mermaid-js. Licencia MIT. Es madura y muy extendida (~91k estrellas), y tiene soporte nativo en GitHub, Slidev y muchas otras herramientas.
- **Cuándo elegirlo:** Casos: Documentar un proceso; Preparar un diagrama de secuencia.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Editor o entorno que renderice Mermaid; texto del proceso; hardware prerequisites; API de IA: no; Editor o entorno que renderice Mermaid; texto del proceso.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install mermaid` — fuente: https://github.com/mermaid-js/mermaid/blob/develop/docs/intro/getting-started.md
- **Primera prueba propuesta (no ejecutada):** Escribe un flujo con una decisión y comprueba que sus flechas representan el proceso real Éxito: Puedes relacionar cada nodo con un paso
- **Combina con:** `slidev` [31/slides], `claude-code` [20/terminal], `archify`, `marp` [31/slides], `reveal.js` [31/slides], `drawio`
- **Alternativas:** `d2`, `plantuml`, `excalidraw`
- **Riesgos y avisos:** Alternativas (elige una): excalidraw. No requiere un LLM para convertir sintaxis a diagramas; un diagrama válido puede representar un proceso equivocado y necesita revisión.

### archify (`archify`)

- **Repo:** https://github.com/tt-a1i/archify · Apache-2.0 · nivel 1 · 70/100 · recomendado en «Skills de diagramas de arquitectura»
- **Qué es:** Archify, skill que convierte ideas, preguntas o planes en visuales HTML interactivos, de @tt-a1i. Licencia Apache-2.0 (las concesiones MIT históricas siguen vigentes; servicios de terceros y planes de pago no son del proyecto).
- **Cuándo elegirlo:** Casos: Explicar una arquitectura; Preparar un plan de trabajo visual.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente con archivos y ejecución; idea o repositorio de prueba; hardware prerequisites; API de IA: no; Agente con archivos y ejecución; idea o repositorio de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/tt-a1i/archify/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Dibuja el flujo de una app pequeña y revisa que cada componente exista en la fuente Éxito: Puedes contrastar nodos, enlaces y responsabilidades
- **Combina con:** `claude-code` [20/terminal], `opencode` [20/terminal], `mermaid`
- **Alternativas:** `diagram-design`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativa (elige una): diagram-design. Documenta Claude Code y Codex; la comprobación de actualizaciones puede hacer una petición de metadatos y no instala nuevas versiones automáticamente.

### draw.io (`drawio`)

- **Repo:** https://github.com/jgraph/drawio · Apache-2.0 · nivel 1 · 69/100
- **Qué es:** Editor de diagramas de código abierto (Apache-2.0) de JGraph, muy usado y activo. Los iconos, plantillas y librerías de formas tienen condiciones adicionales. El proyecto no acepta contribuciones externas.
- **Cuándo elegirlo:** Casos: dibujar diagramas de arquitectura o redes con iconos de AWS, Azure o GCP; convertir un diagrama Mermaid en uno editable a mano.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; JavaScript; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/jgraph/drawio/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Abre app.diagrams.net en el navegador o instala draw.io Desktop, y crea un diagrama desde una plantilla. Éxito: Guardas un archivo .drawio editable o lo exportas a PNG, SVG o PDF.
- **Combina con:** `claude-code` [20/terminal], `mermaid`, `plantuml`, `kroki`

### Kroki (`kroki`)

- **Repo:** https://github.com/yuzutech/kroki · MIT · nivel 1 · 60/100
- **Qué es:** Servidor de código abierto (MIT) de Yuzutech, con instancia pública gratuita en kroki.io y despliegue propio con Docker. Activo.
- **Cuándo elegirlo:** Casos: renderizar diagramas de varios lenguajes en una wiki o generador de documentación; autoalojar el renderizado para no enviar diagramas a servicios públicos.
- **Requisitos:** nivel 1: preparación sencilla; JavaScript, package.json, pom.xml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d -p 8000:8000 yuzutech/kroki` — fuente: https://github.com/yuzutech/kroki/blob/main/README.adoc
- **Primera prueba propuesta (no ejecutada):** Ejecuta `docker run -d -p 8000:8000 yuzutech/kroki` y abre `http://localhost:8000/plantuml/svg/` con un diagrama codificado. Éxito: Obtienes el SVG del diagrama desde tu propio servidor.
- **Combina con:** `plantuml`, `d2`, `mermaid`, `excalidraw` [9/diseno], `drawio`
- **Riesgos y avisos:** Útil como backend para Asciidoctor, MkDocs y otros generadores; autoalojarlo evita enviar diagramas a kroki.io.

### D2 (`d2`)

- **Repo:** https://github.com/d2lang/d2 · MPL-2.0 · nivel 1 · 58/100 · alternativa en «Diagramas como código»
- **Qué es:** Lenguaje y herramienta de código abierto (MPL-2.0) de Terrastruct. Muy popular y activo. Su motor TALA, antes un componente aparte, ahora se incluye en el repositorio bajo la misma licencia.
- **Cuándo elegirlo:** Casos: mantener diagramas de arquitectura como texto versionado junto al código; generar diagramas desde scripts o documentación técnica.
- **Requisitos:** nivel 1: preparación sencilla; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://d2lang.com/install.sh | sh -s --` — fuente: https://github.com/d2lang/d2/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con el script oficial, escribe `x -> y` en `in.d2` y ejecuta `d2 --watch in.d2 out.svg`. Éxito: Se abre una vista en el navegador que se actualiza al guardar el archivo.
- **Combina con:** `kroki`, `pandoc` [13/conversion], `logseq` [15/notas], `claude-code` [20/terminal]
- **Alternativas:** `mermaid`, `plantuml`
- **Riesgos y avisos:** Alternativa de PlantUML y Mermaid; D2 prioriza la legibilidad del código y la calidad del layout.

### diagram-design (`diagram-design`)

- **Repo:** https://github.com/cathrynlavery/diagram-design · MIT · nivel 2 · 56/100 · alternativa en «Skills de diagramas de arquitectura»
- **Qué es:** diagram-design, skill que dibuja diagramas como un único archivo HTML + SVG autocontenido con tu marca, de @cathrynlavery. Licencia MIT. Creado en abril de 2026, tiene ~67k estrellas y sin releases.
- **Cuándo elegirlo:** Casos: Documentar un proceso comercial; Explicar una arquitectura con SVG.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente compatible; proceso descrito; marca opcional; navegador; hardware prerequisites; API de IA: no; Agente compatible; proceso descrito; marca opcional; navegador.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add cathrynlavery/diagram-design` — fuente: https://github.com/cathrynlavery/diagram-design/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera un diagrama de cinco pasos y revisa orden, etiquetas y legibilidad a tamaño móvil Éxito: Puedes explicar cada relación y abrir el HTML
- **Combina con:** `playwright` [32/bibliotecas], `claude-code` [20/terminal], `slidev` [31/slides]
- **Alternativas:** `archify`
- **Riesgos y avisos:** Alternativa (elige una): archify. Portable en hosts Agent Skills; un solo HTML con SVG no implica que todas las fuentes o recursos externos se hayan incrustado.

### PlantUML (`plantuml`)

- **Repo:** https://github.com/plantuml/plantuml · Multilicencia (GPL-3.0, LGPL-3.0, Apache-2.0, EPL-2.0 o MIT) · nivel 1 · 55/100 · alternativa en «Diagramas como código»
- **Qué es:** Proyecto de código abierto veterano y muy activo, publicado con varias licencias a elegir (GPL, LGPL, Apache, EPL o MIT) según la distribución. Muy integrado en wikis, IDEs y herramientas de documentación.
- **Cuándo elegirlo:** Casos: documentar diagramas de secuencia y clases como texto en el repositorio; generar diagramas automáticamente en la documentación técnica.
- **Requisitos:** nivel 1: preparación sencilla; Java, Dockerfile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/plantuml/plantuml.git` — fuente: https://github.com/plantuml/plantuml/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el JAR de las releases, escribe un `@startuml` sencillo en `a.puml` y ejecuta `java -jar plantuml.jar a.puml`. Éxito: Obtienes un PNG con el diagrama.
- **Combina con:** `kroki`, `claude-code` [20/terminal], `drawio`
- **Alternativas:** `mermaid`, `d2`
- **Riesgos y avisos:** Alternativa de D2 y Mermaid; PlantUML cubre más tipos de diagramas UML formales.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-31.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Presentaciones, diagramas y explicación visual», lee `docs/alexandria/categoria-31.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-31.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
