# 27. Skills de diseño, contenido y especialidades — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `3dviz-pro-max`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,javascript

**Qué es:** Skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/viettranx/3dviz-pro-max

**Instalación** [?]: `Seguir la instalación original: https://github.com/viettranx/3dviz-pro-max/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible
**Alternativas (elige una):** `threejs-skills`

## `agency-agents`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,prompts,skills,coding-agent

**Qué es:** Plantillas de subagente en Markdown agrupadas por divisiones, como una agencia completa: ingeniería, diseño, paid media, ventas, marketing, producto, testing, seguridad, soporte, finanzas, videojuegos y más. Cada agente define identidad, misión, flujo de trabajo, entregables con ejemplos y métricas de éxito, y hay runbooks que arman equipos para escenarios como un MVP o una campaña.
**Stack:** Markdown, Bash, Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/msitarzewski/agency-agents

**Instalación** [?]: `Seguir la instalación original: https://github.com/msitarzewski/agency-agents/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código
**Evita si:** solo necesitas skills de marketing y growth; mira `marketingskills`
**Combina con:** `marketingskills`, `geo-seo-claude`, `claude-code`
**Alternativas (elige una):** `wshobson-agents`

## `anatomy`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,javascript

**Qué es:** Skill para crear ilustraciones isométricas e interactivas de máquinas y sistemas con SVG y efectos visuales opcionales.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/wheresryan22/anatomy

**Instalación** [?]: `Seguir la instalación original: https://github.com/wheresryan22/anatomy/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para crear ilustraciones isométricas e interactivas de máquinas y sistemas con SVG y efectos visuales opcionales.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `arcads-claude-code`
role=skill · exec=cloud · setup=medium · mcp=False · prov=— · tags=video,image,skills,python

**Qué es:** Repo de trabajo que convierte Claude Code o Cursor en un estudio de anuncios: genera videos UGC, presentaciones de producto, lookbooks y miniaturas de YouTube con los modelos de Arcads, y anuncios estáticos para Meta con 37 plantillas. Incluye pipelines multipaso (estilo Pixar o plastilina con ffmpeg), subtitulado con Whisper y HyperFrames, y publicación como anuncios pausados en Meta.
**Stack:** Python, Bash, ffmpeg, Node.js (HyperFrames), Whisper
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo de APIs o servicios. La skill funciona dentro del agente, pero las generaciones consumen la API de Arcads; la suscripción del agente no paga Arcads.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial

**Instalación** [?]: `Seguir la instalación original: https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** ya tienes cuenta de Arcads y quieres producir creatividades publicitarias desde Claude Code o Cursor
**Evita si:** quieres generar video con modelos abiertos sin servicio de pago; mira `comfyui` u `openmontage`
**Combina con:** `hyperframes`, `whisper`, `ffmpeg`, `marketingskills`

## `blender-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=creacion-3d,skill,typescript

**Qué es:** Skills para guiar a un agente por modelado y preparación de escenas en Blender mediante herramientas y conexiones MCP.
**Stack:** TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/arjun988/blender-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/arjun988/blender-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills para guiar a un agente por modelado y preparación de escenas en Blender mediante herramientas y conexiones MCP.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible
**Combina con:** `blender`

## `claude-seo`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/AgriciDaniel/claude-seo

**Instalación** [?]: `Seguir la instalación original: https://github.com/AgriciDaniel/claude-seo/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `creative-architect`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=anthropic,openai · tags=direccion-de-arte,fotos-producto,ugc,claude-code,creative-architect

**Qué es:** Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de imagen o video.
**Stack:** Plugin Claude Code; Markdown; conectores o API de medios
**Acceso y costes:**
- API de IA: API de IA opcional. Para preparar briefs y prompts utiliza tu agente. Para generar conecta Higgsfield, Magnific u OpenAI con la cuenta, conector o API que corresponda.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. El plugin vive en tu equipo; la documentación no ofrece un generador local de imágenes o video.
- Coste: El coste depende del proveedor o la ruta. Plugin MIT. Consume tu agente y, si generas medios, los créditos o tarifas del proveedor elegido.
- Equipo: Equipo normal; revisar dependencias. Git y Claude Code para el plugin; los servicios conectados tienen sus propios requisitos.
**Repo:** https://github.com/Hainrixz/creative-architect

**Instalación** [+]: `claude plugin marketplace add Hainrixz/creative-architect
claude plugin install creative-architect@creative-architect`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** ya usas Claude Code y buscas una guía de dirección de arte con proveedores conectables
**Evita si:** necesitas generación local documentada o un plugin nativo de Codex

## `design-dna`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,javascript

**Qué es:** Skill para analizar referencias visuales, extraer decisiones de diseño y generar interfaces con un estilo coherente.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/zanwei/design-dna

**Instalación** [+]: `npx skills add zanwei/design-dna`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Skill para analizar referencias visuales, extraer decisiones de diseño y generar interfaces con un estilo coherente.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `design.md`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design,typescript

**Qué es:** Resuelve la inconsistencia de marca cuando varias personas o agentes tocan la UI.
**Stack:** Markdown/YAML
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/google-labs-code/design.md

**Instalación** [?]: `Seguir la instalación original: https://github.com/google-labs-code/design.md/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres consistencia de marca con IA y usas agentes para UI
**Evita si:** no usas agentes para generar código de UI
**Combina con:** `impeccable`

