# 26. Animación, gráficos y creación 3D — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `animejs`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,design,javascript

**Qué es:** Motor de animación JavaScript ligero para CSS, SVG, DOM y objetos.
**Stack:** Proyecto JavaScript; DOM o SVG de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca MIT no requiere modelo ni API; recursos externos se evalúan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Los comandos npm i del apartado de desarrollo preparan el repositorio y no deben confundirse con instalar la biblioteca en tu propia app
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca MIT no requiere modelo ni API; recursos externos se evalúan aparte
- Equipo: Preparación según la ruta elegida. Proyecto JavaScript; DOM o SVG de prueba
**Repo:** https://github.com/juliangarnier/anime

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/juliangarnier/anime/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Mostrar una transición de estado; Animar un SVG sencillo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Anima un cuadrado y cambia duración y easing para observar la diferencia
**Qué comprobar:** Puedes identificar qué propiedad cambia y cuándo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `three.js`, `magicui`, `motion-design-skill`, `zdog`
**Alternativas (elige una):** `gsap`, `motion`

## `awesome-cad`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=creacion-3d,reference

**Qué es:** Directorio de programas, bibliotecas y recursos de diseño asistido por computadora organizados por especialidad.
**Stack:** Navegador; tipo de diseño que necesitas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Consultar la lista es libre; cada herramienta tiene requisitos y licencia propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Los recursos MCP y agentes se han movido a una lista dedicada; el directorio no es por sí mismo un conector de CAD
- Coste: Sin pago a un modelo en la ruta básica. Consultar la lista es libre; cada herramienta tiene requisitos y licencia propios
- Equipo: Preparación según la ruta elegida. Navegador; tipo de diseño que necesitas
**Repo:** https://github.com/mlightcad/awesome-cad

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar software CAD; Comparar bibliotecas de geometría
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Escoge una herramienta de CAD paramétrico y otra de mallas y compara sus formatos de salida
**Qué comprobar:** Puedes explicar cuál se ajusta al objeto que quieres diseñar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `blender`, `three.js`, `filament`, `freecad`, `openscad`

## `babylonjs`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=javascript,3d,webgl,webxr

**Qué es:** Motor 3D completo para la web de Microsoft y la comunidad, con física, materiales PBR, WebXR, editor de nodos y playground en línea.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/BabylonJS/Babylon.js

**Instalación** [+]:

```
npm install babylonjs --save
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: mostrar un configurador de producto 3D en una web; crear un juego o experiencia WebXR en el navegador
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Abre el playground oficial, carga un ejemplo y modifícalo; o instala con `npm install babylonjs --save`.
**Qué comprobar:** La escena 3D se renderiza en el navegador con tus cambios.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `blender`, `meshoptimizer`, `gsap`
**Alternativas (elige una):** `three.js`, `playcanvas`

## `bevy`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=rust,gamedev,ecs,3d

**Qué es:** Motor de juegos en Rust basado en datos y en el patrón ECS, libre (MIT o Apache-2.0), modular y con funciones 2D y 3D para juegos y simulaciones.
**Stack:** Rust, Cargo.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/bevyengine/bevy

**Instalación** [+]:

```
cargo run --example breakout
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: programar un juego 2D o 3D en Rust con alto rendimiento; crear una simulación o herramienta visual que compile también a WebAssembly
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Clona el repositorio y ejecuta `cargo run --example breakout`.
**Qué comprobar:** Se abre el juego de ejemplo Breakout en una ventana.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `blender`, `meshoptimizer`, `claude-code`
**Alternativas (elige una):** `godot`

## `blender`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=creacion-3d,app,c

