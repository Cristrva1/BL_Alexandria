[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Transcripción (voz a texto)

# 🧩 sherpa-onnx

> Motor de voz offline con ONNX Runtime: reconocimiento, síntesis, VAD, diarización e identificación de hablante en móvil, embebido, escritorio y servidor.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16k | Apache-2.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## ¿Qué es?

Motor de voz de código abierto (Apache-2.0) del proyecto k2-fsa (Next-gen Kaldi). Muy activo y con muchos proyectos que lo usan en móviles y dispositivos embebidos.

## ¿Qué hace?

Ofrece, sin conexión, reconocimiento de voz en streaming y por archivos, síntesis de voz, separación de fuentes, identificación, verificación y diarización de hablantes, identificación de idioma, etiquetado de audio, detección de actividad de voz (VAD), detección de palabras clave, puntuación y mejora de voz.

## ¿Cómo lo hace?

Usa ONNX Runtime para ejecutar modelos exportados en x86, ARM, RISC-V y NPUs. Tiene APIs en una docena de lenguajes y binarios para Android, iOS, HarmonyOS, Windows, macOS, Linux, WebAssembly y Flutter. Los modelos preentrenados se descargan desde su documentación o releases.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [whisper](whisper.md) | sherpa-onnx ejecuta modelos Whisper exportados a ONNX para reconocimiento e identificación de idioma. | Descarga un modelo Whisper preparado para sherpa-onnx; después úsalo con el reconocedor offline. |
| [NeMo Speech](nemo.md) | sherpa-onnx ejecuta modelos de NeMo como Parakeet TDT y transductores/CTC exportados a ONNX. | Descarga el modelo NeMo convertido; después úsalo con el reconocedor de sherpa-onnx. |
| [Kokoro](kokoro.md) | sherpa-onnx incluye Kokoro-82M entre sus motores de síntesis de voz. | Descarga el modelo Kokoro para sherpa-onnx; después genera audio con la API de TTS. |
| [pyannote.audio](pyannote-audio.md) | La diarización de sherpa-onnx usa el modelo de segmentación de pyannote exportado a ONNX junto a un modelo de embeddings de hablante. | Descarga el modelo de segmentación de pyannote para sherpa-onnx; después ejecuta la diarización. |

**Notas:** Alternativa ligera y multiplataforma a whisper.cpp o faster-whisper cuando necesitas varias tareas de voz en dispositivos.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.0.1 (2026-10-26) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/k2-fsa/sherpa-onnx/blob/master/README.md) · [2](https://k2-fsa.github.io/sherpa/onnx/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/k2-fsa/sherpa-onnx/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar sherpa-onnx para mi objetivo y necesito pasos guiados. Lee https://github.com/k2-fsa/sherpa-onnx/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala el paquete de Python, descarga un modelo de reconocimiento preentrenado de la documentación y transcribe un WAV de prueba..

**Qué comprobar:** Obtienes el texto reconocido sin conexión a internet..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- añadir dictado o transcripción sin conexión a una app Android o iOS
- poner reconocimiento y síntesis de voz en una Raspberry Pi sin nube

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: añadir dictado o transcripción sin conexión a una app Android o iOS; poner reconocimiento y síntesis de voz en una Raspberry Pi sin nube | no quieres preparar modelos, dependencias y hardware propios |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. El código es Apache-2.0; cada modelo preentrenado tiene su propia licencia.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt, pom.xml, setup.py
- **Etiquetas:** `speech` `stt` `tts` `onnx`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx)
- 🌐 Web: <https://k2-fsa.github.io/sherpa/onnx/index.html>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/k2-fsa/sherpa-onnx/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
