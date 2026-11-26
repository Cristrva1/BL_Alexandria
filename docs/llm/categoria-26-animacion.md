# Alexandría para agentes · Animación y 3D

Categoría 26 «Animación, gráficos y creación 3D» › subcategoría `animacion`. 14 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=26&sub=animacion · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `motion` | Librería de animación declarativa para React/JS (antes Framer Motion) que añade… | 2 Intermedio | 77 | MIT (OSI permisiva) | recomendado |
| `react-three-fiber` | Renderer de React para three.js que expresa escenas 3D como componentes… | 2 Intermedio | 76 | MIT (OSI permisiva) | sin grupo |
| `pixijs` | Motor de renderizado 2D para la web sobre WebGL y WebGPU, muy rápido, para… | 2 Intermedio | 73 | MIT (OSI permisiva) | sin grupo |
| `three.js` | Biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y… | 3 Avanzado | 70 | MIT (OSI permisiva) | recomendado |
| `babylonjs` | Motor 3D completo para la web de Microsoft y la comunidad, con física… | 2 Intermedio | 67 | Apache-2.0 (OSI permisiva) | alternativa |
| `playcanvas` | Motor gráfico web de código abierto sobre WebGPU y WebGL2 para apps, juegos y… | 2 Intermedio | 66 | MIT (OSI permisiva) | alternativa |
| `pixelfx` | Colección de efectos de pixel art hechos con código y una skill para ayudar a… | 2 Intermedio | 64 | MIT (OSI permisiva) | sin grupo |
| `animejs` | Motor de animación JavaScript ligero para CSS, SVG, DOM y objetos. | 2 Intermedio | 61 | MIT (OSI permisiva) | alternativa |
| `regl` | Biblioteca funcional para organizar comandos de renderizado WebGL y dibujar… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `gsap` | Librería de animación de alto rendimiento para la web, capaz de orquestar… | 2 Intermedio | 55 | — (sin licencia detectada) | alternativa |
| `scenejs` | Biblioteca JavaScript para crear y controlar animaciones mediante líneas de… | 2 Intermedio | 50 | MIT (OSI permisiva) | sin grupo |
| `pencil` | Aplicación para crear animación 2D dibujada a mano mediante herramientas de… | 1 Básico | 48 | GPL-2.0 (OSI copyleft) | sin grupo |
| `zdog` | Motor de gráficos pseudo-3D que permite dibujar y animar ilustraciones… | 2 Intermedio | 47 | — (sin licencia detectada) | sin grupo |
| `webgl-noise` | Rutinas de ruido procedural para shaders de WebGL, útiles para crear texturas y… | 2 Intermedio | 46 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### motion (`motion`)

- **Repo:** https://github.com/motiondivision/motion · MIT · nivel 2 · 77/100 · recomendado en «Animación web en JavaScript»
- **Qué es:** Motion (antes Framer Motion), librería de animación open source para JavaScript, React y Vue, de motiondivision. Licencia MIT. Es madura (~35k estrellas) y tiene oferta de pago (Motion+).
- **Cuándo elegirlo:** Casos: Animar apertura de contenido; Crear una transición de lista.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Proyecto React, JavaScript o Vue; componente de prueba; agente opcional; hardware prerequisites; API de IA: opcional; Proyecto React, JavaScript o Vue; componente de prueba; agente opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/motiondivision/motion/blob/main/README.md

  ```bash
  # React / JavaScript
  npm install motion
  ```
- **Primera prueba propuesta (no ejecutada):** Añade una transición sencilla a un elemento y comprueba su estado inicial y final Éxito: Puedes ajustar la animación y seguir usando el control con teclado
- **Combina con:** `magicui` [9/componentes], `react-three-fiber`, `claude-code` [20/terminal], `gsap`, `motion-design-skill` [27/skills], `skills-emil` [27/skills]
- **Alternativas:** `animejs`, `gsap`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): animejs. El MCP busca documentación y metadatos de ejemplos; no concede acceso a recursos premium ni ejecuta una suscripción de Codex por sí mismo.

