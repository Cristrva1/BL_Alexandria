[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Creación, renderizado y animación 3D

# 📚 filament

> Motor de renderizado físicamente basado para integrar gráficos 3D en aplicaciones móviles, web y de escritorio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 20.7k | Apache-2.0 | C++ | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Filament, motor de renderizado físicamente basado (PBR) en tiempo real de Google. Licencia Apache-2.0. Es maduro (~21k estrellas, v1.80.1).

## ¿Qué hace?

Renderiza en Android, iOS, Linux, macOS, Windows y WebAssembly con materiales PBR, iluminación basada en imagen, sombras y postprocesado, priorizando tamaño y eficiencia en Android. Incluye un visor y una librería glTF (gltfio).

## ¿Cómo lo hace?

Se descargan las releases estables o se compila con CMake. Soporta Vulkan, Metal, OpenGL y WebGL, y trae herramientas como `matc` (compilador de materiales) y `cmgen` (mapas de entorno).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [meshoptimizer](meshoptimizer.md) | Optimizar geometría glTF antes de cargarla. (combinación por arquitectura) | Procesa los modelos con gltfpack. |
| [blender](blender.md) | Exportar modelos glTF. (combinación por arquitectura) | Exporta desde Blender y carga con gltfio. |
| [ozz-animation](ozz-animation.md) | Animación esquelética en runtime. (combinación por arquitectura) | Integra ozz en el motor. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.80.1 (2026-11-11) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google/filament/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API de IA; recursos, hardware y distribución tienen costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El compilador de materiales y runtime deben ser de la misma versión; las dependencias Gradle son configuración del proyecto Android, no comandos de shell |
| Coste | Sin pago a un modelo en la ruta básica. No necesita API de IA; recursos, hardware y distribución tienen costes propios |
| Equipo | Preparación según la ruta elegida. Plataforma de destino; runtime y herramientas de la misma release; modelo glTF de prueba |

El compilador de materiales y runtime deben ser de la misma versión; las dependencias Gradle son configuración del proyecto Android, no comandos de shell

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Plataforma de destino
- runtime y herramientas de la misma release
- modelo glTF de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google/filament/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar filament para mi objetivo y necesito pasos guiados. Lee https://github.com/google/filament/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un modelo de muestra y cambia iluminación o material para observar la respuesta.

**Qué comprobar:** Puedes distinguir geometría, material y entorno.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Integrar un visor 3D móvil
- Estudiar render físicamente basado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Integrar un visor 3D móvil; Estudiar render físicamente basado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El compilador de materiales y runtime deben ser de la misma versión; las dependencias Gradle son configuración del proyecto Android, no comandos de shell

## Stack y modelos

- **Stack:** Plataforma de destino; runtime y herramientas de la misma release; modelo glTF de prueba
- **Etiquetas:** `creacion-3d` `library` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google/filament](https://github.com/google/filament)
- 🌐 Web: <https://google.github.io/filament/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google/filament/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
