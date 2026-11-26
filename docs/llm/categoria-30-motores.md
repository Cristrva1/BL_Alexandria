# Alexandría para agentes · Motores de video y escenas por código

Categoría 30 «Video con código y agentes creativos» › subcategoría `motores`. 8 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=30&sub=motores · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `hyperframes` | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4… | 1 Básico | 73 | Apache-2.0 (OSI permisiva) | recomendado |
| `manim-community` | Motor de animación de Python para producir videos explicativos de matemáticas… | 2 Intermedio | 71 | MIT (OSI permisiva) | recomendado |
| `remotion` | Framework de React para crear videos por código y renderizar composiciones con… | 2 Intermedio | 68 | Remotion License (no OSI) (source-available) | alternativa |
| `mediabunny` | Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video… | 2 Intermedio | 65 | MPL-2.0 (OSI copyleft) | sin grupo |
| `motion-canvas` | Biblioteca TypeScript para crear animaciones y vídeos explicativos con código… | 2 Intermedio | 56 | MIT (OSI permisiva) | alternativa |
| `manim` | Motor de animación en Python para videos matemáticos explicativos, creado por… | 2 Intermedio | 54 | MIT (OSI permisiva) | alternativa |
| `moviepy` | Librería Python para editar video por código: cortes, concatenaciones, títulos… | 2 Intermedio | 54 | MIT (OSI permisiva) | alternativa |
| `revideo` | Motor TypeScript para crear vídeos con código y renderizarlos sin interfaz… | 2 Intermedio | 51 | MIT (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### HyperFrames (`hyperframes`)

- **Repo:** https://github.com/heygen-com/hyperframes · Apache-2.0 · nivel 1 · 73/100 · recomendado en «Video y escenas por código»
- **Qué es:** HyperFrames, framework de HeyGen que convierte HTML, CSS, medios y animaciones navegables en vídeos MP4 deterministas, pensado para agentes. Licencia Apache-2.0, sin tarifas por render ni umbrales comerciales.
- **Cuándo elegirlo:** Casos: Preparar un video explicativo por código; Crear una pieza de presentación con HTML.
- **Requisitos:** nivel 1: preparación sencilla; Node 22+; FFmpeg; composición pequeña; agente opcional; hardware prerequisites; API de IA: opcional; Node 22+; FFmpeg; composición pequeña; agente opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `npx hyperframes init my-video` — fuente: https://github.com/heygen-com/hyperframes/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un proyecto con un título de pocos segundos, previsualiza y renderiza un MP4 Éxito: Puedes comprobar duración, primer y último frame y archivo exportado
- **Combina con:** `claude-code` [20/terminal], `gsap` [26/animacion], `kokoro` [29/tts], `whisperx` [29/stt], `arcads-claude-code` [27/dominio], `brag` [30/skills-video]
- **Alternativas:** `remotion`, `motion-canvas`, `moviepy`, `revideo`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): remotion, moviepy. Su README compara explícitamente su licencia con la de Remotion. Los skills deben coincidir con la versión del CLI; el núcleo basta para empezar y no es necesario instalar todo el catálogo de extensiones.

### manim (`manim-community`)

