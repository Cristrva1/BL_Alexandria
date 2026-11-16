[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Animación y 3D

# 📚 Babylon.js

> Motor 3D completo para la web de Microsoft y la comunidad, con física, materiales PBR, WebXR, editor de nodos y playground en línea.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.4k | Apache-2.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor 3D de código abierto (Apache-2.0) creado en Microsoft y mantenido con la comunidad. Maduro y activo, con playground, sandbox y foro oficiales.

## ¿Qué hace?

Permite crear escenas y juegos 3D en el navegador: materiales PBR, luces y sombras, animación y esqueletos, partículas, física, GUI, audio espacial, WebXR, editores visuales de nodos (materiales, partículas, GUI) e inspector de depuración.

## ¿Cómo lo hace?

Se instala con npm (paquetes UMD o ES6 con tree shaking) o se prueba en el playground. Renderiza con WebGL o WebGPU y carga glTF, OBJ, STL y su formato .babylon; el exportador para Blender genera archivos .babylon.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [blender](blender.md) | Babylon.js mantiene un exportador para Blender que genera archivos .babylon; también carga glTF exportado desde Blender. | Exporta la escena desde Blender (glTF o exportador .babylon); después cárgala con `SceneLoader`. |
| [meshoptimizer](meshoptimizer.md) | El cargador glTF de Babylon.js admite la extensión EXT_meshopt_compression para mallas comprimidas con meshoptimizer. | Comprime el glTF con gltfpack/meshoptimizer; después cárgalo con el cargador glTF de Babylon.js. |
| [GSAP](gsap.md) | GSAP puede animar propiedades de objetos de Babylon.js como cualquier objeto JavaScript (combinación por arquitectura). | Crea la escena con Babylon.js; después anima posiciones o materiales con `gsap.to`. |

**Notas:** Alternativa de three.js y PlayCanvas: más "todo incluido" que three.js.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 9.36.0 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/BabylonJS/Babylon.js/blob/master/readme.md) · [2](https://github.com/BabylonJS/Babylon.js/tree/master/packages/dev/loaders/src/glTF/2.0/Extensions) · [3](https://github.com/BabylonJS/BlenderExporter)</sub>

## Ver similares

Grupo **Motores 3D para la web**: Babylon.js ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [three.js](three-js.md) ⭐ recomendado | 69 | Si buscas esto: biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y WebGPU. |
| 2 | **Babylon.js** (esta ficha) | 67 | Si buscas esto: motor 3D completo para la web de Microsoft y la comunidad, con física, materiales PBR, WebXR, editor de nodos y playground en línea. |
| 3 | [PlayCanvas Engine](playcanvas.md) | 65 | Si buscas esto: motor gráfico web de código abierto sobre WebGPU y WebGL2 para apps, juegos y visualizaciones 2D y 3D, con soporte de Gaussian splats y glTF. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
npm install babylonjs --save
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/BabylonJS/Babylon.js/blob/master/readme.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Babylon.js para mi objetivo y necesito pasos guiados. Lee https://github.com/BabylonJS/Babylon.js/blob/master/readme.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre el playground oficial, carga un ejemplo y modifícalo; o instala con `npm install babylonjs --save`..

**Qué comprobar:** La escena 3D se renderiza en el navegador con tus cambios..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- mostrar un configurador de producto 3D en una web
- crear un juego o experiencia WebXR en el navegador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: mostrar un configurador de producto 3D en una web; crear un juego o experiencia WebXR en el navegador | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `javascript` `3d` `webgl` `webxr`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [three.js](three-js.md) | 118k | Biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y WebGPU. |
| [PlayCanvas Engine](playcanvas.md) | 17.3k | Motor gráfico web de código abierto sobre WebGPU y WebGL2 para apps, juegos y visualizaciones 2D y 3D, con soporte de Gaussian splats y glTF. |

## Enlaces

- 🐙 GitHub: [BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js)
- 🌐 Web: <http://www.babylonjs.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/BabylonJS/Babylon.js/blob/master/readme.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
