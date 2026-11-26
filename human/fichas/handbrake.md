[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🖥️ HandBrake

> Transcodificador de vídeo libre para Linux, macOS y Windows con interfaz gráfica, CLI, presets por dispositivo y colas de trabajo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25k | GPL-2.0 | C | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — app de escritorio con instalador para Windows, macOS y Linux · corregido a mano

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Transcodificador de vídeo de código abierto (GPL-2.0 en la mayoría de archivos) mantenido por el HandBrake Team desde 2003. Muy maduro.

## ¿Qué hace?

Convierte vídeos de casi cualquier formato (cámaras, móviles, grabaciones de pantalla, DVD y Blu-ray sin protección) a formatos modernos para móviles, TV, consolas o navegador, con presets, recorte, escalado, filtros, subtítulos, capítulos y colas por lotes.

## ¿Cómo lo hace?

Escrito en C con interfaces nativas para cada sistema y HandBrakeCLI; usa bibliotecas como FFmpeg (libav), x264, x265 y SVT-AV1. Se descarga desde handbrake.fr o se compila desde el código según su documentación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | HandBrake se apoya en las bibliotecas de FFmpeg (libav) para decodificar y en códecs comunes; FFmpeg queda para operaciones que HandBrake no expone. | Usa HandBrake para conversiones con presets; recurre a FFmpeg para tareas por script. |
| [OBS Studio](obs-studio.md) | Las grabaciones de OBS Studio en MKV se convierten con HandBrake a MP4 de menor tamaño para publicarlas (combinación por arquitectura). | Graba con OBS; después transcodifica con un preset de HandBrake. |
| [LosslessCut](lossless-cut.md) | LosslessCut recorta sin recodificar y HandBrake recodifica solo el resultado final (combinación por arquitectura). | Recorta primero con LosslessCut; después convierte con HandBrake. |
| [Jellyfin](jellyfin.md) | Combinación recíproca: Jellyfin lo enlaza como «Convertir la videoteca a formatos compatibles con HandBrake reduce la transcodificación en tiempo real de Jellyfin (combinación por arquitectura)». | Orden indicado desde Jellyfin: Convierte con HandBrake; después añade los archivos a la biblioteca. |

**Notas:** No elimina protecciones anticopia; respeta los derechos del material que conviertes.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.11.2 (2026-06-07) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/HandBrake/HandBrake/blob/master/README.markdown) · [2](https://handbrake.fr/docs) · [3](https://github.com/HandBrake/HandBrake/blob/master/LICENSE)</sub>

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/HandBrake/HandBrake/blob/master/README.markdown)

[Abrir la web o descarga indicada por el autor](https://handbrake.fr)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar HandBrake para mi objetivo y necesito pasos guiados. Lee https://github.com/HandBrake/HandBrake/blob/master/README.markdown. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala HandBrake, abre un vídeo corto y conviértelo con un preset de 1080p..

**Qué comprobar:** Obtienes un MP4 reproducible en el móvil con menor tamaño que el original..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- convertir grabaciones de cámara o pantalla a MP4 compatibles con móviles y webs
- reducir el tamaño de una videoteca manteniendo la calidad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: convertir grabaciones de cámara o pantalla a MP4 compatibles con móviles y webs; reducir el tamaño de una videoteca manteniendo la calidad | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `video` `c` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [HandBrake/HandBrake](https://github.com/HandBrake/HandBrake)
- 🌐 Web: <https://handbrake.fr>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/HandBrake/HandBrake/blob/master/README.markdown)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