**Qué es:** Código de Blender, la aplicación para modelar, animar, renderizar y editar escenas y contenido tridimensional.
**Stack:** Aplicación Blender para tu sistema; equipo adecuado a la escena
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La app no exige API de IA; assets, plugins, render en nube y hardware tienen condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Este repositorio es un espejo del código; para utilizar Blender elige la distribución de la aplicación y no compiles todo el espejo; los conectores AI son otros proyectos
- Coste: Sin pago a un modelo en la ruta básica. La app no exige API de IA; assets, plugins, render en nube y hardware tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Aplicación Blender para tu sistema; equipo adecuado a la escena
**Repo:** https://github.com/blender/blender

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/blender/blender/blob/main/.github/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Modelar un objeto sencillo; Preparar una escena de presentación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa una escena nueva con un cubo y prueba mover, iluminar y renderizar una imagen
**Qué comprobar:** Puedes guardar el proyecto y localizar el render
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `blender-mcp`, `3dviz-pro-max`, `three.js`

## `filament`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=creacion-3d,library,c

**Qué es:** Motor de renderizado físicamente basado para integrar gráficos 3D en aplicaciones móviles, web y de escritorio.
**Stack:** Plataforma de destino; runtime y herramientas de la misma release; modelo glTF de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API de IA; recursos, hardware y distribución tienen costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El compilador de materiales y runtime deben ser de la misma versión; las dependencias Gradle son configuración del proyecto Android, no comandos de shell
- Coste: Sin pago a un modelo en la ruta básica. No necesita API de IA; recursos, hardware y distribución tienen costes propios
- Equipo: Preparación según la ruta elegida. Plataforma de destino; runtime y herramientas de la misma release; modelo glTF de prueba
**Repo:** https://github.com/google/filament

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/google/filament/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Integrar un visor 3D móvil; Estudiar render físicamente basado
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un modelo de muestra y cambia iluminación o material para observar la respuesta
**Qué comprobar:** Puedes distinguir geometría, material y entorno
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `meshoptimizer`, `blender`, `ozz-animation`, `awesome-cad`

## `freecad`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=cad,3d,cpp,app

**Qué es:** Modelador CAD 3D paramétrico libre para diseño de producto, ingeniería mecánica y arquitectura (BIM), con planos técnicos, FEM, CAM y Python.
**Stack:** C++, CMakeLists.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/FreeCAD/FreeCAD

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/FreeCAD/FreeCAD/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: diseñar una pieza mecánica paramétrica y exportarla a STL para impresión 3D; generar planos técnicos acotados a partir de un modelo 3D
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala FreeCAD desde su web, crea un boceto en Part Design y extrúyelo.
**Qué comprobar:** Obtienes un sólido paramétrico que cambia al editar las cotas del boceto.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openscad`, `blender`, `awesome-cad`

## `genesis-world`
role=library · exec=local · setup=hard · mcp=False · prov=— · tags=simulation,robotics,physics,python

**Qué es:** Plataforma de simulación para IA física y robótica con motor multifísica unificado (rígidos, FEM, MPM, fluidos), render fotorrealista y paralelismo masivo en GPU.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Genesis-Embodied-AI/genesis-world

**Instalación** [+]:

```
pip install genesis-world
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: entrenar políticas de robots con miles de entornos paralelos en GPU; generar datos sintéticos de manipulación con cuerpos rígidos y deformables
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala PyTorch y después `pip install genesis-world`; ejecuta el ejemplo `examples/rigid/single_franka.py`.
**Qué comprobar:** Se simula un brazo Franka en una escena con visor.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `mujoco`, `blender`

## `godot`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=gamedev,3d,2d,cpp

**Qué es:** Motor de videojuegos 2D y 3D libre (MIT) con editor integrado, scripting en GDScript o C# y exportación a escritorio, móvil, web y consolas.
**Stack:** C++, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/godotengine/godot

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/godotengine/godot/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: crear un juego 2D o 3D y exportarlo a Windows, Android y web; construir una visualización interactiva o una simulación con editor visual
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga Godot desde su web, abre un proyecto de las demos oficiales y ejecútalo con F5.
**Qué comprobar:** La demo se ejecuta en una ventana y puedes modificar sus escenas en el editor.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `blender`, `meshoptimizer`, `ffmpeg`
**Alternativas (elige una):** `bevy`

