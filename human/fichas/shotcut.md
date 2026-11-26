[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🖥️ Shotcut

> Editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de tiempo, filtros, amplio soporte de formatos y subtítulos por voz.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.7k | GPL-3.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Editor de vídeo de código abierto (GPL-3.0) cuyo autor principal es Dan Dennedy, también mantenedor de MLT. Maduro, con versiones regulares para Windows, macOS y Linux.

## ¿Qué hace?

Ofrece edición en línea de tiempo con múltiples pistas, filtros de vídeo y audio, transiciones, fotogramas clave, corrección de color, soporte nativo de muchos formatos sin importación, captura y exportación con presets, y generación de subtítulos por reconocimiento de voz.

## ¿Cómo lo hace?

Escrito en C++ con Qt y QML sobre MLT, con FFmpeg, frei0r y otras bibliotecas como dependencias. Se descarga como binario desde shotcut.org; la función de voz a texto descarga modelos Whisper.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Shotcut depende de las bibliotecas de FFmpeg (a través de MLT) para leer y codificar formatos. | Viene incluido en los binarios; usa FFmpeg aparte solo para tareas por script. |
| [whisper.cpp](whisper-cpp.md) | Shotcut incluye una extensión de modelos Whisper para su función de voz a texto y subtítulos. | Descarga el modelo desde Shotcut; después genera subtítulos desde el menú correspondiente. |
| [OBS Studio](obs-studio.md) | Las grabaciones de OBS Studio se editan en Shotcut antes de publicarlas (combinación por arquitectura). | Graba con OBS; después importa los archivos en Shotcut. |

**Notas:** Alternativas (elige una): kdenlive, opencut.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v26.9.27 (2026-09-28) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mltframework/shotcut/blob/master/README.md) · [2](https://github.com/mltframework/shotcut/blob/master/src/qml/extensions/whispermodel.qml) · [3](https://www.shotcut.org/features/)</sub>

## Ver similares

Grupo **Editores de video**: Shotcut ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenCut](opencut.md) ⭐ recomendado | 63 | Si buscas esto: editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. |
| 2 | **Shotcut** (esta ficha) | 60 | Si buscas esto: editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de tiempo, filtros, amplio soporte de formatos y subtítulos por voz. |
| 3 | [Kdenlive](kdenlive.md) | 59 | Si buscas esto: editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos, titulación, proxys y subtítulos por reconocimiento de voz. |

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

[Instrucciones originales de instalación](https://github.com/mltframework/shotcut/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://www.shotcut.org)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Shotcut para mi objetivo y necesito pasos guiados. Lee https://github.com/mltframework/shotcut/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Shotcut desde shotcut.org, importa dos clips, córtalos en la línea de tiempo y exporta un MP4..

**Qué comprobar:** El MP4 exportado reproduce los dos clips con el corte aplicado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- editar vídeos de YouTube o cursos con cortes, transiciones y títulos
- generar subtítulos automáticos a partir del audio de un vídeo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: editar vídeos de YouTube o cursos con cortes, transiciones y títulos; generar subtítulos automáticos a partir del audio de un vídeo | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt
- **Etiquetas:** `video` `cpp` `app` `edicion`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kdenlive](kdenlive.md) | 6.1k | Editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos, titulación, proxys y subtítulos por reconocimiento de voz. |
| [OpenCut](opencut.md) | 98.4k | Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. |

## Enlaces

- 🐙 GitHub: [mltframework/shotcut](https://github.com/mltframework/shotcut)
- 🌐 Web: <https://www.shotcut.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mltframework/shotcut/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
