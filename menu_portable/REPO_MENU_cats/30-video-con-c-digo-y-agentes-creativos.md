# 30. Video con código y agentes creativos — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `brag`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,python

**Qué es:** Skills para que un agente convierta un proyecto o sitio en un video breve de lanzamiento con composición y música.
**Stack:** Agente; runtime y FFmpeg según variante; sitio propio de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. La skill usa el agente y render propio; el servicio letsbrag.app es una ruta separada y sin suscripción no implica precio cero
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Brag-slim y el flujo clásico tienen dependencias distintas; documenta plugins Claude Code y Codex y no garantiza resultados iguales con todos los modelos
- Coste: El coste depende del proveedor o la ruta. La skill usa el agente y render propio; el servicio letsbrag.app es una ruta separada y sin suscripción no implica precio cero
- Equipo: Preparación según la ruta elegida. Agente; runtime y FFmpeg según variante; sitio propio de prueba
**Repo:** https://github.com/latent-spaces/brag

**Instalación** [+]:

```
npx skills add https://github.com/latent-spaces/brag --skill brag-slim
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Presentar una demo de producto; Preparar una pieza de lanzamiento
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un video corto de una función real del sitio y contrasta lo mostrado con su comportamiento
**Qué comprobar:** Puedes revisar guion, capturas, música y duración
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `hyperframes`, `claude-code`, `gsap`

## `claude-animated-shorts`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,typescript

**Qué es:** Skill de Claude para crear cortos animados por código combinando personajes y escenas con Three.js y Remotion.
**Stack:** Claude Code; Three.js y Remotion; dependencias de render; historia propia
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La skill usa el agente y recursos de render; Remotion y assets mantienen condiciones propias
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Código y documentos MIT; los frames de referencia son solo para estudio de estilo y no se entregan como assets comerciales reutilizables; viral no es garantía
- Coste: Consumo del agente que ya utilizas. La skill usa el agente y recursos de render; Remotion y assets mantienen condiciones propias
- Equipo: Preparación según la ruta elegida. Claude Code; Three.js y Remotion; dependencias de render; historia propia
**Repo:** https://github.com/mromidev/claude-animated-shorts

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/mromidev/claude-animated-shorts/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un corto animado de prueba; Estudiar personajes 2D en escena 3D
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prepara un plano de pocos segundos y revisa personajes, cámara y tiempos antes de un corto completo
**Qué comprobar:** Puedes reproducir la escena y contrastarla con el guion
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `remotion`, `three.js`, `claude-code`

## `huashu-motion`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,javascript

**Qué es:** Skill para crear videos de presentación de productos con un agente de código, composición, música y revisión visual.
**Stack:** Agente compatible; dependencias del runtime; brief y recursos propios
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el plan o proveedor del agente y cómputo de render; los precios de ejemplos históricos no son una tarifa actual garantizada
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Documenta Claude Code y Codex; comercial-grade es una descripción del autor y la licencia GSAP y fuentes siguen aplicándose
- Coste: Consumo del agente que ya utilizas. Usa el plan o proveedor del agente y cómputo de render; los precios de ejemplos históricos no son una tarifa actual garantizada
- Equipo: Preparación según la ruta elegida. Agente compatible; dependencias del runtime; brief y recursos propios
**Repo:** https://github.com/alchaincyf/huashu-motion

**Instalación** [+]:

```
npx skills add alchaincyf/huashu-motion
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una presentación de producto; Explorar estilos de motion graphics
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera una escena corta y revisa ritmo, títulos y sincronía antes de extender la pieza
**Qué comprobar:** Puedes identificar decisiones de composición y duración
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gsap`, `kokoro`, `claude-code`

## `hyperframes`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=video,agents,skills,typescript

**Qué es:** Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes.
**Stack:** Node 22+; FFmpeg; composición pequeña; agente opcional
**Acceso y costes:**
- API de IA: API de IA opcional. El render local Apache no cobra por render; el agente y generaciones o planes Pro usan recursos separados
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Los skills deben coincidir con la versión del CLI; el núcleo basta para empezar y no es necesario instalar todo el catálogo de extensiones
- Coste: El coste depende del proveedor o la ruta. El render local Apache no cobra por render; el agente y generaciones o planes Pro usan recursos separados
- Equipo: Preparación según la ruta elegida. Node 22+; FFmpeg; composición pequeña; agente opcional
**Repo:** https://github.com/heygen-com/hyperframes

**Instalación** [+]:

```
npx hyperframes init my-video
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un video explicativo por código; Crear una pieza de presentación con HTML
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un proyecto con un título de pocos segundos, previsualiza y renderiza un MP4
**Qué comprobar:** Puedes comprobar duración, primer y último frame y archivo exportado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `gsap`, `kokoro`, `whisperx`
**Alternativas (elige una):** `remotion`, `moviepy`