## `gsap`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=ui,design,javascript

**Qué es:** Librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados sobre cualquier propiedad del DOM.
**Stack:** Proyecto JavaScript; elementos de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El README describe uso sin cargo bajo la licencia estándar de GreenSock; no debe sustituirse esa licencia por MIT
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una biblioteca web sin LLM; los efectos requieren diseño, implementación y pruebas en la página que los usa
- Coste: Sin pago a un modelo en la ruta básica. El README describe uso sin cargo bajo la licencia estándar de GreenSock; no debe sustituirse esa licencia por MIT
- Equipo: Preparación según la ruta elegida. Proyecto JavaScript; elementos de prueba
**Repo:** https://github.com/greensock/GSAP

**Instalación** [+]:

```
npm install gsap
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Sincronizar una transición compleja; Animar un diagrama explicativo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una timeline con dos movimientos y cambia el orden y duración
**Qué comprobar:** Puedes ver cómo se coordinan los pasos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `three.js`, `motion`, `remotion`
**Alternativas (elige una):** `animejs`

## `meshoptimizer`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=creacion-3d,library,c

**Qué es:** Biblioteca para optimizar geometría y reducir el coste de almacenar y renderizar mallas tridimensionales.
**Stack:** Entorno de desarrollo compatible; malla pequeña; copia del original
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. MIT sin API de IA; assets y herramientas de procesamiento tienen sus licencias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Simplificar geometría implica un compromiso de detalle; conserva el original y evalúa la salida antes de reemplazar assets
- Coste: Sin pago a un modelo en la ruta básica. MIT sin API de IA; assets y herramientas de procesamiento tienen sus licencias
- Equipo: Preparación según la ruta elegida. Entorno de desarrollo compatible; malla pequeña; copia del original
**Repo:** https://github.com/zeux/meshoptimizer

**Instalación** [+]:

```
git clone -b v1.3 https://github.com/zeux/meshoptimizer.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir peso de un asset 3D; Preparar mallas para render en tiempo real
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Optimiza una malla de prueba y compara número de vértices, tamaño y apariencia
**Qué comprobar:** Puedes medir una reducción y detectar si cambia demasiado el detalle
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `three.js`, `filament`, `blender`, `ozz-animation`, `regl`

## `motion`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=ui,design,typescript

**Qué es:** Librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteracciones con muy poco código.
**Stack:** Proyecto React, JavaScript o Vue; componente de prueba; agente opcional
**Acceso y costes:**
- API de IA: API de IA opcional. El núcleo y MCP de documentación son gratuitos; Motion+, Studio y el modelo del agente tienen condiciones separadas
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. El MCP busca documentación y metadatos de ejemplos; no concede acceso a recursos premium ni ejecuta una suscripción de Codex por sí mismo
- Coste: El coste depende del proveedor o la ruta. El núcleo y MCP de documentación son gratuitos; Motion+, Studio y el modelo del agente tienen condiciones separadas
- Equipo: Preparación según la ruta elegida. Proyecto React, JavaScript o Vue; componente de prueba; agente opcional
**Repo:** https://github.com/motiondivision/motion

**Instalación** [+]:

