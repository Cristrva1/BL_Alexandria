[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ OBS Studio

> App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 79.6k | GPL-2.0 | C | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

OBS Studio, software libre para grabar y transmitir vídeo en directo. Licencia GPL-2.0 o posterior. Es muy maduro (~80k estrellas, 33.0.1).

## ¿Qué hace?

Captura, compone, codifica, graba y transmite vídeo con escenas, fuentes, mezclador de audio, filtros y transiciones. Admite plugins, scripting y control remoto por WebSocket. Funciona en Windows, macOS y Linux.

## ¿Cómo lo hace?

Se instala con los instaladores oficiales o paquetes de la distribución. Está escrito en C/C++ con Qt y aprovecha codificadores por hardware (NVENC, AMF, QuickSync, Apple VT).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LosslessCut](lossless-cut.md) | Recortar grabaciones sin recodificar. (combinación por arquitectura) | Graba con OBS y recorta con LosslessCut. |
| [OpenCut](opencut.md) | Editar las grabaciones. (combinación por arquitectura) | Importa las grabaciones en el editor. |
| [faster-whisper](faster-whisper.md) | Subtitular las grabaciones. (combinación por arquitectura) | Transcribe el audio exportado. |
| [rnnoise](rnnoise.md) | Combinación recíproca: rnnoise lo enlaza como «Supresión de ruido en streaming». | Orden indicado desde rnnoise: Usa el filtro de supresión de ruido RNNoise de OBS. |
| [Deep-Live-Cam](deep-live-cam.md) | Combinación recíproca: Deep-Live-Cam lo enlaza como «Emitir la cámara virtual. (combinación por arquitectura)». | Orden indicado desde Deep-Live-Cam: Captura la salida en OBS. |
| [RVC WebUI](rvc.md) | Combinación recíproca: RVC WebUI lo enlaza como «Cambiador de voz en tiempo real para streaming. (combinación por arquitectura)». | Orden indicado desde RVC WebUI: Enruta el audio a OBS. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada 33.0.1 (2026-10-29) · licencia declarada GPL-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/obsproject/obs-studio/blob/master/README.rst) · [2](https://obsproject.com)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa un modelo ni necesita API de IA; streaming, almacenamiento y equipos son costes externos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Prueba el archivo antes de una sesión larga; seleccionar una fuente no acredita que capture el audio deseado |
| Coste | Sin pago a un modelo en la ruta básica. No usa un modelo ni necesita API de IA; streaming, almacenamiento y equipos son costes externos |
| Equipo | Preparación según la ruta elegida. Instalador oficial; permisos de captura; micrófono opcional; disco |

Prueba el archivo antes de una sesión larga; seleccionar una fuente no acredita que capture el audio deseado

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador oficial
- permisos de captura
- micrófono opcional
- disco

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://obsproject.com/download)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OBS Studio para mi objetivo y necesito pasos guiados. Lee https://obsproject.com/download. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una escena con pantalla y micrófono y graba veinte segundos.

**Qué comprobar:** El archivo tiene imagen, audio y niveles aceptables.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Grabar una explicación de pantalla
- Preparar escenas para una transmisión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Grabar una explicación de pantalla; Preparar escenas para una transmisión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Prueba el archivo antes de una sesión larga; seleccionar una fuente no acredita que capture el audio deseado

## Stack y modelos

- **Stack:** Instalador oficial; permisos de captura; micrófono opcional; disco
- **Etiquetas:** `video` `audio` `ui` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [obsproject/obs-studio](https://github.com/obsproject/obs-studio)
- 🌐 Web: <https://obsproject.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/obsproject/obs-studio/blob/master/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