### react-three-fiber (`react-three-fiber`)

- **Repo:** https://github.com/pmndrs/react-three-fiber · MIT · nivel 2 · 76/100
- **Qué es:** react-three-fiber (@react-three/fiber), renderer de React para three.js, de pmndrs. Licencia MIT. Es madura (~34k estrellas, v9.8.2).
- **Cuándo elegirlo:** Casos: Crear un configurador 3D; Construir una escena React interactiva.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; React; Three.js; versiones compatibles; navegador; hardware prerequisites; API de IA: no; React; Three.js; versiones compatibles; navegador.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install three @types/three @react-three/fiber` — fuente: https://github.com/pmndrs/react-three-fiber/blob/master/readme.md
- **Primera prueba propuesta (no ejecutada):** Monta una escena con un cubo y cambia una propiedad mediante estado de React Éxito: Puedes observar la actualización declarativa del objeto
- **Combina con:** `three.js`, `react-three-rapier` [26/simulacion], `motion`, `threejs-skills` [27/skills], `webgl-noise`
- **Riesgos y avisos:** Sin alternativas declaradas. Es un renderer React sobre Three.js; hay que alinear la versión de React y Fiber y no es un editor 3D para uso directo.

### PixiJS (`pixijs`)

- **Repo:** https://github.com/pixijs/pixijs · MIT · nivel 2 · 73/100
- **Qué es:** Biblioteca de código abierto (MIT) para gráficos 2D en la web, una de las más usadas para juegos y experiencias interactivas en navegador. Activa (v8 con WebGPU).
- **Cuándo elegirlo:** Casos: crear un juego 2D o una experiencia interactiva para navegador; dibujar miles de elementos animados en una visualización web.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `npm create pixi.js@latest` — fuente: https://github.com/pixijs/pixijs/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un proyecto con `npm create pixi.js@latest`, añade un sprite y anímalo en el ticker. Éxito: El sprite se mueve en el canvas del navegador a alta tasa de fotogramas.
- **Combina con:** `gsap`, `mediabunny` [30/motores], `planck-js` [26/simulacion]
- **Riesgos y avisos:** Para 3D en la web, three.js, Babylon.js o PlayCanvas.

### three.js (`three.js`)

- **Repo:** https://github.com/mrdoob/three.js · MIT · nivel 3 · 70/100 · recomendado en «Motores 3D para la web»
- **Qué es:** three.js, biblioteca JavaScript 3D de propósito general, de @mrdoob y comunidad. Licencia MIT. Es muy madura (~119k estrellas, r187).
- **Cuándo elegirlo:** Casos: Crear un visor 3D web; Prototipar una escena interactiva.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, necesita GPU; Proyecto JavaScript; servidor de desarrollo; navegador con GPU compatible; hardware prerequisites; API de IA: no; Proyecto JavaScript; servidor de desarrollo; navegador con GPU compatible.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --depth=1 https://github.com/mrdoob/three.js.git` — fuente: https://github.com/mrdoob/three.js/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el ejemplo del cubo y cambia su color o rotación Éxito: Puedes ver la escena, cámara y objeto y reconocer su relación
- **Combina con:** `react-three-fiber`, `gsap`, `threejs-skills` [27/skills], `meshoptimizer` [26/creacion-3d]
- **Alternativas:** `babylonjs`, `playcanvas`
- **Riesgos y avisos:** Sin alternativas declaradas. Es una biblioteca y no un editor de escenas listo para usar; clonar todo el historial no es necesario para integrarla en una app.

### Babylon.js (`babylonjs`)

