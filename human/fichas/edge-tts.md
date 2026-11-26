[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🎬 edge-tts

> Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.5k | LGPL-3.0 (un archivo MIT) | Python | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** LGPL-3.0 (un archivo MIT). Solo src/edge_tts/srt_composer.py es MIT. Fuente: [LICENSE](https://github.com/rany2/edge-tts/blob/master/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

edge-tts, módulo Python y CLI no oficial para usar el servicio TTS en línea de Microsoft Edge, de @rany2. Licencia LGPL-3.0, salvo un archivo bajo MIT (GitHub muestra NOASSERTION). Es maduro (~13k estrellas, 7.3.1).

## ¿Qué hace?

Sintetiza voz con las voces neuronales de Edge en muchos idiomas y genera subtítulos. Ya no admite SSML personalizado porque Microsoft lo bloquea.

## ¿Cómo lo hace?

Se instala con `pip install edge-tts` y se usa con `edge-tts` o `edge-playback` (este último requiere mpv salvo en Windows). Depende de un servicio de Microsoft que puede cambiar o cortarse.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [MoviePy](moviepy.md) | Narración rápida para vídeos. | Genera el MP3 y móntalo. |
| [whisper](whisper.md) | Comparar o subtitular. (combinación por arquitectura) | Combina según el caso. |
| [FFmpeg](ffmpeg.md) | Convertir el audio. (combinación por arquitectura) | Convierte el formato. |
| [short-video-factory](short-video-factory.md) | Combinación recíproca: short-video-factory lo enlaza como «Síntesis de voz con Edge TTS». | Orden indicado desde short-video-factory: Viene integrada en la app. |

**Notas:** Alternativas (elige una): kokoro. Servicio no oficial: riesgo de términos de uso y disponibilidad.

Estado en GitHub: activo · último push 2026-10-14 · última versión publicada 7.3.1 (2026-10-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/rany2/edge-tts/blob/master/README.md)</sub>

## Ver similares

Grupo **TTS ligero y rápido**: edge-tts ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **edge-tts** (esta ficha) ⭐ recomendado | 60 | Si buscas esto: biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. |
| 2 | [LuxTTS](luxtts.md) | 52 | Si buscas esto: modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. |
| 3 | [Kokoro](kokoro.md) | 48 | Si buscas esto: modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el servicio online de Microsoft Edge sin pedir una clave propia en el ejemplo; no se confirma garantía de coste, cuota o SLA |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. No es inferencia local aunque el script se ejecute en tu PC; la biblioteca es independiente y el servicio puede cambiar sus condiciones o interfaz |
| Coste | Coste por confirmar. Usa el servicio online de Microsoft Edge sin pedir una clave propia en el ejemplo; no se confirma garantía de coste, cuota o SLA |
| Equipo | Preparación según la ruta elegida. Python y pipx; internet; texto no sensible |

No es inferencia local aunque el script se ejecute en tu PC; la biblioteca es independiente y el servicio puede cambiar sus condiciones o interfaz

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y pipx
- internet
- texto no sensible

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (shell):**

```
pipx install edge-tts
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/rany2/edge-tts/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar edge-tts para mi objetivo y necesito pasos guiados. Lee https://github.com/rany2/edge-tts/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera un audio y subtítulos de una frase y escucha pronunciación y pausas.

**Qué comprobar:** Puedes localizar MP3 y SRT y comprobar su contenido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una voz de prueba online
- Explorar voces disponibles

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una voz de prueba online; Explorar voces disponibles | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No es inferencia local aunque el script se ejecute en tu PC; la biblioteca es independiente y el servicio puede cambiar sus condiciones o interfaz

## Stack y modelos

- **Stack:** Python y pipx; internet; texto no sensible
- **Etiquetas:** `tts` `speech-synthesis` `text-to-speech` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kokoro](kokoro.md) | 10.1k | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |

## Enlaces

- 🐙 GitHub: [rany2/edge-tts](https://github.com/rany2/edge-tts)
- 🌐 Web: <https://pypi.org/project/edge-tts/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/rany2/edge-tts/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