```
# React / JavaScript
npm install motion
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Animar apertura de contenido; Crear una transición de lista
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade una transición sencilla a un elemento y comprueba su estado inicial y final
**Qué comprobar:** Puedes ajustar la animación y seguir usando el control con teclado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `magicui`, `react-three-fiber`, `claude-code`, `gsap`, `motion-design-skill`, `skills-emil`
**Alternativas (elige una):** `animejs`

## `mujoco`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=simulation,robotics,physics,python

**Qué es:** Motor de física de Google DeepMind para simular estructuras articuladas con contacto, estándar en robótica, biomecánica y aprendizaje por refuerzo.
**Stack:** C++, CMakeLists.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/google-deepmind/mujoco

**Instalación** [+]:

```
pip install mujoco
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: simular un robot o un brazo para probar controladores antes del hardware; entrenar políticas de aprendizaje por refuerzo en entornos físicos
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install mujoco`, carga un modelo MJCF de ejemplo y ábrelo con `python -m mujoco.viewer`.
**Qué comprobar:** Ves el modelo simulado en el visor interactivo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `jax`, `warp`, `genesis-world`

## `openscad`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=cad,3d,code,app

**Qué es:** CAD 3D por código: describes la pieza en un lenguaje de script y OpenSCAD la compila a un sólido exportable (STL, 3MF), ideal para piezas paramétricas.
**Stack:** C++, CMakeLists.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/openscad/openscad

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/openscad/openscad/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: diseñar piezas paramétricas para impresión 3D cambiando variables; generar variantes de una pieza (tamaños, agujeros) desde el mismo script
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala OpenSCAD, escribe `cube(10); translate([5,5,5]) sphere(6);`, renderiza con F6 y exporta a STL.
**Qué comprobar:** Obtienes un archivo STL listo para el laminador de la impresora.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `freecad`, `awesome-cad`, `claude-code`

## `ozz-animation`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=creacion-3d,library,c

**Qué es:** Biblioteca C++ y herramientas para preparar y reproducir animación esquelética dentro de motores y aplicaciones.
**Stack:** Entorno C++; modelo con esqueleto; herramientas de conversión compatibles
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Biblioteca MIT sin API de IA; assets y herramientas de creación tienen licencias separadas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una biblioteca de bajo nivel independiente del motor; no crea automáticamente un personaje ni su rig
- Coste: Sin pago a un modelo en la ruta básica. Biblioteca MIT sin API de IA; assets y herramientas de creación tienen licencias separadas
- Equipo: Preparación según la ruta elegida. Entorno C++; modelo con esqueleto; herramientas de conversión compatibles
**Repo:** https://github.com/guillaumeblanc/ozz-animation

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/guillaumeblanc/ozz-animation/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Reproducir animaciones de personajes; Combinar clips en un motor propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta una muestra de reproducción y cambia el tiempo de una animación esquelética
**Qué comprobar:** Puedes identificar esqueleto, clip y pose
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `filament`, `blender`, `meshoptimizer`

## `pencil`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=edicion,app,c

**Qué es:** Aplicación para crear animación 2D dibujada a mano mediante herramientas de dibujo y una línea de tiempo.
**Stack:** Instalador de tu sistema; tableta opcional; carpeta de proyecto
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelo ni API; medios y equipo son recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Pencil2D es un editor de animación 2D tradicional; no debe confundirse con herramientas IA o editores de UI que comparten nombre
- Coste: Sin pago a un modelo en la ruta básica. No necesita modelo ni API; medios y equipo son recursos propios
- Equipo: Preparación según la ruta elegida. Instalador de tu sistema; tableta opcional; carpeta de proyecto
**Repo:** https://github.com/pencil2d/pencil

**Instalación** [?]:

```
Seguir la instalación original: https://www.pencil2d.org/download/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender animación dibujada a mano; Crear una prueba de movimiento 2D
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Dibuja tres fotogramas sencillos, ajusta su duración y reproduce el movimiento
**Qué comprobar:** Puedes guardar el proyecto y exportar una animación corta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `blender`, `pixelfx`

## `pixelfx`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=animacion,library,javascript