## `dream-loop`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,javascript

**Qué es:** Skill que combina Blender, generación de imágenes y revisión por un agente para preparar visuales tridimensionales.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función. La generación externa de imágenes, clips, música o voces es una configuración distinta: el plan del agente no incluye automáticamente esas generaciones.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/achimala/dream-loop

**Instalación** [?]: `Seguir la instalación original: https://github.com/achimala/dream-loop/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill que combina Blender, generación de imágenes y revisión por un agente para preparar visuales tridimensionales.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `financial-services`
role=skill · exec=cloud · setup=medium · mcp=False · prov=anthropic · tags=dominio,python

**Qué es:** Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros. Reúne instrucciones y conectores para tareas como análisis de empresas y gestión de documentos financieros.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/financial-services

**Instalación** [?]: `Seguir la instalación original: https://github.com/anthropics/financial-services/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar flujos financieros dentro del ecosistema de Claude
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones
**Combina con:** `claude-code`

## `front-end-checklist`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=skills,ai-agent,ai-agents,checklist,css,front-end-developer-tool,front-end-development,frontend

**Qué es:** Checklist y recursos para revisar aspectos de calidad de un frontend antes de entregarlo. Organiza comprobaciones de implementación y publica material para revisión humana y agentes.
**Stack:** MDX, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/thedaviddias/Front-End-Checklist

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres una lista de revisión de interfaz y entrega web
**Evita si:** tu interfaz ya cubre el mismo propósito con una herramienta equivalente

## `genjutsu`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,python

**Qué es:** Skills de diseño y animación para agentes que trabajan con interfaces web, Android y plataformas de Apple.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/AThevon/genjutsu

**Instalación** [?]: `Seguir la instalación original: https://github.com/AThevon/genjutsu/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills de diseño y animación para agentes que trabajan con interfaces web, Android y plataformas de Apple.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `geo-seo-claude`
role=skill · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=skills,search,pdf,python

**Qué es:** Añade a Claude Code comandos `/geo` que auditan un sitio para buscadores con IA (ChatGPT, Claude, Perplexity, Gemini, AI Overviews) sin dejar el SEO técnico: citabilidad del contenido, acceso de crawlers de IA en robots.txt, menciones de marca, datos estructurados y llms.txt. Genera informes para clientes en Markdown o PDF y lleva un pequeño CRM de prospectos.
**Stack:** Python, Markdown, ReportLab, JSON-LD, Playwright (opcional)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/zubair-trabzada/geo-seo-claude

**Instalación** [?]: `Seguir la instalación original: https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres medir y mejorar cómo te citan los buscadores con IA, no solo tu posición en Google
**Evita si:** solo haces SEO clásico o no usas Claude Code; mira `marketingskills`
**Combina con:** `marketingskills`, `agency-agents`, `playwright`

## `gsap-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,reference

**Qué es:** Skills oficiales con instrucciones y ejemplos para que agentes creen animaciones y utilicen plugins de GSAP.
**Stack:** —
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/greensock/gsap-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/greensock/gsap-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills oficiales con instrucciones y ejemplos para que agentes creen animaciones y utilicen plugins de GSAP.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `hallmark`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,css

**Qué es:** Skill de diseño para agentes que ayuda a construir interfaces con decisiones visuales más específicas y coherentes.
**Stack:** CSS, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Nutlope/hallmark