- **Repo:** https://github.com/ManimCommunity/manim · MIT · nivel 2 · 71/100 · recomendado en «Animaciones matemáticas (Manim)»
- **Qué es:** Manim Community Edition (ManimCE), fork comunitario de 3b1b/manim para animaciones matemáticas explicativas. Doble licencia MIT (3blue1brown LLC y Manim Community Developers). Es madura y activa (~43k estrellas, v0.22.1).
- **Cuándo elegirlo:** Casos: Preparar una explicación matemática; Crear una animación de geometría.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; dependencias de la versión; LaTeX según escena; equipo; hardware prerequisites; API de IA: no; Python; dependencias de la versión; LaTeX según escena; equipo.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install manim` — fuente: https://github.com/ManimCommunity/manim/blob/main/docs/source/installation.rst
- **Primera prueba propuesta (no ejecutada):** Sigue SquareToCircle y modifica una propiedad para observar la transformación Éxito: Puedes renderizar y relacionar el resultado con la escena Python
- **Combina con:** `ffmpeg` [12/edicion], `kokoro` [29/tts], `srt-whiteboard-animation` [30/skills-video]
- **Alternativas:** `manim`
- **Riesgos y avisos:** Alternativas (elige una): manim. Manim Community usa from manim y su propio CLI; es una línea distinta de ManimGL y sus tutoriales no son intercambiables sin adaptar.

### remotion (`remotion`)

- **Repo:** https://github.com/remotion-dev/remotion · Remotion License (no OSI) · nivel 2 · 68/100 · alternativa en «Video y escenas por código»
- **Qué es:** Remotion, framework de React para crear vídeos por código, de remotion-dev. Licencia «Remotion License» especial (GitHub muestra NOASSERTION): exige licencia de empresa en algunos casos. Es maduro (~73k estrellas, v4.0.543).
- **Cuándo elegirlo:** Casos: Crear una plantilla de video con datos; Preparar títulos animados.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node; proyecto React; recursos propios; licencia según uso; agente opcional; hardware prerequisites; API de IA: opcional; Node; proyecto React; recursos propios; licencia según uso; agente opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `npx create-video@latest` — fuente: https://github.com/remotion-dev/remotion/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una composición de prueba y comprueba que la cantidad de frames corresponde a su duración Éxito: Puedes reproducir y exportar un clip con inicio y fin definidos
- **Combina con:** `skills-remotion` [30/skills-video], `remotion-superpowers` [30/skills-video], `gsap` [26/animacion]
- **Alternativas:** `hyperframes`, `motion-canvas`, `moviepy`, `revideo`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): moviepy, hyperframes. Revisa la licencia antes de un uso comercial. La ruta con agentes utiliza las skills oficiales del proyecto compañero; no todo uso comercial es gratuito por estar disponible el código.

### mediabunny (`mediabunny`)

- **Repo:** https://github.com/Vanilagy/mediabunny · MPL-2.0 · nivel 2 · 65/100
- **Qué es:** Mediabunny, librería JavaScript para leer, escribir y convertir medios (MP4, WebM, MP3, HLS) directamente en el navegador, de @Vanilagy. Licencia MPL-2.0. Es activa (~7.5k estrellas, v1.66.0) y la patrocina, entre otros, Remotion.
- **Cuándo elegirlo:** Casos: Procesar video dentro de una aplicación web; Construir una herramienta de conversión en navegador.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; JavaScript ES2021+; navegador moderno; TypeScript >=5.7 para tipos; medio de prueba; hardware prerequisites; API de IA: no; JavaScript ES2021+; navegador moderno; TypeScript >=5.7 para tipos; medio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install mediabunny` — fuente: https://github.com/Vanilagy/mediabunny/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee duración y pistas de un archivo y convierte una copia a un formato admitido Éxito: Puedes contrastar metadatos y reproducir la salida
- **Combina con:** `remotion`, `ffmpeg` [12/edicion], `openfilm` [30/skills-video], `pixijs` [26/animacion]
- **Riesgos y avisos:** Sin alternativas declaradas. Es una biblioteca de medios, no una app de edición completa; comprueba soporte de codecs y destino en los navegadores de tus usuarios.

### Motion Canvas (`motion-canvas`)

- **Repo:** https://github.com/motion-canvas/motion-canvas · MIT · nivel 2 · 56/100 · alternativa en «Video y escenas por código»
- **Qué es:** Biblioteca de código abierto (MIT) orientada a vídeos explicativos. Popular; el desarrollo se ha ralentizado (última versión publicada v3.17.2, diciembre de 2024; último push en julio de 2026).
- **Cuándo elegirlo:** Casos: hacer vídeos explicativos de programación o matemáticas con animaciones precisas; sincronizar animaciones con una narración grabada.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/motion-canvas/motion-canvas/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta `npm init @motion-canvas@latest`, entra en la carpeta, ejecuta `npm install` y `npm start`, y abre el editor. Éxito: Ves la escena de ejemplo y puedes editar el código con recarga en vivo.
- **Combina con:** `ffmpeg` [12/edicion], `kokoro` [29/tts], `claude-code` [20/terminal]
- **Alternativas:** `hyperframes`, `remotion`, `moviepy`, `revideo`
- **Riesgos y avisos:** Alternativa de Revideo (fork orientado a renderizado programático) y Remotion (React).