## `hypit`
role=skill · exec=local · setup=medium · mcp=False · prov=local · tags=generativo,skill,typescript

**Qué es:** Skills para agentes que organizan generación y edición de videos mediante modelos, servicios y recursos configurables.
**Stack:** Agente compatible; modelo o proveedor configurado; video propio de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. La skill no añade cuota por asiento según el autor; los servicios de modelos sí cobran; admite APIs o modelos locales según tarea
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. Las promesas de viralidad no son resultados medidos para tu contenido; revisa permisos de imágenes, voces y clips utilizados
- Coste: El coste depende del proveedor o la ruta. La skill no añade cuota por asiento según el autor; los servicios de modelos sí cobran; admite APIs o modelos locales según tarea
- Equipo: Preparación según la ruta elegida. Agente compatible; modelo o proveedor configurado; video propio de prueba
**Repo:** https://github.com/hypit-ai/hypit

**Instalación** [+]:

```
npx skills add hypit-ai/hypit -g
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear versiones de un video propio; Coordinar subtítulos y B-roll de un tutorial
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Parte de un clip propio, cambia un rótulo y una toma y revisa el workflow antes de renderizar
**Qué comprobar:** Puedes identificar los recursos y reproducir una variante del flujo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ffmpeg`, `comfyui`

## `lemo-opuscar`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,javascript

**Qué es:** Biblioteca de estilos para video por código orientada a Claude,con licencias diferentes para código,guías y medios.
**Stack:** Claude Code; dependencias del estilo; material propio; Kokoro según voz
**Acceso y costes:**
- API de IA: API de IA opcional. Código MIT; prompts y guías actuales CC BY-NC con permiso adicional acotado para crear films; otros usos comerciales pueden requerir licencia
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Compatibilidad por confirmar
- Antigravity: Depende del recurso o la configuración
- Modelos locales: Modelos locales documentados. El autor lo orienta a Claude y advierte diferencias con otros modelos; demos, guías, voz y assets no comparten una licencia única; Kokoro local no sustituye el agente
- Coste: El coste depende del proveedor o la ruta. Código MIT; prompts y guías actuales CC BY-NC con permiso adicional acotado para crear films; otros usos comerciales pueden requerir licencia
- Equipo: Preparación según la ruta elegida. Claude Code; dependencias del estilo; material propio; Kokoro según voz
**Repo:** https://github.com/lemomo-ai/lemo-opuscar

**Instalación** [+]:

```
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar una dirección visual para un video; Preparar una pieza por código
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige un estilo y crea una escena de prueba revisando créditos antes de adaptar el resto
**Qué comprobar:** Puedes identificar código, estilo y assets de la salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ffmpeg`, `three.js`

## `manim`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=video,dataviz,learning,python

