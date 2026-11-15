# 30. Video con código y agentes creativos — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `brag`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,python

**Qué es:** Skills para que un agente convierta un proyecto o sitio en un video breve de lanzamiento con composición y música.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/latent-spaces/brag

**Instalación** [+]: `npx skills add https://github.com/latent-spaces/brag --skill brag-slim`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Skills para que un agente convierta un proyecto o sitio en un video breve de lanzamiento con composición y música.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `claude-animated-shorts`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,typescript

**Qué es:** Skill de Claude para crear cortos animados por código combinando personajes y escenas con Three.js y Remotion.
**Stack:** TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/mromidev/claude-animated-shorts

**Instalación** [?]: `Seguir la instalación original: https://github.com/mromidev/claude-animated-shorts/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill de Claude para crear cortos animados por código combinando personajes y escenas con Three.js y Remotion.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `huashu-motion`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,javascript

**Qué es:** Skill para crear videos de presentación de productos con un agente de código, composición, música y revisión visual.
**Stack:** JavaScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función. La generación externa de imágenes, clips, música o voces es una configuración distinta: el plan del agente no incluye automáticamente esas generaciones.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/alchaincyf/huashu-motion

**Instalación** [?]: `Seguir la instalación original: https://github.com/alchaincyf/huashu-motion/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para crear videos de presentación de productos con un agente de código, composición, música y revisión visual.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `hyperframes`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=video,agents,skills,typescript

**Qué es:** HyperFrames define cada video como un archivo HTML con atributos de tiempo y pistas, animado con GSAP, CSS, Lottie, Three.js u otras librerías, y lo renderiza a MP4. Incluye CLI para crear, previsualizar y renderizar, un catálogo de unos 450 bloques (transiciones, subtítulos, gráficos, mapas) y skills para que Claude Code, Codex o Cursor produzcan videos a partir de una petición.
**Stack:** TypeScript, Node.js, Puppeteer, FFmpeg, GSAP
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/heygen-com/hyperframes

**Instalación** [+]: `npx hyperframes init my-video`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva
**Evita si:** tu equipo ya trabaja con componentes React y el ecosistema de `remotion`, o prefieres editar en una línea de tiempo visual
**Combina con:** `claude-code`, `gsap`, `kokoro`, `whisperx`
**Alternativas (elige una):** `remotion`, `moviepy`

## `lemo-opuscar`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,javascript

**Qué es:** Colección de estilos e instrucciones para crear piezas audiovisuales por código con Claude Code.
**Stack:** JavaScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/lemomo-ai/lemo-opuscar

**Instalación** [?]: `Seguir la instalación original: https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Colección de estilos e instrucciones para crear piezas audiovisuales por código con Claude Code.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `manim`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=video,dataviz,learning,python

**Qué es:** Manim permite describir en código Python escenas con fórmulas LaTeX, gráficas, geometría y transformaciones animadas, y exportarlas a video. Este repo es ManimGL, la versión original que Grant Sanderson usa en 3Blue1Brown; la edición comunitaria (ManimCommunity/manim) es un fork más estable y mejor documentado.
**Stack:** Python, OpenGL, FFmpeg, LaTeX
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/3b1b/manim

**Instalación** [+]: `pip install manimgl`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres animaciones matemáticas o técnicas precisas definidas en código Python
**Evita si:** buscas estabilidad y documentación para empezar (usa la edición comunitaria ManimCommunity/manim) o motion graphics de marketing; mira `remotion` o `hyperframes`
**Combina con:** `kokoro`, `moviepy`, `ffmpeg`
**Alternativas (elige una):** `manim-community`

## `manim-community`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,animations,hacktoberfest,manim,math,python

**Qué es:** Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. Define objetos geométricos y transformaciones en código y renderiza la escena como video.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ManimCommunity/manim

**Instalación** [?]: `Seguir la instalación original: https://github.com/ManimCommunity/manim/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas animaciones matemáticas precisas y reproducibles
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa
**Combina con:** `ffmpeg`
**Alternativas (elige una):** `manim`

## `motionmaxxing`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,javascript

**Qué es:** Skill para mejorar composición, ritmo y movimiento de videos creados con agentes y herramientas de código.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Tejashmakwana/motionmaxxing

**Instalación** [?]: `Seguir la instalación original: https://github.com/Tejashmakwana/motionmaxxing/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para mejorar composición, ritmo y movimiento de videos creados con agentes y herramientas de código.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `openfilm`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,typescript

**Qué es:** Herramientas y skill para que un agente cree proyectos de video y permita editar después sus elementos.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/openfilm/openfilm

**Instalación** [+]: `npx skills add openfilm/openfilm`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Herramientas y skill para que un agente cree proyectos de video y permita editar después sus elementos.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `openmontage`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=video,coding-agent,skills

**Qué es:** Describes el video y el agente investiga, escribe el guion, genera recursos y monta el resultado.
**Stack:** Markdown, Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/OpenMontageInc/OpenMontage

**Instalación** [?]: `Seguir la instalación original: https://github.com/OpenMontageInc/OpenMontage/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres producir videos completos con un agente
**Evita si:** solo necesitas editar clips; mira `video-use`
**Combina con:** `remotion`
**Alternativas (elige una):** `remotion-superpowers`, `moneyprinterturbo`