**Qué es:** Colección de efectos de pixel art hechos con código y una skill para ayudar a generar efectos propios.
**Stack:** Proyecto JavaScript o motor que admita sprites; Claude Code opcional
**Acceso y costes:**
- API de IA: API de IA opcional. Los efectos básicos no requieren modelo; crear nuevos con el skill usa el agente y publicar con Patch tiene condiciones propias
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Documenta plugin de Claude Code; no es necesario publicar el juego para usar o estudiar un efecto existente
- Coste: El coste depende del proveedor o la ruta. Los efectos básicos no requieren modelo; crear nuevos con el skill usa el agente y publicar con Patch tiene condiciones propias
- Equipo: Preparación según la ruta elegida. Proyecto JavaScript o motor que admita sprites; Claude Code opcional
**Repo:** https://github.com/patch-gg/pixelfx

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/patch-gg/pixelfx/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir un efecto a un juego; Preparar una hoja de sprites
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un efecto existente y cambia tamaño o paleta antes de pedir generar uno nuevo
**Qué comprobar:** Puedes inspeccionar frames y exportar una muestra
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `threejs-game-skills`, `planck-js`, `pencil`

## `pixijs`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=javascript,2d,webgl,animation

**Qué es:** Motor de renderizado 2D para la web sobre WebGL y WebGPU, muy rápido, para juegos, gráficos interactivos y aplicaciones visuales en el navegador.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/pixijs/pixijs

**Instalación** [+]:

```
npm create pixi.js@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: crear un juego 2D o una experiencia interactiva para navegador; dibujar miles de elementos animados en una visualización web
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Crea un proyecto con `npm create pixi.js@latest`, añade un sprite y anímalo en el ticker.
**Qué comprobar:** El sprite se mueve en el canvas del navegador a alta tasa de fotogramas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gsap`, `mediabunny`, `planck-js`

## `planck-js`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=animacion,library,typescript

**Qué es:** Motor de física 2D para simular cuerpos, colisiones y uniones dentro de juegos o aplicaciones JavaScript.
**Stack:** Proyecto JavaScript; escena 2D de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelos ni API; hosting y assets se costean aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un motor de física 2D basado en Box2D y corresponde a simulación; no genera animaciones por instrucciones de IA
- Coste: Sin pago a un modelo en la ruta básica. No necesita modelos ni API; hosting y assets se costean aparte
- Equipo: Preparación según la ruta elegida. Proyecto JavaScript; escena 2D de prueba
**Repo:** https://github.com/piqnt/planck.js

**Instalación** [?]:

```
Seguir la instalación original: https://piqnt.com/planck.js/docs/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar física de un juego 2D; Explicar gravedad con una simulación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una demo de un cuerpo que cae y modifica gravedad o rebote
**Qué comprobar:** Puedes observar colisión y estado del cuerpo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pixelfx`, `threejs-game-skills`, `three.js`, `pixijs`

## `playcanvas`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=javascript,3d,webgpu,gamedev

**Qué es:** Motor gráfico web de código abierto sobre WebGPU y WebGL2 para apps, juegos y visualizaciones 2D y 3D, con soporte de Gaussian splats y glTF.
**Stack:** JavaScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/playcanvas/engine

**Instalación** [+]:

```
npm install playcanvas
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: publicar una escena 3D o un escaneo con Gaussian splats en una web; crear un juego ligero que funcione en cualquier navegador y móvil
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Crea un proyecto con `npm create playcanvas@latest` o instala `npm install playcanvas` y ejecuta el ejemplo del cubo giratorio.
**Qué comprobar:** El cubo 3D gira en un canvas del navegador.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `meshoptimizer`, `blender`, `gsap`
**Alternativas (elige una):** `three.js`, `babylonjs`

## `react-three-fiber`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=ui,design,typescript

**Qué es:** Renderer de React para three.js que expresa escenas 3D como componentes declarativos y reactivos.
**Stack:** React; Three.js; versiones compatibles; navegador
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API de IA; modelos, texturas y alojamiento son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un renderer React sobre Three.js; hay que alinear la versión de React y Fiber y no es un editor 3D para uso directo
- Coste: Sin pago a un modelo en la ruta básica. Sin API de IA; modelos, texturas y alojamiento son independientes
- Equipo: Preparación según la ruta elegida. React; Three.js; versiones compatibles; navegador
**Repo:** https://github.com/pmndrs/react-three-fiber

**Instalación** [+]:

```
npm install three @types/three @react-three/fiber
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un configurador 3D; Construir una escena React interactiva
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Monta una escena con un cubo y cambia una propiedad mediante estado de React
**Qué comprobar:** Puedes observar la actualización declarativa del objeto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `three.js`, `react-three-rapier`, `motion`, `threejs-skills`, `webgl-noise`