- **Repo:** https://github.com/BabylonJS/Babylon.js · Apache-2.0 · nivel 2 · 67/100 · alternativa en «Motores 3D para la web»
- **Qué es:** Motor 3D de código abierto (Apache-2.0) creado en Microsoft y mantenido con la comunidad. Maduro y activo, con playground, sandbox y foro oficiales.
- **Cuándo elegirlo:** Casos: mostrar un configurador de producto 3D en una web; crear un juego o experiencia WebXR en el navegador.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `npm install babylonjs --save` — fuente: https://github.com/BabylonJS/Babylon.js/blob/master/readme.md
- **Primera prueba propuesta (no ejecutada):** Abre el playground oficial, carga un ejemplo y modifícalo; o instala con `npm install babylonjs --save`. Éxito: La escena 3D se renderiza en el navegador con tus cambios.
- **Combina con:** `blender` [26/creacion-3d], `meshoptimizer` [26/creacion-3d], `gsap`
- **Alternativas:** `three.js`, `playcanvas`
- **Riesgos y avisos:** Alternativa de three.js y PlayCanvas: más "todo incluido" que three.js.

### PlayCanvas Engine (`playcanvas`)

- **Repo:** https://github.com/playcanvas/engine · MIT · nivel 2 · 66/100 · alternativa en «Motores 3D para la web»
- **Qué es:** Motor gráfico de código abierto (MIT) de PlayCanvas (propiedad de Snap Inc.). Lo acompañan un editor colaborativo en la nube (servicio con planes) y herramientas como SuperSplat. Activo.
- **Cuándo elegirlo:** Casos: publicar una escena 3D o un escaneo con Gaussian splats en una web; crear un juego ligero que funcione en cualquier navegador y móvil.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; JavaScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `npm install playcanvas` — fuente: https://github.com/playcanvas/engine/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un proyecto con `npm create playcanvas@latest` o instala `npm install playcanvas` y ejecuta el ejemplo del cubo giratorio. Éxito: El cubo 3D gira en un canvas del navegador.
- **Combina con:** `meshoptimizer` [26/creacion-3d], `blender` [26/creacion-3d], `gsap`
- **Alternativas:** `three.js`, `babylonjs`
- **Riesgos y avisos:** Alternativa de three.js y Babylon.js; destaca en carga ligera y visualización de Gaussian splats.

### pixelfx (`pixelfx`)

- **Repo:** https://github.com/patch-gg/pixelfx · MIT · nivel 2 · 64/100
- **Qué es:** pixelfx, colección de 244 efectos y animaciones de pixel art hechos con código, de patch-gg. Licencia MIT. Es muy reciente (octubre de 2026) y ya tiene ~7.6k estrellas.
- **Cuándo elegirlo:** Casos: Añadir un efecto a un juego; Preparar una hoja de sprites.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Proyecto JavaScript o motor que admita sprites; Claude Code opcional; hardware prerequisites; API de IA: opcional; Proyecto JavaScript o motor que admita sprites; Claude Code opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `/plugin marketplace add patch-gg/pixelfx` — fuente: https://github.com/patch-gg/pixelfx/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre un efecto existente y cambia tamaño o paleta antes de pedir generar uno nuevo Éxito: Puedes inspeccionar frames y exportar una muestra
- **Combina con:** `claude-code` [20/terminal], `threejs-game-skills` [27/skills], `planck-js` [26/simulacion], `pencil`
- **Riesgos y avisos:** Sin alternativas declaradas. Documenta plugin de Claude Code; no es necesario publicar el juego para usar o estudiar un efecto existente.

### Anime.js (`animejs`)

