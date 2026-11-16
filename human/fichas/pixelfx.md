[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Animación y 3D

# 📚 pixelfx

> Colección de efectos de pixel art hechos con código y una skill para ayudar a generar efectos propios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.5k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

pixelfx, colección de 244 efectos y animaciones de pixel art hechos con código, de patch-gg. Licencia MIT. Es muy reciente (octubre de 2026) y ya tiene ~7.6k estrellas.

## ¿Qué hace?

Ofrece efectos de fuego, explosiones, magia, clima, UI, objetos recogibles, criaturas y más, que se reproducen en vivo, se recolorean y se exportan como sprite sheets para cualquier motor. Incluye una skill de Claude Code para crear efectos nuevos con un ciclo de borrador, render, revisión y refinado.

## ¿Cómo lo hace?

Se instala con `npm i github:patch-gg/pixelfx` o copiando `src/core` y los efectos deseados. También funciona como bloque en Patch (patch.gg), cuya CLI se promociona en el README.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Skill para generar efectos nuevos. | Instala la skill del repo. |
| [threejs-game-skills](threejs-game-skills.md) | Efectos para juegos de navegador. (combinación por arquitectura) | Integra los sprite sheets en el juego. |
| [planck.js](planck-js.md) | Física 2D para el juego que usa los efectos. (combinación por arquitectura) | Combina en el mismo juego. |
| [pencil](pencil.md) | Combinación recíproca: pencil lo enlaza como «Efectos de pixel art de referencia. (combinación por arquitectura)». | Orden indicado desde pencil: Usa los sprite sheets como guía. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-13 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/patch-gg/pixelfx/blob/main/README.md) · [2](https://patch-gg.github.io/pixelfx/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Los efectos básicos no requieren modelo; crear nuevos con el skill usa el agente y publicar con Patch tiene condiciones propias |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Documenta plugin de Claude Code; no es necesario publicar el juego para usar o estudiar un efecto existente |
| Coste | El coste depende del proveedor o la ruta. Los efectos básicos no requieren modelo; crear nuevos con el skill usa el agente y publicar con Patch tiene condiciones propias |
| Equipo | Preparación según la ruta elegida. Proyecto JavaScript o motor que admita sprites; Claude Code opcional |

Documenta plugin de Claude Code; no es necesario publicar el juego para usar o estudiar un efecto existente

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto JavaScript o motor que admita sprites
- Claude Code opcional

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/patch-gg/pixelfx/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pixelfx para mi objetivo y necesito pasos guiados. Lee https://github.com/patch-gg/pixelfx/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un efecto existente y cambia tamaño o paleta antes de pedir generar uno nuevo.

**Qué comprobar:** Puedes inspeccionar frames y exportar una muestra.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Añadir un efecto a un juego
- Preparar una hoja de sprites

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Añadir un efecto a un juego; Preparar una hoja de sprites | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta plugin de Claude Code; no es necesario publicar el juego para usar o estudiar un efecto existente

## Stack y modelos

- **Stack:** Proyecto JavaScript o motor que admita sprites; Claude Code opcional
- **Etiquetas:** `animacion` `library` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)
- 🌐 Web: <https://patch-gg.github.io/pixelfx/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/patch-gg/pixelfx/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