## `papermorph`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,javascript

**Qué es:** Skill que convierte libros en experiencias web animadas y narradas, con distintas rutas de voz y recursos visuales.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función. La generación externa de imágenes, clips, música o voces es una configuración distinta: el plan del agente no incluye automáticamente esas generaciones.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/DozenTwelve/Papermorph

**Instalación** [+]: `npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Skill que convierte libros en experiencias web animadas y narradas, con distintas rutas de voz y recursos visuales.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `rea-video`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=— · tags=programatico,agent-skills,ai-video,aigc-detection,claude-code,codex,ffmpeg,prompt-engineering

**Qué es:** Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO.md. Clasifica planos y registra capas, ritmo y técnicas de producción en un formato legible por agentes.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/JuneYaooo/rea-video

**Instalación** [?]: `Seguir la instalación original: https://github.com/JuneYaooo/rea-video/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar o recrear la estructura de un video de referencia
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa
**Combina con:** `remotion`

## `remotion`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=video,typescript

**Qué es:** Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. El render no requiere por sí solo una API de IA; revisa las condiciones de licencia del proyecto.
**Stack:** Node.js, React, Chromium, ffmpeg
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. El renderizado de React no requiere una API de IA. Revisar la licencia de Remotion para el tamaño del equipo y el uso comercial.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/remotion-dev/remotion

**Instalación** [+]: `npx create-video@latest`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** generas video a escala con React y quieres variantes parametrizadas
**Evita si:** trabajas en Python (moviepy) o buscas un editor visual
**Combina con:** `open-generative-ai`
**Alternativas (elige una):** `moviepy`, `hyperframes`

## `remotion-superpowers`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=video,skills,coding-agent

**Qué es:** Añade locución con IA, música, footage de stock e imágenes para producir videos en código.
**Stack:** Shell, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/DojoCodingLabs/remotion-superpowers

**Instalación** [?]: `Seguir la instalación original: https://github.com/DojoCodingLabs/remotion-superpowers/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** usas Remotion con un agente y quieres producción completa
**Evita si:** no usas Remotion
**Combina con:** `remotion`, `skills-remotion`
**Alternativas (elige una):** `openmontage`, `video-use`

## `skills-remotion`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=video,skills

**Qué es:** Enseñan al agente las buenas prácticas de Remotion: composiciones, animaciones, audio y render.
**Stack:** TypeScript, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/remotion-dev/skills

**Instalación** [+]: `npx skills add remotion-dev/skills`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** haces videos con Remotion y un agente
**Evita si:** no usas Remotion
**Combina con:** `remotion`, `remotion-superpowers`

## `srt-whiteboard-animation`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,python

**Qué es:** Skill para crear animaciones de pizarra con trazos y contenido organizados a partir de archivos de subtítulos SRT.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Integración no documentada
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/geeklee/srt-whiteboard-animation

**Instalación** [?]: `Seguir la instalación original: https://github.com/geeklee/srt-whiteboard-animation/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para crear animaciones de pizarra con trazos y contenido organizados a partir de archivos de subtítulos SRT.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `video-shotcraft`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,typescript

**Qué es:** Skill para crear videos de producto editables con Remotion, composición de planos, movimiento y trabajo de sonido.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Vincentwei1021/video-shotcraft

**Instalación** [?]: `Seguir la instalación original: https://github.com/Vincentwei1021/video-shotcraft/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Skill para crear videos de producto editables con Remotion, composición de planos, movimiento y trabajo de sonido.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `video-use`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=video,coding-agent,skills,python

**Qué es:** El agente corta, une, subtitula y ajusta videos a partir de instrucciones en lenguaje natural.
**Stack:** Python, ffmpeg
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/browser-use/video-use

**Instalación** [?]: `Seguir la instalación original: https://github.com/browser-use/video-use/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres editar videos pidiéndoselo a tu agente
**Evita si:** quieres una app de edición visual; mira `opencut`
**Combina con:** `ffmpeg`, `claude-code`
**Alternativas (elige una):** `remotion-superpowers`

## `videofy-minimal`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,typescript

**Qué es:** Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión. La ruta documentada requiere APIs de OpenAI y ElevenLabs aunque la interfaz y el montaje se ejecuten en tu equipo.
**Stack:** Python/Node
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo de APIs o servicios. El flujo documentado usa OPENAI_API_KEY y ELEVENLABS_API_KEY. La interfaz local no elimina esas llamadas remotas.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/schibsted/videofy_minimal

**Instalación** [?]: `Seguir la instalación original: https://github.com/schibsted/videofy_minimal/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres reels simples ya, sin montar un pipeline entero
**Evita si:** necesitas variantes programáticas a escala (remotion) o control fino por código (moviepy)
**Combina con:** `whisper`, `supertonic`
**Alternativas (elige una):** `moneyprinterturbo`