## `react-three-rapier`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=animacion,library,typescript

**Qué es:** Integración del motor de física Rapier con React Three Fiber para añadir simulación a escenas tridimensionales.
**Stack:** React y Fiber compatibles; escena 3D; Rapier
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API de IA; recursos y cómputo de la aplicación separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La versión 2 documenta React 19 y Fiber 9, mientras React 18 requiere la versión 1 y Fiber 8; no mezcles las líneas de versiones
- Coste: Sin pago a un modelo en la ruta básica. Sin API de IA; recursos y cómputo de la aplicación separados
- Equipo: Preparación según la ruta elegida. React y Fiber compatibles; escena 3D; Rapier
**Repo:** https://github.com/pmndrs/react-three-rapier

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/pmndrs/react-three-rapier/blob/main/readme.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una escena física React; Prototipar interacción con objetos 3D
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade un cuerpo y un suelo con debug visible y comprueba la colisión
**Qué comprobar:** Puedes relacionar collider, geometría y movimiento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `react-three-fiber`, `three.js`, `threejs-game-skills`

## `regl`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=animacion,library,javascript

**Qué es:** Biblioteca funcional para organizar comandos de renderizado WebGL y dibujar gráficos acelerados en una aplicación web.
**Stack:** Node; proyecto WebGL; nociones de shaders
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Biblioteca MIT sin modelo ni API de IA
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una abstracción de WebGL para desarrolladores y no un editor gráfico o biblioteca de componentes de interfaz
- Coste: Sin pago a un modelo en la ruta básica. Biblioteca MIT sin modelo ni API de IA
- Equipo: Preparación según la ruta elegida. Node; proyecto WebGL; nociones de shaders
**Repo:** https://github.com/regl-project/regl

**Instalación** [+]:

```
npm i -S regl
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar visualización acelerada; Aprender render funcional
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Dibuja un triángulo de ejemplo y cambia una propiedad del comando de render
**Qué comprobar:** Puedes identificar buffers, shader y llamada de dibujo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `webgl-noise`, `three.js`, `meshoptimizer`

## `scenejs`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=animacion,library,typescript

**Qué es:** Biblioteca JavaScript para crear y controlar animaciones mediante líneas de tiempo y propiedades de elementos.
**Stack:** Node; proyecto web; elemento de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Biblioteca MIT sin modelo ni API de IA
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Los bloques JavaScript se integran en una app y no son órdenes para pegar en la terminal; los plugins de medios tienen dependencias separadas
- Coste: Sin pago a un modelo en la ruta básica. Biblioteca MIT sin modelo ni API de IA
- Equipo: Preparación según la ruta elegida. Node; proyecto web; elemento de prueba
**Repo:** https://github.com/daybrush/scenejs

**Instalación** [+]:

```
npm install scenejs
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una animación de interfaz; Explorar una línea de tiempo web
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una animación con dos keyframes y cambia su progreso desde un control
**Qué comprobar:** Puedes identificar tiempo, propiedad y valor final
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `motion-design-skill`, `remotion`, `zdog`

## `three.js`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=ui,design,javascript

**Qué es:** Biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y WebGPU.
**Stack:** Proyecto JavaScript; servidor de desarrollo; navegador con GPU compatible
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no necesita API de IA; modelos 3D, texturas y hosting tienen licencias y costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una biblioteca y no un editor de escenas listo para usar; clonar todo el historial no es necesario para integrarla en una app
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no necesita API de IA; modelos 3D, texturas y hosting tienen licencias y costes propios
- Equipo: Preparación según la ruta elegida. Proyecto JavaScript; servidor de desarrollo; navegador con GPU compatible
**Repo:** https://github.com/mrdoob/three.js

