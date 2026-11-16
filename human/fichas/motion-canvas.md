[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Motores de video y escenas por código

# 📚 Motion Canvas

> Biblioteca TypeScript para crear animaciones y vídeos explicativos con código, con editor en tiempo real que sincroniza animaciones con una pista de voz.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 20k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (MIT) orientada a vídeos explicativos. Popular; el desarrollo se ha ralentizado (última versión publicada v3.17.2, diciembre de 2024; último push en julio de 2026).

## ¿Qué hace?

Permite programar animaciones vectoriales (formas, texto, código, imágenes) con TypeScript y previsualizarlas en un editor web, con línea de tiempo, sincronización con audio y renderizado a secuencias de imágenes o vídeo.

## ¿Cómo lo hace?

Las escenas se escriben como funciones generadoras en TypeScript; el editor corre sobre Vite en el navegador. El paquete `@motion-canvas/ffmpeg` exporta directamente a vídeo con FFmpeg.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | El exportador `@motion-canvas/ffmpeg` renderiza el proyecto directamente a vídeo con FFmpeg. | Instala `@motion-canvas/ffmpeg` y añádelo al proyecto; después elige el exportador de vídeo. |
| [Kokoro](kokoro.md) | Una narración generada con Kokoro puede usarse como pista de audio para sincronizar las animaciones (combinación por arquitectura). | Genera la narración con Kokoro; después cárgala como audio del proyecto de Motion Canvas. |
| [Claude Code](claude-code.md) | Las escenas son código TypeScript que un agente de código puede escribir y modificar (combinación por arquitectura). | Crea el proyecto con `npm init @motion-canvas@latest`; después pide al agente las escenas. |

**Notas:** Alternativa de Revideo (fork orientado a renderizado programático) y Remotion (React).

Estado en GitHub: activo · último push 2026-07-02 · última versión publicada v3.17.2 (2024-12-14) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/motion-canvas/motion-canvas/blob/main/README.md) · [2](https://motion-canvas.io/docs/quickstart) · [3](https://github.com/motion-canvas/motion-canvas/tree/main/packages/ffmpeg)</sub>

## Ver similares

Grupo **Video y escenas por código**: Motion Canvas ocupa la posición 3 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [HyperFrames](hyperframes.md) ⭐ recomendado | 73 | Si quieres que un agente componga video desde HTML con HeyGen HyperFrames. |
| 2 | [remotion](remotion.md) | 68 | Si sabes React y quieres generar videos programáticos con calidad de producción (revisa su licencia). |
| 3 | **Motion Canvas** (esta ficha) | 56 | Si haces animaciones explicativas en TypeScript con editor en tiempo real. |
| 4 | [MoviePy](moviepy.md) | 54 | Si editas video desde Python (cortes, composición, texto) sin interfaz. |
| 5 | [Revideo](revideo.md) | 51 | Si quieres renderizar videos desde código TypeScript como API o servicio. |

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/motion-canvas/motion-canvas/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Motion Canvas para mi objetivo y necesito pasos guiados. Lee https://github.com/motion-canvas/motion-canvas/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta `npm init @motion-canvas@latest`, entra en la carpeta, ejecuta `npm install` y `npm start`, y abre el editor..

**Qué comprobar:** Ves la escena de ejemplo y puedes editar el código con recarga en vivo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- hacer vídeos explicativos de programación o matemáticas con animaciones precisas
- sincronizar animaciones con una narración grabada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: hacer vídeos explicativos de programación o matemáticas con animaciones precisas; sincronizar animaciones con una narración grabada | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. La última versión publicada (v3.17.2) es de diciembre de 2024 y el último push de julio de 2026: mantenimiento lento.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `animation` `typescript` `video` `code`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Revideo](revideo.md) | 4.2k | Motor TypeScript para crear vídeos con código y renderizarlos sin interfaz desde una API, con reproductor React para previsualizar escenas en el navegador. |
| [remotion](remotion.md) | 73.2k | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. |

## Enlaces

- 🐙 GitHub: [motion-canvas/motion-canvas](https://github.com/motion-canvas/motion-canvas)
- 🌐 Web: <https://motion-canvas.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/motion-canvas/motion-canvas/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
