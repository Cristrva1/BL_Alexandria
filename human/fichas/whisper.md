[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Transcripción (voz a texto)

# 📝 whisper

> Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 113k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Whisper, modelo de reconocimiento de voz de propósito general de OpenAI, entrenado con datos débilmente supervisados. Licencia MIT para código y pesos. Tiene ~113k estrellas y su release es v20250625; el repo recibe pocos cambios.

## ¿Qué hace?

Transcribe en decenas de idiomas, traduce al inglés y detecta el idioma, con modelos de tiny a large y turbo.

## ¿Cómo lo hace?

Se instala con `pip install -U openai-whisper` y requiere FFmpeg en el sistema. Usa PyTorch; el código se probó con Python 3.8–3.11.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Requisito para leer audio. | Instala FFmpeg con el gestor de paquetes. |
| [whisperX](whisperx.md) | Añadir marcas de tiempo por palabra y diarización. | Usa WhisperX con modelos Whisper. |
| [PyTorch](pytorch.md) | Backend. | Instala PyTorch con CUDA si hay GPU. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (9). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Arcads AI Video Skill Pack](arcads-claude-code.md) · [DaVinci Resolve MCP](davinci-resolve-mcp.md) · [edge-tts](edge-tts.md) · [instaloader](instaloader.md) · [Kdenlive](kdenlive.md) · [sherpa-onnx](sherpa-onnx.md) · [TEN Framework](ten-framework.md) · [transformers.js](transformers-js.md) · [videofy_minimal](videofy-minimal.md)

**Notas:** Alternativas (elige una): whisper-cpp. Para producción suelen preferirse faster-whisper o whisper.cpp por velocidad.

Estado en GitHub: activo · último push 2026-08-31 · última versión publicada v20250625 (2025-06-26) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openai/whisper/blob/main/README.md)</sub>

## Ver similares

Grupo **Transcripción con Whisper**: whisper ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [whisper.cpp](whisper-cpp.md) ⭐ recomendado | 73 | Si buscas esto: port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. |
| 2 | [faster-whisper](faster-whisper.md) | 70 | Si buscas esto: runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. |
| 3 | **whisper** (esta ficha) | 67 | Si buscas esto: modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Código y pesos MIT para ejecución propia sin API; cómputo independiente |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No es la API hospedada de OpenAI y no usa créditos de ChatGPT; puede inventar texto en silencios o audio difícil y requiere revisión |
| Coste | Sin pago a un modelo en la ruta básica. Código y pesos MIT para ejecución propia sin API; cómputo independiente |
| Equipo | Preparación según la ruta elegida. Python; PyTorch; FFmpeg; modelo con memoria suficiente; audio autorizado |

No es la API hospedada de OpenAI y no usa créditos de ChatGPT; puede inventar texto en silencios o audio difícil y requiere revisión

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- PyTorch
- FFmpeg
- modelo con memoria suficiente
- audio autorizado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
pip install -U openai-whisper
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/openai/whisper/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whisper para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/whisper/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Transcribe una nota de voz breve y corrige manualmente las palabras dudosas.

**Qué comprobar:** Puedes contrastar texto con audio original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una transcripción local
- Traducir habla al inglés como borrador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una transcripción local; Traducir habla al inglés como borrador | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No es la API hospedada de OpenAI y no usa créditos de ChatGPT; puede inventar texto en silencios o audio difícil y requiere revisión

## Stack y modelos

- **Stack:** Python; PyTorch; FFmpeg; modelo con memoria suficiente; audio autorizado
- **Etiquetas:** `stt` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper.cpp](whisper-cpp.md) | 55.2k | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. |

## Enlaces

- 🐙 GitHub: [openai/whisper](https://github.com/openai/whisper)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openai/whisper/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
