[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Creación, renderizado y animación 3D

# 🖥️ blender

> Código de Blender, la aplicación para modelar, animar, renderizar y editar escenas y contenido tridimensional.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 22k | NOASSERTION | C++ | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Blender, suite libre de creación 3D, de la Blender Foundation. Licencia GPL-3.0 en conjunto, con algunos archivos bajo licencias compatibles (GitHub muestra NOASSERTION). El repo de GitHub es un espejo del desarrollo oficial, con ~22k estrellas.

## ¿Qué hace?

Cubre modelado, escultura, rigging, animación, simulación, render (Cycles y EEVEE), composición, edición de vídeo y Grease Pencil, y es extensible con Python.

## ¿Cómo lo hace?

Los binarios se descargan de blender.org. Para compilar desde el espejo hay que clonar con `GIT_LFS_SKIP_SMUDGE=1` para evitar errores de LFS.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Blender MCP](blender-mcp.md) | Controlar Blender desde un agente vía MCP. | Instala el addon y el servidor MCP. |
| [3dviz-pro-max](3dviz-pro-max.md) | Skill de escenas 3D con Blender. | Añade la skill al agente. |
| [three.js](three-js.md) | Exportar a glTF para la web. (combinación por arquitectura) | Exporta glTF desde Blender. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (16). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[4D-Humans](4d-humans.md) · [awesome-cad](awesome-cad.md) · [blender-skills](blender-skills.md) · [ChatDev](chatdev.md) · [dream-loop](dream-loop.md) · [EasyMocap](easymocap.md) · [filament](filament.md) · [meshoptimizer](meshoptimizer.md) · [ODM](odm.md) · [OpenRV](openrv.md) · [ozz-animation](ozz-animation.md) · [pencil](pencil.md) · [unity-mcp](unity-mcp.md) · [warp](warp.md) · [WebODM](webodm.md) · [WHAM](wham.md)

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/blender/blender/blob/main/.github/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La app no exige API de IA; assets, plugins, render en nube y hardware tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Este repositorio es un espejo del código; para utilizar Blender elige la distribución de la aplicación y no compiles todo el espejo; los conectores AI son otros proyectos |
| Coste | Sin pago a un modelo en la ruta básica. La app no exige API de IA; assets, plugins, render en nube y hardware tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Aplicación Blender para tu sistema; equipo adecuado a la escena |

Este repositorio es un espejo del código; para utilizar Blender elige la distribución de la aplicación y no compiles todo el espejo; los conectores AI son otros proyectos

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Aplicación Blender para tu sistema
- equipo adecuado a la escena

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/blender/blender/blob/main/.github/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar blender para mi objetivo y necesito pasos guiados. Lee https://github.com/blender/blender/blob/main/.github/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa una escena nueva con un cubo y prueba mover, iluminar y renderizar una imagen.

**Qué comprobar:** Puedes guardar el proyecto y localizar el render.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Modelar un objeto sencillo
- Preparar una escena de presentación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Modelar un objeto sencillo; Preparar una escena de presentación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Este repositorio es un espejo del código; para utilizar Blender elige la distribución de la aplicación y no compiles todo el espejo; los conectores AI son otros proyectos

## Stack y modelos

- **Stack:** Aplicación Blender para tu sistema; equipo adecuado a la escena
- **Etiquetas:** `creacion-3d` `app` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [blender/blender](https://github.com/blender/blender)
- 🌐 Web: <https://developer.blender.org/docs/handbook/contributing/using_git/#github-mirror>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/blender/blender/blob/main/.github/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
