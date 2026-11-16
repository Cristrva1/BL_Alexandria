[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Creación, renderizado y animación 3D

# 📚 Bevy

> Motor de juegos en Rust basado en datos y en el patrón ECS, libre (MIT o Apache-2.0), modular y con funciones 2D y 3D para juegos y simulaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 49.8k | MIT OR Apache-2.0 | Rust | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de juegos de código abierto en Rust, con licencia dual MIT o Apache-2.0, impulsado por la comunidad y la Bevy Foundation. Muy activo, pero el propio README advierte que está en una fase temprana, con funciones importantes ausentes y cambios incompatibles en cada versión.

## ¿Qué hace?

Ofrece un conjunto completo de funciones 2D y 3D: ECS paralelo, renderizado PBR, animación, interfaz, audio, entrada, escenas, recursos con recarga en caliente y despliegue a escritorio, web (WebAssembly/WebGPU) y móvil.

## ¿Cómo lo hace?

Se usa como dependencia de Cargo en un proyecto Rust. La lógica se escribe como sistemas que operan sobre componentes; el renderizado usa wgpu. Carga glTF de forma nativa. La versión mínima de Rust suele ser la última estable.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [blender](blender.md) | Bevy carga escenas glTF, el formato que Blender exporta de forma nativa, y la comunidad lo usa como herramienta de contenido. | Exporta el modelo desde Blender a glTF/GLB; después cárgalo con `AssetServer` en Bevy. |
| [meshoptimizer](meshoptimizer.md) | La función de geometría virtual (meshlets) de Bevy usa el crate meshopt, enlace de meshoptimizer, para preparar las mallas. | Activa la feature `meshlet_processor` de Bevy; después convierte las mallas en meshlets. |
| [Claude Code](claude-code.md) | Un proyecto Bevy es código Rust y archivos de recursos, que un agente de código puede editar y compilar con cargo (combinación por arquitectura). | Crea el proyecto con cargo; después pide cambios al agente y compílalos con `cargo run`. |

**Notas:** Alternativa de Godot: Bevy es solo código (sin editor estable), Godot ofrece un editor completo.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.20.1 (2026-10-28) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/bevyengine/bevy/blob/main/README.md) · [2](https://github.com/bevyengine/bevy/blob/main/crates/bevy_pbr/Cargo.toml)</sub>

## Ver similares

Grupo **Motores de videojuegos**: Bevy ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Godot Engine](godot.md) ⭐ recomendado | 77 | Si buscas esto: motor de videojuegos 2D y 3D libre (MIT) con editor integrado, scripting en GDScript o C# y exportación a escritorio, móvil, web y consolas. |
| 2 | **Bevy** (esta ficha) | 66 | Si buscas esto: motor de juegos en Rust basado en datos y en el patrón ECS, libre (MIT o Apache-2.0), modular y con funciones 2D y 3D para juegos y simulaciones. |

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
cargo run --example breakout
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/bevyengine/bevy/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Bevy para mi objetivo y necesito pasos guiados. Lee https://github.com/bevyengine/bevy/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona el repositorio y ejecuta `cargo run --example breakout`..

**Qué comprobar:** Se abre el juego de ejemplo Breakout en una ventana..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- programar un juego 2D o 3D en Rust con alto rendimiento
- crear una simulación o herramienta visual que compile también a WebAssembly

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: programar un juego 2D o 3D en Rust con alto rendimiento; crear una simulación o herramienta visual que compile también a WebAssembly | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Proyecto en fase temprana: publica versiones con cambios incompatibles aproximadamente cada tres meses y no tiene editor visual estable.

## Stack y modelos

- **Stack:** Rust, Cargo.toml
- **Etiquetas:** `rust` `gamedev` `ecs` `3d`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Godot Engine](godot.md) | 120k | Motor de videojuegos 2D y 3D libre (MIT) con editor integrado, scripting en GDScript o C# y exportación a escritorio, móvil, web y consolas. |

## Enlaces

- 🐙 GitHub: [bevyengine/bevy](https://github.com/bevyengine/bevy)
- 🌐 Web: <https://bevy.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/bevyengine/bevy/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
