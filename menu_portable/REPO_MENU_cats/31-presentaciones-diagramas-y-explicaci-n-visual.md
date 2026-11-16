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

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

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

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/mermaid-js/mermaid/blob/develop/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar un proceso; Preparar un diagrama de secuencia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Escribe un flujo con una decisión y comprueba que sus flechas representan el proceso real
**Qué comprobar:** Puedes relacionar cada nodo con un paso
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `slidev`, `claude-code`, `archify`, `marp`, `reveal.js`
**Alternativas (elige una):** `excalidraw`

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

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

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

**Instalación** [?]:

```
Seguir la instalación original: https://revealjs.com/installation
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

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