**Qué es:** Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL.
**Stack:** Python; FFmpeg; OpenGL; LaTeX si escribes fórmulas; escena pequeña
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Código MIT sin API de IA; cómputo y recursos externos aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Este es ManimGL de 3Blue1Brown y usa manimgl; no mezcles sus imports o comandos con Manim Community
- Coste: Sin pago a un modelo en la ruta básica. Código MIT sin API de IA; cómputo y recursos externos aparte
- Equipo: Preparación según la ruta elegida. Python; FFmpeg; OpenGL; LaTeX si escribes fórmulas; escena pequeña
**Repo:** https://github.com/3b1b/manim

**Instalación** [+]:

```
# Install manimgl
pip install manimgl

# Try it out
manimgl
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar una transformación matemática; Preparar una animación geométrica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta una escena de ejemplo y cambia una forma o texto
**Qué comprobar:** Puedes abrir la animación y localizar su código
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `kokoro`, `moviepy`
**Alternativas (elige una):** `manim-community`

## `manim-community`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,animations,hacktoberfest,manim,math,python

**Qué es:** Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas.
**Stack:** Python; dependencias de la versión; LaTeX según escena; equipo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Código MIT sin API de IA; render y recursos independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Manim Community usa from manim y su propio CLI; es una línea distinta de ManimGL y sus tutoriales no son intercambiables sin adaptar
- Coste: Sin pago a un modelo en la ruta básica. Código MIT sin API de IA; render y recursos independientes
- Equipo: Preparación según la ruta elegida. Python; dependencias de la versión; LaTeX según escena; equipo
**Repo:** https://github.com/ManimCommunity/manim

**Instalación** [?]:

```
Seguir la instalación original: https://docs.manim.community/en/stable/installation.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una explicación matemática; Crear una animación de geometría
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue SquareToCircle y modifica una propiedad para observar la transformación
**Qué comprobar:** Puedes renderizar y relacionar el resultado con la escena Python
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `kokoro`, `srt-whiteboard-animation`
**Alternativas (elige una):** `manim`

## `mediabunny`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=edicion,library,typescript

**Qué es:** Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones web.
**Stack:** JavaScript ES2021+; navegador moderno; TypeScript >=5.7 para tipos; medio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca MPL-2.0 no exige IA; codecs y capacidades del navegador pueden limitar la ruta
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una biblioteca de medios, no una app de edición completa; comprueba soporte de codecs y destino en los navegadores de tus usuarios
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca MPL-2.0 no exige IA; codecs y capacidades del navegador pueden limitar la ruta
- Equipo: Preparación según la ruta elegida. JavaScript ES2021+; navegador moderno; TypeScript >=5.7 para tipos; medio de prueba
**Repo:** https://github.com/Vanilagy/mediabunny

**Instalación** [+]:

