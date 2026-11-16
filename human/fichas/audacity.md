[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Procesamiento y limpieza de audio

# 🖥️ Audacity

> Editor y grabador de audio multipista libre para Windows, macOS y Linux, con efectos, análisis y plugins, incluidos plugins de IA locales de Intel.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.1k | GPL-3.0 (mayoría de archivos GPL-2.0-or-later) | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Editor de audio libre (GPLv3; la mayoría de archivos GPLv2 o posterior) mantenido por el equipo de Audacity con apoyo de Muse Group. Referencia histórica en edición de audio libre. El repositorio está en una reestructuración profunda hacia Audacity 4 (nueva interfaz).

## ¿Qué hace?

Graba y edita audio multipista: cortar, mezclar, efectos (ecualización, compresión, reducción de ruido), análisis espectral, etiquetas, procesado por lotes con macros y soporte de plugins VST3, LV2, Audio Units y Nyquist. Importa y exporta WAV, MP3, FLAC, OGG y, con FFmpeg, muchos más formatos.

## ¿Cómo lo hace?

Aplicación C++ multiplataforma. Se instala desde los binarios oficiales; la biblioteca FFmpeg se instala aparte para formatos adicionales. Los plugins OpenVINO de Intel (proyecto aparte, GPL-3.0) añaden funciones de IA locales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Audacity usa la biblioteca FFmpeg para importar y exportar formatos adicionales (AAC, M4A, WMA, audio de vídeos). | Instala la biblioteca FFmpeg compatible; después Audacity la detecta en Preferencias > Bibliotecas. |
| [Demucs](demucs.md) | Los plugins OpenVINO de Intel para Audacity incluyen separación musical con Demucs v4. | Instala los plugins OpenVINO para Audacity; después usa el efecto Music Separation. |
| [whisper.cpp](whisper-cpp.md) | Los plugins OpenVINO de Intel para Audacity transcriben voz a una pista de etiquetas con whisper.cpp. | Instala los plugins OpenVINO; después usa el analizador Whisper Transcription. |
| [AudioCraft](audiocraft.md) | Los plugins OpenVINO de Intel para Audacity generan y continúan música con MusicGen de AudioCraft. | Instala los plugins OpenVINO y los modelos MusicGen; después usa Music Generation. |
| [YuE2](yue.md) | Combinación recíproca: YuE2 lo enlaza como «Las canciones generadas por YuE2 se pueden recortar, mezclar y masterizar en Audacity (combinación por arquitectura)». | Orden indicado desde YuE2: Genera el audio con YuE2; después ábrelo en Audacity para editarlo. |

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada Audacity-4.0.2 (2026-11-02) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/audacity/audacity/blob/master/README.md) · [2](https://github.com/intel/openvino-plugins-ai-audacity/blob/main/README.md)</sub>

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

[Instrucciones originales de instalación](https://github.com/audacity/audacity/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Audacity para mi objetivo y necesito pasos guiados. Lee https://github.com/audacity/audacity/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga Audacity desde su web, graba o importa un audio y aplica reducción de ruido y normalización..

**Qué comprobar:** Exportas un MP3 o WAV más limpio..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- limpiar, cortar y normalizar una grabación de voz o podcast
- editar stems separados con IA antes de mezclarlos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: limpiar, cortar y normalizar una grabación de voz o podcast; editar stems separados con IA antes de mezclarlos | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. La rama master está en plena reestructuración hacia Audacity 4 y no es estable para compilar; usa las versiones publicadas.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt
- **Etiquetas:** `audio` `editor` `cpp` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [audacity/audacity](https://github.com/audacity/audacity)
- 🌐 Web: <https://www.audacityteam.org/manual/getting-started/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/audacity/audacity/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
