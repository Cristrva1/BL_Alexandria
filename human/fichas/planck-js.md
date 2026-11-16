[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Física y simulación

# 📚 planck.js

> Motor de física 2D para simular cuerpos, colisiones y uniones dentro de juegos o aplicaciones JavaScript.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.3k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Planck.js, reescritura en JavaScript/TypeScript del motor de física 2D Box2D, de piqnt. Licencia MIT. Es madura (~5.3k estrellas) y está activa.

## ¿Qué hace?

Simula cuerpos rígidos, colisiones, uniones y fuerzas para juegos HTML5 multiplataforma, con código legible y editable que aprovecha el diseño de Box2D.

## ¿Cómo lo hace?

Se instala con `npm install planck` (o `planck-js`) y funciona en navegador y Node. Incluye un testbed para depurar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pixelfx](pixelfx.md) | Efectos visuales para juegos con física. (combinación por arquitectura) | Combina en el mismo juego. |
| [threejs-game-skills](threejs-game-skills.md) | Juegos de navegador asistidos por agente. (combinación por arquitectura) | Usa Planck para la física 2D. |
| [three.js](three-js.md) | Simular física 2D y dibujar el resultado en una escena three.js (por ejemplo, con cámara ortográfica). (combinación por arquitectura) | Actualiza las posiciones de las mallas desde el paso de simulación de Planck. |
| [PixiJS](pixijs.md) | Combinación recíproca: PixiJS lo enlaza como «Planck.js simula física 2D y PixiJS puede dibujar sus cuerpos (combinación por arquitectura)». | Orden indicado desde PixiJS: Calcula la física con Planck.js; después sincroniza las posiciones de los sprites en cada fotograma. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-14 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/piqnt/planck.js/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita modelos ni API; hosting y assets se costean aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un motor de física 2D basado en Box2D y corresponde a simulación; no genera animaciones por instrucciones de IA |
| Coste | Sin pago a un modelo en la ruta básica. No necesita modelos ni API; hosting y assets se costean aparte |
| Equipo | Preparación según la ruta elegida. Proyecto JavaScript; escena 2D de prueba |

Es un motor de física 2D basado en Box2D y corresponde a simulación; no genera animaciones por instrucciones de IA

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto JavaScript
- escena 2D de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://piqnt.com/planck.js/docs/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar planck.js para mi objetivo y necesito pasos guiados. Lee https://piqnt.com/planck.js/docs/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una demo de un cuerpo que cae y modifica gravedad o rebote.

**Qué comprobar:** Puedes observar colisión y estado del cuerpo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar física de un juego 2D
- Explicar gravedad con una simulación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar física de un juego 2D; Explicar gravedad con una simulación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un motor de física 2D basado en Box2D y corresponde a simulación; no genera animaciones por instrucciones de IA

## Stack y modelos

- **Stack:** Proyecto JavaScript; escena 2D de prueba
- **Etiquetas:** `animacion` `library` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [piqnt/planck.js](https://github.com/piqnt/planck.js)
- 🌐 Web: <http://piqnt.com/planck.js/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría corregida en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/piqnt/planck.js/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