```
npm install mediabunny
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Procesar video dentro de una aplicación web; Construir una herramienta de conversión en navegador
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee duración y pistas de un archivo y convierte una copia a un formato admitido
**Qué comprobar:** Puedes contrastar metadatos y reproducir la salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `remotion`, `ffmpeg`, `openfilm`

## `motionmaxxing`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,javascript

**Qué es:** Skill para mejorar composición, ritmo y movimiento de videos creados con agentes y herramientas de código.
**Stack:** Node 22+; Python 3; FFmpeg; Chrome; agente con shell
**Acceso y costes:**
- API de IA: API de IA opcional. Voz, música y SFX ElevenLabs son opcionales; Codex puede generar imágenes con su cuenta y cuotas; el núcleo usa render propio y agente
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. El skill admite hosts que leen SKILL.md pero las funciones dependen de herramientas disponibles; no garantiza una valoración profesional por sus puntuaciones
- Coste: El coste depende del proveedor o la ruta. Voz, música y SFX ElevenLabs son opcionales; Codex puede generar imágenes con su cuenta y cuotas; el núcleo usa render propio y agente
- Equipo: Preparación según la ruta elegida. Node 22+; Python 3; FFmpeg; Chrome; agente con shell
**Repo:** https://github.com/Tejashmakwana/motionmaxxing

**Instalación** [+]:

```
git clone https://github.com/Tejashmakwana/motionmaxxing ~/.claude/skills/motionmaxxing
bash ~/.claude/skills/motionmaxxing/install.sh        # checks the requirements; installs nothing system-wide
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Mejorar una pieza de lanzamiento; Preparar una animación tipográfica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Revisa providers.sh y crea una escena tipográfica breve antes de añadir voces o imágenes
**Qué comprobar:** Puedes comparar composición y tiempos de dos versiones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gsap`, `hyperframes`, `claude-code`

## `moviepy`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=video,audio,automation,python

**Qué es:** Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos.
**Stack:** Python; FFmpeg según instalación; fuente tipográfica para títulos; video de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El montaje no requiere modelo; renderizar consume CPU, memoria y disco; medios y fuentes tienen licencias propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. v2 cambia APIs como subclipped y with_volume_scaled; los ejemplos v1 no son intercambiables
- Coste: Sin pago a un modelo en la ruta básica. El montaje no requiere modelo; renderizar consume CPU, memoria y disco; medios y fuentes tienen licencias propias
- Equipo: Preparación según la ruta elegida. Python; FFmpeg según instalación; fuente tipográfica para títulos; video de prueba
**Repo:** https://github.com/Zulko/moviepy

**Instalación** [?]:

```
Seguir la instalación original: https://zulko.github.io/moviepy/getting_started/install.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar variantes de un video; Componer clips y rótulos desde Python
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Recorta diez segundos y superpone un título usando el ejemplo v2
**Qué comprobar:** El render conserva duración y audio y muestra el título
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `whisperx`, `kokoro`, `ffmpeg`
**Alternativas (elige una):** `remotion`, `hyperframes`

## `openfilm`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,typescript

**Qué es:** Herramientas y skill para que un agente cree proyectos de video y permita editar después sus elementos.
**Stack:** Node 22.2+; FFmpeg; Git para versiones; agente; recursos propios
**Acceso y costes:**
- API de IA: API de IA opcional. Formato, CLI y Studio MIT; el agente y servicios de generación opcionales tienen costes propios
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. El video se describe como páginas web y puede editarse; instalar la skill y abrir Studio son pasos distintos y el nombre y logo conservan reglas de marca
- Coste: El coste depende del proveedor o la ruta. Formato, CLI y Studio MIT; el agente y servicios de generación opcionales tienen costes propios
- Equipo: Preparación según la ruta elegida. Node 22.2+; FFmpeg; Git para versiones; agente; recursos propios
**Repo:** https://github.com/openfilm/openfilm

**Instalación** [+]:

```
npx skills add openfilm/openfilm
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un video editable; Revisar el resultado de un agente en un editor
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un ejemplo y modifica un título en Studio antes de exportar un clip corto
**Qué comprobar:** Puedes inspeccionar el proyecto editable y el MP4
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `gsap`, `three.js`

## `openmontage`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=video,coding-agent,skills

**Qué es:** Pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcionales.
**Stack:** Python; Node; FFmpeg; dependencias de la ruta; material autorizado
**Acceso y costes:**
- API de IA: API de IA opcional. API keys opcionales amplían proveedores; el agente, render, Remotion y recursos tienen condiciones propias
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. Documenta asistentes con archivos y ejecución de código; Piper permite voz offline, pero no implica que el modelo del agente o todos los pipelines sean locales
- Coste: El coste depende del proveedor o la ruta. API keys opcionales amplían proveedores; el agente, render, Remotion y recursos tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Python; Node; FFmpeg; dependencias de la ruta; material autorizado
**Repo:** https://github.com/OpenMontageInc/OpenMontage

**Instalación** [+]:

```
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un video con recursos locales; Comparar un pipeline con servicios opcionales
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Empieza con material propio y narración Piper y comprueba guion, timeline y exportación
**Qué comprobar:** Puedes revisar la procedencia de cada asset y abrir el MP4
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `remotion`, `ffmpeg`, `kokoro`
**Alternativas (elige una):** `remotion-superpowers`, `moneyprinterturbo`

