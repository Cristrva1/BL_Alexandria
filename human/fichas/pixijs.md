[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Animación y 3D

# 📚 PixiJS

> Motor de renderizado 2D para la web sobre WebGL y WebGPU, muy rápido, para juegos, gráficos interactivos y aplicaciones visuales en el navegador.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 48.7k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (MIT) para gráficos 2D en la web, una de las más usadas para juegos y experiencias interactivas en navegador. Activa (v8 con WebGPU).

## ¿Qué hace?

Renderiza escenas 2D con sprites, texto, gráficos vectoriales y SVG, texturas dinámicas, máscaras, filtros y modos de fusión, con soporte de ratón y multitáctil y un cargador de recursos. Sirve para juegos, anuncios interactivos, visualizaciones y apps.

## ¿Cómo lo hace?

Se instala con npm (`pixi.js`) o se crea un proyecto con `npm create pixi.js@latest`. Usa un grafo de escena y renderizadores WebGL o WebGPU con agrupación de dibujado para alto rendimiento.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [GSAP](gsap.md) | GSAP incluye PixiPlugin para animar propiedades de objetos de PixiJS (posición, escala, filtros, color). | Instala `gsap` y registra `PixiPlugin` con tu instancia de PIXI; después anima con `gsap.to(sprite, {pixi: {...}})`. |
| [mediabunny](mediabunny.md) | Mediabunny puede codificar en el navegador vídeo a partir de un canvas, como el que dibuja PixiJS (combinación por arquitectura). | Renderiza la escena con PixiJS; después captura su canvas con la fuente de canvas de Mediabunny. |
| [planck.js](planck-js.md) | Planck.js simula física 2D y PixiJS puede dibujar sus cuerpos (combinación por arquitectura). | Calcula la física con Planck.js; después sincroniza las posiciones de los sprites en cada fotograma. |

**Notas:** Para 3D en la web, three.js, Babylon.js o PlayCanvas.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada v8.23.0 (2026-11-11) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pixijs/pixijs/blob/dev/README.md) · [2](https://gsap.com/docs/v3/Plugins/PixiPlugin/) · [3](https://mediabunny.dev/guide/media-sources)</sub>

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
npm create pixi.js@latest
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/pixijs/pixijs/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PixiJS para mi objetivo y necesito pasos guiados. Lee https://github.com/pixijs/pixijs/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un proyecto con `npm create pixi.js@latest`, añade un sprite y anímalo en el ticker..

**Qué comprobar:** El sprite se mueve en el canvas del navegador a alta tasa de fotogramas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- crear un juego 2D o una experiencia interactiva para navegador
- dibujar miles de elementos animados en una visualización web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: crear un juego 2D o una experiencia interactiva para navegador; dibujar miles de elementos animados en una visualización web | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `javascript` `2d` `webgl` `animation`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [pixijs/pixijs](https://github.com/pixijs/pixijs)
- 🌐 Web: <http://pixijs.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pixijs/pixijs/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
