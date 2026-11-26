[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🧩 F5-TTS

> Síntesis de voz con clonación a partir de pocos segundos de audio de referencia, basada en flow matching con Diffusion Transformer; incluye app Gradio y CLI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.6k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; necesita GPU

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de investigación de código abierto (código MIT) del equipo SWivid, publicado con su artículo en arXiv. Los pesos preentrenados son CC-BY-NC. Activo (modelo base v1 en marzo de 2025).

## ¿Qué hace?

Genera voz a partir de texto imitando la voz de un audio de referencia de pocos segundos (clonación zero-shot). Incluye app web Gradio (con chat por voz y varios hablantes), CLI, servidor socket, entrenamiento y ajuste fino.

## ¿Cómo lo hace?

Usa flow matching con un Diffusion Transformer y ConvNeXt V2, muestreo Sway en inferencia y el vocoder Vocos. Se instala con pip después de PyTorch (CUDA, ROCm, XPU o Apple Silicon); también hay imagen Docker. Requiere FFmpeg.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | F5-TTS necesita PyTorch y torchaudio instalados para el dispositivo (CUDA, ROCm, XPU o CPU). | Instala PyTorch para tu GPU; después `pip install f5-tts`. |
| [FFmpeg](ffmpeg.md) | El README pide instalar FFmpeg para procesar el audio. | Instala FFmpeg (p. ej. `conda install ffmpeg`); después F5-TTS. |
| [Gradio](gradio.md) | F5-TTS incluye una aplicación web Gradio (`f5-tts_infer-gradio`) para generar voz sin programar. | Instala F5-TTS (incluye Gradio); después ejecuta `f5-tts_infer-gradio`. |

**Notas:** Alternativa de Fish Speech y CosyVoice para clonación de voz; revisa siempre la licencia de los pesos antes de usos comerciales.

Estado en GitHub: activo · último push 2026-11-03 · última versión publicada 1.1.22 (2026-07-23) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/SWivid/F5-TTS/blob/main/README.md) · [2](https://arxiv.org/abs/2410.06885)</sub>

## Ver similares

Grupo **Clonación de voz y TTS multilingüe**: F5-TTS ocupa la posición 2 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [GPT-SoVITS](gpt-sovits.md) ⭐ recomendado | 69 | Si quieres entrenar una voz propia con pocos minutos de audio y una interfaz web. |
| 2 | **F5-TTS** (esta ficha) | 64 | Si quieres clonación de voz zero-shot con pocos segundos de audio. |
| 3 | [CosyVoice](cosyvoice.md) | 61 | Si necesitas clonación de voz multilingüe de calidad, con soporte fuerte de chino. |
| 4 | [Fish Speech](fish-speech.md) | 61 | Si buscas TTS multilingüe con clonación y buena latencia. |
| 5 | [IndexTTS](index-tts.md) | 53 | Si necesitas controlar duración y emoción de la voz sintetizada. |

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

**Entrada documentada (consulta la sintaxis original):**

```
pip install f5-tts
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/SWivid/F5-TTS/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar F5-TTS para mi objetivo y necesito pasos guiados. Lee https://github.com/SWivid/F5-TTS/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala PyTorch y `pip install f5-tts`; ejecuta `f5-tts_infer-gradio` y genera audio con una referencia de tu voz..

**Qué comprobar:** Obtienes un audio con el texto leído imitando la voz de referencia..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- generar narración con tu propia voz a partir de una muestra corta
- prototipar voces para un proyecto de investigación sin uso comercial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: generar narración con tu propia voz a partir de una muestra corta; prototipar voces para un proyecto de investigación sin uso comercial | no tienes el hardware o no aceptas la licencia de los pesos |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Los pesos preentrenados son CC-BY-NC (solo uso no comercial) por el dataset Emilia; clonar voces ajenas sin consentimiento puede violar derechos de imagen y voz.

## Stack y modelos

- **Stack:** Python, Dockerfile, pyproject.toml
- **Etiquetas:** `tts` `voice-cloning` `pytorch` `speech`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Fish Speech](fish-speech.md) | 33.7k | Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante. |
| [CosyVoice](cosyvoice.md) | 24.4k | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. |

## Enlaces

- 🐙 GitHub: [SWivid/F5-TTS](https://github.com/SWivid/F5-TTS)
- 🌐 Web: <https://arxiv.org/abs/2410.06885>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SWivid/F5-TTS/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