**Instalación** [?]: `Seguir la instalación original: https://github.com/Nutlope/hallmark/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill de diseño para agentes que ayuda a construir interfaces con decisiones visuales más específicas y coherentes.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `humanizer`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,prompts,docs

**Qué es:** Detecta 26 patrones típicos de la prosa de LLM (contrastes tipo 'no es X, es Y', cierres dramáticos, tríadas forzadas, frases de falsa profundidad, importancia inflada) y reescribe el texto sin cambiar lo que dice. Puede imitar tu estilo si le das una muestra y, sobre un archivo, solo toca la prosa: no el código, los datos ni el frontmatter.
**Stack:** Markdown, SKILL.md
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/blader/humanizer

**Instalación** [?]: `Seguir la instalación original: https://github.com/blader/humanizer/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** publicas textos redactados con IA y quieres que se lean como escritos por una persona
**Evita si:** quieres reglas de estilo cortas para pegar en un system prompt, con rúbrica propia; mira `stop-slop`
**Combina con:** `marketingskills`, `claude-code`, `codex`
**Alternativas (elige una):** `stop-slop`

## `i-have-adhd`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=escritura,skill,python

**Qué es:** Skill para que un agente presente primero la respuesta y organice su salida con menos distracciones y rodeos.
**Stack:** Python, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ayghri/i-have-adhd

**Instalación** [?]: `Seguir la instalación original: https://github.com/ayghri/i-have-adhd/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para que un agente presente primero la respuesta y organice su salida con menos distracciones y rodeos.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `impeccable`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design,rust

**Qué es:** Ataca el patrón repetitivo de interfaces que "huelen" a IA.
**Stack:** Node (`npx impeccable`)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/pbakaus/impeccable

**Instalación** [+]: `npx impeccable`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres frontends que no parezcan generados por IA
**Evita si:** no generas UI con agentes
**Combina con:** `taste-skill`, `ui-ux-pro-max-skill`

## `instagram-agent-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de Instagram.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Jakeschincariol/instagram-agent-skill

**Instalación** [?]: `Seguir la instalación original: https://github.com/Jakeschincariol/instagram-agent-skill/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de Instagram.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `linkedin-agent-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de LinkedIn.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Jakeschincariol/linkedin-agent-skill

**Instalación** [?]: `Seguir la instalación original: https://github.com/Jakeschincariol/linkedin-agent-skill/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de LinkedIn.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `logo-design-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,html

**Qué es:** Skill para diseñar logotipos con un agente, desde la idea y las referencias hasta SVG y comprobaciones de diseño.
**Stack:** HTML
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/kaankiziltug/logo-design-skill

**Instalación** [?]: `Seguir la instalación original: https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para diseñar logotipos con un agente, desde la idea y las referencias hasta SVG y comprobaciones de diseño.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `marketingskills`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,analytics,email,search

**Qué es:** Skills de Corey Haines para marketers técnicos y founders que trabajan con agentes de código: conversión, copywriting, SEO y SEO para IA, anuncios, emails, analítica y atribución, pricing, lanzamientos, retención y ventas. La skill product-marketing guarda el contexto de tu producto y las demás la consultan antes de actuar.
**Stack:** Markdown, SKILL.md, JavaScript (scripts del repo)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/coreyhaines31/marketingskills

**Instalación** [+]: `npx skills add coreyhaines31/marketingskills`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** eres founder o marketer técnico y quieres que tu agente de código haga trabajo de growth con marcos probados
**Evita si:** necesitas una herramienta que envíe campañas o mida resultados; mira `mautic`, `listmonk` o `posthog`
**Combina con:** `agency-agents`, `geo-seo-claude`, `mautic`, `posthog`

## `minimalist-entrepreneur-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,reference

**Qué es:** Skills basadas en ideas de The Minimalist Entrepreneur para orientar trabajo de negocio y emprendimiento con un agente.
**Stack:** —
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/slavingia/skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/slavingia/skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills basadas en ideas de The Minimalist Entrepreneur para orientar trabajo de negocio y emprendimiento con un agente.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `modern-web-guidance`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,reference

**Qué es:** Herramienta y skill para que un agente consulte documentación actual sobre prácticas y APIs de desarrollo web.
**Stack:** package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/GoogleChrome/modern-web-guidance

**Instalación** [?]: `Seguir la instalación original: https://github.com/GoogleChrome/modern-web-guidance/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Herramienta y skill para que un agente consulte documentación actual sobre prácticas y APIs de desarrollo web.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `motion-design-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,reference

**Qué es:** Skill con principios de ritmo, transiciones y composición del movimiento para diseñar animaciones de interfaces.
**Stack:** —
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/LottieFiles/motion-design-skill