- **Repo:** https://github.com/juliangarnier/anime · MIT · nivel 2 · 61/100 · alternativa en «Animación web en JavaScript»
- **Qué es:** Anime.js, motor de animación JavaScript ligero, de @juliangarnier. Licencia MIT. Es maduro (~75k estrellas, v4.5.0) y se financia con patrocinios.
- **Cuándo elegirlo:** Casos: Mostrar una transición de estado; Animar un SVG sencillo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Proyecto JavaScript; DOM o SVG de prueba; hardware prerequisites; API de IA: no; Proyecto JavaScript; DOM o SVG de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/juliangarnier/anime/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Anima un cuadrado y cambia duración y easing para observar la diferencia Éxito: Puedes identificar qué propiedad cambia y cuándo
- **Combina con:** `three.js`, `magicui` [9/componentes], `motion-design-skill` [27/skills], `zdog`
- **Alternativas:** `motion`, `gsap`
- **Riesgos y avisos:** Alternativas (elige una): gsap, motion. Los comandos npm i del apartado de desarrollo preparan el repositorio y no deben confundirse con instalar la biblioteca en tu propia app.

### regl (`regl`)

- **Repo:** https://github.com/regl-project/regl · MIT · nivel 2 · 58/100
- **Qué es:** regl, biblioteca funcional para WebGL, de regl-project. Licencia MIT. Es madura y estable (~5.6k estrellas).
- **Cuándo elegirlo:** Casos: Prototipar visualización acelerada; Aprender render funcional.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node; proyecto WebGL; nociones de shaders; hardware prerequisites; API de IA: no; Node; proyecto WebGL; nociones de shaders.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i -S regl` — fuente: https://github.com/regl-project/regl/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Dibuja un triángulo de ejemplo y cambia una propiedad del comando de render Éxito: Puedes identificar buffers, shader y llamada de dibujo
- **Combina con:** `webgl-noise`, `three.js`, `meshoptimizer` [26/creacion-3d]
- **Riesgos y avisos:** Sin alternativas declaradas. Es una abstracción de WebGL para desarrolladores y no un editor gráfico o biblioteca de componentes de interfaz.

### GSAP (`gsap`)

- **Repo:** https://github.com/greensock/GSAP · — · nivel 2 · 55/100 · alternativa en «Animación web en JavaScript»
- **Qué es:** GSAP (GreenSock Animation Platform), librería de animación JavaScript independiente del framework, propiedad de Webflow. Usa la licencia propia «Standard No Charge», gratuita pero no OSI (GitHub no detecta licencia).
- **Cuándo elegirlo:** Casos: Sincronizar una transición compleja; Animar un diagrama explicativo.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Proyecto JavaScript; elementos de prueba; hardware prerequisites; API de IA: no; Proyecto JavaScript; elementos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install gsap` — fuente: https://github.com/greensock/GSAP/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una timeline con dos movimientos y cambia el orden y duración Éxito: Puedes ver cómo se coordinan los pasos
- **Combina con:** `three.js`, `motion`, `remotion` [30/motores]
- **Alternativas:** `motion`, `animejs`
- **Riesgos y avisos:** Licencia no OSI: revisa las condiciones de uso y redistribución. Alternativas (elige una): animejs. La licencia prohíbe usarla en herramientas visuales de animación sin código que compitan con Webflow. Es una biblioteca web sin LLM; los efectos requieren diseño, implementación y pruebas en la página que los usa.

### scenejs (`scenejs`)

