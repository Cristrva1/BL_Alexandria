# Alexandría para agentes · Física y simulación

Categoría 26 «Animación, gráficos y creación 3D» › subcategoría `simulacion`. 7 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=26&sub=simulacion · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `genesis-world` | Plataforma de simulación para IA física y robótica con motor multifísica… | 3 Avanzado | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `mujoco` | Motor de física de Google DeepMind para simular estructuras articuladas con… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `warp` | Framework de NVIDIA para kernels y simulación física en CPU o GPU; no es un… | 3 Avanzado | 68 | Apache-2.0 (OSI permisiva) | sin grupo |
| `planck-js` | Motor de física 2D para simular cuerpos, colisiones y uniones dentro de juegos… | 2 Intermedio | 56 | MIT (OSI permisiva) | sin grupo |
| `react-three-rapier` | Integración del motor de física Rapier con React Three Fiber para añadir… | 2 Intermedio | 47 | MIT (OSI permisiva) | sin grupo |
| `motionbricks` | Genera movimiento de personajes a partir de poses y objetivos mediante modelos… | 3 Avanzado | — | Apache-2.0 | sin grupo |
| `robotics-antigravity-plugin` | Añade a Antigravity instrucciones para crear, probar y observar escenas de… | 2 Intermedio | — | Apache-2.0 | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Genesis World (`genesis-world`)

- **Repo:** https://github.com/Genesis-Embodied-AI/genesis-world · Apache-2.0 · nivel 3 · 74/100
- **Qué es:** Plataforma de simulación de código abierto (Apache-2.0), antes llamada Genesis, que nació como proyecto académico en diciembre de 2024 y ahora cuenta con el apoyo de la empresa Genesis AI. Muy activa (Genesis World 1.0).
- **Cuándo elegirlo:** Casos: entrenar políticas de robots con miles de entornos paralelos en GPU; generar datos sintéticos de manipulación con cuerpos rígidos y deformables.
- **Requisitos:** nivel 3: pip install; simulación física con GPU; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install genesis-world` — fuente: https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala PyTorch y después `pip install genesis-world`; ejecuta el ejemplo `examples/rigid/single_franka.py`. Éxito: Se simula un brazo Franka en una escena con visor.
- **Combina con:** `pytorch` [24/entrenamiento], `mujoco`, `blender` [26/creacion-3d]
- **Riesgos y avisos:** Simulador cercano a MuJoCo e Isaac; Genesis prioriza multifísica y paralelismo en GPU.

### MuJoCo (`mujoco`)

- **Repo:** https://github.com/google-deepmind/mujoco · Apache-2.0 · nivel 2 · 74/100
- **Qué es:** Motor de física de código abierto (Apache-2.0) mantenido por Google DeepMind, que lo adquirió en 2021 y lo liberó en 2022. Referencia en investigación de robótica y aprendizaje por refuerzo. Muy activo.
- **Cuándo elegirlo:** Casos: simular un robot o un brazo para probar controladores antes del hardware; entrenar políticas de aprendizaje por refuerzo en entornos físicos.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; C++, CMakeLists.txt; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install mujoco` — fuente: https://github.com/google-deepmind/mujoco/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install mujoco`, carga un modelo MJCF de ejemplo y ábrelo con `python -m mujoco.viewer`. Éxito: Ves el modelo simulado en el visor interactivo.
- **Combina con:** `jax` [24/entrenamiento], `warp`, `genesis-world`

### warp (`warp`)

- **Repo:** https://github.com/NVIDIA/warp · Apache-2.0 · nivel 3 · 68/100
- **Qué es:** NVIDIA Warp, framework Python para simulación, robótica y ML acelerados por GPU. Licencia Apache-2.0. Es maduro (~7.3k estrellas, v1.19.0).
- **Cuándo elegirlo:** Casos: Estudiar simulación física; Prototipar cómputo para robótica.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él; Python 3.11+; CPU o GPU soportada; ejemplo pequeño; hardware prerequisites; API de IA: no; Python 3.11+; CPU o GPU soportada; ejemplo pequeño.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install warp-lang` — fuente: https://github.com/NVIDIA/warp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta una simulación de ejemplo con pocas partículas y revisa su evolución Éxito: Puedes identificar kernel, dispositivo y estado simulado
- **Combina con:** `pytorch` [24/entrenamiento], `blender` [26/creacion-3d], `cosmos` [24/modelos], `mujoco`
- **Riesgos y avisos:** Sin alternativas declaradas. NVIDIA Warp es un framework de kernels y simulación, no el terminal Warp ni un modelo conversacional; corresponde mejor a simulación y gráficos que a….

### planck.js (`planck-js`)

- **Repo:** https://github.com/piqnt/planck.js · MIT · nivel 2 · 56/100
- **Qué es:** Planck.js, reescritura en JavaScript/TypeScript del motor de física 2D Box2D, de piqnt. Licencia MIT. Es madura (~5.3k estrellas) y está activa.
- **Cuándo elegirlo:** Casos: Prototipar física de un juego 2D; Explicar gravedad con una simulación.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Proyecto JavaScript; escena 2D de prueba; hardware prerequisites; API de IA: no; Proyecto JavaScript; escena 2D de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install planck` — fuente: https://github.com/piqnt/planck.js/blob/master/docs/pages/install.md
- **Primera prueba propuesta (no ejecutada):** Abre una demo de un cuerpo que cae y modifica gravedad o rebote Éxito: Puedes observar colisión y estado del cuerpo
- **Combina con:** `pixelfx` [26/animacion], `threejs-game-skills` [27/skills], `three.js` [26/animacion], `pixijs` [26/animacion]
- **Riesgos y avisos:** Sin alternativas declaradas. Es un motor de física 2D basado en Box2D y corresponde a simulación; no genera animaciones por instrucciones de IA.