**Instalación** [?]: `Seguir la instalación original: https://github.com/LottieFiles/motion-design-skill/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill con principios de ritmo, transiciones y composición del movimiento para diseñar animaciones de interfaces.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `no-ai-slop`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=escritura,skill,python

**Qué es:** Skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con IA.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/petergyang/no-ai-slop

**Instalación** [?]: `Seguir la instalación original: https://github.com/petergyang/no-ai-slop/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con IA.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `scientific-agent-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas de dominio.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/K-Dense-AI/scientific-agent-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas de dominio.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `skills-emil`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design

**Qué es:** Resuelve el handoff diseño↔código, no solo la estética final.
**Stack:** Markdown (skills), TypeScript/React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/emilkowalski/skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/emilkowalski/skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas diseño+dev en equipo y sufres el handoff
**Evita si:** buscas componentes listos o trabajas solo
**Combina con:** `ui-ux-pro-max-skill`

## `social-media-research-skills`
role=skill · exec=cloud · setup=medium · mcp=False · prov=— · tags=dominio,agent-skills,ai-agents,claude-code,claude-skills,competitor-analysis,content-marketing,cursor · tools=claude-code,codex

**Qué es:** Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators. Guía al agente por flujos de investigación que consultan datos sociales y producen informes de negocio.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La clave exigida es de un servicio externo. No es una API de un modelo de lenguaje; el agente o aplicación que use sus datos tiene su propio acceso a IA.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo de APIs o servicios. El modelo lo aporta tu agente; las consultas de datos requieren acceso a ScrapeCreators por separado.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ScrapeCreators/social-media-research-skills

**Instalación** [+]: `npx skills add ScrapeCreators/social-media-research-skills`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres investigación de contenido social desde un agente compatible con Agent Skills
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones
**Alternativas (elige una):** `last30days-skill`

## `stitch-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design,ui

**Qué es:** Skills en el estándar abierto Agent Skills que enseñan a Claude Code, Codex o Gemini CLI a diseñar con Stitch.
**Stack:** TypeScript, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/google-labs-code/stitch-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/google-labs-code/stitch-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** usas Stitch con un agente de código
**Evita si:** no usas Stitch
**Combina con:** `stitch-sdk`, `gemini-cli`

## `stop-slop`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,prompts,docs

**Qué es:** Un SKILL.md con tres archivos de referencia (frases a eliminar, estructuras a evitar y ejemplos antes/después) que enseña a Claude o a cualquier LLM a quitar muletillas, contrastes binarios, fragmentos dramáticos, voz pasiva y otros patrones predecibles. Cierra con una rúbrica de cinco dimensiones para decidir si el texto necesita otra vuelta.
**Stack:** Markdown, SKILL.md
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/hardikpandya/stop-slop

**Instalación** [?]: `Seguir la instalación original: https://github.com/hardikpandya/stop-slop/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt
**Evita si:** prefieres una skill que reescriba mostrando su proceso y pueda imitar tu voz; mira `humanizer`
**Combina con:** `marketingskills`, `claude-code`
**Alternativas (elige una):** `humanizer`

## `taste-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design,javascript

**Qué es:** Ataca el acabado "de plantilla" que delata a las UIs generadas por IA.
**Stack:** Markdown/skills
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Leonxlnx/taste-skill

**Instalación** [+]: `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres frontends con gusto y no te basta con UI funcional
**Evita si:** ya tienes un design system cerrado o no usas generadores de imagen
**Combina con:** `ui-ux-pro-max-skill`, `impeccable`

## `threejs-game-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,python

**Qué es:** Skills para que un agente construya juegos de navegador con Three.js, interfaz y recursos visuales o sonoros opcionales.
**Stack:** Python, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función. La generación externa de imágenes, clips, música o voces es una configuración distinta: el plan del agente no incluye automáticamente esas generaciones.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/majidmanzarpour/threejs-game-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/majidmanzarpour/threejs-game-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skills para que un agente construya juegos de navegador con Three.js, interfaz y recursos visuales o sonoros opcionales.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `threejs-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,reference

**Qué es:** Colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js.
**Stack:** —
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/CloudAI-X/threejs-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/CloudAI-X/threejs-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible
**Alternativas (elige una):** `3dviz-pro-max`

## `ui-ux-pro-max-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design,python

**Qué es:** Resuelve el punto débil habitual del código asistido por IA: la jerarquía visual y el acabado.
**Stack:** Node.js (uipro-cli), TypeScript/React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

**Instalación** [?]: `Seguir la instalación original: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** generas UI con IA y el resultado se ve genérico o despulido
**Evita si:** no trabajas frontend o ya tienes un sistema de diseño impuesto
**Combina con:** `taste-skill`, `impeccable`, `tailwindcss`
