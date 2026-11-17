[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Animación y 3D

# 🔺 three.js

> Biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y WebGPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 118k | MIT | JavaScript | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; requiere programar con él; necesita GPU

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

three.js, biblioteca JavaScript 3D de propósito general, de @mrdoob y comunidad. Licencia MIT. Es muy madura (~119k estrellas, r187).

## ¿Qué hace?

Crea escenas 3D interactivas en el navegador con renderizadores WebGL y WebGPU (SVG y CSS3D como addons), cámaras, luces, materiales, cargadores (glTF y otros), animación y postprocesado.

## ¿Cómo lo hace?

Se instala con `npm install three` o se importa desde CDN como módulo ES. Tiene una amplia colección de ejemplos y addons.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [react-three-fiber](react-three-fiber.md) | Renderer de React para three.js. | Instala `@react-three/fiber` junto a three. |
| [GSAP](gsap.md) | Animar propiedades de objetos 3D con timelines. (combinación por arquitectura) | Anima `mesh.position` con GSAP. |
| [threejs-skills](threejs-skills.md) | Skills para que un agente programe escenas. | Añade las skills al agente. |
| [meshoptimizer](meshoptimizer.md) | Optimizar geometría glTF. | Comprime los modelos antes de cargarlos. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (20). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[3dviz-pro-max](3dviz-pro-max.md) · [Anime.js](animejs.md) · [awesome-cad](awesome-cad.md) · [blender](blender.md) · [claude-animated-shorts](claude-animated-shorts.md) · [genjutsu](genjutsu.md) · [GlobalBuildingAtlas](globalbuildingatlas.md) · [lemo-opuscar](lemo-opuscar.md) · [mediapipe](mediapipe.md) · [NiceGUI](nicegui.md) · [ODM](odm.md) · [openfilm](openfilm.md) · [planck.js](planck-js.md) · [react-three-rapier](react-three-rapier.md) · [regl](regl.md) · [tfjs-models](tfjs-models.md) · [threejs-game-skills](threejs-game-skills.md) · [webgl-noise](webgl-noise.md) · [WebODM](webodm.md) · [zdog](zdog.md)

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada r187 (2026-10-30) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mrdoob/three.js/blob/dev/README.md) · [2](https://threejs.org/docs/)</sub>

## Ver similares

Grupo **Motores 3D para la web**: three.js ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **three.js** (esta ficha) ⭐ recomendado | 69 | Si buscas esto: biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y WebGPU. |
| 2 | [Babylon.js](babylonjs.md) | 67 | Si buscas esto: motor 3D completo para la web de Microsoft y la comunidad, con física, materiales PBR, WebXR, editor de nodos y playground en línea. |
| 3 | [PlayCanvas Engine](playcanvas.md) | 65 | Si buscas esto: motor gráfico web de código abierto sobre WebGPU y WebGL2 para apps, juegos y visualizaciones 2D y 3D, con soporte de Gaussian splats y glTF. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no necesita API de IA; modelos 3D, texturas y hosting tienen licencias y costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una biblioteca y no un editor de escenas listo para usar; clonar todo el historial no es necesario para integrarla en una app |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no necesita API de IA; modelos 3D, texturas y hosting tienen licencias y costes propios |
| Equipo | Preparación según la ruta elegida. Proyecto JavaScript; servidor de desarrollo; navegador con GPU compatible |

Es una biblioteca y no un editor de escenas listo para usar; clonar todo el historial no es necesario para integrarla en una app

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto JavaScript
- servidor de desarrollo
- navegador con GPU compatible

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
git clone --depth=1 https://github.com/mrdoob/three.js.git
```

Comando copiado literalmente de el README (sección «Cloning this repository»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/mrdoob/three.js/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar three.js para mi objetivo y necesito pasos guiados. Lee https://github.com/mrdoob/three.js/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el ejemplo del cubo y cambia su color o rotación.

**Qué comprobar:** Puedes ver la escena, cámara y objeto y reconocer su relación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un visor 3D web
- Prototipar una escena interactiva

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un visor 3D web; Prototipar una escena interactiva | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca y no un editor de escenas listo para usar; clonar todo el historial no es necesario para integrarla en una app

## Stack y modelos

- **Stack:** Proyecto JavaScript; servidor de desarrollo; navegador con GPU compatible
- **Etiquetas:** `ui` `design` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Babylon.js](babylonjs.md) | 26.4k | Motor 3D completo para la web de Microsoft y la comunidad, con física, materiales PBR, WebXR, editor de nodos y playground en línea. |
| [PlayCanvas Engine](playcanvas.md) | 17.3k | Motor gráfico web de código abierto sobre WebGPU y WebGL2 para apps, juegos y visualizaciones 2D y 3D, con soporte de Gaussian splats y glTF. |

## Enlaces

- 🐙 GitHub: [mrdoob/three.js](https://github.com/mrdoob/three.js)
- 🌐 Web: <https://threejs.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mrdoob/three.js/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
