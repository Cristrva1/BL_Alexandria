# Alexandría para agentes · Creación, renderizado y animación 3D

Categoría 26 «Animación, gráficos y creación 3D» › subcategoría `creacion-3d`. 11 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=26&sub=creacion-3d · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `godot` | Motor de videojuegos 2D y 3D libre (MIT) con editor integrado, scripting en… | 2 Intermedio | 77 | MIT (OSI permisiva) | recomendado |
| `blender` | Código de Blender, la aplicación para modelar, animar, renderizar y editar… | 1 Básico | 76 | GPL-2.0-or-later (OSI copyleft) | sin grupo |
| `freecad` | Modelador CAD 3D paramétrico libre para diseño de producto, ingeniería mecánica… | 1 Básico | 71 | LGPL-2.1 (OSI copyleft) | sin grupo |
| `filament` | Motor de renderizado físicamente basado para integrar gráficos 3D en… | 2 Intermedio | 69 | Apache-2.0 (OSI permisiva) | sin grupo |
| `bevy` | Motor de juegos en Rust basado en datos y en el patrón ECS, libre (MIT o… | 2 Intermedio | 66 | MIT OR Apache-2.0 (OSI permisiva) | alternativa |
| `meshoptimizer` | Biblioteca para optimizar geometría y reducir el coste de almacenar y… | 2 Intermedio | 62 | MIT (OSI permisiva) | sin grupo |
| `openscad` | CAD 3D por código: describes la pieza en un lenguaje de script y OpenSCAD la… | 1 Básico | 59 | GPL-2.0 (con excepción CGAL) (OSI copyleft) | sin grupo |
| `ozz-animation` | Biblioteca C++ y herramientas para preparar y reproducir animación esquelética… | 2 Intermedio | 42 | MIT (OSI permisiva) | sin grupo |
| `awesome-cad` | Directorio de programas, bibliotecas y recursos de diseño asistido por… | 1 Básico | 34 | MIT (OSI permisiva) | sin grupo |
| `openreality` | Convierte video propio en escenas 3D consultables y ofrece herramientas MCP… | 3 Avanzado | — | BSD-2-Clause | sin grupo |
| `video2threejs` | Explica con un caso cómo reconstruir la apariencia de un video como una escena… | 1 Básico | — | MIT | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Godot Engine (`godot`)

- **Repo:** https://github.com/godotengine/godot · MIT · nivel 2 · 77/100 · recomendado en «Motores de videojuegos»
- **Qué es:** Motor de juegos de código abierto (MIT), sin regalías, desarrollado por la comunidad y respaldado por la Godot Foundation (sin ánimo de lucro). El motor libre más popular; muy activo.
- **Cuándo elegirlo:** Casos: crear un juego 2D o 3D y exportarlo a Windows, Android y web; construir una visualización interactiva o una simulación con editor visual.
- **Requisitos:** nivel 2: instalación simple, pero crear juegos exige aprender el motor y GDScript; C++, pyproject.toml; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/godotengine/godot/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga Godot desde su web, abre un proyecto de las demos oficiales y ejecútalo con F5. Éxito: La demo se ejecuta en una ventana y puedes modificar sus escenas en el editor.
- **Combina con:** `blender`, `meshoptimizer`, `ffmpeg` [12/edicion]
- **Alternativas:** `bevy`
- **Riesgos y avisos:** Alternativa de Bevy (motor en Rust con ECS y sin editor visual completo).

### blender (`blender`)

- **Repo:** https://github.com/blender/blender · GPL-2.0-or-later · nivel 1 · 76/100
- **Qué es:** Blender, suite libre de creación 3D, de la Blender Foundation. Licencia GPL-3.0 en conjunto, con algunos archivos bajo licencias compatibles (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Modelar un objeto sencillo; Preparar una escena de presentación.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Aplicación Blender para tu sistema; equipo adecuado a la escena; hardware prerequisites; API de IA: no; Aplicación Blender para tu sistema; equipo adecuado a la escena.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/blender/blender/blob/main/.github/README.md
- **Primera prueba propuesta (no ejecutada):** Usa una escena nueva con un cubo y prueba mover, iluminar y renderizar una imagen Éxito: Puedes guardar el proyecto y localizar el render
- **Combina con:** `blender-mcp` [5/servidores], `3dviz-pro-max` [27/skills], `three.js` [26/animacion]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Este repositorio es un espejo del código; para utilizar Blender elige la distribución de la aplicación y no compiles todo el espejo; los conectores AI son….

### FreeCAD (`freecad`)

- **Repo:** https://github.com/FreeCAD/FreeCAD · LGPL-2.1 · nivel 1 · 71/100
- **Qué es:** Modelador 3D paramétrico de código abierto (LGPL-2.1) desarrollado por la comunidad, con financiación de la FreeCAD Project Association. Activo; versión 1.x estable.
- **Cuándo elegirlo:** Casos: diseñar una pieza mecánica paramétrica y exportarla a STL para impresión 3D; generar planos técnicos acotados a partir de un modelo 3D.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; C++, CMakeLists.txt; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/FreeCAD/FreeCAD/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala FreeCAD desde su web, crea un boceto en Part Design y extrúyelo. Éxito: Obtienes un sólido paramétrico que cambia al editar las cotas del boceto.
- **Combina con:** `openscad`, `blender`, `awesome-cad`

### filament (`filament`)

- **Repo:** https://github.com/google/filament · Apache-2.0 · nivel 2 · 69/100
- **Qué es:** Filament, motor de renderizado físicamente basado (PBR) en tiempo real de Google. Licencia Apache-2.0. Es maduro (~21k estrellas, v1.80.1).
- **Cuándo elegirlo:** Casos: Integrar un visor 3D móvil; Estudiar render físicamente basado.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Plataforma de destino; runtime y herramientas de la misma release; modelo glTF de prueba; hardware prerequisites; API de IA: no; Plataforma de destino; runtime y herramientas de la misma release; modelo glTF de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/google/filament/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre un modelo de muestra y cambia iluminación o material para observar la respuesta Éxito: Puedes distinguir geometría, material y entorno
- **Combina con:** `meshoptimizer`, `blender`, `ozz-animation`, `awesome-cad`
- **Riesgos y avisos:** Sin alternativas declaradas. El compilador de materiales y runtime deben ser de la misma versión; las dependencias Gradle son configuración del proyecto Android, no comandos de shell.

### Bevy (`bevy`)

- **Repo:** https://github.com/bevyengine/bevy · MIT OR Apache-2.0 · nivel 2 · 66/100 · alternativa en «Motores de videojuegos»
- **Qué es:** Motor de juegos de código abierto en Rust, con licencia dual MIT o Apache-2.0, impulsado por la comunidad y la Bevy Foundation. Muy activo, pero el propio README advierte que está en una fase temprana, con funciones importantes ausentes y…
- **Cuándo elegirlo:** Casos: programar un juego 2D o 3D en Rust con alto rendimiento; crear una simulación o herramienta visual que compile también a WebAssembly.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Rust, Cargo.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `cargo run --example breakout` — fuente: https://github.com/bevyengine/bevy/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio y ejecuta `cargo run --example breakout`. Éxito: Se abre el juego de ejemplo Breakout en una ventana.
- **Combina con:** `blender`, `meshoptimizer`, `claude-code` [20/terminal]
- **Alternativas:** `godot`
- **Riesgos y avisos:** Alternativa de Godot: Bevy es solo código (sin editor estable), Godot ofrece un editor completo.

### meshoptimizer (`meshoptimizer`)

- **Repo:** https://github.com/zeux/meshoptimizer · MIT · nivel 2 · 62/100
- **Qué es:** meshoptimizer, biblioteca para optimizar mallas de triángulos para GPU, de @zeux. Licencia MIT. Es madura y muy usada en la industria (~8.9k estrellas, v1.3).
- **Cuándo elegirlo:** Casos: Reducir peso de un asset 3D; Preparar mallas para render en tiempo real.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Entorno de desarrollo compatible; malla pequeña; copia del original; hardware prerequisites; API de IA: no; Entorno de desarrollo compatible; malla pequeña; copia del original.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone -b v1.3 https://github.com/zeux/meshoptimizer.git` — fuente: https://github.com/zeux/meshoptimizer/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Optimiza una malla de prueba y compara número de vértices, tamaño y apariencia Éxito: Puedes medir una reducción y detectar si cambia demasiado el detalle
- **Combina con:** `three.js` [26/animacion], `filament`, `blender`, `ozz-animation`, `regl` [26/animacion]
- **Riesgos y avisos:** Sin alternativas declaradas. Simplificar geometría implica un compromiso de detalle; conserva el original y evalúa la salida antes de reemplazar assets.

### OpenSCAD (`openscad`)

- **Repo:** https://github.com/openscad/openscad · GPL-2.0 (con excepción CGAL) · nivel 1 · 59/100
- **Qué es:** Programa libre (GPL-2.0 con excepción para CGAL) para crear modelos CAD sólidos, disponible para Linux, Windows y macOS. Muy usado en impresión 3D (p. ej. el personalizador de Thingiverse).
- **Cuándo elegirlo:** Casos: diseñar piezas paramétricas para impresión 3D cambiando variables; generar variantes de una pieza (tamaños, agujeros) desde el mismo script.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; C++, CMakeLists.txt; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/openscad/openscad/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala OpenSCAD, escribe `cube(10); translate([5,5,5]) sphere(6);`, renderiza con F6 y exporta a STL. Éxito: Obtienes un archivo STL listo para el laminador de la impresora.
- **Combina con:** `freecad`, `awesome-cad`, `claude-code` [20/terminal]

### ozz-animation (`ozz-animation`)

- **Repo:** https://github.com/guillaumeblanc/ozz-animation · MIT · nivel 2 · 42/100
- **Qué es:** ozz-animation, biblioteca C++ open source de animación esquelética 3D con herramientas, de @guillaumeblanc. El README indica licencia MIT (GitHub muestra NOASSERTION). Es madura (~3.1k estrellas, 0.17.0).
- **Cuándo elegirlo:** Casos: Reproducir animaciones de personajes; Combinar clips en un motor propio.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Entorno C++; modelo con esqueleto; herramientas de conversión compatibles; hardware prerequisites; API de IA: no; Entorno C++; modelo con esqueleto; herramientas de conversión compatibles.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/guillaumeblanc/ozz-animation/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta una muestra de reproducción y cambia el tiempo de una animación esquelética Éxito: Puedes identificar esqueleto, clip y pose
- **Combina con:** `filament`, `blender`, `meshoptimizer`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Es una biblioteca de bajo nivel independiente del motor; no crea automáticamente un personaje ni su rig.

### awesome-cad (`awesome-cad`)

- **Repo:** https://github.com/mlightcad/awesome-cad · MIT · nivel 1 · 34/100
- **Qué es:** Awesome CAD, lista curada de software, librerías y herramientas CAD open source, de mlightcad. Licencia MIT. Es reciente (enero de 2026) y de nicho (~240 estrellas).
- **Cuándo elegirlo:** Casos: Encontrar software CAD; Comparar bibliotecas de geometría.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; tipo de diseño que necesitas; hardware prerequisites; API de IA: no; Navegador; tipo de diseño que necesitas.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mlightcad/awesome-cad/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Escoge una herramienta de CAD paramétrico y otra de mallas y compara sus formatos de salida Éxito: Puedes explicar cuál se ajusta al objeto que quieres diseñar
- **Combina con:** `blender`, `three.js` [26/animacion], `filament`, `freecad`, `openscad`
- **Riesgos y avisos:** Sin alternativas declaradas. Recurso, no software. Los recursos MCP y agentes se han movido a una lista dedicada; el directorio no es por sí mismo un conector de CAD.

### Open Reality (`openreality`)

- **Repo:** https://github.com/reality-opened/openreality · BSD-2-Clause · nivel 3 · —/100
- **Qué es:** Convierte video propio en escenas 3D consultables y ofrece herramientas MCP para trabajar con la reconstrucción desde un asistente.
- **Cuándo elegirlo:** Casos: Explorar un objeto propio grabado desde varios ángulos.; Comprobar la representación 3D de un elemento de una escena de ejemplo. Evítalo si necesitas un producto autónomo y esta pieza requiere un cliente MCP.
- **Requisitos:** nivel 3: preparación media, se instala dentro de un agente (skill, plugin o MCP), necesita GPU; Python; API de IA: no; Node.js para el conector, datos propios y un servidor que pueda procesar el video; la ruta alojada y la GPU tienen requisitos aparte..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://open-reality.io/mcp
- **Primera prueba propuesta (no ejecutada):** Prueba primero un ejemplo de escena y distingue si lo procesa el servidor propio o el servicio alojado. Éxito: Puedes abrir la escena o consultar un elemento sin compartir datos privados.
- **Riesgos y avisos:** Los pesos mencionados pueden estar limitados a usos no comerciales. Alojamiento y cómputo GPU no están incluidos por instalar el conector.

### video2threejs (`video2threejs`)

- **Repo:** https://github.com/cpppppp7/video2threejs · MIT · nivel 1 · —/100
- **Qué es:** Explica con un caso cómo reconstruir la apariencia de un video como una escena navegable en Three.js.
- **Cuándo elegirlo:** Casos: Comparar el encuadre de una escena y su referencia.; Estudiar cómo combinar geometría y textura en una recreación sencilla.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; JavaScript; API de IA: no; Navegador para leer el caso y, si adaptas la técnica, una escena de prueba en Three.js..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/cpppppp7/video2threejs/blob/4c3869e2e4338283c32c56dc9f371fef371dd447/README.md
- **Primera prueba propuesta (no ejecutada):** Abre el caso y localiza un punto de vista reconstruido para compararlo con su referencia. Éxito: Puedes identificar una diferencia visible y el principio que la guía usa para reducirla.
- **Riesgos y avisos:** Es un caso técnico, no se verificó una app capaz de reconstruir cualquier clip. Revisión documental; no acredita binarios ni una instalación probada.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-26-creacion-3d.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Creación, renderizado y animación 3D», lee `docs/alexandria/categoria-26-creacion-3d.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-26-creacion-3d.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
