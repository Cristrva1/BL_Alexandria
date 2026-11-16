[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ Kokoro

> Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.1k | Apache-2.0 | JavaScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

kokoro, librería de inferencia para Kokoro-82M, modelo TTS de pesos abiertos de 82 millones de parámetros, de @hexgrad. Licencia Apache-2.0. Tiene ~10k estrellas, pero no cambia desde agosto de 2025.

## ¿Qué hace?

Genera voz de calidad comparable a modelos mayores siendo mucho más rápido y barato, según el autor, con varias voces e idiomas (inglés, japonés, chino y otros).

## ¿Cómo lo hace?

Se instala con `pip install kokoro>=0.9.4 soundfile`. Usa misaki (G2P) y espeak-ng como respaldo para inglés fuera de vocabulario y algunos idiomas; los idiomas extra se instalan con `misaki[ja]` y similares.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Pipecat](pipecat.md) | TTS local en agentes de voz. (combinación por arquitectura) | Expón Kokoro como servicio TTS. |
| [whisper.cpp](whisper-cpp.md) | STT local para un ciclo voz a voz. (combinación por arquitectura) | Combina en el mismo pipeline. |
| [MoviePy](moviepy.md) | Narración de vídeos. (combinación por arquitectura) | Monta el audio generado. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (15). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[dograh](dograh.md) · [huashu-motion](huashu-motion.md) · [HyperFrames](hyperframes.md) · [KoboldCpp](koboldcpp.md) · [LiveKit Agents](livekit-agents.md) · [Manim (ManimGL)](manim.md) · [manim](manim-community.md) · [MoneyPrinterTurbo](moneyprinterturbo.md) · [Motion Canvas](motion-canvas.md) · [OpenMontage](openmontage.md) · [Papermorph](papermorph.md) · [sherpa-onnx](sherpa-onnx.md) · [SillyTavern](sillytavern.md) · [srt-whiteboard-animation](srt-whiteboard-animation.md) · [VoiceStudio](omnivoice-studio.md)

**Notas:** Alternativas (elige una): luxtts, edge-tts. Inactivo desde 2025.

Estado en GitHub: activo · último push 2025-08-06 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/hexgrad/kokoro/blob/main/README.md)</sub>

## Ver similares

Grupo **TTS ligero y rápido**: Kokoro ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [edge-tts](edge-tts.md) ⭐ recomendado | 60 | Si buscas esto: biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. |
| 2 | [LuxTTS](luxtts.md) | 56 | Si buscas esto: modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. |
| 3 | **Kokoro** (esta ficha) | 52 | Si buscas esto: modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Modelo local Apache sin API de pago; equipo y recursos de voz independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los ejemplos con !pip y !apt son de notebook y no se pegan sin cambios en PowerShell; selecciona el idioma y sus dependencias |
| Coste | Sin pago a un modelo en la ruta básica. Modelo local Apache sin API de pago; equipo y recursos de voz independientes |
| Equipo | Preparación según la ruta elegida. Python; Kokoro y soundfile; espeak-ng según idioma; pesos |

Los ejemplos con !pip y !apt son de notebook y no se pegan sin cambios en PowerShell; selecciona el idioma y sus dependencias

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Kokoro y soundfile
- espeak-ng según idioma
- pesos

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/hexgrad/kokoro/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kokoro para mi objetivo y necesito pasos guiados. Lee https://github.com/hexgrad/kokoro/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera dos frases en español y revisa pronunciación y pausas.

**Qué comprobar:** Puedes localizar el archivo de audio y reconocer voz e idioma seleccionados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Narrar una nota propia
- Probar una voz para una demo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Narrar una nota propia; Probar una voz para una demo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los ejemplos con !pip y !apt son de notebook y no se pegan sin cambios en PowerShell; selecciona el idioma y sus dependencias

## Stack y modelos

- **Stack:** Python; Kokoro y soundfile; espeak-ng según idioma; pesos
- **Etiquetas:** `tts` `audio` `local`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LuxTTS](luxtts.md) | 5.6k | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. |
| [edge-tts](edge-tts.md) | 12.5k | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. |

## Enlaces

- 🐙 GitHub: [hexgrad/kokoro](https://github.com/hexgrad/kokoro)
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/hexgrad/kokoro/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