## `papermorph`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,javascript

**Qué es:** Skill que convierte libros en experiencias web animadas y narradas, con distintas rutas de voz y recursos visuales.
**Stack:** uv; FFmpeg; navegadores Playwright; libro propio o autorizado; voz local o remota
**Acceso y costes:**
- API de IA: API de IA opcional. Kokoro ofrece voz local y Edge TTS voz online; generación de imágenes, clips o voces opcionales puede cobrar aparte
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: Modelos locales documentados. Documenta Claude Code y OpenCode; sus ejemplos de coste son de producciones concretas y los recursos del sitio conservan licencias separadas del código
- Coste: El coste depende del proveedor o la ruta. Kokoro ofrece voz local y Edge TTS voz online; generación de imágenes, clips o voces opcionales puede cobrar aparte
- Equipo: Preparación según la ruta elegida. uv; FFmpeg; navegadores Playwright; libro propio o autorizado; voz local o remota
**Repo:** https://github.com/DozenTwelve/Papermorph

**Instalación** [+]:

```
npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code   # or --agent opencode
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una lección animada; Explorar una historia interactiva
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Transforma una página breve autorizada en una lección y comprueba texto, narración y controles
**Qué comprobar:** Puedes contrastar el contenido con la página original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `opencode`, `kokoro`

## `rea-video`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=— · tags=programatico,agent-skills,ai-video,aigc-detection,claude-code,codex,ffmpeg,prompt-engineering

**Qué es:** Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO.md.
**Stack:** Python >=3.10; FFmpeg; video autorizado; modelo con visión solo si eliges revisión AI
**Acceso y costes:**
- API de IA: API de IA opcional. Tools-only funciona offline; análisis con modelo o generación adicional cobra según proveedor y el agente usa su plan
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. Las clasificaciones de material AI o filmado son estimaciones, no pruebas forenses; recrea técnicas con recursos de los que tengas derechos
- Coste: El coste depende del proveedor o la ruta. Tools-only funciona offline; análisis con modelo o generación adicional cobra según proveedor y el agente usa su plan
- Equipo: Preparación según la ruta elegida. Python >=3.10; FFmpeg; video autorizado; modelo con visión solo si eliges revisión AI
**Repo:** https://github.com/JuneYaooo/rea-video

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/JuneYaooo/rea-video/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar ritmo de una pieza; Preparar un plan de recreación con material propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Analiza un clip corto y contrasta los planos del VIDEO.md con el original
**Qué comprobar:** Puedes revisar tiempos, estructura e hipótesis de técnica
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `remotion`, `ffmpeg`, `claude-code`

## `remotion`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=video,typescript

**Qué es:** Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos.
**Stack:** Node; proyecto React; recursos propios; licencia según uso; agente opcional
**Acceso y costes:**
- API de IA: API de IA opcional. No requiere API de IA para renderizar; usa una licencia especial que exige licencia de empresa en ciertos casos y servicios externos aparte
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. La ruta con agentes utiliza las skills oficiales del proyecto compañero; no todo uso comercial es gratuito por estar disponible el código
- Coste: El coste depende del proveedor o la ruta. No requiere API de IA para renderizar; usa una licencia especial que exige licencia de empresa en ciertos casos y servicios externos aparte
- Equipo: Preparación según la ruta elegida. Node; proyecto React; recursos propios; licencia según uso; agente opcional
**Repo:** https://github.com/remotion-dev/remotion

**Instalación** [+]:

```
npx create-video@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una plantilla de video con datos; Preparar títulos animados
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una composición de prueba y comprueba que la cantidad de frames corresponde a su duración
**Qué comprobar:** Puedes reproducir y exportar un clip con inicio y fin definidos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `skills-remotion`, `remotion-superpowers`, `gsap`
**Alternativas (elige una):** `moviepy`, `hyperframes`

