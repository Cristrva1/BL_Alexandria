[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ LosslessCut

> App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 46k | GPL-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

LosslessCut, app de escritorio para editar vídeo y audio sin pérdida mediante FFmpeg, de @mifi. Licencia GPL-2.0. Es madura (~46k estrellas, v3.70.2) y la mantiene una sola persona.

## ¿Qué hace?

Recorta, corta, une y remuxa vídeo, audio y subtítulos sin recodificar, muy rápido y sin pérdida de calidad. También extrae pistas, cambia metadatos, hace capturas y detecta escenas o silencios. Es útil para hacer un primer corte de material grande de cámara, GoPro o dron.

## ¿Cómo lo hace?

Es una app Electron que usa FFmpeg, para Windows, macOS y Linux. Las descargas oficiales son las de GitHub y las tiendas de Mac y Microsoft (de pago en las tiendas); el README advierte de copias en otras webs.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Es una interfaz gráfica de FFmpeg. | Viene incluido en la app. |
| [yt-dlp](yt-dlp.md) | Recortar vídeos descargados. (combinación por arquitectura) | Descarga con yt-dlp y abre el archivo en LosslessCut. |
| [whisperX](whisperx.md) | Subtitular los fragmentos recortados. (combinación por arquitectura) | Exporta el audio y transcríbelo. |
| [MoviePy](moviepy.md) | Automatizar en Python lo que se hace a mano en la app. (combinación por arquitectura) | Usa MoviePy para lotes repetitivos. |
| [OBS Studio](obs-studio.md) | Combinación recíproca: OBS Studio lo enlaza como «Recortar grabaciones sin recodificar. (combinación por arquitectura)». | Orden indicado desde OBS Studio: Graba con OBS y recorta con LosslessCut. |
| [OpenCut](opencut.md) | Combinación recíproca: OpenCut lo enlaza como «Recortes sin recodificar antes de editar. (combinación por arquitectura)». | Orden indicado desde OpenCut: Corta el material bruto con LosslessCut y edita en OpenCut. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[HandBrake](handbrake.md) · [WanGP](wan2gp.md)

**Notas:** Sin alternativas declaradas. Descarga solo desde las fuentes oficiales.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v3.70.2 (2026-10-28) · licencia declarada GPL-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mifi/lossless-cut/blob/master/README.md) · [2](https://losslesscut.app/docs/faq)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Los ejecutables manuales se ofrecen gratis; tiendas pueden cobrar para apoyar el proyecto; no usa modelo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Los cortes sin recodificar dependen de fotogramas clave y del contenedor; no prometas precisión idéntica a un render completo |
| Coste | El coste depende del proveedor o la ruta. Los ejecutables manuales se ofrecen gratis; tiendas pueden cobrar para apoyar el proyecto; no usa modelo |
| Equipo | Preparación según la ruta elegida. Distribución para tu sistema; archivo compatible; espacio de salida |

Los cortes sin recodificar dependen de fotogramas clave y del contenedor; no prometas precisión idéntica a un render completo

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Distribución para tu sistema
- archivo compatible
- espacio de salida

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://losslesscut.app/docs/getting-started)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LosslessCut para mi objetivo y necesito pasos guiados. Lee https://losslesscut.app/docs/getting-started. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Marca dos puntos de un video propio y exporta el segmento sin recodificar.

**Qué comprobar:** Compruebas duración, comienzo, final y pistas del clip.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Quitar una parte de una grabación
- Separar o unir medios compatibles

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Quitar una parte de una grabación; Separar o unir medios compatibles | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los cortes sin recodificar dependen de fotogramas clave y del contenedor; no prometas precisión idéntica a un render completo

## Stack y modelos

- **Stack:** Distribución para tu sistema; archivo compatible; espacio de salida
- **Etiquetas:** `video` `audio` `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [mifi/lossless-cut](https://github.com/mifi/lossless-cut)
- 🌐 Web: <https://losslesscut.app/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mifi/lossless-cut/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