### Manim (ManimGL) (`manim`)

- **Repo:** https://github.com/3b1b/manim · MIT · nivel 2 · 54/100 · alternativa en «Animaciones matemáticas (Manim)»
- **Qué es:** ManimGL, motor de animación programática para vídeos matemáticos explicativos, creado por el autor de 3Blue1Brown (@3b1b). Licencia MIT. Tiene ~97k estrellas (v1.7.2); es la versión personal del autor, distinta de la edición comunitaria.
- **Cuándo elegirlo:** Casos: Explicar una transformación matemática; Preparar una animación geométrica.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; FFmpeg; OpenGL; LaTeX si escribes fórmulas; escena pequeña; hardware prerequisites; API de IA: no; Python; FFmpeg; OpenGL; LaTeX si escribes fórmulas; escena pequeña.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/3b1b/manim/blob/master/README.md

  ```sh
  # Install manimgl
  pip install manimgl

  # Try it out
  manimgl
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta una escena de ejemplo y cambia una forma o texto Éxito: Puedes abrir la animación y localizar su código
- **Combina con:** `ffmpeg` [12/edicion], `kokoro` [29/tts], `moviepy`
- **Alternativas:** `manim-community`
- **Riesgos y avisos:** Alternativas (elige una): manim-community. Para documentación y estabilidad, la comunidad recomienda ManimCE. Este es ManimGL de 3Blue1Brown y usa manimgl; no mezcles sus imports o comandos con Manim Community.

### MoviePy (`moviepy`)

- **Repo:** https://github.com/Zulko/moviepy · MIT · nivel 2 · 54/100 · alternativa en «Video y escenas por código»
- **Qué es:** MoviePy, librería Python para editar vídeo por código, de @Zulko. Licencia MIT. Es madura (~15k estrellas, v2.2.1); la v2.0 introdujo cambios incompatibles y la v1 ya no se mantiene.
- **Cuándo elegirlo:** Casos: Automatizar variantes de un video; Componer clips y rótulos desde Python.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; FFmpeg según instalación; fuente tipográfica para títulos; video de prueba; hardware prerequisites; API de IA: no; Python; FFmpeg según instalación; fuente tipográfica para títulos; video de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install moviepy` — fuente: https://github.com/Zulko/moviepy/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Recorta diez segundos y superpone un título usando el ejemplo v2 Éxito: El render conserva duración y audio y muestra el título
- **Combina con:** `whisperx` [29/stt], `kokoro` [29/tts], `ffmpeg` [12/edicion]
- **Alternativas:** `hyperframes`, `remotion`, `motion-canvas`, `revideo`
- **Riesgos y avisos:** Alternativas (elige una): remotion, hyperframes. Se quita comfyui de las combinaciones (sin relación directa). V2 cambia APIs como subclipped y with_volume_scaled; los ejemplos v1 no son intercambiables.

### Revideo (`revideo`)

- **Repo:** https://github.com/midrender/revideo · MIT · nivel 2 · 51/100 · alternativa en «Video y escenas por código»
- **Qué es:** Framework de código abierto (MIT) mantenido por Midrender (es el motor de su producto), derivado históricamente de Motion Canvas. Actividad moderada: el último push es de julio de 2026.
- **Cuándo elegirlo:** Casos: generar muchas variantes de un vídeo a partir de datos o plantillas; añadir un renderizador de vídeo a una aplicación web.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `npm init @revideo@latest` — fuente: https://github.com/midrender/revideo/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta `npm init @revideo@latest` y sigue el asistente; después renderiza el proyecto de ejemplo. Éxito: Obtienes un MP4 generado desde código.
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `ffmpeg` [12/edicion]
- **Alternativas:** `hyperframes`, `remotion`, `motion-canvas`, `moviepy`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativa de Motion Canvas y Remotion; frente a Remotion, su licencia MIT no exige licencia comercial para empresas.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-30-motores.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Motores de video y escenas por código», lee `docs/alexandria/categoria-30-motores.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-30-motores.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
