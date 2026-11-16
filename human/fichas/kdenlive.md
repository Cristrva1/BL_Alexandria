[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🖥️ Kdenlive

> Editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos, titulación, proxys y subtítulos por reconocimiento de voz.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.1k | GPL-3.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Editor de vídeo de código abierto (GPL-3.0 según GitHub) desarrollado por la comunidad KDE. El repositorio de GitHub es un espejo: el desarrollo canónico vive en invent.kde.org (multimedia/kdenlive). Maduro, con versiones trimestrales.

## ¿Qué hace?

Edición no lineal con múltiples pistas, efectos y transiciones, keyframes, titulación, corrección de color, clips proxy para equipos modestos, edición de audio y generación de subtítulos con reconocimiento de voz.

## ¿Cómo lo hace?

Escrito en C++ con Qt, KDE Frameworks y MLT (que usa FFmpeg). Se instala desde kdenlive.org (Windows, macOS, AppImage, Flatpak) o repositorios de distribución; la voz a texto requiere instalar Whisper o VOSK desde la configuración.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Kdenlive usa FFmpeg a través de MLT para decodificar y renderizar. | Viene con los paquetes oficiales; comprueba la versión en la configuración si fallan códecs. |
| [whisper](whisper.md) | La función de voz a texto de Kdenlive puede usar Whisper para generar subtítulos. | Instala Whisper desde la configuración de voz a texto; después genera los subtítulos. |
| [OBS Studio](obs-studio.md) | Las grabaciones de OBS Studio se montan en Kdenlive (combinación por arquitectura). | Graba con OBS; después importa los clips en Kdenlive. |

**Notas:** Alternativas (elige una): shotcut, opencut. Reporta incidencias y contribuye en invent.kde.org, no en el espejo de GitHub.

Estado en KDE Invent (GitLab): activo · última actividad 2026-11-12 · última versión publicada v26.08.3 (2026-11-03) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

Copia antigua en GitHub: activo · último push 2026-11-16 · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/KDE/kdenlive/blob/master/README.md) · [2](https://docs.kdenlive.org/en/effects_and_filters/speech_to_text.html) · [3](https://invent.kde.org/multimedia/kdenlive)</sub>

## Ver similares

Grupo **Editores de video**: Kdenlive ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenCut](opencut.md) ⭐ recomendado | 62 | Si buscas esto: editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. |
| 2 | [Shotcut](shotcut.md) | 59 | Si buscas esto: editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de tiempo, filtros, amplio soporte de formatos y subtítulos por voz. |
| 3 | **Kdenlive** (esta ficha) | 59 | Si buscas esto: editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos, titulación, proxys y subtítulos por reconocimiento de voz. |

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

[Instrucciones originales de instalación](https://github.com/KDE/kdenlive/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://invent.kde.org/multimedia/kdenlive)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kdenlive para mi objetivo y necesito pasos guiados. Lee https://github.com/KDE/kdenlive/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Kdenlive desde kdenlive.org, crea un proyecto, añade clips a la línea de tiempo y renderiza un MP4..

**Qué comprobar:** El render termina y el archivo reproduce el montaje..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- montar vídeos con varias pistas, efectos y corrección de color
- subtitular automáticamente entrevistas o tutoriales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: montar vídeos con varias pistas, efectos y corrección de color; subtitular automáticamente entrevistas o tutoriales | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt
- **Etiquetas:** `video` `cpp` `app` `edicion`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Shotcut](shotcut.md) | 15.7k | Editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de tiempo, filtros, amplio soporte de formatos y subtítulos por voz. |
| [OpenCut](opencut.md) | 98.4k | Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. |

## Enlaces

- 🐙 GitHub: [KDE/kdenlive](https://github.com/KDE/kdenlive)
- 🌐 Web: <https://invent.kde.org/multimedia/kdenlive>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/KDE/kdenlive/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