## `remotion-superpowers`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=video,skills,coding-agent

**Qué es:** Orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por etapa.
**Stack:** Node 22.18+; Remotion; skills oficiales; claves de medios; uv para MCP opcional
**Acceso y costes:**
- API de IA: API de IA necesaria. ElevenLabs, KIE y TwelveLabs aparecen como claves necesarias del flujo; modelos, Remotion y agente tienen condiciones distintas
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. Las captions pueden usar Whisper local pero el conjunto no es enteramente local; hooks y subagentes son extras de Claude Code y no se heredan en todos los hosts
- Coste: Consumo de APIs o servicios. ElevenLabs, KIE y TwelveLabs aparecen como claves necesarias del flujo; modelos, Remotion y agente tienen condiciones distintas
- Equipo: Preparación según la ruta elegida. Node 22.18+; Remotion; skills oficiales; claves de medios; uv para MCP opcional
**Repo:** https://github.com/DojoCodingLabs/remotion-superpowers

**Instalación** [+]:

```
codex plugin marketplace add DojoCodingLabs/remotion-superpowers
codex plugin add remotion-superpowers@remotion-superpowers
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un video narrado; Combinar clips y subtítulos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta setup y prepara un guion corto con estimación de servicios antes de generar
**Qué comprobar:** Puedes identificar claves, proveedores y resultado de cada etapa
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `remotion`, `skills-remotion`, `claude-code`
**Alternativas (elige una):** `openmontage`, `video-use`

## `skills-remotion`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=video,skills

**Qué es:** Skills oficiales de Remotion para que tu agente de código cree videos con React.
**Stack:** Agente compatible; proyecto Remotion; Node; recursos propios
**Acceso y costes:**
- API de IA: API de IA opcional. Las skills usan el agente; Remotion tiene licencia propia y servicios de voz o imagen se pagan aparte
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Son instrucciones oficiales para hosts Agent Skills; no incluyen la licencia de Remotion ni créditos de medios
- Coste: El coste depende del proveedor o la ruta. Las skills usan el agente; Remotion tiene licencia propia y servicios de voz o imagen se pagan aparte
- Equipo: Preparación según la ruta elegida. Agente compatible; proyecto Remotion; Node; recursos propios
**Repo:** https://github.com/remotion-dev/skills

**Instalación** [+]:

```
npx skills add remotion-dev/skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender Remotion con un agente; Preparar una plantilla de video
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide una composición corta y comprueba frames y duración antes de añadir voz o servicios
**Qué comprobar:** Puedes revisar la composición React y su render
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `remotion`, `claude-code`, `remotion-superpowers`

## `srt-whiteboard-animation`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,python

**Qué es:** Skill para crear animaciones de pizarra con trazos y contenido organizados a partir de archivos de subtítulos SRT.
**Stack:** Agente con skill; Python y renderizadores del proyecto; SRT y recursos autorizados
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El render básico usa recursos propios y el agente; modelos o medios añadidos tienen condiciones independientes
- Claude Code: Depende del recurso o la configuración
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Incluye metadatos Codex; no se confirma una instalación específica equivalente de otros hosts y el SRT no aporta automáticamente una narración
- Coste: Consumo del agente que ya utilizas. El render básico usa recursos propios y el agente; modelos o medios añadidos tienen condiciones independientes
- Equipo: Preparación según la ruta elegida. Agente con skill; Python y renderizadores del proyecto; SRT y recursos autorizados
**Repo:** https://github.com/geeklee/srt-whiteboard-animation

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/geeklee/srt-whiteboard-animation/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una explicación de pizarra; Prototipar una secuencia narrada
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa tres líneas de subtítulos y revisa el orden de trazos y la sincronización con cada frase
**Qué comprobar:** Puedes comparar tiempos del SRT y salida MP4
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `whisperx`, `kokoro`, `manim-community`

