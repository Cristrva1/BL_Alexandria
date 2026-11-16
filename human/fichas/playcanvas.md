[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Animación y 3D

# 📚 PlayCanvas Engine

> Motor gráfico web de código abierto sobre WebGPU y WebGL2 para apps, juegos y visualizaciones 2D y 3D, con soporte de Gaussian splats y glTF.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.3k | MIT | JavaScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor gráfico de código abierto (MIT) de PlayCanvas (propiedad de Snap Inc.). Lo acompañan un editor colaborativo en la nube (servicio con planes) y herramientas como SuperSplat. Activo.

## ¿Qué hace?

Crea aplicaciones, juegos y visualizaciones 2D y 3D en el navegador: grafo de entidades y componentes, materiales PBR, animación, física rígida con ammo.js, audio, XR, entrada y carga de glTF, texturas comprimidas y Gaussian splats (PLY y SOG).

## ¿Cómo lo hace?

Se instala con npm o se crea un proyecto con `create-playcanvas`. Prefiere WebGPU y cae a WebGL2. El parser glTF incluye decodificadores Draco y meshopt.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [meshoptimizer](meshoptimizer.md) | El cargador glTF de PlayCanvas incluye un decodificador para mallas comprimidas con meshoptimizer (EXT_meshopt_compression). | Comprime el modelo con gltfpack/meshoptimizer; después cárgalo como asset glTF en PlayCanvas. |
| [blender](blender.md) | PlayCanvas carga modelos glTF/GLB, el formato que Blender exporta de forma nativa (combinación por arquitectura). | Exporta el modelo desde Blender a GLB; después cárgalo en PlayCanvas. |
| [GSAP](gsap.md) | GSAP puede animar propiedades de entidades de PlayCanvas como cualquier objeto JavaScript (combinación por arquitectura). | Crea las entidades en PlayCanvas; después anima sus valores con `gsap.to`. |

**Notas:** Alternativa de three.js y Babylon.js; destaca en carga ligera y visualización de Gaussian splats.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.24.1 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/playcanvas/engine/blob/main/README.md) · [2](https://github.com/playcanvas/engine/tree/main/src/framework/parsers)</sub>

## Ver similares

Grupo **Motores 3D para la web**: PlayCanvas Engine ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [three.js](three-js.md) ⭐ recomendado | 69 | Si buscas esto: biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y WebGPU. |
| 2 | [Babylon.js](babylonjs.md) | 67 | Si buscas esto: motor 3D completo para la web de Microsoft y la comunidad, con física, materiales PBR, WebXR, editor de nodos y playground en línea. |
| 3 | **PlayCanvas Engine** (esta ficha) | 65 | Si buscas esto: motor gráfico web de código abierto sobre WebGPU y WebGL2 para apps, juegos y visualizaciones 2D y 3D, con soporte de Gaussian splats y glTF. |

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
npm install playcanvas
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/playcanvas/engine/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PlayCanvas Engine para mi objetivo y necesito pasos guiados. Lee https://github.com/playcanvas/engine/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un proyecto con `npm create playcanvas@latest` o instala `npm install playcanvas` y ejecuta el ejemplo del cubo giratorio..

**Qué comprobar:** El cubo 3D gira en un canvas del navegador..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- publicar una escena 3D o un escaneo con Gaussian splats en una web
- crear un juego ligero que funcione en cualquier navegador y móvil

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: publicar una escena 3D o un escaneo con Gaussian splats en una web; crear un juego ligero que funcione en cualquier navegador y móvil | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. El motor es MIT; el editor en la nube de PlayCanvas es un servicio con planes de pago.

## Stack y modelos

- **Stack:** JavaScript, package.json
- **Etiquetas:** `javascript` `3d` `webgpu` `gamedev`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [three.js](three-js.md) | 118k | Biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y WebGPU. |
| [Babylon.js](babylonjs.md) | 26.4k | Motor 3D completo para la web de Microsoft y la comunidad, con física, materiales PBR, WebXR, editor de nodos y playground en línea. |

## Enlaces

- 🐙 GitHub: [playcanvas/engine](https://github.com/playcanvas/engine)
- 🌐 Web: <https://playcanvas.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/playcanvas/engine/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