- **Repo:** https://github.com/daybrush/scenejs · MIT · nivel 2 · 50/100
- **Qué es:** Scene.js, biblioteca JavaScript y CSS de animación basada en líneas de tiempo, de @daybrush. Licencia MIT. Tiene ~2.8k estrellas y no se actualiza desde junio de 2023 (1.10.3).
- **Cuándo elegirlo:** Casos: Crear una animación de interfaz; Explorar una línea de tiempo web.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node; proyecto web; elemento de prueba; hardware prerequisites; API de IA: no; Node; proyecto web; elemento de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install scenejs` — fuente: https://github.com/daybrush/scenejs/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una animación con dos keyframes y cambia su progreso desde un control Éxito: Puedes identificar tiempo, propiedad y valor final
- **Combina con:** `motion-design-skill` [27/skills], `remotion` [30/motores], `zdog`
- **Riesgos y avisos:** Sin alternativas declaradas. Inactivo. Los bloques JavaScript se integran en una app y no son órdenes para pegar en la terminal; los plugins de medios tienen dependencias separadas.

### pencil (`pencil`)

- **Repo:** https://github.com/pencil2d/pencil · GPL-2.0 · nivel 1 · 48/100
- **Qué es:** Pencil2D, software libre de animación 2D tradicional dibujada a mano, desarrollado por voluntarios. Licencia GPL-2.0. Tiene ~1.9k estrellas y su última release es v0.7.2 (marzo de 2026).
- **Cuándo elegirlo:** Casos: Aprender animación dibujada a mano; Crear una prueba de movimiento 2D.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador de tu sistema; tableta opcional; carpeta de proyecto; hardware prerequisites; API de IA: no; Instalador de tu sistema; tableta opcional; carpeta de proyecto.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://www.pencil2d.org/download/
- **Primera prueba propuesta (no ejecutada):** Dibuja tres fotogramas sencillos, ajusta su duración y reproduce el movimiento Éxito: Puedes guardar el proyecto y exportar una animación corta
- **Combina con:** `ffmpeg` [12/edicion], `blender` [26/creacion-3d], `pixelfx`
- **Riesgos y avisos:** Sin alternativas declaradas. Pencil2D es un editor de animación 2D tradicional; no debe confundirse con herramientas IA o editores de UI que comparten nombre.

### zdog (`zdog`)

- **Repo:** https://github.com/metafizzy/zdog · — · nivel 2 · 47/100
- **Qué es:** Zdog, motor pseudo-3D «redondo, plano y amigable para diseñadores», de Metafizzy. El README indica licencia MIT, pero GitHub no detecta archivo de licencia. Tiene ~11k estrellas y no se actualiza desde julio de 2023 (v1.1.1).
- **Cuándo elegirlo:** Casos: Diseñar un icono pseudo-3D; Preparar una ilustración interactiva.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Página de prueba; JavaScript; canvas o SVG; hardware prerequisites; API de IA: no; Página de prueba; JavaScript; canvas o SVG.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install zdog` — fuente: https://github.com/metafizzy/zdog/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una ilustración pequeña y cambia su rotación para observar la profundidad aparente Éxito: Puedes reconocer las formas y su orden
- **Combina con:** `animejs`, `gsap`, `three.js`, `scenejs`
- **Riesgos y avisos:** Sin alternativas declaradas. Inactivo. Es pseudo-3D para ilustraciones simples y no un motor de modelado o render físicamente basado.

### webgl-noise (`webgl-noise`)

- **Repo:** https://github.com/ashima/webgl-noise · MIT · nivel 2 · 46/100
- **Qué es:** webgl-noise, rutinas de ruido procedural en GLSL (simplex, clásico, celular y psrdnoise) de Ashima Arts y @stegu. Licencia MIT. Es un repo histórico y estable (~3k estrellas, sin cambios desde noviembre de 2024).
- **Cuándo elegirlo:** Casos: Crear textura de nube procedural; Explorar variaciones de una superficie.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Proyecto WebGL; conocimientos de GLSL; shader de prueba; hardware prerequisites; API de IA: no; Proyecto WebGL; conocimientos de GLSL; shader de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ashima/webgl-noise/blob/master/README
- **Primera prueba propuesta (no ejecutada):** Integra una función de ruido y cambia su escala para observar el patrón Éxito: Puedes reconocer un patrón procedural sin cargar una textura
- **Combina con:** `three.js`, `regl`, `react-three-fiber`
- **Riesgos y avisos:** Sin alternativas declaradas. El autor remite a su clon stegu/webgl-noise para mantenimiento; es código de shader y no una aplicación generativa de IA.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-26-animacion.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Animación y 3D», lee `docs/alexandria/categoria-26-animacion.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-26-animacion.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