**Instalación** [?]:

```
Seguir la instalación original: https://threejs.org/manual/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un visor 3D web; Prototipar una escena interactiva
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue el ejemplo del cubo y cambia su color o rotación
**Qué comprobar:** Puedes ver la escena, cámara y objeto y reconocer su relación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `react-three-fiber`, `gsap`, `threejs-skills`, `meshoptimizer`
**Alternativas (elige una):** `babylonjs`, `playcanvas`

## `warp`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=entrenamiento,cuda,differentiable-programming,gpu,gpu-acceleration,nvidia,nvidia-warp,python

**Qué es:** Framework de NVIDIA para kernels y simulación física en CPU o GPU; no es un modelo ni un terminal.
**Stack:** Python 3.11+; CPU o GPU soportada; ejemplo pequeño
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API de IA; GPU, energía y servicios de cómputo son costes separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. NVIDIA Warp es un framework de kernels y simulación, no el terminal Warp ni un modelo conversacional; corresponde mejor a simulación y gráficos que a fine-tuning de LLM
- Coste: Sin pago a un modelo en la ruta básica. Sin API de IA; GPU, energía y servicios de cómputo son costes separados
- Equipo: Preparación según la ruta elegida. Python 3.11+; CPU o GPU soportada; ejemplo pequeño
**Repo:** https://github.com/NVIDIA/warp

**Instalación** [+]:

```
pip install warp-lang
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar simulación física; Prototipar cómputo para robótica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta una simulación de ejemplo con pocas partículas y revisa su evolución
**Qué comprobar:** Puedes identificar kernel, dispositivo y estado simulado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `blender`, `cosmos`, `mujoco`

## `webgl-noise`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=animacion,library,c

**Qué es:** Rutinas de ruido procedural para shaders de WebGL, útiles para crear texturas y efectos visuales en tiempo real.
**Stack:** Proyecto WebGL; conocimientos de GLSL; shader de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Rutinas MIT sin API ni datos externos; el render utiliza la GPU
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El autor remite a su clon stegu/webgl-noise para mantenimiento; es código de shader y no una aplicación generativa de IA
- Coste: Sin pago a un modelo en la ruta básica. Rutinas MIT sin API ni datos externos; el render utiliza la GPU
- Equipo: Preparación según la ruta elegida. Proyecto WebGL; conocimientos de GLSL; shader de prueba
**Repo:** https://github.com/ashima/webgl-noise

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/ashima/webgl-noise/blob/master/README
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear textura de nube procedural; Explorar variaciones de una superficie
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Integra una función de ruido y cambia su escala para observar el patrón
**Qué comprobar:** Puedes reconocer un patrón procedural sin cargar una textura
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `three.js`, `regl`, `react-three-fiber`

## `zdog`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=animacion,library,javascript

**Qué es:** Motor de gráficos pseudo-3D que permite dibujar y animar ilustraciones sencillas mediante canvas o SVG.
**Stack:** Página de prueba; JavaScript; canvas o SVG
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. MIT y sin API de IA; alojamiento y recursos propios separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es pseudo-3D para ilustraciones simples y no un motor de modelado o render físicamente basado
- Coste: Sin pago a un modelo en la ruta básica. MIT y sin API de IA; alojamiento y recursos propios separados
- Equipo: Preparación según la ruta elegida. Página de prueba; JavaScript; canvas o SVG
**Repo:** https://github.com/metafizzy/zdog

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/metafizzy/zdog/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar un icono pseudo-3D; Preparar una ilustración interactiva
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una ilustración pequeña y cambia su rotación para observar la profundidad aparente
**Qué comprobar:** Puedes reconocer las formas y su orden
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `animejs`, `gsap`, `three.js`, `scenejs`