### react-three-rapier (`react-three-rapier`)

- **Repo:** https://github.com/pmndrs/react-three-rapier · MIT · nivel 2 · 47/100
- **Qué es:** @react-three/rapier, wrapper del motor de física Rapier (WASM) para react-three-fiber, de pmndrs. Licencia MIT. Tiene ~1.7k estrellas (v2.2.0).
- **Cuándo elegirlo:** Casos: Crear una escena física React; Prototipar interacción con objetos 3D.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; React y Fiber compatibles; escena 3D; Rapier; hardware prerequisites; API de IA: no; React y Fiber compatibles; escena 3D; Rapier.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/pmndrs/react-three-rapier/blob/main/readme.md
- **Primera prueba propuesta (no ejecutada):** Añade un cuerpo y un suelo con debug visible y comprueba la colisión Éxito: Puedes relacionar collider, geometría y movimiento
- **Combina con:** `react-three-fiber` [26/animacion], `three.js` [26/animacion], `threejs-game-skills` [27/skills]
- **Riesgos y avisos:** Sin alternativas declaradas. La versión 2 documenta React 19 y Fiber 9, mientras React 18 requiere la versión 1 y Fiber 8; no mezcles las líneas de versiones.

### MotionBricks (`motionbricks`)

- **Repo:** https://github.com/NVlabs/motionbricks · Apache-2.0 · nivel 3 · —/100
- **Qué es:** Genera movimiento de personajes a partir de poses y objetivos mediante modelos locales y una escena de demostración.
- **Cuándo elegirlo:** Casos: Completar fotogramas entre dos poses de un personaje de prueba.; Comparar un giro de personaje con dos recorridos virtuales. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; GPU NVIDIA con TensorRT, entorno x86-64 compatible y pesos para el ejemplo. Las pruebas del autor se hicieron con RTX 4090..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/NVlabs/motionbricks/blob/54fc563aeaaf819a753d72cc9fdc6713989cdd43/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue Setup y abre el ejemplo de poses recomendado con sus pesos autorizados. Éxito: Ves el movimiento entre las poses y puedes revisar cambios de trayectoria.
- **Riesgos y avisos:** El código, los modelos y los movimientos de ejemplo tienen licencias diferentes; revisa la tabla del README antes de usar o redistribuir.

### Robotics for Antigravity (`robotics-antigravity-plugin`)

- **Repo:** https://github.com/google-deepmind/robotics-antigravity-plugin · Apache-2.0 · nivel 2 · —/100
- **Qué es:** Añade a Antigravity instrucciones para crear, probar y observar escenas de robótica con flujos como la simulación en MuJoCo.
- **Cuándo elegirlo:** Casos: Abrir un escenario de simulación y cambiar la posición de un objeto virtual.; Documentar cómo medir el recorrido de un brazo virtual en una escena de ejemplo. Evítalo si no usas un agente compatible con skills.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Python; API de IA: depends; Antigravity, dependencias de simulación indicadas y una escena de ejemplo sin robot físico..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/google-deepmind/robotics-antigravity-plugin/blob/3dde33820355c70fe8d8e33e42707cdcb742ceb4/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona un ejemplo de solo simulación y revisa qué herramientas pide antes de autorizarlo. Éxito: Se observa el comportamiento de la escena virtual y queda un resultado que puedes comparar.
- **Riesgos y avisos:** Gemini API, hardware y componentes externos pueden tener costes y requisitos aparte. Alcance de la ficha: simulación, sin control de hardware.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-26-simulacion.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Física y simulación», lee `docs/alexandria/categoria-26-simulacion.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-26-simulacion.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