## `video-shotcraft`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,skill,typescript

**Qué es:** Skill para crear videos de producto editables con Remotion, composición de planos, movimiento y trabajo de sonido.
**Stack:** Agente; Node y Remotion; herramientas de captura; recursos autorizados
**Acceso y costes:**
- API de IA: API de IA opcional. Usa el agente y render; fuentes de sonido, generación y licencia Remotion se revisan por separado
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Documenta Claude Code y Codex; los servicios de publicación son opcionales y no se deben activar al preparar un borrador
- Coste: El coste depende del proveedor o la ruta. Usa el agente y render; fuentes de sonido, generación y licencia Remotion se revisan por separado
- Equipo: Preparación según la ruta elegida. Agente; Node y Remotion; herramientas de captura; recursos autorizados
**Repo:** https://github.com/Vincentwei1021/video-shotcraft

**Instalación** [+]:

```
npx skills add Vincentwei1021/video-shotcraft
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una promo de producto; Organizar planos sincronizados con sonido
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Captura una pantalla propia y crea un plano corto verificando legibilidad, tiempo y audio
**Qué comprobar:** Puedes revisar composición editable y exportación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `remotion`, `claude-code`, `codex`

## `video-use`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=video,coding-agent,skills,python

**Qué es:** Edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe.
**Stack:** Agente con shell; Python y uv; FFmpeg; material propio; clave ElevenLabs
**Acceso y costes:**
- API de IA: API de IA necesaria. El flujo documentado usa ElevenLabs Scribe por fuente y el plan del agente; ejecutar FFmpeg local no elimina ese consumo
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. Documenta Claude Code, Codex y otros agentes con shell; la ruta instalada requiere configurar la transcripción externa y no se debe anunciar como totalmente offline
- Coste: Consumo de APIs o servicios. El flujo documentado usa ElevenLabs Scribe por fuente y el plan del agente; ejecutar FFmpeg local no elimina ese consumo
- Equipo: Preparación según la ruta elegida. Agente con shell; Python y uv; FFmpeg; material propio; clave ElevenLabs
**Repo:** https://github.com/browser-use/video-use

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/browser-use/video-use/blob/main/install.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Editar una entrevista propia; Seleccionar tomas de un tutorial
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Importa un clip corto y revisa transcripción y plan de cortes antes de exportar
**Qué comprobar:** Puedes contrastar el montaje con el material original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `claude-code`, `hermes-agent`
**Alternativas (elige una):** `remotion-superpowers`

## `videofy-minimal`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,typescript

**Qué es:** Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión.
**Stack:** uv; Node; FFmpeg; claves OpenAI y ElevenLabs; artículo autorizado
**Acceso y costes:**
- API de IA: API de IA necesaria. Necesita modelos y voz por API; Reuters o AP requieren además acceso a sus fuentes si los eliges
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La aplicación local usa servicios remotos y no incluye derechos de noticias o medios; las fuentes y afirmaciones requieren revisión
- Coste: Consumo de APIs o servicios. Necesita modelos y voz por API; Reuters o AP requieren además acceso a sus fuentes si los eliges
- Equipo: Preparación según la ruta elegida. uv; Node; FFmpeg; claves OpenAI y ElevenLabs; artículo autorizado
**Repo:** https://github.com/schibsted/videofy_minimal

**Instalación** [+]:

```
uv sync
npm install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una noticia para señalización; Probar una pieza informativa breve
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un borrador desde un artículo de prueba y revisa guion, voz y fuentes antes de exportar
**Qué comprobar:** Puedes identificar qué contenido se usó y verificar el video
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `remotion`, `whisper`, `ffmpeg`
**Alternativas (elige una):** `moneyprinterturbo`
