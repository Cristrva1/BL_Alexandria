[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Creación, renderizado y animación 3D

# 🖥️ Godot Engine

> Motor de videojuegos 2D y 3D libre (MIT) con editor integrado, scripting en GDScript o C# y exportación a escritorio, móvil, web y consolas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 120k | MIT | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — instalación simple, pero crear juegos exige aprender el motor y GDScript · corregido a mano

**Puntuación de calidad** 77/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de juegos de código abierto (MIT), sin regalías, desarrollado por la comunidad y respaldado por la Godot Foundation (sin ánimo de lucro). El motor libre más popular; muy activo.

## ¿Qué hace?

Ofrece un editor unificado para juegos 2D y 3D: escenas y nodos, scripting en GDScript, C# o extensiones nativas (GDExtension), animación, física (incluye Jolt), audio, interfaz, red, navegación y XR. Exporta con un clic a Linux, macOS, Windows, Android, iOS y web; las consolas requieren socios externos.

## ¿Cómo lo hace?

Está escrito en C++ con renderizadores Vulkan, Direct3D 12 y OpenGL. Importa glTF, FBX y archivos .blend (usando Blender instalado). Se descarga como un ejecutable ligero; también se compila desde el código con SCons.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [blender](blender.md) | Godot importa directamente archivos .blend llamando a Blender instalado para convertirlos a glTF. | Instala Blender e indica su ruta en la configuración del editor de Godot; después arrastra el .blend al proyecto. |
| [meshoptimizer](meshoptimizer.md) | Godot incluye meshoptimizer (en thirdparty) para generar niveles de detalle (LOD) de las mallas importadas. | No requiere instalación aparte: viene integrado en el importador de Godot. |
| [FFmpeg](ffmpeg.md) | El modo Movie Maker de Godot graba AVI o secuencias PNG/WAV, y la documentación recomienda FFmpeg para convertirlos a otros formatos. | Graba con Movie Maker en Godot; después convierte el resultado con FFmpeg. |

**Notas:** Alternativa de Bevy (motor en Rust con ECS y sin editor visual completo).

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada 4.7.2-stable (2026-08-18) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/godotengine/godot/blob/master/README.md) · [2](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html) · [3](https://docs.godotengine.org/en/stable/tutorials/animation/creating_movies.html) · [4](https://github.com/godotengine/godot/tree/master/thirdparty)</sub>

## Ver similares

Grupo **Motores de videojuegos**: Godot Engine ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Godot Engine** (esta ficha) ⭐ recomendado | 77 | Si buscas esto: motor de videojuegos 2D y 3D libre (MIT) con editor integrado, scripting en GDScript o C# y exportación a escritorio, móvil, web y consolas. |
| 2 | [Bevy](bevy.md) | 66 | Si buscas esto: motor de juegos en Rust basado en datos y en el patrón ECS, libre (MIT o Apache-2.0), modular y con funciones 2D y 3D para juegos y simulaciones. |

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

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una copia de datos o archivos para la primera prueba.

1. Abre las descargas o la web de la aplicación enlazadas por el autor; elige la versión para tu sistema.
2. Sigue su guía de inicio y configura únicamente la función que necesitas probar.
3. Abre un archivo o caso pequeño, guarda un resultado y comprueba que puedes recuperarlo antes de importar material real.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/godotengine/godot/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://godotengine.org)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Godot Engine para mi objetivo y necesito pasos guiados. Lee https://github.com/godotengine/godot/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga Godot desde su web, abre un proyecto de las demos oficiales y ejecútalo con F5..

**Qué comprobar:** La demo se ejecuta en una ventana y puedes modificar sus escenas en el editor..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- crear un juego 2D o 3D y exportarlo a Windows, Android y web
- construir una visualización interactiva o una simulación con editor visual

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: crear un juego 2D o 3D y exportarlo a Windows, Android y web; construir una visualización interactiva o una simulación con editor visual | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C++, pyproject.toml
- **Etiquetas:** `gamedev` `3d` `2d` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Bevy](bevy.md) | 49.8k | Motor de juegos en Rust basado en datos y en el patrón ECS, libre (MIT o Apache-2.0), modular y con funciones 2D y 3D para juegos y simulaciones. |

## Enlaces

- 🐙 GitHub: [godotengine/godot](https://github.com/godotengine/godot)
- 🌐 Web: <https://godotengine.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/godotengine/godot/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
